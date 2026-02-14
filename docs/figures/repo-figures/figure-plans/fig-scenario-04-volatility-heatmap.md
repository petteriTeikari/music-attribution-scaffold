# fig-scenario-04: Volatility Heatmap: 78 Nodes

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-scenario-04 |
| **Title** | Volatility Heatmap: 78 Nodes |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | A (Hero) |

## Purpose

Shows that the 78-node network exhibits a clear volatility bifurcation: the 50 core infrastructure nodes trend Stable/Shifting while the 28 ecosystem nodes are predominantly Volatile. This answers: "Which parts of the network are settled versus still in flux?"

## Key Message

The 78-node network shows a clear volatility bifurcation -- core infrastructure nodes (50) trend Stable/Shifting while ecosystem nodes (28) are predominantly Volatile, reflecting the speculative nature of partnership and integration decisions.

## Visual Concept

A hero heatmap with 78 cells arranged in horizontal level bands (L1 through L5). Each cell is colored by volatility classification: Stable = cool tone, Shifting = warm/amber tone, Volatile = hot/coral tone. The left portion of each band shows core infrastructure nodes (predominantly cool), while the right portion shows ecosystem nodes (predominantly hot). A clear visual split emerges between the two regions. A legend at the bottom maps colors to volatility classes.

```
+-----------------------------------------------------------------------+
|  VOLATILITY HEATMAP                                                    |
|  ■ 78 Nodes: Core Infrastructure vs Ecosystem                         |
+-----------------------------------------------------------------------+
|                                                                        |
|  L1 BUSINESS ─────────────────────────────────────────────────         |
|  [■][■][■][□]                                                          |
|   S   S   S   V   ← regulatory_posture = Volatile                     |
|                                                                        |
|  L2 ARCHITECTURE ──────────────────────────────────────────────        |
|  [■][■][▧][▧][■][▧][■]  [□][□]                                        |
|   S   S  Sh  Sh  S  Sh  S    V   V   ← ecosystem = Volatile           |
|                                                                        |
|  L3 IMPLEMENTATION ────────────────────────────────────────────        |
|  [■][■][■][▧][■][■][▧][▧][□][□][■][▧][■][■]                          |
|   S   S   S  Sh  S   S  Sh  Sh  V   V   S  Sh  S   S                  |
|                                                                        |
|  L3 COMPONENTS ────────────────────────────────────────────────        |
|  [▧][▧][▧][□][▧][▧]  [□][□][□][□][□][□][□][□][□][□][□][□]            |
|  Sh  Sh  Sh  V  Sh  Sh   V   V   V   V   V   V   V   V   V           |
|  ← existing commercial     ← new ecosystem (all Volatile)             |
|                                                                        |
|  L4 DEPLOYMENT ────────────────────────────────────────────────        |
|  [■][■][■][■][■][▧][■][▧][▧]  [□][□][□][□]                           |
|   S   S   S   S   S  Sh  S  Sh  Sh    V   V   V   V                   |
|                                                                        |
|  L5 OPERATIONS ────────────────────────────────────────────────        |
|  [■][■][■][■][▧][■][▧][▧][□][□]  [□][□][□][□]                        |
|   S   S   S   S  Sh  S  Sh  Sh  V   V     V   V   V   V              |
|                                                                        |
|  ─── CORE INFRASTRUCTURE (50) ───|─── ECOSYSTEM (28) ───              |
|                                                                        |
+-----------------------------------------------------------------------+
|  LEGEND: ■ Stable  ▧ Shifting  □ Volatile                             |
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
    content: "VOLATILITY HEATMAP: 78 NODES"
    role: title

  - id: heatmap_zone
    bounds: [60, 140, 1800, 800]
    role: content_area

  - id: legend_zone
    bounds: [60, 960, 1800, 80]
    role: callout_bar

anchors:
  - id: l1_band
    position: [60, 160]
    size: [1800, 80]
    role: processing_stage

  - id: l2_band
    position: [60, 260]
    size: [1800, 80]
    role: processing_stage

  - id: l3_impl_band
    position: [60, 360]
    size: [1800, 80]
    role: processing_stage

  - id: l3_comp_band
    position: [60, 460]
    size: [1800, 120]
    role: processing_stage

  - id: l4_band
    position: [60, 600]
    size: [1800, 80]
    role: processing_stage

  - id: l5_band
    position: [60, 700]
    size: [1800, 80]
    role: processing_stage

  - id: divider_line
    position: [1100, 160]
    size: [2, 640]
    role: accent_line_v

  - id: legend
    position: [60, 980]
    size: [1800, 40]
    role: callout_bar
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Heatmap cells (78) | `decision_point` | Individual cells for each node, colored by volatility |
| Stable cells | `confidence_high` | Cool-toned cells for Stable nodes |
| Shifting cells | `confidence_medium` | Warm/amber-toned cells for Shifting nodes |
| Volatile cells | `confidence_low` | Hot/coral-toned cells for Volatile nodes |
| Level band labels | `label_editorial` | L1 Business, L2 Architecture, L3 Implementation, L3 Components, L4 Deployment, L5 Operations |
| Core/Ecosystem divider | `accent_line_v` | Visual split between core infrastructure (left) and ecosystem (right) |
| Legend bar | `callout_bar` | Color key: Stable, Shifting, Volatile |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Core region (left) | Stable/Shifting | dashed | "predominantly settled" |
| Ecosystem region (right) | Volatile | dashed | "predominantly speculative" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "CORE: 50 NODES" | Predominantly Stable and Shifting -- infrastructure decisions are increasingly settled | left-margin |
| "ECOSYSTEM: 28 NODES" | Predominantly Volatile -- partnership and integration decisions reflect honest uncertainty | right-margin |
| "BIFURCATION" | Clear split between settled core and speculative ecosystem reflects phased decision-making | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "50 core infrastructure nodes"
- Label 2: "28 ecosystem nodes"
- Label 3: "Stable: settled decisions"
- Label 4: "Shifting: evolving choices"
- Label 5: "Volatile: speculative/open"
- Label 6: "Core = Stable/Shifting"
- Label 7: "Ecosystem = Volatile"
- Label 8: "Bifurcation visible"

### Caption (for embedding in documentation)

The 78-node volatility heatmap reveals a clear bifurcation: core infrastructure nodes (50) cluster in the Stable/Shifting range, while ecosystem integration nodes (28) are predominantly Volatile -- encoding honest uncertainty about partnership and integration decisions.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `confidence_high`, `confidence_medium`, `confidence_low` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text.

### Figure-Specific Rules

9. Some core nodes have formal volatility classifications from the tech-trends report: api_protocol Shifting to Stable, ai_framework_strategy Volatile to Shifting, agentic_ui_framework Volatile to Shifting, regulatory_posture Volatile (unchanged), graph_rag_engine Volatile (unchanged).
10. Ecosystem nodes (28 added in v3.0.0) are NOT formally classified in the volatility system yet. Their Volatile classification is inferred from high "none" prior probabilities (0.40-0.55) and lack of archetype-specific weights.
11. The volatility assignments for individual nodes are approximate/interpretive. Do NOT claim they come from a formal quantitative analysis unless referencing the tech-trends report directly.
12. The core/ecosystem split is 50/28 nodes. This matches the v3.0.0 network: 50 existing nodes + 28 new ecosystem nodes.
13. Do NOT use exact volatility scores -- use categorical labels (Stable, Shifting, Volatile) only.

## Alt Text

Volatility heatmap: 78 PRD nodes showing core stable vs ecosystem volatile bifurcation

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "scenario-04",
    "title": "Volatility Heatmap: 78 Nodes",
    "audience": "L2",
    "layout_template": "A"
  },
  "content_architecture": {
    "primary_message": "The 78-node network shows a clear volatility bifurcation -- core infrastructure trends Stable/Shifting while ecosystem nodes are predominantly Volatile.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Core Infrastructure Region",
        "role": "confidence_high",
        "is_highlighted": true,
        "labels": ["50 nodes", "Stable/Shifting"]
      },
      {
        "name": "Ecosystem Region",
        "role": "confidence_low",
        "is_highlighted": true,
        "labels": ["28 nodes", "Volatile"]
      },
      {
        "name": "Level Bands",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["L1", "L2", "L3 Impl", "L3 Comp", "L4", "L5"]
      }
    ],
    "relationships": [
      {
        "from": "Core region",
        "to": "Ecosystem region",
        "type": "dashed",
        "label": "volatility bifurcation boundary"
      }
    ],
    "callout_boxes": [
      {
        "heading": "BIFURCATION",
        "body_text": "Core infrastructure settled; ecosystem deliberately speculative",
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
