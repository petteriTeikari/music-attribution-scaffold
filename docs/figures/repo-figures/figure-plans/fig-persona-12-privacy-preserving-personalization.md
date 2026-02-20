# fig-persona-12: Privacy-Preserving Personalization

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-12 |
| **Title** | Privacy-Preserving Personalization: Three Tiers of Data Minimization |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/knowledge-base/, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Demonstrates that privacy and personalization effectiveness are not inversely proportional. Three data minimization tiers show that restricting personal data to categories-only still achieves 97.2% of full-history effectiveness. Answers: "How much personalization quality do we actually lose by maximizing privacy?"

## Key Message

97.2% personalization effectiveness is achievable at the most restrictive data tier -- privacy and personalization are not opposites.

## Visual Concept

Three descending tiers arranged top-to-bottom, each progressively more private. Each tier shows: data type collected, privacy level indicator, and effectiveness percentage. The visual weight shifts from dense data representation at top to minimal at bottom, while effectiveness bars remain nearly equal height. A dramatic callout emphasizes the negligible effectiveness gap.

```
+-----------------------------------------------------------------------+
|  PRIVACY-PRESERVING PERSONALIZATION                                    |
|  -- Three Tiers of Data Minimization                                   |
+-----------------------------------------------------------------------+
|                                                                        |
|  TIER 1 -- FULL HISTORY                                               |
|  ═══════════════════════════════════════════════════════               |
|  ┌─────────────────────────────────────────────────────┐              |
|  │  Data: Complete interaction logs, timestamps,        │              |
|  │        click sequences, dwell times, full queries    │  ████████  |
|  │  Privacy: Minimal                                    │  100%      |
|  │  Effectiveness: 100% (baseline)                      │            |
|  └─────────────────────────────────────────────────────┘              |
|                         │                                              |
|                         ▼  Privacy increases                           |
|                                                                        |
|  TIER 2 -- KEYWORDS + SENTIMENT                                       |
|  ═══════════════════════════════════════════════════════               |
|  ┌─────────────────────────────────────────────────────┐              |
|  │  Data: Extracted keywords, sentiment scores,         │              |
|  │        interaction summaries (no raw logs)           │  ████████  |
|  │  Privacy: Moderate                                   │  ~99%      |
|  │  Effectiveness: ~99% of baseline                     │            |
|  └─────────────────────────────────────────────────────┘              |
|                         │                                              |
|                         ▼  Privacy increases                           |
|                                                                        |
|  TIER 3 -- CATEGORIES ONLY                                            |
|  ═══════════════════════════════════════════════════════               |
|  ┌─────────────────────────────────────────────────────┐              |
|  │  Data: Genre preferences, role category,             │              |
|  │        interaction frequency bucket                  │  ███████▌  |
|  │  Privacy: Maximum                                    │  97.2%     |
|  │  Effectiveness: 97.2% of baseline                    │            |
|  └─────────────────────────────────────────────────────┘              |
|                                                                        |
|  -- 97.2% EFFECTIVENESS AT MOST RESTRICTIVE TIER                      |
|     PRIVACY AND PERSONALIZATION ARE NOT OPPOSITES                      |
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
    content: "PRIVACY-PRESERVING PERSONALIZATION"
    role: title

  - id: tier_1_zone
    bounds: [80, 140, 1760, 220]
    content: "TIER 1 -- FULL HISTORY"
    role: content_area

  - id: tier_2_zone
    bounds: [80, 400, 1760, 220]
    content: "TIER 2 -- KEYWORDS + SENTIMENT"
    role: content_area

  - id: tier_3_zone
    bounds: [80, 660, 1760, 220]
    content: "TIER 3 -- CATEGORIES ONLY"
    role: content_area

  - id: callout_zone
    bounds: [80, 920, 1760, 120]
    content: "97.2% EFFECTIVENESS AT MOST RESTRICTIVE TIER"
    role: callout_box

anchors:
  - id: tier_1_data
    position: [120, 180]
    size: [1200, 140]
    role: processing_stage
    label: "Full interaction history"

  - id: tier_1_bar
    position: [1400, 180]
    size: [360, 60]
    role: confidence_high
    label: "100%"

  - id: tier_2_data
    position: [120, 440]
    size: [1200, 140]
    role: processing_stage
    label: "Keywords and sentiment"

  - id: tier_2_bar
    position: [1400, 440]
    size: [356, 60]
    role: confidence_high
    label: "~99%"

  - id: tier_3_data
    position: [120, 700]
    size: [1200, 140]
    role: processing_stage
    label: "Categories only"

  - id: tier_3_bar
    position: [1400, 700]
    size: [350, 60]
    role: confidence_high
    label: "97.2%"

  - id: privacy_arrow
    from: tier_1_zone
    to: tier_3_zone
    type: arrow
    label: "Privacy increases"

  - id: effectiveness_annotation
    position: [1400, 860]
    size: [360, 40]
    role: data_mono
    label: "Effectiveness %"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Tier 1 block | `processing_stage` | Full history -- complete interaction logs, timestamps, click sequences, dwell times |
| Tier 2 block | `processing_stage` | Keywords + sentiment -- extracted keywords, sentiment scores, interaction summaries |
| Tier 3 block | `processing_stage` | Categories only -- genre preferences, role category, interaction frequency bucket |
| Effectiveness bars | `confidence_high` | Near-equal horizontal bars showing 100%, ~99%, 97.2% |
| Privacy gradient | `data_flow` | Downward arrow indicating increasing privacy protection |
| Callout bar | `callout_box` | Key insight about 97.2% effectiveness at maximum privacy |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Tier 1 | Tier 2 | arrow | "privacy increases" |
| Tier 2 | Tier 3 | arrow | "privacy increases" |
| Tier 1 bar | Tier 3 bar | dashed | "only 2.8% gap" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "THE PRIVACY GAP" | "97.2% EFFECTIVENESS AT MOST RESTRICTIVE TIER -- PRIVACY AND PERSONALIZATION ARE NOT OPPOSITES" | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "TIER 1 -- FULL HISTORY"
- Label 2: "TIER 2 -- KEYWORDS + SENTIMENT"
- Label 3: "TIER 3 -- CATEGORIES ONLY"
- Label 4: "100% effectiveness"
- Label 5: "~99% effectiveness"
- Label 6: "97.2% effectiveness"
- Label 7: "Privacy increases"
- Label 8: "Only 2.8% gap"

### Caption (for embedding in documentation)

Three privacy tiers for personalization data minimization, demonstrating that restricting data to categories-only (Tier 3) retains 97.2% of full-history effectiveness -- evidence that privacy and personalization are not fundamentally opposed.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `confidence_high`, `callout_box` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The 97.2% figure is from research on privacy-preserving personalization. Do NOT claim it as proprietary project data.
10. Tier effectiveness percentages: 100% (baseline), ~99% (keywords+sentiment), 97.2% (categories only). Do NOT alter these values.
11. The effectiveness bars must be visually near-identical in length to emphasize the small gap. Do NOT exaggerate the difference.
12. Privacy tiers are ordered from least private (top) to most private (bottom). Do NOT reverse the order.
13. Do NOT imply that Tier 3 is always sufficient -- the point is that the trade-off is smaller than expected.

## Alt Text

Tiered diagram of privacy-preserving personalization showing three data minimization levels -- full history, keywords, and categories-only -- achieving 97.2% effectiveness at maximum privacy, proving hyperpersonalization and data protection are not opposites.

## Image Embed

![Tiered diagram of privacy-preserving personalization showing three data minimization levels -- full history, keywords, and categories-only -- achieving 97.2% effectiveness at maximum privacy, proving hyperpersonalization and data protection are not opposites.](docs/figures/repo-figures/assets/fig-persona-12-privacy-preserving-personalization.jpg)

*Three privacy tiers for personalization data minimization, demonstrating that restricting data to categories-only (Tier 3) retains 97.2% of full-history effectiveness -- evidence that privacy and personalization are not fundamentally opposed.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-12",
    "title": "Privacy-Preserving Personalization: Three Tiers of Data Minimization",
    "audience": "L2",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "97.2% personalization effectiveness at the most restrictive privacy tier proves privacy and personalization are not opposites.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Tier 1 Full History",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["TIER 1 -- FULL HISTORY", "100% effectiveness", "Minimal privacy"]
      },
      {
        "name": "Tier 2 Keywords + Sentiment",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["TIER 2 -- KEYWORDS + SENTIMENT", "~99% effectiveness", "Moderate privacy"]
      },
      {
        "name": "Tier 3 Categories Only",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["TIER 3 -- CATEGORIES ONLY", "97.2% effectiveness", "Maximum privacy"]
      }
    ],
    "relationships": [
      {
        "from": "Tier 1",
        "to": "Tier 2",
        "type": "arrow",
        "label": "privacy increases, effectiveness barely decreases"
      },
      {
        "from": "Tier 2",
        "to": "Tier 3",
        "type": "arrow",
        "label": "privacy maximized, only 2.8% effectiveness gap"
      }
    ],
    "callout_boxes": [
      {
        "heading": "THE PRIVACY GAP",
        "body_text": "97.2% EFFECTIVENESS AT MOST RESTRICTIVE TIER -- PRIVACY AND PERSONALIZATION ARE NOT OPPOSITES",
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
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
