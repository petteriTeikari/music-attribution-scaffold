# fig-persona-16: Persona Platform Landscape

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-16 |
| **Title** | Persona Platform Landscape: Commercial/Open-Source x Text/Voice |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/knowledge-base/, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Maps the current persona platform ecosystem across two critical dimensions: commercial vs open-source and text vs voice modality. Reveals the structural gap where no single platform bridges character consistency with production reliability across both modalities. Answers: "Where are the players, and where is the gap?"

## Key Message

No single platform bridges character consistency and reliability across text and voice modalities -- the persona platform landscape remains fragmented.

## Visual Concept

2x2 grid matrix with axes labeled. Horizontal axis: Text (left) vs Voice (right). Vertical axis: Commercial (top) vs Open-Source (bottom). Each quadrant contains 3-4 platform names with brief descriptors. The center of the grid (where axes cross) is empty, emphasizing the gap. A callout highlights the missing "bridge" platform.

```
+-----------------------------------------------------------------------+
|  PERSONA PLATFORM LANDSCAPE                                            |
|  -- Commercial/Open-Source x Text/Voice                                |
+-----------------------------------------------------------------------+
|                                                                        |
|               TEXT                          VOICE                      |
|          ◄──────────────────────────────────────────►                  |
|                                                                        |
|  C  ┌──────────────────────┐  ┌──────────────────────┐               |
|  O  │                      │  │                      │               |
|  M  │  Character.AI        │  │  ElevenLabs          │               |
|  M  │  (largest user base) │  │  (voice cloning)     │               |
|  E  │                      │  │                      │               |
|  R  │  Inworld             │  │  Hume EVI            │               |
|  C  │  (game NPCs)         │  │  (emotional voice)   │               |
|  I  │                      │  │                      │               |
|  A  │  Convai              │  │  Cartesia Line       │               |
|  L  │  (enterprise)        │  │  (real-time)         │               |
|     │                      │  │                      │               |
|     │  Charisma.ai         │  │                      │               |
|  ▲  │  (branching stories) │  │                      │               |
|  │  └──────────────────────┘  └──────────────────────┘               |
|  │                                                                     |
|  │          ◆ NO PLATFORM BRIDGES THIS GAP ◆                          |
|  │                                                                     |
|  │  ┌──────────────────────┐  ┌──────────────────────┐               |
|  ▼  │                      │  │                      │               |
|     │  SillyTavern         │  │  Sesame CSM          │               |
|  O  │  (roleplay frontend) │  │  (conversational     │               |
|  P  │                      │  │   speech model)      │               |
|  E  │  CrewAI              │  │                      │               |
|  N  │  (multi-agent)       │  │  Orpheus TTS         │               |
|     │                      │  │  (emotive speech)    │               |
|  S  │  PydanticAI          │  │                      │               |
|  O  │  (typed agents)      │  │  XTTS-v2             │               |
|  U  │                      │  │  (multilingual)      │               |
|  R  │                      │  │                      │               |
|  C  └──────────────────────┘  └──────────────────────┘               |
|  E                                                                     |
|                                                                        |
|  -- NO SINGLE PLATFORM BRIDGES CHARACTER AND RELIABILITY               |
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
    content: "PERSONA PLATFORM LANDSCAPE"
    role: title

  - id: quadrant_commercial_text
    bounds: [200, 160, 720, 360]
    content: "Commercial Text platforms"
    role: content_area

  - id: quadrant_commercial_voice
    bounds: [980, 160, 720, 360]
    content: "Commercial Voice platforms"
    role: content_area

  - id: quadrant_open_text
    bounds: [200, 580, 720, 360]
    content: "Open-Source Text platforms"
    role: content_area

  - id: quadrant_open_voice
    bounds: [980, 580, 720, 360]
    content: "Open-Source Voice platforms"
    role: content_area

  - id: gap_zone
    bounds: [600, 520, 700, 60]
    content: "NO PLATFORM BRIDGES THIS GAP"
    role: problem_statement

  - id: callout_zone
    bounds: [80, 960, 1760, 80]
    content: "NO SINGLE PLATFORM BRIDGES CHARACTER AND RELIABILITY"
    role: callout_box

anchors:
  - id: axis_text_label
    position: [440, 140]
    size: [200, 30]
    role: data_mono
    label: "TEXT"

  - id: axis_voice_label
    position: [1260, 140]
    size: [200, 30]
    role: data_mono
    label: "VOICE"

  - id: axis_commercial_label
    position: [80, 340]
    size: [100, 200]
    role: data_mono
    label: "COMMERCIAL"

  - id: axis_open_label
    position: [80, 740]
    size: [100, 200]
    role: data_mono
    label: "OPEN SOURCE"

  - id: character_ai
    position: [260, 200]
    size: [280, 50]
    role: stakeholder_platform
    label: "Character.AI"

  - id: inworld
    position: [260, 260]
    size: [280, 50]
    role: stakeholder_platform
    label: "Inworld"

  - id: convai
    position: [260, 320]
    size: [280, 50]
    role: stakeholder_platform
    label: "Convai"

  - id: charisma
    position: [260, 380]
    size: [280, 50]
    role: stakeholder_platform
    label: "Charisma.ai"

  - id: elevenlabs
    position: [1040, 200]
    size: [280, 50]
    role: stakeholder_platform
    label: "ElevenLabs"

  - id: hume
    position: [1040, 260]
    size: [280, 50]
    role: stakeholder_platform
    label: "Hume EVI"

  - id: cartesia
    position: [1040, 320]
    size: [280, 50]
    role: stakeholder_platform
    label: "Cartesia Line"

  - id: sillytavern
    position: [260, 620]
    size: [280, 50]
    role: stakeholder_platform
    label: "SillyTavern"

  - id: crewai
    position: [260, 680]
    size: [280, 50]
    role: stakeholder_platform
    label: "CrewAI"

  - id: pydanticai
    position: [260, 740]
    size: [280, 50]
    role: stakeholder_platform
    label: "PydanticAI"

  - id: sesame
    position: [1040, 620]
    size: [280, 50]
    role: stakeholder_platform
    label: "Sesame CSM"

  - id: orpheus
    position: [1040, 680]
    size: [280, 50]
    role: stakeholder_platform
    label: "Orpheus TTS"

  - id: xtts
    position: [1040, 740]
    size: [280, 50]
    role: stakeholder_platform
    label: "XTTS-v2"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Commercial Text quadrant | `content_area` | Character.AI (largest user base), Inworld (game NPCs), Convai (enterprise), Charisma.ai (branching stories) |
| Commercial Voice quadrant | `content_area` | ElevenLabs (voice cloning), Hume EVI (emotional voice), Cartesia Line (real-time) |
| Open-Source Text quadrant | `content_area` | SillyTavern (roleplay frontend), CrewAI (multi-agent), PydanticAI (typed agents) |
| Open-Source Voice quadrant | `content_area` | Sesame CSM (conversational speech model), Orpheus TTS (emotive speech), XTTS-v2 (multilingual) |
| Gap indicator | `problem_statement` | Empty center showing no platform bridges character + reliability across modalities |
| Axis labels | `data_mono` | Text/Voice horizontal, Commercial/Open-Source vertical |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Commercial Text | Commercial Voice | dashed | "no bridge" |
| Open-Source Text | Open-Source Voice | dashed | "no bridge" |
| Commercial Text | Open-Source Text | dashed | "different trade-offs" |
| Commercial Voice | Open-Source Voice | dashed | "different trade-offs" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "THE GAP" | "NO SINGLE PLATFORM BRIDGES CHARACTER AND RELIABILITY" | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "TEXT"
- Label 2: "VOICE"
- Label 3: "COMMERCIAL"
- Label 4: "OPEN SOURCE"
- Label 5: "Character.AI"
- Label 6: "Inworld"
- Label 7: "Convai"
- Label 8: "Charisma.ai"
- Label 9: "ElevenLabs"
- Label 10: "Hume EVI"
- Label 11: "Cartesia Line"
- Label 12: "SillyTavern"
- Label 13: "CrewAI"
- Label 14: "PydanticAI"
- Label 15: "Sesame CSM"
- Label 16: "Orpheus TTS"
- Label 17: "XTTS-v2"

### Caption (for embedding in documentation)

2x2 landscape of persona platforms across commercial/open-source and text/voice dimensions, revealing that no single platform bridges character consistency with production reliability across both modalities.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `content_area`, `stakeholder_platform`, `problem_statement` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- Keep platform names as proper nouns; avoid internal architecture details for L2 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. All platform names are real products/projects as of early 2026. Do NOT invent platforms or features.
10. Character.AI is the largest consumer persona platform by users. Do NOT overstate other platforms' scale.
11. Sesame CSM (Conversational Speech Model) is an open-source voice model released March 2025. Do NOT confuse with Sesame Street.
12. PydanticAI is listed under Open-Source Text because the scaffold uses it for typed agents. It is not primarily a "persona platform."
13. The "gap" is the key insight: no platform does both text persona consistency AND voice persona consistency well. Do NOT fill the gap with a speculative product.
14. All four quadrants must be visually equal in size and weight.
15. Cartesia Line is the product name (not just "Cartesia"). Do NOT truncate.

## Alt Text

2x2 landscape matrix of persona platforms mapping commercial versus open-source and text versus voice modalities, featuring Character.AI, ElevenLabs, SillyTavern, Sesame CSM, and others -- revealing that no single platform bridges persona coherence across both modalities.

## Image Embed

![2x2 landscape matrix of persona platforms mapping commercial versus open-source and text versus voice modalities, featuring Character.AI, ElevenLabs, SillyTavern, Sesame CSM, and others -- revealing that no single platform bridges persona coherence across both modalities.](docs/figures/repo-figures/assets/fig-persona-16-persona-platform-landscape.jpg)

*2x2 landscape of persona platforms across commercial/open-source and text/voice dimensions, revealing that no single platform bridges character consistency with production reliability across both modalities.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-16",
    "title": "Persona Platform Landscape: Commercial/Open-Source x Text/Voice",
    "audience": "L2",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "No single platform bridges character consistency and reliability across text and voice modalities.",
    "layout_flow": "centered",
    "key_structures": [
      {
        "name": "Commercial Text Quadrant",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["Character.AI", "Inworld", "Convai", "Charisma.ai"]
      },
      {
        "name": "Commercial Voice Quadrant",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["ElevenLabs", "Hume EVI", "Cartesia Line"]
      },
      {
        "name": "Open-Source Text Quadrant",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["SillyTavern", "CrewAI", "PydanticAI"]
      },
      {
        "name": "Open-Source Voice Quadrant",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["Sesame CSM", "Orpheus TTS", "XTTS-v2"]
      },
      {
        "name": "Bridge Gap",
        "role": "problem_statement",
        "is_highlighted": true,
        "labels": ["NO PLATFORM BRIDGES THIS GAP"]
      }
    ],
    "relationships": [
      {
        "from": "Commercial Text",
        "to": "Commercial Voice",
        "type": "dashed",
        "label": "no bridge between modalities"
      },
      {
        "from": "Open-Source Text",
        "to": "Open-Source Voice",
        "type": "dashed",
        "label": "no bridge between modalities"
      }
    ],
    "callout_boxes": [
      {
        "heading": "THE GAP",
        "body_text": "NO SINGLE PLATFORM BRIDGES CHARACTER AND RELIABILITY",
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
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
