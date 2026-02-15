# fig-backend-06: Resolution Orchestrator Flow

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-06 |
| **Title** | Resolution Orchestrator: Multi-Signal Entity Resolution Pipeline |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/, docs/resolution/ |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the complete entity resolution pipeline orchestrated by ResolutionOrchestrator. It traces the path from input NormalizedRecords through six resolution methods to output ResolvedEntities, showing how records are grouped, scored, and flagged for review.

The key message is: "Entity resolution is a cascade -- exact identifier match first, then string similarity for unmatched records, with embedding, Splink, graph, and LLM methods available as additional signals. Each method contributes a weighted score to the final resolution confidence."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  RESOLUTION ORCHESTRATOR                                       |
|  ■ Multi-Signal Entity Resolution                              |
+---------------------------------------------------------------+
|                                                                 |
|  NormalizedRecord[]                                            |
|        │                                                        |
|        ▼                                                        |
|  ┌─────────────────────┐                                       |
|  │ STEP 1: Group by    │   Union-find on shared identifiers    |
|  │ Identifiers (exact) │   Fields: isrc, iswc, isni, mbid,    |
|  │ Weight: 1.0         │          acoustid                     |
|  └──────────┬──────────┘                                       |
|        ┌────┴────┐                                              |
|   GROUPED    UNGROUPED                                         |
|        │         │                                              |
|        │         ▼                                              |
|        │  ┌─────────────────────┐                              |
|        │  │ STEP 2: String      │  Jaro-Winkler + token_sort   |
|        │  │ Similarity (fuzzy)  │  Threshold: 0.85             |
|        │  │ Weight: 0.6         │  Union-find clustering       |
|        │  └──────────┬──────────┘                              |
|        │        ┌────┴────┐                                    |
|        │   GROUPED    SINGLETONS                               |
|        │        │         │                                    |
|        └────────┼─────────┘                                    |
|                 ▼                                               |
|  ┌──────────────────────────────────────┐                      |
|  │ STEP 3: Per-Group Resolution          │                      |
|  │  ┌──────────┬───────────┬──────────┐ │  SIGNAL WEIGHTS      |
|  │  │Embedding │  Splink   │   LLM    │ │  ──────────────      |
|  │  │  0.7     │   0.8     │   0.85   │ │  identifier: 1.0    |
|  │  │(semantic)│(probabil.)│(disambig)│ │  splink: 0.8        |
|  │  └──────────┴───────────┴──────────┘ │  embedding: 0.7     |
|  │  + Graph evidence (0.75)              │  graph: 0.75        |
|  └──────────────────┬───────────────────┘  string: 0.6        |
|                     ▼                      llm: 0.85           |
|  ┌──────────────────────────────────┐                          |
|  │ Weighted Confidence = Σ(sᵢ*wᵢ)/Σwᵢ │                       |
|  │ Assurance Level: A0-A3            │                          |
|  │ Conflict Detection                │                          |
|  │ Review if confidence < 0.5        │                          |
|  └──────────────────┬───────────────┘                          |
|                     ▼                                           |
|           ┌──────────────────┐                                 |
|           │  ResolvedEntity   │                                 |
|           │     (BO-2)        │                                 |
|           └──────────────────┘                                 |
|                                                                 |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "RESOLUTION ORCHESTRATOR" |
| Input records | `etl_extract` | NormalizedRecord[] input from ETL pipeline |
| Step 1: Identifier match | `entity_resolve` | Union-find grouping on shared identifiers |
| Step 2: String similarity | `entity_resolve` | Jaro-Winkler + token_sort_ratio fuzzy matching |
| Step 3: Per-group resolution | `entity_resolve` | Additional signals: embedding, Splink, LLM, graph |
| Signal weights sidebar | `data_mono` | Six weights in monospace: 1.0, 0.8, 0.7, 0.75, 0.6, 0.85 |
| Weighted confidence formula | `final_score` | Mathematical formula for combined score |
| Review threshold | `confidence_low` | Records below 0.5 flagged for review |
| ResolvedEntity output | `primary_outcome` | BO-2 boundary object output |
| Grouped/Ungrouped branches | `data_flow` | Branching paths after each grouping step |
| Singleton handling | `processing_stage` | Remaining ungrouped records become singletons |
| Assurance level computation | `processing_stage` | A0-A3 based on sources and identifiers present |

## Anti-Hallucination Rules

1. The exact signal weights are from `_DEFAULT_WEIGHTS` in orchestrator.py: identifier=1.0, splink=0.8, string=0.6, embedding=0.7, graph=0.75, llm=0.85.
2. The review threshold is 0.5 (`_REVIEW_THRESHOLD`), not 0.85 or any other value.
3. String similarity threshold is 0.85 (from StringSimilarityMatcher default).
4. The grouping algorithm uses union-find (also known as disjoint-set), not hierarchical clustering.
5. Identifier fields checked are: isrc, iswc, isni, mbid, acoustid_fingerprint (from _group_by_identifiers).
6. Assurance level logic: A3 if ISNI + multiple sources, A2 if multiple sources + any standard ID, A1 if any standard ID, A0 otherwise.
7. Confidence formula is weighted average: sum(score_i * weight_i) / sum(weight_i), capped at 1.0.
8. The class is ResolutionOrchestrator in `music_attribution.resolution.orchestrator`.

## Alt Text

Flow diagram of the multi-signal entity resolution pipeline in the music attribution scaffold, showing a cascade from exact identifier matching (ISRC, ISWC, ISNI, MBID) through fuzzy string similarity to per-group resolution using six weighted signals — identifier (1.0), Splink probabilistic linkage (0.8), embedding semantic match (0.7), graph evidence (0.75), string similarity (0.6), and LLM disambiguation (0.85) — producing ResolvedEntity output with assurance levels A0-A3.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Flow diagram of the multi-signal entity resolution pipeline in the music attribution scaffold, showing a cascade from exact identifier matching (ISRC, ISWC, ISNI, MBID) through fuzzy string similarity to per-group resolution using six weighted signals — identifier (1.0), Splink probabilistic linkage (0.8), embedding semantic match (0.7), graph evidence (0.75), string similarity (0.6), and LLM disambiguation (0.85) — producing ResolvedEntity output with assurance levels A0-A3.](docs/figures/repo-figures/assets/fig-backend-06-resolution-orchestrator-flow.jpg)

*Figure 6. The ResolutionOrchestrator implements a cascade strategy — exact identifiers first, then string similarity for unmatched records — with six weighted signals contributing to a final resolution confidence that maps to assurance levels A0-A3.*

### From this figure plan (relative)

![Flow diagram of the multi-signal entity resolution pipeline in the music attribution scaffold, showing a cascade from exact identifier matching (ISRC, ISWC, ISNI, MBID) through fuzzy string similarity to per-group resolution using six weighted signals — identifier (1.0), Splink probabilistic linkage (0.8), embedding semantic match (0.7), graph evidence (0.75), string similarity (0.6), and LLM disambiguation (0.85) — producing ResolvedEntity output with assurance levels A0-A3.](../assets/fig-backend-06-resolution-orchestrator-flow.jpg)
