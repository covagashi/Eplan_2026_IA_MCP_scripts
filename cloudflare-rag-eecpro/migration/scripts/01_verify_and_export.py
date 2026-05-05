"""
Verify EEC Pro ChromaDB RAG data integrity, then export embeddings + metadata
as NDJSON batches for Cloudflare Vectorize migration.

Source: eplan-eecpro-rag-builder/rag_db_llama_chroma (LlamaIndex + ChromaDB)
Target: Cloudflare Vectorize index 'eecpro-knowledge-base'
"""
import chromadb
import json
import os
import sys
import time
import numpy as np

# --- Config ---
CHROMA_DB_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "..",
    "eplan-eecpro-rag-builder", "rag_db_llama_chroma"
)
COLLECTION_NAME = "eplan_docs"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..")
BATCH_SIZE = 5000  # ChromaDB get() batch size


def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def main():
    print("=" * 60)
    print("STEP 1: Verify ChromaDB RAG (EEC Pro)")
    print("=" * 60)

    db_path = os.path.abspath(CHROMA_DB_PATH)
    print(f"DB path: {db_path}")

    if not os.path.exists(db_path):
        print(f"ERROR: Path does not exist: {db_path}")
        sys.exit(1)

    client = chromadb.PersistentClient(path=db_path)
    collections = client.list_collections()
    print(f"Collections: {[c.name for c in collections]}")

    collection = client.get_collection(COLLECTION_NAME)
    total = collection.count()
    print(f"'{COLLECTION_NAME}': {total} embeddings")

    # --- Verify data integrity ---
    print("\n--- Data verification ---")
    sample = collection.get(
        limit=5,
        include=["embeddings", "metadatas", "documents"],
    )

    dims = len(sample["embeddings"][0]) if sample["embeddings"] is not None and len(sample["embeddings"]) > 0 else 0
    print(f"Dimensions: {dims}")
    assert dims == 768, f"Expected 768 dims, got {dims}"

    print(f"Sample IDs: {sample['ids'][:3]}")
    for i in range(min(3, len(sample["ids"]))):
        meta = sample["metadatas"][i] if sample["metadatas"] else {}
        doc = sample["documents"][i] if sample["documents"] else ""
        title = meta.get("title", meta.get("source", "?"))
        emb_norm = np.linalg.norm(sample["embeddings"][i])
        print(f"  {i+1}. {title}")
        print(f"     meta keys: {list(meta.keys())}")
        print(f"     doc length: {len(doc)} chars")
        print(f"     embedding norm: {emb_norm:.4f}")

    # Manual similarity test between first two embeddings
    if len(sample["embeddings"]) >= 2:
        sim = cosine_similarity(sample["embeddings"][0], sample["embeddings"][1])
        print(f"\nCosine sim (sample 0 vs 1): {sim:.4f}")

    # Check for zero/nan embeddings
    zero_count = 0
    nan_count = 0
    check_batch = collection.get(limit=100, include=["embeddings"])
    for emb in check_batch["embeddings"]:
        if all(v == 0 for v in emb):
            zero_count += 1
        if any(np.isnan(v) for v in emb):
            nan_count += 1
    print(f"Zero embeddings (of 100): {zero_count}")
    print(f"NaN embeddings (of 100): {nan_count}")

    if zero_count > 10 or nan_count > 0:
        print("WARNING: Data quality issues detected!")

    print("\nData verification OK")

    # --- Export ---
    print("\n" + "=" * 60)
    print("STEP 2: Export for Cloudflare Vectorize (EEC Pro)")
    print("=" * 60)

    batch_num = 0
    exported = 0
    offset = 0
    t_start = time.time()

    while offset < total:
        batch = collection.get(
            include=["embeddings", "metadatas", "documents"],
            limit=BATCH_SIZE,
            offset=offset,
        )

        ids = batch["ids"]
        embeddings = batch["embeddings"]
        metadatas = batch["metadatas"]
        documents = batch["documents"]

        if not ids:
            break

        # Build NDJSON file for this batch
        # Vectorize format: {"id": str, "values": [float], "metadata": {}}
        batch_file = os.path.join(OUTPUT_DIR, f"vectors_batch_{batch_num:04d}.ndjson")
        with open(batch_file, "w", encoding="utf-8") as f:
            for i, vec_id in enumerate(ids):
                meta = metadatas[i] if metadatas else {}
                doc = documents[i] if documents else ""

                # Keep metadata lean for Vectorize (max 40KB per vector)
                # EEC Pro metadata keys differ from P8:
                #   title, source, category, file, header_path, parent_id
                clean_meta = {}
                if meta:
                    for k in ["title", "source", "source_url", "category",
                              "file", "header_path", "parent_id"]:
                        if k in meta:
                            clean_meta[k] = str(meta[k])[:500]

                # Store first 1000 chars of content in metadata
                if doc:
                    clean_meta["content"] = doc[:1000]

                # Convert numpy array to list for JSON serialization
                values = embeddings[i]
                if hasattr(values, "tolist"):
                    values = values.tolist()

                record = {
                    "id": vec_id,
                    "values": values,
                    "metadata": clean_meta,
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

        exported += len(ids)
        batch_num += 1
        offset += BATCH_SIZE
        elapsed = time.time() - t_start
        print(f"  Batch {batch_num}: {len(ids)} vectors -> {os.path.basename(batch_file)} "
              f"({exported}/{total}) [{elapsed:.1f}s]")

    elapsed = time.time() - t_start
    print(f"\nExported: {exported} vectors in {batch_num} batches ({elapsed:.1f}s)")
    print(f"Output dir: {OUTPUT_DIR}")

    # Write manifest
    manifest = {
        "source": "eplan-eecpro-rag-builder/rag_db_llama_chroma",
        "collection": COLLECTION_NAME,
        "total_vectors": exported,
        "dimensions": 768,
        "model": "BAAI/bge-base-en-v1.5",
        "metric": "cosine",
        "batches": batch_num,
        "batch_size": BATCH_SIZE,
        "exported_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "vectorize_index_name": "eecpro-knowledge-base",
    }
    manifest_path = os.path.join(OUTPUT_DIR, "manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"Manifest: {manifest_path}")
    print("\nDone!")


if __name__ == "__main__":
    main()
