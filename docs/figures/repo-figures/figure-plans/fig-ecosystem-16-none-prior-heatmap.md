# fig-ecosystem-16: Ecosystem Node "None" Prior Heatmap

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-16 |
| **Title** | Ecosystem Node "None" Prior Heatmap |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | A (Hero) |

## Purpose

Visualizes the 0.40-0.55 "none" priors across ecosystem nodes as a heatmap, encoding strategic ambiguity as honest uncertainty rather than disinterest. Contrasts ecosystem node uncertainty against core infrastructure nodes (which have lower "none" priors due to selected options). Answers: "Why are 'none' priors so high across ecosystem nodes, and what does that signal?"

## Key Message

High "none" priors (0.40-0.55) across ecosystem nodes encode honest uncertainty -- the scaffold captures the possibility space without committing to partnerships that haven't materialized.

## Visual Concept

Hero layout with a grid/heatmap as the central element. Each of the 28 ecosystem nodes appears as a cell, colored by "none" prior probability intensity (darker = higher "none" prior). Core infrastructure nodes appear in a contrasting strip with lower "none" priors for visual comparison. A prominent callout reads "Strategic ambiguity by design."

```
+---------------------------------------------------------------+
|  ECOSYSTEM NODE "NONE" PRIOR HEATMAP                           |
|  -- Strategic Ambiguity by Design                              |
+---------------------------------------------------------------+
|                                                                |
|  ECOSYSTEM NODES (28 nodes)                                    |
|  "none" prior intensity: darker = higher probability           |
|                                                                |
|  ┌──┬──┬──┬──┬──┬──┬──┐                                      |
|  │▓▓│▓▓│▓▓│▓▓│▓▓│▓▓│▓▓│  0.50-0.55 range                    |
|  ├──┼──┼──┼──┼──┼──┼──┤  (company partnerships,              |
|  │▓▓│▓▓│▓▓│▓▓│▓▓│▓▓│▓▓│   external integrations)             |
|  ├──┼──┼──┼──┼──┼──┼──┤                                      |
|  │▓ │▓ │▓ │▓ │▓ │▓ │▓ │  0.45-0.50 range                    |
|  ├──┼──┼──┼──┼──┼──┼──┤  (protocol choices,                  |
|  │▓ │▓ │▓ │▓ │▓ │▓ │▓ │   infrastructure options)             |
|  └──┴──┴──┴──┴──┴──┴──┘                                      |
|                                                                |
|  vs CORE INFRASTRUCTURE (contrast)                             |
|  ┌──┬──┬──┬──┬──┬──┬──┐                                      |
|  │░ │░ │░ │░ │░ │░ │░ │  0.15-0.35 range                    |
|  └──┴──┴──┴──┴──┴──┴──┘  (selected options, lower "none")    |
|                                                                |
|  ┌─────────────────────────────────────────────────────────┐  |
|  │  "STRATEGIC AMBIGUITY BY DESIGN"                         │  |
|  │  High "none" encodes: honest uncertainty, resource       │  |
|  │  constraints, sequential strategy. NOT disinterest.      │  |
|  └─────────────────────────────────────────────────────────┘  |
|                                                                |
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
    content: 'ECOSYSTEM NODE "NONE" PRIOR HEATMAP'
    role: title

  - id: ecosystem_grid_zone
    bounds: [80, 150, 1760, 480]
    role: content_area

  - id: core_contrast_zone
    bounds: [80, 660, 1760, 120]
    role: content_area

  - id: callout_zone
    bounds: [80, 820, 1760, 180]
    role: callout_box

anchors:
  - id: heatmap_grid
    position: [960, 390]
    size: [1600, 400]
    role: decision_point
    label: "Ecosystem node heatmap"

  - id: core_strip
    position: [960, 720]
    size: [1600, 80]
    role: selected_option
    label: "Core infrastructure contrast"

  - id: legend_high
    position: [1700, 220]
    size: [200, 40]
    role: confidence_low
    label: "0.50-0.55 (high none)"

  - id: legend_mid
    position: [1700, 350]
    size: [200, 40]
    role: confidence_medium
    label: "0.40-0.50 (mid none)"

  - id: legend_low
    position: [1700, 720]
    size: [200, 40]
    role: confidence_high
    label: "0.15-0.35 (low none)"

  - id: callout_box
    position: [960, 910]
    size: [1600, 140]
    role: callout_bar
    label: "Strategic ambiguity by design"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | 'ECOSYSTEM NODE "NONE" PRIOR HEATMAP' with coral accent square |
| Ecosystem heatmap grid | `decision_point` | 28 cells, each representing an ecosystem node, colored by "none" prior intensity |
| Core infrastructure contrast strip | `selected_option` | Lower "none" priors (0.15-0.35) showing already-decided infrastructure |
| Legend -- high none | `confidence_low` | 0.50-0.55 range indicator (red-toned, high uncertainty) |
| Legend -- mid none | `confidence_medium` | 0.40-0.50 range indicator (amber-toned) |
| Legend -- low none (core) | `confidence_high` | 0.15-0.35 range indicator (green-toned, lower uncertainty) |
| Strategic ambiguity callout | `callout_bar` | "Strategic ambiguity by design" with explanation |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Ecosystem grid | Core contrast | bidirectional | "uncertainty gradient" |
| Section 5 design rationale | All ecosystem nodes | dashed | "strategic ambiguity encoding" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "STRATEGIC AMBIGUITY BY DESIGN" | High "none" encodes honest uncertainty, resource constraints, and sequential strategy -- NOT disinterest | bottom-center |
| "WHAT HIGH 'NONE' MEANS" | The scaffold captures possibility space without committing to partnerships that haven't materialized | right-margin |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "ECOSYSTEM NODES"
- Label 2: "CORE INFRASTRUCTURE"
- Label 3: "0.50-0.55 (high none)"
- Label 4: "0.40-0.50 (mid none)"
- Label 5: "0.15-0.35 (low none)"
- Label 6: "Strategic ambiguity"
- Label 7: "Honest uncertainty"
- Label 8: "28 ecosystem nodes"

### Caption (for embedding in documentation)

Heatmap of "none" prior probabilities across 28 ecosystem nodes (0.40-0.55 range) contrasted against core infrastructure nodes (0.15-0.35 range), encoding strategic ambiguity by design -- the scaffold captures the possibility space without committing to partnerships that haven't materialized.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `decision_point`, `selected_option`, `confidence_low` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Most ecosystem nodes have "none" priors between 0.40 and 0.55 -- this is the primary data being visualized.
10. Core infrastructure nodes have selected options with lower "none" priors (0.15-0.35) -- used as visual contrast only.
11. This concept comes from `docs/planning/expand-probabilistic-prd-to-discussion.md` Section 5 "Strategic Ambiguity by Design."
12. High "none" priors encode three things: honest uncertainty, resource constraints, sequential strategy.
13. Do NOT interpret high "none" as disinterest or rejection -- it means honest uncommitted state.
14. The 28 ecosystem nodes are the nodes added in PRD v3.0.0 -- do NOT include core infrastructure nodes in the heatmap count.
15. Individual node names may be shown as cell labels but exact "none" values should be approximate ranges, not precise to decimal places.
16. The heatmap is a visualization of strategic posture, not a recommendation to avoid partnerships.

## Alt Text

None prior heatmap: ecosystem nodes show 0.40-0.55 strategic ambiguity encoding

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-16",
    "title": "Ecosystem Node 'None' Prior Heatmap",
    "audience": "L2",
    "layout_template": "A"
  },
  "content_architecture": {
    "primary_message": "High 'none' priors (0.40-0.55) across ecosystem nodes encode honest uncertainty -- the scaffold captures the possibility space without committing to partnerships that haven't materialized.",
    "layout_flow": "centered",
    "key_structures": [
      {
        "name": "Ecosystem Heatmap Grid",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["ECOSYSTEM NODES", "28 nodes", "0.40-0.55 range"]
      },
      {
        "name": "Core Infrastructure Contrast",
        "role": "selected_option",
        "is_highlighted": false,
        "labels": ["CORE INFRASTRUCTURE", "0.15-0.35 range"]
      },
      {
        "name": "Strategic Ambiguity Callout",
        "role": "callout_bar",
        "is_highlighted": true,
        "labels": ["Strategic ambiguity by design"]
      }
    ],
    "relationships": [
      {
        "from": "Ecosystem grid",
        "to": "Core contrast",
        "type": "bidirectional",
        "label": "uncertainty gradient"
      }
    ],
    "callout_boxes": [
      {
        "heading": "STRATEGIC AMBIGUITY BY DESIGN",
        "body_text": "High 'none' encodes honest uncertainty, resource constraints, and sequential strategy -- NOT disinterest",
        "position": "bottom-center"
      },
      {
        "heading": "WHAT HIGH 'NONE' MEANS",
        "body_text": "The scaffold captures possibility space without committing to partnerships that haven't materialized",
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
- [x] Layout template identified (A)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
