# fig-howto-04: How to Use the Agent Sidebar

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-howto-04 |
| **Title** | How to Use the Agent Sidebar |
| **Audience** | L1 (Music Industry Professional) |
| **Complexity** | L1 (concept introduction) |
| **Location** | docs/guides/agent-sidebar.md, README.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows how a non-technical user interacts with the AI agent sidebar to query attribution data using natural language. It presents the sidebar as a conversational interface where users ask questions about any work's attribution and receive structured, confidence-scored answers. It answers: "How do I talk to the system about music credits?"

The key message is: "Type a natural-language question in the sidebar, and the agent calls the right tools behind the scenes to return attribution data with confidence scores -- no API knowledge required."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  HOW TO USE THE AGENT SIDEBAR                                  |
|  ■ Ask About Any Work's Attribution                            |
+---------------------------------------------------------------+
|                                                                |
|  ┌──────────────────────────────────────────────────────────┐ |
|  │  MAIN APPLICATION                  │  AGENT SIDEBAR      │ |
|  │                                    │                      │ |
|  │  ┌──────────────────────────┐     │  I. ASK              │ |
|  │  │  Works Dashboard          │     │  ──────              │ |
|  │  │  ──────────────          │     │  ┌──────────────┐   │ |
|  │  │  Hide and Seek  ■ 0.87  │     │  │ "Who produced │   │ |
|  │  │  Headlock       ■ 0.72  │     │  │  Hide and     │   │ |
|  │  │  Goodnight...   ■ 0.41  │     │  │  Seek?"       │   │ |
|  │  │                          │     │  └──────────────┘   │ |
|  │  └──────────────────────────┘     │         │            │ |
|  │                                    │         v            │ |
|  │                                    │  II. TOOL CALLS      │ |
|  │                                    │  ───────────────     │ |
|  │                                    │  ■ lookup_work()     │ |
|  │                                    │  ■ get_attribution() │ |
|  │                                    │         │            │ |
|  │                                    │         v            │ |
|  │                                    │  III. RESPONSE       │ |
|  │                                    │  ──────────────      │ |
|  │                                    │  "Hide and Seek was  │ |
|  │                                    │   produced by Imogen │ |
|  │                                    │   Heap. Confidence:  │ |
|  │                                    │   0.87 (high).       │ |
|  │                                    │   Sources: MusicBrz, │ |
|  │                                    │   Discogs."          │ |
|  │                                    │                      │ |
|  └──────────────────────────────────────────────────────────┘ |
|                                                                |
+---------------------------------------------------------------+
|  ■ The agent uses the same tools as the API -- no magic       |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "HOW TO USE THE AGENT SIDEBAR" in Instrument Serif ALL-CAPS with coral accent square |
| Subtitle | `label_editorial` | "Ask About Any Work's Attribution" in Plus Jakarta Sans caps |
| Main application panel (left) | `solution_component` | Works dashboard showing three works with confidence scores |
| Agent sidebar panel (right) | `solution_component` | Three-step conversational flow: ask, tool calls, response |
| Step I: User query | `stakeholder_artist` | Natural language question in chat input field |
| Step II: Tool calls | `processing_stage` | Agent tool invocations shown as small badges (lookup_work, get_attribution) |
| Step III: Response | `final_score` | Natural language answer with confidence score and source list |
| Confidence scores in dashboard | `confidence_high` / `confidence_medium` / `confidence_low` | 0.87 (green), 0.72 (amber), 0.41 (red) |
| Flow arrows (I to II to III) | `data_flow` | Downward arrows within sidebar panel |
| Roman numerals I-III | `section_numeral` | Step headers in editorial style |
| Footer callout | `callout_box` | "The agent uses the same tools as the API" transparency note |

## Anti-Hallucination Rules

1. The agent sidebar is built with CopilotKit (AG-UI protocol) -- but do NOT show this technical detail in an L1 figure.
2. The agent has four tools, not two -- but showing two (lookup_work, get_attribution) is sufficient for the illustration.
3. The default agent model is `claude-haiku-4-5` -- do NOT mention model names in an L1 figure.
4. Confidence score 0.87 is in the high tier (>= 0.85) -- use green.
5. Confidence score 0.72 is in the medium tier (0.50-0.84) -- use amber.
6. Confidence score 0.41 is in the low tier (< 0.50) -- use red.
7. The works shown (Hide and Seek, Headlock, Goodnight and Go) are from the Imogen Heap mock dataset.
8. Voice agent features are Pro-tier only and should NOT be shown in this figure.
9. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Screenshot-style layout showing main application with works dashboard on left and agent sidebar on right with three-step flow: ask, tool calls, response.
