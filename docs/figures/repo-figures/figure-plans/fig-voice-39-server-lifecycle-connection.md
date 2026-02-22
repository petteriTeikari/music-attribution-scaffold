# fig-voice-39: Server Lifecycle & Connection Management

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-39 |
| **Title** | Server Lifecycle & Connection Management |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md, Section 12.1 |
| **Priority** | P1 (Important) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Show FastAPI startup -> create_voice_router() -> WS accept -> asyncio.Lock -> build_pipecat_pipeline() -> PipelineRunner -> cleanup. Shows the lock pattern and MAX_CONNECTIONS=10. Answers: "What happens when a voice client connects, and how are concurrent connections limited?"

## Key Message

Each WebSocket connection creates a fresh Pipecat pipeline guarded by an asyncio.Lock, with a hard limit of 10 concurrent connections. The lifecycle is: accept -> lock -> build pipeline -> run -> cleanup on disconnect.

## Visual Concept

Flowchart (Template C) top-to-bottom. Entry: FastAPI startup -> include_router(create_voice_router()). Then: WS /api/v1/voice/ws accept. Decision diamond: "active < MAX_CONNECTIONS (10)?" If no: reject with 503. If yes: asyncio.Lock acquire -> build_pipecat_pipeline(config, ws) -> PipelineRunner.run(pipeline) -> on disconnect: cleanup, release lock, decrement counter. Side note: GET /api/v1/voice/health reports active count.

```
+-------------------------------------------------------------------+
|  SERVER LIFECYCLE & CONNECTION MANAGEMENT                    [sq]   |
|  -- WebSocket Pipeline with asyncio.Lock Guard                     |
+-------------------------------------------------------------------+
|                                                                    |
|  FastAPI startup                                                   |
|  include_router(create_voice_router())                             |
|        │                                                           |
|        ▼                                                           |
|  TWO ENDPOINTS REGISTERED                                          |
|  ┌─────────────────────┐    ┌─────────────────────┐               |
|  │ WS /api/v1/voice/ws  │    │ GET /api/v1/voice/  │               |
|  │ (voice sessions)     │    │     health           │               |
|  └──────────┬──────────┘    │ (reports active cnt) │               |
|             │                └─────────────────────┘               |
|             ▼                                                      |
|      ◇ active < MAX_CONNECTIONS (10)?                              |
|     / \                                                            |
|   NO    YES                                                        |
|   │       │                                                        |
|   ▼       ▼                                                        |
|  Reject  asyncio.Lock acquire                                      |
|  503     active_connections += 1                                   |
|           │                                                        |
|           ▼                                                        |
|  build_pipecat_pipeline(config, ws)                                |
|           │                                                        |
|           ▼                                                        |
|  PipelineRunner.run(pipeline)                                      |
|  ┌─────────────────────────────┐                                  |
|  │  ■ STT -> LLM -> TTS loop    │                                  |
|  │  ■ Runs until disconnect      │                                  |
|  └──────────┬──────────────────┘                                  |
|             │ (disconnect / error)                                  |
|             ▼                                                      |
|  CLEANUP                                                           |
|  ■ pipeline.stop()                                                 |
|  ■ active_connections -= 1                                         |
|  ■ asyncio.Lock release                                            |
|  ■ WebSocket close                                                 |
|                                                                    |
+-------------------------------------------------------------------+
|  ELI5: Recording studio with 10 booths -- each gets a fresh       |
|  mixing setup, cleaned and reset when the artist leaves            |
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
    content: "SERVER LIFECYCLE & CONNECTION MANAGEMENT"
    role: title

  - id: flow_zone
    bounds: [200, 140, 1200, 700]
    role: content_area

  - id: health_zone
    bounds: [1400, 200, 440, 120]
    role: content_area

  - id: callout_zone
    bounds: [60, 940, 1800, 100]
    content: "ELI5: Recording studio with 10 booths"
    role: callout_box

anchors:
  - id: startup
    position: [800, 180]
    size: [600, 50]
    role: processing_stage
    label: "FastAPI startup"

  - id: ws_endpoint
    position: [600, 280]
    size: [400, 80]
    role: processing_stage
    label: "WS /api/v1/voice/ws"

  - id: health_endpoint
    position: [1500, 280]
    size: [360, 80]
    role: processing_stage
    label: "GET /api/v1/voice/health"

  - id: decision_diamond
    position: [600, 400]
    size: [400, 60]
    role: decision_point
    label: "active < MAX_CONNECTIONS (10)?"

  - id: reject_503
    position: [300, 500]
    size: [200, 50]
    role: security_layer
    label: "Reject 503"

  - id: lock_acquire
    position: [800, 500]
    size: [400, 60]
    role: security_layer
    label: "asyncio.Lock acquire"

  - id: build_pipeline
    position: [800, 600]
    size: [400, 60]
    role: processing_stage
    label: "build_pipecat_pipeline()"

  - id: pipeline_runner
    position: [800, 700]
    size: [400, 100]
    role: processing_stage
    label: "PipelineRunner.run()"

  - id: cleanup
    position: [800, 850]
    size: [400, 120]
    role: processing_stage
    label: "CLEANUP"

  - id: flow_startup_to_ws
    from: startup
    to: ws_endpoint
    type: arrow
    label: "include_router"

  - id: flow_ws_to_decision
    from: ws_endpoint
    to: decision_diamond
    type: arrow
    label: "WS accept"

  - id: flow_decision_no
    from: decision_diamond
    to: reject_503
    type: arrow
    label: "NO"

  - id: flow_decision_yes
    from: decision_diamond
    to: lock_acquire
    type: arrow
    label: "YES"

  - id: flow_lock_to_build
    from: lock_acquire
    to: build_pipeline
    type: arrow
    label: "locked"

  - id: flow_build_to_run
    from: build_pipeline
    to: pipeline_runner
    type: arrow
    label: "fresh pipeline"

  - id: flow_run_to_cleanup
    from: pipeline_runner
    to: cleanup
    type: arrow
    label: "disconnect / error"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "SERVER LIFECYCLE & CONNECTION MANAGEMENT" with coral accent square |
| FastAPI startup | `processing_stage` | Application startup, include_router(create_voice_router()) |
| WS endpoint | `processing_stage` | WebSocket /api/v1/voice/ws -- voice session entry point |
| Health endpoint | `processing_stage` | GET /api/v1/voice/health -- reports active connection count |
| Connection decision | `decision_point` | Diamond: "active < MAX_CONNECTIONS (10)?" |
| Reject 503 | `security_layer` | Connection refused when at capacity |
| asyncio.Lock acquire | `security_layer` | Lock acquisition + increment active counter |
| build_pipecat_pipeline | `processing_stage` | Creates fresh Pipecat pipeline for each connection |
| PipelineRunner.run | `processing_stage` | Runs the STT -> LLM -> TTS loop until disconnect |
| Cleanup block | `processing_stage` | pipeline.stop(), decrement counter, release lock, close WS |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| FastAPI startup | WS endpoint | arrow | "include_router" |
| WS endpoint | Decision diamond | arrow | "WS accept" |
| Decision diamond | Reject 503 | arrow | "NO (at capacity)" |
| Decision diamond | asyncio.Lock | arrow | "YES (under limit)" |
| asyncio.Lock | build_pipecat_pipeline | arrow | "lock acquired" |
| build_pipecat_pipeline | PipelineRunner | arrow | "fresh pipeline" |
| PipelineRunner | Cleanup | arrow | "disconnect / error" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Think of the voice server like a recording studio with 10 booths: when all booths are occupied, new artists have to wait. Each booth (WebSocket connection) gets its own fresh mixing setup (pipeline), and when the artist leaves, the booth is cleaned and reset for the next session. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "FastAPI startup"
- Label 2: "create_voice_router()"
- Label 3: "WS /api/v1/voice/ws"
- Label 4: "GET /api/v1/voice/health"
- Label 5: "active < MAX_CONNECTIONS?"
- Label 6: "MAX_CONNECTIONS = 10"
- Label 7: "Reject 503"
- Label 8: "asyncio.Lock acquire"
- Label 9: "active_connections += 1"
- Label 10: "build_pipecat_pipeline()"
- Label 11: "PipelineRunner.run(pipeline)"
- Label 12: "STT -> LLM -> TTS loop"
- Label 13: "CLEANUP"
- Label 14: "pipeline.stop()"
- Label 15: "active_connections -= 1"
- Label 16: "asyncio.Lock release"
- Label 17: "WebSocket close"
- Label 18: "Reports active count"

### Caption (for embedding in documentation)

Server lifecycle flowchart for voice agent WebSocket connections -- FastAPI startup registers the voice router, each incoming WebSocket is checked against MAX_CONNECTIONS (10), guarded by asyncio.Lock, builds a fresh Pipecat pipeline, runs until disconnect, then cleans up resources and releases the connection slot.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `decision_point`, `security_layer` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon is ALLOWED** -- this is an L3 figure targeting software engineers. asyncio.Lock, WebSocket, PipelineRunner, FastAPI are appropriate.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. MAX_CONNECTIONS value must be 10 (matching the actual server.py implementation). Do NOT use any other number.
10. The asyncio.Lock must be shown explicitly as a synchronization mechanism guarding the pipeline build, not just a generic "lock" icon.
11. The two endpoints (WS /api/v1/voice/ws and GET /api/v1/voice/health) must both be shown as registered routes.
12. The cleanup path must show explicit resource release: pipeline.stop(), decrement counter, release lock, close WebSocket -- not just "disconnect."
13. The decision diamond must show the comparison against MAX_CONNECTIONS, with reject-503 on the "no" branch.
14. Each WebSocket connection gets a FRESH pipeline -- this is not a shared/pooled pipeline.

## Alt Text

Server lifecycle flowchart: FastAPI startup to WebSocket accept, MAX_CONNECTIONS=10 guard, asyncio.Lock, fresh Pipecat pipeline per connection, cleanup on disconnect.

## Image Embed

![Server lifecycle flowchart: FastAPI startup to WebSocket accept, MAX_CONNECTIONS=10 guard, asyncio.Lock, fresh Pipecat pipeline per connection, cleanup on disconnect.](docs/figures/repo-figures/assets/fig-voice-39-server-lifecycle-connection.jpg)

*Server lifecycle flowchart for voice agent WebSocket connections -- FastAPI startup registers the voice router, each incoming WebSocket is checked against MAX_CONNECTIONS (10), guarded by asyncio.Lock, builds a fresh Pipecat pipeline, runs until disconnect, then cleans up resources and releases the connection slot.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-39",
    "title": "Server Lifecycle & Connection Management",
    "audience": "L3",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "Each WebSocket connection creates a fresh Pipecat pipeline guarded by asyncio.Lock, with a hard limit of 10 concurrent connections and explicit cleanup on disconnect.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "FastAPI Startup",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["FastAPI startup", "create_voice_router()"]
      },
      {
        "name": "WebSocket Endpoint",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["WS /api/v1/voice/ws"]
      },
      {
        "name": "Health Endpoint",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["GET /api/v1/voice/health", "Reports active count"]
      },
      {
        "name": "Connection Guard",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["active < MAX_CONNECTIONS?", "MAX_CONNECTIONS = 10"]
      },
      {
        "name": "Reject Path",
        "role": "security_layer",
        "is_highlighted": false,
        "labels": ["Reject 503"]
      },
      {
        "name": "Lock + Build",
        "role": "security_layer",
        "is_highlighted": true,
        "labels": ["asyncio.Lock acquire", "build_pipecat_pipeline()"]
      },
      {
        "name": "Pipeline Runner",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["PipelineRunner.run()", "STT -> LLM -> TTS loop"]
      },
      {
        "name": "Cleanup",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["pipeline.stop()", "decrement counter", "release lock", "close WS"]
      }
    ],
    "relationships": [
      {
        "from": "FastAPI startup",
        "to": "WS endpoint",
        "type": "arrow",
        "label": "include_router"
      },
      {
        "from": "WS endpoint",
        "to": "Connection Guard",
        "type": "arrow",
        "label": "WS accept"
      },
      {
        "from": "Connection Guard",
        "to": "Reject 503",
        "type": "arrow",
        "label": "NO"
      },
      {
        "from": "Connection Guard",
        "to": "Lock + Build",
        "type": "arrow",
        "label": "YES"
      },
      {
        "from": "Lock + Build",
        "to": "Pipeline Runner",
        "type": "arrow",
        "label": "fresh pipeline"
      },
      {
        "from": "Pipeline Runner",
        "to": "Cleanup",
        "type": "arrow",
        "label": "disconnect"
      }
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Recording studio with 10 booths: each gets a fresh mixing setup, cleaned and reset when the artist leaves.",
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
- [x] Anti-hallucination rules listed (8 default + 6 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L3)
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
