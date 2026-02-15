# fig-repo-12: Backend-Frontend Connection

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-12 |
| **Title** | Backend-Frontend Connection: REST + AG-UI SSE |
| **Audience** | Technical (full-stack contributors) |
| **Complexity** | L3 (integration detail) |
| **Location** | docs/architecture/api.md, docs/architecture/agent.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

The frontend communicates with the backend through two channels: traditional REST API calls for CRUD operations, and AG-UI Server-Sent Events (SSE) for the conversational AI agent. This figure shows both communication paths, the endpoints involved, and how CopilotKit on the frontend connects to PydanticAI on the backend.

The key message is: "Two communication channels -- REST for data CRUD, AG-UI SSE for real-time AI conversation -- both flowing through FastAPI on port 8000."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  BACKEND-FRONTEND CONNECTION                                           |
|  ■ REST + AG-UI SSE: Two Channels, One Server                         |
+-----------------------------------------------------------------------+
|                                                                        |
|  FRONTEND (:3000)                    BACKEND (:8000)                   |
|  ─────────────────                   ──────────────                    |
|                                                                        |
|  ┌─────────────────┐                ┌──────────────────┐              |
|  │  Next.js 15     │                │  FastAPI          │              |
|  │                 │   I. REST      │                  │              |
|  │  fetch/SWR  ────│──── JSON ────▶ │  /api/v1/works   │              |
|  │                 │    GET/POST    │  /api/v1/health  │              |
|  │                 │                │  /api/v1/perms   │              |
|  │                 │                │                  │              |
|  │  ┌───────────┐ │   II. AG-UI    │  ┌────────────┐  │              |
|  │  │CopilotKit │ │                │  │ PydanticAI │  │              |
|  │  │ Provider  ├─│──── SSE ──────▶│  │ Agent      │  │              |
|  │  │           │ │  /api/v1/      │  │            │  │              |
|  │  │useCopilot │ │  copilotkit    │  │ 4 tools    │  │              |
|  │  │Readable   │ │                │  │ Haiku 4.5  │  │              |
|  │  │useCopilot │ │  ◀──── SSE ───│  │ + fallback │  │              |
|  │  │Action     │ │  stream events │  └────────────┘  │              |
|  │  └───────────┘ │                │                  │              |
|  └─────────────────┘                └──────────────────┘              |
|                                                                        |
|  ────────────────────────────────────────────────────                  |
|                                                                        |
|  ■ REST: Standard JSON request/response for works, permissions, health |
|  ■ AG-UI: Server-Sent Events for streaming AI agent conversation       |
|  ■ CORS: Frontend origin (localhost:3000) allowed via env var          |
|  ■ Agent model: claude-haiku-4-5 default, FallbackModel for failover  |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "BACKEND-FRONTEND CONNECTION" Instrument Serif ALL-CAPS |
| Frontend box | `system_box` | Next.js 15 container, port 3000 |
| Backend box | `system_box` | FastAPI container, port 8000 |
| REST channel | `channel_rest` | Labeled "I. REST", JSON arrows bidirectional |
| AG-UI channel | `channel_agui` | Labeled "II. AG-UI", SSE stream arrows |
| CopilotKit sub-box | `component_box` | Inside frontend, showing hooks |
| PydanticAI sub-box | `component_box` | Inside backend, showing agent config |
| REST endpoints | `data_mono` | /api/v1/works, /api/v1/health, /api/v1/perms |
| AG-UI endpoint | `data_mono` | /api/v1/copilotkit |
| Legend items | `feature_list` | Four items explaining each channel |
| Roman numerals I-II | `section_numeral` | Channel identifiers |
| Accent line divider | `accent_line` | Separating diagram from legend |

## Anti-Hallucination Rules

1. The AG-UI endpoint is `/api/v1/copilotkit`, not `/api/v1/chat` or `/ws/chat`.
2. Communication protocol is SSE (Server-Sent Events), not WebSocket.
3. CopilotKit hooks are `useCopilotReadable` and `useCopilotAction` -- not custom hooks.
4. PydanticAI agent has 4 tools (not more, not less).
5. Default model is `anthropic:claude-haiku-4-5`, with FallbackModel for failover.
6. Model is configurable via `ATTRIBUTION_AGENT_MODEL` environment variable.
7. Agent creation is lazy singleton (`_get_agent()`) to avoid requiring API key at import.
8. CORS is configured via `CORS_ORIGINS` environment variable.
9. REST endpoints are under `/api/v1/` prefix -- include health, works, permissions routes.
10. The backend serves BOTH REST and AG-UI from the same FastAPI application on port 8000.

## Alt Text

Architecture diagram: two communication channels connecting the music attribution scaffold frontend and backend -- REST JSON via FastAPI for music metadata CRUD operations on works, permissions, and health endpoints, and AG-UI Server-Sent Events for real-time PydanticAI agent conversation via CopilotKit with transparent confidence scoring queries, both served from a single FastAPI application on port 8000.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture diagram: two communication channels connecting the music attribution scaffold frontend and backend -- REST JSON via FastAPI for music metadata CRUD operations on works, permissions, and health endpoints, and AG-UI Server-Sent Events for real-time PydanticAI agent conversation via CopilotKit with transparent confidence scoring queries, both served from a single FastAPI application on port 8000.](docs/figures/repo-figures/assets/fig-repo-12-backend-frontend-connection.jpg)

*Figure 12. The backend-frontend integration uses dual communication channels: traditional REST for attribution data CRUD and AG-UI SSE for streaming AI agent conversation, with CopilotKit hooks (useCopilotReadable, useCopilotAction) on the frontend connecting to a PydanticAI agent with four tools and claude-haiku-4-5 default model on the backend.*

### From this figure plan (relative)

![Architecture diagram: two communication channels connecting the music attribution scaffold frontend and backend -- REST JSON via FastAPI for music metadata CRUD operations on works, permissions, and health endpoints, and AG-UI Server-Sent Events for real-time PydanticAI agent conversation via CopilotKit with transparent confidence scoring queries, both served from a single FastAPI application on port 8000.](../assets/fig-repo-12-backend-frontend-connection.jpg)
