/**
 * EPLAN RAG MCP Server on Cloudflare Workers
 *
 * Exposes EPLAN documentation search via MCP protocol (SSE transport)
 * and also keeps REST endpoints for direct API access.
 *
 * MCP tools:
 *   - eplan_search: Semantic search over EPLAN docs
 *   - eplan_stats:  Index statistics
 *
 * REST endpoints:
 *   - GET  /health
 *   - POST /search
 *   - GET  /stats
 *   - POST /add-vectors
 */
import { McpAgent } from "agents/mcp";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

// --- MCP Agent (Durable Object) ---

export class EplanRAGMCP extends McpAgent<Env, {}, {}> {
  server = new McpServer({
    name: "eplan-rag",
    version: "1.0.0",
  });

  async init() {
    // Tool: eplan_search
    this.server.tool(
      "eplan_search",
      "Search EPLAN documentation (API Reference, User Guide, hidden actions). " +
        "Use natural language queries. Returns relevant chunks with metadata.",
      {
        query: z.string().describe("Natural language search query about EPLAN"),
        topK: z
          .number()
          .min(1)
          .max(20)
          .default(5)
          .describe("Number of results to return"),
        category: z
          .enum(["API Reference", "User Guide"])
          .optional()
          .describe("Filter by doc category"),
      },
      async ({ query, topK, category }) => {
        const env = this.env;

        // Generate embedding with Workers AI
        const embResponse = await env.AI.run("@cf/baai/bge-base-en-v1.5", {
          text: [query],
        });
        const queryVector = embResponse.data[0];

        // Query Vectorize
        const vectorQuery: VectorizeQueryOptions = {
          topK: topK ?? 5,
          returnValues: false,
          returnMetadata: "all",
        };

        if (category) {
          vectorQuery.filter = { category: { $eq: category } };
        }

        const results = await env.VECTOR_INDEX.query(queryVector, vectorQuery);

        // Format results
        const formatted = results.matches
          .map((m, i) => {
            const meta = (m.metadata ?? {}) as Record<string, string>;
            const lines = [
              `### ${i + 1}. ${meta.title || "Untitled"} (score: ${m.score.toFixed(4)})`,
            ];
            if (meta.category) lines.push(`**Category:** ${meta.category}`);
            if (meta.source_url) lines.push(`**Source:** ${meta.source_url}`);
            if (meta.header_path)
              lines.push(`**Section:** ${meta.header_path}`);
            if (meta.content) lines.push("", meta.content);
            return lines.join("\n");
          })
          .join("\n\n---\n\n");

        return {
          content: [
            {
              type: "text" as const,
              text: `Found ${results.matches.length} results for "${query}":\n\n${formatted}`,
            },
          ],
        };
      }
    );

    // Tool: eplan_stats
    this.server.tool(
      "eplan_stats",
      "Get statistics about the EPLAN RAG index (vector count, dimensions, metric).",
      {},
      async () => {
        const info = await this.env.VECTOR_INDEX.describe();
        return {
          content: [
            {
              type: "text" as const,
              text: JSON.stringify(
                {
                  index: "eplan-knowledge-base",
                  model: "BAAI/bge-base-en-v1.5",
                  dimensions: 768,
                  ...info,
                },
                null,
                2
              ),
            },
          ],
        };
      }
    );
  }
}

// --- Worker fetch handler (REST + MCP routing) ---

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext) {
    const url = new URL(request.url);
    const path = url.pathname;

    const corsHeaders: Record<string, string> = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type, Authorization",
    };

    if (request.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }

    // --- MCP SSE endpoint (handled by Durable Object) ---
    if (path === "/sse" || path === "/mcp" || path.startsWith("/mcp/")) {
      // Route to the MCP Durable Object
      const id = env.MCP_OBJECT.idFromName("default");
      const stub = env.MCP_OBJECT.get(id);
      return stub.fetch(request);
    }

    // --- REST endpoints ---
    try {
      // Public endpoints (no auth required)
      if (path === "/health") {
        return json(
          { status: "ok", mcp: true, timestamp: new Date().toISOString() },
          200,
          corsHeaders
        );
      }

      if (path === "/stats") {
        return await handleStats(env, corsHeaders);
      }

      // Search: public read, no auth needed
      if (path === "/search" && request.method === "POST") {
        return await handleSearch(request, env, corsHeaders);
      }

      // Write endpoints: require WORKER_API_KEY
      if (path === "/add-vectors" && request.method === "POST") {
        const authError = checkAuth(request, env);
        if (authError) return authError;
        return await handleAddVectors(request, env, corsHeaders);
      }

      return json({ error: "Not found", endpoints: ["/health", "/search", "/stats", "/sse", "/mcp"] }, 404, corsHeaders);
    } catch (err: any) {
      return json({ error: err.message }, 500, corsHeaders);
    }
  },
} satisfies ExportedHandler<Env>;

// --- Auth ---

function checkAuth(request: Request, env: Env): Response | null {
  if (!env.WORKER_API_KEY) return null; // no key configured = no auth
  const auth = request.headers.get("Authorization");
  if (auth === `Bearer ${env.WORKER_API_KEY}`) return null;
  return json({ error: "Unauthorized. Set Authorization: Bearer <WORKER_API_KEY>" }, 401);
}

// --- REST handlers ---

async function handleSearch(
  request: Request,
  env: Env,
  corsHeaders: Record<string, string>
) {
  const data = (await request.json()) as {
    query?: string;
    topK?: number;
    category?: string;
  };
  const { query, topK = 5, category } = data;

  if (!query) {
    return json({ error: "Missing 'query' field" }, 400, corsHeaders);
  }

  const embResponse = await env.AI.run("@cf/baai/bge-base-en-v1.5", {
    text: [query],
  });
  const queryVector = embResponse.data[0];

  const vectorQuery: VectorizeQueryOptions = {
    topK: Math.min(topK, 20),
    returnValues: false,
    returnMetadata: "all",
  };

  if (category) {
    vectorQuery.filter = { category: { $eq: category } };
  }

  const results = await env.VECTOR_INDEX.query(queryVector, vectorQuery);

  return json(
    {
      query,
      results: results.matches.map((m) => {
        const meta = (m.metadata ?? {}) as Record<string, string>;
        return {
          id: m.id,
          score: m.score,
          title: meta.title || "",
          category: meta.category || "",
          source: meta.source || "",
          source_url: meta.source_url || "",
          content: meta.content || "",
          header_path: meta.header_path || "",
        };
      }),
      count: results.matches.length,
    },
    200,
    corsHeaders
  );
}

async function handleAddVectors(
  request: Request,
  env: Env,
  corsHeaders: Record<string, string>
) {
  const data = (await request.json()) as {
    vectors?: Array<{ id: string; values: number[]; metadata?: object }>;
  };
  const vectors = data.vectors || [];

  if (vectors.length === 0) {
    return json({ error: "No vectors provided" }, 400, corsHeaders);
  }

  const BATCH = 1000;
  let inserted = 0;

  for (let i = 0; i < vectors.length; i += BATCH) {
    const batch = vectors.slice(i, i + BATCH).map((v) => ({
      id: v.id,
      values: v.values,
      metadata: v.metadata || {},
    }));
    await env.VECTOR_INDEX.insert(batch);
    inserted += batch.length;
  }

  return json({ success: true, inserted }, 200, corsHeaders);
}

async function handleStats(
  env: Env,
  corsHeaders: Record<string, string>
) {
  const info = await env.VECTOR_INDEX.describe();
  return json(
    {
      index: "eplan-knowledge-base",
      model: "BAAI/bge-base-en-v1.5",
      dimensions: 768,
      ...info,
    },
    200,
    corsHeaders
  );
}

function json(
  data: unknown,
  status = 200,
  extraHeaders: Record<string, string> = {}
) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json", ...extraHeaders },
  });
}
