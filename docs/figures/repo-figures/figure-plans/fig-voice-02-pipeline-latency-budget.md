# fig-voice-02: Voice Agent Latency Budget

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-02 |
| **Title** | Voice Agent Latency Budget |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps / Vertical Signal Chain) |

## Purpose

Show the time budget for each pipeline stage, demonstrating how 500ms total latency is achieved. Answers: "How much time does each voice pipeline stage consume, and what is the cumulative budget?"

## Key Message

Production voice agents target <500ms total latency -- VAD (<100ms) + STT (<250ms) + LLM TTFT (<200ms) + TTS TTFA (<100ms) + Transport (<50ms).

## Visual Concept

Vertical timeline (Template E) showing sequential processing stages with time bars. Each stage is a horizontal bar whose width represents latency. Cumulative total shown as running counter. Target line at 500ms and 800ms thresholds. Coral accent squares at stage boundaries. A "Best Available" summary at the bottom shows concrete Feb 2026 numbers.

```
+-------------------------------------------+
|  LATENCY BUDGET                           |
|  TARGET: <500ms                    [sq]   |
|                                           |
|  +-- VAD ----------+ <100ms               |
|  |                                        |
|  +-- STT ----------------------+ <250ms   |
|  |                                        |
|  +-- LLM TTFT ----------------+ <200ms    |
|  |                                        |
|  +-- TTS TTFA ----------+ <100ms          |
|  |                                        |
|  +-- TRANSPORT ------+ <50ms              |
|  |                                        |
|  +----------------------------+ 500ms     |
|  |            ^ TARGET        |           |
|  +----------------------------------+ 800 |
|  |                   ^ ACCEPTABLE   |     |
|                                           |
|  BEST AVAILABLE (FEB 2026):               |
|  Silero 4ms + Flux 260ms +               |
|  Haiku 150ms + Sonic 40ms +              |
|  WebRTC 30ms = ~484ms            [line]   |
+-------------------------------------------+
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
    content: "LATENCY BUDGET"
    role: title

  - id: timeline_zone
    bounds: [80, 140, 1200, 680]
    role: content_area

  - id: threshold_zone
    bounds: [1320, 140, 560, 680]
    role: content_area
    content: "Thresholds and cumulative"

  - id: best_available_zone
    bounds: [80, 860, 1760, 160]
    content: "Best Available Feb 2026"
    role: callout_box

anchors:
  - id: vad_bar
    position: [160, 200]
    size: [280, 80]
    role: processing_stage
    label: "VAD <100ms"

  - id: stt_bar
    position: [160, 320]
    size: [700, 80]
    role: processing_stage
    label: "STT <250ms"

  - id: llm_bar
    position: [160, 440]
    size: [560, 80]
    role: processing_stage
    label: "LLM TTFT <200ms"

  - id: tts_bar
    position: [160, 560]
    size: [280, 80]
    role: processing_stage
    label: "TTS TTFA <100ms"

  - id: transport_bar
    position: [160, 680]
    size: [140, 80]
    role: processing_stage
    label: "Transport <50ms"

  - id: target_line_500
    position: [1400, 140]
    size: [2, 680]
    role: confidence_high
    label: "500ms TARGET"

  - id: acceptable_line_800
    position: [1600, 140]
    size: [2, 680]
    role: confidence_medium
    label: "800ms ACCEPTABLE"

  - id: flow_vad_to_stt
    from: vad_bar
    to: stt_bar
    type: arrow
    label: "sequential"

  - id: flow_stt_to_llm
    from: stt_bar
    to: llm_bar
    type: arrow
    label: "sequential"

  - id: flow_llm_to_tts
    from: llm_bar
    to: tts_bar
    type: arrow
    label: "sequential"

  - id: flow_tts_to_transport
    from: tts_bar
    to: transport_bar
    type: arrow
    label: "sequential"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| VAD Stage | `processing_stage` | Voice activity detection, <100ms target |
| STT Stage | `processing_stage` | Speech-to-text transcription, <250ms target |
| LLM TTFT | `processing_stage` | Time to first token from LLM, <200ms target |
| TTS TTFA | `processing_stage` | Time to first audio from TTS, <100ms target |
| Transport | `processing_stage` | Network + codec overhead, <50ms target |
| 500ms Target Line | `confidence_high` | Natural conversation threshold |
| 800ms Acceptable Line | `confidence_medium` | Acceptable production threshold |
| Best Available Summary | `data_flow` | Concrete Feb 2026 stack achieving ~484ms |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| VAD Stage | STT Stage | arrow | "sequential pipeline" |
| STT Stage | LLM TTFT | arrow | "transcript ready" |
| LLM TTFT | TTS TTFA | arrow | "first token" |
| TTS TTFA | Transport | arrow | "first audio chunk" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "BEST AVAILABLE (FEB 2026)" | Silero 4ms + Deepgram Flux 260ms + Haiku 150ms + Cartesia Sonic Turbo 40ms + WebRTC 30ms = ~484ms total. | bottom-center |
| "TARGET THRESHOLDS" | 500ms = natural conversation feel. 800ms = acceptable for task-oriented agents. >1000ms = user perceives delay. | right-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "VAD <100ms"
- Label 2: "STT <250ms"
- Label 3: "LLM TTFT <200ms"
- Label 4: "TTS TTFA <100ms"
- Label 5: "TRANSPORT <50ms"
- Label 6: "500ms TARGET"
- Label 7: "800ms ACCEPTABLE"
- Label 8: "Silero 4ms"
- Label 9: "Deepgram Flux 260ms"
- Label 10: "Haiku 150ms"
- Label 11: "Cartesia Sonic Turbo 40ms"
- Label 12: "WebRTC 30ms"
- Label 13: "~484ms TOTAL"

### Caption (for embedding in documentation)

Vertical timeline showing the voice agent latency budget across five pipeline stages, targeting under 500 milliseconds total with concrete Feb 2026 best-available stack achieving ~484ms.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `confidence_high`, `confidence_medium` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Latency values are targets, not guarantees. Use "<" prefix for targets (e.g., "<100ms") and "~" for measured totals (e.g., "~484ms").
10. Bar widths must be proportional to their latency values -- STT bar must be visibly wider than VAD bar.
11. Provider names (Silero, Deepgram, Cartesia) appear ONLY in the "Best Available" callout, not in the main timeline bars.
12. The 500ms target line should use `confidence_high` semantic (green), the 800ms line should use `confidence_medium` semantic (amber).
13. TTFT = Time To First Token. TTFA = Time To First Audio. These abbreviations are acceptable for L3 audience.

## Alt Text

Vertical latency budget diagram for a real-time voice agent pipeline showing VAD, speech-to-text, LLM, text-to-speech, and transport stages targeting under 500ms total, with best-available Feb 2026 stack achieving 484ms.

## Image Embed

![Vertical latency budget diagram for a real-time voice agent pipeline showing VAD, speech-to-text, LLM, text-to-speech, and transport stages targeting under 500ms total, with best-available Feb 2026 stack achieving 484ms.](docs/figures/repo-figures/assets/fig-voice-02-pipeline-latency-budget.jpg)

*Vertical timeline showing the voice agent latency budget across five pipeline stages, targeting under 500 milliseconds total with concrete Feb 2026 best-available stack achieving ~484ms.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-02",
    "title": "Voice Agent Latency Budget",
    "audience": "L3",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Production voice agents target <500ms total latency across five sequential pipeline stages.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "VAD Stage",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["VAD <100ms"]
      },
      {
        "name": "STT Stage",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["STT <250ms"]
      },
      {
        "name": "LLM TTFT",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["LLM TTFT <200ms"]
      },
      {
        "name": "TTS TTFA",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["TTS TTFA <100ms"]
      },
      {
        "name": "Transport",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["TRANSPORT <50ms"]
      },
      {
        "name": "500ms Target",
        "role": "confidence_high",
        "is_highlighted": true,
        "labels": ["500ms TARGET"]
      },
      {
        "name": "800ms Acceptable",
        "role": "confidence_medium",
        "is_highlighted": false,
        "labels": ["800ms ACCEPTABLE"]
      }
    ],
    "relationships": [
      {
        "from": "VAD Stage",
        "to": "STT Stage",
        "type": "arrow",
        "label": "sequential pipeline"
      },
      {
        "from": "STT Stage",
        "to": "LLM TTFT",
        "type": "arrow",
        "label": "transcript ready"
      },
      {
        "from": "LLM TTFT",
        "to": "TTS TTFA",
        "type": "arrow",
        "label": "first token"
      },
      {
        "from": "TTS TTFA",
        "to": "Transport",
        "type": "arrow",
        "label": "first audio chunk"
      }
    ],
    "callout_boxes": [
      {
        "heading": "BEST AVAILABLE (FEB 2026)",
        "body_text": "Silero 4ms + Deepgram Flux 260ms + Haiku 150ms + Cartesia Sonic Turbo 40ms + WebRTC 30ms = ~484ms total.",
        "position": "bottom-center"
      },
      {
        "heading": "TARGET THRESHOLDS",
        "body_text": "500ms = natural conversation. 800ms = acceptable task-oriented. >1000ms = perceptible delay.",
        "position": "right-center"
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
- [ ] Layout template identified (E)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
