# fig-persona-01: Multi-Dimensional Persona Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-01 |
| **Title** | Multi-Dimensional Persona Architecture |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/knowledge-base/persona-engineering/, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Shows that persona engineering is not a single monolithic system prompt but a multi-dimensional architecture where each dimension has different stability properties. Answers: "Which parts of a persona should be fixed, and which should adapt per conversation?"

## Key Message

Not all persona dimensions should have the same stability -- Core Identity is immutable while Conversation Flow is fully adaptive, and mixing these up causes either rigidity or drift.

## Visual Concept

Multi-panel layout (Template B) with five horizontal panels stacked vertically, each representing one persona dimension. The panels are grouped into two visual layers separated by an accent line: Stable Layer (top two) and Adaptive Layer (bottom three). Each panel shows the dimension name, stability property tag, and representative examples. A gradient or visual cue runs from locked/immutable at top to free/adaptive at bottom. A large callout bar spans the bottom.

```
+-----------------------------------------------------------------------+
|  MULTI-DIMENSIONAL                                              [sq]   |
|  PERSONA ARCHITECTURE                                                  |
+-----------------------------------------------------------------------+
|                                                                        |
|  STABLE LAYER                                                          |
|  ═══════════                                                           |
|  ┌─────────────────────────────────────────────────────────────────┐   |
|  │  I. CORE IDENTITY            IMMUTABLE                          │   |
|  │     Values, ethical boundaries, fundamental character            │   |
|  ├─────────────────────────────────────────────────────────────────┤   |
|  │  II. FACTUAL GROUNDING       STABLE                             │   |
|  │      Domain knowledge, claimed expertise, biographical facts     │   |
|  └─────────────────────────────────────────────────────────────────┘   |
|                                                                        |
|  ─────────────── STABILITY BOUNDARY ───────────────                    |
|                                                                        |
|  ADAPTIVE LAYER                                                        |
|  ═════════════                                                         |
|  ┌─────────────────────────────────────────────────────────────────┐   |
|  │  III. COMMUNICATION STYLE    BOUNDED                            │   |
|  │       Tone, vocabulary, formality -- adapts within constraints   │   |
|  ├─────────────────────────────────────────────────────────────────┤   |
|  │  IV. USER CONTEXT            FREE                               │   |
|  │      User preferences, session history, personalization          │   |
|  ├─────────────────────────────────────────────────────────────────┤   |
|  │  V. CONVERSATION FLOW        FREE                               │   |
|  │     Turn-taking, topic transitions, pacing                       │   |
|  └─────────────────────────────────────────────────────────────────┘   |
|                                                                        |
|  NOT ALL PERSONA DIMENSIONS SHOULD HAVE THE SAME STABILITY      [sq]  |
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
    content: "MULTI-DIMENSIONAL PERSONA ARCHITECTURE"
    role: title

  - id: stable_label
    bounds: [80, 140, 400, 40]
    content: "STABLE LAYER"
    role: label_editorial

  - id: stable_zone
    bounds: [80, 180, 1760, 240]
    role: content_area

  - id: stability_boundary
    bounds: [80, 440, 1760, 2]
    role: accent_line

  - id: adaptive_label
    bounds: [80, 460, 400, 40]
    content: "ADAPTIVE LAYER"
    role: label_editorial

  - id: adaptive_zone
    bounds: [80, 500, 1760, 380]
    role: content_area

  - id: callout_zone
    bounds: [80, 920, 1760, 100]
    content: "NOT ALL PERSONA DIMENSIONS SHOULD HAVE THE SAME STABILITY"
    role: callout_box

anchors:
  - id: dim_core_identity
    position: [100, 190]
    size: [1720, 100]
    role: security_layer
    label: "I. CORE IDENTITY"

  - id: dim_factual_grounding
    position: [100, 300]
    size: [1720, 100]
    role: processing_stage
    label: "II. FACTUAL GROUNDING"

  - id: dim_communication_style
    position: [100, 510]
    size: [1720, 100]
    role: processing_stage
    label: "III. COMMUNICATION STYLE"

  - id: dim_user_context
    position: [100, 620]
    size: [1720, 100]
    role: branching_path
    label: "IV. USER CONTEXT"

  - id: dim_conversation_flow
    position: [100, 730]
    size: [1720, 100]
    role: branching_path
    label: "V. CONVERSATION FLOW"

  - id: stability_tag_immutable
    position: [1400, 210]
    size: [300, 40]
    role: security_layer
    label: "IMMUTABLE"

  - id: stability_tag_stable
    position: [1400, 320]
    size: [300, 40]
    role: confidence_high
    label: "STABLE"

  - id: stability_tag_bounded
    position: [1400, 530]
    size: [300, 40]
    role: confidence_medium
    label: "BOUNDED"

  - id: stability_tag_free_1
    position: [1400, 640]
    size: [300, 40]
    role: confidence_low
    label: "FREE"

  - id: stability_tag_free_2
    position: [1400, 750]
    size: [300, 40]
    role: confidence_low
    label: "FREE"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "MULTI-DIMENSIONAL PERSONA ARCHITECTURE" in editorial caps with accent square |
| Stable Layer label | `label_editorial` | Section header for immutable/stable dimensions |
| Adaptive Layer label | `label_editorial` | Section header for bounded/free dimensions |
| Core Identity panel | `security_layer` | Dimension I: values, ethical boundaries, fundamental character -- IMMUTABLE |
| Factual Grounding panel | `processing_stage` | Dimension II: domain knowledge, claimed expertise, biographical facts -- STABLE |
| Communication Style panel | `processing_stage` | Dimension III: tone, vocabulary, formality -- BOUNDED adaptation within constraints |
| User Context panel | `branching_path` | Dimension IV: user preferences, session history, personalization -- FREE |
| Conversation Flow panel | `branching_path` | Dimension V: turn-taking, topic transitions, pacing -- FREE |
| Stability boundary | `accent_line` | Visual separator between stable and adaptive layers |
| Stability tags | `confidence_high` / `confidence_medium` / `confidence_low` | IMMUTABLE, STABLE, BOUNDED, FREE labels using confidence-tier semantics |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| Core Identity | Factual Grounding | progression | "anchors" |
| Factual Grounding | Communication Style | dashed | "constrains" |
| Communication Style | User Context | dashed | "adapts within bounds" |
| User Context | Conversation Flow | arrow | "informs" |
| Stable Layer | Adaptive Layer | arrow | "stability boundary" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "NOT ALL PERSONA DIMENSIONS SHOULD HAVE THE SAME STABILITY" | Treating all dimensions as equally mutable causes drift. Treating all as equally fixed causes rigidity. The key architectural insight is matching stability properties to dimension type. | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "STABLE LAYER"
- Label 2: "ADAPTIVE LAYER"
- Label 3: "I. CORE IDENTITY"
- Label 4: "II. FACTUAL GROUNDING"
- Label 5: "III. COMMUNICATION STYLE"
- Label 6: "IV. USER CONTEXT"
- Label 7: "V. CONVERSATION FLOW"
- Label 8: "IMMUTABLE"
- Label 9: "STABLE"
- Label 10: "BOUNDED"
- Label 11: "FREE"
- Label 12: "STABILITY BOUNDARY"
- Label 13: "Values, ethics"
- Label 14: "Domain knowledge"
- Label 15: "Tone, vocabulary"
- Label 16: "User preferences"
- Label 17: "Turn-taking, pacing"

### Caption

Multi-dimensional persona architecture showing five dimensions with graduated stability properties: Core Identity (immutable) and Factual Grounding (stable) form a stable layer, while Communication Style (bounded), User Context (free), and Conversation Flow (free) form an adaptive layer.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Engineering jargon** -- module names and library references are appropriate for L3 audience.
5. **Background MUST be warm cream (#f6f3e6)**.
6. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

9. The five dimensions are a conceptual framework, not a specific library or API -- do NOT attribute them to a particular paper unless specified.
10. IMMUTABLE means the dimension NEVER changes across conversations -- do NOT show it with any adaptation indicators.
11. BOUNDED means the dimension adapts within defined constraints -- do NOT show it as fully free or fully locked.
12. The stability boundary is a hard architectural line, not a gradient -- both sides have fundamentally different update policies.
13. Do NOT show specific persona content (e.g., "I am a helpful assistant") -- show the structural categories only.
14. The five dimensions are ordered by decreasing stability, NOT by importance -- all five are essential.

## Alt Text

Architecture diagram showing five persona dimensions arranged by graduated stability from immutable Core Identity to free Conversation Flow, divided into stable and adaptive layers by a stability boundary for persona coherence engineering.

## Image Embed

![Architecture diagram showing five persona dimensions arranged by graduated stability from immutable Core Identity to free Conversation Flow, divided into stable and adaptive layers by a stability boundary for persona coherence engineering.](docs/figures/repo-figures/assets/fig-persona-01-multi-dimensional-persona-architecture.jpg)

*Multi-dimensional persona architecture showing five dimensions with graduated stability properties: Core Identity (immutable) and Factual Grounding (stable) form a stable layer, while Communication Style (bounded), User Context (free), and Conversation Flow (free) form an adaptive layer.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-01",
    "title": "Multi-Dimensional Persona Architecture",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Not all persona dimensions should have the same stability -- Core Identity is immutable while Conversation Flow is fully adaptive.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Core Identity",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["I. CORE IDENTITY", "IMMUTABLE", "Values, ethics"]
      },
      {
        "name": "Factual Grounding",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["II. FACTUAL GROUNDING", "STABLE", "Domain knowledge"]
      },
      {
        "name": "Communication Style",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["III. COMMUNICATION STYLE", "BOUNDED", "Tone, vocabulary"]
      },
      {
        "name": "User Context",
        "role": "branching_path",
        "is_highlighted": false,
        "labels": ["IV. USER CONTEXT", "FREE", "User preferences"]
      },
      {
        "name": "Conversation Flow",
        "role": "branching_path",
        "is_highlighted": false,
        "labels": ["V. CONVERSATION FLOW", "FREE", "Turn-taking, pacing"]
      },
      {
        "name": "Stability Boundary",
        "role": "accent_line",
        "is_highlighted": true,
        "labels": ["STABILITY BOUNDARY"]
      }
    ],
    "relationships": [
      {
        "from": "Core Identity",
        "to": "Factual Grounding",
        "type": "arrow",
        "label": "anchors"
      },
      {
        "from": "Factual Grounding",
        "to": "Communication Style",
        "type": "dashed",
        "label": "constrains"
      },
      {
        "from": "Communication Style",
        "to": "User Context",
        "type": "dashed",
        "label": "adapts within bounds"
      },
      {
        "from": "User Context",
        "to": "Conversation Flow",
        "type": "arrow",
        "label": "informs"
      }
    ],
    "callout_boxes": [
      {
        "heading": "NOT ALL PERSONA DIMENSIONS SHOULD HAVE THE SAME STABILITY",
        "body_text": "Treating all dimensions as equally mutable causes drift. Treating all as equally fixed causes rigidity. Match stability properties to dimension type.",
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
- [x] Audience level correct (L3)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
