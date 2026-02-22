# fig-voice-13: The Open-Source TTS Revolution

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-13 |
| **Title** | The Open-Source TTS Revolution |
| **Audience** | L2 (Technical Manager) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Highlight the three most impactful open-source TTS models of 2025-2026 and why they matter for cost-sensitive voice attribution deployments. Answers: "Which open-source TTS models are production-ready, what are their key differentiators, and how much do they actually cost to run?"

## Key Message

Three open-source models -- Chatterbox (MIT, 350M, #1 HuggingFace), Orpheus (Apache 2.0, 3B, emotion tags, 200ms), and Kokoro (Apache 2.0, 82M, <1GB VRAM, $0.06/hr) -- make production-quality voice synthesis essentially free to self-host, reducing TTS cost from $0.10/min to $0.001/min.

## Visual Concept

Three-panel horizontal layout (Template B) with Roman numeral headers. Panel I: Chatterbox -- Resemble AI, MIT license, 350M params, #1 HuggingFace trending. Panel II: Orpheus -- Canopy Labs, Apache 2.0, 3B params, Llama backbone, emotion tags, 200ms streaming. Panel III: Kokoro -- Hexgrad, Apache 2.0, 82M params, <1GB VRAM, $0.06/hr self-hosted. License badges prominent on each panel. Bottom callout with the 100x cost reduction headline.

```
+-------------------------------------------------------------------+
|  THE OPEN-SOURCE TTS REVOLUTION                            [sq]   |
|                                                                    |
|  I   CHATTERBOX          II  ORPHEUS              III KOKORO       |
|  ─────────────────       ──────────────────       ────────────     |
|                                                                    |
|  ┌─────────────────┐    ┌─────────────────┐    ┌────────────────┐ |
|  │ Resemble AI     │    │ Canopy Labs     │    │ Hexgrad        │ |
|  │                 │    │                 │    │                │ |
|  │ 350M params     │    │ 3B params       │    │ 82M params     │ |
|  │ [MIT]           │    │ [Apache 2.0]    │    │ [Apache 2.0]   │ |
|  │                 │    │                 │    │                │ |
|  │ #1 HuggingFace  │    │ Emotion tags:   │    │ <1GB VRAM      │ |
|  │ trending        │    │ <laugh> <sigh>  │    │ ~$0.06/hr      │ |
|  │                 │    │ <gasp> <cry>    │    │ self-hosted     │ |
|  │ Zero-shot voice │    │                 │    │                │ |
|  │ cloning         │    │ 200ms streaming  │    │ Runs on CPU    │ |
|  │                 │    │ latency         │    │ or cheap GPU   │ |
|  └─────────────────┘    └─────────────────┘    └────────────────┘ |
|                                                                    |
|  +─────────────────────────────────────────────────────────────+  |
|  │ "FROM $0.10/MIN TO $0.001/MIN -- Self-hosting reduces      │  |
|  │  TTS cost 100x"                                             │  |
|  +─────────────────────────────────────────────────────────────+  |
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
    content: "THE OPEN-SOURCE TTS REVOLUTION"
    role: title

  - id: panel_strip
    bounds: [40, 140, 1840, 680]
    role: content_area

  - id: callout_zone
    bounds: [40, 860, 1840, 180]
    role: callout_box

anchors:
  - id: panel_i_chatterbox
    position: [80, 200]
    size: [560, 580]
    role: processing_stage
    label: "I CHATTERBOX"

  - id: panel_ii_orpheus
    position: [680, 200]
    size: [560, 580]
    role: processing_stage
    label: "II ORPHEUS"

  - id: panel_iii_kokoro
    position: [1280, 200]
    size: [560, 580]
    role: processing_stage
    label: "III KOKORO"

  - id: license_badge_i
    position: [160, 260]
    size: [120, 40]
    role: security_layer
    label: "MIT"

  - id: license_badge_ii
    position: [760, 260]
    size: [160, 40]
    role: security_layer
    label: "Apache 2.0"

  - id: license_badge_iii
    position: [1360, 260]
    size: [160, 40]
    role: security_layer
    label: "Apache 2.0"

  - id: cost_comparison
    position: [80, 880]
    size: [1760, 140]
    role: callout_box
    label: "FROM $0.10/MIN TO $0.001/MIN"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Chatterbox (Panel I) | `processing_stage` | Resemble AI, MIT license, 350M params, #1 HuggingFace trending, zero-shot voice cloning |
| Orpheus (Panel II) | `processing_stage` | Canopy Labs, Apache 2.0, 3B params, Llama backbone, emotion tags (laugh/sigh/gasp/cry), 200ms streaming latency |
| Kokoro (Panel III) | `processing_stage` | Hexgrad, Apache 2.0, 82M params, <1GB VRAM, ~$0.06/hr self-hosted, runs on CPU or cheap GPU |
| License Badges | `security_layer` | MIT and Apache 2.0 license indicators on each panel |
| Cost Comparison | `callout_box` | $0.10/min commercial to $0.001/min self-hosted -- 100x cost reduction |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Panel I Chatterbox | Panel II Orpheus | dashed | "quality spectrum" |
| Panel II Orpheus | Panel III Kokoro | dashed | "size/cost spectrum" |
| All Panels | Cost Comparison | arrow | "self-hosting economics" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "FROM $0.10/MIN TO $0.001/MIN" | Self-hosting these open-source models reduces TTS cost by 100x compared to commercial APIs. Kokoro at $0.06/hr on a commodity GPU delivers production-quality speech for pennies. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I CHATTERBOX"
- Label 2: "II ORPHEUS"
- Label 3: "III KOKORO"
- Label 4: "Resemble AI"
- Label 5: "350M params"
- Label 6: "MIT license"
- Label 7: "#1 HuggingFace"
- Label 8: "Zero-shot voice cloning"
- Label 9: "Canopy Labs"
- Label 10: "3B params"
- Label 11: "Apache 2.0"
- Label 12: "Emotion tags"
- Label 13: "200ms streaming"
- Label 14: "Hexgrad"
- Label 15: "82M params"
- Label 16: "<1GB VRAM"
- Label 17: "~$0.06/hr self-hosted"
- Label 18: "Runs on CPU or cheap GPU"

### Caption (for embedding in documentation)

Three-panel showcase of the open-source TTS revolution: Chatterbox (MIT, 350M, #1 HuggingFace), Orpheus (Apache 2.0, 3B, emotion tags, 200ms), and Kokoro (Apache 2.0, 82M, <1GB VRAM) -- reducing TTS cost by 100x through self-hosting.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `security_layer`, `callout_box` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Roman numerals I, II, III must be used for panel headers, not Arabic numerals.
10. Chatterbox is from Resemble AI with MIT license and 350M parameters -- do not confuse with other Resemble products or attribute to wrong company.
11. The "#1 HuggingFace" claim refers to trending position in mid-2025 -- present as historical fact, not current ranking.
12. Orpheus emotion tags include `<laugh>`, `<sigh>`, `<gasp>`, `<cry>` -- these are literal tokens in the model's vocabulary, not generic descriptions.
13. Orpheus uses a Llama-family backbone at 3B parameters with Apache 2.0 license -- by Canopy Labs. Do not confuse with the LLM Llama itself.
14. Kokoro has exactly 82M parameters, runs in <1GB VRAM -- by Hexgrad. Do not round up or inflate.
15. The $0.06/hr self-hosting cost for Kokoro assumes commodity GPU pricing (T4 or similar) -- not premium GPU tiers.
16. The 100x cost reduction ($0.10/min to $0.001/min) is approximate and depends on hardware and utilization -- present as order-of-magnitude comparison.

## Alt Text

Three-panel comparison of open-source TTS models for voice agent deployment: Chatterbox (MIT, 350M params), Orpheus (Apache 2.0, emotion tags, 200ms streaming), and Kokoro (82M params, $0.06/hr self-hosted), demonstrating 100x cost reduction over commercial speech synthesis APIs.

## Image Embed

![Three-panel comparison of open-source TTS models for voice agent deployment: Chatterbox (MIT, 350M params), Orpheus (Apache 2.0, emotion tags, 200ms streaming), and Kokoro (82M params, $0.06/hr self-hosted), demonstrating 100x cost reduction over commercial speech synthesis APIs.](docs/figures/repo-figures/assets/fig-voice-13-open-source-tts-revolution.jpg)

*Three-panel showcase of the open-source TTS revolution: Chatterbox (MIT, 350M, #1 HuggingFace), Orpheus (Apache 2.0, 3B, emotion tags, 200ms), and Kokoro (Apache 2.0, 82M, <1GB VRAM) -- reducing TTS cost by 100x through self-hosting.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-13",
    "title": "The Open-Source TTS Revolution",
    "audience": "L2",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Three open-source models -- Chatterbox, Orpheus, Kokoro -- make production-quality voice synthesis essentially free to self-host at 100x cost reduction.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Chatterbox",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["I CHATTERBOX", "Resemble AI", "MIT", "350M", "#1 HuggingFace"]
      },
      {
        "name": "Orpheus",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["II ORPHEUS", "Canopy Labs", "Apache 2.0", "3B", "emotion tags", "200ms"]
      },
      {
        "name": "Kokoro",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["III KOKORO", "Hexgrad", "Apache 2.0", "82M", "<1GB VRAM", "$0.06/hr"]
      }
    ],
    "relationships": [
      {
        "from": "Chatterbox",
        "to": "Orpheus",
        "type": "dashed",
        "label": "quality spectrum"
      },
      {
        "from": "Orpheus",
        "to": "Kokoro",
        "type": "dashed",
        "label": "size/cost spectrum"
      }
    ],
    "callout_boxes": [
      {
        "heading": "FROM $0.10/MIN TO $0.001/MIN",
        "body_text": "Self-hosting reduces TTS cost 100x compared to commercial APIs.",
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
- [ ] Layout template identified (B)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
