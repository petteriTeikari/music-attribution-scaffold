# fig-voice-01: Voice Agent Full Stack Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-01 |
| **Title** | Voice Agent Full Stack Architecture |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Show the complete voice agent stack from microphone to speaker, with all component layers and their interactions. Answers: "What are the five stages of a production voice pipeline and how do they connect?"

## Key Message

A production voice agent is a five-layer pipeline -- Transport -> STT -> LLM -> TTS -> Transport -- with VAD and turn detection as the critical orchestration layer.

## Visual Concept

Five-panel layout (Template B) flowing left to right. Panel I: Transport (WebRTC/WebSocket). Panel II: STT (VAD -> Transcription -> Punctuation). Panel III: LLM (Intent -> Tool Calling -> Response). Panel IV: TTS (Voice Selection -> Synthesis -> Prosody). Panel V: Output Transport. A thin teal feedback arc along the bottom edge. Coral accent squares mark panel transitions. Roman numerals I-V above panels.

```
+-------------------------------------------------------------------+
|  VOICE AGENT STACK                                       [coral sq] |
|  FULL ARCHITECTURE                                                  |
+--------+-----------+-----------+-----------+----------------------+
|        |           |           |           |                      |
|  I     |    II     |   III     |    IV     |     V                |
| TRANS- |   STT     |   LLM    |   TTS     |   TRANS-             |
| PORT   |           |          |           |   PORT               |
|        |           |          |           |                      |
| WebRTC |  VAD      | Intent   | Voice     | Audio                |
| WebSkt |  Transcr. | Tools    | Synth     | Stream               |
|        |  Punct.   | Response | Prosody   |                      |
+--------+-----------+-----------+-----------+----------------------+
|  <------------- TURN DETECTION ----------------->                 |
|  SEMANTIC ENDPOINTING: THE ORCHESTRATION LAYER    [accent line]   |
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
    content: "VOICE AGENT STACK"
    role: title

  - id: panel_strip
    bounds: [40, 140, 1840, 700]
    role: content_area

  - id: orchestration_zone
    bounds: [40, 860, 1840, 80]
    content: "SEMANTIC ENDPOINTING: THE ORCHESTRATION LAYER"
    role: callout_box

  - id: feedback_zone
    bounds: [40, 960, 1840, 80]
    role: feedback_arc

anchors:
  - id: panel_i_transport_in
    position: [80, 200]
    size: [300, 600]
    role: processing_stage
    label: "I TRANSPORT"

  - id: panel_ii_stt
    position: [420, 200]
    size: [340, 600]
    role: processing_stage
    label: "II STT"

  - id: panel_iii_llm
    position: [800, 200]
    size: [340, 600]
    role: processing_stage
    label: "III LLM"

  - id: panel_iv_tts
    position: [1180, 200]
    size: [340, 600]
    role: processing_stage
    label: "IV TTS"

  - id: panel_v_transport_out
    position: [1560, 200]
    size: [300, 600]
    role: processing_stage
    label: "V TRANSPORT"

  - id: turn_detection_bar
    position: [80, 870]
    size: [1780, 60]
    role: security_layer
    label: "Turn Detection"

  - id: feedback_arc
    position: [80, 970]
    size: [1780, 40]
    role: feedback_loop
    label: "Response quality feedback"

  - id: flow_i_to_ii
    from: panel_i_transport_in
    to: panel_ii_stt
    type: arrow
    label: "audio stream"

  - id: flow_ii_to_iii
    from: panel_ii_stt
    to: panel_iii_llm
    type: arrow
    label: "transcript"

  - id: flow_iii_to_iv
    from: panel_iii_llm
    to: panel_iv_tts
    type: arrow
    label: "response text"

  - id: flow_iv_to_v
    from: panel_iv_tts
    to: panel_v_transport_out
    type: arrow
    label: "synthesized audio"

  - id: turn_detection_to_all
    from: turn_detection_bar
    to: panel_strip
    type: bidirectional
    label: "orchestration signals"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Transport In (Panel I) | `processing_stage` | WebRTC/WebSocket audio input from client microphone |
| STT Pipeline (Panel II) | `processing_stage` | VAD -> streaming transcription -> punctuation restoration |
| LLM Processing (Panel III) | `processing_stage` | Intent routing, tool calling, response generation |
| TTS Pipeline (Panel IV) | `processing_stage` | Voice selection, synthesis, prosody control |
| Transport Out (Panel V) | `processing_stage` | Audio output streaming to client speaker |
| Turn Detection | `security_layer` | Semantic endpointing orchestration spanning all stages |
| Feedback Loop | `feedback_loop` | Response quality -> prompt refinement arc |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Transport In | STT Pipeline | arrow | "audio stream" |
| STT Pipeline | LLM Processing | arrow | "transcript" |
| LLM Processing | TTS Pipeline | arrow | "response text" |
| TTS Pipeline | Transport Out | arrow | "synthesized audio" |
| Turn Detection | All Panels | bidirectional | "orchestration signals" |
| Transport Out | Transport In | dashed | "feedback loop" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "SEMANTIC ENDPOINTING" | Turn detection moved from simple silence thresholds to acoustic+semantic models in 2025, reducing false interruptions by 30%. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I TRANSPORT"
- Label 2: "II STT"
- Label 3: "III LLM"
- Label 4: "IV TTS"
- Label 5: "V TRANSPORT"
- Label 6: "WebRTC / WebSocket"
- Label 7: "VAD"
- Label 8: "Streaming Transcription"
- Label 9: "Punctuation"
- Label 10: "Intent Routing"
- Label 11: "Tool Calling"
- Label 12: "Response Generation"
- Label 13: "Voice Selection"
- Label 14: "Synthesis"
- Label 15: "Prosody Control"
- Label 16: "Audio Output Stream"
- Label 17: "SEMANTIC ENDPOINTING"

### Caption (for embedding in documentation)

Five-panel architecture diagram showing the complete voice agent pipeline from transport input through STT, LLM, TTS, and back to transport output, with semantic endpointing as the critical orchestration layer.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `security_layer`, `feedback_loop` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. No provider names (Deepgram, ElevenLabs, Cartesia, etc.) in the visual panels -- those are L3 detail in labels only, not in the main diagram structure.
10. Roman numerals I-V must be used for panel headers, not Arabic numerals.
11. The turn detection bar must visually span all five panels to show it orchestrates the entire pipeline.
12. The feedback arc must be visually distinct (thinner, different semantic tag) from the main left-to-right flow.

## Alt Text

Architecture diagram of a five-stage real-time voice agent pipeline showing Transport, STT, LLM, TTS, and output stages with semantic endpointing as the orchestration layer for music attribution voice interactions.

## Image Embed

![Architecture diagram of a five-stage real-time voice agent pipeline showing Transport, STT, LLM, TTS, and output stages with semantic endpointing as the orchestration layer for music attribution voice interactions.](docs/figures/repo-figures/assets/fig-voice-01-full-stack-architecture.jpg)

*Five-panel architecture diagram showing the complete voice agent pipeline from transport input through STT, LLM, TTS, and back to transport output, with semantic endpointing as the critical orchestration layer.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-01",
    "title": "Voice Agent Full Stack Architecture",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "A production voice agent is a five-layer pipeline with VAD and turn detection as the critical orchestration layer.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Transport In",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["I TRANSPORT", "WebRTC / WebSocket"]
      },
      {
        "name": "STT Pipeline",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["II STT", "VAD", "Transcription", "Punctuation"]
      },
      {
        "name": "LLM Processing",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["III LLM", "Intent", "Tools", "Response"]
      },
      {
        "name": "TTS Pipeline",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["IV TTS", "Voice", "Synthesis", "Prosody"]
      },
      {
        "name": "Transport Out",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["V TRANSPORT", "Audio Stream"]
      },
      {
        "name": "Turn Detection",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["SEMANTIC ENDPOINTING"]
      }
    ],
    "relationships": [
      {
        "from": "Transport In",
        "to": "STT Pipeline",
        "type": "arrow",
        "label": "audio stream"
      },
      {
        "from": "STT Pipeline",
        "to": "LLM Processing",
        "type": "arrow",
        "label": "transcript"
      },
      {
        "from": "LLM Processing",
        "to": "TTS Pipeline",
        "type": "arrow",
        "label": "response text"
      },
      {
        "from": "TTS Pipeline",
        "to": "Transport Out",
        "type": "arrow",
        "label": "synthesized audio"
      },
      {
        "from": "Turn Detection",
        "to": "All Panels",
        "type": "bidirectional",
        "label": "orchestration signals"
      }
    ],
    "callout_boxes": [
      {
        "heading": "SEMANTIC ENDPOINTING",
        "body_text": "Turn detection moved from simple silence thresholds to acoustic+semantic models in 2025, reducing false interruptions by 30%.",
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
