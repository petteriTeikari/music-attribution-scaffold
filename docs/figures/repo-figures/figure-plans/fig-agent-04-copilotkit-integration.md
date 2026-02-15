# fig-agent-04: CopilotKit Integration

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-agent-04 |
| **Title** | CopilotKit Integration: Provider, Sidebar, and Bidirectional Hooks |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/agent.md, docs/architecture/frontend.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure details how CopilotKit is integrated into the frontend. It shows the CopilotProvider wrapping the app (with graceful degradation when runtime URL is missing), the CopilotSidebar component (styled with editorial labels), and the two hook families: useCopilotReadable (UI -> Agent context) and useCopilotAction (Agent -> UI manipulation). The DuetUI bidirectional context loop is the central concept.

The key message is: "CopilotKit provides bidirectional context between the UI and agent -- useCopilotReadable feeds the agent what the user is seeing, while useCopilotAction lets the agent manipulate the UI in response."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  COPILOTKIT INTEGRATION                                                |
|  ■ DuetUI Bidirectional Context                                        |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. PROVIDER (layout.tsx)                                              |
|  ────────────────────────                                              |
|                                                                        |
|  CopilotProvider (copilot-provider.tsx)                                 |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  if (!COPILOT_RUNTIME_URL) return <>{children}</>  // graceful   │  |
|  │  else return <CopilotKit runtimeUrl={url}>{children}</CopilotKit>│  |
|  └──────────────────────────────────────────────────────────────────┘  |
|                                                                        |
|  II. SIDEBAR (copilot-sidebar.tsx)                                     |
|  ─────────────────────────────────                                     |
|                                                                        |
|  AgentSidebar({ open, onOpenChange })                                  |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  CopilotSidebar (@copilotkit/react-ui)                           │  |
|  │  ■ title: "Attribution Agent"                                    │  |
|  │  ■ placeholder: "Ask about confidence scores, credits..."        │  |
|  │  ■ Toggled via coral accent button (fixed bottom-right)          │  |
|  └──────────────────────────────────────────────────────────────────┘  |
|                                                                        |
|  III. UI → AGENT (useCopilotReadable)                                  |
|  ────────────────────────────────────                                  |
|                                                                        |
|  useAttributionContext(selectedWork)                                    |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  useCopilotReadable("Current user role")                         │  |
|  │    value: "artist" | "query"  (from userRoleAtom)                │  |
|  │                                                                   │  |
|  │  useCopilotReadable("Currently selected attribution record")     │  |
|  │    value: { attribution_id, work_title, artist_name,             │  |
|  │             confidence_score, assurance_level,                    │  |
|  │             source_agreement, credits_count,                     │  |
|  │             needs_review, review_priority }                      │  |
|  └──────────────────────────────────────────────────────────────────┘  |
|                                                                        |
|  IV. AGENT → UI (useCopilotAction)                                     |
|  ─────────────────────────────────                                     |
|                                                                        |
|  useAgentActions(options)                                               |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  navigate_to_work(workId)        Navigate UI to specific work    │  |
|  │  highlight_credit(entityId)      Highlight credit entity         │  |
|  │  open_feedback_panel(workId)     Open feedback for attribution   │  |
|  │  show_correction_diff(field,     Show before/after diff          │  |
|  │    current, suggested)                                           │  |
|  └──────────────────────────────────────────────────────────────────┘  |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "COPILOTKIT INTEGRATION" in display font |
| CopilotProvider | `processing_stage` | Graceful degradation when URL missing |
| AgentSidebar | `api_endpoint` | CopilotSidebar with editorial labels |
| useCopilotReadable hooks | `data_flow` | UI->Agent: role and selected work context |
| Readable value shapes | `data_mono` | Exact field names passed to agent |
| useCopilotAction hooks | `feedback_loop` | Agent->UI: 4 named actions |
| Action descriptions | `label_editorial` | What each action does |
| Roman numerals I-IV | `section_numeral` | Section identifiers |

## Anti-Hallucination Rules

1. The CopilotProvider is in `frontend/src/lib/copilot/copilot-provider.tsx`.
2. It uses the @copilotkit/react-core package (CopilotKit component) and @copilotkit/react-ui (CopilotSidebar).
3. Graceful degradation: when COPILOT_RUNTIME_URL is falsy, children render without CopilotKit wrapping.
4. The sidebar title is "Attribution Agent" and placeholder is "Ask about confidence scores, credits, or attributions...".
5. There are exactly 2 useCopilotReadable calls in useAttributionContext: role and selected work.
6. There are exactly 4 useCopilotAction calls in useAgentActions: navigate_to_work, highlight_credit, open_feedback_panel, show_correction_diff.
7. The selected work readable passes 9 fields (attribution_id through review_priority), NOT the full AttributionRecord.
8. The agent toggle button is a coral square (bg-accent) fixed at bottom-right with a chat/close SVG icon.
9. useAttributionContext is in `frontend/src/hooks/use-attribution-context.ts`.
10. useAgentActions is in `frontend/src/hooks/use-agent-actions.ts`.

## Alt Text

Integration diagram: CopilotKit bidirectional context for music attribution showing the provider with graceful degradation, sidebar component for credit queries, useCopilotReadable hooks that feed user role and selected music metadata to the agent, and four useCopilotAction hooks enabling the agent to navigate works, highlight credits, and show transparent confidence scoring diffs in the agentic UI.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Integration diagram: CopilotKit bidirectional context for music attribution showing the provider with graceful degradation, sidebar component for credit queries, useCopilotReadable hooks that feed user role and selected music metadata to the agent, and four useCopilotAction hooks enabling the agent to navigate works, highlight credits, and show transparent confidence scoring diffs in the agentic UI.](docs/figures/repo-figures/assets/fig-agent-04-copilotkit-integration.jpg)

*CopilotKit DuetUI integration in the attribution scaffold frontend, illustrating the bidirectional context loop where useCopilotReadable sends user role and selected attribution record to the PydanticAI agent while useCopilotAction lets the agent manipulate the UI in response.*

### From this figure plan (relative)

![Integration diagram: CopilotKit bidirectional context for music attribution showing the provider with graceful degradation, sidebar component for credit queries, useCopilotReadable hooks that feed user role and selected music metadata to the agent, and four useCopilotAction hooks enabling the agent to navigate works, highlight credits, and show transparent confidence scoring diffs in the agentic UI.](../assets/fig-agent-04-copilotkit-integration.jpg)
