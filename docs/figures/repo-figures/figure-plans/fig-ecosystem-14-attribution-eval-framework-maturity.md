# fig-ecosystem-14: Attribution Evaluation Framework Maturity

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-14 |
| **Title** | Attribution Evaluation Framework Maturity |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:10 |
| **Layout Template** | E (Steps/Vertical) |

## Purpose

Shows the maturity progression of attribution evaluation from manual spot-checks through automated regression testing to CI-integrated golden dataset evaluation with drift detection. Answers: "What does the path from ad-hoc testing to continuous evaluation look like for attribution accuracy?"

## Key Message

Attribution evaluation matures through three stages -- manual spot-checks (current), automated regression testing with Promptfoo (recommended), CI-integrated golden dataset evaluation with drift detection (target).

## Visual Concept

Three vertical stages ascending from bottom (current) to top (target), each representing a maturity level. Each stage includes the approach, tooling, probability, and key characteristics. A vertical progress arrow on the left side emphasizes the maturity direction.

```
+---------------------------------------------------------------+
|  ATTRIBUTION EVALUATION FRAMEWORK MATURITY                     |
|  -- From Ad-Hoc to Continuous                                  |
+---------------------------------------------------------------+
|                                                                |
|  ▲                                                             |
|  │  III. CI GOLDEN DATASET (target)                            |
|  │  ┌─────────────────────────────────────────────────────┐   |
|  │  │  Braintrust or custom CI integration                 │   |
|  │  │  Golden dataset with known-correct attributions      │   |
|  │  │  Automated drift detection on every commit           │   |
|  │  │  Regression alerts, confidence calibration tracking   │   |
|  │  │  P = 0.20 (approximate)                              │   |
|  │  └─────────────────────────────────────────────────────┘   |
|  M                                                             |
|  A  II. AUTOMATED REGRESSION (recommended)                     |
|  T  ┌─────────────────────────────────────────────────────┐   |
|  U  │  Promptfoo CI integration (open-source)              │   |
|  R  │  Deterministic test cases, assertion-based            │   |
|  I  │  Runs on pull request, blocks merge on failure        │   |
|  T  │  Covers common attribution patterns                   │   |
|  Y  │  P = 0.45 (approximate)                              │   |
|     └─────────────────────────────────────────────────────┘   |
|  │                                                             |
|  │  I. MANUAL SPOT-CHECK (current)                             |
|  │  ┌─────────────────────────────────────────────────────┐   |
|  │  │  Human review of attribution outputs                 │   |
|  │  │  Ad hoc, no systematic coverage                      │   |
|  │  │  No regression detection                             │   |
|  │  │  Catches obvious errors only                         │   |
|  │  │  P = 0.35 (approximate)                              │   |
|  │  └─────────────────────────────────────────────────────┘   |
|  │                                                             |
+---------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1200
  background: primary_background

zones:
  - id: title_zone
    bounds: [0, 0, 1920, 130]
    content: "ATTRIBUTION EVALUATION FRAMEWORK MATURITY"
    role: title

  - id: maturity_arrow
    bounds: [60, 160, 60, 920]
    role: data_flow

  - id: stage_iii_zone
    bounds: [160, 160, 1700, 260]
    role: content_area

  - id: stage_ii_zone
    bounds: [160, 460, 1700, 260]
    role: content_area

  - id: stage_i_zone
    bounds: [160, 760, 1700, 260]
    role: content_area

anchors:
  - id: stage_iii
    position: [960, 290]
    size: [1560, 220]
    role: processing_stage
    label: "III. CI GOLDEN DATASET"

  - id: stage_ii
    position: [960, 590]
    size: [1560, 220]
    role: processing_stage
    label: "II. AUTOMATED REGRESSION"

  - id: stage_i
    position: [960, 890]
    size: [1560, 220]
    role: processing_stage
    label: "I. MANUAL SPOT-CHECK"

  - id: maturity_direction
    from: stage_i
    to: stage_iii
    type: arrow
    label: "MATURITY"

  - id: flow_i_to_ii
    from: stage_i
    to: stage_ii
    type: arrow
    label: "add automation"

  - id: flow_ii_to_iii
    from: stage_ii
    to: stage_iii
    type: arrow
    label: "add golden datasets + drift"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "ATTRIBUTION EVALUATION FRAMEWORK MATURITY" with coral accent square |
| Stage III -- CI Golden Dataset | `processing_stage` | Braintrust or custom, golden dataset, drift detection, P=0.20 |
| Stage II -- Automated Regression | `processing_stage` | Promptfoo CI, deterministic tests, PR blocking, P=0.45 |
| Stage I -- Manual Spot-Check | `processing_stage` | Human review, ad hoc, no regression detection, P=0.35 |
| Maturity arrow | `data_flow` | Vertical arrow showing progression direction |
| Prior probabilities | `data_mono` | P=0.35, P=0.45, P=0.20 for each stage |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Manual Spot-Check | Automated Regression | arrow | "add automation" |
| Automated Regression | CI Golden Dataset | arrow | "add golden datasets + drift" |
| data_quality_strategy (parent) | attribution_eval_framework | arrow | "strong" |
| build_vs_buy_posture (parent) | attribution_eval_framework | dashed | "moderate" |
| attribution_eval_framework | golden_dataset_management (child) | arrow | "strong" |
| attribution_eval_framework | attribution_accuracy_monitoring (child) | arrow | "strong" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "RECOMMENDED NEXT STEP" | Promptfoo automated regression provides the best effort-to-value ratio | right-margin |
| "PRIORS ARE APPROXIMATE" | P=0.35 / P=0.45 / P=0.20 reflect scaffold team assessment of likely adoption path | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "MANUAL SPOT-CHECK"
- Label 2: "AUTOMATED REGRESSION"
- Label 3: "CI GOLDEN DATASET"
- Label 4: "P = 0.35"
- Label 5: "P = 0.45"
- Label 6: "P = 0.20"
- Label 7: "Promptfoo (open-source)"
- Label 8: "Braintrust (commercial)"
- Label 9: "Drift detection"
- Label 10: "MATURITY"

### Caption (for embedding in documentation)

Attribution evaluation matures through three stages -- manual spot-checks (P=0.35, current), Promptfoo automated regression (P=0.45, recommended), and CI-integrated golden dataset evaluation with drift detection (P=0.20, target) -- with each stage building systematic coverage on top of the previous.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `data_flow`, `data_mono` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PRD nodes: `attribution_eval_framework`, `golden_dataset_management`. These are the primary decision nodes.
10. Parent nodes: `data_quality_strategy` (strong), `build_vs_buy_posture` (moderate).
11. Child nodes: `golden_dataset_management` (strong), `attribution_accuracy_monitoring` (strong).
12. Priors: `manual_spot_check` P=0.35, `automated_regression` P=0.45, `ci_golden_dataset` P=0.20.
13. Promptfoo is open-source -- do NOT present it as a paid product.
14. Braintrust is commercial -- do NOT present it as open-source.
15. These priors are approximate scaffold team assessments of likely adoption, NOT market data.
16. The scaffold is currently at Stage I (manual spot-check) -- do NOT imply automated evaluation is implemented.

## Alt Text

Eval framework maturity: manual spot-check to automated regression to CI golden datasets

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-14",
    "title": "Attribution Evaluation Framework Maturity",
    "audience": "L3",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Attribution evaluation matures through three stages -- manual spot-checks (current), automated regression testing with Promptfoo (recommended), CI-integrated golden dataset evaluation with drift detection (target).",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Stage III -- CI Golden Dataset",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["CI GOLDEN DATASET", "Drift detection", "P = 0.20"]
      },
      {
        "name": "Stage II -- Automated Regression",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["AUTOMATED REGRESSION", "Promptfoo", "P = 0.45"]
      },
      {
        "name": "Stage I -- Manual Spot-Check",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["MANUAL SPOT-CHECK", "Ad hoc", "P = 0.35"]
      }
    ],
    "relationships": [
      {
        "from": "Manual Spot-Check",
        "to": "Automated Regression",
        "type": "arrow",
        "label": "add automation"
      },
      {
        "from": "Automated Regression",
        "to": "CI Golden Dataset",
        "type": "arrow",
        "label": "add golden datasets + drift"
      }
    ],
    "callout_boxes": [
      {
        "heading": "RECOMMENDED NEXT STEP",
        "body_text": "Promptfoo automated regression provides the best effort-to-value ratio",
        "position": "right-margin"
      },
      {
        "heading": "PRIORS ARE APPROXIMATE",
        "body_text": "P=0.35 / P=0.45 / P=0.20 reflect scaffold team assessment of likely adoption path",
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
- [x] Anti-hallucination rules listed (8 default + 8 figure-specific)
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
