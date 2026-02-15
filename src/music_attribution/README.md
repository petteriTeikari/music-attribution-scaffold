# music_attribution -- Backend Package

The `music_attribution` Python package implements a five-pipeline architecture for multi-source music attribution with calibrated confidence scores.

## Module Map

| Module | Purpose |
|---|---|
| `schemas/` | Pydantic boundary objects that define contracts between pipelines |
| `etl/` | Data source connectors (MusicBrainz, Discogs, AcoustID, file metadata) |
| `resolution/` | 5-strategy entity resolution cascade with orchestrator |
| `attribution/` | Credit aggregation, conformal prediction scoring, review priority queue |
| `api/` | FastAPI application factory with REST endpoints |
| `chat/` | PydanticAI agent with 4 tools + AG-UI SSE endpoint for CopilotKit |
| `mcp/` | MCP server implementing the Permission Patchbay |
| `db/` | SQLAlchemy ORM models + async engine factory |
| `search/` | Hybrid search combining full-text, vector similarity, and graph context |
| `pipeline/` | DAG-based pipeline runner for orchestrating the full attribution flow |
| `seed/` | Mock data loader (8 Imogen Heap works spanning 0.0--0.95 confidence) |
| `confidence/` | Confidence scoring utilities |
| `feedback/` | Feedback persistence (FeedbackCard storage) |
| `permissions/` | Permission bundle persistence + audit logging |
| `observability/` | Prometheus metrics definitions |
| `quality/` | Drift detection for data quality monitoring |
| `config.py` | Pydantic Settings for environment-based configuration |
| `constants.py` | Shared constants (thresholds, weights, defaults) |
| `core.py` | Core utility functions |

## Pipeline Architecture

Data flows through five sequential pipelines, each consuming and producing typed boundary objects:

```
Pipeline 1: ETL (Data Engineering)
  Input:  External APIs, audio files, artist self-reports
  Output: NormalizedRecord (BO-1)

Pipeline 2: Entity Resolution
  Input:  list[NormalizedRecord]
  Output: list[ResolvedEntity] (BO-2)

Pipeline 3: Attribution Engine
  Input:  ResolvedEntity (work) + list[ResolvedEntity] (contributors)
  Output: AttributionRecord (BO-3)

Pipeline 4: API / MCP Server
  Input:  AttributionRecord, PermissionBundle (BO-5)
  Output: REST responses, MCP tool results

Pipeline 5: Chat / Agent
  Input:  User messages + AttributionRecord context
  Output: AG-UI SSE events (text, state snapshots, tool calls)
```

## Boundary Objects

The `schemas/` package defines the contracts between pipelines:

| Schema | Role | Key Fields |
|---|---|---|
| `NormalizedRecord` | ETL output | source, entity_type, canonical_name, identifiers, source_confidence |
| `ResolvedEntity` | Resolution output | resolution_method, resolution_confidence, assurance_level, conflicts |
| `AttributionRecord` | Attribution output | credits, confidence_score, conformal_set, provenance_chain |
| `FeedbackCard` | Reverse flow | corrections, overall_assessment, evidence_type |
| `PermissionBundle` | Consent queries | permissions, delegation_chain, effective_from/until |

Cross-cutting types include `BatchEnvelope[T]` (wraps any boundary object list with statistical metadata) and `PipelineFeedback` (reverse signals: REFETCH, RECALIBRATE, DISPUTE, STALE).

## Key Patterns

- **In-memory + PostgreSQL repositories**: Every persistence layer has both an in-memory implementation (for tests/dev) and an async PostgreSQL implementation (for production). Example: `AttributionRecordRepository` vs `AsyncAttributionRepository`.
- **Lazy singletons for expensive resources**: The PydanticAI agent and sentence-transformer model are created lazily on first use to avoid requiring API keys at import time.
- **Async everywhere**: All ETL connectors wrap synchronous libraries (musicbrainzngs, discogs_client, acoustid) in `asyncio.to_thread()` for async compatibility.
- **Deterministic UUIDs for seeding**: The seed module uses `uuid5` with a fixed namespace for idempotent database seeding.

## Entry Points

| Entry Point | Module | Command |
|---|---|---|
| FastAPI app | `api.app:create_app()` | `uvicorn music_attribution.api.app:create_app --factory` |
| MCP server | `mcp.server:create_mcp_server()` | Via FastMCP runner |
| Database CLI | `cli.db` | `uv run python -m music_attribution.cli.db` |

## Full Documentation

See the [GitHub Pages documentation site](https://petteriTeikari.github.io/music-attribution-scaffold/) for API reference, concept guides, and tutorials.
