# fig-backend-12: Weighted Source Aggregation

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-12 |
| **Title** | Weighted Source Aggregation: Per-Credit Confidence Formula |
| **Audience** | L4 (AI/ML Architect) |
| **Complexity** | L4 |
| **Location** | docs/architecture/, docs/attribution/ |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure visualizes the mathematical formula for computing per-credit and overall attribution confidence from weighted source reliabilities. It shows how different sources contribute differently to the final score based on their reliability weights.

The key message is: "Attribution confidence is a weighted average -- high-authority sources like MusicBrainz (0.95) contribute more than lower-authority sources like Artist Input (0.60). The overall score is the mean of all per-credit confidences."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WEIGHTED SOURCE AGGREGATION                                   |
|  ■ Per-Credit Confidence Formula                               |
+---------------------------------------------------------------+
|                                                                 |
|  PER-CREDIT CONFIDENCE                                         |
|  ─────────────────────                                         |
|                                                                 |
|            Σ (resolution_confidence * w_source)                 |
|  credit = ─────────────────────────────────────                |
|                     Σ w_source                                  |
|                                                                 |
|  SOURCE RELIABILITY WEIGHTS                                    |
|  ──────────────────────────                                    |
|  ┌────────────────────────────────────────────────┐            |
|  │                                                 │            |
|  │  MusicBrainz  ████████████████████████████ 0.95 │            |
|  │  Discogs      ██████████████████████████  0.85  │            |
|  │  AcoustID     ████████████████████████    0.80  │            |
|  │  File Meta    ██████████████████████      0.70  │            |
|  │  Artist Input ████████████████████        0.60  │            |
|  │                                                 │            |
|  └────────────────────────────────────────────────┘            |
|                                                                 |
|  EXAMPLE                                                       |
|  ───────                                                       |
|  Entity "Imogen Heap" found in 3 sources:                      |
|    MusicBrainz (0.95): res_conf = 0.92                         |
|    Discogs     (0.85): res_conf = 0.88                         |
|    File Meta   (0.70): res_conf = 0.70                         |
|                                                                 |
|  credit = (0.92*0.95 + 0.88*0.85 + 0.70*0.70)                 |
|           / (0.95 + 0.85 + 0.70)                               |
|         = (0.874 + 0.748 + 0.490) / 2.50                      |
|         = 0.845                                                 |
|                                                                 |
|  OVERALL ATTRIBUTION CONFIDENCE                                |
|  ──────────────────────────────                                |
|                                                                 |
|            Σ credit_confidence_i                                |
|  overall = ─────────────────────                               |
|                  N_credits                                      |
|                                                                 |
|  SOURCE AGREEMENT                                              |
|  ────────────────                                              |
|  avg(resolution_confidence) across all contributor entities     |
|  Capped at 1.0                                                  |
|                                                                 |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WEIGHTED SOURCE AGGREGATION" |
| Per-credit formula | `final_score` | Mathematical formula with sigma notation |
| Source weight bar chart | `data_mono` | Horizontal bars proportional to weight values |
| Weight values | `data_mono` | 0.95, 0.85, 0.80, 0.70, 0.60 in monospace |
| Worked example | `callout_box` | "Imogen Heap" example with three sources and arithmetic |
| Overall confidence formula | `final_score` | Mean of per-credit confidences |
| Source agreement formula | `final_score` | Average resolution_confidence across entities |
| Source labels | `source_musicbrainz`, `source_discogs`, `source_file` | Color-coded source names |

## Anti-Hallucination Rules

1. The exact weights are from constants.py SOURCE_RELIABILITY_WEIGHTS: MUSICBRAINZ=0.95, DISCOGS=0.85, ACOUSTID=0.80, FILE_METADATA=0.70, ARTIST_INPUT=0.60.
2. Per-credit formula: sum(resolution_confidence * weight) / sum(weight). This is from _weighted_confidence() in aggregator.py.
3. Overall confidence is arithmetic mean of per-credit confidences (from _compute_confidence).
4. Source agreement is average of resolution_confidence across all entities, capped at 1.0 (from _compute_source_agreement).
5. If no sources found, _weighted_confidence returns entity.resolution_confidence unchanged.
6. The default for unknown sources is weight 0.5 (from get() default in _weighted_confidence).
7. Do NOT show Bayesian updating or multiplicative combination -- the method is simple weighted average.
8. The worked example numbers must be arithmetically correct.

## Alt Text

Mathematical diagram showing weighted source aggregation formula with bar chart of five source reliability weights and worked example computing 0.845 per-credit confidence from three sources.
