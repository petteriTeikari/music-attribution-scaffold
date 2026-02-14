# fig-backend-11: Attribution Engine Flow

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-11 |
| **Title** | Attribution Engine: From Resolved Entities to Calibrated Attribution |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/, docs/attribution/ |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the complete Attribution Engine pipeline -- from resolved entities through weighted aggregation, conformal calibration, and review prioritization to the final AttributionRecord. It is the core scoring pipeline that produces the confidence-scored output.

The key message is: "The Attribution Engine takes resolved entities and produces calibrated, confidence-scored attribution records through three stages: weighted source aggregation, conformal prediction calibration, and active learning review prioritization."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  ATTRIBUTION ENGINE                                            |
|  ■ Calibrated Confidence Scoring Pipeline                      |
+---------------------------------------------------------------+
|                                                                 |
|  INPUTS                                                        |
|  ──────                                                        |
|  ┌────────────────┐  ┌──────────────────────┐                 |
|  │  Work Entity    │  │  Contributor Entities │                 |
|  │  (ResolvedEntity│  │  (ResolvedEntity[])   │                 |
|  │   BO-2)         │  │  + role mappings      │                 |
|  └───────┬────────┘  └──────────┬───────────┘                 |
|          │                      │                               |
|          └──────────┬───────────┘                               |
|                     ▼                                           |
|  ┌──────────────────────────────────────────┐                  |
|  │ STAGE 1: CREDIT AGGREGATION               │                  |
|  │ CreditAggregator                          │                  |
|  │                                            │                  |
|  │ Per-credit confidence:                    │                  |
|  │   w_src * resolution_confidence / Σ w_src │                  |
|  │                                            │                  |
|  │ Source Weights (SOURCE_RELIABILITY_WEIGHTS)│                  |
|  │   MusicBrainz: 0.95                       │                  |
|  │   Discogs:     0.85                       │                  |
|  │   AcoustID:    0.80                       │                  |
|  │   File Meta:   0.70                       │                  |
|  │   Artist Input: 0.60                      │                  |
|  └──────────────────┬───────────────────────┘                  |
|                     ▼                                           |
|  ┌──────────────────────────────────────────┐                  |
|  │ STAGE 2: CONFORMAL CALIBRATION            │                  |
|  │ ConformalScorer (APS method)              │                  |
|  │                                            │                  |
|  │ predictions ──> sort by confidence        │                  |
|  │ ──> accumulate until coverage >= 0.90     │                  |
|  │ ──> ConformalSet with calibration_error   │                  |
|  └──────────────────┬───────────────────────┘                  |
|                     ▼                                           |
|  ┌──────────────────────────────────────────┐                  |
|  │ STAGE 3: REVIEW PRIORITIZATION            │                  |
|  │ ReviewPriorityQueue                       │                  |
|  │                                            │                  |
|  │ needs_review = confidence < 0.50          │                  |
|  │ review_priority = 1.0 - confidence        │                  |
|  └──────────────────┬───────────────────────┘                  |
|                     ▼                                           |
|           ┌──────────────────┐                                 |
|           │ AttributionRecord │                                 |
|           │     (BO-3)        │                                 |
|           └──────────────────┘                                 |
|                                                                 |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "ATTRIBUTION ENGINE" |
| Work Entity input | `entity_resolve` | Single ResolvedEntity representing the work/recording |
| Contributor Entities input | `entity_resolve` | List of ResolvedEntities with role mappings |
| Stage 1: Credit Aggregation | `source_corroborate` | Weighted confidence from source reliabilities |
| Source weight table | `data_mono` | Five source weights in monospace |
| Stage 2: Conformal Calibration | `final_score` | APS method producing calibrated prediction sets |
| Stage 3: Review Prioritization | `processing_stage` | Priority scoring for human review queue |
| Review threshold | `confidence_low` | "confidence < 0.50" flagging |
| AttributionRecord output | `primary_outcome` | BO-3 boundary object with accent marker |
| Stage flow arrows | `data_flow` | Sequential flow through three stages |
| Coverage level | `data_mono` | "0.90" target coverage |

## Anti-Hallucination Rules

1. The source reliability weights are from constants.py: MUSICBRAINZ=0.95, DISCOGS=0.85, ACOUSTID=0.80, FILE_METADATA=0.70, ARTIST_INPUT=0.60.
2. The review threshold is 0.50 (REVIEW_THRESHOLD = CONFIDENCE_MEDIUM_THRESHOLD from constants.py).
3. review_priority formula is 1.0 - confidence (from CreditAggregator.aggregate()).
4. The conformal method is APS (Adaptive Prediction Sets), not split-conformal or jackknife.
5. Default target coverage is 0.90, from ConformalScorer.score().
6. Overall confidence is mean of per-credit confidences (sum / len from _compute_confidence).
7. Assurance level is the minimum across all contributor entities.
8. The classes are: CreditAggregator, ConformalScorer, ReviewPriorityQueue -- all in `music_attribution.attribution`.

## Alt Text

Pipeline diagram of the three-stage music attribution engine showing weighted credit aggregation with source reliability weights (MusicBrainz 0.95, Discogs 0.85, AcoustID 0.80, file metadata 0.70, Artist Input 0.60), conformal prediction calibration using Adaptive Prediction Sets at 90% coverage, and active learning review prioritization — producing the final AttributionRecord with transparent confidence scoring for open-source music credits.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Pipeline diagram of the three-stage music attribution engine showing weighted credit aggregation with source reliability weights (MusicBrainz 0.95, Discogs 0.85, AcoustID 0.80, file metadata 0.70, Artist Input 0.60), conformal prediction calibration using Adaptive Prediction Sets at 90% coverage, and active learning review prioritization — producing the final AttributionRecord with transparent confidence scoring for open-source music credits.](docs/figures/repo-figures/assets/fig-backend-11-attribution-engine-flow.jpg)

*Figure 11. The Attribution Engine is the core scoring pipeline: it transforms resolved entities into calibrated, confidence-scored attribution records through weighted source aggregation, conformal prediction calibration, and review prioritization — ensuring that confidence scores are statistically meaningful.*

### From this figure plan (relative)

![Pipeline diagram of the three-stage music attribution engine showing weighted credit aggregation with source reliability weights (MusicBrainz 0.95, Discogs 0.85, AcoustID 0.80, file metadata 0.70, Artist Input 0.60), conformal prediction calibration using Adaptive Prediction Sets at 90% coverage, and active learning review prioritization — producing the final AttributionRecord with transparent confidence scoring for open-source music credits.](../assets/fig-backend-11-attribution-engine-flow.jpg)
