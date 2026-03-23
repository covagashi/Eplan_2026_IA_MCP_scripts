export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;
    
    // Health check
    if (path === '/health') {
      return new Response(JSON.stringify({ status: 'ok' }), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    // MCP endpoint for tool discovery
    if (path === '/mcp') {
      return new Response(JSON.stringify({
        name: 'cloudflare-vectorize-mcp',
        version: '1.0.0',
        description: 'MCP server for Vectorize and Workers AI',
        tools: [
          {
            name: 'search',
            description: 'Search for similar vectors in the knowledge base',
            inputSchema: {
              type: 'object',
              properties: {
                query: {
                  type: 'string',
                  description: 'Search query text'
                },
                topK: {
                  type: 'number',
                  description: 'Number of results to return',
                  default: 5
                }
              },
              required: ['query']
            }
          },
          {
            name: 'add',
            description: 'Add new vectors to the knowledge base',
            inputSchema: {
              type: 'object',
              properties: {
                vectors: {
                  type: 'array',
                  description: 'Array of vectors to add',
                  items: {
                    type: 'object',
                    properties: {
                      id: { type: 'string' },
                      vector: { type: 'array', items: { type: 'number' } },
                      metadata: { type: 'object' }
                    },
                    required: ['id', 'vector', 'metadata']
                  }
                }
              },
              required: ['vectors']
            }
          }
        ]
      }), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    // MCP SSE endpoint for actual tool execution
    if (path === '/mcp/sse') {
      const encoder = new TextEncoder();
      const stream = new ReadableStream({
        async start(controller) {
          // Send tool discovery response
          const toolsResponse = JSON.stringify({
            method: 'tools/list',
            result: {
              tools: [
                {
                  name: 'search',
                  description: 'Search for similar vectors in the knowledge base',
                  inputSchema: {
                    type: 'object',
                    properties: {
                      query: { type: 'string' },
                      topK: { type: 'number', default: 5 }
                    },
                    required: ['query']
                  }
                },
                {
                  name: 'add',
                  description: 'Add new vectors to the knowledge base',
                  inputSchema: {
                    type: 'object',
                    properties: {
                      vectors: {
                        type: 'array',
                        items: {
                          type: 'object',
                          properties: {
                            id: { type: 'string' },
                            vector: { type: 'array', items: { type: 'number' } },
                            metadata: { type: 'object' }
                          },
                          required: ['id', 'vector', 'metadata']
                        }
                      }
                    },
                    required: ['vectors']
                  }
                }
              ]
            }
          });
          controller.enqueue(encoder.encode('data: ' + toolsResponse + '\n\n'));
          controller.close();
        }
      });
      
      return new Response(stream, {
        headers: {
          'Content-Type': 'text/event-stream',
          'Cache-Control': 'no-cache',
          'Connection': 'keep-alive'
        }
      });
    }
    
    // Add vectors endpoint
    if (path === '/add-vectors' && request.method === 'POST') {
      const data = await request.json();
      const vectors = data.vectors || [];
      
      for (const vector of vectors) {
        await env.VECTOR_INDEX.insert({
          id: vector.id,
          vector: vector.vector,
          metadata: vector.metadata
        });
      }
      
      return new Response(JSON.stringify({ 
        success: true, 
        count: vectors.length 
      }), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    // Search endpoint
    if (path === '/search' && request.method === 'POST') {
      const data = await request.json();
      const query = data.query;
      const topK = data.topK || 5;
      
      // Generate embedding using Workers AI
      const aiResponse = await env.AI.run('@cf/baai/bge-base-en-v1.5', {
        text: query
      });
      
      // Query Vectorize
      const results = await env.VECTOR_INDEX.query({
        vector: aiResponse,
        topK: topK,
        returnValues: true,
        returnMetadata: 'all'
      });
      
      return new Response(JSON.stringify({
        query,
        results: results.results.map(r => ({
          id: r.id,
          score: r.score,
          metadata: r.metadata
        }))
      }), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    return new Response('Not found', { status: 404 });
  }
};
