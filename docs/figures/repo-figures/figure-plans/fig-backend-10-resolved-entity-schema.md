# fig-backend-10: ResolvedEntity Schema

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-10 |
| **Title** | ResolvedEntity (BO-2): Unified Identity with Provenance Chain |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/, docs/schemas/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the complete field layout of the ResolvedEntity Pydantic model -- the boundary object produced by the Entity Resolution pipeline and consumed by the Attribution Engine. It emphasizes the provenance chain: which source records contributed, how they were resolved, and what confidence was achieved.

The key message is: "ResolvedEntity carries full provenance -- every source record that contributed, the resolution method used, per-method confidence breakdown, detected conflicts, and a review flag for uncertain resolutions."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  RESOLVEDENTITY (BO-2)                                         |
|  ■ Pydantic BaseModel — schema_version 1.0.0                  |
+---------------------------------------------------------------+
|                                                                 |
|  CORE IDENTITY                   RESOLUTION PROVENANCE          |
|  ─────────────                   ─────────────────────          |
|  entity_id: UUID (auto)          resolution_method: Enum        |
|  entity_type: EntityTypeEnum       EXACT_ID | FUZZY_STRING      |
|  canonical_name: str               EMBEDDING | GRAPH            |
|  alternative_names: list[str]      LLM | MANUAL                 |
|  identifiers: IdentifierBundle   resolution_confidence: [0,1]   |
|  resolved_at: datetime(UTC)                                     |
|                                  ResolutionDetails:              |
|  SOURCE RECORDS (min 1)            string_similarity: float?    |
|  ─────────────────────             embedding_similarity: float? |
|  ┌──────────────────────┐          graph_path_confidence: float?|
|  │ SourceReference       │          llm_confidence: float?      |
|  │  record_id: UUID     │          matched_identifiers: list    |
|  │  source: SourceEnum  │                                       |
|  │  source_id: str      │       ASSURANCE & REVIEW              |
|  │  agreement_score:[0,1]│       ─────────────────              |
|  └──────────────────────┘       assurance_level: A0-A3          |
|  (one per contributing record)  needs_review: bool              |
|                                  review_reason: str | None      |
|  CONFLICTS                                                      |
|  ─────────                       RELATIONSHIPS                  |
|  ┌──────────────────────┐       ─────────────                   |
|  │ Conflict              │       ┌──────────────────────┐       |
|  │  field: str          │       │ ResolvedRelationship  │       |
|  │  values: {src: val}  │       │  target_entity_id: UUID│      |
|  │  severity: LOW-CRIT  │       │  relationship_type    │       |
|  └──────────────────────┘       │  confidence: [0,1]    │       |
|                                  │  supporting_sources   │       |
|  merged_from: list[UUID]?       └──────────────────────┘       |
|                                                                 |
+---------------------------------------------------------------+
|  VALIDATORS                                                     |
|  ■ resolved_at must be timezone-aware (UTC)                    |
|  ■ If needs_review=True, review_reason must be non-None        |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "RESOLVEDENTITY (BO-2)" in editorial caps |
| Core identity section | `entity_resolve` | Primary fields: entity_id, type, name, identifiers |
| Source records section | `source_corroborate` | SourceReference sub-model with provenance |
| Resolution provenance | `entity_resolve` | Method, confidence, and per-method breakdown |
| ResolutionDetails | `data_mono` | Per-method confidence scores (all optional) |
| Assurance & review | `processing_stage` | A0-A3 level, needs_review flag, review_reason |
| Conflicts section | `confidence_low` | Conflict sub-model with field, values, severity |
| Relationships section | `processing_stage` | ResolvedRelationship with cross-entity links |
| Validators | `callout_box` | Two Pydantic validators at bottom |
| Field types | `data_mono` | Type annotations in monospace |

## Anti-Hallucination Rules

1. The exact fields come from `src/music_attribution/schemas/resolved.py`. Do NOT invent fields.
2. ResolutionMethodEnum has exactly 6 values: EXACT_ID, FUZZY_STRING, EMBEDDING, GRAPH, LLM, MANUAL.
3. ConflictSeverityEnum has exactly 4 values: LOW, MEDIUM, HIGH, CRITICAL.
4. source_records has min_length=1 -- there must be at least one source record.
5. All four ResolutionDetails scores (string, embedding, graph, llm) are optional (float | None).
6. There are exactly 2 validators: validate_resolved_at and validate_review_fields.
7. The review_reason validation is: if needs_review is True, review_reason must be non-None.
8. AssuranceLevelEnum values are LEVEL_0 through LEVEL_3, not A0-A3 in the enum names.

## Alt Text

Data schema diagram of the ResolvedEntity Pydantic model in the music attribution scaffold, showing core identity fields with assurance levels A0-A3, source provenance references tracking which MusicBrainz, Discogs, or AcoustID records contributed, per-method resolution confidence breakdown (string, embedding, graph, LLM), conflict detection with severity levels, and review flags for uncertain music credits requiring human verification.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Data schema diagram of the ResolvedEntity Pydantic model in the music attribution scaffold, showing core identity fields with assurance levels A0-A3, source provenance references tracking which MusicBrainz, Discogs, or AcoustID records contributed, per-method resolution confidence breakdown (string, embedding, graph, LLM), conflict detection with severity levels, and review flags for uncertain music credits requiring human verification.](docs/figures/repo-figures/assets/fig-backend-10-resolved-entity-schema.jpg)

*Figure 10. The ResolvedEntity (BO-2) carries full provenance from entity resolution — every contributing source record, the resolution method used, per-method confidence scores, and detected conflicts — enabling transparent confidence scoring in the downstream attribution engine.*

### From this figure plan (relative)

![Data schema diagram of the ResolvedEntity Pydantic model in the music attribution scaffold, showing core identity fields with assurance levels A0-A3, source provenance references tracking which MusicBrainz, Discogs, or AcoustID records contributed, per-method resolution confidence breakdown (string, embedding, graph, LLM), conflict detection with severity levels, and review flags for uncertain music credits requiring human verification.](../assets/fig-backend-10-resolved-entity-schema.jpg)
