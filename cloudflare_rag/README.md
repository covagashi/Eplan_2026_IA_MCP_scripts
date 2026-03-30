# EPLAN RAG documents MCP Server (Cloudflare)

Remote MCP server that allows Claude to search the EPLAN documentation (API Reference, User Guide, hidden actions) using semantic search with vectors.

Deployed on Cloudflare Workers with Vectorize + Workers AI.

## Architecture

```
Claude Code  -->  MCP (Streamable HTTP)  -->  Cloudflare Worker
                                                   |
                                              Workers AI (bge-base-en-v1.5)
                                                   |
                                              Vectorize (eplan-knowledge-base)
                                              57,492 vectores / 768 dims / cosine
```

## Instalacion del MCP en Claude Code

### via mcp-remote

```bash
claude mcp add eplan-rag -- cmd /c npx mcp-remote https://rag2026.covaga.xyz/mcp
```

### Verificar

```bash
claude mcp list
```

Should show `eplan-rag` in the list. Then inside Claude Code:

```
/mcp
```

Should show `eplan-rag` connected with 2 tools available.

## Tools available

| Tool | Description |
|------|-------------|
| `eplan_search` | Semantic search in EPLAN documentation. Supports filtering by category (API Reference, User Guide, Api) |
| `eplan_stats` | Statistics of the vector index (number of vectors, dimensions, metric) |


## REST Endpoints

In addition to the MCP, the worker exposes direct REST endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/search` | Semantic search (body: `{"query": "...", "topK": 5}`) |
| GET | `/stats` | Estadisticas del indice |
| POST | `/add-vectors` | Insertar vectores (requiere `Authorization: Bearer <WORKER_API_KEY>`) |


## Structure

```
cloudflare_rag/
├── worker/
│   ├── src/
│   │   └── index.ts          # Worker principal (MCP + REST)
│   ├── wrangler.jsonc         # Cloudflare configuration
│   ├── package.json
│   └── tsconfig.json
└── README.md                  # This file
```
