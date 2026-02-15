# schemas -- Boundary Object Definitions

Pydantic models that define the typed contracts between pipelines. Every pipeline boundary crossing uses one of these schemas, ensuring validation, serialization, and provenance tracking at every step.

## Boundary Objects

| Schema | File | Pipeline Boundary |
|---|---|---|
| `NormalizedRecord` | `normalized.py` | ETL --> Entity Resolution |
| `ResolvedEntity` | `resolved.py` | Entity Resolution --> Attribution Engine |
| `AttributionRecord` | `attribution.py` | Attribution Engine --> API/MCP + Chat |
| `FeedbackCard` | `feedback.py` | Chat --> Attribution Engine (reverse flow) |
| `PermissionBundle` | `permissions.py` | API/MCP Server (consent queries) |

## Cross-Cutting Types

| Schema | File | Purpose |
|---|---|---|
| `BatchEnvelope[T]` | `batch.py` | Generic envelope wrapping any list of records with `BatchMetadata` (confidence stats, source distribution) |
| `PipelineFeedback` | `pipeline_feedback.py` | Reverse-flow signals between pipelines: REFETCH, RECALIBRATE, DISPUTE, STALE |
| `UncertaintyAwareProvenance` | `uncertainty.py` | Per-step uncertainty tracking with source contributions and calibration metadata |
| `TrainingAttribution` | `training_attribution.py` | Training data attribution for generative AI models |
| `ComplianceRecord` | `compliance.py` | Regulatory compliance tracking (EU AI Act, ISO 42001) |

## Enumerations

All enums are defined in `enums.py` as `StrEnum` for JSON-friendly serialization:

| Enum | Values | Usage |
|---|---|---|
| `SourceEnum` | MUSICBRAINZ, DISCOGS, ACOUSTID, ARTIST_INPUT, FILE_METADATA | Data source identifiers |
| `EntityTypeEnum` | RECORDING, WORK, ARTIST, RELEASE, LABEL, CREDIT | Music entity types |
| `ResolutionMethodEnum` | EXACT_ID, FUZZY_STRING, EMBEDDING, GRAPH, LLM, MANUAL | How entities were resolved |
| `AssuranceLevelEnum` | LEVEL_0 through LEVEL_3 | Verification depth (A0-A3) |
| `CreditRoleEnum` | PERFORMER, SONGWRITER, PRODUCER, ENGINEER, ... | 14 credit roles |
| `PermissionTypeEnum` | AI_TRAINING, VOICE_CLONING, STREAM, SYNC_LICENSE, ... | 15 permission types |
| `PermissionValueEnum` | ALLOW, DENY, ASK, ALLOW_WITH_ATTRIBUTION, ALLOW_WITH_ROYALTY | Permission responses |
| `ConfidenceMethodEnum` | SELF_REPORT, CONFORMAL, ENSEMBLE, SOURCE_WEIGHTED, ... | How confidence was computed |

Commercial landscape enums (future stubs): `AttributionMethodEnum`, `RightsTypeEnum`, `MediaTypeEnum`, `CertificationTypeEnum`, `WatermarkTypeEnum`, `RevenueModelEnum`.

Regulatory enums: `RegulatoryFrameworkEnum`, `ComplianceActorEnum`, `TdmReservationMethodEnum`.

## Key Design Decisions

- **Pydantic v2 models** with strict validation (field validators, model validators).
- **Timezone-aware datetimes enforced**: Every timestamp field has a validator rejecting naive datetimes.
- **Machine sources require identifiers**: MusicBrainz, Discogs, and AcoustID records must have at least one standard identifier (ISRC, ISWC, ISNI, MBID, or AcoustID).
- **Schema versioning**: Every boundary object carries a `schema_version` field for forward compatibility.
- **Discriminated unions**: Provenance event details use Pydantic's discriminated union pattern (`Field(discriminator="type")`) for type-safe event payloads.

## Connection to Adjacent Pipelines

- **Upstream**: ETL connectors produce `NormalizedRecord` instances.
- **Downstream**: The resolution orchestrator consumes `NormalizedRecord` and produces `ResolvedEntity`. The attribution aggregator consumes `ResolvedEntity` and produces `AttributionRecord`.
- **API layer**: Routes serialize `AttributionRecord` and `PermissionBundle` as JSON responses.
- **Chat agent**: Tools query `AttributionRecord` and produce `FeedbackCard` for corrections.

## Full API Documentation

See the [API Reference: Schemas](https://petteriTeikari.github.io/music-attribution-scaffold/api-reference/schemas/) on the documentation site.
