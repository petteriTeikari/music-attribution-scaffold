# fig-voice-38: Tool Bridge Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-38 |
| **Title** | Tool Bridge Architecture |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md, Section 2.3 |
| **Priority** | P1 (Important) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Show how PydanticAI tools get converted via get_tool_schemas() to Pipecat FunctionSchema declarations, then wired via register_function() to the OpenAILLMService. The bridge crosses two SDKs; a figure shows where the boundary sits. Answers: "How do the existing text agent's tools become available in the voice pipeline?"

## Key Message

The tool bridge is a thin translation layer: PydanticAI tool definitions are converted to Pipecat FunctionSchema declarations, with register_function() wiring each tool handler to the LLM service. The session factory shares the database connection pool with the REST API.

## Visual Concept

Multi-panel (Template B). Left panel: "PYDANTICAI DOMAIN" showing 4 tool functions stacked vertically. Center bridge: get_tool_schemas() converting to FunctionSchema + register_function(). Right panel: "PIPECAT DOMAIN" showing OpenAILLMService with registered function handlers. Below: _session_factory arrow pointing to shared DB connection pool. Coral accent line marks the SDK boundary.

```
+-------------------------------------------------------------------+
|  TOOL BRIDGE ARCHITECTURE                                    [sq]   |
|  -- PydanticAI to Pipecat Translation Layer                        |
+-------------------------------------------------------------------+
|                                                                    |
|  PYDANTICAI DOMAIN          BRIDGE          PIPECAT DOMAIN         |
|  ──────────────────    ─────────────────    ───────────────────     |
|                              │                                      |
|  ┌──────────────────┐        │        ┌──────────────────┐         |
|  │ explain_confidence│        │        │ OpenAILLMService  │         |
|  │   (work_id)       │   get_tool_     │                  │         |
|  ├──────────────────┤   schemas()      │  Registered      │         |
|  │ search_            │   ──────>      │  Handlers:        │         |
|  │   attributions    │        │        │                  │         |
|  │   (query)          │   FunctionSchema│  ■ explain_conf  │         |
|  ├──────────────────┤   declarations   │  ■ search_attr   │         |
|  │ suggest_correction │        │        │  ■ suggest_corr  │         |
|  │   (work_id, field, │   register_    │  ■ submit_feed   │         |
|  │    current,        │   function()   │                  │         |
|  │    suggested,      │   ──────>      │  LLM calls tool  │         |
|  │    reason)         │        │        │  handler on      │         |
|  ├──────────────────┤        │        │  function_call   │         |
|  │ submit_feedback   │        │        │                  │         |
|  │   (work_id,        │        │        └──────────────────┘         |
|  │    overall_assess, │  [accent line                               |
|  │    free_text?)     │   SDK BOUNDARY]                              |
|  └──────────────────┘        │                                      |
|                              │                                      |
|  ─────────────────────────────────────────────── [accent line]     |
|                                                                    |
|  _session_factory ──────────> SHARED DB CONNECTION POOL             |
|  (voice tools + REST API share the same pool)                      |
|                                                                    |
+-------------------------------------------------------------------+
|  ELI5: Like a UN translator -- same ideas in two SDK languages,    |
|  get_tool_schemas() ensures both sides understand each other       |
+-------------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: primary_background

zones:
  - id: title_zone
    bounds: [0, 0, 1920, 120]
    content: "TOOL BRIDGE ARCHITECTURE"
    role: title

  - id: left_panel
    bounds: [60, 160, 600, 560]
    content: "PYDANTICAI DOMAIN"
    role: content_area

  - id: center_bridge
    bounds: [680, 160, 400, 560]
    content: "BRIDGE"
    role: content_area

  - id: right_panel
    bounds: [1100, 160, 600, 560]
    content: "PIPECAT DOMAIN"
    role: content_area

  - id: db_zone
    bounds: [60, 780, 1800, 100]
    role: content_area

  - id: callout_zone
    bounds: [60, 940, 1800, 100]
    content: "ELI5: Like a UN translator"
    role: callout_box

anchors:
  - id: tool_explain
    position: [340, 260]
    size: [480, 80]
    role: processing_stage
    label: "explain_confidence(work_id)"

  - id: tool_search
    position: [340, 360]
    size: [480, 80]
    role: processing_stage
    label: "search_attributions(query)"

  - id: tool_suggest
    position: [340, 460]
    size: [480, 80]
    role: processing_stage
    label: "suggest_correction(...)"

  - id: tool_feedback
    position: [340, 560]
    size: [480, 80]
    role: processing_stage
    label: "submit_feedback(...)"

  - id: get_tool_schemas
    position: [880, 320]
    size: [280, 60]
    role: data_flow
    label: "get_tool_schemas()"

  - id: function_schema
    position: [880, 400]
    size: [280, 60]
    role: data_flow
    label: "FunctionSchema declarations"

  - id: register_function
    position: [880, 480]
    size: [280, 60]
    role: data_flow
    label: "register_function()"

  - id: llm_service
    position: [1400, 400]
    size: [480, 360]
    role: processing_stage
    label: "OpenAILLMService"

  - id: sdk_boundary
    position: [680, 160]
    size: [4, 560]
    role: accent_line_v
    label: "SDK BOUNDARY"

  - id: session_factory
    position: [400, 820]
    size: [300, 50]
    role: data_flow
    label: "_session_factory"

  - id: db_pool
    position: [1200, 820]
    size: [400, 50]
    role: processing_stage
    label: "SHARED DB CONNECTION POOL"

  - id: flow_factory_to_pool
    from: session_factory
    to: db_pool
    type: arrow
    label: "shared connection"

  - id: flow_schemas_to_service
    from: register_function
    to: llm_service
    type: arrow
    label: "wire handlers"

  - id: divider_panels_db
    position: [60, 750]
    size: [1800, 2]
    role: accent_line
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "TOOL BRIDGE ARCHITECTURE" with coral accent square |
| explain_confidence tool | `processing_stage` | PydanticAI tool: explain_confidence(work_id) -> confidence decomposition |
| search_attributions tool | `processing_stage` | PydanticAI tool: search_attributions(query) -> attribution records |
| suggest_correction tool | `processing_stage` | PydanticAI tool: suggest_correction(work_id, field, current, suggested, reason) -> correction proposal |
| submit_feedback tool | `processing_stage` | PydanticAI tool: submit_feedback(work_id, overall_assessment, free_text?) -> FeedbackCard |
| get_tool_schemas() | `data_flow` | Conversion function: PydanticAI tool defs -> Pipecat FunctionSchema |
| register_function() | `data_flow` | Wiring function: connects each tool handler to OpenAILLMService |
| OpenAILLMService | `processing_stage` | Pipecat LLM service with registered function handlers |
| SDK boundary line | `accent_line_v` | Coral vertical line marking PydanticAI / Pipecat boundary |
| _session_factory | `data_flow` | Session factory shared between voice tools and REST API |
| Shared DB pool | `processing_stage` | Database connection pool used by both voice and REST contexts |
| Panel divider | `accent_line` | Coral line separating tool bridge from DB layer |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| PydanticAI tools | get_tool_schemas() | arrow | "extract definitions" |
| get_tool_schemas() | FunctionSchema | arrow | "convert format" |
| FunctionSchema | register_function() | arrow | "declare to service" |
| register_function() | OpenAILLMService | arrow | "wire handlers" |
| _session_factory | Shared DB pool | arrow | "shared connection" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Think of the tool bridge like a translator at a United Nations session: the same ideas (attribution tools) are expressed in two languages (PydanticAI for text, Pipecat for voice), and the translator (get_tool_schemas) ensures both sides understand each other perfectly. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "PYDANTICAI DOMAIN"
- Label 2: "PIPECAT DOMAIN"
- Label 3: "BRIDGE"
- Label 4: "explain_confidence(work_id)"
- Label 5: "search_attributions(query)"
- Label 6: "suggest_correction(...)"
- Label 7: "submit_feedback(...)"
- Label 8: "get_tool_schemas()"
- Label 9: "FunctionSchema declarations"
- Label 10: "register_function()"
- Label 11: "OpenAILLMService"
- Label 12: "SDK BOUNDARY"
- Label 13: "_session_factory"
- Label 14: "SHARED DB CONNECTION POOL"
- Label 15: "Registered Handlers"

### Caption (for embedding in documentation)

Tool bridge architecture showing PydanticAI tool definitions (explain_confidence, search_attributions, suggest_correction, submit_feedback) translated via get_tool_schemas() to Pipecat FunctionSchema declarations, wired to OpenAILLMService via register_function(), with a shared database connection pool between voice tools and the REST API.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `data_flow`, `accent_line_v` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon is ALLOWED** -- this is an L3 figure targeting software engineers. PydanticAI, Pipecat, FunctionSchema, register_function are appropriate.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The 4 tool names must exactly match the actual tool function names: explain_confidence, search_attributions, suggest_correction, submit_feedback.
10. The SDK boundary (PydanticAI <-> Pipecat) must be visually marked with a clear vertical divider -- this is the core insight of the figure.
11. Do NOT show tool implementation details -- only the declaration to registration flow. No function bodies, no return types beyond brief annotations.
12. The session factory must be shown as shared between voice tools and REST API -- it is a single pool, not separate connections.
13. get_tool_schemas() is a function that extracts tool definitions from PydanticAI and returns Pipecat-compatible FunctionSchema objects.
14. register_function() is called once per tool on the OpenAILLMService instance.

## Alt Text

Tool bridge architecture: four PydanticAI tools translated via get_tool_schemas to Pipecat FunctionSchema, wired to OpenAILLMService with shared DB pool.

## Image Embed

![Tool bridge architecture: four PydanticAI tools translated via get_tool_schemas to Pipecat FunctionSchema, wired to OpenAILLMService with shared DB pool.](docs/figures/repo-figures/assets/fig-voice-38-tool-bridge-architecture.jpg)

*Tool bridge architecture showing PydanticAI tool definitions (explain_confidence, search_attributions, suggest_correction, submit_feedback) translated via get_tool_schemas() to Pipecat FunctionSchema declarations, wired to OpenAILLMService via register_function(), with a shared database connection pool between voice tools and the REST API.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-38",
    "title": "Tool Bridge Architecture",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "The tool bridge translates PydanticAI tool definitions to Pipecat FunctionSchema declarations via get_tool_schemas(), with register_function() wiring handlers to OpenAILLMService and a shared DB connection pool.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "PydanticAI Domain",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["explain_confidence", "search_attributions", "suggest_correction", "submit_feedback"]
      },
      {
        "name": "Bridge Layer",
        "role": "data_flow",
        "is_highlighted": true,
        "labels": ["get_tool_schemas()", "FunctionSchema", "register_function()"]
      },
      {
        "name": "Pipecat Domain",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["OpenAILLMService", "Registered Handlers"]
      },
      {
        "name": "Shared DB Pool",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["_session_factory", "SHARED DB CONNECTION POOL"]
      }
    ],
    "relationships": [
      {
        "from": "PydanticAI tools",
        "to": "get_tool_schemas()",
        "type": "arrow",
        "label": "extract definitions"
      },
      {
        "from": "get_tool_schemas()",
        "to": "register_function()",
        "type": "arrow",
        "label": "FunctionSchema"
      },
      {
        "from": "register_function()",
        "to": "OpenAILLMService",
        "type": "arrow",
        "label": "wire handlers"
      },
      {
        "from": "_session_factory",
        "to": "Shared DB pool",
        "type": "arrow",
        "label": "shared connection"
      }
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Like a UN translator: same attribution tools expressed in two SDK languages, get_tool_schemas() ensures both sides understand each other.",
        "position": "bottom-center"
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
- [x] Anti-hallucination rules listed (8 default + 6 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L3)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
