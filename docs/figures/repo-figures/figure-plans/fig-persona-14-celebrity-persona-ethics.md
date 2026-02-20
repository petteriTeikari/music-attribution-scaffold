# fig-persona-14: Celebrity Persona Ethics Decision Flow

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-14 |
| **Title** | Celebrity Persona Ethics: Consent-First Decision Flowchart |
| **Audience** | L1 (Music Industry Professional) |
| **Location** | docs/knowledge-base/, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Provides a clear decision flowchart for determining whether an AI celebrity persona meets ethical and legal requirements. The flow begins with consent as the gate and progresses through PRAC3 dimensions (Privacy, Rights, Authenticity, Compensation, Consent, Control). Answers: "When is it acceptable to create an AI persona based on a real artist?"

## Key Message

Celebrity AI personas require affirmative consent as the first gate, followed by all six PRAC3 dimensions -- without consent, the only acceptable path is A0 (no provenance claim).

## Visual Concept

Top-down flowchart beginning with a single decision diamond: "Does the person consent?" The "No" branch terminates immediately at a STOP block with "A0 ONLY -- no persona claim." The "Yes" branch cascades through four sequential decision gates: "Active compensation model?", "Usage scope defined?", "Revocation mechanism?", and final PRAC3 checkpoint. Each gate maps to PRAC3 dimensions shown as sidebar annotations. The successful path terminates at "A3 APPROVED."

```
+-----------------------------------------------------------------------+
|  CELEBRITY PERSONA ETHICS                                              |
|  -- Consent-First Decision Flowchart                                   |
+-----------------------------------------------------------------------+
|                                                                        |
|                    ┌─────────────────────┐                             |
|                    │  DOES THE PERSON     │                             |
|                    │  CONSENT?            │                             |
|                    └──────────┬──────────┘                             |
|                       ┌──────┴──────┐                                  |
|                       │             │                                  |
|                      YES           NO                                  |
|                       │             │                                  |
|                       ▼             ▼                                  |
|                       │      ┌──────────────┐                          |
|                       │      │    STOP       │                          |
|                       │      │  A0 ONLY      │   PRAC3 DIMENSIONS      |
|                       │      │  No persona   │   ──────────────        |
|                       │      │  claim        │                         |
|                       │      └──────────────┘   P  Privacy             |
|                       ▼                         R  Rights              |
|              ┌─────────────────┐                A  Authenticity        |
|              │ ACTIVE           │                C  Compensation        |
|              │ COMPENSATION?    │◄──── C        C  Consent             |
|              └────────┬────────┘                C  Control             |
|                       │ Yes                                            |
|                       ▼                                                |
|              ┌─────────────────┐                                       |
|              │ USAGE SCOPE     │                                       |
|              │ DEFINED?        │◄──── R, P                             |
|              └────────┬────────┘                                       |
|                       │ Yes                                            |
|                       ▼                                                |
|              ┌─────────────────┐                                       |
|              │ REVOCATION      │                                       |
|              │ MECHANISM?      │◄──── C (Control)                      |
|              └────────┬────────┘                                       |
|                       │ Yes                                            |
|                       ▼                                                |
|              ┌─────────────────┐                                       |
|              │ AUTHENTICITY    │                                       |
|              │ GUARDRAILS?     │◄──── A                                |
|              └────────┬────────┘                                       |
|                       │ Yes                                            |
|                       ▼                                                |
|              ┌─────────────────┐                                       |
|              │   A3 APPROVED   │                                       |
|              │   All 6 PRAC3   │                                       |
|              │   dimensions    │                                       |
|              └─────────────────┘                                       |
|                                                                        |
|  -- CELEBRITY AI PERSONAS REQUIRE ALL SIX PRAC3 DIMENSIONS             |
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
    content: "CELEBRITY PERSONA ETHICS"
    role: title

  - id: flowchart_zone
    bounds: [200, 140, 1200, 780]
    content: "Decision flowchart"
    role: content_area

  - id: prac3_sidebar
    bounds: [1480, 200, 380, 500]
    content: "PRAC3 dimension legend"
    role: content_area

  - id: callout_zone
    bounds: [80, 940, 1760, 100]
    content: "CELEBRITY AI PERSONAS REQUIRE ALL SIX PRAC3 DIMENSIONS"
    role: callout_box

anchors:
  - id: consent_gate
    position: [600, 180]
    size: [320, 100]
    role: decision_point
    label: "DOES THE PERSON CONSENT?"

  - id: no_branch
    position: [1000, 320]
    size: [240, 120]
    role: confidence_low
    label: "STOP -- A0 ONLY"

  - id: compensation_gate
    position: [600, 360]
    size: [320, 80]
    role: decision_point
    label: "ACTIVE COMPENSATION?"

  - id: scope_gate
    position: [600, 480]
    size: [320, 80]
    role: decision_point
    label: "USAGE SCOPE DEFINED?"

  - id: revocation_gate
    position: [600, 600]
    size: [320, 80]
    role: decision_point
    label: "REVOCATION MECHANISM?"

  - id: authenticity_gate
    position: [600, 720]
    size: [320, 80]
    role: decision_point
    label: "AUTHENTICITY GUARDRAILS?"

  - id: approved
    position: [600, 840]
    size: [320, 80]
    role: confidence_high
    label: "A3 APPROVED"

  - id: consent_to_no
    from: consent_gate
    to: no_branch
    type: arrow
    label: "No"

  - id: consent_to_compensation
    from: consent_gate
    to: compensation_gate
    type: arrow
    label: "Yes"

  - id: compensation_to_scope
    from: compensation_gate
    to: scope_gate
    type: arrow
    label: "Yes"

  - id: scope_to_revocation
    from: scope_gate
    to: revocation_gate
    type: arrow
    label: "Yes"

  - id: revocation_to_authenticity
    from: revocation_gate
    to: authenticity_gate
    type: arrow
    label: "Yes"

  - id: authenticity_to_approved
    from: authenticity_gate
    to: approved
    type: arrow
    label: "Yes"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Consent gate | `decision_point` | First and most critical gate: "Does the person consent?" |
| STOP block | `confidence_low` | Terminal for No path: A0 only, no persona claim permitted |
| Compensation gate | `decision_point` | PRAC3 Compensation dimension: active compensation model in place? |
| Scope gate | `decision_point` | PRAC3 Rights + Privacy: usage scope clearly defined and bounded? |
| Revocation gate | `decision_point` | PRAC3 Control: mechanism for artist to revoke at any time? |
| Authenticity gate | `decision_point` | PRAC3 Authenticity: guardrails preventing misrepresentation? |
| A3 Approved block | `confidence_high` | Terminal for successful path: all six PRAC3 dimensions satisfied |
| PRAC3 sidebar | `content_area` | Legend explaining all six PRAC3 dimensions |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Consent gate | STOP block | arrow | "No" |
| Consent gate | Compensation gate | arrow | "Yes" |
| Compensation gate | Scope gate | arrow | "Yes" |
| Scope gate | Revocation gate | arrow | "Yes" |
| Revocation gate | Authenticity gate | arrow | "Yes" |
| Authenticity gate | A3 Approved | arrow | "Yes" |
| PRAC3 sidebar | Each gate | dashed | "dimension mapping" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "CONSENT IS THE GATE" | "CELEBRITY AI PERSONAS REQUIRE ALL SIX PRAC3 DIMENSIONS" | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "DOES THE PERSON CONSENT?"
- Label 2: "STOP -- A0 ONLY"
- Label 3: "ACTIVE COMPENSATION?"
- Label 4: "USAGE SCOPE DEFINED?"
- Label 5: "REVOCATION MECHANISM?"
- Label 6: "AUTHENTICITY GUARDRAILS?"
- Label 7: "A3 APPROVED"
- Label 8: "P -- Privacy"
- Label 9: "R -- Rights"
- Label 10: "A -- Authenticity"
- Label 11: "C -- Compensation"
- Label 12: "C -- Consent"
- Label 13: "C -- Control"

### Caption (for embedding in documentation)

Decision flowchart for celebrity AI persona ethics: consent gates the entire flow, followed by PRAC3 dimension checkpoints for compensation, scope, revocation, and authenticity -- without consent, only A0 (no provenance claim) is permitted.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `decision_point`, `confidence_low`, `confidence_high` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear. This is L1 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PRAC3 stands for Privacy, Rights, Authenticity, Compensation, Consent, Control. Do NOT alter or reorder these dimensions.
10. Consent is the FIRST gate. Do NOT place any decision before consent.
11. The "No" path from consent must terminate IMMEDIATELY at STOP/A0. Do NOT add intermediate steps on the No path.
12. A3 is the assurance level for artist-verified attribution. Do NOT use A3 to mean anything else.
13. A0 means "no provenance data" -- it is the only acceptable level when consent is absent.
14. Each gate on the Yes path maps to specific PRAC3 dimensions. Do NOT shuffle the mappings.
15. This is L1 audience: use "trust level" language, not technical jargon. Keep all labels in plain business English.

## Alt Text

Consent-first decision flowchart for celebrity AI persona ethics showing PRAC3 dimension checkpoints -- Privacy, Rights, Authenticity, Compensation, Consent, Control -- gating progression from consent to A3 artist-verified approval for music attribution.

## Image Embed

![Consent-first decision flowchart for celebrity AI persona ethics showing PRAC3 dimension checkpoints -- Privacy, Rights, Authenticity, Compensation, Consent, Control -- gating progression from consent to A3 artist-verified approval for music attribution.](docs/figures/repo-figures/assets/fig-persona-14-celebrity-persona-ethics.jpg)

*Decision flowchart for celebrity AI persona ethics: consent gates the entire flow, followed by PRAC3 dimension checkpoints for compensation, scope, revocation, and authenticity -- without consent, only A0 (no provenance claim) is permitted.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-14",
    "title": "Celebrity Persona Ethics: Consent-First Decision Flowchart",
    "audience": "L1",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "Celebrity AI personas require consent as the first gate, then all six PRAC3 dimensions for A3 approval.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Consent Gate",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["DOES THE PERSON CONSENT?"]
      },
      {
        "name": "STOP Block",
        "role": "confidence_low",
        "is_highlighted": true,
        "labels": ["STOP -- A0 ONLY", "No persona claim"]
      },
      {
        "name": "Compensation Gate",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["ACTIVE COMPENSATION?", "PRAC3: Compensation"]
      },
      {
        "name": "Scope Gate",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["USAGE SCOPE DEFINED?", "PRAC3: Rights, Privacy"]
      },
      {
        "name": "Revocation Gate",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["REVOCATION MECHANISM?", "PRAC3: Control"]
      },
      {
        "name": "Authenticity Gate",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["AUTHENTICITY GUARDRAILS?", "PRAC3: Authenticity"]
      },
      {
        "name": "A3 Approved",
        "role": "confidence_high",
        "is_highlighted": true,
        "labels": ["A3 APPROVED", "All 6 PRAC3 dimensions"]
      }
    ],
    "relationships": [
      {
        "from": "Consent Gate",
        "to": "STOP Block",
        "type": "arrow",
        "label": "No -- immediate termination"
      },
      {
        "from": "Consent Gate",
        "to": "Compensation Gate",
        "type": "arrow",
        "label": "Yes -- proceed to PRAC3 checks"
      },
      {
        "from": "Compensation Gate",
        "to": "A3 Approved",
        "type": "arrow",
        "label": "Yes through all gates"
      }
    ],
    "callout_boxes": [
      {
        "heading": "CONSENT IS THE GATE",
        "body_text": "CELEBRITY AI PERSONAS REQUIRE ALL SIX PRAC3 DIMENSIONS",
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
- [x] Audience level correct (L1)
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
