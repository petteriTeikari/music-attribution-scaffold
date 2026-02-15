# fig-ecosystem-09: Agent Interoperability Protocol Stack

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-09 |
| **Title** | Agent Interoperability Protocol Stack |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:10 |
| **Layout Template** | E (Steps/Vertical) |

## Purpose

Shows the progressive adoption path for agent interoperability protocols: starting with MCP tool access at MVP, scaling through A2A agent coordination, and ultimately enabling agentic commerce via ACP. Answers: "How do protocol layers build on each other, and what does each unlock?"

## Key Message

Progressive protocol adoption -- start with MCP tool access (MVP), add A2A agent coordination (scale), enable agentic commerce via ACP (monetize) -- each layer builds on the previous.

## Visual Concept

Three vertical stages ascending from bottom to top, each representing a progressively more capable protocol layer. A feedback arc curves from the top commerce layer back down to the tool access layer, representing how commercial signals inform tool design. Each stage has a Roman numeral, phase label, and key capabilities.

```
+---------------------------------------------------------------+
|  AGENT INTEROPERABILITY PROTOCOL STACK                         |
|  -- Progressive Adoption Path                                  |
+---------------------------------------------------------------+
|                                                                |
|  III. AGENTIC COMMERCE (aspirational)                          |
|  ┌─────────────────────────────────────────────────────┐      |
|  │  ACP (OpenAI + Stripe)                               │      |
|  │  Payment negotiation, agent-to-agent billing          │      |
|  │  XAA (Okta) identity layer (contested)               │      |
|  │  Phase: MONETIZE                                     │      |
|  └──────────────────────┬──────────────────────────────┘      |
|                         │                                      |
|            ┌────────────┘                                      |
|            ▼                                                   |
|  II. A2A COORDINATION (future)                                 |
|  ┌─────────────────────────────────────────────────────┐      |
|  │  A2A (Google, Linux Foundation)                      │      |
|  │  Multi-agent task delegation, capability discovery    │      |
|  │  Agent-to-agent negotiation                          │      |
|  │  Phase: SCALE                                        │      |
|  └──────────────────────┬──────────────────────────────┘      |
|                         │                                      |
|            ┌────────────┘                                      |
|            ▼                                                   |
|  I. MCP TOOL ACCESS (current MVP)                              |
|  ┌─────────────────────────────────────────────────────┐      |
|  │  MCP (AAIF / Linux Foundation)                       │      |
|  │  Tool discovery, permission queries, consent infra    │      |
|  │  Machine-readable training rights                    │      |
|  │  Phase: BUILD                                        │      |
|  └─────────────────────────────────────────────────────┘      |
|                                                                |
|  ╭───── FEEDBACK ARC ──────────────────────────────────╮      |
|  │  Commerce signals inform tool design + permissions   │      |
|  ╰──────────────────────────────────────────────────────╯      |
|                                                                |
+---------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1200
  background: primary_background

zones:
  - id: title_zone
    bounds: [0, 0, 1920, 130]
    content: "AGENT INTEROPERABILITY PROTOCOL STACK"
    role: title

  - id: stage_iii_zone
    bounds: [120, 160, 1680, 240]
    role: content_area

  - id: stage_ii_zone
    bounds: [120, 440, 1680, 240]
    role: content_area

  - id: stage_i_zone
    bounds: [120, 720, 1680, 240]
    role: content_area

  - id: feedback_zone
    bounds: [120, 1000, 1680, 120]
    role: callout_box

anchors:
  - id: stage_iii
    position: [960, 280]
    size: [1500, 200]
    role: processing_stage
    label: "III. AGENTIC COMMERCE"

  - id: stage_ii
    position: [960, 560]
    size: [1500, 200]
    role: processing_stage
    label: "II. A2A COORDINATION"

  - id: stage_i
    position: [960, 840]
    size: [1500, 200]
    role: processing_stage
    label: "I. MCP TOOL ACCESS"

  - id: flow_i_to_ii
    from: stage_i
    to: stage_ii
    type: arrow
    label: "protocol foundation"

  - id: flow_ii_to_iii
    from: stage_ii
    to: stage_iii
    type: arrow
    label: "coordination enables commerce"

  - id: feedback_arc
    from: stage_iii
    to: stage_i
    type: dashed
    label: "commerce signals inform tool design"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "AGENT INTEROPERABILITY PROTOCOL STACK" with coral accent square |
| Stage III -- Agentic Commerce | `processing_stage` | ACP (OpenAI + Stripe), payment negotiation, XAA identity (contested) |
| Stage II -- A2A Coordination | `processing_stage` | A2A (Google/Linux Foundation), multi-agent delegation, capability discovery |
| Stage I -- MCP Tool Access | `processing_stage` | MCP (AAIF/Linux Foundation), tool discovery, permission queries, consent |
| Phase labels | `label_editorial` | BUILD, SCALE, MONETIZE as phase indicators |
| Feedback arc | `feedback_loop` | Commerce signals informing tool design and permissions |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Stage I (MCP) | Stage II (A2A) | arrow | "protocol foundation" |
| Stage II (A2A) | Stage III (ACP) | arrow | "coordination enables commerce" |
| Stage III (ACP) | Stage I (MCP) | dashed | "commerce signals inform tool design" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "CURRENT STATE" | MCP is the only implemented layer in this scaffold | bottom-left |
| "IDENTITY LAYER" | XAA (Okta) identity is contested -- not yet standardized | right-margin |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "MCP TOOL ACCESS"
- Label 2: "A2A COORDINATION"
- Label 3: "AGENTIC COMMERCE"
- Label 4: "BUILD"
- Label 5: "SCALE"
- Label 6: "MONETIZE"
- Label 7: "FEEDBACK ARC"

### Caption (for embedding in documentation)

Progressive protocol adoption for agent interoperability -- MCP tool access (current MVP) provides the foundation for A2A coordination (future scaling) and ACP agentic commerce (monetization), with each layer building on the previous and a feedback arc from commerce back to tool design.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `feedback_loop`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PRD nodes: `agent_interop_protocol`, `agentic_commerce_protocol`. These are the decision nodes driving this figure.
10. MCP is now under AAIF (AI Alliance Infrastructure Foundation) / Linux Foundation -- NOT Anthropic-exclusive.
11. A2A is Google's protocol, also contributed to the Linux Foundation.
12. ACP is OpenAI + Stripe -- Agent Commerce Protocol for payment negotiation.
13. XAA (Okta) is an identity layer -- its standardization is contested; do NOT present as settled.
14. Parent edges: `api_protocol` -> `agent_interop_protocol` (strong), `ai_framework_strategy` -> `agent_interop_protocol` (moderate).
15. Only MCP is currently implemented in the scaffold. A2A and ACP are future/aspirational.
16. Do NOT imply any protocol has "won" -- the ecosystem is actively evolving.

## Alt Text

Protocol stack: MCP tool access to A2A coordination to agentic commerce layers

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-09",
    "title": "Agent Interoperability Protocol Stack",
    "audience": "L2",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Progressive protocol adoption -- start with MCP tool access (MVP), add A2A agent coordination (scale), enable agentic commerce via ACP (monetize) -- each layer builds on the previous.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Stage III -- Agentic Commerce",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["AGENTIC COMMERCE", "ACP", "MONETIZE"]
      },
      {
        "name": "Stage II -- A2A Coordination",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["A2A COORDINATION", "A2A", "SCALE"]
      },
      {
        "name": "Stage I -- MCP Tool Access",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["MCP TOOL ACCESS", "MCP", "BUILD"]
      }
    ],
    "relationships": [
      {
        "from": "Stage I",
        "to": "Stage II",
        "type": "arrow",
        "label": "protocol foundation"
      },
      {
        "from": "Stage II",
        "to": "Stage III",
        "type": "arrow",
        "label": "coordination enables commerce"
      },
      {
        "from": "Stage III",
        "to": "Stage I",
        "type": "dashed",
        "label": "commerce signals inform tool design"
      }
    ],
    "callout_boxes": [
      {
        "heading": "CURRENT STATE",
        "body_text": "MCP is the only implemented layer in this scaffold",
        "position": "bottom-left"
      },
      {
        "heading": "IDENTITY LAYER",
        "body_text": "XAA (Okta) identity is contested -- not yet standardized",
        "position": "right-margin"
      }
    ]
  }
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed (8 default + 8 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L2)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
