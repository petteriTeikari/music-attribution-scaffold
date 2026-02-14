# fig-supplementary-07: Full PRD Network Topology (Academic)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-supplementary-07 |
| **Title** | Full PRD Network Topology (Academic) |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | Supplementary materials (supplementary.tex \missingfigure placeholder), docs/figures/repo-figures/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 3:4 (portrait, for print) |
| **Layout Template** | B (Multi-Panel) |
| **Medium** | Nano Banana Pro (print-ready) |

## Purpose

Adapts fig-prd-02 content for academic print -- no cream background, LaTeX-compatible, high-contrast for B&W printing. Answers: "What is the complete architectural decision space for the music attribution scaffold, in a format suitable for journal supplementary materials?"

## Key Message

78-node Bayesian decision network across 5 levels with ~131 conditional probability edges -- the complete architectural decision space for the music attribution scaffold.

## Visual Concept

Portrait layout with 5 level bands arranged vertically. L1 Business (4 nodes) at top, L5 Operations (14 nodes) at bottom. Core nodes (50) on the left half, ecosystem nodes (28) on the right half. Edges shown as thin lines with direction arrows. High contrast for B&W print readability.

```
+-------------------------------------------+
|  FULL PRD NETWORK TOPOLOGY                 |
|  78 Nodes · ~131 Edges · 5 Levels          |
+-------------------------------------------+
|                                            |
|  L1 BUSINESS (4 nodes)                     |
|  ┌────┐ ┌────┐ ┌────┐ ┌────┐              |
|  │BvB │ │TgtM│ │Rev │ │Reg │              |
|  └─┬──┘ └─┬──┘ └─┬──┘ └─┬──┘              |
|    │       │      │      │                  |
|  L2 ARCHITECTURE (9 nodes)                 |
|  CORE (7)          │  ECOSYSTEM (2)         |
|  ┌──┐┌──┐┌──┐┌──┐ │  ┌──────┐┌──────┐     |
|  │DM││AP││SD││AF│ │  │PltStg││PrtMdl│     |
|  └──┘└──┘└──┘└──┘ │  └──┬───┘└──┬───┘     |
|  ┌──┐┌──┐┌──┐     │     │       │          |
|  │AD││UA││  │     │     │       │          |
|  └──┘└──┘└──┘     │     │       │          |
|                    │     │       │          |
|  L3 IMPLEMENTATION (38 nodes)              |
|  CORE (14)         │  ECOSYSTEM (24)        |
|  ┌─┐┌─┐┌─┐┌─┐┌─┐  │  ┌─┐┌─┐┌─┐┌─┐┌─┐    |
|  │ ││ ││ ││ ││ │  │  │ ││ ││ ││ ││ │    |
|  └─┘└─┘└─┘└─┘└─┘  │  └─┘└─┘└─┘└─┘└─┘    |
|  ┌─┐┌─┐┌─┐┌─┐┌─┐  │  ┌─┐┌─┐┌─┐┌─┐       |
|  │ ││ ││ ││ ││ │  │  │ ││ ││ ││ │       |
|  └─┘└─┘└─┘└─┘└─┘  │  └─┘└─┘└─┘└─┘       |
|  ┌─┐┌─┐┌─┐┌─┐     │  + 15 more            |
|  │ ││ ││ ││ │     │                        |
|  └─┘└─┘└─┘└─┘     │                        |
|                    │                        |
|  L4 DEPLOYMENT (13 nodes)                  |
|  CORE (9)          │  ECOSYSTEM (4)         |
|  ┌──┐┌──┐┌──┐┌──┐ │  ┌──┐┌──┐┌──┐┌──┐    |
|  │  ││  ││  ││  │ │  │  ││  ││  ││  │    |
|  └──┘└──┘└──┘└──┘ │  └──┘└──┘└──┘└──┘    |
|  ┌──┐┌──┐┌──┐┌──┐ │                        |
|  │  ││  ││  ││  │ │                        |
|  └──┘└──┘└──┘└──┘ │                        |
|  ┌──┐              │                        |
|  │  │              │                        |
|  └──┘              │                        |
|                    │                        |
|  L5 OPERATIONS (14 nodes)                  |
|  CORE (10)         │  ECOSYSTEM (4)         |
|  ┌──┐┌──┐┌──┐┌──┐ │  ┌──┐┌──┐┌──┐┌──┐    |
|  │  ││  ││  ││  │ │  │  ││  ││  ││  │    |
|  └──┘└──┘└──┘└──┘ │  └──┘└──┘└──┘└──┘    |
|  ┌──┐┌──┐┌──┐┌──┐ │                        |
|  │  ││  ││  ││  │ │                        |
|  └──┘└──┘└──┘└──┘ │                        |
|  ┌──┐┌──┐          │                        |
|  │  ││  │          │                        |
|  └──┘└──┘          │                        |
|                                            |
+-------------------------------------------+
|  LEGEND                                    |
|  ─── same-level  ─·─ adjacent  ··· skip   |
|  ▪ core (50)   □ ecosystem (28)            |
+-------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1080
  height: 1440
  background: white  # Academic print -- WHITE, not cream

zones:
  - id: title_zone
    bounds: [0, 0, 1080, 100]
    content: "FULL PRD NETWORK TOPOLOGY"
    role: title

  - id: l1_band
    bounds: [40, 120, 1000, 120]
    role: level_band
    label: "L1 BUSINESS (4)"

  - id: l2_band
    bounds: [40, 260, 1000, 160]
    role: level_band
    label: "L2 ARCHITECTURE (9)"

  - id: l3_band
    bounds: [40, 440, 1000, 320]
    role: level_band
    label: "L3 IMPLEMENTATION (38)"

  - id: l4_band
    bounds: [40, 780, 1000, 160]
    role: level_band
    label: "L4 DEPLOYMENT (13)"

  - id: l5_band
    bounds: [40, 960, 1000, 200]
    role: level_band
    label: "L5 OPERATIONS (14)"

  - id: core_column
    bounds: [40, 120, 500, 1040]
    role: content_area
    label: "Core (50 nodes)"

  - id: ecosystem_column
    bounds: [560, 260, 480, 900]
    role: content_area_highlighted
    label: "Ecosystem (28 nodes)"

  - id: legend_zone
    bounds: [40, 1180, 1000, 100]
    role: callout_bar

anchors:
  - id: l1_nodes
    position: [200, 160]
    size: [640, 60]
    role: decision_point
    label: "4 L1 business nodes"

  - id: l2_core_nodes
    position: [120, 300]
    size: [380, 80]
    role: decision_point
    label: "7 L2 core architecture nodes"

  - id: l2_ecosystem_nodes
    position: [600, 300]
    size: [380, 80]
    role: decision_point
    label: "2 L2 ecosystem nodes"

  - id: l3_core_nodes
    position: [120, 500]
    size: [380, 220]
    role: decision_point
    label: "14 L3 core implementation nodes"

  - id: l3_ecosystem_nodes
    position: [600, 500]
    size: [380, 220]
    role: decision_point
    label: "24 L3 ecosystem component nodes"

  - id: l4_core_nodes
    position: [120, 820]
    size: [380, 80]
    role: decision_point
    label: "9 L4 core deployment nodes"

  - id: l4_ecosystem_nodes
    position: [600, 820]
    size: [380, 80]
    role: decision_point
    label: "4 L4 ecosystem deployment nodes"

  - id: l5_core_nodes
    position: [120, 1000]
    size: [380, 120]
    role: decision_point
    label: "10 L5 core operations nodes"

  - id: l5_ecosystem_nodes
    position: [600, 1000]
    size: [380, 80]
    role: decision_point
    label: "4 L5 ecosystem operations nodes"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "FULL PRD NETWORK TOPOLOGY" -- high contrast, no accent color for B&W |
| Subtitle | `label_editorial` | "78 Nodes, ~131 Edges, 5 Levels" |
| L1 Business band (4 nodes) | `level_band` | build_vs_buy, target_market, revenue_model, regulatory_posture |
| L2 Architecture band (9 nodes) | `level_band` | 7 core + 2 ecosystem (platform_strategy, partnership_model) |
| L3 Implementation band (38 nodes) | `level_band` | 14 core implementation + 24 ecosystem components |
| L4 Deployment band (13 nodes) | `level_band` | 9 core + 4 ecosystem deployment nodes |
| L5 Operations band (14 nodes) | `level_band` | 10 core + 4 ecosystem operations nodes |
| Core column | `content_area` | 50 nodes forming the original scaffold core |
| Ecosystem column | `content_area_highlighted` | 28 nodes added in v3.0.0 expansion |
| Edge lines | `data_flow` | ~131 edges with line weight variation for B&W differentiation |
| Legend bar | `callout_bar` | Edge type legend using line styles (not colors) |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| L1 nodes | L2 nodes | arrow | "business drives architecture" |
| L2 nodes | L3 nodes | arrow | "architecture drives implementation" |
| L3 nodes | L4 nodes | arrow | "implementation drives deployment" |
| L4 nodes | L5 nodes | arrow | "deployment drives operations" |
| Same-level nodes | Same-level nodes | bidirectional | "peer constraints" |
| Core nodes | Ecosystem nodes | dashed | "integration surfaces" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "v3.0.0" | Network version identifier | top-right |
| "LEVEL COUNTS" | L1=4, L2=9, L3=38, L4=13, L5=14 | bottom-left |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Full PRD Network (Academic)"
- Label 2: "78 Nodes, ~131 Edges"
- Label 3: "Core (50) + Ecosystem (28)"
- Label 4: "5 Levels: L1-L5"
- Label 5: "v3.0.0"

### Caption (for embedding in documentation)

The complete 78-node Bayesian decision network spanning 5 levels (L1 Business through L5 Operations) with approximately 131 conditional probability edges, adapted for academic print format. Core infrastructure (50 nodes) and ecosystem integration (28 nodes) are distinguished by fill style for B&W readability.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `decision_point`, `level_band`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be WHITE** -- EXCEPTION to default cream rule. This is an academic print figure for LaTeX/PDF. Pure white background for print compatibility.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. **This ADAPTS fig-prd-02 for academic print.** Key differences from repo version: (1) WHITE background, not cream, for LaTeX compatibility. (2) HIGH CONTRAST -- must be readable in B&W print. (3) PORTRAIT 3:4 -- for journal/preprint column format.
10. Node counts: L1=4, L2=9, L3=38 (14 implementation + 24 components), L4=13, L5=14 = **78 total**. Do NOT alter these counts.
11. Edge count: ~131 edges from `_network.yaml` v3.0.0. Do NOT invent a different count.
12. Use **line weight variation** (not color) to differentiate edge types for B&W compatibility: thin = same-level, medium = adjacent-level, thick = skip-connections.
13. Use **fill patterns** (solid, hatched, dotted) or **stroke weight** to differentiate core vs. ecosystem nodes in B&W.
14. The supplementary.tex file has `\missingfigure{Full PRD Network Topology}` placeholder that this figure will replace.
15. Do NOT include node names not in the actual `_network.yaml` v3.0.0.

## Alt Text

Academic print PRD: 78-node Bayesian decision network across 5 levels for print format

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "supplementary-07",
    "title": "Full PRD Network Topology (Academic)",
    "audience": "L2",
    "layout_template": "B",
    "medium": "nano_banana_pro_print"
  },
  "content_architecture": {
    "primary_message": "78-node Bayesian decision network across 5 levels with ~131 conditional probability edges, adapted for academic print.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "L1 Business",
        "role": "level_band",
        "is_highlighted": false,
        "labels": ["4 nodes", "Business strategy"]
      },
      {
        "name": "L2 Architecture",
        "role": "level_band",
        "is_highlighted": false,
        "labels": ["9 nodes", "7 core + 2 ecosystem"]
      },
      {
        "name": "L3 Implementation",
        "role": "level_band",
        "is_highlighted": true,
        "labels": ["38 nodes", "14 core + 24 ecosystem"]
      },
      {
        "name": "L4 Deployment",
        "role": "level_band",
        "is_highlighted": false,
        "labels": ["13 nodes", "9 core + 4 ecosystem"]
      },
      {
        "name": "L5 Operations",
        "role": "level_band",
        "is_highlighted": false,
        "labels": ["14 nodes", "10 core + 4 ecosystem"]
      },
      {
        "name": "Core Column",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["50 core nodes"]
      },
      {
        "name": "Ecosystem Column",
        "role": "content_area_highlighted",
        "is_highlighted": true,
        "labels": ["28 ecosystem nodes"]
      }
    ],
    "relationships": [
      {
        "from": "L1 Business",
        "to": "L2 Architecture",
        "type": "arrow",
        "label": "business drives architecture"
      },
      {
        "from": "L2 Architecture",
        "to": "L3 Implementation",
        "type": "arrow",
        "label": "architecture drives implementation"
      },
      {
        "from": "L3 Implementation",
        "to": "L4 Deployment",
        "type": "arrow",
        "label": "implementation drives deployment"
      },
      {
        "from": "L4 Deployment",
        "to": "L5 Operations",
        "type": "arrow",
        "label": "deployment drives operations"
      },
      {
        "from": "Core nodes",
        "to": "Ecosystem nodes",
        "type": "dashed",
        "label": "integration surfaces"
      }
    ],
    "callout_boxes": [
      {
        "heading": "v3.0.0",
        "body_text": "Network version identifier",
        "position": "top-right"
      },
      {
        "heading": "LEVEL COUNTS",
        "body_text": "L1=4, L2=9, L3=38, L4=13, L5=14",
        "position": "bottom-left"
      }
    ]
  },
  "print_spec": {
    "background": "white",
    "color_mode": "B&W compatible (high contrast)",
    "aspect_ratio": "3:4 portrait",
    "target": "LaTeX supplementary materials",
    "placeholder": "\\missingfigure{Full PRD Network Topology}"
  }
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed (8 default + 7 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L2)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro (print-ready variant)
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in supplementary.tex
