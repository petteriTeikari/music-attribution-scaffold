# fig-landscape-02: Where the Money Went: $500M+ by Category

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-02 |
| **Title** | Where the Money Went: $500M+ by Category |
| **Audience** | L1 (Music Industry) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

This figure reveals the structural funding gap between music generation and music attribution. It answers: "Where has the money actually gone in music AI, and what does the imbalance tell us about risk and opportunity?"

## Key Message

$375M+ went to generation, less than $70M to attribution -- a structural funding gap that creates both risk and opportunity.

## Visual Concept

Split-panel layout with a dramatic size contrast. Left panel shows the generation funding mountain (large, dominant), right panel shows the attribution funding hill (small, dwarfed). Dollar amounts in monospace. A bottom callout bar highlights the gap as both risk and opportunity. The visual asymmetry IS the message -- the left panel should visually dominate.

```
+---------------------------------------------------------------+
|  WHERE THE MONEY WENT                                          |
|  ■ $500M+ Music AI Funding by Category                        |
+-------------------------------+-------------------------------+
|                               |                               |
|  I. GENERATION                |  II. ATTRIBUTION              |
|  ─────────────                |  ──────────────               |
|                               |                               |
|      $375M+                   |      <$70M                    |
|      ┌───────────┐            |      ┌───┐                    |
|      │           │            |      │   │                    |
|      │   Suno    │            |      │   │                    |
|      │  $375M+   │            |      │   │                    |
|      │           │            |      │   │                    |
|      │           │  ┌────┐    |      │   │  ┌──┐  ┌──┐       |
|      │           │  │Udio│    |      │   │  │  │  │  │       |
|      │           │  │$33M│    |  $40M│   │  │  │  │  │       |
|      │           │  │    │    | ProR.│   │  │  │  │  │       |
|      │           │  │    │    |      │$16│  │$6│  │? │       |
|      │           │  │    │    |      │Ver│  │Mu│  │Su│       |
|      └───────────┘  └────┘    |      └───┘  └──┘  └──┘       |
|                               |                               |
+-------------------------------+-------------------------------+
|                                                                |
|  ■ THE FUNDING GAP IS THE OPPORTUNITY                          |
|    $375M generation : <$70M attribution = 5:1 imbalance        |
|                                                                |
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
      text: "WHERE THE MONEY WENT"
    - type: label_editorial
      text: "$500M+ Music AI Funding by Category"

panel_generation:
  position: [60, 140]
  width: 880
  height: 720
  label: "I. GENERATION"
  total: "$375M+"
  bars:
    - { name: "Suno", amount: "$375M+", height_pct: 95 }
    - { name: "Udio", amount: "$33M", height_pct: 8 }

panel_attribution:
  position: [960, 140]
  width: 880
  height: 720
  label: "II. ATTRIBUTION"
  total: "<$70M"
  bars:
    - { name: "ProRata", amount: "$40M", height_pct: 10 }
    - { name: "Vermillio", amount: "$16M", height_pct: 4 }
    - { name: "Musical AI", amount: "$6M", height_pct: 1.5 }
    - { name: "Sureel", amount: "undisclosed", height_pct: 2 }

callout_bottom:
  position: [60, 880]
  width: 1800
  height: 120
  elements:
    - type: callout_bar
      text: "THE FUNDING GAP IS THE OPPORTUNITY"
    - type: data_mono
      text: "$375M generation : <$70M attribution = 5:1 imbalance"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "WHERE THE MONEY WENT" with coral accent square |
| Subtitle | `label_editorial` | "$500M+ Music AI Funding by Category" |
| Generation panel | `problem_statement` | Left panel: large bars showing generation funding dominance |
| Attribution panel | `solution_component` | Right panel: small bars showing attribution funding scarcity |
| Suno bar | `data_mono` | Tallest bar: $375M+ label |
| Udio bar | `data_mono` | Shorter bar: $33M label |
| ProRata bar | `data_mono` | Attribution side: $40M label |
| Vermillio bar | `data_mono` | Attribution side: $16M label |
| Musical AI bar | `data_mono` | Attribution side: $6M label |
| Sureel bar | `data_mono` | Attribution side: undisclosed label |
| Panel divider | `callout_bar` | Coral vertical accent line between panels |
| Bottom callout | `callout_bar` | "THE FUNDING GAP IS THE OPPORTUNITY" |
| Ratio display | `data_mono` | "5:1 imbalance" calculation |
| Roman numerals | `section_numeral` | I and II panel headers |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Generation panel | Attribution panel | contrast | "5:1 funding ratio" |
| Funding gap | Bottom callout | implication | "Risk and opportunity" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Funding Gap Callout | "The funding gap IS the opportunity" | Bottom full-width bar |
| Ratio | "$375M generation : <$70M attribution = 5:1 imbalance" | Within bottom callout |

## Text Content

### Labels (Max 30 chars each)

- WHERE THE MONEY WENT
- GENERATION
- ATTRIBUTION
- Suno $375M+
- Udio $33M
- ProRata $40M
- Vermillio $16M
- Musical AI $6M
- Sureel (undisclosed)
- THE FUNDING GAP IS THE OPP.
- 5:1 imbalance

### Caption (for embedding in documentation)

Music AI funding split: over $375M went to generation platforms (Suno alone raised $375M+), while attribution infrastructure received less than $70M combined (ProRata $40M, Vermillio $16M, Musical AI $6M, Sureel undisclosed) -- a 5:1 structural imbalance that defines both the risk landscape and the market opportunity.

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

1. Dollar amounts are approximate and publicly reported -- do NOT claim exact precision.
2. Suno's $375M+ is cumulative across multiple rounds -- do NOT break down by round.
3. Sureel's amount is "undisclosed" -- do NOT invent a number.
4. The 5:1 ratio is approximate -- do NOT claim mathematical exactness.
5. This is about FUNDING CATEGORIES, not company valuations -- do NOT conflate the two.
6. Do NOT imply that more funding equals better outcomes.
7. The visual asymmetry between panels IS intentional -- the generation panel should visually dominate to convey the imbalance.
8. Bar heights should be roughly proportional to dollar amounts within each panel.

## Alt Text

Split-panel funding comparison: $375M+ to music generation vs less than $70M to attribution, showing 5:1 gap.

## JSON Export Block

```json
{
  "id": "fig-landscape-02",
  "title": "Where the Money Went: $500M+ by Category",
  "audience": "L1",
  "priority": "P0",
  "layout": "D",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Explain",
  "funding_data": {
    "generation": {
      "total": "$375M+",
      "companies": [
        { "name": "Suno", "amount": "$375M+" },
        { "name": "Udio", "amount": "$33M" }
      ]
    },
    "attribution": {
      "total": "<$70M",
      "companies": [
        { "name": "ProRata", "amount": "$40M" },
        { "name": "Vermillio", "amount": "$16M" },
        { "name": "Musical AI", "amount": "$6M" },
        { "name": "Sureel", "amount": "undisclosed" }
      ]
    },
    "ratio": "5:1"
  },
  "semantic_tags_used": [
    "heading_display", "label_editorial", "problem_statement", "solution_component",
    "data_mono", "callout_bar", "section_numeral"
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
