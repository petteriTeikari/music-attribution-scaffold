# fig-backend-15: Review Priority Queue

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-15 |
| **Title** | Review Priority Queue: Active Learning Multi-Factor Ranking |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/, docs/attribution/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the multi-factor priority formula used to rank attribution records for human expert review. It explains each factor, its weight, and how the composite priority score determines the review queue ordering.

The key message is: "Review priority is a weighted composite of five factors -- boundary proximity (30%), source disagreement (25%), conformal set ambiguity (15%), never-reviewed penalty (15%), and staleness (15%) -- designed to surface the most informative records for active learning."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  REVIEW PRIORITY QUEUE                                         |
|  ■ Active Learning — Multi-Factor Ranking                      |
+---------------------------------------------------------------+
|                                                                 |
|  PRIORITY FORMULA                                              |
|  ────────────────                                              |
|  priority = 0.30 * boundary                                    |
|           + 0.25 * disagreement                                |
|           + 0.15 * ambiguity                                   |
|           + 0.15 * never_reviewed                              |
|           + 0.15 * staleness                                   |
|                                                                 |
|  FACTOR DETAILS                                                |
|  ──────────────                                                |
|  ┌─────────────────────────────────────────────────────┐       |
|  │ BOUNDARY (0.30)                                      │       |
|  │ = 1.0 - |confidence - 0.5| * 2.0                    │       |
|  │ ■ Peaks at 0.5 (most uncertain)                     │       |
|  │ ■ 0.0 at confidence 0.0 or 1.0                     │       |
|  │                      ^                               │       |
|  │ score    1.0 ──────/  \──────                       │       |
|  │          0.0 ─────/    \─────                       │       |
|  │              0.0   0.5   1.0  confidence            │       |
|  └─────────────────────────────────────────────────────┘       |
|  ┌─────────────────────────────────────────────────────┐       |
|  │ DISAGREEMENT (0.25) = 1.0 - source_agreement        │       |
|  │ ■ Low agreement between sources = high priority     │       |
|  └─────────────────────────────────────────────────────┘       |
|  ┌─────────────────────────────────────────────────────┐       |
|  │ AMBIGUITY (0.15) = min(Σ set_sizes / 5.0, 1.0)     │       |
|  │ ■ Larger conformal set = more ambiguous roles       │       |
|  └─────────────────────────────────────────────────────┘       |
|  ┌─────────────────────────────────────────────────────┐       |
|  │ NEVER REVIEWED (0.15)                                │       |
|  │ = 1.0 if version == 1, else max(0, 1-(ver-1)*0.25) │       |
|  │ ■ Unreviewed records get full penalty               │       |
|  └─────────────────────────────────────────────────────┘       |
|  ┌─────────────────────────────────────────────────────┐       |
|  │ STALENESS (0.15) = min(age_days / 30.0, 1.0)       │       |
|  │ ■ Records older than 30 days get maximum score      │       |
|  └─────────────────────────────────────────────────────┘       |
|                                                                 |
|  OUTPUT: Ranked list, highest priority first                   |
|  next_for_review(records, limit=10)                            |
|                                                                 |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "REVIEW PRIORITY QUEUE" |
| Priority formula | `final_score` | Weighted sum of 5 factors |
| Boundary factor | `processing_stage` | V-shaped curve peaking at 0.5 confidence |
| Boundary curve | `data_mono` | Small ASCII visualization of the boundary score curve |
| Disagreement factor | `processing_stage` | Inverse of source_agreement |
| Ambiguity factor | `processing_stage` | Normalized conformal set size |
| Never-reviewed factor | `processing_stage` | Version-based review status |
| Staleness factor | `processing_stage` | Time-based decay normalized to 30 days |
| Weight labels | `data_mono` | 0.30, 0.25, 0.15, 0.15, 0.15 in monospace |
| Factor formulas | `data_mono` | Exact formulas for each factor |
| Output description | `callout_box` | next_for_review with default limit=10 |

## Anti-Hallucination Rules

1. The exact weights are from _WEIGHTS in priority_queue.py: boundary=0.30, disagreement=0.25, ambiguity=0.15, never_reviewed=0.15, staleness=0.15.
2. Boundary score formula: 1.0 - abs(confidence - 0.5) * 2.0. This peaks at confidence=0.5.
3. Disagreement score: 1.0 - source_agreement. Simple inverse.
4. Ambiguity score: min(total_set_size / 5.0, 1.0). Normalized by 5.0.
5. Never-reviewed score: 1.0 if version == 1, else max(0.0, 1.0 - (version - 1) * 0.25).
6. Staleness score: min(age_days / 30.0, 1.0). Maxes out at 30 days.
7. Final priority is clamped to [0.0, 1.0] via min(max(priority, 0.0), 1.0).
8. Default limit for next_for_review is 10.
9. The class is ReviewPriorityQueue in `music_attribution.attribution.priority_queue`.

## Alt Text

Multi-factor review priority formula showing five weighted components: boundary proximity (30%), source disagreement (25%), ambiguity (15%), never-reviewed (15%), and staleness (15%) with exact formulas.
