# fig-choice-02: Why CopilotKit + AG-UI?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-02 |
| **Title** | Why CopilotKit + AG-UI? |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/prd/decisions/REPORT.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains the agentic UI framework decision. The scaffold chose CopilotKit with AG-UI protocol over Vercel AI SDK, custom WebSocket, or REST polling. Shows the protocol comparison (AG-UI SSE streaming with 31 event types), the MCP integration, and the shared state model (useCopilotReadable/useCopilotAction).

The key message is: "CopilotKit + AG-UI provides open-source agentic UI with native MCP integration, 31-event streaming protocol, and bidirectional shared state -- the most complete open-source option."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WHY COPILOTKIT + AG-UI?                                       |
|  ■ Agentic UI Framework: copilotkit_agui (selected)            |
+---------------------------------------------------------------+
|                                                                |
|  ┌─────────────────────────────────────────────────────────┐   |
|  │  AG-UI PROTOCOL (31 Event Types)                        │   |
|  │  ═══════════════════════════════                        │   |
|  │  Frontend ←──── SSE Stream ────→ Backend Agent          │   |
|  │                                                         │   |
|  │  Events: TextMessage | ToolCall | StateSync |           │   |
|  │          RunStart | RunEnd | Error | ...                │   |
|  └─────────────────────────────────────────────────────────┘   |
|                                                                |
|  COMPARISON                                                    |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │ CopilotKit   │ │ Vercel AI    │ │ Custom WS    │          |
|  │ + AG-UI      │ │ SDK          │ │              │          |
|  │ ■ SELECTED   │ │              │ │              │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ Open-source  │ │ Vercel-tied  │ │ Full control │          |
|  │ 28.7k stars  │ │ Ecosystem    │ │ Full effort  │          |
|  │              │ │ lock-in      │ │              │          |
|  │ MCP native   │ │ No MCP      │ │ Build MCP    │          |
|  │ (Jan 2026)   │ │              │ │ from scratch │          |
|  │              │ │              │ │              │          |
|  │ Shared state │ │ Streaming    │ │ Manual state │          |
|  │ bidirectional│ │ only         │ │ sync         │          |
|  │              │ │              │ │              │          |
|  │ CoAgents for │ │ React Server │ │ N/A          │          |
|  │ LangGraph    │ │ Components   │ │              │          |
|  │              │ │              │ │              │          |
|  │ P=0.50       │ │ P=0.25      │ │ P=0.15      │          |
|  └──────────────┘ └──────────────┘ └──────────────┘          |
|                                                                |
+---------------------------------------------------------------+
|  Key hook: useCopilotReadable (share state) +                  |
|  useCopilotAction (register tool-callable actions)             |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WHY COPILOTKIT + AG-UI?" with coral accent square |
| AG-UI protocol banner | `api_endpoint` | Protocol overview showing SSE streaming with 31 event types |
| CopilotKit card | `selected_option` | Open-source, 28.7k stars, MCP native, shared state, CoAgents |
| Vercel AI SDK card | `deferred_option` | Vercel ecosystem, streaming, React Server Components |
| Custom WebSocket card | `deferred_option` | Full control, full effort, no MCP |
| Probability labels | `data_mono` | Prior probabilities: 0.50, 0.25, 0.15 |
| React hooks callout | `callout_bar` | useCopilotReadable and useCopilotAction hook descriptions |

## Anti-Hallucination Rules

1. CopilotKit has 28.7k GitHub stars -- per the agentic_ui_framework decision node.
2. AG-UI protocol has 31 event types -- per the decision node description.
3. MCP integration shipped January 2026 -- per the decision node.
4. Prior probabilities: copilotkit_agui 0.50, vercel_ai_sdk 0.25, custom_agent_ui 0.15, no_agentic_ui 0.25.
5. P(CopilotKit | MCP Primary) = 0.55 -- from the conditional table.
6. P(CopilotKit | Next.js) = 0.50 -- from the conditional table.
7. CopilotKit requires Next.js/React -- this is a hard dependency.
8. CoAgents provides LangGraph interop -- per the decision node description.
9. Do NOT claim Vercel AI SDK lacks streaming -- it has strong streaming. The difference is MCP integration and open-source governance.
10. Background must be warm cream (#f6f3e6).

## Alt Text

Three-card comparison of agentic UI frameworks: CopilotKit with AG-UI selected for open-source governance, MCP integration, and bidirectional shared state.
