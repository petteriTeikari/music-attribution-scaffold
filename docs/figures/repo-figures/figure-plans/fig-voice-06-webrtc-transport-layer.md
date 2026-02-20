# fig-voice-06: Voice Transport: WebRTC vs WebSocket

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-06 |
| **Title** | Voice Transport: WebRTC vs WebSocket |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P2 |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Compare the two primary voice transport protocols side by side, showing why WebRTC is preferred for production voice agents while WebSocket remains a viable simpler alternative. Answers: "Which transport protocol should we use for voice streaming, and what are the tradeoffs?"

## Key Message

WebRTC provides sub-30ms transport with built-in echo cancellation and adaptive bitrate -- the production choice -- while WebSocket adds 50-100ms but offers simpler implementation.

## Visual Concept

Split-panel layout (Template D). Left panel (full color, emphasized): WebRTC transport showing the peer connection flow with STUN/TURN, built-in echo cancellation, adaptive bitrate, and sub-30ms latency badge. Right panel (muted/de-emphasized): WebSocket transport showing the simpler client-server model with audio chunk streaming, 50-100ms added latency, and no built-in audio processing. A horizontal accent line divides the two panels. The left panel uses full-saturation semantic colors while the right uses muted tones to visually communicate the recommendation. A callout bar at the bottom notes framework support.

```
+----------------------------------+----------------------------------+
|  WEBRTC                    [sq]  |  WEBSOCKET                       |
|  RECOMMENDED                     |  SIMPLER ALTERNATIVE             |
|  (full color)                    |  (muted)                         |
|                                  |                                  |
|  +--------+     +--------+      |  +--------+     +--------+       |
|  | Client | <-> | Server |      |  | Client | --> | Server |       |
|  +--------+     +--------+      |  +--------+     +--------+       |
|       |  STUN/TURN  |           |       |  HTTP Upgrade  |          |
|       |  ICE        |           |       |  Audio Chunks  |          |
|       +------+------+           |       +------+---------+          |
|              |                  |              |                    |
|  BUILT-IN:                      |  REQUIRES:                       |
|  * Echo cancellation            |  * External AEC library          |
|  * Adaptive bitrate             |  * Manual bitrate control        |
|  * Jitter buffering             |  * Custom jitter handling        |
|  * Noise suppression            |  * Separate noise filter         |
|                                  |                                  |
|  LATENCY: <30ms         [badge] |  LATENCY: 50-100ms added        |
|  P2P when possible               |  Always through server           |
|                                  |                                  |
+----------------------------------+----------------------------------+
|  BOTH PIPECAT AND LIVEKIT SUPPORT WEBRTC                     [line] |
+---------------------------------------------------------------------+
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
    content: "VOICE TRANSPORT"
    role: title

  - id: left_panel
    bounds: [40, 140, 900, 720]
    content: "WebRTC"
    role: content_area

  - id: right_panel
    bounds: [980, 140, 900, 720]
    content: "WebSocket"
    role: content_area

  - id: callout_zone
    bounds: [40, 900, 1840, 140]
    content: "BOTH PIPECAT AND LIVEKIT SUPPORT WEBRTC"
    role: callout_box

anchors:
  - id: webrtc_client
    position: [120, 240]
    size: [200, 100]
    role: processing_stage
    label: "CLIENT"

  - id: webrtc_server
    position: [560, 240]
    size: [200, 100]
    role: processing_stage
    label: "SERVER"

  - id: webrtc_connection
    from: webrtc_client
    to: webrtc_server
    type: bidirectional
    label: "STUN/TURN ICE"

  - id: webrtc_features
    position: [120, 420]
    size: [700, 280]
    role: annotation
    label: "Built-in features"

  - id: webrtc_latency_badge
    position: [120, 740]
    size: [200, 60]
    role: confidence_high
    label: "<30ms"

  - id: ws_client
    position: [1060, 240]
    size: [200, 100]
    role: processing_stage
    label: "CLIENT"

  - id: ws_server
    position: [1500, 240]
    size: [200, 100]
    role: processing_stage
    label: "SERVER"

  - id: ws_connection
    from: ws_client
    to: ws_server
    type: arrow
    label: "HTTP Upgrade"

  - id: ws_features
    position: [1060, 420]
    size: [700, 280]
    role: annotation
    label: "Requires external"

  - id: ws_latency_badge
    position: [1060, 740]
    size: [240, 60]
    role: confidence_medium
    label: "50-100ms added"

  - id: divider_line
    position: [960, 140]
    size: [2, 720]
    role: accent_line

  - id: recommendation_bar
    position: [80, 920]
    size: [1760, 100]
    role: callout_box
    label: "BOTH PIPECAT AND LIVEKIT SUPPORT WEBRTC"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| WebRTC Client | `processing_stage` | Browser/app client with WebRTC peer connection |
| WebRTC Server | `processing_stage` | Media server with STUN/TURN/ICE negotiation |
| WebRTC Features | `annotation` | Built-in: echo cancellation, adaptive bitrate, jitter buffering, noise suppression |
| WebRTC Latency | `confidence_high` | Sub-30ms transport latency badge |
| WebSocket Client | `processing_stage` | Browser/app client with WebSocket connection |
| WebSocket Server | `processing_stage` | HTTP server with WebSocket upgrade |
| WebSocket Features | `annotation` | Requires external: AEC library, manual bitrate, custom jitter, separate noise filter |
| WebSocket Latency | `confidence_medium` | 50-100ms added latency badge |
| Panel Divider | `accent_line` | Vertical line separating the two transport options |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| WebRTC Client | WebRTC Server | bidirectional | "STUN/TURN peer connection" |
| WebSocket Client | WebSocket Server | arrow | "HTTP upgrade, audio chunks" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "BOTH PIPECAT AND LIVEKIT SUPPORT WEBRTC" | Both recommended open-source frameworks include WebRTC transport as a first-class option. Pipecat uses Daily.co transport. LiveKit has native WebRTC. WebSocket fallback available in both for simpler deployments. | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "WEBRTC"
- Label 2: "RECOMMENDED"
- Label 3: "WEBSOCKET"
- Label 4: "SIMPLER ALTERNATIVE"
- Label 5: "CLIENT"
- Label 6: "SERVER"
- Label 7: "STUN/TURN"
- Label 8: "ICE Negotiation"
- Label 9: "HTTP Upgrade"
- Label 10: "Audio Chunks"
- Label 11: "Echo cancellation"
- Label 12: "Adaptive bitrate"
- Label 13: "Jitter buffering"
- Label 14: "Noise suppression"
- Label 15: "External AEC library"
- Label 16: "Manual bitrate control"
- Label 17: "Custom jitter handling"
- Label 18: "<30ms"
- Label 19: "50-100ms added"
- Label 20: "P2P when possible"
- Label 21: "Always through server"

### Caption

Split-panel comparison of WebRTC and WebSocket voice transport protocols, with WebRTC recommended for its sub-30ms latency and built-in audio processing capabilities.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text
3. **Hex codes are INTERNAL** -- do NOT render them
4. **Background MUST be warm cream (#f6f3e6)**
5. **No generic flowchart aesthetics**
6. **No figure captions** -- no "Figure 1." prefix
7. **No prompt leakage**

### Figure-Specific Rules

8. The WebRTC panel (left) MUST use full-saturation colors -- it is the recommended option.
9. The WebSocket panel (right) MUST use muted/desaturated tones -- it is the secondary option.
10. The WebRTC connection must be bidirectional (two-way arrows) -- peer-to-peer communication.
11. The WebSocket connection should be unidirectional or show explicit request/response -- client-server model.
12. Do NOT show specific port numbers, IP addresses, or codec names (Opus, PCM, etc.) in the main panels.
13. Latency badges should use `confidence_high` (green) for WebRTC and `confidence_medium` (amber) for WebSocket.
14. "P2P when possible" is a key differentiator and must be visible on the WebRTC side.

## Alt Text

Split-panel comparison of WebRTC and WebSocket voice transport protocols for real-time voice agents, showing WebRTC recommended with sub-30ms latency and built-in echo cancellation versus WebSocket adding 50-100ms overhead.

## Image Embed

![Split-panel comparison of WebRTC and WebSocket voice transport protocols for real-time voice agents, showing WebRTC recommended with sub-30ms latency and built-in echo cancellation versus WebSocket adding 50-100ms overhead.](docs/figures/repo-figures/assets/fig-voice-06-webrtc-transport-layer.jpg)

*Split-panel comparison of WebRTC and WebSocket voice transport protocols, with WebRTC recommended for its sub-30ms latency and built-in audio processing capabilities.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-06",
    "title": "Voice Transport: WebRTC vs WebSocket",
    "audience": "L3",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "WebRTC provides sub-30ms transport with built-in echo cancellation -- the production choice for voice agents.",
    "layout_flow": "side-by-side",
    "key_structures": [
      {
        "name": "WebRTC Panel",
        "role": "content_area",
        "is_highlighted": true,
        "labels": ["WEBRTC", "RECOMMENDED", "<30ms", "Echo cancellation", "Adaptive bitrate"]
      },
      {
        "name": "WebSocket Panel",
        "role": "content_area",
        "is_highlighted": false,
        "labels": ["WEBSOCKET", "SIMPLER ALTERNATIVE", "50-100ms added", "External AEC required"]
      }
    ],
    "relationships": [
      {
        "from": "WebRTC Client",
        "to": "WebRTC Server",
        "type": "bidirectional",
        "label": "STUN/TURN peer connection"
      },
      {
        "from": "WebSocket Client",
        "to": "WebSocket Server",
        "type": "arrow",
        "label": "HTTP upgrade, audio chunks"
      }
    ],
    "callout_boxes": [
      {
        "heading": "BOTH PIPECAT AND LIVEKIT SUPPORT WEBRTC",
        "body_text": "Both recommended frameworks include WebRTC as first-class transport. WebSocket fallback available for simpler deployments.",
        "position": "bottom-full-width"
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
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
