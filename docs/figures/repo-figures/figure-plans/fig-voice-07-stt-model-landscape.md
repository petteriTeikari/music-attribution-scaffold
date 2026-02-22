# fig-voice-07: STT Model Landscape (Feb 2026)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-07 |
| **Title** | STT Model Landscape (Feb 2026) |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Map the current STT model landscape as a four-quadrant positioning chart showing accuracy versus cost, with models placed to reveal the tradeoff clusters and identify best-in-class for production, self-hosted, and edge deployment scenarios. Answers: "Which STT model should we choose, and what are the tradeoff axes?"

## Key Message

The STT landscape stratifies into four quadrants -- Canary-Qwen leads accuracy (5.63% WER), Deepgram leads production readiness, Faster-Whisper leads self-hosted, and Moonshine leads edge deployment.

## Visual Concept

Four-quadrant chart (Template B adapted as positioning map). X-axis: Cost (left=free/self-hosted, right=paid API). Y-axis: Accuracy (bottom=higher WER, top=lower WER). Models positioned as labeled nodes within the quadrants. Top-left quadrant: "BEST ACCURACY, SELF-HOSTED" (Canary-Qwen, Voxtral). Top-right quadrant: "BEST ACCURACY, MANAGED" (Deepgram Nova-3, Speechmatics). Bottom-left quadrant: "GOOD ENOUGH, SELF-HOSTED" (Whisper, Faster-Whisper). Bottom-right quadrant: "EDGE / EMBEDDED" (Moonshine). Each model node shows name and key metric. Coral accent lines on the quadrant axes. A callout strip at the bottom summarizes the four recommendations.

```
+---------------------------------------------------------------------+
|  STT MODEL LANDSCAPE                                         [sq]   |
|  (FEB 2026)                                                         |
|                                                                     |
|  HIGH ACCURACY                                                      |
|  (low WER)                                                          |
|       |                                                             |
|       |  Canary-Qwen        |  Deepgram Nova-3                     |
|       |  (5.63% WER)        |  (streaming, API)                    |
|       |                     |                                       |
|       |  Voxtral            |  Speechmatics                        |
|       |  (Mistral, 7B)      |  (real-time)                         |
|       |                     |                                       |
|  -----+---------------------+------ COST -->                        |
|       |                     |                                       |
|       |  Whisper (v3-turbo) |                                       |
|       |  Faster-Whisper     |                                       |
|       |  (CTranslate2)      |                                       |
|       |                     |  Moonshine                            |
|       |  (self-hosted)      |  (edge, 17ms/chunk)                  |
|       |                     |                                       |
|  LOW ACCURACY                                                       |
|  (high WER)                                                         |
|                                                                     |
|  ACCURACY: CANARY-QWEN 5.63% / PRODUCTION: DEEPGRAM /       [line] |
|  SELF-HOSTED: FASTER-WHISPER / EDGE: MOONSHINE                      |
+---------------------------------------------------------------------+
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
    content: "STT MODEL LANDSCAPE (FEB 2026)"
    role: title

  - id: quadrant_zone
    bounds: [80, 140, 1760, 700]
    role: content_area

  - id: callout_zone
    bounds: [80, 880, 1760, 160]
    content: "STT Recommendations Summary"
    role: callout_box

anchors:
  - id: y_axis
    position: [480, 160]
    size: [2, 680]
    role: accent_line
    label: "Accuracy (inverse WER)"

  - id: x_axis
    position: [100, 520]
    size: [1720, 2]
    role: accent_line
    label: "Cost (free -> paid API)"

  - id: quadrant_tl_label
    position: [120, 180]
    size: [340, 40]
    role: annotation
    label: "BEST ACCURACY, SELF-HOSTED"

  - id: quadrant_tr_label
    position: [520, 180]
    size: [340, 40]
    role: annotation
    label: "BEST ACCURACY, MANAGED"

  - id: quadrant_bl_label
    position: [120, 560]
    size: [340, 40]
    role: annotation
    label: "GOOD ENOUGH, SELF-HOSTED"

  - id: quadrant_br_label
    position: [520, 560]
    size: [340, 40]
    role: annotation
    label: "EDGE / EMBEDDED"

  - id: node_canary_qwen
    position: [180, 260]
    size: [260, 80]
    role: selected_option
    label: "CANARY-QWEN"

  - id: node_voxtral
    position: [180, 380]
    size: [260, 80]
    role: processing_stage
    label: "VOXTRAL"

  - id: node_deepgram
    position: [600, 260]
    size: [260, 80]
    role: selected_option
    label: "DEEPGRAM NOVA-3"

  - id: node_speechmatics
    position: [600, 380]
    size: [260, 80]
    role: processing_stage
    label: "SPEECHMATICS"

  - id: node_whisper
    position: [180, 580]
    size: [260, 80]
    role: processing_stage
    label: "WHISPER V3-TURBO"

  - id: node_faster_whisper
    position: [180, 700]
    size: [260, 80]
    role: selected_option
    label: "FASTER-WHISPER"

  - id: node_moonshine
    position: [600, 680]
    size: [260, 80]
    role: selected_option
    label: "MOONSHINE"

  - id: recommendation_bar
    position: [80, 900]
    size: [1760, 120]
    role: callout_box
    label: "STT RECOMMENDATIONS"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Accuracy Axis (Y) | `accent_line` | Vertical axis: low WER at top, high WER at bottom |
| Cost Axis (X) | `accent_line` | Horizontal axis: free/self-hosted at left, paid API at right |
| Canary-Qwen Node | `selected_option` | NVIDIA Canary-Qwen, 5.63% WER, best accuracy (Feb 2026) |
| Voxtral Node | `processing_stage` | Mistral Voxtral, 7B parameter model, competitive accuracy |
| Deepgram Nova-3 Node | `selected_option` | Deepgram Nova-3, streaming API, production-grade |
| Speechmatics Node | `processing_stage` | Speechmatics real-time API, enterprise-grade |
| Whisper v3-turbo Node | `processing_stage` | OpenAI Whisper v3-turbo, open-source baseline |
| Faster-Whisper Node | `selected_option` | CTranslate2 optimized Whisper, best self-hosted option |
| Moonshine Node | `selected_option` | Useful Sensors Moonshine, edge-optimized, 17ms per chunk |
| Recommendations Bar | `callout_box` | Summary of four category leaders |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| Whisper | Faster-Whisper | dashed | "CTranslate2 optimization" |
| Canary-Qwen | Deepgram Nova-3 | none | "accuracy vs production trade" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "STT RECOMMENDATIONS" | ACCURACY: Canary-Qwen (5.63% WER, NVIDIA). PRODUCTION: Deepgram Nova-3 (streaming API, lowest integration friction). SELF-HOSTED: Faster-Whisper (CTranslate2, no API cost). EDGE: Moonshine (17ms/chunk, runs on-device). | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "STT MODEL LANDSCAPE"
- Label 2: "FEB 2026"
- Label 3: "ACCURACY (inverse WER)"
- Label 4: "COST"
- Label 5: "CANARY-QWEN"
- Label 6: "5.63% WER"
- Label 7: "VOXTRAL"
- Label 8: "Mistral, 7B"
- Label 9: "DEEPGRAM NOVA-3"
- Label 10: "Streaming API"
- Label 11: "SPEECHMATICS"
- Label 12: "Real-time"
- Label 13: "WHISPER V3-TURBO"
- Label 14: "Open-source baseline"
- Label 15: "FASTER-WHISPER"
- Label 16: "CTranslate2 optimized"
- Label 17: "MOONSHINE"
- Label 18: "Edge, 17ms/chunk"
- Label 19: "BEST ACCURACY, SELF-HOSTED"
- Label 20: "BEST ACCURACY, MANAGED"
- Label 21: "GOOD ENOUGH, SELF-HOSTED"
- Label 22: "EDGE / EMBEDDED"

### Caption

Four-quadrant STT model positioning chart showing accuracy versus cost for Feb 2026, with category leaders identified for production, self-hosted, accuracy-optimized, and edge deployment scenarios.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text
3. **Hex codes are INTERNAL** -- do NOT render them
4. **Background MUST be warm cream (#f6f3e6)**
5. **No generic flowchart aesthetics**
6. **No figure captions** -- no "Figure 1." prefix
7. **No prompt leakage**

### Figure-Specific Rules

8. Models must be positioned APPROXIMATELY correctly in their quadrants -- do not place them randomly.
9. WER percentages are the PRIMARY metric -- they must appear next to model names where known.
10. The four quadrant labels must be visible and serve as category headers.
11. "Feb 2026" is a temporal qualifier -- this landscape changes rapidly and the date is critical context.
12. Do NOT show company logos -- text nodes only.
13. Category leaders (Canary-Qwen, Deepgram, Faster-Whisper, Moonshine) should use `selected_option` semantic tag to distinguish them from other models.
14. The axes should use coral accent lines, not generic black lines.

## Alt Text

Four-quadrant positioning chart of speech-to-text models (Feb 2026) mapping accuracy versus cost, with Canary-Qwen leading accuracy at 5.63% WER, Deepgram Nova-3 for production, Faster-Whisper for self-hosted, and Moonshine for edge deployment.

## Image Embed

![Four-quadrant positioning chart of speech-to-text models (Feb 2026) mapping accuracy versus cost, with Canary-Qwen leading accuracy at 5.63% WER, Deepgram Nova-3 for production, Faster-Whisper for self-hosted, and Moonshine for edge deployment.](docs/figures/repo-figures/assets/fig-voice-07-stt-model-landscape.jpg)

*Four-quadrant STT model positioning chart showing accuracy versus cost for Feb 2026, with category leaders identified for production, self-hosted, accuracy-optimized, and edge deployment scenarios.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-07",
    "title": "STT Model Landscape (Feb 2026)",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "The STT landscape stratifies into four quadrants with distinct category leaders for accuracy, production, self-hosted, and edge.",
    "layout_flow": "quadrant-positioning",
    "key_structures": [
      {
        "name": "Canary-Qwen",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["CANARY-QWEN", "5.63% WER", "NVIDIA"]
      },
      {
        "name": "Deepgram Nova-3",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["DEEPGRAM NOVA-3", "Streaming API"]
      },
      {
        "name": "Voxtral",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["VOXTRAL", "Mistral, 7B"]
      },
      {
        "name": "Speechmatics",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["SPEECHMATICS", "Real-time"]
      },
      {
        "name": "Whisper v3-turbo",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["WHISPER V3-TURBO", "Open-source baseline"]
      },
      {
        "name": "Faster-Whisper",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["FASTER-WHISPER", "CTranslate2"]
      },
      {
        "name": "Moonshine",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["MOONSHINE", "Edge, 17ms/chunk"]
      }
    ],
    "relationships": [
      {
        "from": "Whisper",
        "to": "Faster-Whisper",
        "type": "dashed",
        "label": "CTranslate2 optimization"
      }
    ],
    "callout_boxes": [
      {
        "heading": "STT RECOMMENDATIONS",
        "body_text": "ACCURACY: Canary-Qwen 5.63% WER. PRODUCTION: Deepgram Nova-3. SELF-HOSTED: Faster-Whisper. EDGE: Moonshine.",
        "position": "bottom-full-width"
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
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
