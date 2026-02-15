# fig-landscape-17: Five Licensing Models: Economics at Scale

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-17 |
| **Title** | Five Licensing Models: Economics at Scale |
| **Audience** | L1 (Music Industry) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

This figure compares five distinct licensing models for AI-generated music, revealing how the economics of each model change dramatically as output scales from thousands to billions of tracks. It answers: "Which licensing approach works at what scale, and why do simple models break?"

## Key Message

Five licensing models exist (flat settlement, per-output, cohort, blanket, attribution-weighted) -- what works at 1K tracks fails at 1B, and the economics change dramatically with scale.

## Visual Concept

Five horizontal panels stacked vertically, each representing one licensing model. Each panel contains the model name, a real-world example, a brief mechanism description, and a three-column scale indicator showing viability at 1K / 1M / 1B tracks. A coral accent line marks the "scaling cliff" where each model breaks down. The bottom panel (attribution-weighted) is visually distinguished as the theoretical ideal.

```
+---------------------------------------------------------------+
|  FIVE LICENSING MODELS                                         |
|  ■ Economics at Scale                                          |
+---------------------------------------------------------------+
|                                                                |
|  I. FLAT SETTLEMENT                        1K    1M    1B     |
|  ─────────────────────                   ┌────┬────┬────┐     |
|  Suno/Warner one-time payment            │ OK │ OK │FAIL│     |
|  Simple but unfair to individuals        └────┴────┴────┘     |
|  ──────────────────────────────────────── ■ cliff at fairness  |
|                                                                |
|  II. PER-OUTPUT                            1K    1M    1B     |
|  ──────────────                          ┌────┬────┬────┐     |
|  Ideal precision, requires attribution   │ OK │HARD│FAIL│     |
|  Computationally expensive at scale      └────┴────┴────┘     |
|  ──────────────────────────────────────── ■ cliff at compute   |
|                                                                |
|  III. COHORT-BASED                         1K    1M    1B     |
|  ────────────────                        ┌────┬────┬────┐     |
|  Lemonaide genre/style grouping          │ OK │ OK │HARD│     |
|  Middle ground, approximate fairness     └────┴────┴────┘     |
|  ──────────────────────────────────────── ■ cliff at granulrty |
|                                                                |
|  IV. BLANKET LICENSE                       1K    1M    1B     |
|  ──────────────────                      ┌────┬────┬────┐     |
|  STIM collective model, traditional      │ OK │ OK │ OK │     |
|  Scales well, low attribution accuracy   └────┴────┴────┘     |
|  ──────────────────────────────────────── ■ no cliff, low acc. |
|                                                                |
|  V. ATTRIBUTION-WEIGHTED                   1K    1M    1B     |
|  ────────────────────────                ┌────┬────┬────┐     |
|  Proportional to measured influence      │HARD│ OK │ OK │     |
|  Theoretical ideal, high infra cost      └────┴────┴────┘     |
|  ──────────────────────────────────────── ■ cliff at bootstrap |
|                                                                |
+---------------------------------------------------------------+
|  ■ Simple models break at scale; sophisticated models need     |
|    infrastructure that only pays off at scale                   |
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
      text: "FIVE LICENSING MODELS"
    - type: label_editorial
      text: "Economics at Scale"

scale_header:
  position: [1400, 130]
  width: 460
  height: 40
  elements:
    - type: data_mono
      text: "1K        1M        1B"

panel_flat_settlement:
  position: [60, 160]
  width: 1800
  height: 140
  label: "I. FLAT SETTLEMENT"
  example: "Suno/Warner one-time payment"
  mechanism: "Simple but unfair to individuals"
  scale_viability: { "1K": "viable", "1M": "viable", "1B": "fails" }
  cliff: "fairness — individual artists invisible"

panel_per_output:
  position: [60, 310]
  width: 1800
  height: 140
  label: "II. PER-OUTPUT"
  example: "Ideal precision model"
  mechanism: "Requires per-track attribution"
  scale_viability: { "1K": "viable", "1M": "difficult", "1B": "fails" }
  cliff: "compute — attribution cost per track"

panel_cohort:
  position: [60, 460]
  width: 1800
  height: 140
  label: "III. COHORT-BASED"
  example: "Lemonaide genre/style grouping"
  mechanism: "Middle ground, approximate fairness"
  scale_viability: { "1K": "viable", "1M": "viable", "1B": "difficult" }
  cliff: "granularity — cohort boundaries blur"

panel_blanket:
  position: [60, 610]
  width: 1800
  height: 140
  label: "IV. BLANKET LICENSE"
  example: "STIM collective model"
  mechanism: "Traditional collective, scales well"
  scale_viability: { "1K": "viable", "1M": "viable", "1B": "viable" }
  cliff: "none — but attribution accuracy is low"

panel_attribution_weighted:
  position: [60, 760]
  width: 1800
  height: 140
  label: "V. ATTRIBUTION-WEIGHTED"
  example: "Theoretical ideal"
  mechanism: "Proportional to measured influence"
  scale_viability: { "1K": "difficult", "1M": "viable", "1B": "viable" }
  cliff: "bootstrap — infrastructure cost before scale"

callout_bottom:
  position: [60, 940]
  width: 1800
  height: 100
  elements:
    - type: callout_bar
      text: "Simple models break at scale; sophisticated models need infrastructure that only pays off at scale"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "FIVE LICENSING MODELS" with coral accent square |
| Subtitle | `label_editorial` | "Economics at Scale" |
| Scale header | `data_mono` | Column headers: 1K / 1M / 1B tracks |
| Flat settlement panel | `solution_component` | Row I: one-time payment model with scale viability |
| Per-output panel | `solution_component` | Row II: per-track licensing with compute cliff |
| Cohort-based panel | `solution_component` | Row III: genre/style grouping with granularity cliff |
| Blanket license panel | `solution_component` | Row IV: collective model, no cliff but low accuracy |
| Attribution-weighted panel | `solution_component` | Row V: theoretical ideal with bootstrap cliff |
| Viability indicators | `badge_label` | OK / HARD / FAIL status per scale tier |
| Scaling cliff markers | `callout_bar` | Coral accent marking where each model breaks |
| Roman numerals | `section_numeral` | I through V panel headers |
| Bottom insight | `callout_bar` | Paradox: simple breaks at scale, complex needs scale |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Flat settlement | Per-output | progression | "Increasing precision" |
| Per-output | Cohort-based | tradeoff | "Precision vs cost" |
| Cohort-based | Blanket license | progression | "Increasing coverage" |
| Blanket license | Attribution-weighted | aspiration | "Adding attribution layer" |
| All models | Scaling cliff | threshold | "Each model has a breaking point" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Scale Paradox | "Simple models break at scale; sophisticated models need infrastructure that only pays off at scale" | Bottom full-width bar |
| Cliff Legend | OK = viable, HARD = strained, FAIL = breaks | Top-right corner |

## Text Content

### Labels (Max 30 chars each)

- FIVE LICENSING MODELS
- Economics at Scale
- FLAT SETTLEMENT
- PER-OUTPUT
- COHORT-BASED
- BLANKET LICENSE
- ATTRIBUTION-WEIGHTED
- Suno/Warner one-time payment
- Lemonaide genre grouping
- STIM collective model
- Proportional to influence
- 1K tracks
- 1M tracks
- 1B tracks
- Scaling cliff

### Caption (for embedding in documentation)

Five licensing models for AI-generated music -- flat settlement (simple but unfair at scale), per-output (precise but computationally expensive), cohort-based (middle ground via genre grouping), blanket license (scales well but low attribution accuracy), and attribution-weighted (theoretical ideal requiring significant infrastructure) -- each with different scaling cliffs where their economics break down.

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

1. There are exactly FIVE licensing models -- do NOT add or remove any.
2. Scale tiers are exactly 1K, 1M, 1B -- do NOT use other breakpoints.
3. Do NOT imply any single model is "correct" -- the point is that EACH has tradeoffs.
4. The Suno/Warner deal is a FLAT SETTLEMENT example, not per-output -- do NOT conflate.
5. Lemonaide uses COHORT-BASED licensing -- do NOT describe it as blanket or per-output.
6. Attribution-weighted is THEORETICAL -- do NOT imply it is currently deployed at scale.
7. The scaling cliff is a VIABILITY threshold, not a hard failure -- models degrade gradually.
8. This figure compares MODELS side by side, not the STIM flow (which is fig-trends-07).

## Alt Text

Five licensing models compared at 1K, 1M, and 1B scale, showing where each model's economics break down.

## JSON Export Block

```json
{
  "id": "fig-landscape-17",
  "title": "Five Licensing Models: Economics at Scale",
  "audience": "L1",
  "priority": "P0",
  "layout": "B",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Synthesize",
  "models": [
    { "name": "Flat Settlement", "example": "Suno/Warner", "cliff": "fairness", "scale_1k": "viable", "scale_1m": "viable", "scale_1b": "fails" },
    { "name": "Per-Output", "example": "ideal precision", "cliff": "compute", "scale_1k": "viable", "scale_1m": "difficult", "scale_1b": "fails" },
    { "name": "Cohort-Based", "example": "Lemonaide", "cliff": "granularity", "scale_1k": "viable", "scale_1m": "viable", "scale_1b": "difficult" },
    { "name": "Blanket License", "example": "STIM", "cliff": "accuracy", "scale_1k": "viable", "scale_1m": "viable", "scale_1b": "viable" },
    { "name": "Attribution-Weighted", "example": "theoretical ideal", "cliff": "bootstrap", "scale_1k": "difficult", "scale_1m": "viable", "scale_1b": "viable" }
  ],
  "semantic_tags_used": [
    "heading_display", "label_editorial", "solution_component", "badge_label",
    "callout_bar", "section_numeral", "data_mono"
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
