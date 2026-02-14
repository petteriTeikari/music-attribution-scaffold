# fig-backend-20: Dependency Injection

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-20 |
| **Title** | FastAPI Dependency Injection: Request to Response Chain |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/, docs/api/ |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 675px (16:9) |

## Purpose & Key Message

This figure traces the dependency injection chain in the FastAPI application -- from incoming HTTP request through app.state, session factory, database sessions, repositories, and services to the final response. Engineers need this to understand how to add new endpoints and where to inject dependencies.

The key message is: "Dependencies flow through app.state -- the lifespan creates the async engine and session factory at startup, route handlers access them via request.app.state, and sessions are scoped to single requests with automatic rollback on errors."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  DEPENDENCY INJECTION CHAIN                                    |
|  ■ FastAPI app.state + Session Scoping                         |
+---------------------------------------------------------------+
|                                                                 |
|  STARTUP (lifespan)                                            |
|  ──────────────────                                            |
|  Settings() ──> database_url                                   |
|      │                                                          |
|      ├──> create_async_engine_factory(url) ──> engine          |
|      └──> async_session_factory(engine) ──> factory            |
|                                                                 |
|  Stored on app.state:                                          |
|    app.state.async_engine                                      |
|    app.state.async_session_factory                             |
|    app.state.settings                                          |
|                                                                 |
|  ─────────────────────────────────────────────────────         |
|                                                                 |
|  REQUEST FLOW                                                  |
|  ────────────                                                  |
|                                                                 |
|  HTTP Request                                                  |
|       │                                                         |
|       ▼                                                         |
|  ┌──────────────────┐                                          |
|  │ Route Handler     │                                          |
|  │ (e.g. GET /api/v1/│                                         |
|  │  attributions/)   │                                          |
|  └────────┬─────────┘                                          |
|           │                                                     |
|           ▼                                                     |
|  ┌──────────────────┐    request.app.state                     |
|  │ _get_session()    │──> .async_session_factory                |
|  │ (per-route helper)│    returns factory()                     |
|  └────────┬─────────┘                                          |
|           │                                                     |
|           ▼                                                     |
|  ┌──────────────────┐    OR (via get_db_session):              |
|  │ AsyncSession      │    try: yield session                    |
|  │ (request-scoped)  │    except: rollback                      |
|  └────────┬─────────┘                                          |
|           │                                                     |
|           ▼                                                     |
|  ┌──────────────────┐                                          |
|  │ Repository        │    e.g. AsyncAttributionRepository      |
|  │ (data access)     │         AsyncPermissionRepository       |
|  └────────┬─────────┘                                          |
|           │                                                     |
|           ▼                                                     |
|  ┌──────────────────┐                                          |
|  │ Service Layer     │    e.g. HybridSearchService             |
|  │ (business logic)  │         CreditAggregator                |
|  └────────┬─────────┘                                          |
|           │                                                     |
|           ▼                                                     |
|  HTTP Response (JSON)                                          |
|                                                                 |
+---------------------------------------------------------------+
|  SHUTDOWN (lifespan)                                           |
|  ■ engine.dispose() — close all connections                    |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "DEPENDENCY INJECTION CHAIN" |
| Startup section | `processing_stage` | Lifespan: Settings -> engine -> session factory |
| app.state storage | `storage_layer` | Three state attributes: engine, factory, settings |
| Route handler | `api_endpoint` | Entry point for HTTP requests |
| _get_session helper | `processing_stage` | Per-route session acquisition from app.state |
| get_db_session dependency | `processing_stage` | FastAPI Depends() with try/yield/rollback |
| AsyncSession | `storage_layer` | Request-scoped database session |
| Repository layer | `storage_layer` | Data access: AsyncAttributionRepository, AsyncPermissionRepository |
| Service layer | `processing_stage` | Business logic: HybridSearchService, CreditAggregator |
| Response | `primary_outcome` | JSON response to client |
| Shutdown section | `processing_stage` | engine.dispose() at app shutdown |
| Flow arrows | `data_flow` | Linear flow from request to response |
| Accent divider | `accent_line` | Separating startup from request flow |

## Anti-Hallucination Rules

1. The lifespan creates: async_engine (via create_async_engine_factory), async_session_factory (via async_session_factory), and settings (via Settings()).
2. State is stored as: app.state.async_engine, app.state.async_session_factory, app.state.settings.
3. Route handlers use _get_session(request) to get sessions -- this is a per-route helper, not FastAPI Depends().
4. The get_db_session function in dependencies.py IS a Depends()-compatible async generator with try/yield/rollback.
5. The engine is create_async_engine_factory (async engine), not sync.
6. Shutdown calls engine.dispose() to close all connections.
7. Settings requires database_url and cors_origins configuration.
8. Repository examples: AsyncAttributionRepository, AsyncPermissionRepository. Service examples: HybridSearchService.
9. Sessions are created per-request via `async with factory() as session`.

## Alt Text

Architecture diagram of the FastAPI dependency injection chain in the music attribution scaffold, showing the lifespan creating an async PostgreSQL engine and session factory stored on app.state, with request-scoped database sessions flowing through route handlers, repository layer (attribution and permission repositories), and service layer (hybrid search, credit aggregation) to produce JSON responses for music credit confidence scoring queries.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture diagram of the FastAPI dependency injection chain in the music attribution scaffold, showing the lifespan creating an async PostgreSQL engine and session factory stored on app.state, with request-scoped database sessions flowing through route handlers, repository layer (attribution and permission repositories), and service layer (hybrid search, credit aggregation) to produce JSON responses for music credit confidence scoring queries.](docs/figures/repo-figures/assets/fig-backend-20-dependency-injection.jpg)

*Figure 20. Dependencies flow through app.state in a clean chain: the lifespan creates the async engine and session factory at startup, route handlers acquire request-scoped sessions, and repositories and services are composed without global state — enabling straightforward testing and extension of the attribution API.*

### From this figure plan (relative)

![Architecture diagram of the FastAPI dependency injection chain in the music attribution scaffold, showing the lifespan creating an async PostgreSQL engine and session factory stored on app.state, with request-scoped database sessions flowing through route handlers, repository layer (attribution and permission repositories), and service layer (hybrid search, credit aggregation) to produce JSON responses for music credit confidence scoring queries.](../assets/fig-backend-20-dependency-injection.jpg)
