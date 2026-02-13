# fig-agent-01: Agentic UI Full Stack

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-agent-01 |
| **Title** | Agentic UI Full Stack: CopilotKit to PydanticAI Agent End-to-End |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 |
| **Location** | docs/architecture/agent.md, README.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the complete end-to-end agentic UI architecture from the user's browser to the database and back. It traces the path: CopilotKit Sidebar (React) -> AG-UI SSE protocol -> FastAPI /api/v1/copilotkit endpoint -> PydanticAI Agent with 4 tools -> PostgreSQL database -> response streamed back via SSE events. The DuetUI bidirectional context loop (UI state readable by agent, agent actions manipulating UI) is highlighted.

The key message is: "The agentic UI is a full-stack loop -- CopilotKit sends user messages via AG-UI SSE to a PydanticAI agent that queries the database with 4 domain tools, then streams responses back to update the sidebar and shared state."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  AGENTIC UI FULL STACK                                                 |
|  ■ End-to-End Architecture                                             |
+-----------------------------------------------------------------------+
|                                                                        |
|  FRONTEND (Next.js 15)                  BACKEND (FastAPI)              |
|  ──────────────────────                 ─────────────────              |
|                                                                        |
|  ┌──────────────────────┐              ┌──────────────────────┐       |
|  │  CopilotKit Provider  │              │  FastAPI Router       │       |
|  │  (layout.tsx)         │              │  /api/v1/copilotkit   │       |
|  └──────────┬───────────┘              └──────────┬───────────┘       |
|             │                                      │                   |
|             ▼                                      │                   |
|  ┌──────────────────────┐    AG-UI SSE            │                   |
|  │  CopilotSidebar      │ ═══════════════>        │                   |
|  │  "Ask about credits, │    POST /copilotkit     │                   |
|  │   confidence..."     │    { messages: [...] }   │                   |
|  └──────────────────────┘                         │                   |
|             ▲                                      ▼                   |
|             │                          ┌──────────────────────┐       |
|             │                          │  _generate_sse_events │       |
|             │                          │  (AG-UI adapter)      │       |
|             │                          └──────────┬───────────┘       |
|             │                                      │                   |
|             │                                      ▼                   |
|             │                          ┌──────────────────────┐       |
|             │                          │  PydanticAI Agent     │       |
|             │                          │  (lazy singleton)     │       |
|             │                          │  4 domain tools       │       |
|             │                          └──────────┬───────────┘       |
|             │                                      │                   |
|             │                                      ▼                   |
|  SSE EVENTS (streamed)                 ┌──────────────────────┐       |
|  ┌────────────────────┐               │  PostgreSQL           │       |
|  │ RunStarted          │               │  (async session)      │       |
|  │ TextMessageStart    │ <═══════════  │  AttributionRecord    │       |
|  │ TextMessageContent  │  chunked      │  FeedbackCard         │       |
|  │ TextMessageEnd      │  response     └──────────────────────┘       |
|  │ StateSnapshot       │                                               |
|  │ RunFinished         │                                               |
|  └────────────────────┘                                               |
|                                                                        |
|  DUET UI: BIDIRECTIONAL CONTEXT                                        |
|  ──────────────────────────────                                        |
|  UI → Agent: useCopilotReadable (role, selected work)                  |
|  Agent → UI: useCopilotAction (navigate, highlight, show diff)         |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "AGENTIC UI FULL STACK" in display font |
| CopilotKit Provider | `processing_stage` | CopilotKit wrapper in layout.tsx |
| CopilotSidebar | `api_endpoint` | Chat sidebar sending user messages |
| AG-UI SSE connection | `data_flow` | POST to /api/v1/copilotkit with messages payload |
| FastAPI router | `api_endpoint` | copilotkit_endpoint handler |
| SSE event generator | `processing_stage` | _generate_sse_events function |
| PydanticAI Agent | `processing_stage` | Lazy singleton with 4 tools |
| PostgreSQL | `storage_layer` | Async session factory for DB access |
| SSE event sequence | `data_mono` | RunStarted, TextMessage*, StateSnapshot, RunFinished |
| DuetUI bidirectional | `feedback_loop` | useCopilotReadable (UI->Agent) and useCopilotAction (Agent->UI) |

## Anti-Hallucination Rules

1. The endpoint is POST /api/v1/copilotkit (not /api/agent or /api/chat).
2. The protocol is AG-UI via Server-Sent Events (SSE), NOT WebSockets.
3. The agent is a lazy singleton created via _get_agent() in agui_endpoint.py.
4. The PydanticAI agent has exactly 4 tools: explain_confidence, search_attributions, suggest_correction, submit_feedback.
5. SSE event types: RunStarted, TextMessageStart, TextMessageContent, TextMessageEnd, StateSnapshot, RunFinished.
6. Response text is chunked at 50 characters for streaming feel.
7. The async session factory is obtained from request.app.state.async_session_factory.
8. DuetUI uses useCopilotReadable (3 hooks in use-attribution-context.ts) and useCopilotAction (4 actions in use-agent-actions.ts).
9. CopilotKit gracefully degrades to no-op when COPILOT_RUNTIME_URL env var is missing.

## Alt Text

End-to-end agentic UI: CopilotKit sidebar sends messages via AG-UI SSE to FastAPI, PydanticAI agent queries database, streams response back with state.
