"""
RAG Engine for EPLAN Documentation

Semantic search over Eplan_DOCS/ using ChromaDB + sentence-transformers.

Embedding model: all-mpnet-base-v2 (768 dims, high quality)
Persistence: local ChromaDB in mcp_server/chroma_db/
"""

import os
import re
import hashlib
import json
import time
import zipfile
import tempfile
import urllib.request
from pathlib import Path
from typing import List, Dict, Optional

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


# =============================================================================
# CONFIGURATION
# =============================================================================

EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"
COLLECTION_NAME = "eplan_docs"
CHUNK_SIZE = 1500       # max characters per chunk
CHUNK_OVERLAP = 200     # overlap between chunks
MAX_RESULTS = 10
BATCH_SIZE = 256        # ChromaDB insert batch size

# Paths (relative to this file)
SCRIPT_DIR = Path(__file__).parent
DOCS_DIR = SCRIPT_DIR.parent / "Eplan_DOCS"
CHROMA_DIR = SCRIPT_DIR / "chroma_db"


# Pre-computed DB URL to skip 3 hours of local indexing!
# TODO: Update this URL once we publish the actual .zip release on GitHub
PRECOMPUTED_DB_URL = "https://github.com/covagashi/Eplan_2026_IA_MCP_scripts/releases/download/v1.0.0/chroma_db_bge.zip"


# =============================================================================
# RAG ENGINE
# =============================================================================

class EplanRAG:
    """
    RAG engine for EPLAN documentation.
    
    - Indexes all .md and .csv files from Eplan_DOCS/
    - Splits large documents into overlapping chunks
    - Stores embeddings in a persistent ChromaDB collection
    - Provides semantic search with category filtering
    - Auto-detects when docs change and needs re-indexing
    """

    def __init__(self, docs_dir: str = None, db_dir: str = None):
        self.docs_dir = Path(docs_dir) if docs_dir else DOCS_DIR
        self.db_dir = Path(db_dir) if db_dir else CHROMA_DIR
        self.db_dir.mkdir(parents=True, exist_ok=True)

        print(f"Loading embedding model '{EMBEDDING_MODEL}'...", flush=True)
        print("(This may take a few minutes if downloading for the first time)", flush=True)
        # BGE requires "Represent this sentence for searching relevant passages: " for queries ONLY.
        # However, Chroma's SentenceTransformerEmbeddingFunction doesn't naturally support diff 
        # prefixes for encode vs query. We'll handle the query prefix in the search() method.
        self._embedding_fn = SentenceTransformerEmbeddingFunction(
            model_name=EMBEDDING_MODEL
        )
        print("Embedding model loaded successfully.", flush=True)

        # Persistent ChromaDB client
        self._client = chromadb.PersistentClient(path=str(self.db_dir))
        self._collection = None

    # -------------------------------------------------------------------------
    # Collection access
    # -------------------------------------------------------------------------

    @property
    def collection(self) -> chromadb.Collection:
        """Get or create the ChromaDB collection."""
        if self._collection is None:
            self._collection = self._client.get_or_create_collection(
                name=COLLECTION_NAME,
                embedding_function=self._embedding_fn,
                metadata={"hnsw:space": "cosine"},
            )
        return self._collection

    # -------------------------------------------------------------------------
    # Change detection
    # -------------------------------------------------------------------------

    def _compute_docs_fingerprint(self) -> str:
        """Hash of all doc file paths + modification times to detect changes."""
        md_files = sorted(self.docs_dir.rglob("*.md"))
        csv_files = sorted(self.docs_dir.rglob("*.csv"))
        hasher = hashlib.md5()
        for f in md_files + csv_files:
            rel = str(f.relative_to(self.docs_dir))
            hasher.update(rel.encode("utf-8"))
            try:
                hasher.update(str(f.stat().st_mtime_ns).encode())
            except OSError:
                pass
        return hasher.hexdigest()

    def _needs_indexing(self) -> bool:
        """Check if documentation needs (re)indexing."""
        if self.collection.count() == 0:
            return True

        meta_file = self.db_dir / "index_meta.json"
        if not meta_file.exists():
            return True

        try:
            with open(meta_file, encoding="utf-8") as f:
                meta = json.load(f)
            return meta.get("fingerprint") != self._compute_docs_fingerprint()
        except Exception:
            return True

    def _try_download_precomputed_db(self) -> bool:
        """Download pre-computed ChromaDB zip if available to save indexing time."""
        if not PRECOMPUTED_DB_URL or PRECOMPUTED_DB_URL.startswith("TODO"):
            return False
            
        print(f"\n[RAG] Missing vector database. Trying to download pre-computed DB to save 3 hours of indexing...", flush=True)
        print(f"[RAG] URL: {PRECOMPUTED_DB_URL}", flush=True)
        
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                zip_path = Path(temp_dir) / "chroma_db.zip"
                
                # Download with basic progress
                req = urllib.request.Request(PRECOMPUTED_DB_URL, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response, open(zip_path, 'wb') as out_file:
                    total_size = int(response.info().get('Content-Length', 0))
                    downloaded = 0
                    block_size = 1024 * 1024 * 5 # 5MB chunks
                    
                    while True:
                        buffer = response.read(block_size)
                        if not buffer:
                            break
                        downloaded += len(buffer)
                        out_file.write(buffer)
                        if total_size > 0:
                            print(f"[RAG] Downloaded {downloaded / (1024*1024):.1f} MB / {total_size / (1024*1024):.1f} MB...", end='\r', flush=True)
                
                print("\n[RAG] Download complete. Extracting...", flush=True)
                
                # Ensure target directory is clean before extraction
                if self.db_dir.exists():
                    import shutil
                    shutil.rmtree(self.db_dir)
                self.db_dir.mkdir(parents=True, exist_ok=True)
                
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    # Extract contents directly into self.db_dir
                    # Assuming the zip contains the *contents* of chroma_db, not the folder itself
                    zip_ref.extractall(self.db_dir)
                    
                print("[RAG] Pre-computed vector database installed successfully!", flush=True)
                
                # Check for nested chroma_db structure and move files up if needed
                nested_dir = self.db_dir / "chroma_db"
                if nested_dir.exists() and nested_dir.is_dir():
                    import shutil
                    for item in nested_dir.iterdir():
                        shutil.move(str(item), str(self.db_dir))
                    nested_dir.rmdir()
                return True
                
        except Exception as e:
            print(f"\n[RAG] Failed to download pre-computed DB: {e}", flush=True)
            print("[RAG] Will fall back to local indexing.", flush=True)
            return False

    def _save_index_meta(self, fingerprint: str, stats: Dict):
        """Persist indexing metadata."""
        meta = {
            "fingerprint": fingerprint,
            "model": EMBEDDING_MODEL,
            "docs_dir": str(self.docs_dir),
            "indexed_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            **stats,
        }
        with open(self.db_dir / "index_meta.json", "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2)

    # -------------------------------------------------------------------------
    # Document parsing
    # -------------------------------------------------------------------------

    def _read_file(self, filepath: Path) -> Optional[Dict]:
        """Read a file and extract metadata from content."""
        try:
            text = filepath.read_text(encoding="utf-8", errors="replace").strip()
        except Exception:
            return None

        if not text:
            return None

        # Extract title from first markdown heading
        title_match = re.search(r"^#\s+(.+)", text, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filepath.stem

        # Extract source URL if present
        url_match = re.search(r"\*\*Source URL:\*\*\s*(\S+)", text)
        source_url = url_match.group(1).strip() if url_match else ""

        # Relative path for metadata
        rel_path = str(filepath.relative_to(self.docs_dir)).replace("\\", "/")

        # Category from directory structure
        parts = rel_path.split("/")
        category = parts[0] if parts else "General"
        subcategory = parts[1] if len(parts) > 2 else ""

        return {
            "text": text,
            "title": title,
            "source_url": source_url,
            "rel_path": rel_path,
            "category": category,
            "subcategory": subcategory,
        }

    # -------------------------------------------------------------------------
    # Chunking
    # -------------------------------------------------------------------------

    def _chunk_text(self, text: str) -> List[str]:
        """
        Split text into overlapping chunks.
        
        Strategy:
        1. If text fits in one chunk, return as-is
        2. Try splitting by markdown headers
        3. Fall back to paragraph splitting
        4. Hard split as last resort
        """
        if len(text) <= CHUNK_SIZE:
            return [text]

        chunks = []

        # Split by markdown headers (##, ###)
        sections = re.split(r"(?=^#{1,3}\s)", text, flags=re.MULTILINE)

        current = ""
        for section in sections:
            # If adding this section still fits, accumulate
            if len(current) + len(section) <= CHUNK_SIZE:
                current += section
            else:
                # Save current chunk
                if current.strip():
                    chunks.append(current.strip())

                # If section itself is too big, split by paragraphs
                if len(section) > CHUNK_SIZE:
                    para_chunks = self._split_by_paragraphs(section)
                    chunks.extend(para_chunks)
                    current = ""
                else:
                    current = section

        if current.strip():
            chunks.append(current.strip())

        return chunks if chunks else [text[:CHUNK_SIZE]]

    def _split_by_paragraphs(self, text: str) -> List[str]:
        """Split text by paragraphs, with overlap for context."""
        paragraphs = text.split("\n\n")
        chunks = []
        current = ""

        for para in paragraphs:
            if len(current) + len(para) + 2 <= CHUNK_SIZE:
                current += para + "\n\n"
            else:
                if current.strip():
                    chunks.append(current.strip())
                # Hard split if single paragraph is too big
                if len(para) > CHUNK_SIZE:
                    for i in range(0, len(para), CHUNK_SIZE - CHUNK_OVERLAP):
                        piece = para[i : i + CHUNK_SIZE].strip()
                        if piece:
                            chunks.append(piece)
                    current = ""
                else:
                    # Keep overlap from previous chunk
                    overlap_text = current[-CHUNK_OVERLAP:] if current else ""
                    current = overlap_text + para + "\n\n"

        if current.strip():
            chunks.append(current.strip())

        return chunks

    # -------------------------------------------------------------------------
    # Indexing
    # -------------------------------------------------------------------------

    def index_docs(self, force: bool = False) -> Dict:
        """
        Index all documentation files.
        
        Args:
            force: Re-index even if docs haven't changed
            
        Returns:
            Dict with indexing stats
        """
        # Try downloading pre-computed DB to skip indexing
        if self.collection.count() == 0:
            if self._try_download_precomputed_db():
                return {
                    "status": "downloaded_precomputed",
                    "total_chunks": self.collection.count(),
                    "message": "Used pre-computed index to save time.",
                }

        fingerprint = self._compute_docs_fingerprint()

        if not force and not self._needs_indexing():
            return {
                "status": "up_to_date",
                "total_chunks": self.collection.count(),
                "message": "Index is current — no changes detected in docs.",
            }

        start_time = time.time()

        # Clear existing collection for clean re-index
        try:
            self._client.delete_collection(COLLECTION_NAME)
        except Exception:
            pass
        self._collection = None  # Reset cached reference

        # Gather all files
        print(f"Scanning directory {self.docs_dir} for markdown and CSV files...", flush=True)
        md_files = sorted(self.docs_dir.rglob("*.md"))
        csv_files = sorted(self.docs_dir.rglob("*.csv"))
        all_files = md_files + csv_files
        
        total_files = len(all_files)
        print(f"Found {total_files} files to index.", flush=True)

        all_ids = []
        all_docs = []
        all_metas = []
        files_ok = 0
        files_skipped = 0
        
        print("Parsing files and chunking text...", flush=True)

        for filepath in all_files:
            doc_info = self._read_file(filepath)
            if not doc_info:
                files_skipped += 1
                continue

            files_ok += 1
            chunks = self._chunk_text(doc_info["text"])

            for i, chunk in enumerate(chunks):
                chunk_id = hashlib.md5(
                    f"{doc_info['rel_path']}::chunk_{i}".encode()
                ).hexdigest()

                all_ids.append(chunk_id)
                all_docs.append(chunk)
                all_metas.append({
                    "title": doc_info["title"],
                    "source": doc_info["rel_path"],
                    "source_url": doc_info["source_url"],
                    "category": doc_info["category"],
                    "subcategory": doc_info["subcategory"],
                    "chunk_index": i,
                    "total_chunks": len(chunks),
                })

            if files_ok % 1000 == 0:
                print(f"  Processed {files_ok}/{total_files} files... ({len(all_ids)} chunks generated)", flush=True)

        print(f"Done parsing. Generated {len(all_ids)} chunks from {files_ok} files.", flush=True)
        print("Inserting into ChromaDB vector store (this will take a while)...", flush=True)

        # Batch insert into ChromaDB
        for i in range(0, len(all_ids), BATCH_SIZE):
            end = min(i + BATCH_SIZE, len(all_ids))
            if (i // BATCH_SIZE) % 10 == 0:
                print(f"  Inserting batch {i // BATCH_SIZE + 1} ... (chunks {i} to {end})", flush=True)
            self.collection.add(
                ids=all_ids[i:end],
                documents=all_docs[i:end],
                metadatas=all_metas[i:end],
            )
        
        print("Indexing complete!", flush=True)

        elapsed = round(time.time() - start_time, 1)

        stats = {
            "files_processed": files_ok,
            "files_skipped": files_skipped,
            "total_chunks": len(all_ids),
        }
        self._save_index_meta(fingerprint, stats)

        return {
            "status": "indexed",
            "elapsed_seconds": elapsed,
            "model": EMBEDDING_MODEL,
            **stats,
        }

    # -------------------------------------------------------------------------
    # Search
    # -------------------------------------------------------------------------

    def search(
        self,
        query: str,
        n_results: int = MAX_RESULTS,
        category: str = None,
    ) -> List[Dict]:
        """
        Semantic search over indexed documentation.
        
        Args:
            query: Natural language search query
            n_results: Number of results (max 20)
            category: Filter by category (e.g. "API Reference", "User Guide")
            
        Returns:
            List of result dicts with content, metadata, and relevance score
        """
        # Auto-index on first search if needed
        if self.collection.count() == 0:
            idx = self.index_docs()
            if self.collection.count() == 0:
                return [{
                    "error": "No documents indexed. Check that Eplan_DOCS/ exists.",
                    "index_result": idx,
                }]

        # Build filter
        where_filter = None
        if category:
            where_filter = {"category": category}

        # BGE model explicitly requires this prefix for queries to get optimal semantic matching
        bge_query = f"Represent this sentence for searching relevant passages: {query}"
        
        results = self.collection.query(
            query_texts=[bge_query],
            n_results=min(n_results, 20),
            where=where_filter,
            include=["documents", "metadatas", "distances"],
        )

        output = []
        if results and results["ids"] and results["ids"][0]:
            for i, doc_id in enumerate(results["ids"][0]):
                meta = results["metadatas"][0][i]
                distance = results["distances"][0][i]

                output.append({
                    "title": meta.get("title", ""),
                    "source": meta.get("source", ""),
                    "source_url": meta.get("source_url", ""),
                    "category": meta.get("category", ""),
                    "chunk": f"{meta.get('chunk_index', 0)+1}/{meta.get('total_chunks', 1)}",
                    "relevance": round(1 - distance, 4),
                    "content": results["documents"][0][i],
                })

        return output

    # -------------------------------------------------------------------------
    # Stats
    # -------------------------------------------------------------------------

    def get_stats(self) -> Dict:
        """Get current index statistics."""
        count = self.collection.count()

        meta = {}
        meta_file = self.db_dir / "index_meta.json"
        if meta_file.exists():
            try:
                with open(meta_file, encoding="utf-8") as f:
                    meta = json.load(f)
            except Exception:
                pass

        return {
            "indexed_chunks": count,
            "model": meta.get("model", EMBEDDING_MODEL),
            "docs_dir": str(self.docs_dir),
            "indexed_at": meta.get("indexed_at", "never"),
            "files_processed": meta.get("files_processed", 0),
            "needs_reindex": self._needs_indexing() if count > 0 else True,
        }


# =============================================================================
# SINGLETON
# =============================================================================

_instance: Optional[EplanRAG] = None


def get_rag(docs_dir: str = None) -> EplanRAG:
    """Get or create the singleton RAG engine."""
    global _instance
    if _instance is None:
        _instance = EplanRAG(docs_dir=docs_dir)
    return _instance
