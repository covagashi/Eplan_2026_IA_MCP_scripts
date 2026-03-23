**Cloudflare Vectorize** is a globally distributed vector database that lets you build AI-powered applications with Cloudflare Workers.


**What it does:**
- **Vector similarity search** - Find the most similar vectors (embeddings) from your data
- **Metadata filtering** - Filter results based on metadata fields
- **High performance** - Low-latency queries across Cloudflare's global network
- **Large scale** - Supports up to 5 million vector dimensions (v2 beta)

**Common use cases:**
- Semantic search and RAG applications
- Recommendations and content discovery
- Anomaly detection
- LLM context retrieval

**Quick start:**

1. Create Vectorize Index
Run this command in your terminal:

```
npx wrangler vectorize create ai-knowledge-base --dimensions=768 --metric=cosine

```

This creates a Vectorize index with 768 dimensions (standard for BGE embeddings) using cosine similarity.

2. Create Worker Script
Create a file named worker.js with this code:

´´´
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

´´´

3. Create Wrangler Configuration
Create a file named wrangler.toml:

´´´
name = "ai-vectorize-mcp"
main = "worker.js"
compatibility_date = "2026-03-23"

[ai]
binding = "AI"

[vectorize]
binding = "VECTOR_INDEX"
index_name = "ai-knowledge-base"

´´´

4. Deploy the Worker

npx wrangler deploy


5. Test the Setup
Test Health Check:

curl https://ai-vectorize-mcp.5fd07f46b629b20c52e79cfbcf28155e.workers.dev/health

Test MCP Discovery:

curl https://ai-vectorize-mcp.5fd07f46b629b20c52e79cfbcf28155e.workers.dev/mcp

Add Some Vectors:

```
curl -X POST https://ai-vectorize-mcp.<ACCOUNT_ID>.workers.dev/add-vectors \
  -H "Content-Type: application/json" \
  -d '{
    "vectors": [
      {
        "id": "doc1",
        "vector": [0.1, 0.2, 0.3, 0.4, 0.5],
        "metadata": {
          "title": "Introduction to AI",
          "category": "learning"
        }
      }
    ]
  }'

```

Search:

```
curl -X POST https://ai-vectorize-mcp.<ACCOUNT_ID>.workers.dev/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is artificial intelligence?",
    "topK": 5
  }'

```
Dashboard Links
Vectorize Index: https://dash.cloudflare.com/5fd07f46b629b20c52e79cfbcf28155e/vectorize/indexes/ai-knowledge-base
Worker: https://dash.cloudflare.com/5fd07f46b629b20c52e79cfbcf28155e/workers/scripts/ai-vectorize-mcp


Aquí tienes el script completo de migración para tu setup específico:

Paso 1: Exportar de ChromaDB
Crea un archivo migrate-chroma-to-vectorize.js:

```
// migrate-chroma-to-vectorize.js
const fs = require('fs');
const path = require('path');

// Configuración de ChromaDB
const COLLECTIONS = [
  {
    name: 'eplan_docs',
    dbDir: 'rag_db_llama_chroma',
    outputPath: 'eplan_docs_vectors.json'
  },
  {
    name: 'rag_db_llama_chroma',
    dbDir: 'rag_db_llama_chroma',
    outputPath: 'rag_db_llama_chroma_vectors.json'
  }
];

// Dimensión del modelo BAAI/bge-base-en-v1.5
const DIMENSIONS = 768;

function exportCollection(collection) {
  console.log(`\n📦 Exportando colección: ${collection.name}`);
  console.log(`📁 Base de datos: ${collection.dbDir}`);
  
  // Buscar archivos ChromaDB
  const dbDir = path.join(process.cwd(), collection.dbDir);
  
  if (!fs.existsSync(dbDir)) {
    console.log(`⚠️  Directorio no encontrado: ${dbDir}`);
    return { collection: collection.name, count: 0, vectors: [] };
  }
  
  // Buscar archivos .parquet o .json en el directorio
  const files = fs.readdirSync(dbDir).filter(f => f.endsWith('.parquet') || f.endsWith('.json'));
  
  if (files.length === 0) {
    console.log(`⚠️  No se encontraron archivos .parquet o .json en ${dbDir}`);
    return { collection: collection.name, count: 0, vectors: [] };
  }
  
  let allVectors = [];
  
  for (const file of files) {
    const filePath = path.join(dbDir, file);
    console.log(`📄 Procesando: ${file}`);
    
    try {
      // Intentar leer como JSON
      if (file.endsWith('.json')) {
        const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
        const vectors = extractVectorsFromJSON(data, collection.name, file);
        allVectors.push(...vectors);
        console.log(`   ✓ Importadas ${vectors.length} vectores`);
      }
      // Intentar leer como Parquet (requiere librería)
      else if (file.endsWith('.parquet')) {
        console.log(`   ⚠️  Archivo Parquet detectado. Necesitarás instalar la librería: npm install @parquetjs/parquet`);
        // Aquí podrías agregar lógica para leer Parquet
      }
    } catch (error) {
      console.log(`   ✗ Error leyendo ${file}: ${error.message}`);
    }
  }
  
  // Guardar vectores exportados
  const outputPath = path.join(process.cwd(), collection.outputPath);
  fs.writeFileSync(outputPath, JSON.stringify(allVectors, null, 2));
  
  console.log(`\n✅ Colección ${collection.name} exportada a: ${outputPath}`);
  console.log(`📊 Total: ${allVectors.length} vectores con ${DIMENSIONS} dimensiones`);
  
  return { collection: collection.name, count: allVectors.length, vectors: allVectors };
}

function extractVectorsFromJSON(data, collectionName, fileName) {
  const vectors = [];
  
  // Intentar diferentes formatos de ChromaDB
  
  // Formato 1: ChromaDB con metadatos y documentos
  if (data.embeddings && data.documents) {
    data.embeddings.forEach((embedding, idx) => {
      vectors.push({
        id: `${collectionName}_${fileName}_${idx}`,
        vector: embedding,
        metadata: {
          content: data.documents[idx] || '',
          source: collectionName,
          filename: fileName,
          chunk_index: idx,
          embedding_model: 'BAAI/bge-base-en-v1.5',
          chunk_size: 512,
          chunk_overlap: 64
        }
      });
    });
  }
  // Formato 2: Array de embeddings directo
  else if (Array.isArray(data)) {
    data.forEach((embedding, idx) => {
      vectors.push({
        id: `${collectionName}_${fileName}_${idx}`,
        vector: embedding,
        metadata: {
          content: '',
          source: collectionName,
          filename: fileName,
          chunk_index: idx,
          embedding_model: 'BAAI/bge-base-en-v1.5',
          chunk_size: 512,
          chunk_overlap: 64
        }
      });
    });
  }
  // Formato 3: ChromaDB con metadatos
  else if (data && data.vectors) {
    Object.entries(data.vectors).forEach(([id, embedding]) => {
      vectors.push({
        id,
        vector: embedding.values || embedding,
        metadata: {
          ...data.metadatas?.[id],
          source: collectionName,
          filename: fileName,
          embedding_model: 'BAAI/bge-base-en-v1.5',
          chunk_size: 512,
          chunk_overlap: 64
        }
      });
    });
  }
  
  return vectors;
}

async function main() {
  console.log('🚀 Iniciando migración de ChromaDB a Vectorize');
  console.log(`📐 Dimensión: ${DIMENSIONS} (BAAI/bge-base-en-v1.5)\n`);
  
  const results = [];
  
  for (const collection of COLLECTIONS) {
    const result = exportCollection(collection);
    results.push(result);
  }
  
  // Resumen
  console.log('\n' + '='.repeat(60));
  console.log('📊 RESUMEN DE MIGRACIÓN');
  console.log('='.repeat(60));
  
  let totalVectors = 0;
  results.forEach(r => {
    console.log(`\n📦 ${r.collection}: ${r.count} vectores`);
    totalVectors += r.count;
  });
  
  console.log(`\n${'='.repeat(60)}`);
  console.log(`✅ TOTAL: ${totalVectors} vectores exportados`);
  console.log(`${'='.repeat(60)}\n`);
  
  console.log('📝 Próximos pasos:');
  console.log('1. Crear índice Vectorize: npx wrangler vectorize create mi-datos --dimensions=768 --metric=cosine');
  console.log('2. Importar vectores: node import-to-vectorize.js');
}

main().catch(console.error);
```

Ejecuta la exportación:

node migrate-chroma-to-vectorize.js


Paso 2: Crear Índice Vectorize

npx wrangler vectorize create mi-datos --dimensions=768 --metric=cosine


Paso 3: Importar a Vectorize
Crea import-to-vectorize.js:

```
// import-to-vectorize.js
const fs = require('fs');
const path = require('child_process');

async function importToVectorize() {
  // Configuración
  const VECTORIZE_INDEX_NAME = 'mi-datos';
  const BATCH_SIZE = 1000;
  
  // Buscar archivos de vectores exportados
  const vectorFiles = fs.readdirSync(process.cwd())
    .filter(f => f.endsWith('_vectors.json'));
  
  if (vectorFiles.length === 0) {
    console.error('❌ No se encontraron archivos de vectores exportados');
    return;
  }
  
  console.log(`📁 Archivos de vectores encontrados: ${vectorFiles.length}\n`);
  
  let totalImported = 0;
  
  for (const vectorFile of vectorFiles) {
    console.log(`\n📦 Importando: ${vectorFile}`);
    
    const vectors = JSON.parse(fs.readFileSync(vectorFile, 'utf-8'));
    console.log(`📊 Vectores en archivo: ${vectors.length}`);
    
    // Importar en lotes
    for (let i = 0; i < vectors.length; i += BATCH_SIZE) {
      const batch = vectors.slice(i, i + BATCH_SIZE);
      const batchNum = Math.floor(i / BATCH_SIZE) + 1;
      const totalBatches = Math.ceil(vectors.length / BATCH_SIZE);
      
      console.log(`   🔄 Lote ${batchNum}/${totalBatches} (${batch.length} vectores)...`);
      
      // Crear archivo de lote
      const batchPath = path.join(process.cwd(), `batch-${i}.json`);
      fs.writeFileSync(batchPath, JSON.stringify({ vectors: batch }));
      
      try {
        // Importar usando wrangler
        await new Promise((resolve, reject) => {
          const child = path.exec(
            `npx wrangler vectorize insert ${VECTORIZE_INDEX_NAME} --file=${batchPath}`,
            { stdio: 'inherit' },
            (error) => {
              if (error) reject(error);
              else resolve();
            }
          );
        });
        
        // Limpiar archivo temporal
        fs.unlinkSync(batchPath);
        
        console.log(`   ✅ Lote ${batchNum} completado`);
        
      } catch (error) {
        console.error(`   ❌ Error en lote ${batchNum}:`, error.message);
        fs.unlinkSync(batchPath);
      }
    }
    
    totalImported += vectors.length;
    console.log(`✅ Archivo ${vectorFile} completado: ${vectors.length} vectores`);
  }
  
  console.log(`\n${'='.repeat(60)}`);
  console.log(`✅ MIGRACIÓN COMPLETADA`);
  console.log(`📊 Total importado: ${totalImported} vectores`);
  console.log(`${'='.repeat(60)}\n`);
  
  console.log('🔗 Link al índice:');
  console.log(`https://dash.cloudflare.com/5fd07f46b629b20c52e79cfbcf28155e/vectorize/indexes/${VECTORIZE_INDEX_NAME}`);
}

importToVectorize().catch(console.error);
``_

```

Ejecuta la importación:

node import-to-vectorize.js

Dashboard Links
Índice Vectorize: https://dash.cloudflare.com/5fd07f46b629b20c52e79cfbcf28155e/vectorize/indexes/mi-datos

Prueba la Migración
Una vez importado, prueba con tu Worker:

```
curl -X POST https://ai-vectorize-mcp.<ACCOUNT_ID>.workers.dev/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "documentación sobre planificación de proyectos",
    "topK": 5
  }'
```
Notas Importantes
Formato de ChromaDB: Si tus archivos tienen un formato diferente, necesitarás ajustar la función extractVectorsFromJSON

npm install @parquetjs/parquet

Metadatos: El script incluye metadatos básicos. Si necesitas más información, ajusta el objeto metadata