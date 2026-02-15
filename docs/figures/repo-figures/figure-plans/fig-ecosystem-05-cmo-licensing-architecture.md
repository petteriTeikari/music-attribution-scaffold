# fig-ecosystem-05: CMO Licensing Integration Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-05 |
| **Title** | CMO Licensing Integration Architecture |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Shows rights holder to collective licensing to per-output royalty flow, with the scaffold providing the confidence scoring layer. Answers: "How does the scaffold fit into the CMO licensing chain?"

## Key Message

Rights holders delegate to CMOs (STIM, GEMA, PRS), which licence AI platforms; the scaffold provides the attribution confidence layer that makes per-output royalty calculation possible.

## Visual Concept

Top-to-bottom flow. Rights holders (many) delegate to CMOs (STIM as exemplar). CMOs licence AI platforms (Suno, Udio). The scaffold sits as a confidence scoring layer between the CMO and the platform, providing attribution confidence for royalty calculation. Bottom shows per-output royalty flow back to rights holders.

```
+-----------------------------------------------------------------------+
|  CMO LICENSING INTEGRATION                                             |
|  ■ Scaffold as Attribution Confidence Layer                            |
+-----------------------------------------------------------------------+
|                                                                        |
|  RIGHTS HOLDERS                                                        |
|  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐                    |
|  │  ♪  │ │  ♪  │ │  ♪  │ │  ♪  │ │  ♪  │ │  ♪  │                    |
|  └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘                    |
|     │       │       │       │       │       │                          |
|     └───────┴───────┴───┬───┴───────┴───────┘                          |
|                         │ delegate                                     |
|                         ▼                                              |
|              ┌─────────────────────┐                                   |
|              │  CMO                │                                   |
|              │  (STIM exemplar)    │                                   |
|              │  ─────────────────  │                                   |
|              │  World's FIRST      │                                   |
|              │  collective AI      │                                   |
|              │  music licence      │                                   |
|              │  (Sep 2025)         │                                   |
|              └──────────┬──────────┘                                   |
|                         │ licences                                     |
|        ┌────────────────┼────────────────┐                             |
|        │                │                │                             |
|        ▼                ▼                ▼                             |
|  ┌──────────┐  ┌─────────────────────────────────┐  ┌──────────┐     |
|  │ Suno     │  │  SCAFFOLD CONFIDENCE LAYER       │  │ Udio     │     |
|  │ Platform │  │  ═══════════════════════════      │  │ Platform │     |
|  │          │◄─┤  Attribution confidence scores    │─►│          │     |
|  └──────────┘  │  → per-output royalty calc        │  └──────────┘     |
|                │  → rights holder identification   │                   |
|                │  → provenance verification        │                   |
|                └──────────────┬────────────────────┘                   |
|                               │                                        |
|                               │ per-output royalties                   |
|                               ▼                                        |
|              ┌──────────────────────────────┐                          |
|              │  ROYALTY DISTRIBUTION         │                          |
|              │  Confidence-weighted payments │                          |
|              │  back to rights holders       │                          |
|              └──────────────────────────────┘                          |
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
    content: "CMO LICENSING INTEGRATION"
    role: title

  - id: rights_holders_zone
    bounds: [400, 140, 1120, 100]
    role: content_area
    label: "Rights Holders"

  - id: cmo_zone
    bounds: [600, 280, 720, 180]
    role: content_area
    label: "CMO (STIM)"

  - id: scaffold_zone
    bounds: [400, 520, 1120, 240]
    role: content_area_highlighted
    label: "Scaffold Confidence Layer"

  - id: platforms_zone
    bounds: [100, 560, 300, 160]
    role: content_area
    label: "AI Platforms"

  - id: royalty_zone
    bounds: [600, 820, 720, 140]
    role: content_area
    label: "Royalty Distribution"

anchors:
  - id: rights_holder_group
    position: [560, 160]
    size: [800, 60]
    role: stakeholder_artist
    label: "Rights Holders (many)"

  - id: cmo_stim
    position: [700, 300]
    size: [520, 140]
    role: decision_point
    label: "CMO (STIM exemplar)"

  - id: scaffold_layer
    position: [500, 540]
    size: [920, 200]
    role: final_score
    label: "Scaffold Confidence Layer"

  - id: suno_platform
    position: [160, 580]
    size: [280, 120]
    role: stakeholder_platform
    label: "Suno"

  - id: udio_platform
    position: [1480, 580]
    size: [280, 120]
    role: stakeholder_platform
    label: "Udio"

  - id: royalty_distribution
    position: [700, 840]
    size: [520, 100]
    role: feedback_loop
    label: "Royalty Distribution"

  - id: delegate_flow
    from: rights_holder_group
    to: cmo_stim
    type: arrow
    label: "delegate rights"

  - id: licence_flow
    from: cmo_stim
    to: scaffold_layer
    type: arrow
    label: "licences AI platforms"

  - id: confidence_to_suno
    from: scaffold_layer
    to: suno_platform
    type: bidirectional
    label: "confidence scores"

  - id: confidence_to_udio
    from: scaffold_layer
    to: udio_platform
    type: bidirectional
    label: "confidence scores"

  - id: royalty_flow
    from: scaffold_layer
    to: royalty_distribution
    type: arrow
    label: "per-output royalties"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Rights Holders | `stakeholder_artist` | Multiple rights holders delegating to CMOs |
| CMO (STIM exemplar) | `decision_point` | World's first collective AI music licence (Sep 2025) |
| Scaffold Confidence Layer | `final_score` | Attribution confidence scores for royalty calculation |
| Suno Platform | `stakeholder_platform` | AI music generation platform |
| Udio Platform | `stakeholder_platform` | AI music generation platform |
| Royalty Distribution | `feedback_loop` | Confidence-weighted payments back to rights holders |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Rights Holders | CMO (STIM) | arrow | "delegate rights" |
| CMO (STIM) | Scaffold Layer | arrow | "licences AI platforms" |
| Scaffold Layer | Suno | bidirectional | "confidence scores + metadata" |
| Scaffold Layer | Udio | bidirectional | "confidence scores + metadata" |
| Scaffold Layer | Royalty Distribution | arrow | "per-output royalties" |
| Royalty Distribution | Rights Holders | dashed | "payments flow back" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "WORLD'S FIRST" | STIM launched the world's first collective AI music licence in September 2025, with Sureel AI as technology partner | right of CMO node |
| "CONFIDENCE LAYER" | The scaffold provides attribution confidence that makes per-output royalty calculation possible -- not the licence itself | center of scaffold zone |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Rights Holders"
- Label 2: "CMO (STIM exemplar)"
- Label 3: "Scaffold Confidence Layer"
- Label 4: "Per-output royalties"
- Label 5: "Confidence-weighted payments"
- Label 6: "Suno / Udio platforms"

### Caption (for embedding in documentation)

The CMO licensing integration architecture positions the scaffold as the attribution confidence layer between collective management organizations and AI music platforms, enabling per-output royalty calculation based on confidence-scored creator identification.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `stakeholder_artist`, `final_score`, `stakeholder_platform` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" may appear as this is L3 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. STIM launched world's FIRST collective AI music licence (Sep 2025) with Sureel AI as technology partner. Do NOT attribute this to any other CMO.
10. Per-output royalty based on attribution confidence scores. The scaffold provides confidence, NOT the licence.
11. PRD nodes: cmo_licensing_integration -> stim_cmo_pilot (strong), partnership_model -> cmo_licensing_integration (strong).
12. Do NOT claim the scaffold is currently integrated with STIM -- this is an expansion/discussion node.
13. Other CMOs (GEMA, PRS) are mentioned as potential future integrations but STIM is the exemplar for this diagram.

## Alt Text

CMO licensing architecture with scaffold providing attribution confidence for royalties

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-05",
    "title": "CMO Licensing Integration Architecture",
    "audience": "L3",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "The scaffold provides the attribution confidence layer that enables per-output royalty calculation between CMOs and AI platforms.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Rights Holders",
        "role": "stakeholder_artist",
        "is_highlighted": false,
        "labels": ["Rights Holders", "Many creators"]
      },
      {
        "name": "CMO (STIM)",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["CMO (STIM exemplar)", "First AI music licence"]
      },
      {
        "name": "Scaffold Confidence Layer",
        "role": "final_score",
        "is_highlighted": true,
        "labels": ["Attribution confidence", "Per-output royalty calc"]
      },
      {
        "name": "AI Platforms",
        "role": "stakeholder_platform",
        "is_highlighted": false,
        "labels": ["Suno", "Udio"]
      },
      {
        "name": "Royalty Distribution",
        "role": "feedback_loop",
        "is_highlighted": false,
        "labels": ["Confidence-weighted payments"]
      }
    ],
    "relationships": [
      {
        "from": "Rights Holders",
        "to": "CMO (STIM)",
        "type": "arrow",
        "label": "delegate rights"
      },
      {
        "from": "CMO (STIM)",
        "to": "Scaffold Confidence Layer",
        "type": "arrow",
        "label": "licences AI platforms"
      },
      {
        "from": "Scaffold Confidence Layer",
        "to": "AI Platforms",
        "type": "bidirectional",
        "label": "confidence scores + metadata"
      },
      {
        "from": "Scaffold Confidence Layer",
        "to": "Royalty Distribution",
        "type": "arrow",
        "label": "per-output royalties"
      }
    ],
    "callout_boxes": [
      {
        "heading": "WORLD'S FIRST",
        "body_text": "STIM launched the first collective AI music licence (Sep 2025) with Sureel AI",
        "position": "top-right"
      },
      {
        "heading": "CONFIDENCE LAYER",
        "body_text": "Scaffold provides attribution confidence, not the licence itself",
        "position": "left-margin"
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
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
