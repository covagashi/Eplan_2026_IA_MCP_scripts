#!/bin/bash
# Deploy EPLAN RAG to Cloudflare (Workers + Vectorize)
# Run from temp/output/ directory
set -e

echo "============================================"
echo "EPLAN RAG -> Cloudflare Deployment"
echo "============================================"

# Step 1: Login (opens browser)
echo ""
echo "STEP 1: Cloudflare login"
npx wrangler login

# Step 2: Create Vectorize index
echo ""
echo "STEP 2: Create Vectorize index (768 dims, cosine)"
npx wrangler vectorize create eplan-knowledge-base \
  --dimensions=768 \
  --metric=cosine \
  || echo "Index may already exist, continuing..."

# Step 3: Import vectors batch by batch
echo ""
echo "STEP 3: Import vectors (57,492 vectors in 12 batches)"
for batch_file in vectors_batch_*.ndjson; do
  echo "  Importing: $batch_file"
  npx wrangler vectorize insert eplan-knowledge-base \
    --file="$batch_file" \
    --batch-size=1000
  echo "  Done: $batch_file"
done

# Step 4: Deploy Worker
echo ""
echo "STEP 4: Deploy Worker"
npx wrangler deploy

# Step 5: (Optional) Set API key secret
echo ""
echo "STEP 5: (Optional) Configure API key"
echo "To protect the Worker, run:"
echo "  npx wrangler secret put WORKER_API_KEY"
echo ""

# Step 6: Test
echo ""
echo "STEP 6: Test"
WORKER_URL=$(npx wrangler whoami 2>/dev/null | grep -oP 'https://[^\s]+' || echo "https://eplan-rag-mcp.<YOUR_SUBDOMAIN>.workers.dev")
echo "Health check:"
echo "  curl $WORKER_URL/health"
echo ""
echo "Search test:"
echo "  curl -X POST $WORKER_URL/search -H 'Content-Type: application/json' -d '{\"query\": \"export project\", \"topK\": 3}'"
echo ""
echo "Stats:"
echo "  curl $WORKER_URL/stats"

echo ""
echo "============================================"
echo "DEPLOYMENT COMPLETE"
echo "============================================"
