# api -- FastAPI REST Server

The API layer exposes attribution records, permission checks, and the agentic chat endpoint via a FastAPI application. This is Pipeline 4 in the architecture.

## Files

| File | Purpose |
|---|---|
| `app.py` | Application factory (`create_app()`) with lifespan management |
| `dependencies.py` | FastAPI dependency injection (async database sessions) |
| `routes/attribution.py` | Attribution query endpoints (CRUD, search, provenance) |
| `routes/permissions.py` | Permission check and listing endpoints |
| `routes/health.py` | Health check endpoint (`/health`) |
| `routes/metrics.py` | Prometheus metrics endpoint |

## Application Factory

The `create_app()` function builds and configures the FastAPI app:

```python
from music_attribution.api.app import create_app

app = create_app()
```

Lifespan management:
- **Startup**: Creates an async SQLAlchemy engine and session factory from `DATABASE_URL`. Stores both on `app.state`.
- **Shutdown**: Disposes the engine to close all database connections.

CORS is configured from the `CORS_ORIGINS` environment variable (comma-separated origins).

## Routes

### Attribution Endpoints (prefix: `/api/v1`)

| Method | Path | Description |
|---|---|---|
| `GET` | `/attributions/work/{work_id}` | Get attribution record by work entity UUID |
| `GET` | `/attributions/` | List records with pagination, filtering by `needs_review` and `assurance_level` |
| `GET` | `/attributions/{attribution_id}/provenance` | Get full provenance chain with uncertainty metadata |
| `GET` | `/attributions/search?q=...` | Hybrid search (text + vector + graph via RRF fusion) |

### Permission Endpoints (prefix: `/api/v1`)

| Method | Path | Description |
|---|---|---|
| `POST` | `/permissions/check` | Check a specific permission (AI_TRAINING, VOICE_CLONING, etc.) for an entity |
| `GET` | `/permissions/{entity_id}` | List all permission bundles for an entity |

The permission check endpoint also records an audit log entry for compliance tracking.

### Infrastructure Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/health` | Returns `{"status": "healthy"}` |
| `GET` | `/metrics` | Prometheus-format metrics |

### CopilotKit Endpoint (prefix: `/api/v1`)

| Method | Path | Description |
|---|---|---|
| `POST` | `/copilotkit` | AG-UI SSE endpoint for CopilotKit agentic sidebar |

This endpoint is mounted from `chat/agui_endpoint.py`. See the `chat/` module README for details.

## Dependencies

The `get_db_session` dependency (in `dependencies.py`) yields an `AsyncSession` per request with automatic rollback on errors:

```python
async def get_db_session(factory) -> AsyncGenerator[AsyncSession]:
    async with factory() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
```

Route handlers access the session factory via `request.app.state.async_session_factory`.

## Configuration

Key environment variables (managed by `config.py`):

| Variable | Default | Purpose |
|---|---|---|
| `DATABASE_URL` | (required) | PostgreSQL connection string |
| `CORS_ORIGINS` | `http://localhost:3000` | Allowed CORS origins |
| `ATTRIBUTION_AGENT_MODEL` | `anthropic:claude-haiku-4-5` | PydanticAI model for chat agent |

## Connection to Adjacent Pipelines

- **Upstream**: Reads `AttributionRecord` and `PermissionBundle` from the PostgreSQL database.
- **Chat integration**: The CopilotKit endpoint is mounted on the same app, sharing the same database session factory.
- **MCP complement**: The REST API and MCP server expose the same underlying data -- REST for web clients, MCP for AI platform integration.

## Running

```bash
# Via the Makefile (starts Docker with PostgreSQL + backend + frontend)
make dev

# Directly
uvicorn music_attribution.api.app:create_app --factory --reload --port 8000
```

Swagger UI is available at `http://localhost:8000/docs`.

## Full API Documentation

See the [API Reference: REST API](https://petteriTeikari.github.io/music-attribution-scaffold/api-reference/api/) on the documentation site.
