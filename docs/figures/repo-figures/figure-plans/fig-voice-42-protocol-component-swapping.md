# fig-voice-42: Protocol-Based Component Swapping

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-42 |
| **Title** | Protocol-Based Component Swapping |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md, new subsection (Appendix) |
| **Priority** | P2 (Nice-to-have) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Show STTServiceProtocol / TTSServiceProtocol / DriftDetectorProtocol -- structural typing means no inheritance. Show how multiple providers all satisfy the same duck-typed contract. Answers: "How do Python Protocols let us swap voice components without coupling?"

## Key Message

Python Protocols enable component swapping without class inheritance: any service that implements transcribe(audio) -> str and close() -> None satisfies STTServiceProtocol. This is structural typing (duck typing with type checking) -- providers don't need to know the protocol exists.

## Visual Concept

Multi-panel (Template B). Three columns, one per protocol. Each column shows: protocol definition at top (method signatures), then 2-3 concrete implementations below connected by dashed "satisfies" lines (NOT inheritance arrows). STTServiceProtocol column: WhisperSTTService, DeepgramSTTService, AssemblyAISTTService. TTSServiceProtocol: PiperTTSService, ElevenLabsTTSService, CartesiaTTSService. DriftDetectorProtocol: DriftDetector (embedding), JaccardDriftDetector (fallback). A callout: "No import needed -- structural typing."

```
+-------------------------------------------------------------------+
|  PROTOCOL-BASED COMPONENT SWAPPING                         [sq]    |
|  -- Structural Typing, Not Inheritance                             |
+-------------------------------------------------------------------+
|                    |                    |                           |
|  STTServiceProtocol|  TTSServiceProtocol|  DriftDetectorProtocol   |
|  ──────────────────|  ──────────────────|  ──────────────────────  |
|  transcribe(audio) |  synthesize(text)  |  score(response_text)    |
|    -> str          |    -> bytes        |    -> float              |
|  close() -> None   |  close() -> None   |  state() -> str          |
|         |          |         |          |         |                |
|    - - -|- - -     |    - - -|- - -     |    - - -|- - -           |
|         |          |         |          |         |                |
|  [WhisperSTT]      |  [PiperTTS]        |  [DriftDetector]         |
|         |          |         |          |    (embedding)            |
|    - - -|- - -     |    - - -|- - -     |         |                |
|         |          |         |          |    - - -|- - -           |
|  [DeepgramSTT]     |  [ElevenLabsTTS]   |         |                |
|         |          |         |          |  [JaccardDrift]           |
|    - - -|- - -     |    - - -|- - -     |    (fallback)             |
|         |          |         |          |                           |
|  [AssemblyAISTT]   |  [CartesiaTTS]     |                           |
|                    |                    |                           |
+-------------------------------------------------------------------+
|  "No import needed -- structural typing"                   [sq]    |
|  Like a 1/4-inch jack: any instrument fits the same connector.     |
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
    content: "PROTOCOL-BASED COMPONENT SWAPPING"
    role: title

  - id: stt_column
    bounds: [40, 140, 580, 700]
    role: content_area

  - id: tts_column
    bounds: [660, 140, 580, 700]
    role: content_area

  - id: drift_column
    bounds: [1280, 140, 600, 700]
    role: content_area

  - id: callout_zone
    bounds: [40, 920, 1840, 120]
    role: callout_box

anchors:
  - id: stt_protocol
    position: [320, 200]
    size: [480, 100]
    role: decision_point
    label: "STTServiceProtocol"

  - id: stt_signature
    position: [320, 280]
    size: [400, 60]
    role: data_flow
    label: "transcribe(audio) -> str"

  - id: whisper_impl
    position: [320, 420]
    size: [360, 50]
    role: processing_stage
    label: "WhisperSTTService"

  - id: deepgram_impl
    position: [320, 520]
    size: [360, 50]
    role: processing_stage
    label: "DeepgramSTTService"

  - id: assemblyai_impl
    position: [320, 620]
    size: [360, 50]
    role: processing_stage
    label: "AssemblyAISTTService"

  - id: tts_protocol
    position: [950, 200]
    size: [480, 100]
    role: decision_point
    label: "TTSServiceProtocol"

  - id: tts_signature
    position: [950, 280]
    size: [400, 60]
    role: data_flow
    label: "synthesize(text) -> bytes"

  - id: piper_impl
    position: [950, 420]
    size: [360, 50]
    role: processing_stage
    label: "PiperTTSService"

  - id: elevenlabs_impl
    position: [950, 520]
    size: [360, 50]
    role: processing_stage
    label: "ElevenLabsTTSService"

  - id: cartesia_impl
    position: [950, 620]
    size: [360, 50]
    role: processing_stage
    label: "CartesiaTTSService"

  - id: drift_protocol
    position: [1580, 200]
    size: [480, 100]
    role: decision_point
    label: "DriftDetectorProtocol"

  - id: drift_signature
    position: [1580, 280]
    size: [400, 60]
    role: data_flow
    label: "score(response_text) -> float"

  - id: embedding_drift
    position: [1580, 420]
    size: [360, 50]
    role: processing_stage
    label: "DriftDetector (embedding)"

  - id: jaccard_drift
    position: [1580, 540]
    size: [360, 50]
    role: processing_stage
    label: "JaccardDriftDetector"

  - id: stt_to_whisper
    from: stt_protocol
    to: whisper_impl
    type: dashed
    label: "satisfies"

  - id: stt_to_deepgram
    from: stt_protocol
    to: deepgram_impl
    type: dashed
    label: "satisfies"

  - id: stt_to_assemblyai
    from: stt_protocol
    to: assemblyai_impl
    type: dashed
    label: "satisfies"

  - id: tts_to_piper
    from: tts_protocol
    to: piper_impl
    type: dashed
    label: "satisfies"

  - id: tts_to_elevenlabs
    from: tts_protocol
    to: elevenlabs_impl
    type: dashed
    label: "satisfies"

  - id: tts_to_cartesia
    from: tts_protocol
    to: cartesia_impl
    type: dashed
    label: "satisfies"

  - id: drift_to_embedding
    from: drift_protocol
    to: embedding_drift
    type: dashed
    label: "satisfies"

  - id: drift_to_jaccard
    from: drift_protocol
    to: jaccard_drift
    type: dashed
    label: "satisfies"

  - id: col_divider_1
    position: [630, 140]
    size: [2, 700]
    role: accent_line_v

  - id: col_divider_2
    position: [1260, 140]
    size: [2, 700]
    role: accent_line_v
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| STTServiceProtocol | `decision_point` | Protocol definition: transcribe(audio: bytes) -> str, close() -> None |
| TTSServiceProtocol | `decision_point` | Protocol definition: synthesize(text: str) -> bytes, close() -> None |
| DriftDetectorProtocol | `decision_point` | Protocol definition: score(response_text: str) -> float, state() -> str |
| WhisperSTTService | `processing_stage` | Self-hosted Whisper implementation satisfying STT protocol |
| DeepgramSTTService | `processing_stage` | Deepgram Nova-3 cloud implementation satisfying STT protocol |
| AssemblyAISTTService | `processing_stage` | AssemblyAI cloud implementation satisfying STT protocol |
| PiperTTSService | `processing_stage` | Self-hosted Piper implementation satisfying TTS protocol |
| ElevenLabsTTSService | `processing_stage` | ElevenLabs cloud implementation satisfying TTS protocol |
| CartesiaTTSService | `processing_stage` | Cartesia Sonic cloud implementation satisfying TTS protocol |
| DriftDetector | `processing_stage` | Embedding-based drift detection (primary) |
| JaccardDriftDetector | `processing_stage` | Jaccard similarity fallback drift detection |
| Column dividers | `accent_line_v` | Vertical coral accent lines separating the three protocol columns |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| STTServiceProtocol | WhisperSTTService | dashed | "satisfies" |
| STTServiceProtocol | DeepgramSTTService | dashed | "satisfies" |
| STTServiceProtocol | AssemblyAISTTService | dashed | "satisfies" |
| TTSServiceProtocol | PiperTTSService | dashed | "satisfies" |
| TTSServiceProtocol | ElevenLabsTTSService | dashed | "satisfies" |
| TTSServiceProtocol | CartesiaTTSService | dashed | "satisfies" |
| DriftDetectorProtocol | DriftDetector | dashed | "satisfies" |
| DriftDetectorProtocol | JaccardDriftDetector | dashed | "satisfies" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "No import needed" | Like a standard 1/4-inch jack -- any guitar, synth, or bass can plug in because they all use the same connector shape. The instruments don't need to know about each other; they just need to fit the jack. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "STTServiceProtocol"
- Label 2: "TTSServiceProtocol"
- Label 3: "DriftDetectorProtocol"
- Label 4: "transcribe(audio) -> str"
- Label 5: "synthesize(text) -> bytes"
- Label 6: "score(response_text) -> float"
- Label 7: "close() -> None"
- Label 8: "state() -> str"
- Label 9: "WhisperSTTService"
- Label 10: "DeepgramSTTService"
- Label 11: "AssemblyAISTTService"
- Label 12: "PiperTTSService"
- Label 13: "ElevenLabsTTSService"
- Label 14: "CartesiaTTSService"
- Label 15: "DriftDetector (embedding)"
- Label 16: "JaccardDriftDetector"
- Label 17: "satisfies"
- Label 18: "No import needed"

### Caption (for embedding in documentation)

Three Python Protocols (STT, TTS, DriftDetector) with dashed "satisfies" lines to concrete implementations, showing structural typing enables component swapping without inheritance or explicit imports.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `decision_point`, `processing_stage`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon is ALLOWED** -- this is an L3 figure. Protocol, structural typing, transcribe(), synthesize() are appropriate.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text in the figure.

### Figure-Specific Rules

9. Connecting lines must be dashed (structural typing), NOT solid (inheritance).
10. Protocol method signatures must match actual protocols.py definitions.
11. Do NOT show UML class diagram notation -- this is about duck typing, not OOP.
12. The "no import needed" callout must be visually prominent.

## Alt Text

Three Protocol columns (STT, TTS, Drift) with dashed satisfies lines to implementations showing structural typing component swapping.

## Image Embed

![Three Protocol columns (STT, TTS, Drift) with dashed satisfies lines to implementations showing structural typing component swapping.](docs/figures/repo-figures/assets/fig-voice-42-protocol-component-swapping.jpg)

*Three Python Protocols (STT, TTS, DriftDetector) with dashed "satisfies" lines to concrete implementations, showing structural typing enables component swapping without inheritance or explicit imports.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-42",
    "title": "Protocol-Based Component Swapping",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Python Protocols enable component swapping without inheritance -- any service matching the method signatures satisfies the protocol via structural typing.",
    "layout_flow": "top-to-bottom-per-column",
    "key_structures": [
      {
        "name": "STTServiceProtocol",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["STTServiceProtocol", "transcribe(audio) -> str"]
      },
      {
        "name": "TTSServiceProtocol",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["TTSServiceProtocol", "synthesize(text) -> bytes"]
      },
      {
        "name": "DriftDetectorProtocol",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["DriftDetectorProtocol", "score(response_text) -> float"]
      },
      {
        "name": "STT Implementations",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["WhisperSTTService", "DeepgramSTTService", "AssemblyAISTTService"]
      },
      {
        "name": "TTS Implementations",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["PiperTTSService", "ElevenLabsTTSService", "CartesiaTTSService"]
      },
      {
        "name": "Drift Implementations",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["DriftDetector (embedding)", "JaccardDriftDetector"]
      }
    ],
    "relationships": [
      {"from": "STTServiceProtocol", "to": "WhisperSTTService", "type": "dashed", "label": "satisfies"},
      {"from": "STTServiceProtocol", "to": "DeepgramSTTService", "type": "dashed", "label": "satisfies"},
      {"from": "STTServiceProtocol", "to": "AssemblyAISTTService", "type": "dashed", "label": "satisfies"},
      {"from": "TTSServiceProtocol", "to": "PiperTTSService", "type": "dashed", "label": "satisfies"},
      {"from": "TTSServiceProtocol", "to": "ElevenLabsTTSService", "type": "dashed", "label": "satisfies"},
      {"from": "TTSServiceProtocol", "to": "CartesiaTTSService", "type": "dashed", "label": "satisfies"},
      {"from": "DriftDetectorProtocol", "to": "DriftDetector", "type": "dashed", "label": "satisfies"},
      {"from": "DriftDetectorProtocol", "to": "JaccardDriftDetector", "type": "dashed", "label": "satisfies"}
    ],
    "callout_boxes": [
      {
        "heading": "No import needed",
        "body_text": "Like a standard 1/4-inch jack -- any guitar, synth, or bass can plug in because they all use the same connector shape.",
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
- [ ] Anti-hallucination rules listed (8 default + 4 figure-specific)
- [ ] Alt text provided (125 chars max)
- [ ] JSON export block included
- [ ] Audience level correct (L3)
- [ ] Layout template identified (B)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
