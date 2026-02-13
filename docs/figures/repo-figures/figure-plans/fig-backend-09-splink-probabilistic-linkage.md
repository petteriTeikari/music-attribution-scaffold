# fig-backend-09: Splink Probabilistic Linkage

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-09 |
| **Title** | Splink Probabilistic Linkage: Fellegi-Sunter Record Matching |
| **Audience** | L4 (AI/ML Architect) |
| **Complexity** | L4 |
| **Location** | docs/architecture/, docs/resolution/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure explains the Fellegi-Sunter probabilistic record linkage implemented via Splink with DuckDB backend. It shows the parameter estimation process, match/non-match weight computation, prediction, and clustering stages.

The key message is: "Splink applies Fellegi-Sunter theory to music entity records -- estimating match (m) and non-match (u) probabilities via EM, then computing pairwise match probabilities and clustering records above a 0.85 threshold using union-find."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  SPLINK PROBABILISTIC LINKAGE                                  |
|  ■ Fellegi-Sunter Model with DuckDB Backend                   |
+---------------------------------------------------------------+
|                                                                 |
|  STEP 1: CONFIGURE                                             |
|  ─────────────────                                             |
|  Comparison columns ──> ExactMatch comparisons                 |
|  (configurable)         + term frequency adjustments           |
|  Blocking rules ──> block_on(col) per comparison column        |
|                                                                 |
|  STEP 2: ESTIMATE PARAMETERS                                  |
|  ──────────────────────────                                    |
|  ┌───────────────────────────────────────────┐                 |
|  │  Random sampling (max_pairs = 1e5)        │                 |
|  │  ──> estimate u (non-match) probabilities │                 |
|  │                                            │                 |
|  │  EM per blocking column                   │                 |
|  │  ──> estimate m (match) probabilities     │                 |
|  │                                            │                 |
|  │  m = P(agree | match)                     │                 |
|  │  u = P(agree | non-match)                 │                 |
|  │  weight = log2(m/u)                       │                 |
|  └───────────────────────────────────────────┘                 |
|                                                                 |
|  STEP 3: PREDICT                                               |
|  ───────────────                                               |
|  Record pairs ──> match_probability per pair                   |
|                   (via trained Splink Linker)                   |
|                                                                 |
|  STEP 4: CLUSTER                                               |
|  ────────────────                                              |
|  ┌───────────────────────────────────────────┐                 |
|  │  Filter: match_probability >= 0.85        │                 |
|  │  Union-find clustering                    │                 |
|  │                                            │                 |
|  │  ┌───┐  0.92  ┌───┐                      │                 |
|  │  │ A │────────│ B │  ──> Cluster {A,B,C}  │                 |
|  │  └───┘        └─┬─┘                      │                 |
|  │          0.88   │                          │                 |
|  │          ┌──────┘                          │                 |
|  │          │                                 │                 |
|  │        ┌─┴─┐                              │                 |
|  │        │ C │          ┌───┐               │                 |
|  │        └───┘          │ D │  ──> Singleton│                 |
|  │                       └───┘               │                 |
|  └───────────────────────────────────────────┘                 |
|                                                                 |
|  FALLBACK: If Splink unavailable, exact match on columns       |
|  Orchestrator weight: 0.8                                       |
|                                                                 |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "SPLINK PROBABILISTIC LINKAGE" |
| Configure step | `processing_stage` | Model configuration with comparison columns and blocking rules |
| Estimate step | `processing_stage` | Parameter estimation via random sampling + EM |
| m/u formulas | `data_mono` | Match and non-match probability definitions |
| Weight formula | `data_mono` | log2(m/u) in monospace |
| Predict step | `entity_resolve` | Pairwise match probability computation |
| Cluster step | `entity_resolve` | Union-find clustering above threshold |
| Cluster visualization | `entity_resolve` | Small graph showing linked nodes forming clusters |
| Threshold value | `data_mono` | "0.85" clustering threshold |
| Fallback note | `callout_box` | Exact-match fallback when Splink is unavailable |
| Orchestrator weight | `data_mono` | "Weight: 0.8" from orchestrator config |
| DuckDB backend | `storage_layer` | DuckDB as Splink's processing backend |

## Anti-Hallucination Rules

1. The Splink backend is DuckDB (DuckDBAPI), not Spark or PostgreSQL.
2. The clustering threshold default is 0.85, from SplinkMatcher.cluster().
3. The orchestrator weight for Splink is 0.8, from _DEFAULT_WEIGHTS.
4. Random sampling max_pairs is 1e5 (100,000), from estimate_parameters().
5. The fallback when Splink is unavailable is simple exact matching on comparison columns, producing match_probability = matches/total.
6. Splink v4 import path is `from splink import block_on, DuckDBAPI, Linker, SettingsCreator`.
7. The link_type is "dedupe_only" (not "link_only" or "link_and_dedupe").
8. Comparisons use ExactMatch with term_frequency_adjustments=True.
9. The class is SplinkMatcher in `music_attribution.resolution.splink_linkage`.

## Alt Text

Four-step Splink probabilistic linkage diagram: configure comparisons, estimate Fellegi-Sunter m/u parameters via EM, predict match probabilities, and cluster records above 0.85 threshold using union-find.
