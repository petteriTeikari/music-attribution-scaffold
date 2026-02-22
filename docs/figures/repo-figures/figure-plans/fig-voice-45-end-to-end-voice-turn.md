# fig-voice-45: End-to-End Voice Turn Anatomy

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-45 |
| **Title** | End-to-End Voice Turn Anatomy |
| **Audience** | L2 (Technical Product Manager) |
| **Location** | docs/tutorials/voice-agent-implementation.md, Section 2.1 |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Show a single user utterance traversing 7 processing steps to produce an agent response, annotated with latency budget at each hop. The ASCII pipeline diagram shows structure; this shows timing. Answers: "How fast is voice-to-voice, and where does the time go?"

## Key Message

A single voice turn traverses 7 processing steps in under 500ms (target): VAD (4ms) -> STT (150-300ms) -> Context Aggregation (5ms) -> LLM TTFT (100-200ms) -> Drift Check (10ms) -> TTS TTFA (40-200ms) -> Transport (30-80ms). Total: 339-799ms depending on stack choice.

## Visual Concept

Steps (Template E) flowing left-to-right with a horizontal timeline. 7 labeled steps with cumulative latency shown as a running total bar. Each step has: step name, component, latency range. Below the timeline: "Target: <500ms voice-to-voice" callout. Two stacked rows: top shows the open-source stack timings, bottom shows the commercial stack timings for comparison.

```
+-----------------------------------------------------------------------+
|  END-TO-END VOICE TURN ANATOMY                                   [sq]  |
|  -- 7 Steps from Utterance to Response                                 |
+-----------------------------------------------------------------------+
|                                                                        |
|  [user mic]                                                            |
|     |                                                                  |
|  ┌──┴──┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌─────┐ |
|  │ VAD  │->│ STT  │->│ CTX  │->│ LLM  │->│DRIFT │->│ TTS  │->│TRNS │ |
|  │ 4ms  │  │150-  │  │ ~5ms │  │100-  │  │~10ms │  │ 40-  │  │ 30- │ |
|  │      │  │300ms │  │      │  │200ms │  │      │  │200ms │  │80ms │ |
|  └──────┘  └──────┘  └──────┘  └──────┘  └──────┘  └──────┘  └─────┘ |
|                                                                        |
|  CUMULATIVE LATENCY BAR                                                |
|  ═══════════════════════════════════════════════════════|═══ 500ms     |
|                                                                        |
|  OPEN-SOURCE  4 + 300 + 5 + 200 + 10 + 200 + 80 = 799ms    [exceeds] |
|  COMMERCIAL   4 + 150 + 5 + 150 + 10 +  40 + 30 = 389ms    [within]  |
|                                                                        |
+-----------------------------------------------------------------------+
|  ELI5: Like a relay race with 7 runners -- the baton passes      [sq]  |
|  from mic through seven specialists in under half a second.            |
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
    content: "END-TO-END VOICE TURN ANATOMY"
    role: title

  - id: steps_zone
    bounds: [40, 140, 1840, 380]
    role: content_area

  - id: cumulative_bar_zone
    bounds: [40, 540, 1840, 80]
    role: content_area

  - id: comparison_zone
    bounds: [40, 640, 1840, 200]
    role: content_area

  - id: callout_zone
    bounds: [40, 940, 1840, 100]
    content: "ELI5: Like a relay race with 7 runners"
    role: callout_box

anchors:
  - id: step_vad
    position: [140, 320]
    size: [200, 160]
    role: processing_stage
    label: "VAD Detection"

  - id: step_stt
    position: [400, 320]
    size: [200, 160]
    role: processing_stage
    label: "Speech-to-Text"

  - id: step_ctx
    position: [660, 320]
    size: [200, 160]
    role: processing_stage
    label: "Context Aggregation"

  - id: step_llm
    position: [920, 320]
    size: [200, 160]
    role: decision_point
    label: "LLM Inference (TTFT)"

  - id: step_drift
    position: [1180, 320]
    size: [200, 160]
    role: processing_stage
    label: "Drift Check"

  - id: step_tts
    position: [1440, 320]
    size: [200, 160]
    role: processing_stage
    label: "Text-to-Speech (TTFA)"

  - id: step_transport
    position: [1700, 320]
    size: [200, 160]
    role: data_flow
    label: "Transport Out"

  - id: target_line
    position: [40, 580]
    size: [1840, 2]
    role: accent_line
    label: "500ms target threshold"

  - id: oss_row
    position: [140, 680]
    size: [1600, 60]
    role: data_flow
    label: "Open-source: 799ms"

  - id: commercial_row
    position: [140, 760]
    size: [1600, 60]
    role: data_flow
    label: "Commercial: 389ms"

  - id: arrow_vad_stt
    from: step_vad
    to: step_stt
    type: arrow
    label: "audio frames"

  - id: arrow_stt_ctx
    from: step_stt
    to: step_ctx
    type: arrow
    label: "transcript"

  - id: arrow_ctx_llm
    from: step_ctx
    to: step_llm
    type: arrow
    label: "enriched prompt"

  - id: arrow_llm_drift
    from: step_llm
    to: step_drift
    type: arrow
    label: "LLM tokens"

  - id: arrow_drift_tts
    from: step_drift
    to: step_tts
    type: arrow
    label: "validated text"

  - id: arrow_tts_transport
    from: step_tts
    to: step_transport
    type: arrow
    label: "audio chunks"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "END-TO-END VOICE TURN ANATOMY" with coral accent square |
| VAD Detection step | `processing_stage` | Silero VAD, 4ms RTF |
| Speech-to-Text step | `processing_stage` | Whisper 150-300ms / Deepgram 150ms |
| Context Aggregation step | `processing_stage` | ContextAggregator, ~5ms |
| LLM Inference step | `decision_point` | TTFT 100-200ms, varies by model |
| Drift Check step | `processing_stage` | DriftDetector, ~10ms (optional) |
| Text-to-Speech step | `processing_stage` | Piper 200ms / Cartesia 40ms |
| Transport Out step | `data_flow` | WebSocket 80ms / WebRTC 30ms |
| Cumulative latency bar | `data_mono` | Running total with 500ms target line |
| Open-source total | `data_flow` | 4+300+5+200+10+200+80 = 799ms |
| Commercial total | `data_flow` | 4+150+5+150+10+40+30 = 389ms |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| VAD | STT | arrow | "audio frames" |
| STT | Context | arrow | "transcript" |
| Context | LLM | arrow | "enriched prompt" |
| LLM | Drift | arrow | "LLM tokens" |
| Drift | TTS | arrow | "validated text" |
| TTS | Transport | arrow | "audio chunks" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Think of a voice turn like a relay race with 7 runners: the baton passes from the microphone through seven specialists, each adding their time. The goal is to complete the entire relay in under half a second -- faster than a drummer's hi-hat stroke. | bottom-center |
| "TARGET" | <500ms voice-to-voice | below cumulative bar |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "VAD Detection"
- Label 2: "Speech-to-Text"
- Label 3: "Context Aggregation"
- Label 4: "LLM Inference (TTFT)"
- Label 5: "Drift Check"
- Label 6: "Text-to-Speech (TTFA)"
- Label 7: "Transport Out"
- Label 8: "Silero VAD, 4ms RTF"
- Label 9: "Whisper / Deepgram"
- Label 10: "ContextAggregator ~5ms"
- Label 11: "100-200ms varies by model"
- Label 12: "DriftDetector ~10ms"
- Label 13: "Piper 200ms / Cartesia 40ms"
- Label 14: "WebSocket / WebRTC"
- Label 15: "Open-source: 799ms total"
- Label 16: "Commercial: 389ms total"
- Label 17: "Target: <500ms"

### Caption (for embedding in documentation)

End-to-end voice turn anatomy showing 7 processing steps from user utterance to agent response, with per-step latency budgets and cumulative totals for both open-source (799ms) and commercial (389ms) stacks against a 500ms target.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `decision_point`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "VAD", "STT", "TTS", "TTFT", "TTFA" are appropriate for L2 audience but should include full expansions on first use.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text in the figure.

### Figure-Specific Rules

9. Latency values must match the ranges stated: VAD 4ms, STT 150-300ms, Context 5ms, LLM 100-200ms, Drift 10ms, TTS 40-200ms, Transport 30-80ms.
10. The timeline must show cumulative latency, not just per-step values.
11. The 500ms target line must be visually prominent as a threshold marker.
12. Both open-source and commercial stacks must be shown for comparison with distinct totals (799ms and 389ms).

## Alt Text

Seven-step voice turn pipeline from VAD to transport, comparing open-source 799ms vs commercial 389ms against 500ms target.

## Image Embed

![Seven-step voice turn pipeline from VAD to transport, comparing open-source 799ms vs commercial 389ms against 500ms target.](docs/figures/repo-figures/assets/fig-voice-45-end-to-end-voice-turn.jpg)

*End-to-end voice turn anatomy showing 7 processing steps from user utterance to agent response, with per-step latency budgets and cumulative totals for both open-source (799ms) and commercial (389ms) stacks against a 500ms target.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-45",
    "title": "End-to-End Voice Turn Anatomy",
    "audience": "L2",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "A single voice turn traverses 7 processing steps in under 500ms (target): VAD, STT, Context, LLM, Drift, TTS, Transport. Open-source totals 799ms; commercial totals 389ms.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "VAD Detection",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["VAD Detection", "Silero VAD, 4ms RTF"]
      },
      {
        "name": "Speech-to-Text",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Speech-to-Text", "Whisper / Deepgram"]
      },
      {
        "name": "Context Aggregation",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Context Aggregation", "~5ms"]
      },
      {
        "name": "LLM Inference",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["LLM Inference (TTFT)", "100-200ms"]
      },
      {
        "name": "Drift Check",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Drift Check", "~10ms"]
      },
      {
        "name": "Text-to-Speech",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Text-to-Speech (TTFA)", "Piper / Cartesia"]
      },
      {
        "name": "Transport Out",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["Transport Out", "WebSocket / WebRTC"]
      }
    ],
    "relationships": [
      {"from": "VAD", "to": "STT", "type": "arrow", "label": "audio frames"},
      {"from": "STT", "to": "Context", "type": "arrow", "label": "transcript"},
      {"from": "Context", "to": "LLM", "type": "arrow", "label": "enriched prompt"},
      {"from": "LLM", "to": "Drift", "type": "arrow", "label": "LLM tokens"},
      {"from": "Drift", "to": "TTS", "type": "arrow", "label": "validated text"},
      {"from": "TTS", "to": "Transport", "type": "arrow", "label": "audio chunks"}
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Think of a voice turn like a relay race with 7 runners: the baton passes from the microphone through seven specialists, each adding their time. The goal is to complete the entire relay in under half a second -- faster than a drummer's hi-hat stroke.",
        "position": "bottom-center"
      },
      {
        "heading": "TARGET",
        "body_text": "<500ms voice-to-voice",
        "position": "below-bar"
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
- [x] Anti-hallucination rules listed (8 default + 4 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L2)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
