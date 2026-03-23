const fs = require('fs');
const { exec } = require('child_process');
const path = require('path');

async function importToVectorize() {
  // Configuración
  const VECTORIZE_INDEX_NAME = 'ai-knowledge-base'; // Actualizado para usar el nombre del índice recién creado
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
          exec(
            `npx wrangler vectorize insert ${VECTORIZE_INDEX_NAME} --file=${batchPath}`,
            (error, stdout, stderr) => {
              if (error) {
                console.error(stderr);
                reject(error);
              } else {
                console.log(stdout);
                resolve();
              }
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
}

importToVectorize().catch(console.error);
