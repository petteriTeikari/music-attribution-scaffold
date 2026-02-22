# fig-voice-48: Extension Points & Plugin Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-48 |
| **Title** | Extension Points & Plugin Architecture |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md, new subsection |
| **Priority** | P2 (Nice-to-have) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Show 6 extension points where teams can plug in custom implementations. Each shows the protocol/interface to implement. Answers: "Where can I swap in my own component, and what interface do I need to satisfy?"

## Key Message

The voice module has 6 extension points where any team can plug in a custom implementation: custom STT, custom TTS, custom drift detector, custom guardrails, custom memory backend, and custom tools. Each point is defined by a Protocol (structural typing) -- implement the methods and it just works.

## Visual Concept

Multi-panel (Template B). Six small panels in a 3x2 grid. Each panel shows: extension point name, the Protocol to satisfy, method signatures, and an example use case. A central "VOICE MODULE CORE" hexagon connects to all 6 panels via dotted extension lines. Coral accent squares mark each extension point slot.

```
+-----------------------------------------------------------------------+
|  EXTENSION POINTS & PLUGIN ARCHITECTURE                          [sq]  |
|  -- 6 Slots, Protocol-Based Structural Typing                         |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌────────────────┐    ┌────────────────┐    ┌────────────────┐       |
|  │ CUSTOM STT      │    │ CUSTOM TTS      │    │ CUSTOM DRIFT    │       |
|  │ STTServiceProto  │    │ TTSServiceProto  │    │ DriftDetProto   │       |
|  │ .transcribe()    │    │ .synthesize()    │    │ .score()        │       |
|  │ .close()         │    │ .close()         │    │ .state          │       |
|  │ ─ ─ ─ ─ ─ ─ ─   │    │ ─ ─ ─ ─ ─ ─ ─   │    │ ─ ─ ─ ─ ─ ─    │       |
|  │ ex: fine-tuned   │    │ ex: Orpheus-TTS  │    │ ex: LLM-as-    │       |
|  │ Whisper for      │    │ for emotional    │    │ judge drift     │       |
|  │ music vocab      │    │ voice            │    │ detection       │       |
|  └───────┬──────────┘    └───────┬──────────┘    └───────┬──────────┘       |
|          │                       │                       │              |
|          └───────────────────────┼───────────────────────┘              |
|                                  │                                     |
|                        ┌─────────┴─────────┐                           |
|                        │  VOICE MODULE      │                           |
|                        │  CORE              │                           |
|                        └─────────┬─────────┘                           |
|                                  │                                     |
|          ┌───────────────────────┼───────────────────────┐              |
|          │                       │                       │              |
|  ┌───────┴──────────┐    ┌───────┴──────────┐    ┌───────┴──────────┐       |
|  │ CUSTOM GUARDRAILS │    │ CUSTOM MEMORY     │    │ CUSTOM TOOLS     │       |
|  │ guardrails_       │    │ memory backend    │    │ register_        │       |
|  │ integration.py    │    │ replacement       │    │ function()       │       |
|  │ ─ ─ ─ ─ ─ ─ ─    │    │ ─ ─ ─ ─ ─ ─ ─    │    │ ─ ─ ─ ─ ─ ─     │       |
|  │ ex: Colang rules  │    │ ex: Redis-backed  │    │ ex: Spotify API  │       |
|  │ for music IP      │    │ session memory    │    │ search, ISRC     │       |
|  └────────────────┘    └────────────────┘    └────────────────┘       |
|                                                                        |
+-----------------------------------------------------------------------+
|  ELI5: Like a modular synthesizer rack -- the core frame          [sq]  |
|  accepts standard-format modules in 6 slots. Match the                 |
|  connector pattern (Protocol) and the rack doesn't care who made it.   |
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
    content: "EXTENSION POINTS & PLUGIN ARCHITECTURE"
    role: title

  - id: top_row
    bounds: [40, 140, 1840, 280]
    role: content_area

  - id: core_zone
    bounds: [760, 440, 400, 120]
    role: content_area

  - id: bottom_row
    bounds: [40, 580, 1840, 280]
    role: content_area

  - id: callout_zone
    bounds: [40, 940, 1840, 100]
    content: "ELI5: Like a modular synthesizer rack"
    role: callout_box

anchors:
  - id: panel_stt
    position: [200, 280]
    size: [480, 240]
    role: processing_stage
    label: "CUSTOM STT"

  - id: panel_tts
    position: [760, 280]
    size: [480, 240]
    role: processing_stage
    label: "CUSTOM TTS"

  - id: panel_drift
    position: [1320, 280]
    size: [480, 240]
    role: processing_stage
    label: "CUSTOM DRIFT"

  - id: core_hex
    position: [960, 500]
    size: [300, 100]
    role: decision_point
    label: "VOICE MODULE CORE"

  - id: panel_guardrails
    position: [200, 700]
    size: [480, 240]
    role: processing_stage
    label: "CUSTOM GUARDRAILS"

  - id: panel_memory
    position: [760, 700]
    size: [480, 240]
    role: processing_stage
    label: "CUSTOM MEMORY"

  - id: panel_tools
    position: [1320, 700]
    size: [480, 240]
    role: processing_stage
    label: "CUSTOM TOOLS"

  - id: stt_to_core
    from: panel_stt
    to: core_hex
    type: dotted_line
    label: "STTServiceProtocol"

  - id: tts_to_core
    from: panel_tts
    to: core_hex
    type: dotted_line
    label: "TTSServiceProtocol"

  - id: drift_to_core
    from: panel_drift
    to: core_hex
    type: dotted_line
    label: "DriftDetectorProtocol"

  - id: guardrails_to_core
    from: panel_guardrails
    to: core_hex
    type: dotted_line
    label: "file replacement"

  - id: memory_to_core
    from: panel_memory
    to: core_hex
    type: dotted_line
    label: "backend swap"

  - id: tools_to_core
    from: panel_tools
    to: core_hex
    type: dotted_line
    label: "register_function()"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "EXTENSION POINTS & PLUGIN ARCHITECTURE" with coral accent square |
| Custom STT panel | `processing_stage` | STTServiceProtocol: transcribe(), close(). Example: fine-tuned Whisper for music vocabulary |
| Custom TTS panel | `processing_stage` | TTSServiceProtocol: synthesize(), close(). Example: Orpheus-TTS for emotional voice |
| Custom Drift panel | `processing_stage` | DriftDetectorProtocol: score(), state. Example: LLM-as-judge drift detection |
| Voice Module Core | `decision_point` | Central hexagon representing the pipeline core that accepts all plugins |
| Custom Guardrails panel | `processing_stage` | Replace guardrails_integration.py. Example: domain-specific Colang rules for music IP |
| Custom Memory panel | `processing_stage` | Replace letta/mem0 integration. Example: Redis-backed session memory |
| Custom Tools panel | `processing_stage` | Add tools via register_function(). Example: Spotify API search, live ISRC lookup |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Custom STT | Core | dotted_line | "STTServiceProtocol" |
| Custom TTS | Core | dotted_line | "TTSServiceProtocol" |
| Custom Drift | Core | dotted_line | "DriftDetectorProtocol" |
| Custom Guardrails | Core | dotted_line | "file replacement" |
| Custom Memory | Core | dotted_line | "backend swap" |
| Custom Tools | Core | dotted_line | "register_function()" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Think of the voice module like a modular synthesizer rack: the core frame (voice module) accepts standard-format modules in 6 slots. Any manufacturer can build a module that fits the slot -- all they need is to match the connector pattern (Protocol). Swap a filter module, add a new oscillator, replace the sequencer -- the rack doesn't care who made it. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "CUSTOM STT"
- Label 2: "CUSTOM TTS"
- Label 3: "CUSTOM DRIFT"
- Label 4: "CUSTOM GUARDRAILS"
- Label 5: "CUSTOM MEMORY"
- Label 6: "CUSTOM TOOLS"
- Label 7: "VOICE MODULE CORE"
- Label 8: "STTServiceProtocol"
- Label 9: "TTSServiceProtocol"
- Label 10: "DriftDetectorProtocol"
- Label 11: "transcribe(), close()"
- Label 12: "synthesize(), close()"
- Label 13: "score(), state"
- Label 14: "register_function()"
- Label 15: "Fine-tuned Whisper"
- Label 16: "Orpheus-TTS emotional"
- Label 17: "LLM-as-judge drift"
- Label 18: "Colang rules for music IP"
- Label 19: "Redis session memory"
- Label 20: "Spotify API, ISRC lookup"

### Caption (for embedding in documentation)

Six extension points in the voice module plugin architecture -- custom STT, TTS, drift detector, guardrails, memory backend, and tools -- each defined by a Protocol interface that any team can implement for domain-specific needs.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `decision_point`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon is ALLOWED** -- "Protocol", "structural typing", "register_function" are appropriate for L3 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text in the figure.

### Figure-Specific Rules

9. Protocol method signatures must match actual protocols.py: STTServiceProtocol (transcribe, close), TTSServiceProtocol (synthesize, close), DriftDetectorProtocol (score, state).
10. Extension points must be achievable with the current architecture (no hypothetical features).
11. Example use cases must be plausible and music-domain relevant.
12. Do NOT show version numbers or specific library versions in any panel.

## Alt Text

Six-slot plugin architecture: STT, TTS, drift, guardrails, memory, and tools extension points around a voice module core via Protocols.

## Image Embed

![Six-slot plugin architecture: STT, TTS, drift, guardrails, memory, and tools extension points around a voice module core via Protocols.](docs/figures/repo-figures/assets/fig-voice-48-extension-points-plugins.jpg)

*Six extension points in the voice module plugin architecture -- custom STT, TTS, drift detector, guardrails, memory backend, and tools -- each defined by a Protocol interface that any team can implement for domain-specific needs.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-48",
    "title": "Extension Points & Plugin Architecture",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "The voice module has 6 extension points defined by Protocol interfaces: custom STT, TTS, drift detector, guardrails, memory, and tools.",
    "layout_flow": "hub-and-spoke",
    "key_structures": [
      {
        "name": "Custom STT",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["CUSTOM STT", "STTServiceProtocol", "transcribe(), close()"]
      },
      {
        "name": "Custom TTS",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["CUSTOM TTS", "TTSServiceProtocol", "synthesize(), close()"]
      },
      {
        "name": "Custom Drift",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["CUSTOM DRIFT", "DriftDetectorProtocol", "score(), state"]
      },
      {
        "name": "Voice Module Core",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["VOICE MODULE CORE"]
      },
      {
        "name": "Custom Guardrails",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["CUSTOM GUARDRAILS", "guardrails_integration.py"]
      },
      {
        "name": "Custom Memory",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["CUSTOM MEMORY", "letta/mem0 replacement"]
      },
      {
        "name": "Custom Tools",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["CUSTOM TOOLS", "register_function()"]
      }
    ],
    "relationships": [
      {"from": "Custom STT", "to": "Core", "type": "dotted_line", "label": "STTServiceProtocol"},
      {"from": "Custom TTS", "to": "Core", "type": "dotted_line", "label": "TTSServiceProtocol"},
      {"from": "Custom Drift", "to": "Core", "type": "dotted_line", "label": "DriftDetectorProtocol"},
      {"from": "Custom Guardrails", "to": "Core", "type": "dotted_line", "label": "file replacement"},
      {"from": "Custom Memory", "to": "Core", "type": "dotted_line", "label": "backend swap"},
      {"from": "Custom Tools", "to": "Core", "type": "dotted_line", "label": "register_function()"}
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Think of the voice module like a modular synthesizer rack: the core frame accepts standard-format modules in 6 slots. Any manufacturer can build a module that fits the slot -- all they need is to match the connector pattern (Protocol). Swap a filter module, add a new oscillator, replace the sequencer -- the rack doesn't care who made it.",
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
- [x] Anti-hallucination rules listed (8 default + 4 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L3)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
