# fig-trends-04: Evaluation Framework Maturity Spectrum

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-trends-04 |
| **Title** | Evaluation Framework Maturity Spectrum |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/tech-trends-agentic-infrastructure-2026.md |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:10 |
| **Layout Template** | E (Steps/Vertical) |

## Purpose

Shows the three-tier evaluation pyramid for agent quality assurance -- from fast deterministic unit mocks at the base, through CI regression testing in the middle, to comprehensive dataset-driven evaluation at the top. Answers: "How do I test agent behavior at different levels of rigor?"

## Key Message

Three-tier evaluation pyramid -- PydanticAI built-in mocks for unit testing (fast, deterministic), Promptfoo for CI regression (open-source, automated), Braintrust for dataset-driven evaluation (comprehensive, drift detection).

## Visual Concept

Vertical pyramid with three tiers, widest at the base. Each tier shows the tool, characteristics, and cadence. A side annotation marks the scaffold's current state (base tier only).

```
+-----------------------------------------------------------------------+
|  EVALUATION FRAMEWORK MATURITY SPECTRUM                                |
|  ■ Three-tier eval pyramid                                             |
+-----------------------------------------------------------------------+
|                                                                        |
|                         ┌─────────────┐                                |
|                         │  BRAINTRUST │                                |
|                         │  DATASET    │                                |
|                         │─────────────│                                |
|                         │ Gold standard                                |
|                         │ Drift detection                              |
|                         │ Quarterly cadence                            |
|                    ┌────┴─────────────┴────┐                           |
|                    │   PROMPTFOO CI         │                           |
|                    │───────────────────────│                           |
|                    │ Automated regression   │                           |
|                    │ Model comparison       │                           |
|                    │ On schedule / nightly  │                           |
|               ┌────┴───────────────────────┴────┐                      |
|               │   PYDANTICAI MOCKS               │                     |
|               │─────────────────────────────────│                     |
|               │ Fast, deterministic              │      ┌───────────┐ |
|               │ Built-in mock models             │      │ SCAFFOLD  │ |
|               │ Every PR                         │  ◄── │ IS HERE   │ |
|               └─────────────────────────────────┘      └───────────┘ |
|                                                                        |
|  ────────────────────────────────────────────────────────────          |
|  SPEED    ■ fast ◄──────────────────────────────── slow ■              |
|  RIGOR    ■ low  ──────────────────────────────► high  ■              |
|  CADENCE  ■ every PR ─────── nightly ─────── quarterly ■              |
|                                                                        |
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
    content: "EVALUATION FRAMEWORK MATURITY SPECTRUM"
    role: title

  - id: pyramid_zone
    bounds: [300, 160, 1100, 640]
    content: "Eval pyramid"
    role: content_area

  - id: scaffold_marker
    bounds: [1480, 600, 300, 100]
    content: "SCAFFOLD IS HERE"
    role: callout_box

  - id: spectrum_bar
    bounds: [60, 860, 1800, 140]
    content: "Speed/Rigor/Cadence spectrum"
    role: content_area

anchors:
  - id: tier_3_braintrust
    position: [660, 200]
    size: [400, 160]
    role: processing_stage

  - id: tier_2_promptfoo
    position: [540, 380]
    size: [640, 140]
    role: processing_stage

  - id: tier_1_pydanticai
    position: [400, 540]
    size: [900, 140]
    role: selected_option

  - id: scaffold_here
    position: [1500, 620]
    size: [260, 60]
    role: callout_box

  - id: arrow_scaffold
    from: scaffold_here
    to: tier_1_pydanticai
    type: arrow
    label: "current state"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Braintrust tier | `processing_stage` | Top of pyramid -- gold standard, drift detection, quarterly cadence |
| Promptfoo tier | `processing_stage` | Middle of pyramid -- automated regression, model comparison, nightly |
| PydanticAI Mocks tier | `selected_option` | Base of pyramid -- fast, deterministic, every PR |
| Scaffold marker | `callout_box` | Arrow pointing to base tier indicating current scaffold state |
| Spectrum bar | `data_flow` | Speed / rigor / cadence spectrum annotations |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| PydanticAI Mocks | Promptfoo CI | arrow | "maturity progression" |
| Promptfoo CI | Braintrust Dataset | arrow | "maturity progression" |
| Scaffold marker | PydanticAI Mocks | arrow | "current state" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "SCAFFOLD IS HERE" | Currently at base tier (PydanticAI mocks only) | right-margin |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "BRAINTRUST DATASET"
- Label 2: "Gold standard"
- Label 3: "Drift detection"
- Label 4: "Quarterly cadence"
- Label 5: "PROMPTFOO CI"
- Label 6: "Automated regression"
- Label 7: "Model comparison"
- Label 8: "Nightly / scheduled"
- Label 9: "PYDANTICAI MOCKS"
- Label 10: "Fast, deterministic"
- Label 11: "Built-in mock models"
- Label 12: "Every PR"

### Caption (for embedding in documentation)

Three-tier evaluation pyramid for agent quality: PydanticAI mocks (unit), Promptfoo (CI regression), Braintrust (dataset-driven). The scaffold currently operates at the base tier.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `selected_option`, `callout_box` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PydanticAI has built-in testing utilities (mock models, deterministic responses) -- these are real, shipped features.
10. Promptfoo is open-source prompt/model evaluation with CI/CD integration -- do NOT confuse with proprietary eval tools.
11. Braintrust provides dataset-driven evaluation with scoring -- it is a separate product from Promptfoo.
12. PRD node: attribution_eval_framework. Current scaffold state: PydanticAI mocks only (manual_spot_check prior P=0.35).
13. Do NOT claim the scaffold currently uses Promptfoo or Braintrust -- these are future tiers.
14. The pyramid progression is aspirational -- teams can skip tiers or use alternatives at each level.
15. Do NOT show specific eval scores or benchmark numbers -- focus on the tier structure.

## Alt Text

Eval maturity spectrum: PydanticAI mocks to Promptfoo CI to Braintrust dataset eval

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "trends-04",
    "title": "Evaluation Framework Maturity Spectrum",
    "audience": "L3",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Three-tier eval pyramid: PydanticAI mocks (fast), Promptfoo CI (automated), Braintrust (comprehensive).",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Braintrust Tier",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["BRAINTRUST DATASET", "Gold standard", "Drift detection", "Quarterly"]
      },
      {
        "name": "Promptfoo Tier",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["PROMPTFOO CI", "Automated regression", "Model comparison", "Nightly"]
      },
      {
        "name": "PydanticAI Mocks Tier",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["PYDANTICAI MOCKS", "Fast, deterministic", "Every PR"]
      }
    ],
    "relationships": [
      {
        "from": "PydanticAI Mocks",
        "to": "Promptfoo CI",
        "type": "arrow",
        "label": "maturity progression"
      },
      {
        "from": "Promptfoo CI",
        "to": "Braintrust Dataset",
        "type": "arrow",
        "label": "maturity progression"
      }
    ],
    "callout_boxes": [
      {
        "heading": "SCAFFOLD IS HERE",
        "body_text": "Currently at base tier: PydanticAI mocks only (manual_spot_check prior P=0.35)",
        "position": "right-margin"
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
- [x] Audience level correct (L3)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
