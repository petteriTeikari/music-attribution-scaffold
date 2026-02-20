# fig-persona-03: Persona Vectors in Activation Space

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-03 |
| **Title** | Persona Vectors in Activation Space |
| **Audience** | L4 (AI/ML Architect) |
| **Location** | docs/knowledge-base/persona-engineering/, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | A (Hero) |

## Purpose

Visualizes the key finding from mechanistic interpretability research that persona traits correspond to identifiable directions in a language model's activation space, and that steering along these vectors changes behavior predictably. Answers: "How do persona traits manifest inside the model, and can we control them?"

## Key Message

Persona traits have identifiable directions in activation space -- steering along these vectors changes model behavior, with the "Assistant Axis" principal component explaining the largest variance in persona-steered outputs.

## Visual Concept

Hero layout (Template A) with a large central visualization of a 2D projection of activation space. The space shows scattered points representing different model states, with labeled directional vectors radiating from a central origin. Key vectors include "evil", "sycophancy", "hallucination", "helpful", and the dominant "Assistant Axis" principal component shown as a thicker arrow. Color semantics differentiate safe directions (confidence_high) from unsafe directions (confidence_low). A region annotation shows how moving along a vector shifts model behavior. The right side has a smaller inset showing the steering mechanism: adding a scaled vector to residual stream activations.

```
+-----------------------------------------------------------------------+
|  PERSONA VECTORS                                                [sq]   |
|  IN ACTIVATION SPACE                                                   |
+-----------------------------------------------------------------------+
|                                                                        |
|                    ACTIVATION SPACE (2D PROJECTION)                     |
|                                                                        |
|                              evil ↗                                     |
|                             /                                          |
|                   sycophancy ↗                                          |
|                           /                                            |
|              hallucination ↗                                            |
|                         /                                              |
|           ○ ○  ○       /                                               |
|         ○    ○  ○   ──●── ORIGIN                                      |
|        ○  ○   ○    /     \                                             |
|       ○     ○     /       \                                            |
|        ○  ○      ↙         ↘                                          |
|               helpful     ASSISTANT AXIS                               |
|                          ═══════════════>                               |
|                          (principal component,                          |
|                           largest variance)                             |
|                                                                        |
|  STEERING MECHANISM          ┌────────────────────┐                   |
|  ═══════════════════         │  h' = h + α·v      │                   |
|  Add scaled persona          │                    │                   |
|  vector to residual          │  h = activation    │                   |
|  stream at layer L           │  v = persona vector │                   |
|                              │  α = steering coeff │                   |
|                              └────────────────────┘                   |
|                                                                        |
|  PERSONA TRAITS HAVE IDENTIFIABLE DIRECTIONS IN ACTIVATION SPACE [sq]  |
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
    content: "PERSONA VECTORS IN ACTIVATION SPACE"
    role: title

  - id: hero_zone
    bounds: [80, 140, 1200, 660]
    role: content_area
    label: "Activation Space Visualization"

  - id: mechanism_zone
    bounds: [1340, 500, 520, 300]
    role: content_area
    label: "Steering Mechanism"

  - id: callout_zone
    bounds: [80, 960, 1760, 100]
    content: "PERSONA TRAITS HAVE IDENTIFIABLE DIRECTIONS IN ACTIVATION SPACE"
    role: callout_box

anchors:
  - id: origin_point
    position: [640, 460]
    size: [20, 20]
    role: decision_point
    label: "Origin"

  - id: evil_vector
    position: [800, 280]
    size: [200, 20]
    role: confidence_low
    label: "evil"

  - id: sycophancy_vector
    position: [780, 340]
    size: [200, 20]
    role: confidence_low
    label: "sycophancy"

  - id: hallucination_vector
    position: [760, 400]
    size: [200, 20]
    role: confidence_low
    label: "hallucination"

  - id: helpful_vector
    position: [500, 600]
    size: [200, 20]
    role: confidence_high
    label: "helpful"

  - id: assistant_axis
    position: [680, 580]
    size: [500, 30]
    role: confidence_high
    label: "ASSISTANT AXIS"

  - id: scattered_points
    position: [300, 350]
    size: [400, 300]
    role: data_flow
    label: "Model activation states"

  - id: steering_formula
    position: [1360, 520]
    size: [480, 260]
    role: processing_stage
    label: "h' = h + alpha * v"

  - id: flow_vector_to_behavior
    from: origin_point
    to: assistant_axis
    type: arrow
    label: "steering changes behavior"

  - id: flow_evil_direction
    from: origin_point
    to: evil_vector
    type: arrow
    label: "unsafe direction"

  - id: flow_helpful_direction
    from: origin_point
    to: helpful_vector
    type: arrow
    label: "safe direction"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "PERSONA VECTORS IN ACTIVATION SPACE" in editorial caps |
| Activation space | `content_area` | 2D projection of high-dimensional activation space with scattered model states |
| Origin point | `decision_point` | Central reference point from which persona vectors radiate |
| Evil vector | `confidence_low` | Direction in activation space associated with harmful/toxic behavior |
| Sycophancy vector | `confidence_low` | Direction associated with excessive agreement and flattery |
| Hallucination vector | `confidence_low` | Direction associated with confabulation and false claims |
| Helpful vector | `confidence_high` | Direction associated with genuinely helpful behavior |
| Assistant Axis | `confidence_high` | Principal component explaining largest variance -- the dominant persona direction |
| Scattered points | `data_flow` | Individual model activation states shown as dots in the projected space |
| Steering formula | `processing_stage` | Mathematical mechanism: h' = h + alpha * v (add scaled vector to activations) |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| Origin | Evil vector | arrow | "unsafe direction" |
| Origin | Sycophancy vector | arrow | "unsafe direction" |
| Origin | Hallucination vector | arrow | "unsafe direction" |
| Origin | Helpful vector | arrow | "safe direction" |
| Origin | Assistant Axis | arrow | "principal component" |
| Steering formula | Activation space | dashed | "modifies activations" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "PERSONA TRAITS HAVE IDENTIFIABLE DIRECTIONS IN ACTIVATION SPACE" | Mechanistic interpretability reveals that persona attributes correspond to linear directions. The Assistant Axis principal component captures the largest variance. Steering by adding scaled vectors to residual stream activations at specific layers predictably shifts model behavior. | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "ACTIVATION SPACE"
- Label 2: "evil"
- Label 3: "sycophancy"
- Label 4: "hallucination"
- Label 5: "helpful"
- Label 6: "ASSISTANT AXIS"
- Label 7: "Principal component"
- Label 8: "STEERING MECHANISM"
- Label 9: "h' = h + alpha * v"
- Label 10: "h = activation"
- Label 11: "v = persona vector"
- Label 12: "alpha = steering coeff"
- Label 13: "2D Projection"
- Label 14: "Largest variance"

### Caption

Persona vectors in activation space showing identifiable directions for traits like helpfulness, sycophancy, and hallucination. The Assistant Axis principal component captures the largest variance. Steering via h' = h + alpha * v modifies residual stream activations to shift behavior predictably.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Engineering jargon** -- activation space, residual stream, principal component are appropriate for L4 audience.
5. **Background MUST be warm cream (#f6f3e6)**.
6. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

9. The 2D projection is a conceptual illustration, NOT derived from real data -- do NOT show specific axis values or scale bars.
10. The "Assistant Axis" finding is from Anthropic's mechanistic interpretability research -- do NOT attribute to other labs.
11. The vectors shown (evil, sycophancy, hallucination, helpful) are representative examples -- the actual space has many more directions.
12. The steering formula h' = h + alpha * v is a simplified representation -- actual implementation involves layer selection and normalization.
13. Do NOT imply that activation steering is fully reliable or production-ready -- it is a research technique.
14. The scattered points represent model states, NOT individual tokens or training examples.
15. Do NOT show a clean linear separation between safe and unsafe -- the space is high-dimensional and the 2D projection is approximate.

## Alt Text

Visualization of persona trait vectors in LLM activation space with directions for helpfulness, sycophancy, hallucination, and evil radiating from an origin point, highlighting the Assistant Axis principal component and the steering mechanism formula for transparent confidence in AI behavior control.

## Image Embed

![Visualization of persona trait vectors in LLM activation space with directions for helpfulness, sycophancy, hallucination, and evil radiating from an origin point, highlighting the Assistant Axis principal component and the steering mechanism formula for transparent confidence in AI behavior control.](docs/figures/repo-figures/assets/fig-persona-03-persona-vectors-activation-space.jpg)

*Persona vectors in activation space showing identifiable directions for traits like helpfulness, sycophancy, and hallucination. The Assistant Axis principal component captures the largest variance. Steering via h' = h + alpha * v modifies residual stream activations to shift behavior predictably.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-03",
    "title": "Persona Vectors in Activation Space",
    "audience": "L4",
    "layout_template": "A"
  },
  "content_architecture": {
    "primary_message": "Persona traits have identifiable directions in activation space, and steering along these vectors changes model behavior.",
    "layout_flow": "centered",
    "key_structures": [
      {
        "name": "Activation Space",
        "role": "content_area",
        "is_highlighted": true,
        "labels": ["ACTIVATION SPACE", "2D Projection"]
      },
      {
        "name": "Evil Vector",
        "role": "confidence_low",
        "is_highlighted": false,
        "labels": ["evil"]
      },
      {
        "name": "Sycophancy Vector",
        "role": "confidence_low",
        "is_highlighted": false,
        "labels": ["sycophancy"]
      },
      {
        "name": "Hallucination Vector",
        "role": "confidence_low",
        "is_highlighted": false,
        "labels": ["hallucination"]
      },
      {
        "name": "Helpful Vector",
        "role": "confidence_high",
        "is_highlighted": false,
        "labels": ["helpful"]
      },
      {
        "name": "Assistant Axis",
        "role": "confidence_high",
        "is_highlighted": true,
        "labels": ["ASSISTANT AXIS", "Principal component", "Largest variance"]
      },
      {
        "name": "Steering Formula",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["h' = h + alpha * v"]
      }
    ],
    "relationships": [
      {
        "from": "Origin",
        "to": "Evil Vector",
        "type": "arrow",
        "label": "unsafe direction"
      },
      {
        "from": "Origin",
        "to": "Sycophancy Vector",
        "type": "arrow",
        "label": "unsafe direction"
      },
      {
        "from": "Origin",
        "to": "Helpful Vector",
        "type": "arrow",
        "label": "safe direction"
      },
      {
        "from": "Origin",
        "to": "Assistant Axis",
        "type": "arrow",
        "label": "principal component"
      }
    ],
    "callout_boxes": [
      {
        "heading": "PERSONA TRAITS HAVE IDENTIFIABLE DIRECTIONS IN ACTIVATION SPACE",
        "body_text": "Steering by adding scaled vectors to residual stream activations predictably shifts model behavior. The Assistant Axis captures the largest variance.",
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
- [x] Audience level correct (L4)
- [x] Layout template identified (A)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
