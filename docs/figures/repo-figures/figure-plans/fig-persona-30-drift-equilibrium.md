# fig-persona-30: Drift as Controllable Equilibrium

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-30 |
| **Title** | Drift as Controllable Equilibrium -- Old View vs New View |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/architecture/persona.md, docs/planning/ |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Contrasts the old understanding of persona drift (inevitable monotonic decay) with the new understanding from "Drift No More" (arXiv:2510.07777) that drift is a bounded equilibrium controllable through periodic reinforcement, memory blocks, and activation capping. Answers: "Is persona drift inevitable, or can we engineer stability?"

## Key Message

Persona drift is not inevitable decay but a controllable equilibrium -- periodic reinforcement, memory blocks, and activation capping act as restoring forces that keep persona consistency oscillating within acceptable bounds rather than monotonically degrading.

## Visual Concept

Split-panel layout. Left panel ("Old View") shows a monotonically decreasing curve labeled "drift as inevitable decay" -- persona consistency starts high and degrades over time. Right panel ("New View") shows an oscillating curve around a stable mean, with restoring forces annotated at each recovery point. The oscillation stays within bounded limits (dashed horizontal lines). Below the split, restoring force mechanisms are listed. A reference to "Drift No More" (arXiv:2510.07777) is included.

```
+---------------------------------------------------------------+
|  DRIFT AS CONTROLLABLE EQUILIBRIUM                             |
+---------------------------------------------------------------+
|                                                                |
|  LEFT: OLD VIEW                RIGHT: NEW VIEW                 |
|                                                                |
|  ┌──────────────────────┐    ┌──────────────────────────┐     |
|  │ Persona               │    │ Persona                   │     |
|  │ Consistency            │    │ Consistency                │     |
|  │  │                     │    │  │  ---- upper bound ---- │     |
|  │  │\                    │    │  │ /\    /\    /\         │     |
|  │  │ \                   │    │  │/  \  /  \  /  \  /\   │     |
|  │  │  \                  │    │  │    \/    \/    \/  \   │     |
|  │  │   \                 │    │  │  ---- stable mean ---- │     |
|  │  │    \                │    │  │                        │     |
|  │  │     \____           │    │  │  ---- lower bound ---- │     |
|  │  │          \____      │    │  │                        │     |
|  │  └──────────────────  │    │  └──────────────────────  │     |
|  │       Time ──>         │    │       Time ──>            │     |
|  │                        │    │                           │     |
|  │  "Inevitable decay"    │    │  "Bounded equilibrium"    │     |
|  └──────────────────────┘    └──────────────────────────┘     |
|                                                                |
|  RESTORING FORCES:                                             |
|  ■ Periodic reinforcement (system prompt refresh)              |
|  ■ Memory blocks (Letta/MemGPT core memory)                   |
|  ■ Activation capping (prevent runaway attention drift)        |
|                                                                |
|  Reference: "Drift No More" (arXiv:2510.07777)                |
|                                                                |
+---------------------------------------------------------------+
|  DRIFT IS A CONTROLLABLE EQUILIBRIUM -- NOT INEVITABLE DECAY   |
+---------------------------------------------------------------+
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
    content: "DRIFT AS CONTROLLABLE EQUILIBRIUM"
    role: title

  - id: left_panel
    bounds: [80, 160, 820, 480]
    role: content_area

  - id: right_panel
    bounds: [1000, 160, 840, 480]
    role: content_area

  - id: restoring_forces_zone
    bounds: [80, 680, 1760, 160]
    role: content_area

  - id: reference_zone
    bounds: [80, 860, 1760, 40]
    role: content_area

  - id: callout_zone
    bounds: [80, 920, 1760, 120]
    role: callout_box

anchors:
  - id: old_view_label
    position: [480, 200]
    size: [600, 60]
    role: problem_statement
    label: "OLD VIEW"

  - id: old_view_curve
    position: [480, 400]
    size: [600, 300]
    role: confidence_low
    label: "Monotonically decreasing curve"

  - id: new_view_label
    position: [1420, 200]
    size: [640, 60]
    role: confidence_high
    label: "NEW VIEW"

  - id: new_view_curve
    position: [1420, 400]
    size: [640, 300]
    role: confidence_high
    label: "Oscillating curve around stable mean"

  - id: upper_bound
    position: [1420, 300]
    size: [600, 2]
    role: assurance_a2
    label: "upper bound"

  - id: stable_mean
    position: [1420, 400]
    size: [600, 2]
    role: selected_option
    label: "stable mean"

  - id: lower_bound
    position: [1420, 500]
    size: [600, 2]
    role: assurance_a1
    label: "lower bound"

  - id: force_reinforcement
    position: [480, 730]
    size: [500, 40]
    role: processing_stage
    label: "Periodic reinforcement"

  - id: force_memory
    position: [960, 730]
    size: [500, 40]
    role: processing_stage
    label: "Memory blocks"

  - id: force_capping
    position: [1440, 730]
    size: [500, 40]
    role: processing_stage
    label: "Activation capping"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "DRIFT AS CONTROLLABLE EQUILIBRIUM" with accent square |
| Old View panel | `problem_statement` | Left panel -- monotonically decreasing curve, drift as decay |
| New View panel | `confidence_high` | Right panel -- oscillating curve within bounds, drift as equilibrium |
| Decay curve | `confidence_low` | Monotonically decreasing line showing inevitable degradation |
| Equilibrium curve | `confidence_high` | Oscillating line around a stable mean within upper/lower bounds |
| Upper bound line | `assurance_a2` | Dashed horizontal line marking acceptable upper limit |
| Stable mean line | `selected_option` | Solid horizontal line marking the equilibrium target |
| Lower bound line | `assurance_a1` | Dashed horizontal line marking acceptable lower limit |
| Periodic reinforcement | `processing_stage` | Restoring force: system prompt refresh at intervals |
| Memory blocks | `processing_stage` | Restoring force: Letta/MemGPT core memory persistence |
| Activation capping | `processing_stage` | Restoring force: prevent runaway attention drift |
| Reference annotation | `data_mono` | "Drift No More" (arXiv:2510.07777) citation |
| Callout bar | `callout_bar` | Drift is a controllable equilibrium, not inevitable decay |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Old View | New View | arrow | "paradigm shift" |
| Periodic reinforcement | Equilibrium curve | dashed | "restoring force" |
| Memory blocks | Equilibrium curve | dashed | "restoring force" |
| Activation capping | Equilibrium curve | dashed | "restoring force" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "PARADIGM SHIFT" | Drift is not inevitable decay but a controllable equilibrium with restoring forces that maintain bounded oscillation | bottom-center |
| "RESTORING FORCES" | Periodic reinforcement, memory blocks, and activation capping keep persona consistency within acceptable bounds | bottom-left |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "OLD VIEW"
- Label 2: "NEW VIEW"
- Label 3: "Persona Consistency"
- Label 4: "Time"
- Label 5: "Inevitable decay"
- Label 6: "Bounded equilibrium"
- Label 7: "upper bound"
- Label 8: "stable mean"
- Label 9: "lower bound"
- Label 10: "Periodic reinforcement"
- Label 11: "Memory blocks"
- Label 12: "Activation capping"
- Label 13: "arXiv:2510.07777"

### Caption (for embedding in documentation)

Split-panel comparison: Old View shows persona drift as monotonic decay; New View (per "Drift No More," arXiv:2510.07777) shows drift as bounded equilibrium maintained by restoring forces -- periodic reinforcement, memory blocks, and activation capping.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `problem_statement`, `confidence_high`, `processing_stage` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- This is L3 so Letta/MemGPT, activation capping, system prompt ARE allowed.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The OLD VIEW curve MUST be monotonically decreasing -- no recovery points.
10. The NEW VIEW curve MUST oscillate around a stable mean within upper and lower bounds.
11. The bounds (upper and lower) MUST be shown as dashed horizontal lines on the new view.
12. The stable mean MUST be shown as a solid or distinct line between the bounds.
13. "Drift No More" is a real paper at arXiv:2510.07777 -- do NOT fabricate or alter the citation.
14. Three restoring forces are exactly: periodic reinforcement, memory blocks, activation capping.
15. The visual contrast between old (decay) and new (equilibrium) MUST be immediately apparent.
16. Do NOT imply the equilibrium curve is perfectly periodic -- it is irregular but bounded.

## Alt Text

Split-panel comparison of persona drift models showing the old view of inevitable monotonic decay versus the new view from Drift No More research of bounded controllable equilibrium maintained by restoring forces including periodic reinforcement, memory blocks, and activation capping for persona coherence

## Image Embed

![Split-panel comparison of persona drift models showing the old view of inevitable monotonic decay versus the new view from Drift No More research of bounded controllable equilibrium maintained by restoring forces including periodic reinforcement, memory blocks, and activation capping for persona coherence](docs/figures/repo-figures/assets/fig-persona-30-drift-equilibrium.jpg)

*Split-panel comparison: Old View shows persona drift as monotonic decay; New View (per "Drift No More," arXiv:2510.07777) shows drift as bounded equilibrium maintained by restoring forces -- periodic reinforcement, memory blocks, and activation capping.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-30",
    "title": "Drift as Controllable Equilibrium",
    "audience": "L3",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Persona drift is not inevitable decay but a controllable equilibrium maintained by restoring forces -- periodic reinforcement, memory blocks, and activation capping.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Old View Panel",
        "role": "problem_statement",
        "is_highlighted": false,
        "labels": ["OLD VIEW", "Inevitable decay"]
      },
      {
        "name": "New View Panel",
        "role": "confidence_high",
        "is_highlighted": true,
        "labels": ["NEW VIEW", "Bounded equilibrium"]
      },
      {
        "name": "Decay Curve",
        "role": "confidence_low",
        "is_highlighted": false,
        "labels": ["Monotonically decreasing"]
      },
      {
        "name": "Equilibrium Curve",
        "role": "confidence_high",
        "is_highlighted": true,
        "labels": ["Oscillating around stable mean"]
      },
      {
        "name": "Restoring Forces",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Periodic reinforcement", "Memory blocks", "Activation capping"]
      }
    ],
    "relationships": [
      {
        "from": "Old View Panel",
        "to": "New View Panel",
        "type": "arrow",
        "label": "paradigm shift"
      },
      {
        "from": "Restoring Forces",
        "to": "Equilibrium Curve",
        "type": "dashed",
        "label": "maintain bounded oscillation"
      }
    ],
    "callout_boxes": [
      {
        "heading": "PARADIGM SHIFT",
        "body_text": "Drift is a controllable equilibrium, not inevitable decay",
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
- [x] Anti-hallucination rules listed (8 default + 8 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L3)
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
