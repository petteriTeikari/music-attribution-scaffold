# fig-trends-03: Agent Observability: OTel GenAI Stack

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-trends-03 |
| **Title** | Agent Observability: OTel GenAI Stack |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/tech-trends-agentic-infrastructure-2026.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Shows the observability data flow from PydanticAI agent through Logfire to any OTel-compatible backend. Demonstrates that the scaffold's observability is standards-based with no vendor lock-in. Answers: "How do I monitor agent behavior in production?"

## Key Message

PydanticAI agents emit OpenTelemetry spans natively via Logfire -- tool calls, model invocations, and validation errors flow through standard OTel pipelines to any compatible backend, avoiding vendor lock-in.

## Visual Concept

Top-to-bottom flowchart. Agent layer at top emitting spans, Logfire instrumentation in the middle, fan-out to multiple backends at bottom. Side panel shows GenAI semantic conventions.

```
+-----------------------------------------------------------------------+
|  AGENT OBSERVABILITY: OTEL GENAI STACK                                 |
|  ■ Standards-based, zero vendor lock-in                                |
+-----------------------------------------------------------------------+
|                                                                        |
|  PYDANTICAI AGENT                                                      |
|  ┌────────────────────────────────────────────────────┐               |
|  │  tool_call spans  │  model_invoke spans  │ errors  │               |
|  └──────────┬─────────────────┬──────────────┬────────┘               |
|             │                 │              │                          |
|             ▼                 ▼              ▼                          |
|  ┌────────────────────────────────────────────────────┐               |
|  │  PYDANTIC LOGFIRE                                   │               |
|  │  OTel-native instrumentation                        │  ┌─────────┐ |
|  │  Auto span creation for agent lifecycle             │  │ GenAI   │ |
|  │  Token counting, latency, error classification      │  │ SEMANTIC│ |
|  └──────────┬─────────────────┬──────────────┬────────┘  │ CONVNTNS│ |
|             │                 │              │            │─────────│ |
|             ▼                 ▼              ▼            │model.nm │ |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐     │token.ct │ |
|  │   Grafana    │ │   Datadog    │ │  Honeycomb   │     │tool.inv │ |
|  │              │ │              │ │              │     │latency  │ |
|  └──────────────┘ └──────────────┘ └──────────────┘     └─────────┘ |
|  ┌──────────────┐                                                     |
|  │ Self-hosted  │                                                     |
|  │   Jaeger     │                                                     |
|  └──────────────┘                                                     |
|                                                                        |
+-----------------------------------------------------------------------+
|  PRD: agent_observability_otel                                         |
|  Parents: ai_framework_strategy, build_vs_buy_posture                  |
+-----------------------------------------------------------------------+
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
    content: "AGENT OBSERVABILITY: OTEL GENAI STACK"
    role: title

  - id: agent_layer
    bounds: [200, 160, 1200, 120]
    content: "PYDANTICAI AGENT"
    role: content_area

  - id: logfire_layer
    bounds: [200, 380, 1200, 160]
    content: "PYDANTIC LOGFIRE"
    role: content_area

  - id: backend_layer
    bounds: [200, 660, 1200, 240]
    content: "BACKENDS"
    role: content_area

  - id: conventions_panel
    bounds: [1480, 380, 360, 280]
    content: "GenAI SEMANTIC CONVENTIONS"
    role: callout_box

  - id: prd_bar
    bounds: [60, 960, 1800, 80]
    content: "PRD reference"
    role: callout_box

anchors:
  - id: agent_block
    position: [260, 180]
    size: [1080, 80]
    role: processing_stage

  - id: tool_span
    position: [260, 200]
    size: [320, 40]
    role: processing_stage

  - id: model_span
    position: [620, 200]
    size: [320, 40]
    role: processing_stage

  - id: error_span
    position: [980, 200]
    size: [320, 40]
    role: processing_stage

  - id: logfire_block
    position: [260, 400]
    size: [1080, 120]
    role: processing_stage

  - id: flow_agent_to_logfire
    from: agent_block
    to: logfire_block
    type: arrow
    label: "OTel spans"

  - id: grafana_backend
    position: [260, 680]
    size: [300, 120]
    role: storage_layer

  - id: datadog_backend
    position: [600, 680]
    size: [300, 120]
    role: storage_layer

  - id: honeycomb_backend
    position: [940, 680]
    size: [300, 120]
    role: storage_layer

  - id: jaeger_backend
    position: [260, 820]
    size: [300, 80]
    role: storage_layer

  - id: flow_logfire_to_backends
    from: logfire_block
    to: grafana_backend
    type: arrow
    label: "OTLP export"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| PydanticAI Agent | `processing_stage` | Top layer emitting tool_call, model_invoke, and error spans |
| Pydantic Logfire | `processing_stage` | Middle layer with OTel-native instrumentation and auto span creation |
| Backend options | `storage_layer` | Fan-out to Grafana, Datadog, Honeycomb, self-hosted Jaeger |
| GenAI Conventions panel | `callout_box` | Side panel listing semantic convention attributes |
| PRD reference bar | `callout_box` | Bottom bar with node name and parent dependencies |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| PydanticAI Agent | Pydantic Logfire | arrow | "OTel spans" |
| Pydantic Logfire | Grafana | arrow | "OTLP export" |
| Pydantic Logfire | Datadog | arrow | "OTLP export" |
| Pydantic Logfire | Honeycomb | arrow | "OTLP export" |
| Pydantic Logfire | Jaeger | arrow | "OTLP export" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "GenAI SEMANTIC CONVENTIONS" | model.name, token.count, tool.invocation, latency | right-margin |
| "PRD REFERENCE" | agent_observability_otel. Parents: ai_framework_strategy (moderate), build_vs_buy_posture (moderate) | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "PYDANTICAI AGENT"
- Label 2: "tool_call spans"
- Label 3: "model_invoke spans"
- Label 4: "validation errors"
- Label 5: "PYDANTIC LOGFIRE"
- Label 6: "OTel-native instrumentation"
- Label 7: "Auto span creation"
- Label 8: "Token counting"
- Label 9: "Grafana"
- Label 10: "Datadog"
- Label 11: "Honeycomb"
- Label 12: "Self-hosted Jaeger"

### Caption (for embedding in documentation)

PydanticAI agents emit OpenTelemetry spans via Logfire, flowing through standard OTLP pipelines to any compatible backend -- Grafana, Datadog, Honeycomb, or self-hosted Jaeger.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `storage_layer`, `callout_box` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. OTel GenAI semantic conventions are on the experimental-to-stable track -- do NOT claim they are fully stable.
10. AG2 integrated OTel in Feb 2026 -- this is a separate fact, not about PydanticAI's integration.
11. Pydantic Logfire provides OTel-native observability specifically for PydanticAI -- it is not a generic OTel collector.
12. PRD node: agent_observability_otel. Parents: ai_framework_strategy (moderate), build_vs_buy_posture (moderate).
13. Do NOT claim the scaffold currently has Logfire deployed -- this is the intended observability architecture.
14. The fan-out to backends uses standard OTLP export -- do NOT invent proprietary integration paths.
15. GenAI semantic conventions include: model name, token counts, tool invocations -- these are real convention attributes.

## Alt Text

OTel GenAI stack: PydanticAI to Logfire to any OpenTelemetry-compatible backend

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "trends-03",
    "title": "Agent Observability: OTel GenAI Stack",
    "audience": "L3",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "PydanticAI agents emit OTel spans via Logfire to any compatible backend, avoiding vendor lock-in.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "PydanticAI Agent",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["tool_call spans", "model_invoke spans", "validation errors"]
      },
      {
        "name": "Pydantic Logfire",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["OTel-native instrumentation", "Auto span creation", "Token counting"]
      },
      {
        "name": "Backend Options",
        "role": "storage_layer",
        "is_highlighted": false,
        "labels": ["Grafana", "Datadog", "Honeycomb", "Jaeger"]
      },
      {
        "name": "GenAI Conventions",
        "role": "callout_box",
        "is_highlighted": false,
        "labels": ["model.name", "token.count", "tool.invocation"]
      }
    ],
    "relationships": [
      {
        "from": "PydanticAI Agent",
        "to": "Pydantic Logfire",
        "type": "arrow",
        "label": "OTel spans"
      },
      {
        "from": "Pydantic Logfire",
        "to": "Backend Options",
        "type": "arrow",
        "label": "OTLP export"
      }
    ],
    "callout_boxes": [
      {
        "heading": "GenAI SEMANTIC CONVENTIONS",
        "body_text": "model.name, token.count, tool.invocation, latency",
        "position": "right-margin"
      },
      {
        "heading": "PRD REFERENCE",
        "body_text": "agent_observability_otel. Parents: ai_framework_strategy, build_vs_buy_posture",
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
- [x] Anti-hallucination rules listed
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L3)
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
