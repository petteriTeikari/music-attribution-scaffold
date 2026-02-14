# fig-ecosystem-04: TDA Provider Landscape

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-04 |
| **Title** | TDA Provider Landscape |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Compares training-time (Musical AI, Sureel) vs post-hoc (embedding, fingerprint) attribution approaches. Answers: "What are the architectural trade-offs between training-time and post-hoc attribution?"

## Key Message

Training-time attribution (Musical AI) requires model training integration; post-hoc approaches (Sureel fingerprinting, embedding similarity) work on any output but with lower accuracy.

## Visual Concept

Split panel with left side showing training-time attribution and right side showing post-hoc approaches. Left panel features Musical AI with Fairly Trained certification, data influence functions, and model training access requirement. Right panel features fingerprinting (Sureel, 86-90% claimed accuracy), embedding similarity, and content ID. Bottom axis shows accuracy vs integration effort trade-off.

```
+-----------------------------------------------------------------------+
|  TDA PROVIDER LANDSCAPE                                                |
|  ■ Training-Time vs Post-Hoc Attribution                               |
+-----------------------------------------------------------------------+
|                                                                        |
|  TRAINING-TIME                      POST-HOC                           |
|  ══════════════                     ════════                           |
|  Requires model access              Works on any output                |
|                                                                        |
|  ┌──────────────────────────┐      ┌──────────────────────────┐       |
|  │                          │      │                          │       |
|  │  Musical AI              │      │  Sureel AI               │       |
|  │  ──────────              │      │  ─────────               │       |
|  │  $6M funding             │      │  Audio fingerprinting    │       |
|  │  Fairly Trained          │      │  86-90% accuracy         │       |
|  │  certified               │      │  (CLAIMED, not verified) │       |
|  │                          │      │  5 patents pending       │       |
|  │  Data Influence          │      │  STIM partnership        │       |
|  │  Functions               │      │                          │       |
|  │  ──────────────          │      │  Embedding Similarity    │       |
|  │  Traces which training   │      │  ─────────────────────   │       |
|  │  examples influenced     │      │  Vector distance         │       |
|  │  each output             │      │  Handles transformations │       |
|  │                          │      │  Lower precision         │       |
|  │  ┌────────────────────┐  │      │                          │       |
|  │  │ Requires integration│  │      │  Content ID Systems     │       |
|  │  │ during model        │  │      │  ──────────────────     │       |
|  │  │ training pipeline   │  │      │  Fingerprint matching   │       |
|  │  └────────────────────┘  │      │  Works on copies        │       |
|  │                          │      │  Post-hoc only          │       |
|  └──────────────────────────┘      └──────────────────────────┘       |
|                                                                        |
|  ◄─── Higher accuracy / Higher effort ──── Lower effort / Lower ───► |
|                                              accuracy                  |
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
    content: "TDA PROVIDER LANDSCAPE"
    role: title

  - id: training_time_panel
    bounds: [60, 160, 880, 720]
    role: content_area
    label: "TRAINING-TIME"

  - id: post_hoc_panel
    bounds: [980, 160, 880, 720]
    role: content_area
    label: "POST-HOC"

  - id: tradeoff_axis
    bounds: [60, 920, 1800, 120]
    role: callout_bar
    label: "Accuracy vs integration effort trade-off"

anchors:
  - id: musical_ai
    position: [160, 260]
    size: [680, 320]
    role: decision_point
    label: "Musical AI"

  - id: fairly_trained_badge
    position: [520, 300]
    size: [200, 40]
    role: selected_option
    label: "Fairly Trained Certified"

  - id: data_influence
    position: [160, 440]
    size: [680, 100]
    role: processing_stage
    label: "Data Influence Functions"

  - id: model_access_constraint
    position: [200, 560]
    size: [600, 60]
    role: callout_bar
    label: "Requires model training integration"

  - id: sureel_ai
    position: [1080, 260]
    size: [680, 200]
    role: decision_point
    label: "Sureel AI"

  - id: embedding_similarity
    position: [1080, 500]
    size: [680, 140]
    role: processing_stage
    label: "Embedding Similarity"

  - id: content_id
    position: [1080, 680]
    size: [680, 140]
    role: processing_stage
    label: "Content ID Systems"

  - id: tda_to_musical
    from: training_time_panel
    to: musical_ai
    type: arrow
    label: "tda_provider_integration -> musical_ai_partnership"

  - id: content_to_sureel
    from: post_hoc_panel
    to: sureel_ai
    type: arrow
    label: "content_id_system -> sureel_ai_partnership"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Training-Time panel | `content_area` | Left panel: approaches requiring model training access |
| Post-Hoc panel | `content_area` | Right panel: approaches working on any model output |
| Musical AI | `decision_point` | $6M funding, Fairly Trained certified, data influence functions |
| Fairly Trained badge | `selected_option` | Certification indicator within Musical AI |
| Data influence functions | `processing_stage` | Traces which training examples influenced each output |
| Model access constraint | `callout_bar` | Requirement for model training pipeline integration |
| Sureel AI | `decision_point` | Audio fingerprinting, 86-90% claimed accuracy, 5 patents, STIM partner |
| Embedding similarity | `processing_stage` | Vector distance, handles transformations, lower precision |
| Content ID systems | `processing_stage` | Fingerprint matching, works on copies, post-hoc only |
| Trade-off axis | `data_flow` | Accuracy vs integration effort continuum |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| tda_provider_integration | Musical AI | arrow | "strong influence" |
| content_id_system | Sureel AI | arrow | "moderate influence" |
| Training-Time | Trade-off axis left | arrow | "higher accuracy, higher effort" |
| Post-Hoc | Trade-off axis right | arrow | "lower effort, lower accuracy" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "MODEL ACCESS REQUIRED" | Training-time attribution requires integration during the model training pipeline -- not possible for closed-source models | bottom of left panel |
| "ACCURACY CLAIMS" | Sureel's 86-90% accuracy is CLAIMED, not independently verified -- caveat required | right panel inset |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Training-Time Attribution"
- Label 2: "Post-Hoc Attribution"
- Label 3: "Musical AI ($6M funded)"
- Label 4: "Sureel AI (86-90% claimed)"
- Label 5: "Data Influence Functions"
- Label 6: "Embedding Similarity"
- Label 7: "Content ID Systems"

### Caption (for embedding in documentation)

Training-time attribution (Musical AI) provides highest accuracy by tracing data influence during model training, while post-hoc approaches (Sureel fingerprinting, embedding similarity) trade accuracy for broader applicability to any model output.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `decision_point`, `processing_stage`, `content_area` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" may appear as this is L3 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Musical AI has $6M funding, is Fairly Trained certified. Do NOT fabricate additional funding amounts or certifications.
10. Sureel claims 86-90% accuracy (CLAIMED, not independently verified), has 5 patents pending, partnered with STIM. Always mark accuracy as CLAIMED.
11. PRD nodes: tda_provider_integration -> musical_ai_partnership (strong influence), content_id_system -> sureel_ai_partnership (moderate).
12. Do NOT claim specific accuracy numbers for embedding similarity or content ID approaches -- only Sureel has a claimed figure.
13. Do NOT imply the scaffold currently integrates with Musical AI or Sureel -- these are expansion nodes.

## Alt Text

TDA provider landscape: training-time vs post-hoc attribution approaches compared

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-04",
    "title": "TDA Provider Landscape",
    "audience": "L3",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Training-time attribution requires model access but offers higher accuracy; post-hoc works on any output with lower accuracy.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Training-Time Panel",
        "role": "content_area",
        "is_highlighted": true,
        "labels": ["TRAINING-TIME", "Requires model access"]
      },
      {
        "name": "Musical AI",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["Musical AI", "$6M funded", "Fairly Trained"]
      },
      {
        "name": "Post-Hoc Panel",
        "role": "content_area",
        "is_highlighted": true,
        "labels": ["POST-HOC", "Works on any output"]
      },
      {
        "name": "Sureel AI",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["Sureel AI", "86-90% claimed", "5 patents"]
      },
      {
        "name": "Embedding Similarity",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Embedding Similarity", "Vector distance"]
      },
      {
        "name": "Content ID Systems",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Content ID", "Fingerprint matching"]
      }
    ],
    "relationships": [
      {
        "from": "tda_provider_integration",
        "to": "Musical AI",
        "type": "arrow",
        "label": "strong influence"
      },
      {
        "from": "content_id_system",
        "to": "Sureel AI",
        "type": "arrow",
        "label": "moderate influence"
      }
    ],
    "callout_boxes": [
      {
        "heading": "MODEL ACCESS REQUIRED",
        "body_text": "Training-time attribution requires integration during model training pipeline",
        "position": "bottom-left"
      },
      {
        "heading": "ACCURACY CLAIMS",
        "body_text": "Sureel's 86-90% is CLAIMED, not independently verified",
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
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
