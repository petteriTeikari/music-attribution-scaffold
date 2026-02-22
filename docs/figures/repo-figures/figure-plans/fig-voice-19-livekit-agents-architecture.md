# fig-voice-19: LiveKit Agents Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-19 |
| **Title** | LiveKit Agents Architecture |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Show the LiveKit Agents architecture where the agent joins a WebRTC session as a participant, with semantic turn detection, telephony integration, and the managed Cloud Agents deployment model. Answers: "How does LiveKit structure a voice agent, and what makes the agent-as-participant model different?"

## Key Message

LiveKit treats the voice agent as a first-class WebRTC participant -- it joins the room like any other user, enabling natural real-time communication with semantic turn detection, SIP telephony support, and a managed Cloud Agents deployment path.

## Visual Concept

Vertical step flow (Template E). Step I: Room -- the WebRTC room where users and agents coexist as participants. Step II: Agent Worker -- the Python/Node process that connects to the room. Step III: Voice Pipeline -- the internal STT -> LLM -> TTS chain within the agent. Step IV: Services -- pluggable STT, LLM, TTS providers. Step V: Cloud Agents -- managed deployment with auto-scaling. Side annotations for semantic turn detection and telephony 1.0 (SIP, DTMF).

```
+-------------------------------------------------------------------+
|  LIVEKIT AGENTS ARCHITECTURE                               [sq]   |
|  AGENT-AS-PARTICIPANT                                              |
+-------------------------------------------------------------------+
|                                                                    |
|  I   ROOM (WebRTC Session)                                         |
|      ┌─────────────────────────────────────────────────┐          |
|      │  Participant A    Participant B    Agent         │          |
|      │  (user)           (user)          (participant)  │          |
|      │      ↕               ↕               ↕          │          |
|      │           Real-time audio/video tracks           │          |
|      └─────────────────────────────────────────────────┘          |
|      ↓                                                             |
|  II  AGENT WORKER                                                  |
|      Python/Node process connected to room                         |
|      Receives audio tracks, publishes audio/data tracks            |
|      Semantic turn detection (acoustic + semantic)                 |
|      ↓                                                             |
|  III VOICE PIPELINE (VoicePipelineAgent)                           |
|      ┌─────┐  ┌─────┐  ┌─────┐                                   |
|      │ STT │→│ LLM │→│ TTS │                                   |
|      └─────┘  └─────┘  └─────┘                                   |
|      ↓                                                             |
|  IV  SERVICES                                                      |
|      ┌──────────┬──────────┬──────────┐                           |
|      │Deepgram  │ OpenAI   │Cartesia  │  + Telephony 1.0          |
|      │ Whisper  │Anthropic │ElevenLabs│  SIP trunking             |
|      │ Groq     │ Gemini   │ PlayHT   │  DTMF support            |
|      └──────────┴──────────┴──────────┘                           |
|      ↓                                                             |
|  V   CLOUD AGENTS (Managed Deployment)                             |
|      Auto-scaling, zero-config hosting                             |
|      Deploy agent code → LiveKit handles infrastructure            |
|                                                                    |
+-------------------------------------------------------------------+
|  "AGENT-AS-PARTICIPANT: The agent joins the WebRTC session         |
|   like any other user"                               [accent line] |
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
    content: "LIVEKIT AGENTS ARCHITECTURE"
    role: title

  - id: main_zone
    bounds: [40, 140, 1840, 800]
    role: content_area

  - id: callout_zone
    bounds: [40, 960, 1840, 80]
    content: "AGENT-AS-PARTICIPANT"
    role: callout_box

anchors:
  - id: step_i_room
    position: [80, 160]
    size: [1760, 160]
    role: processing_stage
    label: "I ROOM"

  - id: participant_a
    position: [200, 200]
    size: [300, 80]
    role: annotation
    label: "Participant A (user)"

  - id: participant_b
    position: [600, 200]
    size: [300, 80]
    role: annotation
    label: "Participant B (user)"

  - id: agent_participant
    position: [1000, 200]
    size: [300, 80]
    role: selected_option
    label: "Agent (participant)"

  - id: step_ii_worker
    position: [80, 360]
    size: [1760, 120]
    role: processing_stage
    label: "II AGENT WORKER"

  - id: step_iii_pipeline
    position: [80, 520]
    size: [1760, 120]
    role: processing_stage
    label: "III VOICE PIPELINE"

  - id: pipeline_stt
    position: [400, 550]
    size: [200, 60]
    role: processing_stage
    label: "STT"

  - id: pipeline_llm
    position: [700, 550]
    size: [200, 60]
    role: processing_stage
    label: "LLM"

  - id: pipeline_tts
    position: [1000, 550]
    size: [200, 60]
    role: processing_stage
    label: "TTS"

  - id: step_iv_services
    position: [80, 680]
    size: [1300, 140]
    role: module_grid
    label: "IV SERVICES"

  - id: telephony_sidebar
    position: [1420, 680]
    size: [420, 140]
    role: processing_stage
    label: "Telephony 1.0"

  - id: step_v_cloud
    position: [80, 860]
    size: [1760, 80]
    role: processing_stage
    label: "V CLOUD AGENTS"

  - id: flow_room_to_worker
    from: step_i_room
    to: step_ii_worker
    type: arrow
    label: "audio tracks"

  - id: flow_worker_to_pipeline
    from: step_ii_worker
    to: step_iii_pipeline
    type: arrow
    label: "processed audio"

  - id: flow_stt_to_llm
    from: pipeline_stt
    to: pipeline_llm
    type: arrow
    label: "transcript"

  - id: flow_llm_to_tts
    from: pipeline_llm
    to: pipeline_tts
    type: arrow
    label: "response"

  - id: flow_pipeline_to_services
    from: step_iii_pipeline
    to: step_iv_services
    type: bidirectional
    label: "service calls"

  - id: flow_services_to_cloud
    from: step_iv_services
    to: step_v_cloud
    type: arrow
    label: "deployment"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Room (Step I) | `processing_stage` | WebRTC session with users and agent as equal participants |
| User Participants | `annotation` | Human users in the WebRTC room |
| Agent Participant | `selected_option` | The voice agent joining as a first-class room participant |
| Agent Worker (Step II) | `processing_stage` | Python/Node process receiving audio tracks, with semantic turn detection |
| Voice Pipeline (Step III) | `processing_stage` | VoicePipelineAgent: STT -> LLM -> TTS internal chain |
| STT | `processing_stage` | Speech-to-text processor within the pipeline |
| LLM | `processing_stage` | Language model processor within the pipeline |
| TTS | `processing_stage` | Text-to-speech processor within the pipeline |
| Services (Step IV) | `module_grid` | Pluggable STT, LLM, TTS providers (Deepgram, OpenAI, Cartesia, etc.) |
| Telephony 1.0 | `processing_stage` | SIP trunking and DTMF support for phone integration |
| Cloud Agents (Step V) | `processing_stage` | Managed deployment with auto-scaling and zero-config hosting |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Room | Agent Worker | arrow | "audio tracks from room" |
| Agent Worker | Voice Pipeline | arrow | "processed audio to pipeline" |
| STT | LLM | arrow | "transcript" |
| LLM | TTS | arrow | "response text" |
| Voice Pipeline | Services | bidirectional | "service API calls" |
| Services | Cloud Agents | arrow | "managed deployment" |
| Agent Worker | Room | arrow | "published audio/data tracks" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "AGENT-AS-PARTICIPANT" | The agent joins the WebRTC session like any other user. It receives audio tracks, processes them through a voice pipeline, and publishes response audio back to the room. No special protocol -- just WebRTC. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I ROOM"
- Label 2: "II AGENT WORKER"
- Label 3: "III VOICE PIPELINE"
- Label 4: "IV SERVICES"
- Label 5: "V CLOUD AGENTS"
- Label 6: "Participant A (user)"
- Label 7: "Participant B (user)"
- Label 8: "Agent (participant)"
- Label 9: "STT"
- Label 10: "LLM"
- Label 11: "TTS"
- Label 12: "Semantic turn detection"
- Label 13: "VoicePipelineAgent"
- Label 14: "Telephony 1.0"
- Label 15: "SIP trunking"
- Label 16: "DTMF support"
- Label 17: "Auto-scaling"
- Label 18: "Zero-config hosting"

### Caption (for embedding in documentation)

Step-by-step architecture of LiveKit Agents showing the agent-as-participant model in a WebRTC room, with voice pipeline (STT -> LLM -> TTS), pluggable services, telephony integration, and managed Cloud Agents deployment.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `module_grid`, `selected_option` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The agent-as-participant model is LiveKit's core differentiator. The agent MUST be shown as an equal participant in the Room, not as an external service.
10. LiveKit Agents supports both Python and Node.js SDKs. The primary examples use Python.
11. VoicePipelineAgent is the specific class name for the voice pipeline in LiveKit Agents. Do NOT generalize to "Pipeline" or "Agent."
12. Telephony 1.0 includes SIP trunking and DTMF support -- these are real LiveKit features announced in 2025.
13. Cloud Agents is LiveKit's managed hosting product. It auto-scales agent workers. Do NOT confuse with self-hosted deployment.
14. LiveKit's semantic turn detection uses acoustic + semantic signals, similar to but independent from Deepgram Flux or Pipecat Smart Turn.
15. The Room is a LiveKit-specific concept -- it is a real-time communication session, not a chat room.
16. Roman numerals I-V must be used for step headers.

## Alt Text

Architecture diagram of LiveKit Agents showing the agent-as-participant model where the voice agent joins a WebRTC room alongside users, with VoicePipelineAgent (STT, LLM, TTS), pluggable services, telephony 1.0 SIP integration, and managed Cloud Agents deployment.

## Image Embed

![Architecture diagram of LiveKit Agents showing the agent-as-participant model where the voice agent joins a WebRTC room alongside users, with VoicePipelineAgent (STT, LLM, TTS), pluggable services, telephony 1.0 SIP integration, and managed Cloud Agents deployment.](docs/figures/repo-figures/assets/fig-voice-19-livekit-agents-architecture.jpg)

*Step-by-step architecture of LiveKit Agents showing the agent-as-participant model in a WebRTC room, with voice pipeline (STT -> LLM -> TTS), pluggable services, telephony integration, and managed Cloud Agents deployment.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-19",
    "title": "LiveKit Agents Architecture",
    "audience": "L3",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "LiveKit treats the voice agent as a first-class WebRTC participant that joins the room like any other user, with semantic turn detection and managed Cloud Agents deployment.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Room",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["I ROOM", "WebRTC Session", "participants"]
      },
      {
        "name": "Agent Worker",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["II AGENT WORKER", "semantic turn detection"]
      },
      {
        "name": "Voice Pipeline",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["III VOICE PIPELINE", "VoicePipelineAgent", "STT", "LLM", "TTS"]
      },
      {
        "name": "Services",
        "role": "module_grid",
        "is_highlighted": false,
        "labels": ["IV SERVICES", "Deepgram", "OpenAI", "Cartesia"]
      },
      {
        "name": "Telephony 1.0",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Telephony 1.0", "SIP trunking", "DTMF"]
      },
      {
        "name": "Cloud Agents",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["V CLOUD AGENTS", "auto-scaling", "zero-config"]
      }
    ],
    "relationships": [
      {
        "from": "Room",
        "to": "Agent Worker",
        "type": "arrow",
        "label": "audio tracks"
      },
      {
        "from": "Agent Worker",
        "to": "Voice Pipeline",
        "type": "arrow",
        "label": "processed audio"
      },
      {
        "from": "STT",
        "to": "LLM",
        "type": "arrow",
        "label": "transcript"
      },
      {
        "from": "LLM",
        "to": "TTS",
        "type": "arrow",
        "label": "response"
      },
      {
        "from": "Voice Pipeline",
        "to": "Services",
        "type": "bidirectional",
        "label": "service calls"
      }
    ],
    "callout_boxes": [
      {
        "heading": "AGENT-AS-PARTICIPANT",
        "body_text": "The agent joins the WebRTC session like any other user. No special protocol -- just WebRTC.",
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
