interface Env {
  AI: Ai;
  VECTOR_INDEX: VectorizeIndex;
  MCP_OBJECT: DurableObjectNamespace<EplanRAGMCP>;
  WORKER_API_KEY?: string;
}
