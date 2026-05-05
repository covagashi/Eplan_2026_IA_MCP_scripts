"""
EPLAN EEC Pro RAG Query - Modern 2026 LlamaIndex Pipeline
"""
import sys
import json
import argparse
import re
from pathlib import Path
import warnings

# Suppress heavy HF/Torch warnings during CLI use
warnings.filterwarnings("ignore")

from llama_index.core import VectorStoreIndex, StorageContext, Settings, load_index_from_storage
from llama_index.core.retrievers import QueryFusionRetriever
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.retrievers.bm25 import BM25Retriever
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.prompts import PromptTemplate

DB_DIR = Path("rag_db_llama_chroma")
EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"

SYNONYMS = {
    "formula": ["expression", "calculation", "computed", "function"],
    "terminal": ["connection point", "addressing", "connector"],
    "plc": ["programmable logic controller", "io", "fieldbus"],
    "ecad": ["electrical cad", "schematic", "wiring", "circuit"],
    "graph2d": ["2d graphic", "diagram", "drawing", "visualization"],
    "macro": ["template", "reusable", "symbol"],
    "bom": ["bill of materials", "parts list", "material list"],
    "csv": ["export", "import", "comma separated", "data exchange"],
    "xml": ["export", "import", "data exchange", "markup"],
    "job": ["jobserver", "batch", "automation", "scheduled task"],
    "api": ["rest", "interface", "endpoint", "webservice"],
    "script": ["scripting", "eecscripting", "automation", "code"],
    "panel": ["propanel", "cabinet", "enclosure", "layout"],
    "sap": ["erp", "integration", "material management"],
    "form": ["formui", "dialog", "user interface", "ui"],
    "command": ["action", "execute", "run", "operation"],
    "parameter": ["property", "attribute", "setting", "value"],
    "project": ["model", "workspace", "configuration"],
    "report": ["output", "document", "listing", "printout"],
    "backup": ["export", "save", "restore", "archive"],
    "addressing": ["terminal", "numbering", "io addressing"],
    "regex": ["regular expression", "pattern", "match", "text pattern"],
}

def expand_query(query: str) -> str:
    words = query.lower().split()
    expansions = []
    for word in words:
        clean = re.sub(r'[^\w]', '', word)
        if clean in SYNONYMS:
            expansions.extend(SYNONYMS[clean][:2])
    if expansions:
        return f"{query} {' '.join(expansions)}"
    return query

_reranker = None
def get_reranker():
    global _reranker
    if _reranker is None:
        try:
            from sentence_transformers import CrossEncoder
            # UPGRADED TO BGE-RERANKER-BASE in 2026 pipeline for vastly superior MRR/NDCG
            _reranker = CrossEncoder("BAAI/bge-reranker-base")
            print("  [Reranker loaded: BAAI/bge-reranker-base (SOTA)]")
        except Exception as e:
            print(f"  [Reranker not available: {e}]")
            _reranker = False
    return _reranker if _reranker else None

def rerank(query: str, candidates: list[dict], top_k: int) -> list[dict]:
    reranker = get_reranker()
    if not reranker or not candidates:
        return candidates[:top_k]

    pairs = [(query, c["content"][:1024]) for c in candidates]
    scores = reranker.predict(pairs)

    for i, c in enumerate(candidates):
        c["rerank_score"] = float(scores[i])

    candidates.sort(key=lambda x: x["rerank_score"], reverse=True)
    return candidates[:top_k]

def load_parent_map():
    parent_path = DB_DIR / "parent_map.json"
    if not parent_path.exists():
        return {}
    with open(parent_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def query_rag(question: str, top_k: int = 5, category: str = None,
              use_parent: bool = True, use_rerank: bool = True,
              chat_with_llm: bool = False, llm_model: str = "llama3.2") -> tuple[list[dict], str | None]:
              
    Settings.embed_model = HuggingFaceEmbedding(model_name=EMBEDDING_MODEL)
    
    if chat_with_llm:
        try:
            from llama_index.llms.ollama import Ollama
            Settings.llm = Ollama(model=llm_model, request_timeout=120.0)
            print(f"  [LLM Enabled: Ollama model '{llm_model}']")
        except ImportError:
            print("  [Failed to load Ollama, using Mock LLM]")
            Settings.llm = None
    else:
        Settings.llm = None
    
    db = chromadb.PersistentClient(path=str(DB_DIR))
    chroma_collection = db.get_or_create_collection("eplan_docs")
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    
    # Storage context handles loading the metadata and BM25 docs natively
    storage_context = StorageContext.from_defaults(persist_dir=str(DB_DIR), vector_store=vector_store)
    index = load_index_from_storage(storage_context)
    
    vector_retriever = index.as_retriever(similarity_top_k=top_k * 4)
    
    nodes = list(storage_context.docstore.docs.values())
    if not nodes:
        print("  [Warning: No docstore nodes found for BM25. Ensure you ran the indexer first.]")
    bm25_retriever = BM25Retriever.from_defaults(nodes=nodes, similarity_top_k=top_k * 4) if nodes else vector_retriever
    
    # Multimodal Reciprocal Rank Fusion mapping
    retriever = QueryFusionRetriever(
        [vector_retriever, bm25_retriever],
        similarity_top_k=top_k * 4,
        num_queries=1,
        mode="reciprocal_rerank",
        use_async=False,
    )
    
    expanded = expand_query(question)
    nodes_with_scores = retriever.retrieve(expanded)
    
    if category:
        nodes_with_scores = [n for n in nodes_with_scores if n.node.metadata.get("category") == category]
        
    parent_map = load_parent_map() if use_parent else {}
    
    candidates = []
    for n in nodes_with_scores:
        meta = n.node.metadata
        # Dynamically calculate header path if available from MarkdownNodeParser
        header_path = meta.get("header_path", "")
        if not header_path:
            h1 = meta.get("Header_1")
            h2 = meta.get("Header_2")
            h3 = meta.get("Header_3")
            header_path = " > ".join(filter(None, [h1, h2, h3]))

        r = {
            "id": n.node.id_,
            "distance": n.score,
            "title": meta.get("title", "Untitled"),
            "source": meta.get("source", ""),
            "category": meta.get("category", ""),
            "file": meta.get("file", ""),
            "header_path": header_path,
            "parent_id": meta.get("parent_id", ""),
            "content": n.node.get_content()
        }
        candidates.append(r)
        
    if use_rerank:
        candidates = rerank(question, candidates, top_k)
    else:
        candidates = candidates[:top_k]

    if use_parent:
        for c in candidates:
            pid = c.get("parent_id", "")
            if pid in parent_map:
                c["parent_content"] = parent_map[pid]["content"]
            else:
                c["parent_content"] = ""
                
    generated_answer = None
    if chat_with_llm and Settings.llm:
        qa_prompt_tmpl_str = (
            "You are an expert technical assistant for EPLAN EEC Pro.\n"
            "Use ONLY the provided context information below to answer the user's question.\n"
            "If you cannot answer the question based on the context, say 'I cannot answer this based on the provided documentation.'\n"
            "---------------------\n"
            "{context_str}\n"
            "---------------------\n"
            "Question: {query_str}\n"
            "Answer: "
        )
        qa_prompt_tmpl = PromptTemplate(qa_prompt_tmpl_str)
        
        query_engine = RetrieverQueryEngine.from_args(
            retriever=retriever,
            text_qa_template=qa_prompt_tmpl
        )
        print("  [Thinking...]")
        response = query_engine.query(expanded)
        generated_answer = str(response)
                
    return candidates, generated_answer

def main():
    parser = argparse.ArgumentParser(description="EPLAN EEC Pro RAG Query (SOTA LlamaIndex)")
    parser.add_argument("question", help="Your question")
    parser.add_argument("--top", type=int, default=5, help="Number of results (default: 5)")
    parser.add_argument("--category", type=str, default=None, help="Filter by category")
    parser.add_argument("--no-parent", action="store_true", help="Don't show parent context")
    parser.add_argument("--no-rerank", action="store_true", help="Skip cross-encoder reranking")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--chat", action="store_true", help="Generate an answer using local LLM via Ollama")
    parser.add_argument("--model", type=str, default="llama3.2", help="Ollama model to use (default: llama3.2)")
    args = parser.parse_args()

    results, answer = query_rag(
        args.question, args.top, args.category,
        use_parent=not args.no_parent,
        use_rerank=not args.no_rerank,
        chat_with_llm=args.chat,
        llm_model=args.model,
    )

    if args.json:
        for r in results:
             r.pop("parent_content", None)
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(f"\n{'='*60}")
        print(f"Query: {args.question}")
        expanded = expand_query(args.question)
        if expanded != args.question:
            print(f"Expanded: {expanded}")
        print(f"Results: {len(results)}")
        print(f"{'='*60}\n")

        for i, r in enumerate(results, 1):
            score_info = f"score: {r['distance']:.4f}" if r['distance'] is not None else "BM25 only"
            if "rerank_score" in r:
                score_info += f", rerank: {r['rerank_score']:.4f}"
            print(f"--- Result {i} ({score_info}) ---")
            print(f"Title:    {r['title']}")
            if r['header_path']: print(f"Path:     {r['header_path']}")
            print(f"Category: {r['category']}")
            if r['source']: print(f"Source:   {r['source']}")
            print(f"\n{r['content'][:800]}")
            if r.get("parent_content") and not args.no_parent:
                print(f"\n  [Parent Overview Available]")
            print()
            
        if args.chat and answer:
            print(f"{'='*60}")
            print("🤖 LLM GENERATED ANSWER:")
            print(f"{'='*60}\n")
            print(answer)
            print(f"\n{'='*60}")

if __name__ == "__main__":
    main()
