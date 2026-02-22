# fig-voice-31: Recommended Voice Agent MVP Stack

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-31 |
| **Title** | Recommended Voice Agent MVP Stack |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Define the specific production stack recommended for adding voice capabilities to the music attribution scaffold. Each layer (framework, STT, LLM, TTS, transport, turn detection) names the recommended provider and fallback, with reasoning tied to the existing architecture. Answers: "What exact technology should we use for each layer of the voice stack, and why?"

## Key Message

The recommended MVP stack builds on the existing PydanticAI agent by wrapping it with Pipecat for voice I/O: Pipecat framework, Deepgram Nova-3 for STT, the existing PydanticAI agent (Haiku 4.5 with Sonnet escalation) for LLM, Cartesia Sonic for TTS with Orpheus self-hosted fallback, Daily.co WebRTC for transport, and Pipecat Smart Turn for turn detection. Estimated operating cost: ~$0.05-0.08/min for standard tier.

## Visual Concept

Six vertical steps (Template E) representing the stack layers from bottom (framework) to top (turn detection). Each step shows the recommended choice with a solid accent marker and the fallback option with a dashed marker. A vertical "spine" connects all layers. The right side of each step shows the key rationale. A cost estimate appears at the bottom.

```
+-------------------------------------------------------------------+
|  RECOMMENDED VOICE AGENT MVP STACK                           [sq]   |
|  -- Production Stack for Music Attribution                         |
+-------------------------------------------------------------------+
|                                                                    |
|  VI. TURN DETECTION                                                |
|  ─────────────────                                                 |
|  ■ Pipecat Smart Turn (open-source)                                |
|    Handles interrupts + end-of-turn detection                      |
|    Fallback: Deepgram utterance_end events                         |
|                                                           [line]   |
|                                                                    |
|  V. TRANSPORT                                                      |
|  ────────────                                                      |
|  ■ WebRTC via Daily.co (Pipecat native)                            |
|    Sub-200ms round-trip latency                                    |
|    Fallback: WebSocket (higher latency)                            |
|                                                           [line]   |
|                                                                    |
|  IV. TTS                                                           |
|  ────────                                                          |
|  ■ Cartesia Sonic (lowest latency, 40ms TTFA)                     |
|    Fallback: Orpheus TTS (self-hosted, Apache 2.0)                |
|    Cost: ~$0.02-0.04/min (Cartesia) / ~$0.001/min (Orpheus)       |
|                                                           [line]   |
|                                                                    |
|  III. LLM                                                          |
|  ────────                                                          |
|  ■ Existing PydanticAI agent (Haiku 4.5 default)                  |
|    Sonnet escalation for complex queries                           |
|    ZERO new LLM integration required                               |
|                                                           [line]   |
|                                                                    |
|  II. STT                                                           |
|  ────────                                                          |
|  ■ Deepgram Nova-3 / Flux (best accuracy + CSR)                   |
|    Real-time streaming transcription                               |
|    Fallback: Self-hosted Whisper (cost savings)                    |
|                                                           [line]   |
|                                                                    |
|  I. FRAMEWORK                                                      |
|  ────────────                                                      |
|  ■ Pipecat (Python-native, matches PydanticAI)                    |
|    40+ service plugins, BSD license, Daily.co                      |
|    Wraps existing agent -- adds voice I/O layer                    |
|                                                                    |
|  ─────────────────────────────────────────────── [accent line]     |
|                                                                    |
|  ESTIMATED COST: ~$0.05-0.08/min (standard tier)                   |
|                                                                    |
+-------------------------------------------------------------------+
|  BUILDS ON EXISTING MVP -- Pipecat wraps the PydanticAI agent,     |
|  adding voice I/O                                                  |
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
    content: "RECOMMENDED VOICE AGENT MVP STACK"
    role: title

  - id: stack_zone
    bounds: [60, 140, 1800, 700]
    role: content_area

  - id: cost_zone
    bounds: [60, 860, 1800, 40]
    role: content_area

  - id: callout_zone
    bounds: [60, 940, 1800, 100]
    content: "BUILDS ON EXISTING MVP"
    role: callout_box

anchors:
  - id: spine
    position: [120, 500]
    size: [4, 680]
    role: accent_line_v
    label: "stack spine"

  - id: step_vi
    position: [960, 180]
    size: [1600, 100]
    role: processing_stage
    label: "VI. TURN DETECTION"

  - id: step_v
    position: [960, 300]
    size: [1600, 100]
    role: processing_stage
    label: "V. TRANSPORT"

  - id: step_iv
    position: [960, 420]
    size: [1600, 100]
    role: processing_stage
    label: "IV. TTS"

  - id: step_iii
    position: [960, 540]
    size: [1600, 100]
    role: selected_option
    label: "III. LLM"

  - id: step_ii
    position: [960, 660]
    size: [1600, 100]
    role: processing_stage
    label: "II. STT"

  - id: step_i
    position: [960, 780]
    size: [1600, 100]
    role: selected_option
    label: "I. FRAMEWORK"

  - id: pipecat_badge
    position: [300, 780]
    size: [160, 40]
    role: selected_option
    label: "PIPECAT"

  - id: deepgram_badge
    position: [300, 660]
    size: [160, 40]
    role: selected_option
    label: "DEEPGRAM NOVA-3"

  - id: pydanticai_badge
    position: [300, 540]
    size: [160, 40]
    role: selected_option
    label: "PYDANTICAI"

  - id: cartesia_badge
    position: [300, 420]
    size: [160, 40]
    role: selected_option
    label: "CARTESIA SONIC"

  - id: daily_badge
    position: [300, 300]
    size: [160, 40]
    role: selected_option
    label: "DAILY.CO WEBRTC"

  - id: smart_turn_badge
    position: [300, 180]
    size: [160, 40]
    role: selected_option
    label: "SMART TURN"

  - id: orpheus_fallback
    position: [600, 420]
    size: [160, 40]
    role: deferred_option
    label: "Orpheus (fallback)"

  - id: whisper_fallback
    position: [600, 660]
    size: [160, 40]
    role: deferred_option
    label: "Whisper (fallback)"

  - id: cost_estimate
    position: [960, 880]
    size: [400, 40]
    role: data_mono
    label: "~$0.05-0.08/min"

  - id: divider_vi_v
    position: [140, 240]
    size: [1640, 2]
    role: accent_line

  - id: divider_v_iv
    position: [140, 360]
    size: [1640, 2]
    role: accent_line

  - id: divider_iv_iii
    position: [140, 480]
    size: [1640, 2]
    role: accent_line

  - id: divider_iii_ii
    position: [140, 600]
    size: [1640, 2]
    role: accent_line

  - id: divider_ii_i
    position: [140, 720]
    size: [1640, 2]
    role: accent_line
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "RECOMMENDED VOICE AGENT MVP STACK" with coral accent square |
| Stack spine | `accent_line_v` | Vertical coral line connecting all six layers |
| Step I: Framework | `selected_option` | Pipecat -- Python-native, 40+ plugins, BSD, wraps existing agent |
| Step II: STT | `processing_stage` | Deepgram Nova-3 / Flux -- best accuracy + conversational speech recognition |
| Step III: LLM | `selected_option` | Existing PydanticAI agent -- Haiku 4.5 default, Sonnet escalation, ZERO new integration |
| Step IV: TTS | `processing_stage` | Cartesia Sonic -- 40ms TTFA, lowest latency. Orpheus fallback for self-hosted. |
| Step V: Transport | `processing_stage` | WebRTC via Daily.co -- Pipecat native integration, sub-200ms RTT |
| Step VI: Turn Detection | `processing_stage` | Pipecat Smart Turn -- open-source, handles interrupts + end-of-turn |
| Fallback badges | `deferred_option` | Orpheus (TTS fallback), Whisper (STT fallback) shown as dashed alternatives |
| Cost estimate | `data_mono` | "~$0.05-0.08/min (standard tier)" |
| Step dividers | `accent_line` | Coral accent lines between each layer |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Step I (Framework) | Step II (STT) | arrow | "Pipecat orchestrates" |
| Step II (STT) | Step III (LLM) | arrow | "transcription to agent" |
| Step III (LLM) | Step IV (TTS) | arrow | "text response to speech" |
| Step IV (TTS) | Step V (Transport) | arrow | "audio to client" |
| Step V (Transport) | Step VI (Turn Detection) | arrow | "manages conversation flow" |
| Cartesia Sonic | Orpheus TTS | dashed | "fallback" |
| Deepgram Nova-3 | Self-hosted Whisper | dashed | "fallback" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "BUILDS ON EXISTING MVP" | Pipecat wraps the PydanticAI agent, adding voice I/O. The LLM layer requires ZERO new integration -- it uses the same agent, tools, and model failover already built. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I. FRAMEWORK"
- Label 2: "II. STT"
- Label 3: "III. LLM"
- Label 4: "IV. TTS"
- Label 5: "V. TRANSPORT"
- Label 6: "VI. TURN DETECTION"
- Label 7: "Pipecat (BSD, Python)"
- Label 8: "Deepgram Nova-3 / Flux"
- Label 9: "PydanticAI agent (existing)"
- Label 10: "Cartesia Sonic (40ms TTFA)"
- Label 11: "Daily.co WebRTC"
- Label 12: "Pipecat Smart Turn"
- Label 13: "Orpheus (self-hosted)"
- Label 14: "Whisper (self-hosted)"
- Label 15: "~$0.05-0.08/min"
- Label 16: "ZERO new LLM integration"

### Caption (for embedding in documentation)

Recommended six-layer voice agent MVP stack for music attribution: Pipecat framework, Deepgram Nova-3 STT, existing PydanticAI agent for LLM, Cartesia Sonic TTS with Orpheus fallback, Daily.co WebRTC transport, and Pipecat Smart Turn detection -- estimated $0.05-0.08/min operating cost.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `selected_option`, `processing_stage`, `deferred_option` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon is ALLOWED** -- this is an L3 figure targeting software engineers. Pipecat, PydanticAI, Deepgram, Cartesia, WebRTC are appropriate.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Pipecat is by Daily.co, BSD licensed, Python-native with 40+ service plugins. These are verified facts from the Pipecat repository.
10. Deepgram Nova-3 is Deepgram's latest production STT model. "Flux" is their newer model with conversational speech recognition (CSR) capabilities.
11. The existing PydanticAI agent uses `anthropic:claude-haiku-4-5` as default with Sonnet escalation via FallbackModel. This is documented in `src/music_attribution/chat/agent.py`.
12. Cartesia Sonic achieves 40ms time-to-first-audio (TTFA) using a state-space model (SSM) architecture. This is from Cartesia's published benchmarks.
13. Orpheus TTS is Apache 2.0 licensed, 3B parameters, uses a Llama backbone, and supports emotion tags. Self-hosted cost is ~$0.001/min.
14. Daily.co provides the WebRTC transport layer that Pipecat natively integrates with. This is not a third-party integration -- Daily.co built Pipecat.
15. Pipecat Smart Turn is an open-source turn detection module that replaced the older VAD-based approach. It handles both interruption and end-of-turn.
16. The $0.05-0.08/min estimate is for the mid-tier stack (Deepgram + Haiku + Cartesia). Budget and premium tiers have different costs.
17. "ZERO new LLM integration" is the key selling point -- the existing PydanticAI agent with its 4 tools works as-is, Pipecat just wraps it.

## Alt Text

Six-layer recommended voice agent MVP stack for music attribution showing deployment architecture from Pipecat framework through Deepgram Nova-3 STT, PydanticAI LLM agent, Cartesia Sonic TTS, Daily.co WebRTC transport, to Smart Turn detection with fallback options and estimated $0.05-0.08 per minute operating cost.

## Image Embed

![Six-layer recommended voice agent MVP stack for music attribution showing deployment architecture from Pipecat framework through Deepgram Nova-3 STT, PydanticAI LLM agent, Cartesia Sonic TTS, Daily.co WebRTC transport, to Smart Turn detection with fallback options and estimated $0.05-0.08 per minute operating cost.](docs/figures/repo-figures/assets/fig-voice-31-recommended-mvp-stack.jpg)

*Recommended six-layer voice agent MVP stack for music attribution: Pipecat framework, Deepgram Nova-3 STT, existing PydanticAI agent for LLM, Cartesia Sonic TTS with Orpheus fallback, Daily.co WebRTC transport, and Pipecat Smart Turn detection -- estimated $0.05-0.08/min operating cost.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-31",
    "title": "Recommended Voice Agent MVP Stack",
    "audience": "L3",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "The recommended MVP stack wraps the existing PydanticAI agent with Pipecat for voice I/O: Deepgram STT, Cartesia TTS, Daily.co transport, Smart Turn detection, at ~$0.05-0.08/min.",
    "layout_flow": "bottom-to-top",
    "key_structures": [
      {
        "name": "Framework: Pipecat",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["I. FRAMEWORK", "Pipecat (BSD, Python)", "40+ plugins"]
      },
      {
        "name": "STT: Deepgram Nova-3",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["II. STT", "Deepgram Nova-3 / Flux"]
      },
      {
        "name": "LLM: PydanticAI Agent",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["III. LLM", "Existing PydanticAI agent", "ZERO new integration"]
      },
      {
        "name": "TTS: Cartesia Sonic",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["IV. TTS", "Cartesia Sonic", "40ms TTFA"]
      },
      {
        "name": "Transport: Daily.co WebRTC",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["V. TRANSPORT", "Daily.co WebRTC"]
      },
      {
        "name": "Turn Detection: Smart Turn",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["VI. TURN DETECTION", "Pipecat Smart Turn"]
      },
      {
        "name": "Orpheus Fallback",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["Orpheus TTS (self-hosted)"]
      },
      {
        "name": "Whisper Fallback",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["Whisper (self-hosted)"]
      }
    ],
    "relationships": [
      {
        "from": "Framework",
        "to": "Turn Detection",
        "type": "arrow",
        "label": "stack layers"
      },
      {
        "from": "Cartesia Sonic",
        "to": "Orpheus TTS",
        "type": "dashed",
        "label": "fallback"
      },
      {
        "from": "Deepgram Nova-3",
        "to": "Whisper",
        "type": "dashed",
        "label": "fallback"
      }
    ],
    "callout_boxes": [
      {
        "heading": "BUILDS ON EXISTING MVP",
        "body_text": "Pipecat wraps the PydanticAI agent, adding voice I/O. The LLM layer requires ZERO new integration.",
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
- [x] Anti-hallucination rules listed (8 default + 9 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L3)
- [x] Layout template identified (E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
