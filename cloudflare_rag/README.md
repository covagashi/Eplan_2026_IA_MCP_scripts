# EPLAN RAG MCP Server (Cloudflare)

Servidor MCP remoto que permite a Claude buscar en la documentacion de EPLAN (API Reference, User Guide, hidden actions) usando busqueda semantica con vectores.

Desplegado en Cloudflare Workers con Vectorize + Workers AI.

## Arquitectura

```
Claude Code  -->  MCP (Streamable HTTP)  -->  Cloudflare Worker
                                                   |
                                              Workers AI (bge-base-en-v1.5)
                                                   |
                                              Vectorize (eplan-knowledge-base)
                                              57,492 vectores / 768 dims / cosine
```

## Instalacion del MCP en Claude Code

### Opcion 1: HTTP directo (recomendado)

```bash
claude mcp add --transport http eplan-rag https://rag2026.covaga.xyz/mcp
```

### Opcion 2: via mcp-remote (si HTTP directo no funciona)

```bash
claude mcp add eplan-rag -- cmd /c npx mcp-remote https://rag2026.covaga.xyz/mcp
```

### Verificar

```bash
claude mcp list
```

Deberia aparecer `eplan-rag` en la lista. Luego dentro de Claude Code:

```
/mcp
```

Deberia mostrar `eplan-rag` conectado con 2 tools disponibles.

## Tools disponibles

| Tool | Descripcion |
|------|-------------|
| `eplan_search` | Busqueda semantica en la documentacion de EPLAN. Soporta filtro por categoria (API Reference, User Guide, Api) |
| `eplan_stats` | Estadisticas del indice vectorial (cantidad de vectores, dimensiones, metrica) |

### Ejemplo de uso

Dentro de Claude Code, simplemente pregunta:

```
Como cierro un proyecto en EPLAN con la API?
```

Claude usara automaticamente `eplan_search` para buscar la documentacion relevante.

## Endpoints REST

Ademas del MCP, el worker expone endpoints REST directos:

| Metodo | Endpoint | Descripcion |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/search` | Busqueda semantica (body: `{"query": "...", "topK": 5}`) |
| GET | `/stats` | Estadisticas del indice |
| POST | `/add-vectors` | Insertar vectores (requiere `Authorization: Bearer <WORKER_API_KEY>`) |

## Deploy

### Requisitos

- Cuenta de Cloudflare con Workers, Vectorize y Workers AI habilitados
- Node.js instalado
- `wrangler` CLI (`npm install -g wrangler`)

### Pasos

```bash
cd cloudflare_rag/worker
npm install
npx wrangler deploy
```

### Configurar el API key para escritura

```bash
npx wrangler secret put WORKER_API_KEY --name eplan-rag-mcp
```

Esto protege el endpoint `/add-vectors` para que solo usuarios autorizados puedan insertar vectores.

## Estructura

```
cloudflare_rag/
├── worker/
│   ├── src/
│   │   └── index.ts          # Worker principal (MCP + REST)
│   ├── wrangler.jsonc         # Configuracion de Cloudflare
│   ├── package.json
│   └── tsconfig.json
└── README.md                  # Este archivo
```
