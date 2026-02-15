# fig-backend-16: FastAPI Route Map

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-backend-16 |
| **Title** | FastAPI Route Map: API Endpoints & Middleware |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/, docs/api/ |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure maps all FastAPI routes, their HTTP methods, prefixes, and purpose. Engineers integrating with the API need a single reference showing every available endpoint, what it does, and how routers are organized.

The key message is: "The Music Attribution API exposes five router groups -- health, metrics, attribution CRUD, permission checks, and the CopilotKit AG-UI endpoint -- all mounted on a single FastAPI app with CORS middleware and async PostgreSQL lifespan management."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  FASTAPI ROUTE MAP                                             |
|  ■ API Endpoints & Router Organization                         |
+---------------------------------------------------------------+
|                                                                 |
|  FastAPI App (create_app)                                      |
|  ├── Middleware: CORSMiddleware (configurable origins)          |
|  ├── Lifespan: async engine + session factory                  |
|  │                                                              |
|  ├── health_router (no prefix)                                 |
|  │   └── GET  /health                                          |
|  │         → {"status": "healthy"}                             |
|  │                                                              |
|  ├── metrics_router (no prefix)                                |
|  │   └── GET  /metrics                                         |
|  │         → Prometheus exposition format                      |
|  │                                                              |
|  ├── attribution_router (prefix: /api/v1)                      |
|  │   ├── GET  /api/v1/attributions/                            |
|  │   │     → List with pagination, filtering, sorting          |
|  │   │     Params: limit, offset, needs_review, assurance_level|
|  │   ├── GET  /api/v1/attributions/work/{work_id}              |
|  │   │     → Get by work entity UUID                           |
|  │   ├── GET  /api/v1/attributions/{id}/provenance             |
|  │   │     → Full provenance chain + uncertainty               |
|  │   └── GET  /api/v1/attributions/search                      |
|  │         → Hybrid search (text + vector + graph RRF)         |
|  │         Params: q, limit                                    |
|  │                                                              |
|  ├── permissions_router (prefix: /api/v1)                      |
|  │   ├── POST /api/v1/permissions/check                        |
|  │   │     → Check permission for entity + type                |
|  │   │     Body: entity_id, permission_type, requester_id      |
|  │   └── GET  /api/v1/permissions/{entity_id}                  |
|  │         → List all permission bundles for entity            |
|  │                                                              |
|  └── copilotkit_router (prefix: /api/v1)                       |
|      └── POST /api/v1/copilotkit                               |
|            → AG-UI SSE streaming (CopilotKit protocol)         |
|                                                                 |
+---------------------------------------------------------------+
|  ■ App version: 0.1.0                                          |
|  ■ All routes use async PostgreSQL sessions via app.state      |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "FASTAPI ROUTE MAP" |
| App container | `api_endpoint` | FastAPI app with middleware and lifespan |
| Health router | `api_endpoint` | GET /health -- simple status check |
| Metrics router | `api_endpoint` | GET /metrics -- Prometheus exposition |
| Attribution router | `api_endpoint` | Four GET endpoints for attribution CRUD + search |
| Permissions router | `api_endpoint` | POST check + GET list endpoints |
| CopilotKit router | `api_endpoint` | POST SSE streaming endpoint |
| HTTP methods | `data_mono` | GET, POST in monospace |
| Route paths | `data_mono` | Full URL paths in monospace |
| Query parameters | `label_editorial` | Parameter descriptions per endpoint |
| CORS middleware | `security_layer` | Configurable allowed origins |
| Lifespan | `processing_stage` | Async engine lifecycle management |
| Tree structure | `data_flow` | Nested tree showing router hierarchy |

## Anti-Hallucination Rules

1. The exact routes come from the actual route files. Do NOT invent endpoints.
2. health_router and metrics_router have no prefix. attribution_router, permissions_router, and copilotkit_router use prefix="/api/v1".
3. The attribution router has exactly 4 endpoints: list, get by work_id, get provenance, search.
4. The permissions router has exactly 2 endpoints: POST check, GET list by entity_id.
5. The CopilotKit endpoint is POST /api/v1/copilotkit -- it uses SSE streaming.
6. The app version is "0.1.0" (from create_app).
7. CORS origins come from settings.cors_origins.split(","), not hardcoded.
8. The lifespan manages: async_engine, async_session_factory, and settings on app.state.
9. The metrics endpoint uses prometheus_client.generate_latest(REGISTRY).
10. Search uses HybridSearchService with RRF fusion (text + vector + graph).

## Alt Text

Architecture diagram of the FastAPI route map for the music attribution scaffold API, showing five router groups — health check, Prometheus metrics, attribution CRUD with hybrid search, MCP-compatible permission checks, and CopilotKit AG-UI streaming endpoint — with CORS middleware and async PostgreSQL session management, providing the REST interface for transparent music credit confidence scoring.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture diagram of the FastAPI route map for the music attribution scaffold API, showing five router groups — health check, Prometheus metrics, attribution CRUD with hybrid search, MCP-compatible permission checks, and CopilotKit AG-UI streaming endpoint — with CORS middleware and async PostgreSQL session management, providing the REST interface for transparent music credit confidence scoring.](docs/figures/repo-figures/assets/fig-backend-16-fastapi-route-map.jpg)

*Figure 16. The Music Attribution API exposes five router groups under a single FastAPI application, including attribution CRUD with hybrid search (text + vector + graph), permission checks for AI training rights, and a CopilotKit AG-UI endpoint for conversational agent access.*

### From this figure plan (relative)

![Architecture diagram of the FastAPI route map for the music attribution scaffold API, showing five router groups — health check, Prometheus metrics, attribution CRUD with hybrid search, MCP-compatible permission checks, and CopilotKit AG-UI streaming endpoint — with CORS middleware and async PostgreSQL session management, providing the REST interface for transparent music credit confidence scoring.](../assets/fig-backend-16-fastapi-route-map.jpg)
