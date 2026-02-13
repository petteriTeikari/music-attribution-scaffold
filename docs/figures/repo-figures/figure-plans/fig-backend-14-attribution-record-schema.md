# fig-backend-14: AttributionRecord Schema

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-14 |
| **Title** | AttributionRecord (BO-3): Complete Attribution with Confidence & Provenance |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/, docs/schemas/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the complete AttributionRecord Pydantic model -- the final boundary object produced by the Attribution Engine and consumed by both the API/MCP Server and the Chat Interface. It is the most complex schema in the system, containing credits, conformal sets, provenance chains, uncertainty summaries, and review metadata.

The key message is: "AttributionRecord is the crown jewel of the pipeline -- it carries per-credit confidence, conformal prediction sets, a full provenance audit trail, uncertainty metadata, and review prioritization in a single versioned document."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  ATTRIBUTIONRECORD (BO-3)                                      |
|  ■ Pydantic BaseModel — schema_version 1.0.0                  |
+---------------------------------------------------------------+
|                                                                 |
|  CORE IDENTITY                   SCORING                       |
|  ─────────────                   ───────                       |
|  attribution_id: UUID            confidence_score: float[0,1]  |
|  work_entity_id: UUID            source_agreement: float[0,1]  |
|  work_title: str                 assurance_level: A0-A3        |
|  artist_name: str                                               |
|  version: int (>= 1)            CONFORMAL SET                  |
|  created_at: datetime(UTC)       ──────────────                |
|  updated_at: datetime(UTC)       coverage_level: float         |
|                                  prediction_sets: dict         |
|  CREDITS (min 1)                 set_sizes: dict               |
|  ──────────────                  marginal_coverage: float      |
|  ┌──────────────────┐           calibration_error: float      |
|  │ Credit            │           calibration_method: str       |
|  │  entity_id: UUID │           calibration_set_size: int     |
|  │  entity_name: str│                                          |
|  │  role: CreditRole│           REVIEW                         |
|  │  role_detail: str?│           ──────                        |
|  │  confidence:[0,1]│           needs_review: bool             |
|  │  sources: list   │           review_priority: float[0,1]   |
|  │  assurance: A0-A3│                                          |
|  └──────────────────┘           PROVENANCE CHAIN               |
|                                  ─────────────────              |
|  UNCERTAINTY SUMMARY             ┌──────────────────┐          |
|  ───────────────────             │ ProvenanceEvent    │          |
|  (UncertaintyAware               │  event_type: Enum │          |
|   Provenance | None)             │  timestamp: UTC   │          |
|                                  │  agent: str       │          |
|                                  │  details: union   │          |
|                                  │  (6 event types)  │          |
|                                  └──────────────────┘          |
|                                                                 |
+---------------------------------------------------------------+
|  PROVENANCE EVENT TYPES                                        |
|  FETCH | RESOLVE | SCORE | REVIEW | UPDATE | FEEDBACK          |
|  (discriminated union on "type" field)                         |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "ATTRIBUTIONRECORD (BO-3)" |
| Core identity section | `primary_outcome` | attribution_id, work_entity_id, display fields, version |
| Credits section | `source_corroborate` | Credit sub-model with per-credit confidence and sources |
| Scoring section | `final_score` | confidence_score, source_agreement, assurance_level |
| Conformal set section | `final_score` | ConformalSet sub-model with calibration metadata |
| Review section | `confidence_low` | needs_review flag and priority score |
| Provenance chain section | `processing_stage` | List of ProvenanceEvent with discriminated union details |
| Uncertainty summary | `processing_stage` | Optional UncertaintyAwareProvenance |
| Event types footer | `data_mono` | Six event types: FETCH, RESOLVE, SCORE, REVIEW, UPDATE, FEEDBACK |
| Field types | `data_mono` | Type annotations in monospace |

## Anti-Hallucination Rules

1. The exact fields come from `src/music_attribution/schemas/attribution.py`. Do NOT invent fields.
2. CreditRoleEnum has 14 values: PERFORMER, SONGWRITER, COMPOSER, LYRICIST, PRODUCER, ENGINEER, MIXING_ENGINEER, MASTERING_ENGINEER, ARRANGER, SESSION_MUSICIAN, FEATURED_ARTIST, CONDUCTOR, DJ, REMIXER.
3. ProvenanceEventTypeEnum has exactly 6 values: FETCH, RESOLVE, SCORE, REVIEW, UPDATE, FEEDBACK.
4. EventDetails is a discriminated union on the "type" field with 6 detail types: FetchEventDetails, ResolveEventDetails, ScoreEventDetails, ReviewEventDetails, UpdateEventDetails, FeedbackEventDetails.
5. credits has min_length=1 -- at least one credit required.
6. work_title and artist_name are display fields (default empty string), added in migration 004.
7. uncertainty_summary is optional (None by default), added in migration 003.
8. Validators: created_at and updated_at must be timezone-aware, updated_at >= created_at.

## Alt Text

Schema diagram of the AttributionRecord Pydantic model showing credits with per-credit confidence, conformal prediction sets, provenance chain with six event types, and review prioritization metadata.
