# fig-repo-04: Technology Stack

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-04 |
| **Title** | Technology Stack: Backend + Frontend at a Glance |
| **Audience** | All (evaluators, contributors) |
| **Complexity** | L1 (reference card) |
| **Location** | README.md, docs/architecture/README.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

A clean reference card showing every major technology used in the project, organized by layer. This serves as a quick "what do I need to know?" for new contributors and evaluators assessing the technical choices. The asymmetric two-column layout separates backend (Python) from frontend (TypeScript) with shared infrastructure at the bottom.

The key message is: "A modern Python 3.13 + Next.js 15 stack with PostgreSQL, PydanticAI, and CopilotKit -- every dependency is deliberate and documented in the PRD decision network."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  TECHNOLOGY STACK                                                      |
|  ■ Backend + Frontend at a Glance                                      |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. BACKEND (PYTHON 3.13)          II. FRONTEND (TYPESCRIPT)          |
|  ─────────────────────────          ─────────────────────────          |
|                                                                        |
|  Framework     FastAPI 0.115        Framework    Next.js 15            |
|  ORM           SQLAlchemy 2.0       State        Jotai                 |
|  Validation    Pydantic v2          Styling      Tailwind CSS v4       |
|  AI Agent      PydanticAI           Agent UI     CopilotKit (AG-UI)    |
|  MCP Server    mcp-python           Analytics    PostHog               |
|  DB            PostgreSQL 17        Testing      Vitest + RTL          |
|  Vectors       pgvector             E2E          Playwright            |
|  Migrations    Alembic              Fonts        Instrument Serif      |
|  Audio         tinytag                           Plus Jakarta Sans     |
|  Search        Splink v4                         IBM Plex Mono         |
|  ─────────────────────────          ─────────────────────────          |
|                                                                        |
|  III. SHARED INFRASTRUCTURE                                            |
|  ──────────────────────────                                            |
|                                                                        |
|  Package Mgr   uv (Python)          Docker       Compose + prod image |
|                npm (Frontend)        Cache        Valkey (Redis-compat) |
|  Linter        ruff                  Pooler       PgBouncer            |
|  Type Check    mypy                  Monitoring   Prometheus + Grafana |
|  Pre-commit    7 hooks               CI           GitHub Actions       |
|  Secrets       detect-secrets        Coverage     Codecov              |
|                                                                        |
+-----------------------------------------------------------------------+
|  "Every dependency is a deliberate PRD decision, not an accident."     |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "TECHNOLOGY STACK" Instrument Serif ALL-CAPS |
| Backend column | `column_backend` | Left panel, wider allocation (~55%) |
| Frontend column | `column_frontend` | Right panel (~45%) |
| Infrastructure row | `infrastructure_bar` | Full-width bottom section |
| Technology names | `label_editorial` | Plus Jakarta Sans, left-aligned category |
| Technology values | `data_mono` | IBM Plex Mono, right-aligned value |
| Roman numerals I-III | `section_numeral` | Section identifiers |
| Accent squares | `accent_square` | Coral squares marking each section |
| Horizontal dividers | `accent_line` | Coral lines separating sections |
| Footer quote | `callout_quote` | Italic editorial quote |

## Anti-Hallucination Rules

1. Python version is 3.13, not 3.11 or 3.12.
2. Package manager is uv for Python, npm for frontend -- NEVER pip or conda.
3. Audio library is tinytag (not mutagen -- mutagen was replaced due to licensing).
4. AI agent framework is PydanticAI (not LangChain, not LlamaIndex, not CrewAI).
5. Frontend state management is Jotai (not Redux, not Zustand, not React Context).
6. Agent UI protocol is AG-UI via CopilotKit (not raw WebSocket or custom SSE).
7. Analytics is PostHog (not Mixpanel, not Amplitude, not Google Analytics).
8. The ORM is SQLAlchemy 2.0 (async), not Django ORM or Tortoise.
9. Entity resolution uses Splink v4, not custom fuzzy matching.
10. Cache is Valkey (Redis-compatible fork), not Redis itself.
11. Connection pooler is PgBouncer, not pgpool-II.

## Alt Text

Technology stack reference card: Python 3.13 backend with FastAPI, SQLAlchemy, PydanticAI; TypeScript frontend with Next.js 15, Jotai, CopilotKit; shared infrastructure with uv, Docker, GitHub Actions.
