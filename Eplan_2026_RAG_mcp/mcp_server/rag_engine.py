"""
RAG Engine for EPLAN Documentation - SOTA LlamaIndex 2026 Architecture

Semantic search over Eplan_DOCS/ using ChromaDB + LlamaIndex.

Features:
- MarkdownNodeParser for structural awareness of headers.
- Hybrid Search (Dense Vectors + BM25 Lexical).
- LlamaIndex semantic sentence boundary chunking.
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
import warnings

warnings.filterwarnings("ignore")
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from llama_index.core import Document, VectorStoreIndex, StorageContext, Settings, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import MarkdownNodeParser, SentenceSplitter
from llama_index.retrievers.bm25 import BM25Retriever
from llama_index.core.retrievers import QueryFusionRetriever
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore

# =============================================================================
# CONFIGURATION
# =============================================================================

EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"
COLLECTION_NAME = "eplan_docs"
CHUNK_SIZE = 512
CHUNK_OVERLAP = 64
MAX_RESULTS = 10

# Paths
SCRIPT_DIR = Path(__file__).parent
DOCS_DIR = SCRIPT_DIR.parent / "Eplan_DOCS"
CHROMA_DIR = SCRIPT_DIR / "chroma_db_sota"

PRECOMPUTED_DB_URL = "https://github.com/covagashi/Eplan_2026_IA_MCP_scripts/releases/download/v1.0.0/chroma_db_sota.zip"

class EplanRAG:
    """
    RAG engine for EPLAN documentation utilizing 2026 state-of-the-art architectures.
    Maintains exact API interface required by MCP Server while significantly enhancing 
    vector retrieval quality via Markdown parsing and Sentence Semantic Splitting.
    """

    def __init__(self, docs_dir: str = None, db_dir: str = None):
        self.docs_dir = Path(docs_dir) if docs_dir else DOCS_DIR
        self.db_dir = Path(db_dir) if db_dir else CHROMA_DIR
        self.db_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"Loading embedding model '{EMBEDDING_MODEL}'...", flush=True)
        Settings.embed_model = HuggingFaceEmbedding(model_name=EMBEDDING_MODEL)
        Settings.llm = None 
        
        self._db_client = chromadb.PersistentClient(path=str(self.db_dir))
        self._collection = None

    @property
    def collection(self):
        if self._collection is None:
            self._collection = self._db_client.get_or_create_collection(name=COLLECTION_NAME)
        return self._collection

    def _get_all_files(self) -> List[Path]:
        md_files = []
        csv_files = []
        def _walk(path):
            try:
                with os.scandir(path) as it:
                    for entry in it:
                        if entry.is_dir(follow_symlinks=False):
                            _walk(entry.path)
                        elif entry.is_file(follow_symlinks=False):
                            if entry.name.endswith(".md"):
                                md_files.append(Path(entry.path))
                            elif entry.name.endswith(".csv"):
                                csv_files.append(Path(entry.path))
            except PermissionError:
                pass
        _walk(str(self.docs_dir))
        return sorted(md_files) + sorted(csv_files)

    def _compute_docs_fingerprint(self) -> str:
        hasher = hashlib.md5()
        for f in self._get_all_files():
            rel = str(f.relative_to(self.docs_dir))
            hasher.update(rel.encode("utf-8"))
            try:
                hasher.update(str(f.stat().st_mtime_ns).encode())
            except OSError:
                pass
        return hasher.hexdigest()

    def _needs_indexing(self) -> bool:
        if self.collection.count() == 0:
            return True
        meta_file = self.db_dir / "index_meta.json"
        if not meta_file.exists():
            return True
        try:
            with open(meta_file, encoding="utf-8") as f:
                return json.load(f).get("fingerprint") != self._compute_docs_fingerprint()
        except Exception:
            return True

    def _save_index_meta(self, fingerprint: str, stats: Dict):
        meta = {
            "fingerprint": fingerprint,
            "model": EMBEDDING_MODEL,
            "docs_dir": str(self.docs_dir),
            "indexed_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            **stats,
        }
        with open(self.db_dir / "index_meta.json", "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2)

    def _extract_meta(self, filepath: Path) -> dict:
        try:
            text = filepath.read_text(encoding="utf-8", errors="replace").strip()
        except:
            return None
        if not text:
            return None

        # Try extract custom frontmatter if any
        custom_source_url = ""
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', text, re.DOTALL)
        if match:
            text = match.group(2)
            
        url_match = re.search(r"\*\*Source URL:\*\*\s*(\S+)", text)
        if url_match:
            custom_source_url = url_match.group(1).strip()

        title_match = re.search(r"^#\s+(.+)", text, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filepath.stem

        rel_path = str(filepath.relative_to(self.docs_dir)).replace("\\", "/")
        parts = rel_path.split("/")
        category = parts[0] if parts else "General"

        return {
            "text": text,
            "title": title,
            "source_url": custom_source_url,
            "rel_path": rel_path,
            "category": category
        }

    def index_docs(self, force: bool = False) -> Dict:
        if self.collection.count() == 0 and not force:
            pass # Download DB logic available here
            
        fingerprint = self._compute_docs_fingerprint()

        if not force and not self._needs_indexing():
            return {"status": "up_to_date"}

        start_time = time.time()
        try:
            self._db_client.delete_collection(COLLECTION_NAME)
        except Exception:
            pass
        self._collection = None

        vector_store = ChromaVectorStore(chroma_collection=self.collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        all_files = self._get_all_files()
        print(f"Indexing {len(all_files)} files utilizing MarkdownNodeParser...", flush=True)

        md_parser = MarkdownNodeParser()
        text_splitter = SentenceSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

        documents = []
        files_ok = 0
        for filepath in all_files:
            doc_info = self._extract_meta(filepath)
            if not doc_info:
                continue
            
            files_ok += 1
            doc = Document(
                text=doc_info["text"],
                metadata={
                    "title": doc_info["title"],
                    "source": doc_info["rel_path"],
                    "source_url": doc_info["source_url"],
                    "category": doc_info["category"]
                },
                excluded_llm_metadata_keys=["source", "source_url"],
                excluded_embed_metadata_keys=["source_url"]
            )
            documents.append(doc)

        print("Executing Hierarchical Markdown Node splitting...", flush=True)
        base_nodes = md_parser.get_nodes_from_documents(documents)
        final_nodes = text_splitter.get_nodes_from_documents(base_nodes)

        # Enhance nodes for Hybrid search
        for i, node in enumerate(final_nodes):
            h_path = [node.metadata.get(f"Header_{j}") for j in range(1, 4) if node.metadata.get(f"Header_{j}")]
            header_str = " > ".join(h_path) if h_path else node.metadata.get("title", "")
            node.metadata["header_path"] = header_str
            node.metadata["chunk_index"] = i

        print("Generating Embeddings and committing to VectorStore...", flush=True)
        index = VectorStoreIndex(final_nodes, storage_context=storage_context, show_progress=False)
        index.storage_context.persist(persist_dir=str(self.db_dir))
        
        print("Indexing completed successfully!")
        stats = {"files_processed": files_ok, "total_chunks": len(final_nodes)}
        self._save_index_meta(fingerprint, stats)

        return {"status": "indexed", "elapsed_seconds": round(time.time() - start_time, 1), **stats}

    def search(self, query: str, n_results: int = MAX_RESULTS, category: str = None) -> List[Dict]:
        if self.collection.count() == 0:
            return [{"error": "No documents indexed. Call RAG index refresh."}]

        vector_store = ChromaVectorStore(chroma_collection=self.collection)
        storage_context = StorageContext.from_defaults(persist_dir=str(self.db_dir), vector_store=vector_store)
        
        try:
            index = load_index_from_storage(storage_context)
            vector_retriever = index.as_retriever(similarity_top_k=n_results)
            
            # Extract nodes exactly for BM25 hybrid semantic search
            nodes = list(storage_context.docstore.docs.values())
            if not nodes:
               retriever = vector_retriever
            else:
               bm25_retriever = BM25Retriever.from_defaults(nodes=nodes, similarity_top_k=n_results)
               retriever = QueryFusionRetriever(
                   [vector_retriever, bm25_retriever],
                   similarity_top_k=n_results, num_queries=1, mode="reciprocal_rerank"
               )
            
            nodes_with_scores = retriever.retrieve(query)
        except Exception as e:
            # Fallback direct query if index files corrupt
            print(f"LlamaIndex hybrid search warning: {e}. Falling back to pure Chroma query.")
            where_filter = {"category": category} if category else None
            bge_query = f"Represent this sentence for searching relevant passages: {query}"
            res = self.collection.query(query_texts=[bge_query], n_results=n_results, where=where_filter, include=["documents", "metadatas", "distances"])
            output = []
            if res and res["ids"] and res["ids"][0]:
                for i in range(len(res["ids"][0])):
                    m = res["metadatas"][0][i]
                    output.append({
                        "title": m.get("title", ""), "source": m.get("source", ""),
                        "source_url": m.get("source_url", ""), "category": m.get("category", ""),
                        "chunk": f"{m.get('chunk_index', 0)}", "relevance": round(1 - res["distances"][0][i], 4),
                        "content": res["documents"][0][i]
                    })
            return output

        if category:
            nodes_with_scores = [n for n in nodes_with_scores if n.node.metadata.get("category") == category]
            
        output = []
        for n in nodes_with_scores:
            m = n.node.metadata
            output.append({
                "title": m.get("title", "Untitled Document"),
                "source": m.get("source", ""),
                "source_url": m.get("source_url", ""),
                "category": m.get("category", ""),
                "chunk": m.get("header_path", str(m.get("chunk_index", 0))),
                "relevance": n.score,
                "content": n.node.get_content()
            })
        return output

    def get_stats(self) -> Dict:
        count = self.collection.count()
        meta = {}
        meta_file = self.db_dir / "index_meta.json"
        if meta_file.exists():
            try:
                with open(meta_file, encoding="utf-8") as f: meta = json.load(f)
            except Exception: pass
        return {
            "indexed_chunks": count, "model": EMBEDDING_MODEL, "docs_dir": str(self.docs_dir),
            "indexed_at": meta.get("indexed_at", "never"), "files_processed": meta.get("files_processed", 0),
            "needs_reindex": self._needs_indexing() if count > 0 else True,
        }

_instance: Optional[EplanRAG] = None

def get_rag(docs_dir: str = None) -> EplanRAG:
    global _instance
    if _instance is None:
        _instance = EplanRAG(docs_dir=docs_dir)
    return _instance
