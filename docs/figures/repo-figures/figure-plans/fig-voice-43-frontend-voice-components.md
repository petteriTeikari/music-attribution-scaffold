# fig-voice-43: Frontend Voice Components

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-43 |
| **Title** | Frontend Voice Components |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md, Section 12 (new subsection) |
| **Priority** | P2 (Nice-to-have) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Show Jotai atoms (voiceStateAtom, voiceConnectionAtom) -> createVoiceClient() -> WebSocket -> backend. Shows the frontend-to-backend boundary. Answers: "How does the browser-side voice layer connect to the server-side pipeline?"

## Key Message

The frontend voice layer uses Jotai atoms for state management and a WebSocket client for audio streaming, with a clear boundary between browser-side (React + Jotai) and server-side (FastAPI + Pipecat).

## Visual Concept

Multi-panel (Template B). Left panel: "BROWSER" with React components, Jotai atoms (voiceStateAtom: idle/listening/thinking/speaking, voiceConnectionAtom: disconnected/connecting/connected), and createVoiceClient(). Right panel: "SERVER" with FastAPI WebSocket endpoint, Pipecat pipeline. Center: WebSocket connection arrow crossing a coral accent line marking the browser-to-server boundary. Audio frames flow bidirectionally.

```
+-------------------------------------------------------------------+
|  FRONTEND VOICE COMPONENTS                                 [sq]    |
|  -- Browser-to-Server Architecture                                 |
+-------------------------------------------------------------------+
|                              |                                     |
|   BROWSER                    |[accent]   SERVER                     |
|   ───────                    | line      ──────                     |
|                              |                                     |
|   [VoiceButton]              |           [FastAPI WS Endpoint]      |
|       |                      |                |                     |
|   [voiceStateAtom]           |           [Pipecat Pipeline]         |
|     idle | listening         |                |                     |
|     thinking | speaking      |           [STT] -> [LLM] -> [TTS]   |
|       |                      |                                     |
|   [voiceConnectionAtom]      |                                     |
|     disconnected             |                                     |
|     connecting | connected   |                                     |
|       |                      |                                     |
|   [createVoiceClient()]      |                                     |
|       |                      |                                     |
|       +--- audio frames ---->|-----> audio in                       |
|       |<--- audio frames ----|<----- audio out                      |
|       |     WebSocket        |                                     |
|                              |                                     |
|   [VoiceIndicator]           |                                     |
|     Shows current state      |                                     |
|     (animated)               |                                     |
|                              |                                     |
|   +------------------------+ |                                     |
|   | idle -> listening ->   | |                                     |
|   | thinking -> speaking   | |                                     |
|   | (cycle)                | |                                     |
|   +------------------------+ |                                     |
+-------------------------------------------------------------------+
|  ELI5: Frontend = stage monitor. Server = backstage rack.  [sq]    |
|  WebSocket = single audio cable.                                   |
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
    content: "FRONTEND VOICE COMPONENTS"
    role: title

  - id: browser_panel
    bounds: [40, 140, 860, 700]
    content: "BROWSER"
    role: content_area

  - id: server_panel
    bounds: [1020, 140, 860, 700]
    content: "SERVER"
    role: content_area

  - id: eli5_callout
    bounds: [40, 920, 1840, 120]
    role: callout_box

anchors:
  - id: browser_heading
    position: [440, 180]
    size: [300, 50]
    role: heading_display
    label: "BROWSER"

  - id: voice_button
    position: [300, 280]
    size: [280, 50]
    role: processing_stage
    label: "VoiceButton"

  - id: voice_state_atom
    position: [300, 380]
    size: [360, 80]
    role: data_flow
    label: "voiceStateAtom"

  - id: state_cycle
    position: [300, 500]
    size: [400, 80]
    role: feedback_loop
    label: "idle -> listening -> ..."

  - id: voice_connection_atom
    position: [300, 560]
    size: [360, 60]
    role: data_flow
    label: "voiceConnectionAtom"

  - id: create_voice_client
    position: [300, 660]
    size: [360, 50]
    role: processing_stage
    label: "createVoiceClient()"

  - id: voice_indicator
    position: [660, 380]
    size: [200, 50]
    role: data_flow
    label: "VoiceIndicator"

  - id: boundary_line
    position: [940, 140]
    size: [4, 700]
    role: accent_line_v
    label: "browser/server boundary"

  - id: server_heading
    position: [1440, 180]
    size: [300, 50]
    role: heading_display
    label: "SERVER"

  - id: fastapi_ws
    position: [1440, 300]
    size: [360, 60]
    role: processing_stage
    label: "FastAPI WS Endpoint"

  - id: pipecat_pipeline
    position: [1440, 420]
    size: [360, 60]
    role: processing_stage
    label: "Pipecat Pipeline"

  - id: stt_stage
    position: [1280, 540]
    size: [160, 50]
    role: processing_stage
    label: "STT"

  - id: llm_stage
    position: [1440, 540]
    size: [160, 50]
    role: processing_stage
    label: "LLM"

  - id: tts_stage
    position: [1600, 540]
    size: [160, 50]
    role: processing_stage
    label: "TTS"

  - id: ws_audio_out
    from: create_voice_client
    to: fastapi_ws
    type: arrow
    label: "audio frames (WebSocket)"

  - id: ws_audio_in
    from: fastapi_ws
    to: create_voice_client
    type: arrow
    label: "audio response"

  - id: stt_to_llm
    from: stt_stage
    to: llm_stage
    type: arrow
    label: "text"

  - id: llm_to_tts
    from: llm_stage
    to: tts_stage
    type: arrow
    label: "response"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Browser panel | `content_area` | Left panel: React components and Jotai atoms |
| VoiceButton | `processing_stage` | UI component triggering voice mode |
| voiceStateAtom | `data_flow` | Jotai atom: idle, listening, thinking, speaking |
| voiceConnectionAtom | `data_flow` | Jotai atom: disconnected, connecting, connected |
| createVoiceClient() | `processing_stage` | WebSocket lifecycle manager for audio streaming |
| VoiceIndicator | `data_flow` | Animated UI showing current voice state |
| Voice state cycle | `feedback_loop` | idle -> listening -> thinking -> speaking (cycle) |
| Browser/server boundary | `accent_line_v` | Coral accent line marking the architectural split |
| Server panel | `content_area` | Right panel: FastAPI + Pipecat pipeline |
| FastAPI WS Endpoint | `processing_stage` | WebSocket endpoint accepting audio connections |
| Pipecat Pipeline | `processing_stage` | Server-side audio processing pipeline |
| STT -> LLM -> TTS chain | `processing_stage` | Three-stage server processing: speech-to-text, inference, text-to-speech |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| VoiceButton | voiceStateAtom | arrow | "triggers state change" |
| voiceStateAtom | VoiceIndicator | arrow | "drives animation" |
| voiceConnectionAtom | createVoiceClient() | arrow | "manages lifecycle" |
| createVoiceClient() | FastAPI WS Endpoint | arrow | "audio frames (WebSocket)" |
| FastAPI WS Endpoint | createVoiceClient() | arrow | "audio response" |
| FastAPI WS Endpoint | Pipecat Pipeline | arrow | "routes audio" |
| STT | LLM | arrow | "transcribed text" |
| LLM | TTS | arrow | "response text" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Think of the frontend as the performer's stage monitor: it shows whether the mic is live (listening), the producer is thinking (processing), or the response is playing back (speaking). The heavy lifting happens in the backstage rack (server), connected by a single audio cable (WebSocket). | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "BROWSER"
- Label 2: "SERVER"
- Label 3: "VoiceButton"
- Label 4: "voiceStateAtom"
- Label 5: "voiceConnectionAtom"
- Label 6: "createVoiceClient()"
- Label 7: "VoiceIndicator"
- Label 8: "FastAPI WS Endpoint"
- Label 9: "Pipecat Pipeline"
- Label 10: "STT"
- Label 11: "LLM"
- Label 12: "TTS"
- Label 13: "audio frames (WebSocket)"
- Label 14: "idle | listening"
- Label 15: "thinking | speaking"
- Label 16: "disconnected | connecting"

### Caption (for embedding in documentation)

Frontend voice architecture showing Jotai atoms (voiceStateAtom, voiceConnectionAtom) and createVoiceClient() in the browser, connected via WebSocket to the FastAPI + Pipecat server pipeline (STT -> LLM -> TTS).

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `data_flow`, `feedback_loop` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon is ALLOWED** -- this is an L3 figure. Jotai, WebSocket, FastAPI, Pipecat are appropriate.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text in the figure.

### Figure-Specific Rules

9. Jotai atom names must be plausible but clearly labeled as "planned" since frontend voice UI is aspirational/Pro tier.
10. The WebSocket boundary must be visually prominent as the key architectural split.
11. Do NOT show CopilotKit components in this diagram -- voice is a separate path.
12. Voice state machine (idle -> listening -> thinking -> speaking) must be shown as a cycle.

## Alt Text

Browser-to-server voice architecture: Jotai atoms and createVoiceClient() connect via WebSocket to FastAPI + Pipecat pipeline.

## Image Embed

![Browser-to-server voice architecture: Jotai atoms and createVoiceClient() connect via WebSocket to FastAPI + Pipecat pipeline.](docs/figures/repo-figures/assets/fig-voice-43-frontend-voice-components.jpg)

*Frontend voice architecture showing Jotai atoms (voiceStateAtom, voiceConnectionAtom) and createVoiceClient() in the browser, connected via WebSocket to the FastAPI + Pipecat server pipeline (STT -> LLM -> TTS).*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-43",
    "title": "Frontend Voice Components",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "The frontend voice layer uses Jotai atoms for state and a WebSocket client for audio streaming, with a clear browser/server boundary.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Jotai Voice Atoms",
        "role": "data_flow",
        "is_highlighted": true,
        "labels": ["voiceStateAtom", "voiceConnectionAtom"]
      },
      {
        "name": "createVoiceClient()",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["createVoiceClient()", "WebSocket lifecycle"]
      },
      {
        "name": "Browser/Server Boundary",
        "role": "accent_line_v",
        "is_highlighted": true,
        "labels": ["WebSocket boundary"]
      },
      {
        "name": "FastAPI WS Endpoint",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["FastAPI WS Endpoint"]
      },
      {
        "name": "Pipecat Pipeline",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["STT", "LLM", "TTS"]
      },
      {
        "name": "Voice State Cycle",
        "role": "feedback_loop",
        "is_highlighted": false,
        "labels": ["idle", "listening", "thinking", "speaking"]
      }
    ],
    "relationships": [
      {"from": "createVoiceClient()", "to": "FastAPI WS Endpoint", "type": "arrow", "label": "audio frames (WebSocket)"},
      {"from": "FastAPI WS Endpoint", "to": "createVoiceClient()", "type": "arrow", "label": "audio response"},
      {"from": "STT", "to": "LLM", "type": "arrow", "label": "transcribed text"},
      {"from": "LLM", "to": "TTS", "type": "arrow", "label": "response text"}
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Frontend = stage monitor showing mic status. Server = backstage rack doing the heavy lifting. WebSocket = single audio cable connecting them.",
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
