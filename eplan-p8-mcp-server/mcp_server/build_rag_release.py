"""
Script to build the Precomputed RAG Database Release (.zip)

Usage:
    python build_rag_release.py

This script will:
  1. Remove any existing local chromadb
  2. Index all markdown and CSV files using BAAI/bge-base-en-v1.5
  3. Compress the resulting DB into chroma_db_sota.zip inside the mcp_server dir.
  
Once finished, you should upload 'chroma_db_sota.zip' to your GitHub 
repository's Releases section so users can auto-download it!
"""

import sys
import os
import shutil
import zipfile
from pathlib import Path

# Insert mcp_server path so we can import rag_engine
sys.path.insert(0, os.path.dirname(__file__))
from rag_engine import EplanRAG, CHROMA_DIR


def clean_existing_db():
    if CHROMA_DIR.exists():
        print(f"Cleaning existing database at {CHROMA_DIR}...")
        try:
            shutil.rmtree(CHROMA_DIR)
        except Exception as e:
            print(f"Warning: Could not fully clean existing DB: {e}")


def build_index():
    print("\n--- Phase 1: Indexing Everything into Vector DB ---")
    rag = EplanRAG()
    # Force indexing just in case
    stats = rag.index_docs(force=True)
    print("\n[Indexing Results]")
    for k, v in stats.items():
        print(f"  {k}: {v}")


def create_zip_release():
    print("\n--- Phase 2: Creating Release Archive (.zip) ---")
    output_zip = Path(__file__).parent / "chroma_db_sota.zip"
    
    if output_zip.exists():
        output_zip.unlink()

    # Create zip file packaging the contents of the Chroma DB
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        # Traverse everything inside chroma_db/
        for root, dirs, files in os.walk(CHROMA_DIR):
            for file in files:
                filepath = Path(root) / file
                # Save it inside the zip with relative path to CHROMA_DIR
                arcname = filepath.relative_to(CHROMA_DIR)
                zipf.write(filepath, arcname)

    size_mb = output_zip.stat().st_size / (1024 * 1024)
    print(f"\n[Release created successfully!]")
    print(f"  File: {output_zip.name}")
    print(f"  Path: {output_zip.absolute()}")
    print(f"  Size: {size_mb:.2f} MB")
    print("\nINSTRUCTIONS:")
    print(f"1. Upload '{output_zip.name}' to a new GitHub Release (e.g. v1.0.0).")
    print("2. Ensure the link matches PRECOMPUTED_DB_URL in rag_engine.py!")


if __name__ == "__main__":
    print("="*60)
    print(" EPLAN MCP - RAG Release Builder ")
    print("="*60)
    
    clean_existing_db()
    build_index()
    create_zip_release()
    
    print("\nAll done.")
