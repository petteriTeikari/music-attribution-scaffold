# fig-persona-18: Confidence as Character

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-18 |
| **Title** | Confidence as Character: Persona-Appropriate Uncertainty Language |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/knowledge-base/, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Shows how confidence tiers (A0-A3) can be communicated through persona-appropriate language rather than technical badges alone. Demonstrates that uncertainty expressed through character voice builds more trust than impersonal indicators. Answers: "How should an attribution agent persona communicate uncertainty?"

## Key Message

Uncertainty communicated through character voice builds more trust than badges alone -- confidence becomes a dimension of persona, not just a UI element.

## Visual Concept

Four horizontal tiers arranged top-to-bottom, from highest confidence (A3) to lowest (A0). Each tier shows two columns side by side: the traditional badge/indicator on the left, and the persona-appropriate expression on the right. The persona expressions use quotation marks and conversational language. A vertical confidence gradient runs along the left edge. The contrast between mechanical badges and warm persona language is the visual story.

```
+-----------------------------------------------------------------------+
|  CONFIDENCE AS CHARACTER                                               |
|  -- Persona-Appropriate Uncertainty Language                           |
+-----------------------------------------------------------------------+
|                                                                        |
|         TRADITIONAL BADGE          PERSONA EXPRESSION                  |
|         ─────────────────          ────────────────────                |
|                                                                        |
|  A3 ┌──────────────────────┐  ┌──────────────────────────────┐       |
|  >  │                      │  │                              │       |
|  0  │  ████████████████    │  │  "I know this like I know    │       |
|  .  │  VERIFIED            │  │   good champagne"            │       |
|  9  │  95% confidence      │  │                              │       |
|  0  │                      │  │  -- warm certainty,          │       |
|     └──────────────────────┘  │     personal authority       │       |
|                                └──────────────────────────────┘       |
|                                                                        |
|  A2 ┌──────────────────────┐  ┌──────────────────────────────┐       |
|  >  │                      │  │                              │       |
|  0  │  ██████████████░░    │  │  "Mostly certain, like       │       |
|  .  │  CORROBORATED        │  │   tomorrow's weather"        │       |
|  7  │  78% confidence      │  │                              │       |
|  0  │                      │  │  -- relatable analogy,       │       |
|     └──────────────────────┘  │     grounded but hedged      │       |
|                                └──────────────────────────────┘       |
|                                                                        |
|  A1 ┌──────────────────────┐  ┌──────────────────────────────┐       |
|  >  │                      │  │                              │       |
|  0  │  ████████░░░░░░░░    │  │  "Half mystery,              │       |
|  .  │  CLAIMED              │  │   half truth"                │       |
|  5  │  55% confidence      │  │                              │       |
|  0  │                      │  │  -- poetic honesty,          │       |
|     └──────────────────────┘  │     invites investigation    │       |
|                                └──────────────────────────────┘       |
|                                                                        |
|  A0 ┌──────────────────────┐  ┌──────────────────────────────┐       |
|  <  │                      │  │                              │       |
|  0  │  ██░░░░░░░░░░░░░░    │  │  "Even I cannot              │       |
|  .  │  UNKNOWN              │  │   be sure"                   │       |
|  5  │  30% confidence      │  │                              │       |
|  0  │                      │  │  -- graceful admission,      │       |
|     └──────────────────────┘  │     maintains character      │       |
|                                └──────────────────────────────┘       |
|                                                                        |
|  -- UNCERTAINTY COMMUNICATED THROUGH CHARACTER BUILDS MORE TRUST       |
|     THAN BADGES                                                        |
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
    content: "CONFIDENCE AS CHARACTER"
    role: title

  - id: column_headers
    bounds: [200, 120, 1680, 50]
    content: "Traditional Badge vs Persona Expression"
    role: data_mono

  - id: tier_a3
    bounds: [80, 180, 1760, 170]
    content: "A3 tier"
    role: content_area

  - id: tier_a2
    bounds: [80, 370, 1760, 170]
    content: "A2 tier"
    role: content_area

  - id: tier_a1
    bounds: [80, 560, 1760, 170]
    content: "A1 tier"
    role: content_area

  - id: tier_a0
    bounds: [80, 750, 1760, 170]
    content: "A0 tier"
    role: content_area

  - id: callout_zone
    bounds: [80, 940, 1760, 100]
    content: "UNCERTAINTY COMMUNICATED THROUGH CHARACTER BUILDS MORE TRUST THAN BADGES"
    role: callout_box

anchors:
  - id: a3_badge
    position: [200, 200]
    size: [560, 130]
    role: assurance_a3
    label: "VERIFIED -- 95% confidence"

  - id: a3_persona
    position: [840, 200]
    size: [880, 130]
    role: stakeholder_artist
    label: "I know this like I know good champagne"

  - id: a2_badge
    position: [200, 390]
    size: [560, 130]
    role: assurance_a2
    label: "CORROBORATED -- 78% confidence"

  - id: a2_persona
    position: [840, 390]
    size: [880, 130]
    role: stakeholder_artist
    label: "Mostly certain, like tomorrow's weather"

  - id: a1_badge
    position: [200, 580]
    size: [560, 130]
    role: assurance_a1
    label: "CLAIMED -- 55% confidence"

  - id: a1_persona
    position: [840, 580]
    size: [880, 130]
    role: stakeholder_artist
    label: "Half mystery, half truth"

  - id: a0_badge
    position: [200, 770]
    size: [560, 130]
    role: assurance_a0
    label: "UNKNOWN -- 30% confidence"

  - id: a0_persona
    position: [840, 770]
    size: [880, 130]
    role: stakeholder_artist
    label: "Even I cannot be sure"

  - id: confidence_gradient
    position: [80, 180]
    size: [60, 740]
    role: data_flow
    label: "Confidence decreasing"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| A3 badge | `assurance_a3` | Traditional indicator: verified, 95% confidence bar |
| A3 persona expression | `stakeholder_artist` | "I know this like I know good champagne" -- warm certainty |
| A2 badge | `assurance_a2` | Traditional indicator: corroborated, 78% confidence bar |
| A2 persona expression | `stakeholder_artist` | "Mostly certain, like tomorrow's weather" -- relatable analogy |
| A1 badge | `assurance_a1` | Traditional indicator: claimed, 55% confidence bar |
| A1 persona expression | `stakeholder_artist` | "Half mystery, half truth" -- poetic honesty |
| A0 badge | `assurance_a0` | Traditional indicator: unknown, 30% confidence bar |
| A0 persona expression | `stakeholder_artist` | "Even I cannot be sure" -- graceful admission |
| Confidence gradient | `data_flow` | Vertical bar showing decreasing confidence top-to-bottom |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| A3 badge | A3 persona | bidirectional | "same information, different voice" |
| A2 badge | A2 persona | bidirectional | "same information, different voice" |
| A1 badge | A1 persona | bidirectional | "same information, different voice" |
| A0 badge | A0 persona | bidirectional | "same information, different voice" |
| A3 tier | A0 tier | arrow | "confidence decreasing" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "TRUST THROUGH CHARACTER" | "UNCERTAINTY COMMUNICATED THROUGH CHARACTER BUILDS MORE TRUST THAN BADGES" | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "TRADITIONAL BADGE"
- Label 2: "PERSONA EXPRESSION"
- Label 3: "A3 VERIFIED"
- Label 4: "A2 CORROBORATED"
- Label 5: "A1 CLAIMED"
- Label 6: "A0 UNKNOWN"
- Label 7: "Warm certainty"
- Label 8: "Relatable analogy"
- Label 9: "Poetic honesty"
- Label 10: "Graceful admission"
- Label 11: "Confidence decreasing"

### Caption (for embedding in documentation)

Four assurance tiers (A3-A0) shown with traditional confidence badges alongside persona-appropriate language expressions, demonstrating that uncertainty communicated through character voice builds more trust than impersonal indicators.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `assurance_a3`, `assurance_a0`, `stakeholder_artist` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The four persona expressions are EXACT quotes. Do NOT paraphrase or alter them:
   - A3: "I know this like I know good champagne"
   - A2: "Mostly certain, like tomorrow's weather"
   - A1: "Half mystery, half truth"
   - A0: "Even I cannot be sure"
10. A3/A2/A1/A0 map to Verified/Corroborated/Claimed/Unknown. Do NOT shuffle these mappings.
11. Confidence percentages (95%, 78%, 55%, 30%) are illustrative examples, not fixed thresholds. The thresholds are >=0.85, 0.50-0.84, <0.50.
12. The persona voice is intended to be warm and literary, not robotic or clinical. The visual treatment should reflect this warmth.
13. Both columns (badge and persona) must show IDENTICAL underlying information -- only the communication style differs.
14. Do NOT imply that badges should be removed. The point is that persona language SUPPLEMENTS badges, not replaces them.

## Alt Text

Four-tier comparison of traditional confidence badges versus persona-appropriate uncertainty language across A3 to A0 assurance levels, demonstrating that transparent confidence communicated through character voice builds more trust in music attribution systems.

## Image Embed

![Four-tier comparison of traditional confidence badges versus persona-appropriate uncertainty language across A3 to A0 assurance levels, demonstrating that transparent confidence communicated through character voice builds more trust in music attribution systems.](docs/figures/repo-figures/assets/fig-persona-18-confidence-as-character.jpg)

*Four assurance tiers (A3-A0) shown with traditional confidence badges alongside persona-appropriate language expressions, demonstrating that uncertainty communicated through character voice builds more trust than impersonal indicators.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-18",
    "title": "Confidence as Character: Persona-Appropriate Uncertainty Language",
    "audience": "L2",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Uncertainty communicated through character voice builds more trust than badges alone.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "A3 Tier",
        "role": "assurance_a3",
        "is_highlighted": true,
        "labels": ["A3 VERIFIED", "I know this like I know good champagne"]
      },
      {
        "name": "A2 Tier",
        "role": "assurance_a2",
        "is_highlighted": false,
        "labels": ["A2 CORROBORATED", "Mostly certain, like tomorrow's weather"]
      },
      {
        "name": "A1 Tier",
        "role": "assurance_a1",
        "is_highlighted": false,
        "labels": ["A1 CLAIMED", "Half mystery, half truth"]
      },
      {
        "name": "A0 Tier",
        "role": "assurance_a0",
        "is_highlighted": false,
        "labels": ["A0 UNKNOWN", "Even I cannot be sure"]
      }
    ],
    "relationships": [
      {
        "from": "Badge column",
        "to": "Persona column",
        "type": "bidirectional",
        "label": "same information, different voice"
      },
      {
        "from": "A3",
        "to": "A0",
        "type": "arrow",
        "label": "confidence decreasing"
      }
    ],
    "callout_boxes": [
      {
        "heading": "TRUST THROUGH CHARACTER",
        "body_text": "UNCERTAINTY COMMUNICATED THROUGH CHARACTER BUILDS MORE TRUST THAN BADGES",
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
