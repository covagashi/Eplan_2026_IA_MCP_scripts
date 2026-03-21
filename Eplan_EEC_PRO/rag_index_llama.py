"""
EPLAN EEC Pro RAG Indexer - LlamaIndex Version
"""
import os
import re
import json
from pathlib import Path
from llama_index.core import Document, VectorStoreIndex, StorageContext, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.schema import TextNode, IndexNode
import logging
import sys

DOCS_DIR = Path("docs_md")
DB_DIR = Path("rag_db_llama_chroma")
EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"
MAX_CHILD_CHARS = 2500
MIN_CHUNK_CHARS = 80

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

def parse_sections(body: str) -> list[dict]:
    lines = body.split('\n')
    sections = []
    headers = {1: '', 2: '', 3: ''}
    current_lines = []
    current_level = 0

    def flush():
        text = '\n'.join(current_lines).strip()
        if len(text) >= MIN_CHUNK_CHARS:
            path_parts = [headers[l] for l in (1, 2, 3) if headers[l]]
            sections.append({
                'level': current_level,
                'header': headers.get(current_level, ''),
                'content': text,
                'header_path': ' > '.join(path_parts),
            })

    for line in lines:
        m = re.match(r'^(#{1,3})\s+(.+)', line)
        if m:
            flush()
            current_lines = [line]
            level = len(m.group(1))
            headers[level] = m.group(2).strip()
            for l in range(level + 1, 4):
                headers[l] = ''
            current_level = level
        else:
            current_lines.append(line)

    flush()
    return sections

def split_long_section(section: dict, max_chars: int = MAX_CHILD_CHARS) -> list[dict]:
    content = section['content']
    if len(content) <= max_chars:
        return [section]

    paragraphs = re.split(r'\n{2,}', content)
    chunks = []
    current = ""

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if len(current) + len(para) + 2 > max_chars and len(current) >= MIN_CHUNK_CHARS:
            chunks.append({**section, 'content': current.strip()})
            current = para
        else:
            current = f"{current}\n\n{para}" if current else para

    if current.strip() and len(current.strip()) >= MIN_CHUNK_CHARS:
        chunks.append({**section, 'content': current.strip()})

    return chunks if chunks else [section]

def main():
    print("=" * 60)
    print("EPLAN EEC Pro RAG Indexer (LlamaIndex)")
    print("=" * 60)

    # 1. Setup LlamaIndex Settings
    Settings.embed_model = HuggingFaceEmbedding(model_name=EMBEDDING_MODEL)
    Settings.llm = None 
    
    DB_DIR.mkdir(exist_ok=True)
    
    print(f"Initializing ChromaDB connection at {DB_DIR}...")
    db = chromadb.PersistentClient(path=str(DB_DIR))
    chroma_collection = db.get_or_create_collection("eplan_docs")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    md_files = sorted(DOCS_DIR.rglob("*.md"))
    print(f"Found {len(md_files)} markdown files\n")
    
    nodes = []
    parent_map = {}

    for i, md_file in enumerate(md_files):
        text = md_file.read_text(encoding="utf-8", errors="replace")
        meta, body = extract_frontmatter(text)

        if not body.strip() or len(body.strip()) < MIN_CHUNK_CHARS:
            continue

        title = meta.get("title", md_file.stem)
        source = meta.get("source", "")
        category = meta.get("category", md_file.parent.name)
        filename = meta.get("file", md_file.stem)
        parent_id = f"parent_{filename}"
        
        parent_map[parent_id] = {
            "title": title,
            "category": category,
            "source": source,
            "content": body.strip(),
        }

        sections = parse_sections(body)
        if not sections:
            sections = [{'level': 0, 'header': title, 'content': body.strip(), 'header_path': title}]

        child_chunks = []
        for sec in sections:
            child_chunks.extend(split_long_section(sec))

        for j, chunk in enumerate(child_chunks):
            child_id = f"{filename}_c{j}"
            header_path = chunk['header_path'] or title
            
            enriched = f"[{category}] [{header_path}]\n{chunk['content']}"
            child_node = TextNode(
                id_=child_id,
                text=enriched,
                metadata={
                    "title": title,
                    "source": source,
                    "category": category,
                    "file": filename,
                    "header_path": header_path,
                    "header": chunk.get('header', ''),
                    "chunk_index": j,
                    "parent_id": parent_id
                }
            )
            nodes.append(child_node)

        if (i + 1) % 200 == 0:
            print(f"  Processed {i + 1}/{len(md_files)} files ({len(nodes)} chunks)")

    print(f"\nTotal child chunks: {len(nodes)}")
    print(f"Total parent pages: {len(parent_map)}")
    
    print("Building VectorStoreIndex...")
    index = VectorStoreIndex(nodes, storage_context=storage_context, show_progress=True)
    
    print(f"Persisting docstore (for BM25) to {DB_DIR}...")
    index.storage_context.persist(persist_dir=str(DB_DIR))
    
    parent_path = DB_DIR / "parent_map.json"
    with open(parent_path, 'w', encoding='utf-8') as f:
        json.dump(parent_map, f, ensure_ascii=False)
        
    print(f"\nDone! Indexed and saved to {DB_DIR.absolute()}")

if __name__ == "__main__":
    main()
