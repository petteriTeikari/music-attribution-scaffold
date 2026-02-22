# fig-voice-11: TTS Model Landscape (Feb 2026)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-11 |
| **Title** | TTS Model Landscape (Feb 2026) |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Map the current TTS model landscape across commercial and open-source offerings, with key stats for engineering decision-making. Answers: "What TTS options exist as of Feb 2026, and what are the concrete tradeoffs in params, latency, cost, and licensing?"

## Key Message

The TTS landscape in Feb 2026 is split between commercial APIs (ElevenLabs, Cartesia, Inworld, Rime) offering turnkey quality and open-source models (Chatterbox, Orpheus, Kokoro, CosyVoice) that crossed the quality threshold in 2025 -- enabling 100x cost reduction through self-hosting.

## Visual Concept

Two-row multi-panel grid (Template B). Top row labeled "COMMERCIAL" with four model cards (ElevenLabs, Cartesia, Inworld, Rime). Bottom row labeled "OPEN-SOURCE" with four model cards (Chatterbox, Orpheus, Kokoro, CosyVoice). Each card shows: model name, parameter count, typical latency, cost tier, and license. Accent line divides the two rows. Bottom callout celebrates the open-source quality crossing. Key stats per model displayed in mono typography.

```
+-------------------------------------------------------------------+
|  TTS MODEL LANDSCAPE (FEB 2026)                            [sq]   |
|                                                                    |
|  COMMERCIAL                                                        |
|  +-------------+-------------+-------------+-------------+        |
|  | I           | II          | III         | IV          |        |
|  | ElevenLabs  | Cartesia    | Inworld     | Rime        |        |
|  | Turbo v2.5  | Sonic       | Arcturus    | Mist        |        |
|  | ~300ms TTFB | ~135ms TTFB | ~150ms TTFB | ~100ms TTFB |        |
|  | $0.10/min   | $0.06/min   | Custom      | $0.04/min   |        |
|  | Proprietary | Proprietary | Proprietary | Proprietary |        |
|  +-------------+-------------+-------------+-------------+        |
|  ────────────────────────────────────────────── [accent line]      |
|  OPEN-SOURCE                                                       |
|  +-------------+-------------+-------------+-------------+        |
|  | V           | VI          | VII         | VIII        |        |
|  | Chatterbox  | Orpheus     | Kokoro      | CosyVoice   |        |
|  | 350M params | 3B params   | 82M params  | 300M params |        |
|  | MIT license | Apache 2.0  | Apache 2.0  | Apache 2.0  |        |
|  | #1 on HF    | Emotion tags| <1GB VRAM   | Multilingual|        |
|  | Resemble AI | Canopy Labs | Hexgrad     | Alibaba     |        |
|  +-------------+-------------+-------------+-------------+        |
|                                                                    |
|  "2025: THE YEAR OPEN-SOURCE TTS CROSSED THE               [line] |
|   QUALITY THRESHOLD"                                               |
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
    content: "TTS MODEL LANDSCAPE (FEB 2026)"
    role: title

  - id: commercial_row
    bounds: [40, 140, 1840, 340]
    content: "COMMERCIAL"
    role: content_area

  - id: divider
    bounds: [40, 500, 1840, 2]
    role: accent_line

  - id: opensource_row
    bounds: [40, 520, 1840, 340]
    content: "OPEN-SOURCE"
    role: content_area

  - id: callout_zone
    bounds: [40, 900, 1840, 140]
    content: "2025: THE YEAR OPEN-SOURCE TTS CROSSED THE QUALITY THRESHOLD"
    role: callout_box

anchors:
  - id: card_elevenlabs
    position: [80, 200]
    size: [420, 240]
    role: processing_stage
    label: "I ElevenLabs"

  - id: card_cartesia
    position: [540, 200]
    size: [420, 240]
    role: processing_stage
    label: "II Cartesia"

  - id: card_inworld
    position: [1000, 200]
    size: [420, 240]
    role: processing_stage
    label: "III Inworld"

  - id: card_rime
    position: [1460, 200]
    size: [420, 240]
    role: processing_stage
    label: "IV Rime"

  - id: card_chatterbox
    position: [80, 580]
    size: [420, 240]
    role: processing_stage
    label: "V Chatterbox"

  - id: card_orpheus
    position: [540, 580]
    size: [420, 240]
    role: processing_stage
    label: "VI Orpheus"

  - id: card_kokoro
    position: [1000, 580]
    size: [420, 240]
    role: processing_stage
    label: "VII Kokoro"

  - id: card_cosyvoice
    position: [1460, 580]
    size: [420, 240]
    role: processing_stage
    label: "VIII CosyVoice"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| ElevenLabs | `processing_stage` | Turbo v2.5, ~300ms TTFB, $0.10/min, proprietary, former market leader |
| Cartesia | `processing_stage` | Sonic, ~135ms TTFB, $0.06/min, proprietary, state-space model architecture |
| Inworld | `processing_stage` | Arcturus, ~150ms TTFB, custom pricing, proprietary, game/entertainment focus |
| Rime | `processing_stage` | Mist, ~100ms TTFB, $0.04/min, proprietary, fastest commercial option |
| Chatterbox | `processing_stage` | 350M params, MIT license, #1 trending on HuggingFace, by Resemble AI |
| Orpheus | `processing_stage` | 3B params, Apache 2.0, emotion tags (laugh, sigh), ~200ms streaming, by Canopy Labs |
| Kokoro | `processing_stage` | 82M params, Apache 2.0, <1GB VRAM, $0.06/hr self-hosted, by Hexgrad |
| CosyVoice | `processing_stage` | 300M params, Apache 2.0, multilingual, by Alibaba DAMO Academy |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Commercial Row | Open-Source Row | dashed | "quality convergence in 2025" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "2025: THE YEAR OPEN-SOURCE TTS CROSSED THE QUALITY THRESHOLD" | Open-source models (Chatterbox, Orpheus, Kokoro) now match or exceed commercial quality in blind preference tests. Self-hosting reduces TTS cost from $0.10/min to $0.001/min -- a 100x reduction. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "COMMERCIAL"
- Label 2: "OPEN-SOURCE"
- Label 3: "I ElevenLabs Turbo v2.5"
- Label 4: "II Cartesia Sonic"
- Label 5: "III Inworld Arcturus"
- Label 6: "IV Rime Mist"
- Label 7: "V Chatterbox"
- Label 8: "VI Orpheus"
- Label 9: "VII Kokoro"
- Label 10: "VIII CosyVoice"
- Label 11: "~300ms TTFB"
- Label 12: "~135ms TTFB"
- Label 13: "~150ms TTFB"
- Label 14: "~100ms TTFB"
- Label 15: "350M params, MIT"
- Label 16: "3B params, Apache 2.0"
- Label 17: "82M params, Apache 2.0"
- Label 18: "300M params, Apache 2.0"
- Label 19: "$0.10/min"
- Label 20: "$0.06/min"
- Label 21: "$0.04/min"
- Label 22: "#1 on HuggingFace"
- Label 23: "Emotion tags"
- Label 24: "<1GB VRAM"
- Label 25: "Multilingual"

### Caption (for embedding in documentation)

Two-row landscape of TTS models as of February 2026: commercial providers (ElevenLabs, Cartesia, Inworld, Rime) versus open-source models (Chatterbox, Orpheus, Kokoro, CosyVoice) with parameter counts, latency, cost, and license for each.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Roman numerals I-VIII must be used for model card headers, not Arabic numerals.
10. ElevenLabs Turbo v2.5 TTFB is approximately 300ms -- this is from community benchmarks, not official latency guarantees. Present as approximate with "~".
11. Cartesia Sonic TTFB is approximately 135ms -- from Cartesia documentation and benchmarks.
12. Rime Mist TTFB is approximately 100ms -- from Rime's published benchmarks as the fastest commercial option.
13. Chatterbox is 350M parameters, MIT license, by Resemble AI -- it trended #1 on HuggingFace in mid-2025.
14. Orpheus is 3B parameters, Apache 2.0, by Canopy Labs -- its differentiator is emotion control tags.
15. Kokoro is 82M parameters, Apache 2.0, by Hexgrad -- its differentiator is extreme efficiency (<1GB VRAM).
16. CosyVoice is approximately 300M parameters, Apache 2.0, by Alibaba DAMO Academy -- its differentiator is multilingual support.
17. Pricing figures are approximate as of Feb 2026 and may change. Present with "~" prefix where uncertain.
18. Do NOT add models not listed in the specification -- the landscape is curated, not exhaustive.

## Alt Text

Two-row text-to-speech model landscape for Feb 2026 comparing commercial APIs (ElevenLabs, Cartesia, Inworld, Rime) with open-source models (Chatterbox, Orpheus, Kokoro, CosyVoice) that crossed the quality threshold enabling 100x cost reduction.

## Image Embed

![Two-row text-to-speech model landscape for Feb 2026 comparing commercial APIs (ElevenLabs, Cartesia, Inworld, Rime) with open-source models (Chatterbox, Orpheus, Kokoro, CosyVoice) that crossed the quality threshold enabling 100x cost reduction.](docs/figures/repo-figures/assets/fig-voice-11-tts-model-landscape.jpg)

*Two-row landscape of TTS models as of February 2026: commercial providers (ElevenLabs, Cartesia, Inworld, Rime) versus open-source models (Chatterbox, Orpheus, Kokoro, CosyVoice) with parameter counts, latency, cost, and license for each.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-11",
    "title": "TTS Model Landscape (Feb 2026)",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "TTS landscape split between commercial APIs and open-source models that crossed the quality threshold in 2025, enabling 100x cost reduction.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "ElevenLabs",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["I ElevenLabs", "Turbo v2.5", "~300ms TTFB", "$0.10/min", "Proprietary"]
      },
      {
        "name": "Cartesia",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["II Cartesia", "Sonic", "~135ms TTFB", "$0.06/min", "Proprietary"]
      },
      {
        "name": "Inworld",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["III Inworld", "Arcturus", "~150ms TTFB", "Custom", "Proprietary"]
      },
      {
        "name": "Rime",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["IV Rime", "Mist", "~100ms TTFB", "$0.04/min", "Proprietary"]
      },
      {
        "name": "Chatterbox",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["V Chatterbox", "350M params", "MIT", "#1 HuggingFace", "Resemble AI"]
      },
      {
        "name": "Orpheus",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["VI Orpheus", "3B params", "Apache 2.0", "Emotion tags", "Canopy Labs"]
      },
      {
        "name": "Kokoro",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["VII Kokoro", "82M params", "Apache 2.0", "<1GB VRAM", "Hexgrad"]
      },
      {
        "name": "CosyVoice",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["VIII CosyVoice", "300M params", "Apache 2.0", "Multilingual", "Alibaba"]
      }
    ],
    "relationships": [
      {
        "from": "Commercial Row",
        "to": "Open-Source Row",
        "type": "dashed",
        "label": "quality convergence in 2025"
      }
    ],
    "callout_boxes": [
      {
        "heading": "2025: THE YEAR OPEN-SOURCE TTS CROSSED THE QUALITY THRESHOLD",
        "body_text": "Self-hosting reduces TTS cost from $0.10/min to $0.001/min -- a 100x reduction.",
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
- [ ] Audience level correct (L3)
- [ ] Layout template identified (B)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
