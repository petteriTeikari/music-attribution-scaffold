# fig-voice-34: VoiceConfig Anatomy

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-34 |
| **Title** | VoiceConfig Anatomy |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md, Section 1.4 |
| **Priority** | P1 (Important) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Map VoiceConfig's 21 fields to their 6 enum types and then to the Pipecat services they configure. Environment variable tables cannot show the cascade from env var to enum to service. Answers: "How does a single environment variable end up configuring a concrete Pipecat service?"

## Key Message

VoiceConfig is a single Pydantic Settings model that maps 21 environment variables through 6 typed enums to concrete Pipecat service instances -- one config object controls the entire pipeline.

## Visual Concept

Split-panel (Template D). Left panel: VoiceConfig fields grouped by category (Provider Selection: 3 fields, STT Settings: 1, Server: 2, VAD Tuning: 3, Persona: 4, Drift: 4, Guardrails: 1, API Keys: 5). Right panel: 6 enum types (STTProvider, TTSProvider, TransportType, WhisperModel, DriftState, VoiceConfig itself) connecting to Pipecat services. Center: arrows showing the cascade from field to enum to service. Coral accent line divides the two panels.

```
+-------------------------------------------------------------------+
|  VOICECONFIG ANATOMY                                     [coral sq] |
|  ENV VAR -> ENUM -> SERVICE CASCADE                                 |
+-------------------------------+-----------------------------------+
|  LEFT PANEL: 21 FIELDS        |  RIGHT PANEL: 6 ENUMS + SERVICES  |
|                               |                                   |
|  PROVIDER SELECTION           |  STTProvider                      |
|    stt_provider         ------|-->  whisper / deepgram / assemblyai|
|    tts_provider         ------|-->  TTSProvider                    |
|    transport            ------|-->  piper / kokoro / elevenlabs    |
|                               |                                   |
|  STT SETTINGS                 |  TransportType                    |
|    whisper_model        ------|-->  websocket / smallwebrtc / daily|
|                               |                                   |
|  SERVER                       |  WhisperModel                     |
|    host, port                 |    tiny / base / small / med / lg |
|                               |                                   |
|  VAD TUNING                   |  DriftState                       |
|    vad_threshold, etc.        |    sync / drift / desync          |
|                               |                                   |
|  PERSONA (4 fields)           |  [Pipecat Services]              |
|  DRIFT (4 fields)             |    STT Service instance           |
|  GUARDRAILS (1 field)         |    TTS Service instance           |
|  API KEYS (5 fields)          |    Transport instance             |
+-------------------------------+-----------------------------------+
|  ELI5: Like a mixing console -- 21 knobs, each controls      [sq]  |
|  one aspect of the signal chain.                                    |
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
    content: "VOICECONFIG ANATOMY"
    role: title

  - id: left_panel
    bounds: [40, 140, 900, 760]
    content: "21 Configuration Fields"
    role: content_area

  - id: right_panel
    bounds: [980, 140, 900, 760]
    content: "6 Enums + Pipecat Services"
    role: content_area

  - id: divider
    bounds: [940, 140, 2, 760]
    role: accent_line

  - id: eli5_callout
    bounds: [40, 920, 1840, 120]
    role: callout_box

anchors:
  - id: group_providers
    position: [80, 180]
    size: [820, 100]
    role: data_flow
    label: "PROVIDER SELECTION"

  - id: field_stt_provider
    position: [100, 200]
    size: [300, 30]
    role: data_flow
    label: "stt_provider"

  - id: field_tts_provider
    position: [100, 240]
    size: [300, 30]
    role: data_flow
    label: "tts_provider"

  - id: field_transport
    position: [100, 280]
    size: [300, 30]
    role: data_flow
    label: "transport"

  - id: group_stt_settings
    position: [80, 320]
    size: [820, 60]
    role: data_flow
    label: "STT SETTINGS"

  - id: group_server
    position: [80, 400]
    size: [820, 60]
    role: data_flow
    label: "SERVER"

  - id: group_vad
    position: [80, 480]
    size: [820, 80]
    role: data_flow
    label: "VAD TUNING"

  - id: group_persona
    position: [80, 580]
    size: [820, 80]
    role: data_flow
    label: "PERSONA"

  - id: group_drift
    position: [80, 680]
    size: [820, 80]
    role: data_flow
    label: "DRIFT"

  - id: group_guardrails
    position: [80, 780]
    size: [820, 40]
    role: data_flow
    label: "GUARDRAILS"

  - id: group_api_keys
    position: [80, 840]
    size: [820, 60]
    role: data_flow
    label: "API KEYS"

  - id: enum_stt_provider
    position: [1020, 180]
    size: [400, 60]
    role: decision_point
    label: "STTProvider"

  - id: enum_tts_provider
    position: [1020, 260]
    size: [400, 60]
    role: decision_point
    label: "TTSProvider"

  - id: enum_transport_type
    position: [1020, 340]
    size: [400, 60]
    role: decision_point
    label: "TransportType"

  - id: enum_whisper_model
    position: [1020, 420]
    size: [400, 60]
    role: decision_point
    label: "WhisperModel"

  - id: enum_drift_state
    position: [1020, 500]
    size: [400, 60]
    role: decision_point
    label: "DriftState"

  - id: pipecat_services
    position: [1020, 620]
    size: [400, 200]
    role: processing_stage
    label: "Pipecat Service Instances"

  - id: cascade_stt
    from: field_stt_provider
    to: enum_stt_provider
    type: arrow
    label: "enum lookup"

  - id: cascade_tts
    from: field_tts_provider
    to: enum_tts_provider
    type: arrow
    label: "enum lookup"

  - id: cascade_transport
    from: field_transport
    to: enum_transport_type
    type: arrow
    label: "enum lookup"

  - id: enum_to_service
    from: enum_stt_provider
    to: pipecat_services
    type: arrow
    label: "instantiate"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Provider Selection group | `data_flow` | 3 fields: stt_provider, tts_provider, transport |
| STT Settings group | `data_flow` | 1 field: whisper_model |
| Server group | `data_flow` | 2 fields: host, port |
| VAD Tuning group | `data_flow` | 3 fields: vad_threshold, vad_start_secs, vad_stop_secs |
| Persona group | `data_flow` | 4 fields: persona dimensions and prompt overrides |
| Drift group | `data_flow` | 4 fields: drift_monitoring, drift_threshold, drift_window, drift_action |
| Guardrails group | `data_flow` | 1 field: guardrails_enabled |
| API Keys group | `data_flow` | 5 fields: provider API keys |
| STTProvider enum | `decision_point` | whisper / deepgram / assemblyai |
| TTSProvider enum | `decision_point` | piper / kokoro / elevenlabs / cartesia |
| TransportType enum | `decision_point` | websocket / smallwebrtc / daily |
| WhisperModel enum | `decision_point` | tiny / base / small / medium / large |
| DriftState enum | `decision_point` | sync / drift / desync |
| Pipecat Services | `processing_stage` | Concrete STT, TTS, Transport instances |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| stt_provider field | STTProvider enum | arrow | "enum lookup" |
| tts_provider field | TTSProvider enum | arrow | "enum lookup" |
| transport field | TransportType enum | arrow | "enum lookup" |
| whisper_model field | WhisperModel enum | arrow | "enum lookup" |
| STTProvider enum | Pipecat STT Service | arrow | "instantiate" |
| TTSProvider enum | Pipecat TTS Service | arrow | "instantiate" |
| TransportType enum | Pipecat Transport | arrow | "instantiate" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Think of VoiceConfig like a recording studio's mixing console: one desk with 21 knobs and switches. Each knob (environment variable) controls one aspect of the signal chain, and moving a knob automatically reconfigures the right piece of gear. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "VOICECONFIG ANATOMY"
- Label 2: "PROVIDER SELECTION"
- Label 3: "stt_provider"
- Label 4: "tts_provider"
- Label 5: "transport"
- Label 6: "STT SETTINGS"
- Label 7: "SERVER"
- Label 8: "VAD TUNING"
- Label 9: "PERSONA"
- Label 10: "DRIFT"
- Label 11: "GUARDRAILS"
- Label 12: "API KEYS"
- Label 13: "STTProvider"
- Label 14: "TTSProvider"
- Label 15: "TransportType"
- Label 16: "WhisperModel"
- Label 17: "DriftState"
- Label 18: "Pipecat Service Instances"

### Caption (for embedding in documentation)

Split-panel diagram showing how VoiceConfig's 21 fields cascade through 6 typed enums to instantiate concrete Pipecat service instances, with field groupings on the left and enum-to-service mappings on the right.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `data_flow`, `decision_point` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "Pipecat", enum names are appropriate for L3 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text in the figure.

### Figure-Specific Rules

9. All 21 field names must exactly match the VoiceConfig class (use VOICE_ prefix for env vars).
10. Enum values must match the actual Python enum definitions.
11. Do NOT show default values in the visual -- they clutter the cascade view.
12. The cascade direction must flow left-to-right: env var to VoiceConfig field to enum to service.

## Alt Text

Split-panel showing VoiceConfig's 21 fields grouped by category cascading through 6 enums to Pipecat service instances.

## Image Embed

![Split-panel showing VoiceConfig's 21 fields grouped by category cascading through 6 enums to Pipecat service instances.](docs/figures/repo-figures/assets/fig-voice-34-voiceconfig-anatomy.jpg)

*Split-panel diagram showing how VoiceConfig's 21 fields cascade through 6 typed enums to instantiate concrete Pipecat service instances, with field groupings on the left and enum-to-service mappings on the right.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-34",
    "title": "VoiceConfig Anatomy",
    "audience": "L3",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "VoiceConfig is a single Pydantic Settings model that maps 21 environment variables through 6 typed enums to concrete Pipecat service instances.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "VoiceConfig Fields",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["PROVIDER SELECTION", "STT SETTINGS", "SERVER", "VAD TUNING", "PERSONA", "DRIFT", "GUARDRAILS", "API KEYS"]
      },
      {
        "name": "Typed Enums",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["STTProvider", "TTSProvider", "TransportType", "WhisperModel", "DriftState"]
      },
      {
        "name": "Pipecat Services",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["STT Service", "TTS Service", "Transport"]
      }
    ],
    "relationships": [
      {"from": "stt_provider", "to": "STTProvider", "type": "arrow", "label": "enum lookup"},
      {"from": "tts_provider", "to": "TTSProvider", "type": "arrow", "label": "enum lookup"},
      {"from": "transport", "to": "TransportType", "type": "arrow", "label": "enum lookup"},
      {"from": "STTProvider", "to": "STT Service", "type": "arrow", "label": "instantiate"},
      {"from": "TTSProvider", "to": "TTS Service", "type": "arrow", "label": "instantiate"},
      {"from": "TransportType", "to": "Transport", "type": "arrow", "label": "instantiate"}
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Think of VoiceConfig like a recording studio's mixing console: one desk with 21 knobs and switches. Each knob (environment variable) controls one aspect of the signal chain, and moving a knob automatically reconfigures the right piece of gear.",
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
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
