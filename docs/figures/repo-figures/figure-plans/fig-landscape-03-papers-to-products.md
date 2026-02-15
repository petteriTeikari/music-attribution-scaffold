# fig-landscape-03: Papers to Products: Academic-to-Industry Pipeline

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-03 |
| **Title** | Papers to Products: Academic-to-Industry Pipeline |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

This figure maps the lineage from foundational research papers to commercial attribution products, showing that every commercial approach traces to a specific research tradition. It answers: "Where did these attribution methods come from, and why is there a translation gap between academia and industry?"

## Key Message

Every commercial attribution approach traces to specific research traditions -- influence functions lead to gradient-tracking products, embeddings lead to content-matching services, unlearning enters translation.

## Visual Concept

Three horizontal streams flowing left-to-right from academic papers to commercial products, with a visible "translation gap" zone in the middle. Each stream shows: foundational paper, key follow-on work, and resulting commercial applications or lack thereof. The streams are stacked vertically and color-coded by research tradition. A dashed vertical zone in the center represents the translation gap.

```
+---------------------------------------------------------------+
|  PAPERS TO PRODUCTS                                            |
|  ■ Academic-to-Industry Pipeline                               |
+---------------------------------------------------------------+
|                                                                |
|  RESEARCH                 TRANSLATION         COMMERCIAL       |
|  TRADITION                GAP                  APPLICATION     |
|  ──────────          ┊ ─────────── ┊          ───────────      |
|                      ┊             ┊                           |
|  Stream 1: INFLUENCE FUNCTIONS     ┊                           |
|  ┌────────────┐  ┌───┊──────────┐  ┊  ┌──────────────┐        |
|  │ Koh & Liang│──│ Ml┊dozeniec  │──┊──│ Gradient-    │        |
|  │ 2017       │  │ 20┊24        │  ┊  │ tracking     │        |
|  └────────────┘  └───┊──────────┘  ┊  │ companies    │        |
|                      ┊             ┊  └──────────────┘        |
|                      ┊             ┊                           |
|  Stream 2: EMBEDDING SIMILARITY    ┊                           |
|  ┌────────────┐  ┌───┊──────────┐  ┊  ┌──────────────┐        |
|  │ CLMR/CLAP  │──│ Co┊ntrastive │──┊──│ Content-     │        |
|  │ embeddings │  │ au┊dio repr. │  ┊  │ matching     │        |
|  └────────────┘  └───┊──────────┘  ┊  │ services     │        |
|                      ┊             ┊  └──────────────┘        |
|                      ┊             ┊                           |
|  Stream 3: ATTRIBUTION-BY-DESIGN   ┊                           |
|  ┌────────────┐  ┌───┊──────────┐  ┊  ┌──────────────┐        |
|  │ Morreale   │──│ In┊ference-  │──┊──│ Inference-   │        |
|  │ et al. 2025│  │ ti┊me provn. │  ┊  │ time systems │        |
|  └────────────┘  └───┊──────────┘  ┊  │ (emerging)   │        |
|                      ┊             ┊  └──────────────┘        |
|                      ┊             ┊                           |
+---------------------------------------------------------------+
|  ■ Most papers never cross the translation gap.                |
|    Commercial viability requires compute + data + legal fit.   |
+---------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: warm_cream

title_block:
  position: [60, 40]
  width: 1800
  height: 80
  elements:
    - type: heading_display
      text: "PAPERS TO PRODUCTS"
    - type: label_editorial
      text: "Academic-to-Industry Pipeline"

column_headers:
  position: [60, 140]
  width: 1800
  height: 60
  columns:
    - { label: "RESEARCH TRADITION", x: 60, width: 500 }
    - { label: "TRANSLATION GAP", x: 680, width: 400 }
    - { label: "COMMERCIAL APPLICATION", x: 1200, width: 600 }

translation_gap_zone:
  position: [680, 200]
  width: 400
  height: 680
  style: dashed_border
  opacity: 0.15

stream_influence:
  position: [60, 220]
  width: 1800
  height: 200
  nodes:
    - { label: "Koh & Liang 2017", type: "paper", x: 100, y: 100 }
    - { label: "Mlodozeniec 2024", type: "paper", x: 780, y: 100 }
    - { label: "Gradient-tracking companies", type: "product", x: 1400, y: 100 }

stream_embedding:
  position: [60, 440]
  width: 1800
  height: 200
  nodes:
    - { label: "CLMR/CLAP embeddings", type: "paper", x: 100, y: 100 }
    - { label: "Contrastive audio repr.", type: "method", x: 780, y: 100 }
    - { label: "Content-matching services", type: "product", x: 1400, y: 100 }

stream_abd:
  position: [60, 660]
  width: 1800
  height: 200
  nodes:
    - { label: "Morreale et al. 2025", type: "paper", x: 100, y: 100 }
    - { label: "Inference-time provenance", type: "method", x: 780, y: 100 }
    - { label: "Inference-time systems (emerging)", type: "product", x: 1400, y: 100 }

callout_bottom:
  position: [60, 900]
  width: 1800
  height: 100
  elements:
    - type: callout_bar
      text: "Most papers never cross the translation gap."
    - type: label_editorial
      text: "Commercial viability requires compute + data + legal fit."
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "PAPERS TO PRODUCTS" with coral accent square |
| Subtitle | `label_editorial` | "Academic-to-Industry Pipeline" |
| Column headers | `label_editorial` | "RESEARCH TRADITION", "TRANSLATION GAP", "COMMERCIAL APPLICATION" |
| Translation gap zone | `decision_point` | Dashed vertical zone representing the gap between research and commercialization |
| Stream 1: Influence functions | `data_flow` | Koh & Liang 2017 to Mlodozeniec 2024 to gradient-tracking companies |
| Stream 2: Embedding similarity | `data_flow` | CLMR/CLAP to contrastive audio representations to content-matching services |
| Stream 3: Attribution-by-Design | `data_flow` | Morreale et al. 2025 to inference-time provenance to emerging systems |
| Paper nodes | `processing_stage` | Rectangular nodes for foundational papers |
| Product nodes | `primary_outcome` | Rectangular nodes for commercial applications |
| Flow arrows | `data_flow` | Directional arrows connecting paper to product |
| Bottom callout | `callout_bar` | "Most papers never cross the translation gap" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Koh & Liang 2017 | Mlodozeniec 2024 | extends | "Scale to generative models" |
| Mlodozeniec 2024 | Gradient-tracking | translates | "Crosses gap" |
| CLMR/CLAP | Contrastive audio | extends | "Audio-specific embeddings" |
| Contrastive audio | Content-matching | translates | "Crosses gap" |
| Morreale et al. 2025 | Inference-time provenance | proposes | "New paradigm" |
| Inference-time provenance | Inference-time systems | translates | "Entering translation" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Translation Gap | "Requires: compute budget, training data access, legal viability" | Center dashed zone |
| Bottom Insight | "Most papers never cross the translation gap" | Full-width bottom bar |

## Text Content

### Labels (Max 30 chars each)

- PAPERS TO PRODUCTS
- RESEARCH TRADITION
- TRANSLATION GAP
- COMMERCIAL APPLICATION
- Koh & Liang 2017
- Mlodozeniec 2024
- Gradient-tracking companies
- CLMR/CLAP embeddings
- Contrastive audio repr.
- Content-matching services
- Morreale et al. 2025
- Inference-time provenance
- Inference-time systems
- INFLUENCE FUNCTIONS
- EMBEDDING SIMILARITY
- ATTRIBUTION-BY-DESIGN

### Caption (for embedding in documentation)

Three research traditions flow from academia to industry: influence functions (Koh & Liang 2017 through Mlodozeniec 2024 to gradient-tracking products), embedding similarity (CLMR/CLAP to content-matching services), and attribution-by-design (Morreale et al. 2025 to emerging inference-time systems). Most papers never cross the translation gap between research and commercial viability.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)**.
5. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

1. Paper citations must be accurate: Koh & Liang 2017, Mlodozeniec 2024, Morreale et al. 2025 -- do NOT invent citations.
2. CLMR and CLAP are real models -- do NOT expand acronyms incorrectly.
3. Do NOT name specific commercial companies in the "product" nodes -- keep them as category descriptions.
4. The translation gap is a CONCEPTUAL zone, not a timeline -- do NOT add dates to the gap.
5. Do NOT imply that all three streams are equally mature -- attribution-by-design is explicitly "emerging."
6. Stream arrows should be thin and elegant, not thick block arrows.
7. The dashed translation gap zone should be subtle, not visually dominant.

## Alt Text

Three research streams flowing from papers to products through a translation gap: influence functions, embeddings, design.

## JSON Export Block

```json
{
  "id": "fig-landscape-03",
  "title": "Papers to Products: Academic-to-Industry Pipeline",
  "audience": "L2",
  "priority": "P0",
  "layout": "C",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Explain",
  "streams": [
    {
      "name": "Influence Functions",
      "papers": ["Koh & Liang 2017", "Mlodozeniec 2024"],
      "product_category": "Gradient-tracking companies"
    },
    {
      "name": "Embedding Similarity",
      "papers": ["CLMR/CLAP"],
      "product_category": "Content-matching services"
    },
    {
      "name": "Attribution-by-Design",
      "papers": ["Morreale et al. 2025"],
      "product_category": "Inference-time systems (emerging)"
    }
  ],
  "semantic_tags_used": [
    "heading_display", "label_editorial", "data_flow", "decision_point",
    "processing_stage", "primary_outcome", "callout_bar"
  ]
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
- [x] Audience level correct (L1/L2/L3/L4)
- [x] Layout template identified (A/B/C/D/E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
