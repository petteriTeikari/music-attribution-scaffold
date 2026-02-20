# fig-persona-04: The Intelligence Sandwich

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-04 |
| **Title** | The Intelligence Sandwich |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/knowledge-base/persona-engineering/, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Shows the three-layer architecture pattern where proprietary value lives in the orchestration and persona layers that sandwich a commodity LLM core. Answers: "If the LLM itself is becoming commoditized, where does the defensible value live in a persona-driven product?"

## Key Message

The LLM is a commodity -- proprietary value lives in the pre-processing orchestration layer (context assembly, persona injection) and post-processing validation layer (safety, persona consistency, confidence calibration).

## Visual Concept

Steps layout (Template E) with three horizontal layers stacked vertically to form a "sandwich". The top bread slice is the Pre-processing layer (orchestration, context assembly, persona injection). The middle filling is the Core LLM layer (commodity, swappable, shown with dashed borders to indicate interchangeability). The bottom bread slice is the Post-processing layer (safety validation, persona consistency check, confidence calibration). Arrows show data flowing down through all three layers. The proprietary layers (top and bottom) are visually emphasized; the commodity LLM layer uses a deferred/dashed treatment.

```
+-----------------------------------------------------------------------+
|  THE INTELLIGENCE                                               [sq]   |
|  SANDWICH                                                              |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────────┐   |
|  │  PRE-PROCESSING LAYER                           PROPRIETARY     │   |
|  │  ═══════════════════                                            │   |
|  │                                                                 │   |
|  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐    │   |
|  │  │ Orchestration│  │ Context     │  │ Persona Injection   │    │   |
|  │  │              │  │ Assembly    │  │                     │    │   |
|  │  │ Tool routing │  │ Memory      │  │ System prompt       │    │   |
|  │  │ API calls    │  │ retrieval   │  │ Persona vectors     │    │   |
|  │  │ Scheduling   │  │ RAG fusion  │  │ Trait composition   │    │   |
|  │  └─────────────┘  └─────────────┘  └─────────────────────┘    │   |
|  └─────────────────────────────────────────────────────────────────┘   |
|                              │                                         |
|                              ▼                                         |
|  ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐   |
|  │  CORE LLM                                      COMMODITY        │   |
|  │  ════════                                                       │   |
|  │                                                                 │   |
|  │  Claude / GPT / Gemini / Llama / Mistral                       │   |
|  │  (swappable -- any foundation model)                            │   |
|  │                                                                 │   |
|  └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘   |
|                              │                                         |
|                              ▼                                         |
|  ┌─────────────────────────────────────────────────────────────────┐   |
|  │  POST-PROCESSING LAYER                          PROPRIETARY     │   |
|  │  ══════════════════════                                         │   |
|  │                                                                 │   |
|  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐    │   |
|  │  │ Safety       │  │ Persona     │  │ Confidence          │    │   |
|  │  │ Validation   │  │ Consistency │  │ Calibration         │    │   |
|  │  │              │  │ Check       │  │                     │    │   |
|  │  │ Guardrails   │  │ Drift       │  │ Uncertainty         │    │   |
|  │  │ Content      │  │ detection   │  │ quantification      │    │   |
|  │  │ filtering    │  │ Repair      │  │ Source weighting     │    │   |
|  │  └─────────────┘  └─────────────┘  └─────────────────────┘    │   |
|  └─────────────────────────────────────────────────────────────────┘   |
|                                                                        |
|  THE LLM IS A COMMODITY -- PROPRIETARY VALUE LIVES IN             [sq] |
|  ORCHESTRATION AND PERSONA                                             |
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
    content: "THE INTELLIGENCE SANDWICH"
    role: title

  - id: pre_processing_zone
    bounds: [80, 140, 1760, 260]
    role: content_area
    label: "Pre-processing Layer"

  - id: core_llm_zone
    bounds: [80, 440, 1760, 160]
    role: content_area
    label: "Core LLM"

  - id: post_processing_zone
    bounds: [80, 640, 1760, 260]
    role: content_area
    label: "Post-processing Layer"

  - id: callout_zone
    bounds: [80, 940, 1760, 100]
    content: "THE LLM IS A COMMODITY -- PROPRIETARY VALUE LIVES IN ORCHESTRATION AND PERSONA"
    role: callout_box

anchors:
  - id: orchestration
    position: [120, 180]
    size: [520, 180]
    role: processing_stage
    label: "Orchestration"

  - id: context_assembly
    position: [700, 180]
    size: [520, 180]
    role: processing_stage
    label: "Context Assembly"

  - id: persona_injection
    position: [1280, 180]
    size: [520, 180]
    role: processing_stage
    label: "Persona Injection"

  - id: core_llm
    position: [120, 460]
    size: [1680, 120]
    role: deferred_option
    label: "Core LLM (Commodity)"

  - id: safety_validation
    position: [120, 680]
    size: [520, 180]
    role: processing_stage
    label: "Safety Validation"

  - id: persona_consistency
    position: [700, 680]
    size: [520, 180]
    role: processing_stage
    label: "Persona Consistency Check"

  - id: confidence_calibration
    position: [1280, 680]
    size: [520, 180]
    role: final_score
    label: "Confidence Calibration"

  - id: flow_pre_to_llm
    from: pre_processing_zone
    to: core_llm
    type: arrow
    label: "assembled prompt"

  - id: flow_llm_to_post
    from: core_llm
    to: post_processing_zone
    type: arrow
    label: "raw generation"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "THE INTELLIGENCE SANDWICH" in editorial caps |
| Pre-processing Layer | `processing_stage` | Top bread: orchestration, context assembly, persona injection -- PROPRIETARY |
| Orchestration | `processing_stage` | Tool routing, API calls, scheduling |
| Context Assembly | `processing_stage` | Memory retrieval, RAG fusion, knowledge grounding |
| Persona Injection | `processing_stage` | System prompt construction, persona vector composition, trait selection |
| Core LLM | `deferred_option` | Middle filling: commodity foundation model, swappable (Claude/GPT/Gemini/Llama/Mistral) |
| Post-processing Layer | `processing_stage` | Bottom bread: safety validation, persona consistency, confidence calibration -- PROPRIETARY |
| Safety Validation | `processing_stage` | Guardrails, content filtering, harm prevention |
| Persona Consistency Check | `processing_stage` | Drift detection, persona repair, behavioral alignment verification |
| Confidence Calibration | `final_score` | Uncertainty quantification, source weighting, conformal prediction |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| Pre-processing Layer | Core LLM | arrow | "assembled prompt" |
| Core LLM | Post-processing Layer | arrow | "raw generation" |
| Post-processing Layer | Pre-processing Layer | dashed | "feedback for next turn" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "THE LLM IS A COMMODITY -- PROPRIETARY VALUE LIVES IN ORCHESTRATION AND PERSONA" | As foundation models commoditize, competitive advantage shifts to the layers that wrap them: pre-processing (how you assemble context and inject persona) and post-processing (how you validate safety, consistency, and calibrate confidence). The LLM itself is swappable. | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "PRE-PROCESSING LAYER"
- Label 2: "CORE LLM"
- Label 3: "POST-PROCESSING LAYER"
- Label 4: "PROPRIETARY"
- Label 5: "COMMODITY"
- Label 6: "Orchestration"
- Label 7: "Context Assembly"
- Label 8: "Persona Injection"
- Label 9: "Safety Validation"
- Label 10: "Persona Consistency Check"
- Label 11: "Confidence Calibration"
- Label 12: "Swappable"
- Label 13: "Tool routing, API calls"
- Label 14: "Memory retrieval, RAG"
- Label 15: "Drift detection, repair"

### Caption

The Intelligence Sandwich architecture showing proprietary value in the pre-processing layer (orchestration, context assembly, persona injection) and post-processing layer (safety validation, persona consistency, confidence calibration) sandwiching a commodity LLM core that is swappable across foundation models.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Engineering jargon** -- "RAG", "guardrails", "conformal prediction" should NOT appear for L2 unless briefly defined. Use accessible equivalents.
5. **Background MUST be warm cream (#f6f3e6)**.
6. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

9. The Core LLM must be visually differentiated from the proprietary layers -- use dashed borders or reduced emphasis to show it is interchangeable.
10. "Commodity" does NOT mean low quality -- it means the core model is not the differentiator. Do NOT depict the LLM negatively.
11. The three layers are sequential in a single request, NOT separate microservices -- do NOT show network boundaries between them.
12. "Persona Injection" in pre-processing is distinct from "Persona Consistency Check" in post-processing -- injection sets the persona, consistency validates it was maintained.
13. List real model families (Claude, GPT, Gemini, Llama, Mistral) to make the swappability concrete -- do NOT use only generic placeholder names.
14. Do NOT imply that pre/post processing layers are optional -- they are the core product value.

## Alt Text

Architecture diagram of the Intelligence Sandwich pattern showing proprietary pre-processing (orchestration, context assembly, persona injection) and post-processing (safety validation, persona consistency, confidence calibration) layers sandwiching a commodity swappable LLM core for music attribution systems.

## Image Embed

![Architecture diagram of the Intelligence Sandwich pattern showing proprietary pre-processing (orchestration, context assembly, persona injection) and post-processing (safety validation, persona consistency, confidence calibration) layers sandwiching a commodity swappable LLM core for music attribution systems.](docs/figures/repo-figures/assets/fig-persona-04-intelligence-sandwich.jpg)

*The Intelligence Sandwich architecture showing proprietary value in the pre-processing layer (orchestration, context assembly, persona injection) and post-processing layer (safety validation, persona consistency, confidence calibration) sandwiching a commodity LLM core that is swappable across foundation models.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-04",
    "title": "The Intelligence Sandwich",
    "audience": "L2",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "The LLM is a commodity -- proprietary value lives in the pre-processing orchestration and post-processing validation layers.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Pre-processing Layer",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["PRE-PROCESSING LAYER", "PROPRIETARY", "Orchestration", "Context Assembly", "Persona Injection"]
      },
      {
        "name": "Core LLM",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["CORE LLM", "COMMODITY", "Swappable"]
      },
      {
        "name": "Post-processing Layer",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["POST-PROCESSING LAYER", "PROPRIETARY", "Safety Validation", "Persona Consistency", "Confidence Calibration"]
      }
    ],
    "relationships": [
      {
        "from": "Pre-processing",
        "to": "Core LLM",
        "type": "arrow",
        "label": "assembled prompt"
      },
      {
        "from": "Core LLM",
        "to": "Post-processing",
        "type": "arrow",
        "label": "raw generation"
      },
      {
        "from": "Post-processing",
        "to": "Pre-processing",
        "type": "dashed",
        "label": "feedback for next turn"
      }
    ],
    "callout_boxes": [
      {
        "heading": "THE LLM IS A COMMODITY -- PROPRIETARY VALUE LIVES IN ORCHESTRATION AND PERSONA",
        "body_text": "Competitive advantage shifts to the wrapping layers as foundation models commoditize. The LLM itself is swappable.",
        "position": "bottom-full-width"
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
- [x] Audience level correct (L2)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
