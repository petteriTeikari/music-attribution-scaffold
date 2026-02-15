# fig-supplementary-06: Agent Chat Sidebar

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-supplementary-06 |
| **Title** | Agent Chat Sidebar |
| **Audience** | L1 (Music Industry Professional) |
| **Location** | Supplementary materials, docs/figures/repo-figures/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:10 |
| **Layout Template** | A (Hero) |
| **Medium** | Frontend screenshot |

## Purpose

Shows the CopilotKit agent chat sidebar in action -- user asking about attribution confidence, agent responding with explanation. Answers: "How does the AI assistant explain attribution confidence in natural language?"

## Key Message

The AI agent sidebar answers attribution questions in natural language -- "Why is this work rated 0.87?" triggers a confidence breakdown showing source agreement, assurance level, and suggested actions.

## Visual Concept

Full browser screenshot of a work detail page with the CopilotKit chat sidebar open on the right. The sidebar shows at least one user message asking about confidence and an agent response explaining the confidence breakdown.

```
+--+-------------------------------------+--------------------+
|  |  HIDE AND SEEK                       | AGENT              |
|S |  Imogen Heap                         |                    |
|I |  ■                                   | You:               |
|D |                                      | Why is this work   |
|E |  CONFIDENCE    0.87                  | rated 0.87?        |
|B |  ████████████░░                      |                    |
|A |                                      | Agent:             |
|R |  ASSURANCE     A2 Corroborated       | "Hide and Seek"    |
|  |                                      | has a confidence   |
|  |  SOURCE PROVENANCE                   | of 0.87 because    |
|  |  ────────────────────                | 3 out of 3 sources |
|  |  MusicBrainz   0.91                  | agree on the       |
|  |  Discogs        0.84                 | primary credits.   |
|  |  AcoustID       0.79                 | MusicBrainz shows  |
|  |                                      | the highest match  |
|  |                                      | at 0.91...         |
|  |                                      |                    |
|  |                                      | [message input]    |
+--+-------------------------------------+--------------------+
```

## Screenshot Specification

| Parameter | Value |
|-----------|-------|
| **Browser** | Chrome / headless Chromium |
| **Viewport** | 1440 x 900 px |
| **Theme** | Light |
| **URL** | `localhost:3000/works/[id]` (work detail with sidebar open) |
| **State** | Chat sidebar open, at least one user message and one agent response visible |
| **Annotations** | Optional -- callout on agent tool usage display |
| **Device pixel ratio** | 1x (standard) |
| **Font loading** | Wait for all three font families to load |
| **Network** | Requires ANTHROPIC_API_KEY for live agent responses |
| **Scroll position** | Top of page |
| **API key** | If ANTHROPIC_API_KEY unavailable, capture graceful degradation state and note in Status |

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Work detail view | `content_area` | Background work detail page with confidence data |
| Chat sidebar panel | `sidebar_panel` | CopilotKit sidebar panel on the right side |
| User message | `chat_user` | User's question about attribution confidence |
| Agent response | `chat_agent` | Agent's natural language explanation of confidence |
| Message input | `chat_input` | Text input for composing new messages |
| Tool usage indicator | `tool_indicator` | Optional display showing which agent tool was used |
| Sidebar | `navigation` | 60px fixed left sidebar (separate from chat sidebar) |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| User message | Agent processing | arrow | "query sent to PydanticAI agent" |
| Agent tools | Work data | arrow | "explain_confidence tool reads work context" |
| useCopilotReadable | Agent context | arrow | "provides role and selected work context" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "AGENT TOOLS" | Optional annotation showing tool: explain_confidence | right-panel |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Agent Chat Sidebar"
- Label 2: "Confidence Explanation"
- Label 3: "Natural Language Q&A"
- Label 4: "PydanticAI + CopilotKit"

### Caption (for embedding in documentation)

The CopilotKit agent chat sidebar enables natural language attribution queries. Asking "Why is this work rated 0.87?" triggers the explain_confidence tool, which returns a source-by-source breakdown with assurance level context -- powered by PydanticAI with claude-haiku-4-5 default.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `chat_user`, `chat_agent`, `sidebar_panel` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. **This is a SCREENSHOT, not AI-generated.** Do NOT use Nano Banana Pro for this figure.
10. **Do NOT mock agent responses** -- capture actual or gracefully-degraded state.
11. CopilotKit sidebar uses `useCopilotReadable` for context (role, selected work) and `useCopilotAction` for UI manipulation.
12. Agent uses PydanticAI with `claude-haiku-4-5` default model. Four tools: `explain_confidence`, `search_attributions`, `suggest_correction`, `submit_feedback`.
13. The sidebar requires `ANTHROPIC_API_KEY` to function. If API key unavailable, capture the graceful degradation state (empty sidebar or "API key required" message).
14. The chat sidebar is the CopilotKit panel, NOT the fixed left navigation sidebar. Both are visible simultaneously -- left nav (60px) and right chat panel.
15. Agent responses should reference actual work data (confidence scores, source names, assurance levels) to demonstrate contextual awareness.

## Alt Text

Agent chat sidebar screenshot: natural language attribution confidence explanation

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "supplementary-06",
    "title": "Agent Chat Sidebar",
    "audience": "L1",
    "layout_template": "A",
    "medium": "frontend_screenshot"
  },
  "content_architecture": {
    "primary_message": "The AI agent sidebar answers attribution questions in natural language with source-by-source confidence breakdowns.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Work Detail Background",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["Confidence gauge", "Source provenance"]
      },
      {
        "name": "Chat Sidebar",
        "role": "sidebar_panel",
        "is_highlighted": true,
        "labels": ["User message", "Agent response"]
      },
      {
        "name": "Agent Response",
        "role": "chat_agent",
        "is_highlighted": true,
        "labels": ["Confidence breakdown", "Source agreement"]
      }
    ],
    "relationships": [
      {
        "from": "User Message",
        "to": "Agent Processing",
        "type": "arrow",
        "label": "query to PydanticAI agent"
      },
      {
        "from": "explain_confidence tool",
        "to": "Agent Response",
        "type": "arrow",
        "label": "source-by-source breakdown"
      }
    ],
    "callout_boxes": []
  },
  "screenshot_spec": {
    "browser": "Chrome/headless",
    "viewport": "1440x900",
    "theme": "light",
    "url": "localhost:3000/works/[id]",
    "state": "chat sidebar open, 1+ exchange visible",
    "annotations": "optional callout on tool usage",
    "api_key_required": "ANTHROPIC_API_KEY"  # pragma: allowlist secret
  }
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Screenshot specification defined (replaces spatial anchors)
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed (8 default + 7 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L1)
- [x] Layout template identified (A)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Frontend running and screenshot captured (requires ANTHROPIC_API_KEY for live agent)
- [ ] Quality reviewed
- [ ] Embedded in supplementary materials
