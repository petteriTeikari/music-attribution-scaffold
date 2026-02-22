# fig-voice-36: 5-Dimension Persona Layers

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-36 |
| **Title** | 5-Dimension Persona Layers |
| **Audience** | L2 (Technical Product Manager) |
| **Location** | docs/tutorials/voice-agent-implementation.md, Section 8.1 |
| **Priority** | P1 (Important) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Show 5 concentric layers with a mutability gradient (IMMUTABLE center to FREE edge). The table in prose is 1D; this is 2D with visual weight showing which dimensions matter most. Answers: "Which parts of the persona can change and which are fixed?"

## Key Message

The persona has 5 layers from immutable core to freely mutable edge: Core Identity (IMMUTABLE) to Factual Grounding (STABLE) to Communication Style (BOUNDED) to User Context (FREE) to Conversation Flow (FREE). The most important layers change the least.

## Visual Concept

Split-panel (Template D). Left panel: 5 concentric rings like tree rings. Center ring (smallest, heaviest visual weight): "CORE IDENTITY" labeled IMMUTABLE. Second ring: "FACTUAL GROUNDING" labeled STABLE. Third: "COMMUNICATION STYLE" labeled BOUNDED. Fourth: "USER CONTEXT" labeled FREE. Outermost: "CONVERSATION FLOW" labeled FREE. Visual weight decreases outward. Right panel: detail table showing each dimension's source constant (CORE_IDENTITY, FACTUAL_GROUNDING, VOICE_STYLE) and what it controls. Coral accent line divides panels.

```
+-------------------------------------------------------------------+
|  5-DIMENSION PERSONA LAYERS                              [coral sq] |
|  MUTABILITY GRADIENT                                                |
+-------------------------------+-----------------------------------+
|  LEFT PANEL: CONCENTRIC RINGS |  RIGHT PANEL: DIMENSION DETAIL    |
|                               |                                   |
|       +-------------------+   |  LAYER       MUTABILITY  SOURCE   |
|       | +--------------+  |   |  -------------------------------- |
|       | | +----------+ |  |   |  Core        IMMUTABLE   CORE_    |
|       | | | +------+ | |  |   |  Identity               IDENTITY |
|       | | | | CORE | | |  |   |                                   |
|       | | | |IDENT.| | |  |   |  Factual    STABLE      FACTUAL_ |
|       | | | +------+ | |  |   |  Grounding             GROUNDING |
|       | | | FACTUAL  | |  |   |                                   |
|       | | +----------+ |  |   |  Communic.  BOUNDED     VOICE_   |
|       | |  COMM STYLE  |  |   |  Style                  STYLE    |
|       | +--------------+  |   |                                   |
|       |   USER CONTEXT    |   |  User       FREE        Letta/   |
|       +-------------------+   |  Context                Mem0     |
|         CONVERSATION FLOW     |                                   |
|                               |  Convers.   FREE        dynamic  |
|  heaviest <<<>>> lightest     |  Flow                   per turn |
|                               |                                   |
+-------------------------------+-----------------------------------+
|  ELI5: Like tree rings -- the heartwood never changes,      [sq]    |
|  the outer bark adapts to every season.                             |
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
    content: "5-DIMENSION PERSONA LAYERS"
    role: title

  - id: left_panel
    bounds: [40, 140, 900, 760]
    content: "Concentric Rings"
    role: content_area

  - id: right_panel
    bounds: [980, 140, 900, 760]
    content: "Dimension Detail Table"
    role: content_area

  - id: divider
    bounds: [940, 140, 2, 760]
    role: accent_line

  - id: eli5_callout
    bounds: [40, 920, 1840, 120]
    role: callout_box

anchors:
  - id: ring_core
    position: [380, 460]
    size: [140, 140]
    role: security_layer
    label: "CORE IDENTITY"

  - id: ring_factual
    position: [310, 390]
    size: [280, 280]
    role: security_layer
    label: "FACTUAL GROUNDING"

  - id: ring_communication
    position: [240, 320]
    size: [420, 420]
    role: processing_stage
    label: "COMMUNICATION STYLE"

  - id: ring_user_context
    position: [170, 250]
    size: [560, 560]
    role: data_flow
    label: "USER CONTEXT"

  - id: ring_conversation
    position: [100, 180]
    size: [700, 700]
    role: data_flow
    label: "CONVERSATION FLOW"

  - id: mutability_immutable
    position: [540, 440]
    size: [120, 30]
    role: security_layer
    label: "IMMUTABLE"

  - id: mutability_stable
    position: [610, 380]
    size: [100, 30]
    role: security_layer
    label: "STABLE"

  - id: mutability_bounded
    position: [680, 320]
    size: [100, 30]
    role: processing_stage
    label: "BOUNDED"

  - id: mutability_free_user
    position: [750, 260]
    size: [80, 30]
    role: data_flow
    label: "FREE"

  - id: mutability_free_conv
    position: [820, 200]
    size: [80, 30]
    role: data_flow
    label: "FREE"

  - id: detail_core
    position: [1020, 200]
    size: [860, 80]
    role: security_layer
    label: "Core Identity"

  - id: detail_factual
    position: [1020, 300]
    size: [860, 80]
    role: security_layer
    label: "Factual Grounding"

  - id: detail_communication
    position: [1020, 400]
    size: [860, 80]
    role: processing_stage
    label: "Communication Style"

  - id: detail_user_context
    position: [1020, 500]
    size: [860, 80]
    role: data_flow
    label: "User Context"

  - id: detail_conversation
    position: [1020, 600]
    size: [860, 80]
    role: data_flow
    label: "Conversation Flow"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Core Identity ring | `security_layer` | Innermost -- "You are the Music Attribution Assistant..." IMMUTABLE |
| Factual Grounding ring | `security_layer` | A0-A3 levels, Oracle Problem, conformal prediction. STABLE |
| Communication Style ring | `processing_stage` | Concise, voice-optimized, natural confidence language. BOUNDED |
| User Context ring | `data_flow` | User expertise level, preferences from Letta/Mem0. FREE |
| Conversation Flow ring | `data_flow` | Turn-taking, topic management, dynamic per session. FREE |
| Detail table | `data_flow` | Right panel: source constants and controls per dimension |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Core Identity | Factual Grounding | concentric | "IMMUTABLE to STABLE" |
| Factual Grounding | Communication Style | concentric | "STABLE to BOUNDED" |
| Communication Style | User Context | concentric | "BOUNDED to FREE" |
| User Context | Conversation Flow | concentric | "FREE to FREE" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Think of the persona like the rings of a tree: the heartwood at the center (core identity) never changes, the outer bark (conversation flow) adapts to every season. You can trim the branches but you cannot change the trunk. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "CORE IDENTITY"
- Label 2: "FACTUAL GROUNDING"
- Label 3: "COMMUNICATION STYLE"
- Label 4: "USER CONTEXT"
- Label 5: "CONVERSATION FLOW"
- Label 6: "IMMUTABLE"
- Label 7: "STABLE"
- Label 8: "BOUNDED"
- Label 9: "FREE"
- Label 10: "CORE_IDENTITY"
- Label 11: "FACTUAL_GROUNDING"
- Label 12: "VOICE_STYLE"
- Label 13: "Letta / Mem0"
- Label 14: "dynamic per turn"
- Label 15: "MUTABILITY GRADIENT"

### Caption (for embedding in documentation)

Concentric ring diagram showing 5 persona dimensions from immutable core identity to freely mutable conversation flow, with a detail table mapping each dimension to its source constant and mutability level.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `security_layer`, `processing_stage`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "Letta", "Mem0" should NOT appear prominently; this is L2 audience. Use in detail panel only.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text in the figure.

### Figure-Specific Rules

9. The concentric layout must show IMMUTABLE at center and FREE at edge -- never reversed.
10. Mutability labels (IMMUTABLE, STABLE, BOUNDED, FREE) must be visually paired with their dimension.
11. Do NOT use traffic light colors -- use opacity/weight gradient instead.
12. The source constants (CORE_IDENTITY, FACTUAL_GROUNDING, VOICE_STYLE) belong in the right panel detail, not the concentric rings.

## Alt Text

Concentric rings showing 5 persona dimensions from immutable core identity to freely mutable conversation flow with mutability gradient.

## Image Embed

![Concentric rings showing 5 persona dimensions from immutable core identity to freely mutable conversation flow with mutability gradient.](docs/figures/repo-figures/assets/fig-voice-36-persona-dimension-layers.jpg)

*Concentric ring diagram showing 5 persona dimensions from immutable core identity to freely mutable conversation flow, with a detail table mapping each dimension to its source constant and mutability level.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-36",
    "title": "5-Dimension Persona Layers",
    "audience": "L2",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "The persona has 5 layers from immutable core to freely mutable edge, with the most important layers changing the least.",
    "layout_flow": "center-outward",
    "key_structures": [
      {
        "name": "Core Identity",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["CORE IDENTITY", "IMMUTABLE"]
      },
      {
        "name": "Factual Grounding",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["FACTUAL GROUNDING", "STABLE"]
      },
      {
        "name": "Communication Style",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["COMMUNICATION STYLE", "BOUNDED"]
      },
      {
        "name": "User Context",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["USER CONTEXT", "FREE"]
      },
      {
        "name": "Conversation Flow",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["CONVERSATION FLOW", "FREE"]
      }
    ],
    "relationships": [
      {"from": "Core Identity", "to": "Factual Grounding", "type": "concentric", "label": "IMMUTABLE to STABLE"},
      {"from": "Factual Grounding", "to": "Communication Style", "type": "concentric", "label": "STABLE to BOUNDED"},
      {"from": "Communication Style", "to": "User Context", "type": "concentric", "label": "BOUNDED to FREE"},
      {"from": "User Context", "to": "Conversation Flow", "type": "concentric", "label": "FREE to FREE"}
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Think of the persona like the rings of a tree: the heartwood at the center (core identity) never changes, the outer bark (conversation flow) adapts to every season. You can trim the branches but you cannot change the trunk.",
        "position": "bottom-center"
      }
    ]
  }
}
```

## Quality Checklist

- [ ] Primary message clear in one sentence
- [ ] Semantic tags used (no colors, hex codes, or font names in content spec)
- [ ] ASCII layout sketched
- [ ] Spatial anchors defined in YAML
- [ ] Labels under 30 characters
- [ ] Anti-hallucination rules listed
- [ ] Alt text provided (125 chars max)
- [ ] JSON export block included
- [ ] Audience level correct (L2)
- [ ] Layout template identified (D)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
