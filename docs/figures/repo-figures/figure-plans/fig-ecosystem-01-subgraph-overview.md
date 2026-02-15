# fig-ecosystem-01: Ecosystem Integration Subgraph Overview

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-01 |
| **Title** | Ecosystem Integration Subgraph Overview |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | A (Hero) |

## Purpose

Shows the 28 new ecosystem nodes as a coherent subgraph connecting platform strategy to 18 components, 4 deployment, and 4 operations nodes. Answers: "How does the v3.0.0 expansion relate to the existing core infrastructure?"

## Key Message

28 new ecosystem nodes form a coherent subgraph -- 2 L2 architecture, 18 L3 components, 4 L4 deployment, 4 L5 operations -- connected by ~63 new edges.

## Visual Concept

Hero view with dual-zone layout. Core infrastructure (50 existing nodes) occupies the left zone, muted. Ecosystem integration (28 new nodes) occupies the right zone, highlighted. Level bands L2-L5 run horizontally across both zones, showing how new nodes slot into the existing level hierarchy.

```
+-----------------------------------------------------------------------+
|  ECOSYSTEM INTEGRATION SUBGRAPH                                        |
|  ■ 28 New Nodes Within 78-Node Network                                |
+-----------------------------------------------------------------------+
|                                                                        |
|  CORE INFRASTRUCTURE (50)       ECOSYSTEM INTEGRATION (28)             |
|  (muted)                        (highlighted)                          |
|                                                                        |
|  L2 ─────────────────────────────────────────────────────────          |
|  ┌─────────┐┌─────────┐        ┌──────────────┐┌────────────┐         |
|  │Data Mdl ││API Proto│   ...  │ Platform     ││Partnership │         |
|  │         ││         │        │ Strategy     ││ Model      │         |
|  └─────┬───┘└─────┬───┘        └──────┬───────┘└──────┬─────┘         |
|        │          │                    │               │                |
|  L3 ─────────────────────────────────────────────────────────          |
|  ┌───┐┌───┐┌───┐┌───┐...      ┌───┐┌───┐┌───┐┌───┐┌───┐┌───┐        |
|  │DB ││GS ││VS ││LLM│        │TDA││CMO││CID││AMP││MRI││WMD│        |
|  └─┬─┘└───┘└───┘└───┘        └─┬─┘└─┬─┘└───┘└───┘└───┘└───┘        |
|    │                            │    │   + 12 more L3 nodes            |
|  L4 ─────────────────────────────────────────────────────────          |
|  ┌───────┐┌───────┐...         ┌──────────┐┌──────────┐               |
|  │Compute││DB Host│            │Compliance││Provenance│               |
|  └───────┘└───────┘            │Pipeline  ││Store     │               |
|                                └──────────┘└──────────┘               |
|  L5 ─────────────────────────────────────────────────────────          |
|  ┌───────┐┌───────┐...         ┌──────────┐┌──────────┐               |
|  │Observ ││Scale  │            │Regulatory││Market    │               |
|  └───────┘└───────┘            │Monitor   ││Intel     │               |
|                                └──────────┘└──────────┘               |
|                                                                        |
|  ■ ~63 new edges connect ecosystem to core + within subgraph           |
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
    content: "ECOSYSTEM INTEGRATION SUBGRAPH"
    role: title

  - id: core_zone
    bounds: [40, 140, 880, 860]
    content: "Core Infrastructure (50 nodes)"
    role: content_area
    opacity: 0.4

  - id: ecosystem_zone
    bounds: [960, 140, 920, 860]
    content: "Ecosystem Integration (28 nodes)"
    role: content_area_highlighted

  - id: level_band_l2
    bounds: [40, 160, 1840, 180]
    role: level_band
    label: "L2 ARCHITECTURE"

  - id: level_band_l3
    bounds: [40, 360, 1840, 260]
    role: level_band
    label: "L3 COMPONENTS"

  - id: level_band_l4
    bounds: [40, 640, 1840, 160]
    role: level_band
    label: "L4 DEPLOYMENT"

  - id: level_band_l5
    bounds: [40, 820, 1840, 160]
    role: level_band
    label: "L5 OPERATIONS"

anchors:
  - id: platform_strategy
    position: [1040, 210]
    size: [180, 80]
    role: decision_point
    label: "Platform Strategy"

  - id: partnership_model
    position: [1280, 210]
    size: [180, 80]
    role: decision_point
    label: "Partnership Model"

  - id: l3_cluster
    position: [1040, 400]
    size: [800, 180]
    role: decision_point
    label: "18 L3 component nodes"

  - id: l4_cluster
    position: [1040, 680]
    size: [400, 100]
    role: decision_point
    label: "4 L4 deployment nodes"

  - id: l5_cluster
    position: [1040, 860]
    size: [400, 100]
    role: decision_point
    label: "4 L5 operations nodes"

  - id: edge_bridge_core_to_eco
    from: core_zone
    to: ecosystem_zone
    type: dashed
    label: "cross-zone edges"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Core infrastructure zone | `content_area` | 50 existing nodes shown muted as context |
| Ecosystem integration zone | `content_area_highlighted` | 28 new nodes highlighted as the focus |
| L2 new nodes (2) | `decision_point` | platform_strategy, partnership_model |
| L3 new nodes (18) | `decision_point` | 12 category + 6 company nodes |
| L4 new nodes (4) | `decision_point` | compliance_reporting_pipeline, training_data_provenance_store, golden_dataset_management, edge_deployment_target |
| L5 new nodes (4) | `decision_point` | regulatory_monitoring, market_intelligence, attribution_accuracy_monitoring, partnership_health_metrics |
| Level bands | `level_band` | L2 through L5 horizontal bands spanning both zones |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Core L1 nodes | platform_strategy | arrow | "business inputs" |
| Core L1 nodes | partnership_model | arrow | "business inputs" |
| platform_strategy | L3 category nodes | arrow | "architecture cascades" |
| partnership_model | L3 company nodes | arrow | "partner activations" |
| L3 ecosystem nodes | L4 ecosystem nodes | arrow | "deployment requirements" |
| L4 ecosystem nodes | L5 ecosystem nodes | arrow | "operational monitoring" |
| Core L3 nodes | Ecosystem L3 nodes | dashed | "cross-zone dependencies" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "NETWORK v3.0.0" | 78 total nodes, ~123 edges, 28 new ecosystem nodes | top-right |
| "LEVEL DISTRIBUTION" | L2: +2, L3: +18, L4: +4, L5: +4 | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Core Infrastructure (50)"
- Label 2: "Ecosystem Integration (28)"
- Label 3: "Platform Strategy"
- Label 4: "Partnership Model"
- Label 5: "~63 new edges"

### Caption (for embedding in documentation)

The 28 ecosystem integration nodes form a coherent subgraph within the v3.0.0 decision network, spanning L2 architecture through L5 operations, connected to the core infrastructure by approximately 63 new edges.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `decision_point`, `content_area`, `level_band` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. v3.0.0 network has 78 total nodes. 28 new ecosystem nodes: 2 L2 (platform_strategy, partnership_model), 18 L3 (12 category + 6 company), 4 L4 (compliance_reporting_pipeline, training_data_provenance_store, golden_dataset_management, edge_deployment_target), 4 L5 (regulatory_monitoring, market_intelligence, attribution_accuracy_monitoring, partnership_health_metrics).
10. ~63 new edges. Do NOT include nodes not in the _network.yaml v3.0.0.
11. Core infrastructure contains 50 existing nodes. Do NOT alter the count or composition of existing nodes.
12. The dual-zone layout must show ecosystem nodes as visually distinct (highlighted) against muted core nodes.

## Alt Text

Subgraph overview: 28 ecosystem integration nodes forming coherent cluster within 78-node PRD network

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-01",
    "title": "Ecosystem Integration Subgraph Overview",
    "audience": "L2",
    "layout_template": "A"
  },
  "content_architecture": {
    "primary_message": "28 new ecosystem nodes form a coherent subgraph connected by ~63 new edges within the 78-node v3.0.0 decision network.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Core Infrastructure Zone",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["Core Infrastructure (50)", "Muted context"]
      },
      {
        "name": "Ecosystem Integration Zone",
        "role": "content_area_highlighted",
        "is_highlighted": true,
        "labels": ["Ecosystem Integration (28)", "L2-L5 new nodes"]
      },
      {
        "name": "Platform Strategy",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["Platform Strategy", "L2 Architecture"]
      },
      {
        "name": "Partnership Model",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["Partnership Model", "L2 Architecture"]
      }
    ],
    "relationships": [
      {
        "from": "Core L1 Business",
        "to": "Platform Strategy",
        "type": "arrow",
        "label": "business inputs shape platform choice"
      },
      {
        "from": "Platform Strategy",
        "to": "L3 Category Nodes",
        "type": "arrow",
        "label": "architecture cascades to components"
      },
      {
        "from": "Partnership Model",
        "to": "L3 Company Nodes",
        "type": "arrow",
        "label": "partner activations"
      },
      {
        "from": "L3 Ecosystem",
        "to": "L4 Ecosystem",
        "type": "arrow",
        "label": "deployment requirements"
      },
      {
        "from": "L4 Ecosystem",
        "to": "L5 Ecosystem",
        "type": "arrow",
        "label": "operational monitoring"
      }
    ],
    "callout_boxes": [
      {
        "heading": "NETWORK v3.0.0",
        "body_text": "78 total nodes, ~123 edges, 28 new ecosystem nodes",
        "position": "top-right"
      },
      {
        "heading": "LEVEL DISTRIBUTION",
        "body_text": "L2: +2, L3: +18, L4: +4, L5: +4",
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
- [x] Audience level correct (L2)
- [x] Layout template identified (A)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
