# fig-voice-29: Voice Rights Stack: PRAC3 Meets Attribution

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-29 |
| **Title** | Voice Rights Stack: PRAC3 Meets Attribution |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Map the PRAC3 voice rights framework (Privacy, Reputation, Accountability, Consent, Credit, Compensation) to concrete music attribution implementations. Shows how each PRAC3 dimension translates to a specific technical mechanism in the scaffold, then maps the complete stack to the A0-A3 assurance levels. Answers: "How does the voice rights framework connect to the attribution system we are building?"

## Key Message

The PRAC3 framework provides six dimensions for voice rights that map directly to music attribution infrastructure: Privacy to encryption, Reputation to deepfake detection, Accountability to C2PA provenance, Consent to MCP permission queries, Credit to ISRC/ISWC metadata, and Compensation to royalty tracking. This extends the attribution-by-design principle from text/metadata to audio.

## Visual Concept

Flowchart (Template C) with two columns. Left column lists the six PRAC3 dimensions as source nodes. Right column shows the corresponding music attribution implementation for each. Arrows connect each PRAC3 dimension to its implementation. Below the mapping, a horizontal bar shows the A0-A3 assurance levels that the combined stack enables.

```
+-------------------------------------------------------------------+
|  VOICE RIGHTS STACK                                          [sq]   |
|  PRAC3 MEETS ATTRIBUTION                                          |
+-------------------------------------------------------------------+
|                                                                    |
|  PRAC3 DIMENSION              ATTRIBUTION IMPLEMENTATION           |
|  ────────────────              ──────────────────────────           |
|                                                                    |
|  ┌────────────────┐    ──>    ┌──────────────────────────┐        |
|  │  P  PRIVACY    │           │ Voice data encryption +   │        |
|  │                │           │ retention limits (90 day) │        |
|  └────────────────┘           └──────────────────────────┘        |
|                                                                    |
|  ┌────────────────┐    ──>    ┌──────────────────────────┐        |
|  │  R  REPUTATION │           │ Deepfake detection +      │        |
|  │                │           │ brand protection           │        |
|  └────────────────┘           └──────────────────────────┘        |
|                                                                    |
|  ┌────────────────┐    ──>    ┌──────────────────────────┐        |
|  │  A  ACCOUNT-   │           │ C2PA provenance chain +   │        |
|  │     ABILITY    │           │ audit trail                │        |
|  └────────────────┘           └──────────────────────────┘        |
|                                                                    |
|  ┌────────────────┐    ──>    ┌──────────────────────────┐        |
|  │  C  CONSENT    │           │ MCP permission queries +  │        |
|  │                │           │ revocation support         │        |
|  └────────────────┘           └──────────────────────────┘        |
|                                                                    |
|  ┌────────────────┐    ──>    ┌──────────────────────────┐        |
|  │  C  CREDIT     │           │ ISRC/ISWC metadata +      │        |
|  │                │           │ attribution chain          │        |
|  └────────────────┘           └──────────────────────────┘        |
|                                                                    |
|  ┌────────────────┐    ──>    ┌──────────────────────────┐        |
|  │  C  COMPEN-    │           │ Royalty tracking +         │        |
|  │     SATION     │           │ smart contracts            │        |
|  └────────────────┘           └──────────────────────────┘        |
|                                                                    |
|  ─────────────────────────────────────────────── [accent line]     |
|                                                                    |
|  ASSURANCE LEVELS                                                  |
|  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                             |
|  │  A0  │ │  A1  │ │  A2  │ │  A3  │                             |
|  │ None │ │Single│ │Multi │ │Artist│                              |
|  │      │ │Source│ │Source│ │Verify│                               |
|  └──────┘ └──────┘ └──────┘ └──────┘                             |
|                                                                    |
+-------------------------------------------------------------------+
|  THE VOICE RIGHTS STACK EXTENDS ATTRIBUTION-BY-DESIGN TO AUDIO     |
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
    content: "VOICE RIGHTS STACK"
    role: title

  - id: mapping_zone
    bounds: [60, 140, 1800, 600]
    role: content_area

  - id: assurance_zone
    bounds: [60, 780, 1800, 120]
    role: content_area

  - id: callout_zone
    bounds: [60, 940, 1800, 100]
    content: "EXTENDS ATTRIBUTION-BY-DESIGN TO AUDIO"
    role: callout_box

anchors:
  - id: prac3_privacy
    position: [240, 200]
    size: [300, 60]
    role: processing_stage
    label: "P — PRIVACY"

  - id: prac3_reputation
    position: [240, 290]
    size: [300, 60]
    role: processing_stage
    label: "R — REPUTATION"

  - id: prac3_accountability
    position: [240, 380]
    size: [300, 60]
    role: processing_stage
    label: "A — ACCOUNTABILITY"

  - id: prac3_consent
    position: [240, 470]
    size: [300, 60]
    role: processing_stage
    label: "C — CONSENT"

  - id: prac3_credit
    position: [240, 560]
    size: [300, 60]
    role: processing_stage
    label: "C — CREDIT"

  - id: prac3_compensation
    position: [240, 650]
    size: [300, 60]
    role: processing_stage
    label: "C — COMPENSATION"

  - id: impl_privacy
    position: [900, 200]
    size: [600, 60]
    role: selected_option
    label: "Voice data encryption + retention limits"

  - id: impl_reputation
    position: [900, 290]
    size: [600, 60]
    role: selected_option
    label: "Deepfake detection + brand protection"

  - id: impl_accountability
    position: [900, 380]
    size: [600, 60]
    role: selected_option
    label: "C2PA provenance chain + audit trail"

  - id: impl_consent
    position: [900, 470]
    size: [600, 60]
    role: selected_option
    label: "MCP permission queries + revocation"

  - id: impl_credit
    position: [900, 560]
    size: [600, 60]
    role: selected_option
    label: "ISRC/ISWC metadata + attribution chain"

  - id: impl_compensation
    position: [900, 650]
    size: [600, 60]
    role: selected_option
    label: "Royalty tracking + smart contracts"

  - id: assurance_a0
    position: [240, 820]
    size: [200, 80]
    role: deferred_option
    label: "A0 — None"

  - id: assurance_a1
    position: [520, 820]
    size: [200, 80]
    role: deferred_option
    label: "A1 — Single Source"

  - id: assurance_a2
    position: [800, 820]
    size: [200, 80]
    role: processing_stage
    label: "A2 — Multi Source"

  - id: assurance_a3
    position: [1080, 820]
    size: [200, 80]
    role: selected_option
    label: "A3 — Artist Verified"

  - id: flow_privacy
    from: prac3_privacy
    to: impl_privacy
    type: arrow
    label: ""

  - id: flow_reputation
    from: prac3_reputation
    to: impl_reputation
    type: arrow
    label: ""

  - id: flow_accountability
    from: prac3_accountability
    to: impl_accountability
    type: arrow
    label: ""

  - id: flow_consent
    from: prac3_consent
    to: impl_consent
    type: arrow
    label: ""

  - id: flow_credit
    from: prac3_credit
    to: impl_credit
    type: arrow
    label: ""

  - id: flow_compensation
    from: prac3_compensation
    to: impl_compensation
    type: arrow
    label: ""
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "VOICE RIGHTS STACK" with subtitle "PRAC3 MEETS ATTRIBUTION" and coral accent square |
| Privacy row | `processing_stage` -> `selected_option` | PRAC3 Privacy mapped to voice data encryption + 90-day retention limits |
| Reputation row | `processing_stage` -> `selected_option` | PRAC3 Reputation mapped to deepfake detection + brand protection |
| Accountability row | `processing_stage` -> `selected_option` | PRAC3 Accountability mapped to C2PA provenance chain + audit trail |
| Consent row | `processing_stage` -> `selected_option` | PRAC3 Consent mapped to MCP permission queries + revocation support |
| Credit row | `processing_stage` -> `selected_option` | PRAC3 Credit mapped to ISRC/ISWC metadata + attribution chain |
| Compensation row | `processing_stage` -> `selected_option` | PRAC3 Compensation mapped to royalty tracking + smart contracts |
| A0 badge | `deferred_option` | No provenance data |
| A1 badge | `deferred_option` | Single source attestation |
| A2 badge | `processing_stage` | Multiple sources agree |
| A3 badge | `selected_option` | Artist-verified (highest assurance) |
| Accent line divider | `accent_line` | Separates mapping zone from assurance level zone |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| PRAC3 Privacy | Voice encryption | arrow | "implements" |
| PRAC3 Reputation | Deepfake detection | arrow | "implements" |
| PRAC3 Accountability | C2PA provenance | arrow | "implements" |
| PRAC3 Consent | MCP permissions | arrow | "implements" |
| PRAC3 Credit | ISRC/ISWC metadata | arrow | "implements" |
| PRAC3 Compensation | Royalty tracking | arrow | "implements" |
| All implementations | Assurance levels | dashed | "enables" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "THE VOICE RIGHTS STACK EXTENDS ATTRIBUTION-BY-DESIGN TO AUDIO" | PRAC3 provides the ethical framework; the attribution scaffold provides the technical implementation. Together they ensure voice is treated as a first-class rights-bearing medium. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "P -- PRIVACY"
- Label 2: "R -- REPUTATION"
- Label 3: "A -- ACCOUNTABILITY"
- Label 4: "C -- CONSENT"
- Label 5: "C -- CREDIT"
- Label 6: "C -- COMPENSATION"
- Label 7: "Voice encryption + retention"
- Label 8: "Deepfake detect + brand"
- Label 9: "C2PA provenance + audit"
- Label 10: "MCP permissions + revoke"
- Label 11: "ISRC/ISWC + attribution"
- Label 12: "Royalty track + contracts"
- Label 13: "A0 -- None"
- Label 14: "A1 -- Single Source"
- Label 15: "A2 -- Multi Source"
- Label 16: "A3 -- Artist Verified"

### Caption (for embedding in documentation)

Mapping of PRAC3 voice rights framework (Privacy, Reputation, Accountability, Consent, Credit, Compensation) to music attribution implementations, showing how each dimension translates to concrete technical mechanisms and maps to A0-A3 assurance levels.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `selected_option`, `deferred_option` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PRAC3 is defined in the voice AI ethics literature as Privacy, Reputation, Accountability, Consent, Credit, Compensation. These are the exact six dimensions -- do NOT add or remove any.
10. The A0-A3 assurance levels are defined in the companion paper (Teikari 2026): A0 = None, A1 = Single source, A2 = Multiple sources agree, A3 = Artist-verified. Use these exact definitions.
11. C2PA (Coalition for Content Provenance and Authenticity) is a real standard for content provenance. Do NOT confuse with C2PA-specific implementations.
12. MCP permission queries are defined in the scaffold's MCP server (`src/music_attribution/mcp/server.py`). This is existing infrastructure being extended.
13. ISRC (International Standard Recording Code) and ISWC (International Standard Musical Work Code) are real music industry identifiers. Do NOT invent others.
14. Smart contracts for compensation are an aspirational implementation -- do NOT claim they are currently built in the scaffold.
15. Deepfake detection for voice is an active research area -- do NOT claim any specific detection accuracy.
16. The 90-day retention limit for voice data is a design recommendation, not a legal requirement -- though it aligns with GDPR data minimization principles.

## Alt Text

Flowchart mapping PRAC3 voice rights framework with six dimensions -- Privacy, Reputation, Accountability, Consent, Credit, Compensation -- to concrete music attribution implementations including encryption, deepfake detection, C2PA provenance, MCP consent, and ISRC/ISWC metadata, connected to A0-A3 assurance levels.

## Image Embed

![Flowchart mapping PRAC3 voice rights framework with six dimensions -- Privacy, Reputation, Accountability, Consent, Credit, Compensation -- to concrete music attribution implementations including encryption, deepfake detection, C2PA provenance, MCP consent, and ISRC/ISWC metadata, connected to A0-A3 assurance levels.](docs/figures/repo-figures/assets/fig-voice-29-prac3-assurance-mapping.jpg)

*Mapping of PRAC3 voice rights framework (Privacy, Reputation, Accountability, Consent, Credit, Compensation) to music attribution implementations, showing how each dimension translates to concrete technical mechanisms and maps to A0-A3 assurance levels.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-29",
    "title": "Voice Rights Stack: PRAC3 Meets Attribution",
    "audience": "L2",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "PRAC3 framework maps directly to music attribution infrastructure: Privacy to encryption, Reputation to deepfake detection, Accountability to C2PA, Consent to MCP, Credit to ISRC/ISWC, Compensation to royalties.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "PRAC3 Privacy",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["P -- PRIVACY"]
      },
      {
        "name": "PRAC3 Reputation",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["R -- REPUTATION"]
      },
      {
        "name": "PRAC3 Accountability",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["A -- ACCOUNTABILITY"]
      },
      {
        "name": "PRAC3 Consent",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["C -- CONSENT"]
      },
      {
        "name": "PRAC3 Credit",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["C -- CREDIT"]
      },
      {
        "name": "PRAC3 Compensation",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["C -- COMPENSATION"]
      },
      {
        "name": "Voice Encryption",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["Voice encryption + 90-day retention"]
      },
      {
        "name": "Deepfake Detection",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["Deepfake detect + brand protection"]
      },
      {
        "name": "C2PA Provenance",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["C2PA provenance + audit trail"]
      },
      {
        "name": "MCP Permissions",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["MCP permission queries + revocation"]
      },
      {
        "name": "ISRC/ISWC Metadata",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["ISRC/ISWC + attribution chain"]
      },
      {
        "name": "Royalty Tracking",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["Royalty tracking + smart contracts"]
      }
    ],
    "relationships": [
      {
        "from": "PRAC3 Privacy",
        "to": "Voice Encryption",
        "type": "arrow",
        "label": "implements"
      },
      {
        "from": "PRAC3 Reputation",
        "to": "Deepfake Detection",
        "type": "arrow",
        "label": "implements"
      },
      {
        "from": "PRAC3 Accountability",
        "to": "C2PA Provenance",
        "type": "arrow",
        "label": "implements"
      },
      {
        "from": "PRAC3 Consent",
        "to": "MCP Permissions",
        "type": "arrow",
        "label": "implements"
      },
      {
        "from": "PRAC3 Credit",
        "to": "ISRC/ISWC Metadata",
        "type": "arrow",
        "label": "implements"
      },
      {
        "from": "PRAC3 Compensation",
        "to": "Royalty Tracking",
        "type": "arrow",
        "label": "implements"
      }
    ],
    "callout_boxes": [
      {
        "heading": "THE VOICE RIGHTS STACK EXTENDS ATTRIBUTION-BY-DESIGN TO AUDIO",
        "body_text": "PRAC3 provides the ethical framework; the attribution scaffold provides the technical implementation.",
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
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
