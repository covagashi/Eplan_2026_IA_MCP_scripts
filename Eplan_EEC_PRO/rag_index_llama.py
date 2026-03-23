"""
EPLAN EEC Pro RAG Indexer - Modern 2026 LlamaIndex Pipeline
"""
import os
import re
import json
from pathlib import Path

from llama_index.core import Document, VectorStoreIndex, StorageContext, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import MarkdownNodeParser, SentenceSplitter
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
import logging
import sys

# Suppress overly verbose transformers warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"

DOCS_DIR = Path("docs_md")
DB_DIR = Path("rag_db_llama_chroma")
EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5" # Solid balance of speed and precision
CHUNK_SIZE = 512
CHUNK_OVERLAP = 64

def extract_frontmatter(text: str) -> tuple[dict, str]:
    meta = {}
    body = text
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', text, re.DOTALL)
    if match:
        for line in match.group(1).split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                meta[key.strip()] = val.strip().strip('"')
        body = match.group(2)
    return meta, body

def main():
    print("=" * 60)
    print("EPLAN EEC PRO RAG Indexer - SOTA 2026 Pipeline")
    print("=" * 60)

    # 1. Pipeline Settings
    print(f"[*] Loading Embedding Model: {EMBEDDING_MODEL}")
    Settings.embed_model = HuggingFaceEmbedding(model_name=EMBEDDING_MODEL)
    Settings.llm = None 
    
    DB_DIR.mkdir(exist_ok=True)
    
    print(f"[*] Initializing ChromaDB connection at {DB_DIR}...")
    db = chromadb.PersistentClient(path=str(DB_DIR))
    chroma_collection = db.get_or_create_collection("eplan_docs")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    # 2. Advanced Node Parsers
    # Markdown parser intelligently chunks by # Headers
    md_parser = MarkdownNodeParser()
    # Sentence splitter ensures no single chunk exceeds context window (e.g., long tables)
    text_splitter = SentenceSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

    md_files = sorted(DOCS_DIR.rglob("*.md"))
    print(f"[*] Found {len(md_files)} markdown files")
    
    documents = []
    parent_map = {}

    print(f"[*] Parsing documents and applying Semantic Metadata...")
    for i, md_file in enumerate(md_files):
        text = md_file.read_text(encoding="utf-8", errors="replace")
        meta, body = extract_frontmatter(text)

        if not body.strip():
            continue

        title = meta.get("title", md_file.stem)
        source = meta.get("source", "")
        category = meta.get("category", md_file.parent.name)
        file_name = meta.get("file", md_file.stem)
        
        # We record parent_map for backward compatibility with your query UI parent visualization
        parent_id = f"parent_{file_name}"
        parent_map[parent_id] = {
            "title": title,
            "category": category,
            "source": source,
            "content": body.strip()[:2000] # store summary instead of bloating index
        }

        # Inject robust global metadata accessible to all child nodes
        doc = Document(
            text=body,
            metadata={
                "title": title,
                "source": source,
                "category": category,
                "file": file_name,
                "parent_id": parent_id
            },
            excluded_llm_metadata_keys=["file", "parent_id"],
            excluded_embed_metadata_keys=["file", "parent_id", "source"]
        )
        documents.append(doc)

    print(f"[*] Executing Markdown Hierarchical Chunking...")
    # This automatically splits by Markdown Headers and injects Header Path to metadata!
    base_nodes = md_parser.get_nodes_from_documents(documents)
    
    print(f"[*] Executing Semantic Sentence Splitting for dense vector quality...")
    # This strictly enforces Token capacity limits without chopping sentences midway
    final_nodes = text_splitter.get_nodes_from_documents(base_nodes)
    
    # Optional Semantic Enhancement: Append Header Path into the chunk text itself so the vector model "sees" the context structure
    for node in final_nodes:
        # MarkdownNodeParser injects keys like 'Header_1', 'Header_2' into metadata. 
        # We combine them into a breadcrumb!
        headers = [node.metadata.get(f"Header_{i}") for i in range(1, 4) if node.metadata.get(f"Header_{i}")]
        if headers:
            breadcrumb = " > ".join(headers)
            node.metadata["header_path"] = breadcrumb
            # Prepend breadcrumbs context directly into text for embedding 
            # node.text = f"[Context: {breadcrumb}]\n{node.text}" # Handled natively by node.get_content() if metadata included

    print(f"    -> Generated {len(final_nodes)} high-quality vector nodes.")
    
    print("[*] Building VectorStoreIndex (Embedding Vectors Generation)...")
    index = VectorStoreIndex(final_nodes, storage_context=storage_context, show_progress=True)
    
    print(f"[*] Persisting Docstore (required for BM25 Hybrid Local Search)...")
    index.storage_context.persist(persist_dir=str(DB_DIR))
    
    parent_path = DB_DIR / "parent_map.json"
    with open(parent_path, 'w', encoding='utf-8') as f:
        json.dump(parent_map, f, ensure_ascii=False)
        
    print(f"\nDone! SOTA Architecture deployed to {DB_DIR.absolute()}")

if __name__ == "__main__":
    main()
