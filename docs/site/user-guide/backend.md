# Backend Guide

## Module Map

```
src/music_attribution/
├── __init__.py              # Package version
├── config.py                # Pydantic Settings configuration
├── core.py                  # Core utilities
├── constants.py             # Project constants
│
├── schemas/                 # Pydantic boundary objects
│   ├── normalized.py        # NormalizedRecord (ETL output)
│   ├── resolved.py          # ResolvedEntity (resolution output)
│   ├── attribution.py       # AttributionRecord (engine output)
│   ├── permissions.py       # Permission request/response
│   ├── feedback.py          # User feedback
│   ├── uncertainty.py       # Uncertainty decomposition
│   └── enums.py             # SourceEnum, AssuranceLevel, etc.
│
├── etl/                     # Pipeline 1: Extract-Transform-Load
│   ├── musicbrainz.py       # MusicBrainz API extractor
│   ├── discogs.py           # Discogs API extractor
│   ├── acoustid.py          # AcoustID fingerprint extractor
│   ├── file_metadata.py     # tinytag file metadata extractor
│   ├── quality_gate.py      # Data quality validation
│   └── rate_limiter.py      # API rate limiting
│
├── resolution/              # Pipeline 2: Entity Resolution
│   ├── orchestrator.py      # Resolution cascade coordinator
│   ├── identifier_match.py  # ISRC/ISWC exact match
│   ├── string_similarity.py # Jaro-Winkler, thefuzz
│   ├── embedding_match.py   # pgvector cosine similarity
│   ├── llm_disambiguation.py # PydanticAI disambiguation
│   ├── splink_linkage.py    # Probabilistic record linkage
│   ├── graph_resolution.py  # Graph-based resolution
│   └── graph_store.py       # Graph persistence
│
├── attribution/             # Pipeline 3: Attribution Engine
│   ├── aggregator.py        # Multi-source confidence aggregation
│   ├── conformal.py         # Conformal prediction calibration
│   ├── persistence.py       # Attribution persistence
│   └── priority_queue.py    # Review queue ordering
│
├── api/                     # Pipeline 4: REST API
│   ├── app.py               # FastAPI application factory
│   ├── dependencies.py      # Dependency injection
│   └── routes/
│       ├── attribution.py   # /api/v1/attributions/
│       ├── permissions.py   # /api/v1/permissions/
│       ├── health.py        # /health
│       └── metrics.py       # /metrics (Prometheus)
│
├── chat/                    # Pipeline 5: Agent
│   ├── agent.py             # PydanticAI agent + 4 tools
│   ├── state.py             # Chat state management
│   └── agui_endpoint.py     # AG-UI SSE endpoint
│
├── mcp/                     # MCP Server
│   └── server.py            # Model Context Protocol server
│
├── db/                      # Database layer
│   ├── engine.py            # Async SQLAlchemy engine
│   ├── models.py            # ORM models
│   └── utils.py             # Database utilities
│
├── search/                  # Search subsystem
│   ├── hybrid_search.py     # Text + vector fusion
│   ├── text_search.py       # PostgreSQL full-text
│   └── vector_search.py     # pgvector cosine
│
├── seed/                    # Sample data
│   └── imogen_heap.py       # 8 works, 0.0-0.95 confidence
│
├── pipeline/                # Orchestration
│   ├── dag.py               # Pipeline DAG definition
│   └── runner.py            # Pipeline execution
│
├── observability/           # Monitoring
│   └── metrics.py           # Prometheus metrics
│
└── quality/                 # Quality monitoring
    └── drift_detector.py    # Confidence distribution drift
```

## Running the Backend

```bash
# Development server with auto-reload
make agent

# Or directly:
uv run uvicorn music_attribution.api.app:create_app --factory --reload --port 8000
```

## Database Management

```bash
# Start PostgreSQL (Docker)
docker compose -f docker-compose.dev.yml up -d postgres

# Run migrations
uv run alembic upgrade head

# Seed sample data
uv run python -m music_attribution.cli.db seed

# Create a new migration
uv run alembic revision --autogenerate -m "description"
```

## Testing

```bash
# Unit tests (fast, no Docker)
make test-local
# or: .venv/bin/python -m pytest tests/unit/ -x -q

# Integration tests (requires PostgreSQL)
make test
# or: .venv/bin/python -m pytest tests/integration/ -x -q

# With coverage
make test-cov
```

### Test Structure

```
tests/
├── unit/                    # 351 tests — mock everything
│   ├── api/                 # API route tests
│   ├── attribution/         # Engine tests
│   ├── etl/                 # Extractor tests
│   ├── resolution/          # Resolution tests
│   ├── schemas/             # Schema validation tests
│   └── test_*.py            # System-level unit tests
├── integration/             # 42 tests — real PostgreSQL
│   ├── etl/                 # Persistence tests
│   └── test_*.py            # Full-stack integration
└── conftest.py              # Shared fixtures
```

## Code Quality

```bash
# All checks (pre-commit runs these)
pre-commit run --all-files

# Individual checks
uv run ruff check src/ tests/   # Lint
uv run ruff format --check .     # Format check
uv run mypy src/                 # Type check
```

## Docker

```bash
# Development environment
docker compose -f docker-compose.dev.yml up

# Test environment (CI parity)
docker compose -f docker-compose.test.yml up

# Production build
docker build -f docker/Dockerfile.prod -t music-attribution:latest .
```
