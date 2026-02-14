# fig-backend-18: Hybrid Search Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-18 |
| **Title** | Hybrid Search: Text + Vector + Graph with Reciprocal Rank Fusion |
| **Audience** | L4 (AI/ML Architect) |
| **Complexity** | L4 |
| **Location** | docs/architecture/, docs/search/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the three-modality hybrid search system that combines full-text search, vector similarity search, and graph context via Reciprocal Rank Fusion (RRF). It illustrates how each modality produces independent rankings that are fused into a single result list.

The key message is: "Hybrid search combines three complementary signals -- text matching for exact keywords, vector similarity for semantic meaning, and graph neighbors for contextual relationships -- fused with RRF at k=60 to produce ranked attribution results."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  HYBRID SEARCH ARCHITECTURE                                    |
|  ■ Three Modalities + Reciprocal Rank Fusion                  |
+---------------------------------------------------------------+
|                                                                 |
|  Query: "Imogen Heap producer credits"                         |
|           │                                                     |
|           ├──────────────────┬──────────────────┐              |
|           ▼                  ▼                  ▼              |
|  ┌────────────────┐ ┌────────────────┐ ┌────────────────┐     |
|  │ MODALITY 1     │ │ MODALITY 2     │ │ MODALITY 3     │     |
|  │ Text Search    │ │ Vector Search  │ │ Graph Context  │     |
|  │────────────────│ │────────────────│ │────────────────│     |
|  │ LIKE on JSONB  │ │ Embed query    │ │ 1-hop neighbors│     |
|  │ fields (work_  │ │ via sentence-  │ │ of vector      │     |
|  │ title, artist_ │ │ transformers   │ │ matches via    │     |
|  │ name, credits) │ │ Cosine sim vs  │ │ edges table    │     |
|  │                │ │ entity_embed-  │ │                │     |
|  │ TextSearchSvc  │ │ dings table    │ │ EdgeModel      │     |
|  └───────┬────────┘ └───────┬────────┘ └───────┬────────┘     |
|          │                  │                  │               |
|   Rank: A1=1, A3=2,  Rank: A2=1, A1=2,  Rank: A3=1, A5=2,   |
|          A5=3               A4=3               A1=3            |
|          │                  │                  │               |
|          └──────────────────┼──────────────────┘               |
|                             ▼                                  |
|  ┌──────────────────────────────────────────────────┐         |
|  │ RECIPROCAL RANK FUSION (RRF)                      │         |
|  │ score(d) = Σ 1/(k + rank_i)    where k = 60      │         |
|  │                                                    │         |
|  │ A1: 1/(60+1) + 1/(60+2) + 1/(60+3) = 0.0488     │         |
|  │ A3: 1/(60+2) + 0       + 1/(60+1) = 0.0325      │         |
|  │ A2: 0        + 1/(60+1) + 0       = 0.0164      │         |
|  │                                                    │         |
|  │ Final: A1 (0.0488), A3 (0.0325), A2 (0.0164)...  │         |
|  └──────────────────────────────────────────────────┘         |
|                             ▼                                  |
|  ┌──────────────────────────────────────────────────┐         |
|  │ Output: [HybridSearchResult(record, rrf_score)]   │         |
|  │ Sorted by rrf_score descending                    │         |
|  └──────────────────────────────────────────────────┘         |
|                                                                 |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "HYBRID SEARCH ARCHITECTURE" |
| Query input | `processing_stage` | Example search query |
| Text Search modality | `processing_stage` | LIKE matching on JSONB fields |
| Vector Search modality | `entity_resolve` | Sentence-transformer embedding + cosine similarity |
| Graph Context modality | `processing_stage` | 1-hop edge neighbors of vector matches |
| Per-modality rankings | `data_mono` | Independent rank lists in monospace |
| RRF fusion box | `final_score` | Mathematical formula: 1/(k + rank_i) with k=60 |
| Worked example | `data_mono` | Arithmetic showing RRF score computation |
| Output | `primary_outcome` | HybridSearchResult with record + rrf_score |
| Three-way split arrows | `data_flow` | Query splitting into three modalities |
| Convergence arrow | `data_flow` | Three modalities merging at RRF |

## Anti-Hallucination Rules

1. The RRF constant k is exactly 60 (RRF_K = 60 in hybrid_search.py).
2. The three modalities are: text search (LIKE on JSONB), vector similarity (sentence-transformers + pgvector), and graph context (1-hop edge neighbors).
3. Text search uses TextSearchService. Vector search embeds the query and compares against entity_embeddings table.
4. Graph context finds 1-hop neighbors via EdgeModel, then maps entity IDs to attribution IDs.
5. Entity-to-attribution mapping checks both work_entity_id and credits JSONB (via LIKE on cast to String).
6. The RRF formula is: score(d) = sum(1 / (k + rank_i)) across all modalities where the document appears.
7. The output is HybridSearchResult (a NamedTuple with record and rrf_score).
8. The service class is HybridSearchService in `music_attribution.search.hybrid_search`.
9. Vector search limits results to `limit` and text search to `limit * 2` (for better recall before fusion).

## Alt Text

Architecture diagram of the hybrid search system for the music attribution scaffold, combining three modalities — full-text LIKE search on music metadata fields, vector similarity via sentence-transformers and pgvector embeddings, and graph context from 1-hop entity relationships — fused with Reciprocal Rank Fusion (RRF, k=60) into a single ranked result list for comprehensive open-source music credit discovery.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture diagram of the hybrid search system for the music attribution scaffold, combining three modalities — full-text LIKE search on music metadata fields, vector similarity via sentence-transformers and pgvector embeddings, and graph context from 1-hop entity relationships — fused with Reciprocal Rank Fusion (RRF, k=60) into a single ranked result list for comprehensive open-source music credit discovery.](docs/figures/repo-figures/assets/fig-backend-18-hybrid-search-architecture.jpg)

*Figure 18. Hybrid search combines three complementary signals — text matching for exact keywords, vector similarity for semantic meaning, and graph neighbors for contextual relationships — ensuring that attribution records are discoverable through any search modality.*

### From this figure plan (relative)

![Architecture diagram of the hybrid search system for the music attribution scaffold, combining three modalities — full-text LIKE search on music metadata fields, vector similarity via sentence-transformers and pgvector embeddings, and graph context from 1-hop entity relationships — fused with Reciprocal Rank Fusion (RRF, k=60) into a single ranked result list for comprehensive open-source music credit discovery.](../assets/fig-backend-18-hybrid-search-architecture.jpg)
