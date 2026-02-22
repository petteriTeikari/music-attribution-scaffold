# fig-persona-15: Suno vs Soundverse Persona Approaches

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-15 |
| **Title** | Suno vs Soundverse: Inference vs Consent-by-Design |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/knowledge-base/, docs/planning/ |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Contrasts two fundamentally different approaches to artist persona capture in generative music platforms. Suno Personas infer style from mixed songs (implicit capture), while Soundverse DNA requires explicit artist upload with verified ownership (consent-by-design). Answers: "What is the attribution quality gap between inferred and explicit persona systems?"

## Key Message

Consent-by-design (Soundverse DNA) produces higher attribution quality than inference-based capture (Suno Personas) because provenance is embedded at creation, not reconstructed post-hoc.

## Visual Concept

Vertical split panel. Left panel shows Suno Personas workflow: user uploads mixed songs, platform infers style elements, creates shareable persona with inferred attribution. Right panel shows Soundverse DNA workflow: verified artist uploads stems with explicit metadata, platform builds DNA profile with consent chain. A central comparison bar highlights the attribution quality gap. The left side uses dashed lines (inferred connections) while the right uses solid lines (explicit provenance).

```
+-----------------------------------------------------------------------+
|  SUNO VS SOUNDVERSE                                                    |
|  -- Inference vs Consent-by-Design                                     |
+----------------------------------+------------------------------------+
|                                  |                                    |
|  SUNO PERSONAS                   |  SOUNDVERSE DNA                   |
|  (Inference-Based)               |  (Consent-by-Design)              |
|  ═══════════════════             |  ═══════════════════              |
|                                  |                                    |
|  ┌──────────────────┐           |  ┌──────────────────┐             |
|  │ User uploads      │           |  │ Verified artist   │             |
|  │ mixed songs       │           |  │ uploads stems     │             |
|  └────────┬─────────┘           |  └────────┬─────────┘             |
|           │                      |           │                        |
|           ▼                      |           ▼                        |
|  ┌──────────────────┐           |  ┌──────────────────┐             |
|  │ Platform infers   │           |  │ Explicit metadata  │             |
|  │ style elements    │           |  │ + ownership proof  │             |
|  │ - - - (dashed) - -│           |  │ ────(solid)────── │             |
|  └────────┬─────────┘           |  └────────┬─────────┘             |
|           │                      |           │                        |
|           ▼                      |           ▼                        |
|  ┌──────────────────┐           |  ┌──────────────────┐             |
|  │ Shareable persona │           |  │ DNA profile with   │             |
|  │ Public / Private  │           |  │ consent chain      │             |
|  └──────────────────┘           |  └──────────────────┘             |
|                                  |                                    |
|  ATTRIBUTION QUALITY             |  ATTRIBUTION QUALITY               |
|  ──────────────────              |  ──────────────────               |
|  Source: Inference               |  Source: Explicit                  |
|  Assurance: A1 (Claimed)        |  Assurance: A2-A3 (Verified)      |
|  Provenance: Reconstructed      |  Provenance: Embedded             |
|  Sharing: User-controlled       |  Sharing: Consent-gated           |
|  Rights: Ambiguous              |  Rights: Clear chain              |
|                                  |                                    |
+----------------------------------+------------------------------------+
|  -- CONSENT-BY-DESIGN VS INFERENCE -- THE ATTRIBUTION QUALITY GAP     |
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
    content: "SUNO VS SOUNDVERSE"
    role: title

  - id: left_panel
    bounds: [40, 140, 920, 780]
    content: "Suno Personas (Inference-Based)"
    role: content_area

  - id: right_panel
    bounds: [960, 140, 920, 780]
    content: "Soundverse DNA (Consent-by-Design)"
    role: content_area

  - id: callout_zone
    bounds: [40, 940, 1840, 100]
    content: "CONSENT-BY-DESIGN VS INFERENCE -- THE ATTRIBUTION QUALITY GAP"
    role: callout_box

anchors:
  - id: suno_input
    position: [120, 200]
    size: [760, 80]
    role: processing_stage
    label: "User uploads mixed songs"

  - id: suno_infer
    position: [120, 340]
    size: [760, 100]
    role: processing_stage
    label: "Platform infers style"

  - id: suno_output
    position: [120, 500]
    size: [760, 80]
    role: processing_stage
    label: "Shareable persona"

  - id: suno_quality
    position: [120, 640]
    size: [760, 220]
    role: assurance_a1
    label: "Attribution: inference, A1"

  - id: soundverse_input
    position: [1040, 200]
    size: [760, 80]
    role: processing_stage
    label: "Verified artist uploads stems"

  - id: soundverse_verify
    position: [1040, 340]
    size: [760, 100]
    role: processing_stage
    label: "Explicit metadata + ownership"

  - id: soundverse_output
    position: [1040, 500]
    size: [760, 80]
    role: processing_stage
    label: "DNA profile with consent chain"

  - id: soundverse_quality
    position: [1040, 640]
    size: [760, 220]
    role: assurance_a3
    label: "Attribution: explicit, A2-A3"

  - id: suno_flow_1
    from: suno_input
    to: suno_infer
    type: dashed
    label: "inferred"

  - id: suno_flow_2
    from: suno_infer
    to: suno_output
    type: dashed
    label: "inferred"

  - id: soundverse_flow_1
    from: soundverse_input
    to: soundverse_verify
    type: arrow
    label: "explicit"

  - id: soundverse_flow_2
    from: soundverse_verify
    to: soundverse_output
    type: arrow
    label: "verified"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Suno input | `processing_stage` | User uploads mixed songs containing multiple artist influences |
| Suno inference | `processing_stage` | Platform extracts and infers style elements from mixed content |
| Suno persona output | `processing_stage` | Shareable persona with public/private toggle |
| Suno quality block | `assurance_a1` | Attribution quality: inference-based, A1 claimed, provenance reconstructed |
| Soundverse input | `processing_stage` | Verified artist uploads isolated stems with identity proof |
| Soundverse verification | `processing_stage` | Explicit metadata attached with ownership verification |
| Soundverse DNA output | `processing_stage` | DNA profile with full consent chain embedded |
| Soundverse quality block | `assurance_a3` | Attribution quality: explicit, A2-A3 verified, provenance embedded |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Suno input | Suno inference | dashed | "style inferred" |
| Suno inference | Suno persona | dashed | "persona constructed" |
| Soundverse input | Soundverse verification | arrow | "explicit metadata" |
| Soundverse verification | Soundverse DNA | arrow | "consent chain embedded" |
| Suno quality | Soundverse quality | bidirectional | "attribution quality gap" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "THE QUALITY GAP" | "CONSENT-BY-DESIGN VS INFERENCE -- THE ATTRIBUTION QUALITY GAP" | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "SUNO PERSONAS"
- Label 2: "SOUNDVERSE DNA"
- Label 3: "Inference-Based"
- Label 4: "Consent-by-Design"
- Label 5: "User uploads mixed songs"
- Label 6: "Verified artist uploads"
- Label 7: "Platform infers style"
- Label 8: "Explicit metadata"
- Label 9: "A1 Claimed"
- Label 10: "A2-A3 Verified"
- Label 11: "Provenance: Reconstructed"
- Label 12: "Provenance: Embedded"

### Caption (for embedding in documentation)

Split comparison of Suno Personas (inference-based style capture from mixed songs, A1 attribution) versus Soundverse DNA (consent-by-design with verified artist uploads, A2-A3 attribution) -- demonstrating the attribution quality gap between post-hoc reconstruction and embedded provenance.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `assurance_a1`, `assurance_a3` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Suno Personas is a real feature allowing users to create and share musical style profiles. Do NOT fabricate additional Suno features.
10. Soundverse DNA is a real feature for artist voice/style upload with ownership verification. Do NOT fabricate additional Soundverse features.
11. Suno Personas uses inference from uploaded songs -- the user may not own the songs. This is the key attribution weakness.
12. Soundverse DNA requires the uploading artist to be the verified owner. This is the key attribution strength.
13. Do NOT present either platform as "better" overall -- focus specifically on the attribution quality dimension.
14. A1 means "single source claims the attribution" -- Suno persona is essentially self-claimed without verification.
15. A2-A3 means "multiple sources agree or artist verified" -- Soundverse DNA embeds ownership proof.
16. Both panels must be visually equal in size. The quality comparison should be the distinguishing element, not panel prominence.

## Alt Text

Split-panel comparison of Suno Personas inference-based style capture versus Soundverse DNA consent-by-design attribution, highlighting the quality gap between reconstructed provenance (A1) and embedded provenance (A2-A3) in generative music platforms.

## Image Embed

![Split-panel comparison of Suno Personas inference-based style capture versus Soundverse DNA consent-by-design attribution, highlighting the quality gap between reconstructed provenance (A1) and embedded provenance (A2-A3) in generative music platforms.](docs/figures/repo-figures/assets/fig-persona-15-suno-vs-soundverse.jpg)

*Split comparison of Suno Personas (inference-based style capture from mixed songs, A1 attribution) versus Soundverse DNA (consent-by-design with verified artist uploads, A2-A3 attribution) -- demonstrating the attribution quality gap between post-hoc reconstruction and embedded provenance.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-15",
    "title": "Suno vs Soundverse: Inference vs Consent-by-Design",
    "audience": "L2",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Consent-by-design produces higher attribution quality than inference-based capture because provenance is embedded at creation.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Suno Personas Panel",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["SUNO PERSONAS", "Inference-Based", "A1 Claimed"]
      },
      {
        "name": "Soundverse DNA Panel",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["SOUNDVERSE DNA", "Consent-by-Design", "A2-A3 Verified"]
      },
      {
        "name": "Attribution Quality Comparison",
        "role": "data_mono",
        "is_highlighted": true,
        "labels": ["Inference vs Explicit", "Reconstructed vs Embedded"]
      }
    ],
    "relationships": [
      {
        "from": "Suno input",
        "to": "Suno persona",
        "type": "dashed",
        "label": "inferred style, no ownership proof"
      },
      {
        "from": "Soundverse input",
        "to": "Soundverse DNA",
        "type": "arrow",
        "label": "explicit metadata, verified ownership"
      }
    ],
    "callout_boxes": [
      {
        "heading": "THE QUALITY GAP",
        "body_text": "CONSENT-BY-DESIGN VS INFERENCE -- THE ATTRIBUTION QUALITY GAP",
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
- [x] Audience level correct (L2)
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
