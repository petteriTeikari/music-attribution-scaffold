# fig-voice-18: Pipecat Pipeline Anatomy

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-18 |
| **Title** | Pipecat Pipeline Anatomy |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Show the detailed internal architecture of a Pipecat voice agent pipeline, from transport layer through the FrameProcessor chain to service integrations. Answers: "How does Pipecat structure a voice agent pipeline, and what are its key abstractions?"

## Key Message

Pipecat is a Python-first, BSD-licensed framework with 40+ service plugins that structures voice agents as a chain of FrameProcessors connected to a transport layer, with Smart Turn for semantic endpointing and Pipecat Flows for declarative state management.

## Visual Concept

Vertical step flow (Template E) showing the Pipecat pipeline anatomy. Step I: Transport (WebRTC/WebSocket/Daily) receives audio frames. Step II: FrameProcessor Chain -- the core abstraction where processors handle frames in sequence: VAD -> STT -> User Context -> LLM -> TTS. Step III: Services layer showing 40+ plugins (Deepgram, ElevenLabs, Cartesia, OpenAI, Anthropic). Step IV: ParallelPipeline for concurrent context processing. Step V: Smart Turn + Pipecat Flows for turn detection and state management. Side panel showing the plugin architecture grid.

```
+-------------------------------------------------------------------+
|  PIPECAT PIPELINE ANATOMY                                  [sq]   |
|  PYTHON-FIRST VOICE FRAMEWORK                                     |
+-------------------------------------------------------------------+
|                                                                    |
|  I   TRANSPORT LAYER                                               |
|      Daily WebRTC / WebSocket / Raw TCP                            |
|      Receives/sends audio frames                                   |
|      ↓                                                             |
|  II  FRAMEPROCESSOR CHAIN (core abstraction)                       |
|      ┌─────┐  ┌─────┐  ┌──────┐  ┌─────┐  ┌─────┐               |
|      │ VAD │→│ STT │→│Context│→│ LLM │→│ TTS │               |
|      └─────┘  └─────┘  └──────┘  └─────┘  └─────┘               |
|      Each processor: process_frame() → yields frames               |
|      ↓                                                             |
|  III SERVICE PLUGINS (40+)                                         |
|      ┌──────────┬──────────┬──────────┬──────────┐                |
|      │Deepgram  │ElevenLabs│ OpenAI   │Anthropic │                |
|      │Cartesia  │ Azure    │ Google   │ Groq     │                |
|      │Silero    │PlayHT    │ Rime     │ LMNT     │                |
|      └──────────┴──────────┴──────────┴──────────┘                |
|      ↓                                                             |
|  IV  PARALLEL PIPELINE                                             |
|      Context aggregation runs concurrently with main pipeline      |
|      Knowledge base lookup | User history | Tool results           |
|      ↓                                                             |
|  V   SMART TURN + PIPECAT FLOWS                                   |
|      Semantic endpointing (acoustic + LLM)                         |
|      Declarative state machine for conversation flow               |
|                                                                    |
+-------------------------------------------------------------------+
|  "PYTHON-FIRST, 40+ PLUGINS, BSD LICENSE"              [accent line]|
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
    content: "PIPECAT PIPELINE ANATOMY"
    role: title

  - id: main_zone
    bounds: [40, 140, 1840, 800]
    role: content_area

  - id: callout_zone
    bounds: [40, 960, 1840, 80]
    content: "PYTHON-FIRST, 40+ PLUGINS, BSD LICENSE"
    role: callout_box

anchors:
  - id: step_i_transport
    position: [80, 160]
    size: [1760, 120]
    role: processing_stage
    label: "I TRANSPORT LAYER"

  - id: step_ii_frameprocessors
    position: [80, 310]
    size: [1760, 180]
    role: processing_stage
    label: "II FRAMEPROCESSOR CHAIN"

  - id: fp_vad
    position: [120, 360]
    size: [200, 80]
    role: processing_stage
    label: "VAD"

  - id: fp_stt
    position: [360, 360]
    size: [200, 80]
    role: processing_stage
    label: "STT"

  - id: fp_context
    position: [600, 360]
    size: [260, 80]
    role: processing_stage
    label: "Context Aggregation"

  - id: fp_llm
    position: [900, 360]
    size: [200, 80]
    role: processing_stage
    label: "LLM"

  - id: fp_tts
    position: [1140, 360]
    size: [200, 80]
    role: processing_stage
    label: "TTS"

  - id: step_iii_plugins
    position: [80, 520]
    size: [1760, 160]
    role: module_grid
    label: "III SERVICE PLUGINS"

  - id: step_iv_parallel
    position: [80, 710]
    size: [1760, 100]
    role: processing_stage
    label: "IV PARALLEL PIPELINE"

  - id: step_v_smart_turn
    position: [80, 840]
    size: [1760, 100]
    role: processing_stage
    label: "V SMART TURN + FLOWS"

  - id: flow_transport_to_fp
    from: step_i_transport
    to: step_ii_frameprocessors
    type: arrow
    label: "audio frames"

  - id: flow_vad_to_stt
    from: fp_vad
    to: fp_stt
    type: arrow
    label: "speech frames"

  - id: flow_stt_to_context
    from: fp_stt
    to: fp_context
    type: arrow
    label: "transcript frames"

  - id: flow_context_to_llm
    from: fp_context
    to: fp_llm
    type: arrow
    label: "enriched frames"

  - id: flow_llm_to_tts
    from: fp_llm
    to: fp_tts
    type: arrow
    label: "text frames"

  - id: flow_fp_to_plugins
    from: step_ii_frameprocessors
    to: step_iii_plugins
    type: bidirectional
    label: "service calls"

  - id: flow_plugins_to_parallel
    from: step_iii_plugins
    to: step_iv_parallel
    type: arrow
    label: "concurrent context"

  - id: flow_parallel_to_smart
    from: step_iv_parallel
    to: step_v_smart_turn
    type: arrow
    label: "state signals"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Transport Layer (Step I) | `processing_stage` | Daily WebRTC, WebSocket, or raw TCP transport for audio frame I/O |
| FrameProcessor Chain (Step II) | `processing_stage` | Core abstraction: VAD -> STT -> Context -> LLM -> TTS, each a process_frame() yielding frames |
| VAD Processor | `processing_stage` | Voice activity detection frame processor |
| STT Processor | `processing_stage` | Speech-to-text frame processor |
| Context Aggregation | `processing_stage` | User context enrichment processor |
| LLM Processor | `processing_stage` | Language model reasoning processor |
| TTS Processor | `processing_stage` | Text-to-speech synthesis processor |
| Service Plugins (Step III) | `module_grid` | 40+ service integrations: Deepgram, ElevenLabs, Cartesia, OpenAI, Anthropic, etc. |
| Parallel Pipeline (Step IV) | `processing_stage` | Concurrent context aggregation alongside main pipeline |
| Smart Turn + Flows (Step V) | `processing_stage` | Semantic turn detection and declarative conversation state machine |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Transport Layer | FrameProcessor Chain | arrow | "audio frames" |
| VAD | STT | arrow | "speech frames" |
| STT | Context Aggregation | arrow | "transcript frames" |
| Context Aggregation | LLM | arrow | "enriched frames" |
| LLM | TTS | arrow | "text frames" |
| FrameProcessor Chain | Service Plugins | bidirectional | "service calls" |
| Service Plugins | Parallel Pipeline | arrow | "concurrent context" |
| Parallel Pipeline | Smart Turn + Flows | arrow | "state signals" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "PYTHON-FIRST, 40+ PLUGINS, BSD LICENSE" | Pipecat is the only BSD-licensed Python voice agent framework with 40+ service plugins. FrameProcessor is the core abstraction -- everything is a frame being passed through processors. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I TRANSPORT LAYER"
- Label 2: "II FRAMEPROCESSOR CHAIN"
- Label 3: "III SERVICE PLUGINS (40+)"
- Label 4: "IV PARALLEL PIPELINE"
- Label 5: "V SMART TURN + FLOWS"
- Label 6: "VAD"
- Label 7: "STT"
- Label 8: "Context Aggregation"
- Label 9: "LLM"
- Label 10: "TTS"
- Label 11: "Daily WebRTC"
- Label 12: "WebSocket"
- Label 13: "process_frame()"
- Label 14: "Deepgram"
- Label 15: "ElevenLabs"
- Label 16: "Cartesia"
- Label 17: "OpenAI"
- Label 18: "Anthropic"
- Label 19: "Smart Turn"
- Label 20: "Pipecat Flows"

### Caption (for embedding in documentation)

Step-by-step anatomy of a Pipecat voice agent pipeline showing transport, FrameProcessor chain (VAD -> STT -> Context -> LLM -> TTS), 40+ service plugins, parallel pipeline for context, and Smart Turn with Pipecat Flows for state management.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `module_grid`, etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Pipecat is built by Daily.co and licensed under BSD. Do NOT describe it as MIT or Apache licensed.
10. The core abstraction is FrameProcessor with a process_frame() method that yields frames. Do NOT describe it as a middleware chain or pipeline stage.
11. Pipecat has 40+ service plugins as of early 2026. This is a real count from the repository -- do NOT inflate or deflate.
12. Smart Turn is Pipecat's semantic turn detection feature combining acoustic and LLM signals. It is NOT the same as Deepgram Flux.
13. Pipecat Flows is a declarative state machine for managing conversation flow. It was introduced in late 2025.
14. ParallelPipeline allows concurrent processing (e.g., knowledge base lookup alongside main conversation). Do NOT confuse with async I/O.
15. The transport layer uses Daily's WebRTC by default, but also supports WebSocket and raw TCP transports.
16. Roman numerals I-V must be used for step headers.

## Alt Text

Step-by-step architecture diagram of the Pipecat voice agent framework showing five layers: transport (WebRTC/WebSocket), FrameProcessor chain (VAD, STT, Context, LLM, TTS), 40+ service plugins (Deepgram, ElevenLabs, Cartesia), parallel pipeline, and Smart Turn with Pipecat Flows for state management.

## Image Embed

![Step-by-step architecture diagram of the Pipecat voice agent framework showing five layers: transport (WebRTC/WebSocket), FrameProcessor chain (VAD, STT, Context, LLM, TTS), 40+ service plugins (Deepgram, ElevenLabs, Cartesia), parallel pipeline, and Smart Turn with Pipecat Flows for state management.](docs/figures/repo-figures/assets/fig-voice-18-pipecat-pipeline-anatomy.jpg)

*Step-by-step anatomy of a Pipecat voice agent pipeline showing transport, FrameProcessor chain (VAD -> STT -> Context -> LLM -> TTS), 40+ service plugins, parallel pipeline for context, and Smart Turn with Pipecat Flows for state management.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-18",
    "title": "Pipecat Pipeline Anatomy",
    "audience": "L3",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Pipecat structures voice agents as a chain of FrameProcessors with 40+ service plugins, Smart Turn for semantic endpointing, and Pipecat Flows for state management.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Transport Layer",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["I TRANSPORT LAYER", "Daily WebRTC", "WebSocket"]
      },
      {
        "name": "FrameProcessor Chain",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["II FRAMEPROCESSOR CHAIN", "VAD", "STT", "Context", "LLM", "TTS"]
      },
      {
        "name": "Service Plugins",
        "role": "module_grid",
        "is_highlighted": true,
        "labels": ["III SERVICE PLUGINS (40+)", "Deepgram", "ElevenLabs", "Cartesia", "OpenAI", "Anthropic"]
      },
      {
        "name": "Parallel Pipeline",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["IV PARALLEL PIPELINE", "concurrent context"]
      },
      {
        "name": "Smart Turn + Flows",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["V SMART TURN + FLOWS", "semantic endpointing", "declarative state"]
      }
    ],
    "relationships": [
      {
        "from": "Transport Layer",
        "to": "FrameProcessor Chain",
        "type": "arrow",
        "label": "audio frames"
      },
      {
        "from": "VAD",
        "to": "STT",
        "type": "arrow",
        "label": "speech frames"
      },
      {
        "from": "STT",
        "to": "Context Aggregation",
        "type": "arrow",
        "label": "transcript frames"
      },
      {
        "from": "Context Aggregation",
        "to": "LLM",
        "type": "arrow",
        "label": "enriched frames"
      },
      {
        "from": "LLM",
        "to": "TTS",
        "type": "arrow",
        "label": "text frames"
      },
      {
        "from": "FrameProcessor Chain",
        "to": "Service Plugins",
        "type": "bidirectional",
        "label": "service calls"
      }
    ],
    "callout_boxes": [
      {
        "heading": "PYTHON-FIRST, 40+ PLUGINS, BSD LICENSE",
        "body_text": "Pipecat is the only BSD-licensed Python voice agent framework with 40+ service plugins. FrameProcessor is the core abstraction.",
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
- [ ] Layout template identified (E)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
