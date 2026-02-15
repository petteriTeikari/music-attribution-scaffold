# fig-landscape-24: $7.4B Revenue Distribution: With vs Without Attribution

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-24 |
| **Title** | $7.4B Revenue Distribution: With vs Without Attribution |
| **Audience** | L1 (Music Industry) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | A (Hero) |

## Purpose

This figure dramatizes the stakes of attribution infrastructure by showing how a $7.4B market distributes revenue in two scenarios -- with and without attribution -- making the economic case that attribution infrastructure is itself a $740M-$1.1B market opportunity. It answers: "What is the economic value of building attribution, and who benefits?"

## Key Message

In a $7.4B market by 2035, without attribution 80% goes to platforms -- with attribution, 40-50% could flow to rights holders, making attribution infrastructure a $740M-$1.1B market itself.

## Visual Concept

Hero layout with two large side-by-side pie/donut charts or stacked bar visualizations. Left shows Scenario A (No Attribution): platforms dominate. Right shows Scenario B (With Attribution): more equitable distribution. The visual delta between the two scenarios is highlighted with a coral accent zone showing the $740M-$1.1B attribution infrastructure market opportunity. A data bar at the bottom shows the source projection: $558M (2024) to $7.4B (2035) at 26.5% CAGR.

```
+---------------------------------------------------------------+
|  $7.4B REVENUE DISTRIBUTION                                    |
|  ■ With vs Without Attribution (2035 Projection)                |
+---------------------------------------------------------------+
|                                                                |
|  SCENARIO A                        SCENARIO B                   |
|  NO ATTRIBUTION                    WITH ATTRIBUTION             |
|  ──────────────                    ─────────────────            |
|                                                                |
|  ┌────────────────────┐            ┌────────────────────┐      |
|  │                    │            │                    │      |
|  │    PLATFORMS       │            │   PLATFORMS        │      |
|  │      80%           │            │     35%            │      |
|  │    $5.92B          │            │   $2.59B           │      |
|  │                    │            ├────────────────────┤      |
|  │                    │            │   LABELS  25%      │      |
|  ├────────────────────┤            │   $1.85B           │      |
|  │ LABELS 15%  $1.11B │            ├────────────────────┤      |
|  ├────────────────────┤            │   ARTISTS 20%      │      |
|  │ ARTISTS 5%  $0.37B │            │   $1.48B           │      |
|  └────────────────────┘            ├────────────────────┤      |
|                                    │   INFRA   20%      │      |
|                                    │   $1.48B           │      |
|                                    └────────────────────┘      |
|                                                                |
|  ┌──────────────────────────────────────────────────────────┐  |
|  │  ■ THE DELTA = ATTRIBUTION INFRASTRUCTURE MARKET          │  |
|  │    $740M - $1.1B opportunity                              │  |
|  └──────────────────────────────────────────────────────────┘  |
|                                                                |
|  $558M (2024) ──── 26.5% CAGR ──── $7.4B (2035)               |
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
      text: "$7.4B REVENUE DISTRIBUTION"
    - type: label_editorial
      text: "With vs Without Attribution (2035 Projection)"

scenario_a:
  position: [60, 160]
  width: 860
  height: 560
  label: "SCENARIO A: NO ATTRIBUTION"
  total: "$7.4B"
  distribution:
    - { stakeholder: "Platforms", share: "80%", amount: "$5.92B" }
    - { stakeholder: "Labels", share: "15%", amount: "$1.11B" }
    - { stakeholder: "Artists", share: "5%", amount: "$0.37B" }

scenario_b:
  position: [940, 160]
  width: 860
  height: 560
  label: "SCENARIO B: WITH ATTRIBUTION"
  total: "$7.4B"
  distribution:
    - { stakeholder: "Platforms", share: "35%", amount: "$2.59B" }
    - { stakeholder: "Labels", share: "25%", amount: "$1.85B" }
    - { stakeholder: "Artists", share: "20%", amount: "$1.48B" }
    - { stakeholder: "Attribution Infrastructure", share: "20%", amount: "$1.48B" }

delta_callout:
  position: [60, 740]
  width: 1800
  height: 120
  elements:
    - type: callout_bar
      text: "THE DELTA = ATTRIBUTION INFRASTRUCTURE MARKET"
    - type: data_mono
      text: "$740M - $1.1B opportunity"

growth_bar:
  position: [60, 900]
  width: 1800
  height: 80
  elements:
    - type: data_mono
      text: "$558M (2024) ──── 26.5% CAGR ──── $7.4B (2035)"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "$7.4B REVENUE DISTRIBUTION" with coral accent square |
| Subtitle | `label_editorial` | "With vs Without Attribution (2035 Projection)" |
| Scenario A | `problem_statement` | No Attribution: 80% platforms, 15% labels, 5% artists |
| Scenario B | `solution_component` | With Attribution: 35% platforms, 25% labels, 20% artists, 20% infra |
| Platforms share (A) | `stakeholder_platform` | 80% / $5.92B in no-attribution scenario |
| Platforms share (B) | `stakeholder_platform` | 35% / $2.59B in attribution scenario |
| Labels share (A) | `stakeholder_label` | 15% / $1.11B without attribution |
| Labels share (B) | `stakeholder_label` | 25% / $1.85B with attribution |
| Artists share (A) | `stakeholder_artist` | 5% / $0.37B without attribution |
| Artists share (B) | `stakeholder_artist` | 20% / $1.48B with attribution |
| Infrastructure share | `solution_component` | 20% / $1.48B — attribution infrastructure slice |
| Delta callout | `callout_bar` | "The delta = attribution infrastructure market" |
| Market opportunity | `data_mono` | "$740M - $1.1B opportunity" |
| Growth projection | `data_mono` | "$558M (2024) to $7.4B (2035) at 26.5% CAGR" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Scenario A | Scenario B | contrast | "Attribution shifts distribution" |
| Platform share (A) | Platform share (B) | reduction | "80% to 35%" |
| Artist share (A) | Artist share (B) | increase | "5% to 20%" |
| Delta | Infrastructure market | implication | "$740M-$1.1B opportunity" |
| Growth bar | Total market | projection | "26.5% CAGR 2024-2035" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Market Delta | "The delta = attribution infrastructure market: $740M-$1.1B" | Between scenarios, bottom |
| Growth Projection | "$558M (2024) to $7.4B (2035) at 26.5% CAGR" | Bottom data bar |
| Artist Impact | "Artist share grows from 5% to 20% — 4x increase with attribution" | Within Scenario B |

## Text Content

### Labels (Max 30 chars each)

- $7.4B REVENUE DISTRIBUTION
- With vs Without Attribution
- SCENARIO A: NO ATTRIBUTION
- SCENARIO B: WITH ATTRIBUTION
- Platforms 80%
- Labels 15%
- Artists 5%
- Platforms 35%
- Labels 25%
- Artists 20%
- Attribution Infra 20%
- $740M-$1.1B opportunity
- 26.5% CAGR
- $558M (2024)
- $7.4B (2035)

### Caption (for embedding in documentation)

Projected $7.4B generative AI music market (2035) under two scenarios: without attribution, 80% flows to platforms with artists receiving only 5%; with attribution infrastructure, distribution shifts to 35% platforms, 25% labels, 20% artists, and 20% to attribution infrastructure itself -- creating a $740M-$1.1B market opportunity for attribution tools and services. Based on $558M (2024) growing at 26.5% CAGR.

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

1. The $7.4B figure is a PROJECTION for 2035 -- do NOT present as current revenue.
2. The 26.5% CAGR is from industry analyst reports -- do NOT claim proprietary analysis.
3. Revenue share percentages are ILLUSTRATIVE scenarios, not predictions -- do NOT claim precision.
4. Scenario A (No Attribution) is the DEFAULT trajectory without intervention.
5. Scenario B (With Attribution) is an ASPIRATIONAL outcome, not guaranteed.
6. The $740M-$1.1B attribution infrastructure market is DERIVED from the scenario delta, not independently sourced.
7. Do NOT name specific platforms in the distribution -- the point is STRUCTURAL, not company-specific.
8. The $558M (2024) starting figure is from "generative AI in music" market sizing -- do NOT conflate with total music industry revenue.
9. Artist share increase (5% to 20%) is the MOST important number for the music industry audience.
10. Do NOT use 3D pie charts or decorative chart effects -- clean, editorial data visualization only.

## Alt Text

Two scenarios showing $7.4B market split: without attribution 80% to platforms, with attribution 20% flows to artists.

## JSON Export Block

```json
{
  "id": "fig-landscape-24",
  "title": "$7.4B Revenue Distribution: With vs Without Attribution",
  "audience": "L1",
  "priority": "P2",
  "layout": "A",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Synthesize",
  "market_size": {
    "current": { "year": 2024, "amount": "$558M" },
    "projected": { "year": 2035, "amount": "$7.4B" },
    "cagr": "26.5%"
  },
  "scenarios": {
    "no_attribution": {
      "platforms": "80%",
      "labels": "15%",
      "artists": "5%"
    },
    "with_attribution": {
      "platforms": "35%",
      "labels": "25%",
      "artists": "20%",
      "infrastructure": "20%"
    }
  },
  "attribution_market": "$740M-$1.1B",
  "semantic_tags_used": [
    "heading_display", "label_editorial", "problem_statement", "solution_component",
    "stakeholder_platform", "stakeholder_label", "stakeholder_artist",
    "callout_bar", "data_mono"
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
