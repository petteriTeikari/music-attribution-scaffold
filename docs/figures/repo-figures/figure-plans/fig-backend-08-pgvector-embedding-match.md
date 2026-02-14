# fig-backend-08: pgvector Embedding Match

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-08 |
| **Title** | Embedding-Based Semantic Match: sentence-transformers + pgvector |
| **Audience** | L4 (AI/ML Architect) |
| **Complexity** | L4 |
| **Location** | docs/architecture/, docs/resolution/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows how entity names and metadata are embedded into dense vector space using sentence-transformers, stored in PostgreSQL via pgvector (HALFVEC), and queried via cosine similarity for semantic entity resolution. It covers cases where string matching fails: translations, very different spellings, or alias variations.

The key message is: "When string similarity fails, semantic embeddings catch what text matching misses -- entities that mean the same thing but look completely different. The all-MiniLM-L6-v2 model embeds names into 768-dimensional HALFVEC vectors stored in pgvector for efficient nearest-neighbor search."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  EMBEDDING-BASED SEMANTIC MATCH                                |
|  ■ sentence-transformers + pgvector HALFVEC(768)               |
+---------------------------------------------------------------+
|                                                                 |
|  EMBEDDING PIPELINE                                            |
|  ──────────────────                                            |
|                                                                 |
|  Entity Name ──> SentenceTransformer ──> 768-dim vector        |
|  "Tchaikovsky"   (all-MiniLM-L6-v2)    [0.12, -0.34, ...]     |
|                                                                 |
|              ┌──────────────────────────────┐                  |
|              │     VECTOR SPACE              │                  |
|              │                               │                  |
|              │     * "Tchaikovsky"           │                  |
|              │    *  "Chaikovsky"            │                  |
|              │   *   "Tschaikowski"          │ cosine           |
|              │                               │ similarity       |
|              │              * "Mozart"       │                  |
|              │             * "W.A. Mozart"   │                  |
|              │                               │                  |
|              │  * "Imogen Heap"              │                  |
|              │  * "iMegaphone" (alias)       │                  |
|              └──────────────────────────────┘                  |
|                                                                 |
|  STORAGE: PostgreSQL                                           |
|  ───────────────────                                           |
|  entity_embeddings table                                       |
|  ┌──────────────┬────────────┬──────────────┬────────────┐    |
|  │ embedding_id │ entity_id  │ model_name   │ embedding  │    |
|  │ UUID         │ UUID (FK)  │ varchar(255) │ HALFVEC    │    |
|  │              │            │              │ (768)      │    |
|  └──────────────┴────────────┴──────────────┴────────────┘    |
|                                                                 |
|  SIMILARITY: cosine_sim(a, b) = (a . b) / (|a| * |b|)         |
|  Weight in orchestrator: 0.7                                    |
|                                                                 |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "EMBEDDING-BASED SEMANTIC MATCH" |
| Embedding pipeline | `processing_stage` | Entity name to vector via SentenceTransformer |
| Model identifier | `data_mono` | "all-MiniLM-L6-v2" model name |
| Vector space visualization | `entity_resolve` | 2D projection showing similar names clustered together |
| PostgreSQL storage | `storage_layer` | entity_embeddings table with HALFVEC(768) column |
| Table schema | `data_mono` | Column names and types in monospace |
| Cosine similarity formula | `final_score` | Mathematical formula for similarity computation |
| Orchestrator weight | `data_mono` | "Weight: 0.7" from orchestrator config |
| Vector dimension | `data_mono` | "768-dim" vector size |
| HALFVEC type | `data_mono` | PostgreSQL pgvector half-precision storage |

## Anti-Hallucination Rules

1. The model is all-MiniLM-L6-v2, the default in EmbeddingMatcher.__init__. Do not use a different model.
2. Vector dimension is 768 (HALFVEC(768) from EntityEmbeddingModel).
3. Storage uses HALFVEC (half-precision), not VECTOR (full-precision). This is explicitly in the ORM model.
4. The cosine similarity is computed manually in the code (dot product / norms), not via pgvector operator.
5. The orchestrator weight for embedding is 0.7, from _DEFAULT_WEIGHTS.
6. The EmbeddingMatcher class supports both in-memory storage and pgvector. The in-memory dict is used for testing.
7. The sentence-transformers library is lazy-loaded (imported only when needed, with ImportError handling).
8. The table has a unique constraint on (entity_id, model_name).

## Alt Text

Architecture diagram of semantic embedding-based entity resolution for music attribution, showing entity names encoded by the all-MiniLM-L6-v2 sentence-transformer model into 768-dimensional vectors, stored in PostgreSQL pgvector HALFVEC columns, with cosine similarity search catching translations and alias variations that string matching misses — weighted at 0.7 in the open-source attribution scaffold's confidence scoring pipeline.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture diagram of semantic embedding-based entity resolution for music attribution, showing entity names encoded by the all-MiniLM-L6-v2 sentence-transformer model into 768-dimensional vectors, stored in PostgreSQL pgvector HALFVEC columns, with cosine similarity search catching translations and alias variations that string matching misses — weighted at 0.7 in the open-source attribution scaffold's confidence scoring pipeline.](docs/figures/repo-figures/assets/fig-backend-08-pgvector-embedding-match.jpg)

*Figure 8. When string similarity fails for translated or heavily aliased music entity names, semantic embeddings in pgvector HALFVEC(768) capture meaning-level similarity, enabling the attribution scaffold to resolve entities like "Tchaikovsky" and "Tschaikowski" that look different but refer to the same person.*

### From this figure plan (relative)

![Architecture diagram of semantic embedding-based entity resolution for music attribution, showing entity names encoded by the all-MiniLM-L6-v2 sentence-transformer model into 768-dimensional vectors, stored in PostgreSQL pgvector HALFVEC columns, with cosine similarity search catching translations and alias variations that string matching misses — weighted at 0.7 in the open-source attribution scaffold's confidence scoring pipeline.](../assets/fig-backend-08-pgvector-embedding-match.jpg)
