# fig-choice-06: Why FastAPI over Django?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-06 |
| **Title** | Why FastAPI over Django? |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/planning/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains the service decomposition and framework choice. The scaffold uses FastAPI (modular monolith) because it provides async-native request handling, automatic OpenAPI documentation, native Pydantic integration (same models for validation and LLM structured output), and lightweight deployment. Django's batteries-included approach adds ORM and admin complexity that is unnecessary for a scaffold focused on API endpoints and MCP serving.

The key message is: "FastAPI's async-native, Pydantic-native design aligns perfectly with a scaffold that serves attribution data via REST and MCP -- no ORM baggage needed."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WHY FASTAPI OVER DJANGO?                                      |
|  ■ Service Decomposition: Modular Monolith                     |
+-------------------------------+-------------------------------+
|                               |                               |
|  FASTAPI (selected)           |  DJANGO                       |
|  ═══════════════════          |  ══════                       |
|                               |                               |
|  ■ Async-native               |  ■ Sync-first                 |
|    async def endpoints        |    ASGI via Daphne/Uvicorn    |
|    built on Starlette         |    bolt-on, not native        |
|                               |                               |
|  ■ Pydantic-native            |  ■ Serializers + Forms        |
|    Same models for API I/O    |    Separate DRF serializers   |
|    AND LLM structured output  |    from Django models         |
|                               |                               |
|  ■ Auto OpenAPI docs          |  ■ DRF generates OpenAPI      |
|    /docs endpoint for free    |    Additional dependency      |
|                               |                               |
|  ■ Lightweight                |  ■ Batteries-included         |
|    ~30 dependencies           |    Admin, ORM, templates,     |
|    Just what you need         |    auth, sessions, ...        |
|                               |                               |
|  ■ MCP endpoint natural       |  ■ MCP requires custom        |
|    SSE streaming native       |    ASGI middleware             |
|                               |                               |
|  ■ SQLAlchemy + Alembic       |  ■ Django ORM + Migrations    |
|    Explicit, separate         |    Tightly coupled            |
|                               |                               |
+-------------------------------+-------------------------------+
|  Scaffold routes: /health, /api/v1/attribution,                |
|  /api/v1/permissions, /api/v1/copilotkit                       |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WHY FASTAPI OVER DJANGO?" with coral accent square |
| FastAPI panel (left) | `selected_option` | Six advantage bullets: async, Pydantic, OpenAPI, lightweight, MCP, SQLAlchemy |
| Django panel (right) | `deferred_option` | Six corresponding Django characteristics |
| Vertical divider | `accent_line_v` | Coral red vertical line |
| Route examples footer | `callout_bar` | Actual API routes from the scaffold |

## Anti-Hallucination Rules

1. The scaffold uses FastAPI with routes at /health, /api/v1/attribution, /api/v1/permissions, /api/v1/copilotkit.
2. FastAPI is built on Starlette (ASGI) and uses Pydantic for request/response validation.
3. The scaffold uses SQLAlchemy + Alembic for database, NOT Django ORM.
4. MCP endpoint uses SSE streaming via the /api/v1/copilotkit route with AG-UI protocol.
5. Django is NOT rejected as a technology -- it is a viable option for teams that need admin panels and ORM.
6. The service decomposition decision selected "modular monolith" -- not microservices.
7. Do NOT claim FastAPI is categorically better than Django -- frame as trade-off for this specific use case.
8. Background must be warm cream (#f6f3e6).

## Alt Text

Comparison chart: FastAPI versus Django for music attribution API serving, highlighting async-native Pydantic integration and MCP endpoint streaming for transparent confidence scoring, with FastAPI selected as lightweight modular monolith over Django's batteries-included ORM approach in the open-source scaffold.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Comparison chart: FastAPI versus Django for music attribution API serving, highlighting async-native Pydantic integration and MCP endpoint streaming for transparent confidence scoring, with FastAPI selected as lightweight modular monolith over Django's batteries-included ORM approach in the open-source scaffold.](docs/figures/repo-figures/assets/fig-choice-06-fastapi-over-django.jpg)

*FastAPI's async-native, Pydantic-native design aligns with the music attribution scaffold's need for REST and MCP serving without ORM overhead, providing auto-generated OpenAPI docs and SSE streaming for the AG-UI agentic endpoint.*

### From this figure plan (relative)

![Comparison chart: FastAPI versus Django for music attribution API serving, highlighting async-native Pydantic integration and MCP endpoint streaming for transparent confidence scoring, with FastAPI selected as lightweight modular monolith over Django's batteries-included ORM approach in the open-source scaffold.](../assets/fig-choice-06-fastapi-over-django.jpg)
