#!/bin/bash
# Deploy EPLAN EEC Pro RAG to Cloudflare (Workers + Vectorize)
# Run from migration/ directory (where NDJSON batches are)
set -e

echo "============================================"
echo "EEC Pro RAG -> Cloudflare Deployment"
echo "============================================"

# Step 1: Login (opens browser)
echo ""
echo "PASO 1: Login en Cloudflare"
npx wrangler login

# Step 2: Create Vectorize index
echo ""
echo "PASO 2: Crear indice Vectorize (768 dims, cosine)"
npx wrangler vectorize create eecpro-knowledge-base \
  --dimensions=768 \
  --metric=cosine \
  || echo "Index may already exist, continuing..."

# Step 3: Import vectors batch by batch
echo ""
echo "PASO 3: Importar vectores (EEC Pro batches)"
for batch_file in vectors_batch_*.ndjson; do
  if [ -f "$batch_file" ]; then
    echo "  Importing: $batch_file"
    npx wrangler vectorize insert eecpro-knowledge-base \
      --file="$batch_file" \
      --batch-size=1000
    echo "  Done: $batch_file"
  fi
done

# Step 4: Deploy Worker
echo ""
echo "PASO 4: Deploy Worker"
cd ../worker
npx wrangler deploy
cd ../migration

# Step 5: (Optional) Set API key secret
echo ""
echo "PASO 5: (Opcional) Configurar API key"
echo "Para proteger el Worker, ejecuta:"
echo "  cd ../worker && npx wrangler secret put WORKER_API_KEY"
echo ""

# Step 6: Test
echo ""
echo "PASO 6: Test"
echo "Health check:"
echo "  curl https://rageecpro.covaga.xyz/health"
echo ""
echo "Search test:"
echo "  curl -X POST https://rageecpro.covaga.xyz/search -H 'Content-Type: application/json' -d '{\"query\": \"formula expression\", \"topK\": 3}'"
echo ""
echo "Stats:"
echo "  curl https://rageecpro.covaga.xyz/stats"

echo ""
echo "============================================"
echo "DEPLOYMENT COMPLETE"
echo "============================================"
