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
