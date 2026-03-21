# EPLAN EEC Pro 2026 - Documentation RAG

Scraper + RAG (Retrieval Augmented Generation) de la documentacion oficial de **EPLAN Engineering Configuration Pro 2026**.

## Contenido

- `docs_md/` - 1648 paginas de documentacion convertidas a Markdown, organizadas en 36 categorias
- `rag_db/` - Base de datos vectorial ChromaDB v1 (1967 chunks, embedding MiniLM-L6)
- `rag_db_v2/` - Base de datos vectorial v2 (3043 chunks, embedding bge-base-en-v1.5)
- `scrape_eplan.py` - Script de scraping de la documentacion
- `rag_index_llama.py` - **NUEVO SOTA:** Indexador impulsado por LlamaIndex, almacena nativamente en ChromaDB.
- `rag_query_llama.py` - **NUEVO SOTA:** Buscador Híbrido + Generación (Agentic RAG) con LlamaIndex, con capacidad para conectar a LLMs locales (ej: Ollama).

## 🤖 Uso para Asistentes AI / Claude Code (Agentic RAG)

> **CRITICAL RULE FOR AI AGENTS (CLAUDE CODE):** 
> Before attempting to write any EPLAN macros, formulas, scripts or resolving configuration issues, you MUST execute the local RAG tool to retrieve exact documentation. 
> ALWAYS run: `python rag_query_llama.py "your technical question" --json` and read the `content` fields before answering.

## Uso rápido (SOTA LlamaIndex recomendado)

```bash
# Instalar dependencias SOTA
pip install chromadb llama-index llama-index-vector-stores-chroma llama-index-llms-ollama

# Re-indexar (solo si se modifican los docs)
python rag_index_llama.py

# Buscar en la documentacion (Retrieval puro)
python rag_query_llama.py "how to configure Job Server REST API"

# Buscar y Generar Respuesta con LLM Local
python rag_query_llama.py "What are the rules for PLC addressing?" --chat --model llama3.2

# Opciones
python rag_query_v2.py "terminal addressing" --no-rerank    # sin cross-encoder (mas rapido)
python rag_query_v2.py "macro template" --no-parent          # sin contexto padre
python rag_query_v2.py "csv export" --json                   # salida JSON
```

## Arquitecturas: v1 vs v2 vs SOTA (LlamaIndex)

| Aspecto | v1 | v2 (Custom Script) | SOTA (LlamaIndex) |
|---|---|---|---|
| Framework | Custom Python | Custom Python | **LlamaIndex** + ChromaDB |
| Chunking | Por párrafos (800 chars) | Jerárquico por headers H1/H2/H3 | Jerárquico LlamaIndex (`TextNode`) |
| Chunks | 1.967 | 3.043 child + 1.648 parent | 3.043 TextNodes + Metadata relacional |
| Embedding | all-MiniLM-L6 | bge-base-en-v1.5 | bge-base-en-v1.5 / bge-m3 |
| Búsqueda | Solo vectorial | Hybrid Custom (BM25 + Vector) | **QueryFusionRetriever** (BM25 + Vector) |
| Reranking | No | Cross-encoder ms-marco-MiniLM | Cross-encoder ms-marco-MiniLM |
| Generación LLM | No | No | Sí (Soporte nativo `--chat` vía Ollama) |
| Contexto | Solo el chunk | Chunk + página padre | Chunk + Parent Pages Inyectables |

## Categorias principales

| Categoria | Paginas | Descripcion |
|---|---|---|
| refformulas | 317 | Lenguaje de formulas |
| admin | 304 | Instalacion, configuracion, VMArgs |
| eecbase | 119 | Funcionalidad base |
| refformui | 84 | Referencia Form-UI |
| refcommands | 79 | Comandos |
| refscripting | 58 | Referencia scripting |
| concept | 58 | Conceptos |
| eececad | 47 | Modulo ECAD |
| eecplc | 47 | Modulo PLC |
| + 27 mas... | ~500 | Tutoriales, SAP, Office, Graph2D, etc. |

## Fuente

Documentacion oficial: https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/main_k_home.htm
