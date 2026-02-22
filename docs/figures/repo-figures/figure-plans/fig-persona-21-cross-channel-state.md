# fig-persona-21: Cross-Channel State Synchronization

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-21 |
| **Title** | Cross-Channel State Synchronization |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/architecture/persona.md, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Shows how three interaction channels -- Chat (AG-UI/CopilotKit), Voice (Pipecat), and MCP (machine-to-machine) -- converge on a shared backend state store. Answers: "How does the system maintain a unified user model across all modalities?"

## Key Message

All three interaction channels read and write to a shared PostgreSQL + pgvector state store, ensuring proficiency model, session context, and persona state remain consistent regardless of which channel the user or agent enters through.

## Visual Concept

Three channel nodes arranged across the top, each flowing bidirectionally into a central shared state store at the bottom. The state store is decomposed into three sub-layers: proficiency model, session context, and persona state. Bidirectional sync arrows emphasize that every channel both reads and writes state.

```
+---------------------------------------------------------------+
|  CROSS-CHANNEL STATE SYNCHRONIZATION                           |
+---------------------------------------------------------------+
|                                                                |
|   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       |
|   │  CHAT         │  │  VOICE        │  │  MCP          │       |
|   │  AG-UI /      │  │  Pipecat      │  │  Machine-to-  │       |
|   │  CopilotKit   │  │  WebSocket    │  │  Machine      │       |
|   └──────┬───────┘  └──────┬───────┘  └──────┬───────┘       |
|          │ ▲               │ ▲               │ ▲               |
|          │ │               │ │               │ │               |
|          ▼ │               ▼ │               ▼ │               |
|   ┌────────────────────────────────────────────────────┐       |
|   │             SHARED BACKEND STATE STORE              │       |
|   │             PostgreSQL + pgvector                   │       |
|   │  ┌────────────┬───────────────┬───────────────┐    │       |
|   │  │ Proficiency │ Session       │ Persona       │    │       |
|   │  │ Model       │ Context       │ State         │    │       |
|   │  └────────────┴───────────────┴───────────────┘    │       |
|   └────────────────────────────────────────────────────┘       |
|                                                                |
+---------------------------------------------------------------+
|  VOICE INTERACTIONS UPDATE THE SAME USER MODEL AS TEXT CHAT    |
+---------------------------------------------------------------+
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
    content: "CROSS-CHANNEL STATE SYNCHRONIZATION"
    role: title

  - id: channels_zone
    bounds: [80, 160, 1760, 300]
    role: content_area

  - id: state_store_zone
    bounds: [200, 560, 1520, 300]
    role: content_area

  - id: callout_zone
    bounds: [80, 920, 1760, 120]
    role: callout_box

anchors:
  - id: channel_chat
    position: [320, 280]
    size: [400, 180]
    role: api_endpoint
    label: "CHAT (AG-UI / CopilotKit)"

  - id: channel_voice
    position: [960, 280]
    size: [400, 180]
    role: api_endpoint
    label: "VOICE (Pipecat)"

  - id: channel_mcp
    position: [1600, 280]
    size: [400, 180]
    role: api_endpoint
    label: "MCP (Machine-to-Machine)"

  - id: state_store
    position: [960, 680]
    size: [1200, 240]
    role: storage_layer
    label: "PostgreSQL + pgvector"

  - id: sub_proficiency
    position: [560, 720]
    size: [300, 100]
    role: processing_stage
    label: "Proficiency Model"

  - id: sub_session
    position: [960, 720]
    size: [300, 100]
    role: processing_stage
    label: "Session Context"

  - id: sub_persona
    position: [1360, 720]
    size: [300, 100]
    role: processing_stage
    label: "Persona State"

  - id: sync_chat_to_store
    from: channel_chat
    to: state_store
    type: bidirectional
    label: "read/write state"

  - id: sync_voice_to_store
    from: channel_voice
    to: state_store
    type: bidirectional
    label: "read/write state"

  - id: sync_mcp_to_store
    from: channel_mcp
    to: state_store
    type: bidirectional
    label: "read/write state"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "CROSS-CHANNEL STATE SYNCHRONIZATION" with accent square |
| Chat channel | `api_endpoint` | AG-UI / CopilotKit text interaction channel |
| Voice channel | `api_endpoint` | Pipecat WebSocket real-time voice channel |
| MCP channel | `api_endpoint` | Machine-to-machine protocol channel for agents |
| Shared state store | `storage_layer` | PostgreSQL + pgvector central persistence |
| Proficiency model | `processing_stage` | User skill level tracking (novice to expert) |
| Session context | `processing_stage` | Current conversation and interaction history |
| Persona state | `processing_stage` | Agent personality parameters and drift baseline |
| Callout bar | `callout_bar` | Key insight about cross-channel consistency |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Chat channel | Shared state store | bidirectional | "read/write state" |
| Voice channel | Shared state store | bidirectional | "read/write state" |
| MCP channel | Shared state store | bidirectional | "read/write state" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "CROSS-CHANNEL CONSISTENCY" | Voice interactions update the same user model as text chat -- no state fragmentation across modalities | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "CHAT (AG-UI / CopilotKit)"
- Label 2: "VOICE (Pipecat)"
- Label 3: "MCP (Machine-to-Machine)"
- Label 4: "PostgreSQL + pgvector"
- Label 5: "Proficiency Model"
- Label 6: "Session Context"
- Label 7: "Persona State"
- Label 8: "read/write state"

### Caption (for embedding in documentation)

Cross-channel state synchronization architecture showing three interaction channels (Chat, Voice, MCP) converging on a shared PostgreSQL + pgvector backend state store that maintains proficiency model, session context, and persona state across all modalities.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `api_endpoint`, `storage_layer`, `processing_stage` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink" should NOT appear unless the figure is L3/L4 audience. This figure IS L3 so PostgreSQL, pgvector, AG-UI, CopilotKit, Pipecat, MCP ARE allowed.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Three channels MUST be shown as peers -- no hierarchy between Chat, Voice, and MCP.
10. All arrows MUST be bidirectional -- channels both read from and write to the state store.
11. The state store MUST show three sub-components: proficiency model, session context, persona state.
12. Do NOT imply Voice or MCP are secondary to Chat -- they are equal-status channels.
13. AG-UI is the protocol, CopilotKit is the SDK -- both are correct labels for the Chat channel.
14. Pipecat is the voice agent framework -- do NOT substitute with "WebRTC" or "Twilio".
15. MCP is Model Context Protocol for machine-to-machine -- do NOT confuse with other acronyms.
16. The callout must emphasize cross-channel consistency, not just architecture.

## Alt Text

Flowchart showing cross-channel state synchronization where Chat, Voice, and MCP channels read and write bidirectionally to a shared PostgreSQL and pgvector backend state store containing proficiency model, session context, and persona state for unified user modeling across modalities

## Image Embed

![Flowchart showing cross-channel state synchronization where Chat, Voice, and MCP channels read and write bidirectionally to a shared PostgreSQL and pgvector backend state store containing proficiency model, session context, and persona state for unified user modeling across modalities](docs/figures/repo-figures/assets/fig-persona-21-cross-channel-state.jpg)

*Cross-channel state synchronization architecture showing three interaction channels (Chat, Voice, MCP) converging on a shared PostgreSQL + pgvector backend state store that maintains proficiency model, session context, and persona state across all modalities.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-21",
    "title": "Cross-Channel State Synchronization",
    "audience": "L3",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "All three interaction channels read and write to a shared PostgreSQL + pgvector state store, ensuring proficiency model, session context, and persona state remain consistent across modalities.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Chat Channel",
        "role": "api_endpoint",
        "is_highlighted": false,
        "labels": ["CHAT (AG-UI / CopilotKit)"]
      },
      {
        "name": "Voice Channel",
        "role": "api_endpoint",
        "is_highlighted": false,
        "labels": ["VOICE (Pipecat)"]
      },
      {
        "name": "MCP Channel",
        "role": "api_endpoint",
        "is_highlighted": false,
        "labels": ["MCP (Machine-to-Machine)"]
      },
      {
        "name": "Shared State Store",
        "role": "storage_layer",
        "is_highlighted": true,
        "labels": ["PostgreSQL + pgvector", "Proficiency Model", "Session Context", "Persona State"]
      }
    ],
    "relationships": [
      {
        "from": "Chat Channel",
        "to": "Shared State Store",
        "type": "bidirectional",
        "label": "read/write state"
      },
      {
        "from": "Voice Channel",
        "to": "Shared State Store",
        "type": "bidirectional",
        "label": "read/write state"
      },
      {
        "from": "MCP Channel",
        "to": "Shared State Store",
        "type": "bidirectional",
        "label": "read/write state"
      }
    ],
    "callout_boxes": [
      {
        "heading": "CROSS-CHANNEL CONSISTENCY",
        "body_text": "Voice interactions update the same user model as text chat -- no state fragmentation across modalities",
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
- [x] Anti-hallucination rules listed (8 default + 8 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L3)
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
