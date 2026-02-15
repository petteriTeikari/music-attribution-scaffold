# fig-landscape-16: UQ in Attribution: From Medical Diagnosis to Music Credits

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-16 |
| **Title** | UQ in Attribution: From Medical Diagnosis to Music Credits |
| **Audience** | L4 (AI/ML Researcher) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

This is a SIGNATURE FIGURE (5/5 novelty) that establishes the structural isomorphism between uncertainty quantification in three mature domains (medical diagnosis, autonomous driving, financial risk) and the nascent field of music attribution. This is not metaphor -- the mathematical frameworks (conformal prediction, Bayesian updating, calibration curves) transfer directly. Answers: "Why should we trust that principled UQ can work for music attribution when no one has done it before?"

## Key Message

Music attribution faces the same uncertainty quantification challenges as medical diagnosis, autonomous driving, and financial risk -- conformal prediction and Bayesian updating transfer directly from these mature domains.

## Visual Concept

Split panel with the left side showing three mature UQ domains stacked vertically (medical, automotive, financial), each with its specific UQ technique and confidence output. The right side shows music attribution UQ challenges mapped structurally from those domains, with explicit arrows showing the isomorphism. The center column contains the shared methodological toolkit that connects both sides (conformal prediction, Bayesian updating, calibration curves, SConU). The visual rhythm emphasizes PARALLEL STRUCTURE -- each left-side domain maps to a specific right-side attribution challenge through a shared method. This is deliberately more detailed than other figures because of its 5/5 novelty rating.

```
+-----------------------------------------------------------------------+
|  UQ IN ATTRIBUTION                                                     |
|  ■ From Medical Diagnosis to Music Credits                              |
+-----------------------------------------------------------------------+
|                                                                        |
|  MATURE UQ DOMAINS           SHARED TOOLKIT        MUSIC ATTRIBUTION   |
|  ════════════════           ══════════════         ═══════════════     |
|                                                                        |
|  ┌───────────────┐    ┌─────────────────┐    ┌───────────────┐        |
|  │ MEDICAL       │    │                 │    │ CONFIDENCE    │        |
|  │ DIAGNOSIS     │    │  Conformal      │    │ SCORING       │        |
|  │ ────────────  │    │  Prediction     │    │ ────────────  │        |
|  │ Diagnostic    │───►│  (Vovk 2005)    │───►│ Attribution   │        |
|  │ confidence    │    │                 │    │ confidence    │        |
|  │ intervals     │    │  Distribution-  │    │ intervals     │        |
|  │               │    │  free coverage  │    │               │        |
|  │ Calibrated    │    │  guarantees     │    │ Per-source    │        |
|  │ probabilities │    │                 │    │ probability   │        |
|  └───────────────┘    │                 │    └───────────────┘        |
|                        │  ─────────────  │                             |
|  ┌───────────────┐    │                 │    ┌───────────────┐        |
|  │ AUTONOMOUS    │    │  Bayesian       │    │ MULTI-SOURCE  │        |
|  │ DRIVING       │    │  Updating       │    │ FUSION        │        |
|  │ ────────────  │    │                 │    │ ────────────  │        |
|  │ Perception    │───►│  Prior beliefs  │───►│ Prior: A0-A3  │        |
|  │ uncertainty   │    │  + new evidence │    │ + new sources │        |
|  │               │    │  = posterior    │    │ = posterior   │        |
|  │ Sensor fusion │    │                 │    │ Multi-source  │        |
|  │ confidence    │    │                 │    │ agreement     │        |
|  └───────────────┘    │                 │    └───────────────┘        |
|                        │  ─────────────  │                             |
|  ┌───────────────┐    │                 │    ┌───────────────┐        |
|  │ FINANCIAL     │    │  Calibration    │    │ ASSURANCE     │        |
|  │ RISK          │    │  Curves         │    │ TIERS         │        |
|  │ ────────────  │    │                 │    │ ────────────  │        |
|  │ Value-at-Risk │───►│  Predicted vs   │───►│ A0-A3 as     │        |
|  │               │    │  observed freq. │    │ risk tiers   │        |
|  │ Credit scoring│    │                 │    │               │        |
|  │ calibration   │    │  SConU          │    │ Confidence    │        |
|  │               │    │  (LLM UQ)       │    │ calibration   │        |
|  └───────────────┘    └─────────────────┘    └───────────────┘        |
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────────┐  |
|  │  STRUCTURAL ISOMORPHISM -- not metaphor, identical mathematics   │  |
|  │  Same conformal prediction framework, same Bayesian updating,    │  |
|  │  same calibration requirements, different domain instantiation   │  |
|  └─────────────────────────────────────────────────────────────────┘  |
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
    bounds: [0, 0, 1920, 100]
    content: "UQ IN ATTRIBUTION"
    role: title

  - id: subtitle_zone
    bounds: [0, 100, 1920, 40]
    content: "From Medical Diagnosis to Music Credits"
    role: subtitle

  - id: column_labels
    bounds: [60, 150, 1800, 30]
    role: label_editorial
    label: "Column headers"

  - id: left_column
    bounds: [60, 180, 540, 680]
    role: content_area
    label: "MATURE UQ DOMAINS"

  - id: center_column
    bounds: [660, 180, 600, 680]
    role: content_area
    label: "SHARED TOOLKIT"

  - id: right_column
    bounds: [1320, 180, 540, 680]
    role: content_area
    label: "MUSIC ATTRIBUTION"

  - id: footer_callout
    bounds: [60, 900, 1800, 140]
    role: callout_bar
    label: "STRUCTURAL ISOMORPHISM"

anchors:
  - id: medical_domain
    position: [80, 200]
    size: [500, 200]
    role: solution_component
    label: "Medical Diagnosis"

  - id: automotive_domain
    position: [80, 430]
    size: [500, 200]
    role: solution_component
    label: "Autonomous Driving"

  - id: financial_domain
    position: [80, 660]
    size: [500, 200]
    role: solution_component
    label: "Financial Risk"

  - id: conformal_prediction
    position: [680, 200]
    size: [560, 160]
    role: processing_stage
    label: "Conformal Prediction"

  - id: bayesian_updating
    position: [680, 400]
    size: [560, 160]
    role: processing_stage
    label: "Bayesian Updating"

  - id: calibration_curves
    position: [680, 600]
    size: [560, 160]
    role: processing_stage
    label: "Calibration Curves + SConU"

  - id: confidence_scoring
    position: [1340, 200]
    size: [500, 200]
    role: solution_component
    label: "Confidence Scoring"

  - id: multisource_fusion
    position: [1340, 430]
    size: [500, 200]
    role: solution_component
    label: "Multi-Source Fusion"

  - id: assurance_tiers
    position: [1340, 660]
    size: [500, 200]
    role: solution_component
    label: "Assurance Tiers"

  - id: iso_medical_to_conformal
    from: medical_domain
    to: conformal_prediction
    type: arrow
    label: "diagnostic CI → conformal prediction"

  - id: iso_conformal_to_confidence
    from: conformal_prediction
    to: confidence_scoring
    type: arrow
    label: "conformal prediction → attribution CI"

  - id: iso_automotive_to_bayesian
    from: automotive_domain
    to: bayesian_updating
    type: arrow
    label: "sensor fusion → Bayesian updating"

  - id: iso_bayesian_to_fusion
    from: bayesian_updating
    to: multisource_fusion
    type: arrow
    label: "Bayesian updating → source fusion"

  - id: iso_financial_to_calibration
    from: financial_domain
    to: calibration_curves
    type: arrow
    label: "credit scoring → calibration curves"

  - id: iso_calibration_to_assurance
    from: calibration_curves
    to: assurance_tiers
    type: arrow
    label: "calibration → A0-A3 tiers"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "UQ IN ATTRIBUTION" in editorial caps with accent square |
| Subtitle | `label_editorial` | "From Medical Diagnosis to Music Credits" |
| Medical Diagnosis domain | `solution_component` | Diagnostic confidence intervals, calibrated probabilities, well-studied for decades |
| Autonomous Driving domain | `solution_component` | Perception uncertainty, sensor fusion confidence, safety-critical UQ |
| Financial Risk domain | `solution_component` | Value-at-Risk, credit scoring calibration, regulatory-driven UQ |
| Conformal Prediction method | `processing_stage` | Vovk (2005) framework: distribution-free coverage guarantees, finite-sample validity |
| Bayesian Updating method | `processing_stage` | Prior beliefs + new evidence = posterior, sequential evidence integration |
| Calibration Curves + SConU | `processing_stage` | Predicted vs observed frequency alignment, SConU for LLM confidence |
| Confidence Scoring output | `solution_component` | Attribution confidence intervals, per-source probability estimates |
| Multi-Source Fusion output | `solution_component` | Prior A0-A3 + new source evidence = posterior assurance, multi-source agreement |
| Assurance Tiers output | `solution_component` | A0-A3 mapped as risk tiers, confidence calibration across tiers |
| Isomorphism arrows | `data_flow` | Left-to-center-to-right arrows showing structural mapping |
| Footer callout | `callout_bar` | "STRUCTURAL ISOMORPHISM -- not metaphor, identical mathematics" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Medical Diagnosis | Conformal Prediction | arrow | Diagnostic CI maps to conformal prediction |
| Conformal Prediction | Confidence Scoring | arrow | Same math, different domain |
| Autonomous Driving | Bayesian Updating | arrow | Sensor fusion maps to Bayesian updating |
| Bayesian Updating | Multi-Source Fusion | arrow | Same math, different domain |
| Financial Risk | Calibration Curves | arrow | Credit scoring maps to calibration |
| Calibration Curves | Assurance Tiers | arrow | Same math, different domain |
| All three methods | Shared toolkit | contains | Unified mathematical framework |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "STRUCTURAL ISOMORPHISM" | This is NOT analogy -- conformal prediction provides the same distribution-free coverage guarantees whether applied to medical diagnosis, autonomous driving, or music attribution. The mathematics is identical; only the domain instantiation changes. | footer, full width, emphasized |
| "CONFORMAL PREDICTION" | Vovk (2005): given exchangeable data and any black-box model, produces prediction sets with guaranteed coverage probability. No distributional assumptions needed. Applied in medicine (diagnostic uncertainty), now transferable to attribution (confidence intervals). | center column, first method |
| "BAYESIAN UPDATING" | Sequential evidence integration: start with prior belief (A0 = no data), observe evidence from each source, update posterior. Identical structure to multi-sensor fusion in autonomous driving, now applied to multi-source attribution. | center column, second method |
| "SConU FRAMEWORK" | Beigi et al. (2024) Semantic Consistency Uncertainty for LLM confidence calibration. Measures consistency of model outputs across reformulations. Applicable to attribution confidence when using LLM-based analysis. | center column, third method inset |
| "VOVK 2005" | The foundational conformal prediction reference. Key property: finite-sample validity without distributional assumptions. This is what makes the cross-domain transfer rigorous, not analogical. | left of conformal prediction |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Medical Diagnosis"
- Label 2: "Autonomous Driving"
- Label 3: "Financial Risk"
- Label 4: "Conformal Prediction"
- Label 5: "Bayesian Updating"
- Label 6: "Calibration Curves"
- Label 7: "SConU Framework"
- Label 8: "Confidence Scoring"
- Label 9: "Multi-Source Fusion"
- Label 10: "Assurance Tiers (A0-A3)"
- Label 11: "Diagnostic CI"
- Label 12: "Perception Uncertainty"
- Label 13: "Value-at-Risk"
- Label 14: "Distribution-Free"
- Label 15: "Prior + Evidence = Posterior"
- Label 16: "Coverage Guarantees"
- Label 17: "Structural Isomorphism"
- Label 18: "Vovk 2005"
- Label 19: "Beigi 2024 (LLM UQ)"
- Label 20: "Identical Mathematics"

### Caption (for embedding in documentation)

SIGNATURE FIGURE. Three mature uncertainty quantification domains -- medical diagnosis (diagnostic confidence intervals), autonomous driving (sensor fusion), and financial risk (Value-at-Risk, credit scoring) -- map structurally to music attribution challenges through a shared methodological toolkit: conformal prediction (Vovk 2005) provides distribution-free coverage guarantees, Bayesian updating enables sequential multi-source evidence integration, and calibration curves (including SConU from Beigi et al. 2024) ensure predicted confidence matches observed frequency. This is structural isomorphism, not metaphor -- the same mathematical frameworks apply directly. A0-A3 assurance levels parallel risk tiers in finance and confidence grades in medicine.

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

8. Conformal prediction is from Vovk (2005), "Algorithmic Learning in a Random World" -- do NOT cite a different year or title.
9. SConU is from Beigi et al. (2024), a taxonomy for LLM uncertainty quantification -- do NOT attribute to other authors.
10. A0-A3 assurance levels are from Teikari (2026) -- they are NOT an established industry standard.
11. The structural isomorphism claim is the CORE NOVELTY -- do NOT weaken it to "analogy" or "metaphor."
12. Conformal prediction provides DISTRIBUTION-FREE guarantees -- do NOT claim it requires specific distributions.
13. Value-at-Risk is a specific financial risk measure -- do NOT conflate with general "risk assessment."
14. Sensor fusion in autonomous driving involves LIDAR, camera, radar -- do NOT oversimplify to "camera only."
15. Bayesian updating is sequential -- prior + evidence = posterior, then posterior becomes new prior -- do NOT describe it as one-shot.
16. Do NOT claim the scaffold currently implements conformal prediction -- it is a framework that CAN be instantiated.
17. The three mature domains are EXAMPLES, not exhaustive -- but these three have the richest UQ literature.
18. Do NOT add deep learning uncertainty (MC dropout, ensembles) as a fourth domain -- keep the focus on the three structural parallels.
19. Credit scoring calibration is regulated (e.g., ECOA, Basel III) -- this regulatory driver parallels potential music attribution regulation.
20. "Identical mathematics" means the same theorems and proofs apply -- do NOT claim the implementation is identical (domain-specific engineering differs).

## Alt Text

Cross-domain UQ isomorphism: medical, automotive, financial domains map to music attribution via shared methods

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "landscape-16",
    "title": "UQ in Attribution: From Medical Diagnosis to Music Credits",
    "audience": "L4",
    "layout_template": "D",
    "novelty": "5/5 -- SIGNATURE FIGURE"
  },
  "content_architecture": {
    "primary_message": "Conformal prediction and Bayesian updating transfer directly from medical/automotive/financial UQ to music attribution -- structural isomorphism, not metaphor.",
    "layout_flow": "three-column-isomorphism",
    "key_structures": [
      {
        "name": "Medical Diagnosis",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["Diagnostic CI", "Calibrated probabilities"]
      },
      {
        "name": "Autonomous Driving",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["Perception uncertainty", "Sensor fusion"]
      },
      {
        "name": "Financial Risk",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["Value-at-Risk", "Credit scoring calibration"]
      },
      {
        "name": "Conformal Prediction",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Vovk 2005", "Distribution-free", "Coverage guarantees"]
      },
      {
        "name": "Bayesian Updating",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Prior + evidence = posterior", "Sequential integration"]
      },
      {
        "name": "Calibration Curves + SConU",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Predicted vs observed", "Beigi 2024", "LLM UQ"]
      },
      {
        "name": "Confidence Scoring",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["Attribution CI", "Per-source probability"]
      },
      {
        "name": "Multi-Source Fusion",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["A0-A3 prior", "Source agreement"]
      },
      {
        "name": "Assurance Tiers",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["A0-A3 as risk tiers", "Calibrated"]
      }
    ],
    "relationships": [
      {
        "from": "Medical Diagnosis",
        "to": "Conformal Prediction",
        "type": "arrow",
        "label": "diagnostic CI uses conformal"
      },
      {
        "from": "Conformal Prediction",
        "to": "Confidence Scoring",
        "type": "arrow",
        "label": "same math → attribution CI"
      },
      {
        "from": "Autonomous Driving",
        "to": "Bayesian Updating",
        "type": "arrow",
        "label": "sensor fusion uses Bayesian"
      },
      {
        "from": "Bayesian Updating",
        "to": "Multi-Source Fusion",
        "type": "arrow",
        "label": "same math → source fusion"
      },
      {
        "from": "Financial Risk",
        "to": "Calibration Curves",
        "type": "arrow",
        "label": "credit scoring uses calibration"
      },
      {
        "from": "Calibration Curves",
        "to": "Assurance Tiers",
        "type": "arrow",
        "label": "same math → A0-A3 tiers"
      }
    ],
    "callout_boxes": [
      {
        "heading": "STRUCTURAL ISOMORPHISM",
        "body_text": "Not metaphor -- identical mathematical frameworks, different domain instantiation",
        "position": "footer-emphasized"
      },
      {
        "heading": "CONFORMAL PREDICTION",
        "body_text": "Vovk 2005: distribution-free coverage guarantees from medicine to attribution",
        "position": "center-top"
      },
      {
        "heading": "BAYESIAN UPDATING",
        "body_text": "Sequential evidence integration: same structure as sensor fusion → source fusion",
        "position": "center-middle"
      },
      {
        "heading": "SConU FRAMEWORK",
        "body_text": "Beigi 2024: semantic consistency uncertainty for LLM confidence, applicable to attribution",
        "position": "center-bottom"
      },
      {
        "heading": "VOVK 2005",
        "body_text": "Foundational reference: finite-sample validity without distributional assumptions",
        "position": "center-left-margin"
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
- [x] Audience level correct (L4)
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
