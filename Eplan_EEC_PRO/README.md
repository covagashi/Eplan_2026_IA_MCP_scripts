# EPLAN EEC Pro 2026 - Documentation RAG

Scraper + RAG (Retrieval Augmented Generation) for the official **EPLAN Engineering Configuration Pro 2026** documentation.

## Contents

- `docs_md/` - 1648 documentation pages converted to Markdown, organized into 36 categories
- `rag_db/` - ChromaDB v1 vector database (1967 chunks, MiniLM-L6 embedding)
- `rag_db_v2/` - v2 vector database (3043 chunks, bge-base-en-v1.5 embedding)
- `scrape_eplan.py` - Documentation scraping script
- `rag_index_llama.py` - **NEW SOTA:** LlamaIndex-powered indexer, stores natively in ChromaDB.
- `rag_query_llama.py` - **NEW SOTA:** Hybrid Search + Generation (Agentic RAG) with LlamaIndex, capable of connecting to local LLMs (e.g., Ollama).

## 🤖 Usage for AI Assistants / Claude Code (Agentic RAG)

> **CRITICAL RULE FOR AI AGENTS (CLAUDE CODE):** 
> Before attempting to write any EPLAN macros, formulas, scripts or resolving configuration issues, you MUST execute the local RAG tool to retrieve exact documentation. 
> ALWAYS run: `python rag_query_llama.py "your technical question" --json` and read the `content` fields before answering.

## Quick Start (SOTA LlamaIndex recommended)

```bash
# Install SOTA dependencies
pip install chromadb llama-index llama-index-vector-stores-chroma llama-index-llms-ollama

# Re-index (only if docs are modified)
python rag_index_llama.py

# Search documentation (Pure Retrieval)
python rag_query_llama.py "how to configure Job Server REST API"

# Search and Generate Response with Local LLM
python rag_query_llama.py "What are the rules for PLC addressing?" --chat --model llama3.2

# Options
python rag_query_v2.py "terminal addressing" --no-rerank    # without cross-encoder (faster)
python rag_query_v2.py "macro template" --no-parent         # without parent context
python rag_query_v2.py "csv export" --json                  # JSON output
```

## Architectures: v1 vs v2 vs SOTA (LlamaIndex)

| Aspect | v1 | v2 (Custom Script) | SOTA (LlamaIndex) |
|---|---|---|---|
| Framework | Custom Python | Custom Python | **LlamaIndex** + ChromaDB |
| Chunking | By paragraphs (800 chars) | Hierarchical by headers H1/H2/H3 | Hierarchical LlamaIndex (`TextNode`) |
| Chunks | 1,967 | 3,043 child + 1,648 parent | 3,043 TextNodes + Relational Metadata |
| Embedding | all-MiniLM-L6 | bge-base-en-v1.5 | bge-base-en-v1.5 / bge-m3 |
| Search | Vector only | Hybrid Custom (BM25 + Vector) | **QueryFusionRetriever** (BM25 + Vector) |
| Reranking | No | Cross-encoder ms-marco-MiniLM | Cross-encoder ms-marco-MiniLM |
| LLM Generation | No | No | Yes (Native `--chat` support via Ollama) |
| Context | Only the chunk | Chunk + parent page | Chunk + Injectable Parent Pages |

## Main Categories

| Category | Pages | Description |
|---|---|---|
| refformulas | 317 | Formula language |
| admin | 304 | Installation, configuration, VMArgs |
| eecbase | 119 | Base functionality |
| refformui | 84 | Form-UI reference |
| refcommands | 79 | Commands |
| refscripting | 58 | Scripting reference |
| concept | 58 | Concepts |
| eececad | 47 | ECAD module |
| eecplc | 47 | PLC module |
| + 27 more... | ~500 | Tutorials, SAP, Office, Graph2D, etc. |

## Source

Official documentation: https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/main_k_home.htm
