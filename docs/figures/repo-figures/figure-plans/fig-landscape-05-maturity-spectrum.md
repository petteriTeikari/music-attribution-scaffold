# fig-landscape-05: Market Maturity Spectrum: TRL x Adoption x Regulation

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-05 |
| **Title** | Market Maturity Spectrum: TRL x Adoption x Regulation |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

This figure visualizes the maturity mismatch across attribution approaches by plotting them against three axes: Technology Readiness Level, market adoption, and regulatory demand. It answers: "Which attribution approaches are technically ready, which have market traction, and where is regulation pushing hardest?"

## Key Message

Audio fingerprinting is technically mature but legally contested; TDA is technically nascent but regulatory demand is surging -- a maturity mismatch that defines the market.

## Visual Concept

Three horizontal spectra stacked vertically, each representing one axis (TRL, adoption, regulation). Attribution approaches are positioned as markers on each spectrum, with connecting lines showing how the same approach appears at different positions across axes. The visual tension comes from approaches that are high on one axis but low on another -- especially the fingerprinting vs TDA contrast.

```
+---------------------------------------------------------------+
|  MARKET MATURITY SPECTRUM                                      |
|  ■ TRL x Adoption x Regulation                                |
+---------------------------------------------------------------+
|                                                                |
|  TECHNOLOGY READINESS (TRL 1-9)                                |
|  ──────────────────────                                        |
|  Low                                              High         |
|  ├──────┼──────┼──────┼──────┼──────┼──────┼──────┤           |
|  1      2      3      4      5      6      7    8-9           |
|     ◆Unlrn  ◆InfFn   ◆Embed        ◆Wmrk  ◆FP  ◆CntID      |
|                                                                |
|  MARKET ADOPTION                                               |
|  ────────────────                                              |
|  Early                                            Mature       |
|  ├──────────────┼──────────────┼──────────────────┤           |
|  Early          Growing        Mature                          |
|  ◆Unlrn ◆InfFn  ◆Embed ◆Wmrk         ◆FP ◆CntID            |
|                                                                |
|  REGULATORY DEMAND                                             |
|  ─────────────────                                             |
|  Low                                              High         |
|  ├──────────────┼──────────────┼──────────────────┤           |
|  Low            Medium         High                            |
|         ◆CntID  ◆FP   ◆Wmrk   ◆Embed ◆InfFn ◆Unlrn         |
|                                                                |
+---------------------------------------------------------------+
|  ■ THE MATURITY MISMATCH                                       |
|                                                                |
|  Fingerprinting:  TRL 8 ■  Adoption: mature ■  Legal: HIGH    |
|  TDA/Unlearning:  TRL 2 ■  Adoption: early  ■  Demand: HIGH   |
|                                                                |
|  ■ Technically ready ≠ legally settled                         |
|  ■ Legally demanded ≠ technically possible                     |
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
      text: "MARKET MATURITY SPECTRUM"
    - type: label_editorial
      text: "TRL x Adoption x Regulation"

axis_trl:
  position: [60, 160]
  width: 1800
  height: 200
  label: "TECHNOLOGY READINESS (TRL 1-9)"
  range: [1, 9]
  markers:
    - { label: "Unlearning TDA", position: 2 }
    - { label: "Influence Functions", position: 3 }
    - { label: "Embedding Similarity", position: 4 }
    - { label: "Watermarking", position: 6 }
    - { label: "Fingerprinting", position: 8 }
    - { label: "Content ID", position: 9 }

axis_adoption:
  position: [60, 380]
  width: 1800
  height: 200
  label: "MARKET ADOPTION"
  range: ["Early", "Growing", "Mature"]
  markers:
    - { label: "Unlearning TDA", position: "Early" }
    - { label: "Influence Functions", position: "Early" }
    - { label: "Embedding Similarity", position: "Growing" }
    - { label: "Watermarking", position: "Growing" }
    - { label: "Fingerprinting", position: "Mature" }
    - { label: "Content ID", position: "Mature" }

axis_regulation:
  position: [60, 600]
  width: 1800
  height: 200
  label: "REGULATORY DEMAND"
  range: ["Low", "Medium", "High"]
  markers:
    - { label: "Content ID", position: "Low-Medium" }
    - { label: "Fingerprinting", position: "Medium" }
    - { label: "Watermarking", position: "Medium" }
    - { label: "Embedding Similarity", position: "Medium-High" }
    - { label: "Influence Functions", position: "High" }
    - { label: "Unlearning TDA", position: "High" }

mismatch_callout:
  position: [60, 840]
  width: 1800
  height: 180
  elements:
    - type: callout_bar
      text: "THE MATURITY MISMATCH"
    - type: data_mono
      text: "Fingerprinting: TRL 8, Adoption mature, Legal HIGH"
    - type: data_mono
      text: "TDA/Unlearning: TRL 2, Adoption early, Demand HIGH"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "MARKET MATURITY SPECTRUM" with coral accent square |
| Subtitle | `label_editorial` | "TRL x Adoption x Regulation" |
| TRL axis | `processing_stage` | Horizontal spectrum from TRL 1 to TRL 9 with approach markers |
| Adoption axis | `processing_stage` | Horizontal spectrum from Early to Mature with approach markers |
| Regulation axis | `processing_stage` | Horizontal spectrum from Low to High with approach markers |
| Approach markers | `badge_label` | Diamond markers positioned on each axis for each approach |
| Axis labels | `label_editorial` | "TECHNOLOGY READINESS", "MARKET ADOPTION", "REGULATORY DEMAND" |
| Mismatch callout | `callout_bar` | Bottom panel highlighting the fingerprinting vs TDA contrast |
| Insight statements | `label_editorial` | "Technically ready does not equal legally settled" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Fingerprinting TRL marker | Fingerprinting regulation marker | contrast | "High TRL, legally contested" |
| TDA TRL marker | TDA regulation marker | contrast | "Low TRL, high regulatory demand" |
| TRL axis | Adoption axis | cross-reference | "Same approaches, different positions" |
| Adoption axis | Regulation axis | cross-reference | "Adoption does not track regulation" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Maturity Mismatch | Fingerprinting vs TDA contrast with data | Bottom section |
| Insight 1 | "Technically ready does not equal legally settled" | Bottom-left |
| Insight 2 | "Legally demanded does not equal technically possible" | Bottom-right |

## Text Content

### Labels (Max 30 chars each)

- MARKET MATURITY SPECTRUM
- TRL x Adoption x Regulation
- TECHNOLOGY READINESS (TRL)
- MARKET ADOPTION
- REGULATORY DEMAND
- Unlearning TDA
- Influence Functions
- Embedding Similarity
- Watermarking
- Fingerprinting
- Content ID
- THE MATURITY MISMATCH
- Early
- Growing
- Mature

### Caption (for embedding in documentation)

Six attribution approaches plotted across three axes -- Technology Readiness Level, market adoption, and regulatory demand -- revealing a critical maturity mismatch: audio fingerprinting scores high on TRL (8) and adoption (mature) but faces legal contestation, while training data attribution is technically nascent (TRL 2) but faces surging regulatory demand from the EU AI Act and similar frameworks.

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

1. TRL values are APPROXIMATE positions for conceptual illustration -- do NOT claim precise TRL assessments.
2. There are exactly 6 approaches shown: Unlearning TDA, Influence Functions, Embedding Similarity, Watermarking, Fingerprinting, Content ID.
3. "Regulatory demand" refers to regulatory pressure for this type of approach, not existing regulation.
4. Do NOT name specific regulations (EU AI Act, DMCA) on the figure itself -- keep it general.
5. Fingerprinting is "legally contested" meaning its application to AI training data is disputed -- NOT that fingerprinting technology itself is illegal.
6. TDA stands for Training Data Attribution -- do NOT expand it differently.
7. The three axes are INDEPENDENT -- do NOT imply they correlate.
8. Marker positions are relative within each axis -- do NOT show exact numerical values for adoption or regulation.

## Alt Text

Six attribution approaches on three axes: TRL, adoption, regulation -- showing fingerprinting-TDA maturity mismatch.

## JSON Export Block

```json
{
  "id": "fig-landscape-05",
  "title": "Market Maturity Spectrum: TRL x Adoption x Regulation",
  "audience": "L2",
  "priority": "P1",
  "layout": "B",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Explain",
  "approaches": [
    { "name": "Unlearning TDA", "trl": 2, "adoption": "early", "regulation": "high" },
    { "name": "Influence Functions", "trl": 3, "adoption": "early", "regulation": "high" },
    { "name": "Embedding Similarity", "trl": 4, "adoption": "growing", "regulation": "medium-high" },
    { "name": "Watermarking", "trl": 6, "adoption": "growing", "regulation": "medium" },
    { "name": "Fingerprinting", "trl": 8, "adoption": "mature", "regulation": "medium" },
    { "name": "Content ID", "trl": 9, "adoption": "mature", "regulation": "low-medium" }
  ],
  "key_contrast": {
    "mature_contested": "Fingerprinting",
    "nascent_demanded": "Unlearning TDA"
  },
  "semantic_tags_used": [
    "heading_display", "label_editorial", "processing_stage",
    "badge_label", "callout_bar", "data_mono"
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
