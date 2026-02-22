# fig-persona-27: Power User Economics

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-27 |
| **Title** | Power User Economics -- Three Pricing Scenarios |
| **Audience** | L1 (Music Industry Professional) |
| **Location** | docs/planning/persona-coherence.md, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Shows three pricing model scenarios side by side with their monthly P&L impact, demonstrating why credit-based pricing with overage billing is the only sustainable model for AI persona agents. Answers: "Why do unlimited and freemium models fail, and how much does the power user problem actually cost?"

## Key Message

Credit-based pricing with overage billing is the only sustainable model -- Scenario A (Unlimited Free) loses $7,500/mo, Scenario B (Freemium) loses $4,852/mo, while Scenario C (Credit-Based) generates +$9,025/mo profit, because 5-10% of power users consume 60-80% of resources.

## Visual Concept

Three side-by-side panels, each showing a pricing scenario with a large P&L number at top (red for losses, green for profit). Below each P&L number, key assumptions are listed. A distribution bar at the bottom shows the 5-10% power user concentration consuming 60-80% of resources. The Character.AI case study ($365M serving vs $32M revenue) is annotated as a real-world cautionary example.

```
+---------------------------------------------------------------+
|  POWER USER ECONOMICS                                          |
+---------------------------------------------------------------+
|                                                                |
|  SCENARIO A            SCENARIO B           SCENARIO C          |
|  UNLIMITED FREE        FREEMIUM             CREDIT-BASED       |
|                                                                |
|  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐     |
|  │              │    │              │    │              │     |
|  │  -$7,500/mo  │    │  -$4,852/mo  │    │  +$9,025/mo  │     |
|  │              │    │              │    │      ★       │     |
|  │  ■ No revenue │    │  ■ 2% convert │    │  ■ Credits   │     |
|  │    gate       │    │  ■ Free tier  │    │    purchased │     |
|  │  ■ Power users│    │    subsidizes │    │  ■ Overage   │     |
|  │    uncapped   │    │    power users│    │    billing    │     |
|  │  ■ Costs grow │    │  ■ Churn at   │    │  ■ Power     │     |
|  │    linearly   │    │    paywall    │    │    users pay │     |
|  │              │    │              │    │    their way  │     |
|  └──────────────┘    └──────────────┘    └──────────────┘     |
|                                                                |
|  POWER USER DISTRIBUTION:                                      |
|  ┌──┐┌──────────────────────────────────────────────────┐     |
|  │5%││             60-80% of resources                   │     |
|  └──┘└──────────────────────────────────────────────────┘     |
|                                                                |
|  Character.AI: $365M serving vs $32M revenue                   |
|                                                                |
+---------------------------------------------------------------+
|  CREDIT-BASED WITH OVERAGE BILLING IS THE ONLY SUSTAINABLE     |
|  MODEL                                                         |
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
    content: "POWER USER ECONOMICS"
    role: title

  - id: scenarios_zone
    bounds: [80, 160, 1760, 500]
    role: content_area

  - id: distribution_zone
    bounds: [80, 700, 1760, 120]
    role: content_area

  - id: case_study_zone
    bounds: [80, 840, 1760, 60]
    role: content_area

  - id: callout_zone
    bounds: [80, 920, 1760, 120]
    role: callout_box

anchors:
  - id: scenario_a
    position: [340, 420]
    size: [480, 420]
    role: confidence_low
    label: "SCENARIO A: UNLIMITED FREE"

  - id: scenario_a_pnl
    position: [340, 260]
    size: [300, 80]
    role: confidence_low
    label: "-$7,500/mo"

  - id: scenario_b
    position: [960, 420]
    size: [480, 420]
    role: confidence_medium
    label: "SCENARIO B: FREEMIUM"

  - id: scenario_b_pnl
    position: [960, 260]
    size: [300, 80]
    role: confidence_medium
    label: "-$4,852/mo"

  - id: scenario_c
    position: [1580, 420]
    size: [480, 420]
    role: confidence_high
    label: "SCENARIO C: CREDIT-BASED"

  - id: scenario_c_pnl
    position: [1580, 260]
    size: [300, 80]
    role: confidence_high
    label: "+$9,025/mo"

  - id: power_user_bar
    position: [960, 740]
    size: [1600, 60]
    role: problem_statement
    label: "5-10% consume 60-80%"

  - id: case_study
    position: [960, 860]
    size: [800, 40]
    role: problem_statement
    label: "Character.AI: $365M vs $32M"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "POWER USER ECONOMICS" with accent square |
| Scenario A panel | `confidence_low` | Unlimited Free: -$7,500/mo loss, no revenue gate |
| Scenario B panel | `confidence_medium` | Freemium: -$4,852/mo loss, 2% conversion, free tier subsidizes |
| Scenario C panel | `confidence_high` | Credit-Based: +$9,025/mo profit, overage billing, sustainable |
| P&L numbers | `data_mono` | Large financial figures at top of each panel |
| Power user distribution | `problem_statement` | Bar showing 5-10% of users consuming 60-80% of resources |
| Character.AI case study | `problem_statement` | Real-world example: $365M serving costs vs $32M revenue |
| Callout bar | `callout_bar` | Credit-based with overage billing is the only sustainable model |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Scenario A | Scenario B | arrow | "reduce losses" |
| Scenario B | Scenario C | arrow | "reach profitability" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ONLY SUSTAINABLE MODEL" | Credit-based with overage billing -- power users pay proportionally to their consumption | bottom-center |
| "CAUTIONARY TALE" | Character.AI: $365M annual serving costs vs $32M revenue -- 11:1 cost-to-revenue ratio | bottom-left |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "SCENARIO A: UNLIMITED FREE"
- Label 2: "SCENARIO B: FREEMIUM"
- Label 3: "SCENARIO C: CREDIT-BASED"
- Label 4: "-$7,500/mo"
- Label 5: "-$4,852/mo"
- Label 6: "+$9,025/mo"
- Label 7: "No revenue gate"
- Label 8: "2% conversion rate"
- Label 9: "Overage billing"
- Label 10: "5-10% consume 60-80%"
- Label 11: "Character.AI: $365M vs $32M"

### Caption (for embedding in documentation)

Three pricing scenarios compared: Unlimited Free (-$7,500/mo), Freemium (-$4,852/mo), and Credit-Based (+$9,025/mo) -- demonstrating that credit-based pricing with overage billing is the only sustainable model when 5-10% of power users consume 60-80% of resources.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `confidence_high`, `confidence_low`, `problem_statement` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear. This is L1 -- use business/financial language.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The three P&L numbers MUST be exact: -$7,500/mo, -$4,852/mo, +$9,025/mo.
10. The power user concentration is 5-10% consuming 60-80% -- do NOT change these ranges.
11. Character.AI case study: $365M serving costs vs $32M revenue -- these are real figures, do NOT alter.
12. Scenario C MUST be visually distinct as the recommended/profitable option.
13. Scenarios A and B MUST show losses clearly (red/negative treatment).
14. The distribution bar MUST make the 5-10% / 60-80% disproportion visually obvious.
15. Do NOT imply these are exact projections for this project -- they are illustrative scenarios.
16. "Overage billing" means users pay per-credit beyond their tier allocation -- do NOT conflate with usage-based pricing without tiers.

## Alt Text

Power user economics comparison of three AI agent pricing models showing Unlimited Free losing $7,500 per month, Freemium losing $4,852 per month, and Credit-Based earning $9,025 per month profit, with 5-10 percent of power users consuming 60-80 percent of resources in music attribution platforms

## Image Embed

![Power user economics comparison of three AI agent pricing models showing Unlimited Free losing $7,500 per month, Freemium losing $4,852 per month, and Credit-Based earning $9,025 per month profit, with 5-10 percent of power users consuming 60-80 percent of resources in music attribution platforms](docs/figures/repo-figures/assets/fig-persona-27-power-user-economics.jpg)

*Three pricing scenarios compared: Unlimited Free (-$7,500/mo), Freemium (-$4,852/mo), and Credit-Based (+$9,025/mo) -- demonstrating that credit-based pricing with overage billing is the only sustainable model when 5-10% of power users consume 60-80% of resources.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-27",
    "title": "Power User Economics",
    "audience": "L1",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Credit-based pricing with overage billing is the only sustainable model -- power users (5-10%) consume 60-80% of resources.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Scenario A: Unlimited Free",
        "role": "confidence_low",
        "is_highlighted": false,
        "labels": ["UNLIMITED FREE", "-$7,500/mo"]
      },
      {
        "name": "Scenario B: Freemium",
        "role": "confidence_medium",
        "is_highlighted": false,
        "labels": ["FREEMIUM", "-$4,852/mo"]
      },
      {
        "name": "Scenario C: Credit-Based",
        "role": "confidence_high",
        "is_highlighted": true,
        "labels": ["CREDIT-BASED", "+$9,025/mo"]
      },
      {
        "name": "Power User Distribution",
        "role": "problem_statement",
        "is_highlighted": true,
        "labels": ["5-10% consume 60-80%"]
      }
    ],
    "relationships": [
      {
        "from": "Scenario A",
        "to": "Scenario B",
        "type": "arrow",
        "label": "reduce losses"
      },
      {
        "from": "Scenario B",
        "to": "Scenario C",
        "type": "arrow",
        "label": "reach profitability"
      }
    ],
    "callout_boxes": [
      {
        "heading": "ONLY SUSTAINABLE MODEL",
        "body_text": "Credit-based with overage billing -- power users pay proportionally",
        "position": "bottom-center"
      },
      {
        "heading": "CAUTIONARY TALE",
        "body_text": "Character.AI: $365M serving vs $32M revenue",
        "position": "bottom-left"
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
- [x] Audience level correct (L1)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
