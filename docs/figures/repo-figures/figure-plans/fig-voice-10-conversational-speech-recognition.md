# fig-voice-10: Conversational Speech Recognition: The Paradigm Shift

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-10 |
| **Title** | Conversational Speech Recognition: The Paradigm Shift |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Compare the traditional fragmented speech recognition pipeline with the unified Conversational Speech Recognition (CSR) paradigm introduced by Deepgram Flux. Answers: "Why is CSR a paradigm shift from the traditional VAD->ASR->Endpointing->Stitcher chain, and what concrete improvements does it deliver?"

## Key Message

Traditional speech recognition fragments the problem into four disconnected stages (VAD, ASR, Endpointing, Stitcher), each introducing latency and error propagation. Deepgram Flux's CSR unifies acoustic and semantic streams into a single model achieving 260ms end-of-turn latency with 30% fewer false interruptions.

## Visual Concept

Split-panel layout (Template D). Left panel (visually muted/desaturated) shows the traditional fragmented pipeline as four separate boxes in a vertical chain: VAD -> ASR -> Endpointing -> Stitcher, each with its own error boundary and "fragile connection" markers between them. Right panel (full color, highlighted) shows Flux CSR as a unified model where acoustic stream and semantic stream merge into fused understanding. Vertical accent line divides panels. Bottom callout highlights the 260ms metric.

```
+-------------------------------------------------------------------+
|  THE PARADIGM SHIFT                                        [sq]   |
+-------------------------------+-----------------------------------+
|  TRADITIONAL (muted)          |  FLUX CSR (highlighted)           |
|                               |                                   |
|  Audio --> [VAD]              |  Audio --> [  UNIFIED CSR  ]      |
|              |                |            [   MODEL       ]      |
|       fragile connection      |            /             \        |
|           [ASR]               |   [Acoustic       [Semantic       |
|              |                |    Stream]         Stream]        |
|       fragile connection      |    prosody         grammar        |
|        [Endpointing]         |    pauses          intent         |
|              |                |            \             /        |
|       fragile connection      |         [Fused Understanding]     |
|         [Stitcher]           |              |                    |
|              |                |        Unified output             |
|        Fragmented output     |                                   |
|                               |                                   |
|  4 error boundaries          |  1 model, 1 error boundary       |
|  Each stage adds latency     |  260ms end-of-turn               |
|  Errors propagate forward    |  30% fewer false interruptions   |
+-------------------------------+-----------------------------------+
|  "260ms END-OF-TURN -- 30% fewer false interruptions"   [line]   |
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
    content: "THE PARADIGM SHIFT"
    role: title

  - id: left_panel
    bounds: [40, 140, 900, 720]
    content: "Traditional Pipeline"
    role: content_area

  - id: right_panel
    bounds: [980, 140, 900, 720]
    content: "Flux CSR"
    role: content_area

  - id: divider
    bounds: [940, 140, 2, 720]
    role: accent_line_v

  - id: callout_zone
    bounds: [40, 900, 1840, 140]
    content: "260ms END-OF-TURN"
    role: callout_box

anchors:
  - id: trad_vad
    position: [200, 220]
    size: [260, 90]
    role: processing_stage
    label: "VAD"

  - id: trad_asr
    position: [200, 340]
    size: [260, 90]
    role: processing_stage
    label: "ASR"

  - id: trad_endpointing
    position: [200, 460]
    size: [260, 90]
    role: processing_stage
    label: "Endpointing"

  - id: trad_stitcher
    position: [200, 580]
    size: [260, 90]
    role: processing_stage
    label: "Stitcher"

  - id: trad_output
    position: [200, 700]
    size: [260, 60]
    role: data_output
    label: "Fragmented output"

  - id: flux_model
    position: [1080, 220]
    size: [360, 160]
    role: selected_option
    label: "UNIFIED CSR MODEL"

  - id: flux_acoustic
    position: [1040, 420]
    size: [200, 100]
    role: data_flow
    label: "Acoustic Stream"

  - id: flux_semantic
    position: [1280, 420]
    size: [200, 100]
    role: data_flow
    label: "Semantic Stream"

  - id: flux_fused
    position: [1080, 560]
    size: [360, 100]
    role: decision_point
    label: "Fused Understanding"

  - id: flux_output
    position: [1080, 700]
    size: [360, 60]
    role: data_output
    label: "Unified output"

  - id: flow_vad_to_asr
    from: trad_vad
    to: trad_asr
    type: arrow
    label: "fragile connection"

  - id: flow_asr_to_ep
    from: trad_asr
    to: trad_endpointing
    type: arrow
    label: "fragile connection"

  - id: flow_ep_to_stitch
    from: trad_endpointing
    to: trad_stitcher
    type: arrow
    label: "fragile connection"

  - id: flow_stitch_to_out
    from: trad_stitcher
    to: trad_output
    type: arrow
    label: "stitched output"

  - id: flow_model_to_acoustic
    from: flux_model
    to: flux_acoustic
    type: arrow
    label: "acoustic features"

  - id: flow_model_to_semantic
    from: flux_model
    to: flux_semantic
    type: arrow
    label: "semantic features"

  - id: flow_acoustic_to_fused
    from: flux_acoustic
    to: flux_fused
    type: arrow
    label: "merge"

  - id: flow_semantic_to_fused
    from: flux_semantic
    to: flux_fused
    type: arrow
    label: "merge"

  - id: flow_fused_to_out
    from: flux_fused
    to: flux_output
    type: arrow
    label: "unified output"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Traditional VAD | `processing_stage` | Voice activity detection -- first stage, detects speech vs silence |
| Traditional ASR | `processing_stage` | Automatic speech recognition -- transcribes detected speech segments |
| Traditional Endpointing | `processing_stage` | Turn boundary detection -- determines when speaker finishes |
| Traditional Stitcher | `processing_stage` | Transcript assembly -- combines fragments into coherent output |
| Flux CSR Unified Model | `selected_option` | Single model ingesting raw audio, replacing all four traditional stages |
| Acoustic Stream | `data_flow` | Sub-component: processes audio features (prosody, pauses, intonation) |
| Semantic Stream | `data_flow` | Sub-component: processes linguistic meaning (grammar, intent completion) |
| Fused Understanding | `decision_point` | Merged acoustic+semantic signal producing unified transcript with turn boundaries |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Traditional VAD | Traditional ASR | arrow | "fragile connection" |
| Traditional ASR | Traditional Endpointing | arrow | "fragile connection" |
| Traditional Endpointing | Traditional Stitcher | arrow | "fragile connection" |
| Flux CSR Unified Model | Acoustic Stream | arrow | "acoustic features" |
| Flux CSR Unified Model | Semantic Stream | arrow | "semantic features" |
| Acoustic Stream | Fused Understanding | arrow | "prosody, pauses, intonation" |
| Semantic Stream | Fused Understanding | arrow | "grammar, intent, context" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "260ms END-OF-TURN" | Deepgram Flux CSR achieves 260ms end-of-turn latency with 30% fewer false interruptions compared to traditional fragmented pipelines. One model, one error boundary, one optimization target. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "TRADITIONAL"
- Label 2: "FLUX CSR"
- Label 3: "VAD"
- Label 4: "ASR"
- Label 5: "Endpointing"
- Label 6: "Stitcher"
- Label 7: "UNIFIED CSR MODEL"
- Label 8: "Acoustic Stream"
- Label 9: "Semantic Stream"
- Label 10: "Fused Understanding"
- Label 11: "4 error boundaries"
- Label 12: "1 model, 1 error boundary"
- Label 13: "260ms end-of-turn"
- Label 14: "30% fewer interruptions"
- Label 15: "Errors propagate forward"
- Label 16: "Fragmented output"
- Label 17: "Unified output"
- Label 18: "fragile connection"
- Label 19: "prosody, pauses"
- Label 20: "grammar, intent"

### Caption (for embedding in documentation)

Split-panel comparison of traditional fragmented speech recognition pipeline (VAD, ASR, Endpointing, Stitcher) versus Deepgram Flux Conversational Speech Recognition unified model with acoustic and semantic stream fusion achieving 260ms end-of-turn latency.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `data_output`, `data_flow`, `decision_point`, `selected_option` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The left panel (traditional) must be visually muted/desaturated compared to the right panel (Flux CSR) to convey the paradigm shift directionality.
10. The 260ms end-of-turn latency is from Deepgram Flux/Nova-3 announcements -- do not alter this value.
11. The 30% fewer false interruptions is Deepgram's claimed improvement over traditional endpointing -- do not present as an independent benchmark.
12. "CSR" stands for Conversational Speech Recognition -- Deepgram's terminology. Do not expand it differently.
13. The four traditional stages (VAD, ASR, Endpointing, Stitcher) are a standard decomposition in speech processing literature -- do not add or remove stages.
14. The acoustic and semantic streams within Flux CSR are conceptual -- the exact internal architecture is proprietary. Present as a conceptual diagram.
15. Neither architecture is shown as "wrong" but the traditional side should feel outdated via visual treatment (muted colors, smaller type).
16. "Fragile connection" markers between traditional stages emphasize error propagation -- each boundary is a potential failure point.

## Alt Text

Split-panel comparison of traditional fragmented speech recognition pipeline (VAD, ASR, Endpointing, Stitcher) versus Deepgram Flux Conversational Speech Recognition unified model fusing acoustic and semantic streams for 260ms end-of-turn latency.

## Image Embed

![Split-panel comparison of traditional fragmented speech recognition pipeline (VAD, ASR, Endpointing, Stitcher) versus Deepgram Flux Conversational Speech Recognition unified model fusing acoustic and semantic streams for 260ms end-of-turn latency.](docs/figures/repo-figures/assets/fig-voice-10-conversational-speech-recognition.jpg)

*Split-panel comparison of traditional fragmented speech recognition pipeline (VAD, ASR, Endpointing, Stitcher) versus Deepgram Flux Conversational Speech Recognition unified model with acoustic and semantic stream fusion achieving 260ms end-of-turn latency.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-10",
    "title": "Conversational Speech Recognition: The Paradigm Shift",
    "audience": "L3",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Flux CSR unifies four fragmented speech stages into one model achieving 260ms end-of-turn with 30% fewer false interruptions.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Traditional Pipeline",
        "role": "branching_path",
        "is_highlighted": false,
        "labels": ["TRADITIONAL", "VAD -> ASR -> Endpointing -> Stitcher"]
      },
      {
        "name": "Flux CSR",
        "role": "branching_path",
        "is_highlighted": true,
        "labels": ["FLUX CSR", "UNIFIED CSR MODEL"]
      },
      {
        "name": "Traditional VAD",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["VAD"]
      },
      {
        "name": "Traditional ASR",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["ASR"]
      },
      {
        "name": "Traditional Endpointing",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Endpointing"]
      },
      {
        "name": "Traditional Stitcher",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Stitcher"]
      },
      {
        "name": "Acoustic Stream",
        "role": "data_flow",
        "is_highlighted": true,
        "labels": ["Acoustic Stream", "prosody, pauses"]
      },
      {
        "name": "Semantic Stream",
        "role": "data_flow",
        "is_highlighted": true,
        "labels": ["Semantic Stream", "grammar, intent"]
      },
      {
        "name": "Fused Understanding",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["Fused Understanding"]
      }
    ],
    "relationships": [
      {
        "from": "Traditional VAD",
        "to": "Traditional ASR",
        "type": "arrow",
        "label": "fragile connection"
      },
      {
        "from": "Traditional ASR",
        "to": "Traditional Endpointing",
        "type": "arrow",
        "label": "fragile connection"
      },
      {
        "from": "Traditional Endpointing",
        "to": "Traditional Stitcher",
        "type": "arrow",
        "label": "fragile connection"
      },
      {
        "from": "Flux CSR Unified Model",
        "to": "Acoustic Stream",
        "type": "arrow",
        "label": "acoustic features"
      },
      {
        "from": "Flux CSR Unified Model",
        "to": "Semantic Stream",
        "type": "arrow",
        "label": "semantic features"
      },
      {
        "from": "Acoustic Stream",
        "to": "Fused Understanding",
        "type": "arrow",
        "label": "prosody, pauses, intonation"
      },
      {
        "from": "Semantic Stream",
        "to": "Fused Understanding",
        "type": "arrow",
        "label": "grammar, intent, context"
      }
    ],
    "callout_boxes": [
      {
        "heading": "260ms END-OF-TURN",
        "body_text": "30% fewer false interruptions compared to traditional fragmented pipelines.",
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
- [ ] Layout template identified (D)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
