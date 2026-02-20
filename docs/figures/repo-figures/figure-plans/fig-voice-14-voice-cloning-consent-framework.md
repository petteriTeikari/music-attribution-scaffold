# fig-voice-14: Voice Cloning Consent: PRAC3 -> A0-A3 Mapping

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-14 |
| **Title** | Voice Cloning Consent: PRAC3 -> A0-A3 Mapping |
| **Audience** | L2 (Technical Manager) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Map the PRAC3 voice cloning consent dimensions to the project's A0-A3 assurance levels, showing how voice consent is not a binary checkbox but a spectrum of provenance. Answers: "How do the six PRAC3 consent dimensions (Privacy, Reputation, Accountability, Consent, Credit, Compensation) map onto our assurance levels, and what does each level guarantee?"

## Key Message

Voice cloning consent requires six dimensions (PRAC3: Privacy, Reputation, Accountability, Consent, Credit, Compensation) that map onto a spectrum from A0 (no provenance, gray) through A1 (basic consent, amber) and A2 (multi-factor verification, blue) to A3 (artist-verified voice print, green). Consent is not a checkbox -- it is a spectrum.

## Visual Concept

Flowchart layout (Template C). Left side: six PRAC3 dimension boxes arranged vertically (Privacy, Reputation, Accountability, Consent, Credit, Compensation). Right side: four assurance level boxes in a horizontal progression A0 -> A1 -> A2 -> A3, each with its semantic color indicator and description. Flow arrows from PRAC3 dimensions map to appropriate assurance levels (some dimensions map to multiple levels). Bottom callout: "CONSENT IS NOT A CHECKBOX -- IT'S A SPECTRUM."

```
+-------------------------------------------------------------------+
|  VOICE CLONING CONSENT                                     [sq]   |
|  PRAC3 -> A0-A3 MAPPING                                          |
+-------------------------------------------------------------------+
|                                                                   |
|  PRAC3 DIMENSIONS               ASSURANCE LEVELS                  |
|                                                                   |
|  ┌──────────────┐               ┌──────────────────────────────┐ |
|  │ P  Privacy   │──────────┐    │ A0: NO PROVENANCE            │ |
|  └──────────────┘          │    │ No consent record            │ |
|  ┌──────────────┐          │    │ No voice print               │ |
|  │ R  Reputation│────┐     │    │ [gray]                       │ |
|  └──────────────┘    │     └──>└──────────────────────────────┘ |
|  ┌──────────────┐    │              │                            |
|  │ A  Account-  │────┤         ┌──────────────────────────────┐ |
|  │    ability   │    │         │ A1: BASIC CONSENT             │ |
|  └──────────────┘    ├────────>│ Click-through consent         │ |
|  ┌──────────────┐    │         │ Usage scope recorded          │ |
|  │ C  Consent   │────┘         │ [amber]                       │ |
|  └──────────────┘              └──────────────────────────────┘ |
|  ┌──────────────┐                   │                            |
|  │ C  Credit    │────────┐    ┌──────────────────────────────┐ |
|  └──────────────┘        │    │ A2: MULTI-FACTOR VERIFIED     │ |
|  ┌──────────────┐        ├──>│ Multiple sources agree         │ |
|  │ C  Compen-   │────────┘    │ Voice print + legal consent   │ |
|  │    sation    │              │ [blue]                        │ |
|  └──────────────┘              └──────────────────────────────┘ |
|                                     │                            |
|                               ┌──────────────────────────────┐ |
|                               │ A3: ARTIST-VERIFIED           │ |
|                               │ All 6 PRAC3 dimensions met    │ |
|                               │ Artist-verified voice print   │ |
|                               │ Compensation agreement active │ |
|                               │ [green]                       │ |
|                               └──────────────────────────────┘ |
|                                                                   |
|  "CONSENT IS NOT A CHECKBOX -- IT'S A SPECTRUM"          [line]  |
+-------------------------------------------------------------------+
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
    content: "VOICE CLONING CONSENT"
    role: title

  - id: prac3_zone
    bounds: [40, 160, 600, 720]
    content: "PRAC3 DIMENSIONS"
    role: content_area

  - id: assurance_zone
    bounds: [720, 160, 1160, 720]
    content: "ASSURANCE LEVELS"
    role: content_area

  - id: callout_zone
    bounds: [40, 920, 1840, 120]
    content: "CONSENT IS NOT A CHECKBOX"
    role: callout_box

anchors:
  - id: prac3_privacy
    position: [80, 200]
    size: [480, 80]
    role: processing_stage
    label: "P Privacy"

  - id: prac3_reputation
    position: [80, 300]
    size: [480, 80]
    role: processing_stage
    label: "R Reputation"

  - id: prac3_accountability
    position: [80, 400]
    size: [480, 80]
    role: processing_stage
    label: "A Accountability"

  - id: prac3_consent
    position: [80, 500]
    size: [480, 80]
    role: processing_stage
    label: "C Consent"

  - id: prac3_credit
    position: [80, 600]
    size: [480, 80]
    role: processing_stage
    label: "C Credit"

  - id: prac3_compensation
    position: [80, 700]
    size: [480, 80]
    role: processing_stage
    label: "C Compensation"

  - id: level_a0
    position: [760, 180]
    size: [1080, 140]
    role: assurance_none
    label: "A0: NO PROVENANCE"

  - id: level_a1
    position: [760, 340]
    size: [1080, 140]
    role: assurance_low
    label: "A1: BASIC CONSENT"

  - id: level_a2
    position: [760, 500]
    size: [1080, 140]
    role: assurance_medium
    label: "A2: MULTI-FACTOR VERIFIED"

  - id: level_a3
    position: [760, 660]
    size: [1080, 140]
    role: assurance_high
    label: "A3: ARTIST-VERIFIED"

  - id: flow_privacy_to_a0
    from: prac3_privacy
    to: level_a0
    type: arrow
    label: "no privacy controls"

  - id: flow_consent_to_a1
    from: prac3_consent
    to: level_a1
    type: arrow
    label: "click-through consent"

  - id: flow_reputation_to_a1
    from: prac3_reputation
    to: level_a1
    type: arrow
    label: "basic scope"

  - id: flow_accountability_to_a2
    from: prac3_accountability
    to: level_a2
    type: arrow
    label: "verified identity"

  - id: flow_credit_to_a2
    from: prac3_credit
    to: level_a2
    type: arrow
    label: "attribution recorded"

  - id: flow_compensation_to_a3
    from: prac3_compensation
    to: level_a3
    type: arrow
    label: "active agreement"

  - id: flow_a0_to_a1
    from: level_a0
    to: level_a1
    type: arrow
    label: "add consent"

  - id: flow_a1_to_a2
    from: level_a1
    to: level_a2
    type: arrow
    label: "add verification"

  - id: flow_a2_to_a3
    from: level_a2
    to: level_a3
    type: arrow
    label: "add artist verification"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Privacy (P) | `processing_stage` | PRAC3 dimension: control over personal voice data, usage boundaries |
| Reputation (R) | `processing_stage` | PRAC3 dimension: protection against misuse that damages artist reputation |
| Accountability (A) | `processing_stage` | PRAC3 dimension: traceable chain of who authorized voice usage |
| Consent (C1) | `processing_stage` | PRAC3 dimension: explicit, informed consent for voice cloning |
| Credit (C2) | `processing_stage` | PRAC3 dimension: proper attribution when voice is used |
| Compensation (C3) | `processing_stage` | PRAC3 dimension: fair payment for voice usage rights |
| A0: No Provenance | `assurance_none` | No consent record, no voice print, no attribution -- gray |
| A1: Basic Consent | `assurance_low` | Click-through consent, usage scope recorded -- amber |
| A2: Multi-Factor Verified | `assurance_medium` | Multiple sources agree, voice print + legal consent -- blue |
| A3: Artist-Verified | `assurance_high` | All 6 PRAC3 dimensions met, artist-verified voice print, active compensation -- green |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Privacy | A0: No Provenance | arrow | "absence = A0" |
| Consent | A1: Basic Consent | arrow | "click-through consent" |
| Reputation | A1: Basic Consent | arrow | "basic scope recording" |
| Accountability | A2: Multi-Factor Verified | arrow | "verified identity" |
| Credit | A2: Multi-Factor Verified | arrow | "attribution recorded" |
| Compensation | A3: Artist-Verified | arrow | "active agreement" |
| A0 | A1 | arrow | "add consent" |
| A1 | A2 | arrow | "add verification" |
| A2 | A3 | arrow | "add artist verification" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "CONSENT IS NOT A CHECKBOX -- IT'S A SPECTRUM" | Voice cloning consent requires six dimensions (PRAC3) that progressively build from no provenance (A0) through basic consent (A1) and multi-factor verification (A2) to full artist-verified voice prints with active compensation (A3). | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "P PRIVACY"
- Label 2: "R REPUTATION"
- Label 3: "A ACCOUNTABILITY"
- Label 4: "C CONSENT"
- Label 5: "C CREDIT"
- Label 6: "C COMPENSATION"
- Label 7: "A0: NO PROVENANCE"
- Label 8: "A1: BASIC CONSENT"
- Label 9: "A2: MULTI-FACTOR VERIFIED"
- Label 10: "A3: ARTIST-VERIFIED"
- Label 11: "No consent record"
- Label 12: "Click-through consent"
- Label 13: "Voice print + legal"
- Label 14: "All 6 PRAC3 dimensions"
- Label 15: "Artist-verified voice print"
- Label 16: "Compensation active"

### Caption (for embedding in documentation)

Flowchart mapping PRAC3 voice cloning consent dimensions (Privacy, Reputation, Accountability, Consent, Credit, Compensation) to A0-A3 assurance levels, showing consent as a spectrum from no provenance to artist-verified voice prints.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `assurance_none`, `assurance_low`, `assurance_medium`, `assurance_high` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PRAC3 stands for Privacy, Reputation, Accountability, Consent, Credit, Compensation -- this is the voice cloning ethics framework. Do not expand the acronym differently.
10. A0-A3 are the project's assurance levels defined in the companion paper (Teikari 2026). Do not invent additional levels.
11. A0 is gray (no provenance), A1 is amber (basic consent), A2 is blue (multi-factor verified), A3 is green (artist-verified). Use the project's semantic color tokens for these.
12. The mapping from PRAC3 to A0-A3 is conceptual -- not all six dimensions map one-to-one to a single level. Show that multiple dimensions contribute to higher levels.
13. A3 requires ALL six PRAC3 dimensions to be satisfied -- it is the union, not the intersection.
14. Do NOT present A0 as morally wrong -- it simply represents the absence of provenance, which is the current default state for most voice synthesis.
15. The flow from A0 to A3 should feel progressive and achievable, not punitive.

## Alt Text

Flowchart mapping six PRAC3 voice cloning consent dimensions (Privacy, Reputation, Accountability, Consent, Credit, Compensation) to A0-A3 music attribution assurance levels, showing voice consent as a progressive spectrum from no provenance to artist-verified voice prints.

## Image Embed

![Flowchart mapping six PRAC3 voice cloning consent dimensions (Privacy, Reputation, Accountability, Consent, Credit, Compensation) to A0-A3 music attribution assurance levels, showing voice consent as a progressive spectrum from no provenance to artist-verified voice prints.](docs/figures/repo-figures/assets/fig-voice-14-voice-cloning-consent-framework.jpg)

*Flowchart mapping PRAC3 voice cloning consent dimensions (Privacy, Reputation, Accountability, Consent, Credit, Compensation) to A0-A3 assurance levels, showing consent as a spectrum from no provenance to artist-verified voice prints.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-14",
    "title": "Voice Cloning Consent: PRAC3 -> A0-A3 Mapping",
    "audience": "L2",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "Voice cloning consent requires six PRAC3 dimensions mapping progressively from A0 (no provenance) to A3 (artist-verified voice print with compensation).",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "PRAC3 Dimensions",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["P Privacy", "R Reputation", "A Accountability", "C Consent", "C Credit", "C Compensation"]
      },
      {
        "name": "A0: No Provenance",
        "role": "assurance_none",
        "is_highlighted": false,
        "labels": ["A0", "No consent record", "No voice print"]
      },
      {
        "name": "A1: Basic Consent",
        "role": "assurance_low",
        "is_highlighted": false,
        "labels": ["A1", "Click-through consent", "Usage scope recorded"]
      },
      {
        "name": "A2: Multi-Factor Verified",
        "role": "assurance_medium",
        "is_highlighted": true,
        "labels": ["A2", "Multiple sources agree", "Voice print + legal consent"]
      },
      {
        "name": "A3: Artist-Verified",
        "role": "assurance_high",
        "is_highlighted": true,
        "labels": ["A3", "All 6 PRAC3 dimensions", "Artist-verified voice print", "Compensation active"]
      }
    ],
    "relationships": [
      {
        "from": "Privacy",
        "to": "A0",
        "type": "arrow",
        "label": "absence = A0"
      },
      {
        "from": "Consent",
        "to": "A1",
        "type": "arrow",
        "label": "click-through"
      },
      {
        "from": "Accountability",
        "to": "A2",
        "type": "arrow",
        "label": "verified identity"
      },
      {
        "from": "Compensation",
        "to": "A3",
        "type": "arrow",
        "label": "active agreement"
      },
      {
        "from": "A0",
        "to": "A1",
        "type": "arrow",
        "label": "add consent"
      },
      {
        "from": "A1",
        "to": "A2",
        "type": "arrow",
        "label": "add verification"
      },
      {
        "from": "A2",
        "to": "A3",
        "type": "arrow",
        "label": "add artist verification"
      }
    ],
    "callout_boxes": [
      {
        "heading": "CONSENT IS NOT A CHECKBOX -- IT'S A SPECTRUM",
        "body_text": "Six PRAC3 dimensions progressively build from no provenance to full artist-verified voice prints.",
        "position": "bottom-center"
      }
    ]
  }
}
```

## Quality Checklist

- [ ] Primary message clear in one sentence
- [ ] Semantic tags used (no colors, hex codes, or font names in content spec)
- [ ] ASCII layout sketched
- [ ] Spatial anchors defined in YAML
- [ ] Labels under 30 characters
- [ ] Anti-hallucination rules listed
- [ ] Alt text provided (125 chars max)
- [ ] JSON export block included
- [ ] Audience level correct (L2)
- [ ] Layout template identified (C)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
