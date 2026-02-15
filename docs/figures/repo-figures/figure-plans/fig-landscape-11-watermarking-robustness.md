# fig-landscape-11: Audio Watermarking: 22 Schemes, 22 Attacks, None Robust

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-11 |
| **Title** | Audio Watermarking: 22 Schemes, 22 Attacks, None Robust |
| **Audience** | L4 (AI/ML Researcher) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Presents the state-of-the-art in audio watermarking robustness by visualizing the SoK survey (Wen et al. 2025) finding that no watermarking scheme survives all known attacks. Answers: "Can we rely on watermarking alone for music attribution?"

## Key Message

A systematic evaluation of 22 watermarking schemes against 22 attack types shows none survive all attacks -- watermarking is necessary but insufficient for attribution.

## Visual Concept

Four panels arranged in a 2x2 grid. Top-left: named watermarking schemes grouped by approach. Top-right: attack categories grouped by type. Bottom-left: robustness matrix showing survival rates (conceptual heatmap). Bottom-right: key named systems with their specific strengths and weaknesses. A prominent callout highlights the 8 previously unknown highly effective attacks. The overall visual communicates fragility through the sparse survival pattern.

```
+-----------------------------------------------------------------------+
|  AUDIO WATERMARKING                                                    |
|  ■ 22 Schemes, 22 Attacks, None Robust                                |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. SCHEMES (22)                    II. ATTACKS (22)                   |
|  ┌──────────────────────┐          ┌──────────────────────┐           |
|  │ Spectral Domain      │          │ Signal Processing     │           |
|  │  AudioSeal (Meta)    │          │  Time-stretch         │           |
|  │  WavMark             │          │  Pitch-shift          │           |
|  │  SilentCipher        │          │  Compression          │           |
|  │                      │          │  Noise addition       │           |
|  │ Generative Model     │          │                       │           |
|  │  SynthID Audio       │          │ Re-encoding           │           |
|  │  (Google DeepMind)   │          │  Codec re-encode      │           |
|  │                      │          │  Format conversion    │           |
|  │ Traditional          │          │                       │           |
|  │  Digimarc            │          │ Model-Based Removal   │           |
|  │  XAttnMark           │          │  Neural regeneration  │           |
|  │  ...17 more          │          │  Adversarial attack   │           |
|  └──────────────────────┘          │  ...14 more           │           |
|                                    └──────────────────────┘           |
|  III. ROBUSTNESS MATRIX             IV. KEY SYSTEMS                    |
|  ┌──────────────────────┐          ┌──────────────────────┐           |
|  │                      │          │ AudioSeal             │           |
|  │ Schemes →            │          │  ■ Localized detect.  │           |
|  │ ┌─┬─┬─┬─┬─┬─┬─┬─┐  │          │  ■ Sample-level       │           |
|  │ │░│ │░│ │ │░│ │ │  │          │                       │           |
|  │ ├─┼─┼─┼─┼─┼─┼─┼─┤  │          │ SynthID Audio         │           |
|  │ │ │░│ │░│ │ │░│ │  │          │  ■ Integrated in Lyria│           |
|  │ │ │ │ │ │ │ │ │ │  │          │  ■ Model-native       │           |
|  │ └─┴─┴─┴─┴─┴─┴─┴─┘  │          │                       │           |
|  │ ↓ Attacks            │          │ ■ 8 NEW attacks       │           |
|  │ No scheme fills      │          │   previously unknown  │           |
|  │ all cells            │          │   highly effective     │           |
|  └──────────────────────┘          └──────────────────────┘           |
|                                                                        |
|  ■ Watermarking is NECESSARY but INSUFFICIENT for attribution          |
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
    content: "AUDIO WATERMARKING"
    role: title

  - id: subtitle_zone
    bounds: [0, 100, 1920, 40]
    content: "22 Schemes, 22 Attacks, None Robust"
    role: subtitle

  - id: panel_schemes
    bounds: [60, 180, 860, 380]
    role: content_area
    label: "I. SCHEMES (22)"

  - id: panel_attacks
    bounds: [980, 180, 860, 380]
    role: content_area
    label: "II. ATTACKS (22)"

  - id: panel_matrix
    bounds: [60, 600, 860, 380]
    role: content_area
    label: "III. ROBUSTNESS MATRIX"

  - id: panel_key_systems
    bounds: [980, 600, 860, 380]
    role: content_area
    label: "IV. KEY SYSTEMS"

  - id: footer_callout
    bounds: [60, 1010, 1800, 40]
    role: callout_bar
    label: "Watermarking is NECESSARY but INSUFFICIENT"

anchors:
  - id: spectral_group
    position: [80, 220]
    size: [380, 160]
    role: solution_component
    label: "Spectral Domain Schemes"

  - id: generative_group
    position: [500, 220]
    size: [380, 160]
    role: solution_component
    label: "Generative Model Schemes"

  - id: signal_attacks
    position: [1000, 220]
    size: [380, 120]
    role: problem_statement
    label: "Signal Processing Attacks"

  - id: model_attacks
    position: [1000, 380]
    size: [380, 120]
    role: problem_statement
    label: "Model-Based Removal"

  - id: robustness_heatmap
    position: [80, 640]
    size: [800, 300]
    role: data_flow
    label: "Survival Rate Matrix"

  - id: audioseal_highlight
    position: [1000, 640]
    size: [800, 100]
    role: solution_component
    label: "AudioSeal"

  - id: synthid_highlight
    position: [1000, 760]
    size: [800, 100]
    role: solution_component
    label: "SynthID Audio"

  - id: new_attacks_callout
    position: [1000, 880]
    size: [800, 80]
    role: callout_bar
    label: "8 previously unknown attacks"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "AUDIO WATERMARKING" in editorial caps with accent square |
| Subtitle | `label_editorial` | "22 Schemes, 22 Attacks, None Robust" |
| Schemes panel | `solution_component` | 22 named watermarking schemes grouped: spectral, generative, traditional |
| Attacks panel | `problem_statement` | 22 attack types grouped: signal processing, re-encoding, model-based removal |
| Robustness matrix | `data_flow` | Conceptual heatmap showing which schemes survive which attacks -- sparse pattern |
| Key systems panel | `solution_component` | AudioSeal (localized detection) and SynthID Audio (Lyria-integrated) highlighted |
| New attacks callout | `callout_bar` | 8 previously unknown highly effective attacks discovered by SoK survey |
| Footer callout | `callout_bar` | "Watermarking is NECESSARY but INSUFFICIENT for attribution" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Schemes | Robustness matrix rows | arrow | Each scheme tested |
| Attacks | Robustness matrix cols | arrow | Each attack applied |
| Robustness matrix | Footer callout | arrow | None survive all |
| AudioSeal | Localized detection | contains | Specific strength |
| SynthID | Lyria integration | contains | Specific strength |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "8 NEW ATTACKS" | The SoK survey (Wen et al. 2025) discovered 8 previously unknown highly effective attacks against audio watermarking | panel IV inset |
| "NONE ROBUST" | No single scheme in the survey survived all 22 attack types -- every scheme has at least one class of attack that defeats it | panel III footer |
| "NECESSARY BUT INSUFFICIENT" | Watermarking provides one evidence layer for attribution but cannot serve as the sole mechanism | bottom footer |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "AudioSeal (Meta)"
- Label 2: "WavMark"
- Label 3: "SilentCipher"
- Label 4: "SynthID Audio (DeepMind)"
- Label 5: "Digimarc"
- Label 6: "XAttnMark"
- Label 7: "Time-Stretch"
- Label 8: "Pitch-Shift"
- Label 9: "Compression"
- Label 10: "Neural Regeneration"
- Label 11: "Adversarial Attack"
- Label 12: "Localized Detection"
- Label 13: "Model-Native Watermark"
- Label 14: "8 New Attacks Found"
- Label 15: "Necessary but Insufficient"

### Caption (for embedding in documentation)

Systematic evaluation of 22 audio watermarking schemes against 22 attack types (Wen et al. 2025 SoK survey) reveals no scheme survives all attacks. Key systems like AudioSeal offer localized detection and SynthID Audio provides model-native integration, but watermarking remains necessary yet insufficient for complete attribution. Eight previously unknown highly effective attacks were discovered.

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

8. The SoK survey is Wen et al. (2025) -- do NOT cite a different year or author set.
9. AudioSeal is from Meta -- do NOT attribute it to another company.
10. SynthID Audio is from Google DeepMind, integrated into Lyria -- do NOT conflate with text-based SynthID.
11. The robustness matrix is CONCEPTUAL -- do NOT invent specific numeric survival rates for individual cells.
12. Do NOT claim any scheme is "fully robust" -- the entire point is that none are.
13. The 8 new attacks were discovered by the SoK survey itself -- do NOT attribute them to earlier work.
14. Do NOT list all 22 schemes or all 22 attacks -- show representative examples with "...N more."
15. WavMark and SilentCipher are distinct schemes -- do NOT conflate them.

## Alt Text

22 watermarking schemes tested against 22 attacks with robustness matrix showing none survive all attack types

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "landscape-11",
    "title": "Audio Watermarking: 22 Schemes, 22 Attacks, None Robust",
    "audience": "L4",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "No watermarking scheme survives all attacks -- watermarking is necessary but insufficient for attribution.",
    "layout_flow": "grid-2x2",
    "key_structures": [
      {
        "name": "Schemes Panel",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["AudioSeal", "WavMark", "SynthID Audio", "22 total"]
      },
      {
        "name": "Attacks Panel",
        "role": "problem_statement",
        "is_highlighted": true,
        "labels": ["Time-stretch", "Neural regeneration", "22 total"]
      },
      {
        "name": "Robustness Matrix",
        "role": "data_flow",
        "is_highlighted": true,
        "labels": ["None fill all cells", "Sparse survival"]
      },
      {
        "name": "Key Systems",
        "role": "solution_component",
        "is_highlighted": false,
        "labels": ["AudioSeal localized", "SynthID model-native"]
      }
    ],
    "relationships": [
      {
        "from": "Schemes",
        "to": "Robustness matrix rows",
        "type": "arrow",
        "label": "each tested"
      },
      {
        "from": "Attacks",
        "to": "Robustness matrix cols",
        "type": "arrow",
        "label": "each applied"
      }
    ],
    "callout_boxes": [
      {
        "heading": "8 NEW ATTACKS",
        "body_text": "Previously unknown highly effective attacks discovered by SoK survey",
        "position": "panel-IV"
      },
      {
        "heading": "NECESSARY BUT INSUFFICIENT",
        "body_text": "Watermarking provides one evidence layer, cannot serve as sole mechanism",
        "position": "footer"
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
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
