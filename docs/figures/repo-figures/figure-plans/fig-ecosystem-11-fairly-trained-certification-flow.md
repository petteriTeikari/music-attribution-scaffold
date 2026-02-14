# fig-ecosystem-11: Fairly Trained Certification Flow

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-11 |
| **Title** | Fairly Trained Certification Flow |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:10 |
| **Layout Template** | E (Steps/Vertical) |

## Purpose

Shows the Fairly Trained certification process as a binary market signal achieved through third-party audit, and how it complements the scaffold's graduated A0-A3 assurance levels. Answers: "How does external certification layer onto internal confidence scoring?"

## Key Message

Fairly Trained provides a binary certified/not-certified market signal via third-party training data audit -- complementing the scaffold's graduated A0-A3 assurance levels with an external trust anchor.

## Visual Concept

Four vertical stages descending from top to bottom, each representing a step in the certification flow. The final stage shows the certified badge displayed alongside A0-A3 scores in the scaffold UI, making clear that binary certification and graduated assurance are complementary -- not competing -- signals.

```
+---------------------------------------------------------------+
|  FAIRLY TRAINED CERTIFICATION FLOW                             |
|  -- Binary Market Signal via Third-Party Audit                 |
+---------------------------------------------------------------+
|                                                                |
|  I. APPLICATION                                                |
|  ┌─────────────────────────────────────────────────────┐      |
|  │  Company submits training data documentation         │      |
|  │  Provenance records, licensing agreements            │      |
|  │  Data sourcing methodology                           │      |
|  └──────────────────────┬──────────────────────────────┘      |
|                         │                                      |
|                         ▼                                      |
|  II. AUDIT                                                     |
|  ┌─────────────────────────────────────────────────────┐      |
|  │  Third-party review of data provenance               │      |
|  │  Independent assessment of training data practices    │      |
|  │  No partial credit -- pass or fail                   │      |
|  └──────────────────────┬──────────────────────────────┘      |
|                         │                                      |
|                    ┌────┴────┐                                 |
|                    ▼         ▼                                 |
|  III. CERTIFICATION (binary outcome)                           |
|  ┌─────────────┐    ┌──────────────┐                          |
|  │  CERTIFIED  │    │  DENIED      │                          |
|  │  ■ Badge    │    │  No badge    │                          |
|  └──────┬──────┘    └──────────────┘                          |
|         │                                                      |
|         ▼                                                      |
|  IV. DISPLAY IN SCAFFOLD                                       |
|  ┌─────────────────────────────────────────────────────┐      |
|  │  Fairly Trained badge shown alongside A0-A3 scores   │      |
|  │  Binary signal ◄────► Graduated confidence           │      |
|  │  External trust anchor + internal provenance         │      |
|  └─────────────────────────────────────────────────────┘      |
|                                                                |
+---------------------------------------------------------------+
|  19 certified entities: 12 company + 2 product + 5 model       |
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
    content: "FAIRLY TRAINED CERTIFICATION FLOW"
    role: title

  - id: stage_i_zone
    bounds: [120, 160, 1680, 180]
    role: content_area

  - id: stage_ii_zone
    bounds: [120, 380, 1680, 180]
    role: content_area

  - id: stage_iii_zone
    bounds: [120, 600, 1680, 180]
    role: content_area

  - id: stage_iv_zone
    bounds: [120, 830, 1680, 200]
    role: content_area

  - id: footer_zone
    bounds: [120, 1070, 1680, 80]
    role: callout_box

anchors:
  - id: stage_i
    position: [960, 250]
    size: [1500, 140]
    role: processing_stage
    label: "I. APPLICATION"

  - id: stage_ii
    position: [960, 470]
    size: [1500, 140]
    role: processing_stage
    label: "II. AUDIT"

  - id: certified_outcome
    position: [600, 690]
    size: [500, 120]
    role: confidence_high
    label: "CERTIFIED"

  - id: denied_outcome
    position: [1200, 690]
    size: [500, 120]
    role: confidence_low
    label: "DENIED"

  - id: stage_iv
    position: [960, 930]
    size: [1500, 160]
    role: processing_stage
    label: "IV. DISPLAY IN SCAFFOLD"

  - id: flow_i_to_ii
    from: stage_i
    to: stage_ii
    type: arrow
    label: "submit documentation"

  - id: flow_ii_to_certified
    from: stage_ii
    to: certified_outcome
    type: arrow
    label: "pass"

  - id: flow_ii_to_denied
    from: stage_ii
    to: denied_outcome
    type: arrow
    label: "fail"

  - id: flow_certified_to_iv
    from: certified_outcome
    to: stage_iv
    type: arrow
    label: "badge displayed"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "FAIRLY TRAINED CERTIFICATION FLOW" with coral accent square |
| Stage I -- Application | `processing_stage` | Company submits training data documentation, provenance records |
| Stage II -- Audit | `processing_stage` | Third-party independent review, no partial credit |
| Certified outcome | `confidence_high` | Binary positive: badge granted |
| Denied outcome | `confidence_low` | Binary negative: no badge |
| Stage IV -- Display | `processing_stage` | Badge shown alongside A0-A3 assurance scores in scaffold UI |
| Footer stats | `data_mono` | "19 certified entities: 12 company + 2 product + 5 model" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Application | Audit | arrow | "submit documentation" |
| Audit | Certified | arrow | "pass" |
| Audit | Denied | arrow | "fail" |
| Certified | Display | arrow | "badge displayed alongside A0-A3" |
| regulatory_posture (parent) | fairly_trained_certification | dashed | "moderate influence" |
| compliance_framework_mapping (parent) | fairly_trained_certification | dashed | "moderate influence" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "BINARY SIGNAL" | Fairly Trained is pass/fail -- no partial credit, no graduated tiers | right-margin |
| "COMPLEMENTARY" | Binary certification + graduated A0-A3 = stronger trust signal than either alone | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "APPLICATION"
- Label 2: "AUDIT"
- Label 3: "CERTIFIED"
- Label 4: "DENIED"
- Label 5: "DISPLAY IN SCAFFOLD"
- Label 6: "Binary market signal"
- Label 7: "A0-A3 graduated confidence"

### Caption (for embedding in documentation)

Fairly Trained certification provides a binary certified/not-certified market signal via independent third-party training data audit, complementing the scaffold's graduated A0-A3 assurance levels with an external trust anchor. Founded by Ed Newton-Rex, 19 entities certified to date.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `confidence_high`, `confidence_low` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PRD node: `fairly_trained_certification`. This is the decision node driving this figure.
10. Parent nodes: `regulatory_posture` (moderate), `compliance_framework_mapping` (moderate).
11. Fairly Trained was founded by Ed Newton-Rex (former VP Audio at Stability AI).
12. 19 certified entities as of latest data: 12 company + 2 product + 5 model certifications.
13. Certification is BINARY -- no partial credit, no graduated scoring. Pass or fail only.
14. Do NOT imply the scaffold is currently certified by Fairly Trained -- it is not.
15. The scaffold's A0-A3 assurance levels are internal; Fairly Trained is an external trust anchor.
16. Do NOT render Ed Newton-Rex's name in the figure unless specifically needed for context.

## Alt Text

Fairly Trained certification: binary audit signal complementing A0-A3 assurance levels

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-11",
    "title": "Fairly Trained Certification Flow",
    "audience": "L2",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Fairly Trained provides a binary certified/not-certified market signal via third-party training data audit -- complementing the scaffold's graduated A0-A3 assurance levels with an external trust anchor.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Stage I -- Application",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["APPLICATION", "Training data docs"]
      },
      {
        "name": "Stage II -- Audit",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["AUDIT", "Third-party review"]
      },
      {
        "name": "Certified Outcome",
        "role": "confidence_high",
        "is_highlighted": true,
        "labels": ["CERTIFIED", "Badge granted"]
      },
      {
        "name": "Denied Outcome",
        "role": "confidence_low",
        "is_highlighted": false,
        "labels": ["DENIED", "No badge"]
      },
      {
        "name": "Stage IV -- Display",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["DISPLAY IN SCAFFOLD", "Badge + A0-A3"]
      }
    ],
    "relationships": [
      {
        "from": "Application",
        "to": "Audit",
        "type": "arrow",
        "label": "submit documentation"
      },
      {
        "from": "Audit",
        "to": "Certified",
        "type": "arrow",
        "label": "pass"
      },
      {
        "from": "Audit",
        "to": "Denied",
        "type": "arrow",
        "label": "fail"
      },
      {
        "from": "Certified",
        "to": "Display",
        "type": "arrow",
        "label": "badge displayed alongside A0-A3"
      }
    ],
    "callout_boxes": [
      {
        "heading": "BINARY SIGNAL",
        "body_text": "Fairly Trained is pass/fail -- no partial credit, no graduated tiers",
        "position": "right-margin"
      },
      {
        "heading": "COMPLEMENTARY",
        "body_text": "Binary certification + graduated A0-A3 = stronger trust signal than either alone",
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
- [x] Audience level correct (L2)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
