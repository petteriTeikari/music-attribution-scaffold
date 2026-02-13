# fig-theory-17: Embedding Space Visualization

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-17 |
| **Title** | Embedding Space Visualization |
| **Audience** | L4 (AI/ML Architect) |
| **Complexity** | L4 (ML terms, vector space concepts) |
| **Location** | docs/theory/entity-resolution.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows a 2D projection of entity embeddings, illustrating how name variants for the same entity cluster together in vector space while distinct entities remain separated. It answers: "How do embeddings help resolve entities when string matching fails?"

The key message is: "In embedding space, semantically equivalent name variants cluster together even when their string forms differ -- cosine distance between vectors captures meaning, not spelling."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  EMBEDDING SPACE                                               |
|  ■ Entity Clusters in Vector Space                             |
+---------------------------------------------------------------+
|                                                                |
|  2D Projection (t-SNE / UMAP)                                 |
|  ─────────────────────────────                                 |
|                                                                |
|        ●₁ "Imogen Heap"                                       |
|           ●₂ "I. Heap"              ▲₁ "Brian Eno"            |
|        ●₃ "HEAP, IMOGEN"               ▲₂ "Eno, Brian"       |
|     ●₄ "Imogen J. Heap"             ▲₃ "B. Eno"              |
|                                                                |
|     ┌─────────────────┐          ┌─────────────────┐          |
|     │ Cluster A        │          │ Cluster B        │          |
|     │ cosine dist < 0.1│          │ cosine dist < 0.1│          |
|     └─────────────────┘          └─────────────────┘          |
|                                                                |
|                                        ◆₁ "Bjork"             |
|              d = 0.85                     ◆₂ "Bjork           |
|         ◄──────────────►                   Gudmundsdottir"    |
|         (between clusters)             ◆₃ "bjork"             |
|                                                                |
|                                  ┌─────────────────┐          |
|                                  │ Cluster C        │          |
|                                  │ cosine dist < 0.1│          |
|                                  └─────────────────┘          |
|                                                                |
+---------------------------------------------------------------+
|                                                                |
|  KEY PROPERTIES                                                |
|  ──────────────                                                |
|                                                                |
|  ■ Within-cluster distance:  cosine < 0.1  (same entity)      |
|  ■ Between-cluster distance: cosine > 0.7  (different entity) |
|  ■ Ambiguous zone:           0.1 < cosine < 0.7 (escalate     |
|    to LLM or Splink)                                           |
|                                                                |
|  Embedding model: sentence-transformers or similar             |
|  Dimensionality: 384-768 → projected to 2D for visualization  |
|                                                                |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "EMBEDDING SPACE" with coral accent square |
| Subtitle | `label_editorial` | "Entity Clusters in Vector Space" |
| Cluster A points | `source_artist` | Four dots: "Imogen Heap," "I. Heap," "HEAP, IMOGEN," "Imogen J. Heap" |
| Cluster B points | `source_artist` | Three dots: "Brian Eno," "Eno, Brian," "B. Eno" |
| Cluster C points | `source_artist` | Three dots: "Bjork," "Bjork Gudmundsdottir," "bjork" |
| Cluster boundaries | `entity_resolve` | Dashed ellipses around each cluster |
| Within-cluster distance annotation | `data_mono` | "cosine dist < 0.1" label per cluster |
| Between-cluster distance | `data_mono` | "d = 0.85" double-headed arrow between clusters |
| Key properties section | `callout_box` | Three distance zones: within (<0.1), between (>0.7), ambiguous (0.1-0.7) |
| Dimensionality note | `data_mono` | "384-768 -> projected to 2D" |
| Projection method note | `label_editorial` | "t-SNE / UMAP" as projection method |

## Anti-Hallucination Rules

1. Distance thresholds (0.1 within, 0.7 between) are ILLUSTRATIVE -- do NOT present as tuned hyperparameters.
2. The ambiguous zone (0.1-0.7) explicitly escalates to LLM or Splink -- do NOT claim embeddings solve everything.
3. Artist examples: Imogen Heap, Brian Eno, Bjork -- these are real artists chosen for name variation diversity.
4. The projection is 2D (t-SNE or UMAP) from 384-768 dimensional space -- do NOT claim the 2D view is the actual space.
5. Do NOT specify a particular embedding model name -- say "sentence-transformers or similar."
6. Cosine DISTANCE (not similarity) is used -- distance = 1 - similarity. Small distance = more similar.
7. Do NOT show audio embeddings or music content embeddings -- these are NAME/TEXT embeddings for entity resolution.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

2D projection of entity embeddings showing three tight clusters for Imogen Heap, Brian Eno, and Bjork name variants, with within-cluster cosine distance below 0.1 and between-cluster distance above 0.7.
