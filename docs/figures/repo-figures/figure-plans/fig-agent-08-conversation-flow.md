# fig-agent-08: Agent Conversation Flow

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-agent-08 |
| **Title** | Agent Conversation Flow: Example Interaction with Tool Calls and State Updates |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 |
| **Location** | docs/architecture/agent.md, README.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows a complete example conversation between a user and the Attribution Agent. The user asks about "Hide and Seek" confidence -- the agent calls search_attributions to find the work, then explain_confidence to break down the score, and finally suggests a correction. Each step shows the tool called, the state updated, and the UI response. This makes the agentic loop tangible.

The key message is: "A single conversation can chain multiple tool calls -- search to find, explain to understand, suggest to improve -- with shared state updating the UI at each step so the user sees live context changes."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  AGENT CONVERSATION FLOW                                               |
|  ■ Example: "Tell me about Hide and Seek"                              |
+-----------------------------------------------------------------------+
|                                                                        |
|  TURN 1: USER                                                         |
|  ─────────────                                                         |
|  "What's the confidence score for Hide and Seek?"                      |
|                                                                        |
|       │                                                                |
|       ▼                                                                |
|  AGENT: search_attributions("Hide and Seek")                           |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  → Found 1 result:                                                │  |
|  │    - Hide and Seek by Imogen Heap (confidence: 92%, A3)          │  |
|  │                                                                   │  |
|  │  State: last_search_query="Hide and Seek", last_search_count=1   │  |
|  └──────────────────────────────────────────────────────────────────┘  |
|       │                                                                |
|       ▼                                                                |
|  AGENT: explain_confidence(work_id="550e8400...")                      |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  → Confidence score: 92%.                                         │  |
|  │    High source agreement (95%).                                   │  |
|  │    Data from 3 source(s): MUSICBRAINZ, DISCOGS, ARTIST_INPUT.   │  |
|  │    Assurance level: LEVEL_3.                                      │  |
|  │                                                                   │  |
|  │  State: current_work_id=..., confidence_score=0.92,               │  |
|  │         explanation_text="..."                                    │  |
|  └──────────────────────────────────────────────────────────────────┘  |
|       │                                                                |
|       ▼                                                                |
|  AGENT RESPONSE (streamed via SSE):                                    |
|  "Hide and Seek by Imogen Heap has a confidence score of 92%.          |
|   This is a high-confidence attribution with:                          |
|   - High source agreement (95%) across 3 sources                      |
|   - MusicBrainz, Discogs, and artist input all corroborate            |
|   - Artist-verified (A3) assurance level"                              |
|                                                                        |
|  ═══════════════════════════════════════════════════════════════       |
|                                                                        |
|  TURN 2: USER                                                         |
|  ─────────────                                                         |
|  "Are there any credits that need improvement?"                        |
|                                                                        |
|       │                                                                |
|       ▼                                                                |
|  AGENT: suggest_correction(work_id=..., field="mixing_engineer",       |
|    current="Unknown", suggested="Guy Sigsworth", reason="MusicBrainz   |
|    credits list Guy Sigsworth as mixing engineer on Speak for           |
|    Yourself sessions")                                                 |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  State: pending_correction = CorrectionPreview(...)               │  |
|  │  UI: show_correction_diff action fires                            │  |
|  └──────────────────────────────────────────────────────────────────┘  |
|                                                                        |
|  UI SIDEBAR UPDATES AT EACH STEP                                       |
|  ────────────────────────────────                                      |
|  ■ StateSnapshot after each tool → CopilotKit reads via hooks          |
|  ■ UI can highlight the work, show confidence breakdown, show diff     |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "AGENT CONVERSATION FLOW" in display font |
| User turn 1 | `stakeholder_artist` | Natural language question about confidence |
| search_attributions call | `etl_extract` | Tool call with query and result |
| explain_confidence call | `source_corroborate` | Tool call with work_id and factor breakdown |
| Agent response | `final_score` | Streamed natural language summary |
| User turn 2 | `stakeholder_artist` | Follow-up about improvements |
| suggest_correction call | `feedback_loop` | Tool call with correction preview |
| State updates | `data_mono` | AttributionAgentState fields updated at each step |
| UI sidebar note | `callout_box` | StateSnapshot drives CopilotKit hook updates |
| Turn separators | `accent_line` | Visual separator between conversation turns |

## Anti-Hallucination Rules

1. The example uses "Hide and Seek" by Imogen Heap -- the project's persona.
2. Tool calls chain: search_attributions -> explain_confidence -> suggest_correction.
3. Each tool call updates specific fields on AttributionAgentState (documented in code).
4. The agent response is streamed via SSE TextMessageContent events (chunked at 50 chars).
5. StateSnapshot is emitted after the response, not between tool calls.
6. The suggest_correction tool creates a CorrectionPreview (not a final correction).
7. The confidence score example is 92% (0.92) -- consistent with the Imogen Heap mock data.
8. Source agreement of 95% is consistent with the mock data for Hide and Seek.

## Alt Text

Two-turn agent conversation: user asks about Hide and Seek, agent chains search and explain tools, then suggests a correction with state updates at each step.
