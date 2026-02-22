# fig-voice-04: Voice Agent Framework Decision

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-04 |
| **Title** | Voice Agent Framework Decision |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Map the voice agent framework decision tree from the top-level build-vs-buy choice through open-source and managed options to a recommended selection. Answers: "Which framework should we use for the voice agent, and why?"

## Key Message

Pipecat is the recommended MVP framework -- Python-native, open-source, and directly compatible with the existing PydanticAI agent stack.

## Visual Concept

Decision tree (Template C) starting with a root node "VOICE FRAMEWORK?" that branches into three paths: Open-Source, Managed, and Custom. Open-Source branches into Pipecat (highlighted as selected) and LiveKit Agents. Managed branches into Retell AI and Vapi. Custom is shown as a terminal node with a caution indicator. Each leaf node has 2-3 bullet annotations. Pipecat's node uses `selected_option` semantic tag with a coral accent square. A horizontal callout bar at the bottom reinforces the recommendation. Decision criteria labels on the branch lines.

```
+---------------------------------------------------------------------+
|  VOICE AGENT FRAMEWORK                                       [sq]   |
|  DECISION TREE                                                      |
|                                                                     |
|                    VOICE FRAMEWORK?                                  |
|                   /       |        \                                 |
|             open-src   managed    custom                             |
|              /    \     /    \       |                               |
|         Pipecat  LiveKit  Retell  Vapi   Build from                  |
|         [SELECTED]  Agents   AI    AI    Scratch                     |
|                                                                     |
|         Python     Rust     Managed  Managed   Full                  |
|         native     core     voice    voice     control               |
|         PydanticAI WebRTC   flows    flows     High cost             |
|         compatible built-in Monthly  Per-min   6+ months             |
|                             pricing  pricing                         |
|                                                                     |
|  RECOMMENDATION: PIPECAT FOR MVP                             [line] |
|  Python-native, matches PydanticAI stack, open-source               |
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
    content: "VOICE AGENT FRAMEWORK DECISION TREE"
    role: title

  - id: tree_zone
    bounds: [80, 140, 1760, 700]
    role: content_area

  - id: callout_zone
    bounds: [80, 880, 1760, 160]
    content: "RECOMMENDATION: PIPECAT FOR MVP"
    role: callout_box

anchors:
  - id: root_node
    position: [840, 180]
    size: [240, 80]
    role: decision_node
    label: "VOICE FRAMEWORK?"

  - id: branch_opensource
    position: [320, 340]
    size: [200, 60]
    role: category_node
    label: "OPEN-SOURCE"

  - id: branch_managed
    position: [840, 340]
    size: [200, 60]
    role: category_node
    label: "MANAGED"

  - id: branch_custom
    position: [1360, 340]
    size: [200, 60]
    role: category_node
    label: "CUSTOM"

  - id: node_pipecat
    position: [160, 480]
    size: [280, 240]
    role: selected_option
    label: "PIPECAT"

  - id: node_livekit
    position: [500, 480]
    size: [280, 240]
    role: processing_stage
    label: "LIVEKIT AGENTS"

  - id: node_retell
    position: [720, 480]
    size: [260, 240]
    role: processing_stage
    label: "RETELL AI"

  - id: node_vapi
    position: [1020, 480]
    size: [260, 240]
    role: processing_stage
    label: "VAPI"

  - id: node_custom
    position: [1300, 480]
    size: [280, 240]
    role: caution_node
    label: "BUILD FROM SCRATCH"

  - id: recommendation_bar
    position: [80, 900]
    size: [1760, 120]
    role: callout_box
    label: "RECOMMENDATION: PIPECAT FOR MVP"

  - id: flow_root_to_opensource
    from: root_node
    to: branch_opensource
    type: arrow
    label: "open-source"

  - id: flow_root_to_managed
    from: root_node
    to: branch_managed
    type: arrow
    label: "managed"

  - id: flow_root_to_custom
    from: root_node
    to: branch_custom
    type: arrow
    label: "custom"

  - id: flow_os_to_pipecat
    from: branch_opensource
    to: node_pipecat
    type: arrow
    label: "Python-native"

  - id: flow_os_to_livekit
    from: branch_opensource
    to: node_livekit
    type: arrow
    label: "Rust core"

  - id: flow_managed_to_retell
    from: branch_managed
    to: node_retell
    type: arrow
    label: "monthly"

  - id: flow_managed_to_vapi
    from: branch_managed
    to: node_vapi
    type: arrow
    label: "per-minute"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Root Decision | `decision_node` | Top-level "Voice Framework?" decision point |
| Open-Source Branch | `category_node` | Category for open-source frameworks |
| Managed Branch | `category_node` | Category for managed/hosted voice platforms |
| Custom Branch | `category_node` | Category for building from scratch |
| Pipecat | `selected_option` | Python-native open-source framework (SELECTED) |
| LiveKit Agents | `processing_stage` | Rust-core open-source framework with WebRTC built-in |
| Retell AI | `processing_stage` | Managed voice platform with monthly pricing |
| Vapi | `processing_stage` | Managed voice platform with per-minute pricing |
| Build from Scratch | `caution_node` | Custom build option with high cost/time warning |
| Recommendation Bar | `callout_box` | Full-width recommendation callout for Pipecat |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| Root Decision | Open-Source Branch | arrow | "control + flexibility" |
| Root Decision | Managed Branch | arrow | "speed to market" |
| Root Decision | Custom Branch | arrow | "full control" |
| Open-Source Branch | Pipecat | arrow | "Python-native" |
| Open-Source Branch | LiveKit Agents | arrow | "Rust core" |
| Managed Branch | Retell AI | arrow | "monthly pricing" |
| Managed Branch | Vapi | arrow | "per-minute pricing" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "RECOMMENDATION: PIPECAT FOR MVP" | Python-native framework, directly compatible with PydanticAI agent stack. Open-source (Apache 2.0). Supports Deepgram, Cartesia, ElevenLabs, OpenAI TTS. WebRTC and WebSocket transports. Daily.co backing for production reliability. | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "VOICE FRAMEWORK?"
- Label 2: "OPEN-SOURCE"
- Label 3: "MANAGED"
- Label 4: "CUSTOM"
- Label 5: "PIPECAT"
- Label 6: "LIVEKIT AGENTS"
- Label 7: "RETELL AI"
- Label 8: "VAPI"
- Label 9: "BUILD FROM SCRATCH"
- Label 10: "Python-native"
- Label 11: "PydanticAI compatible"
- Label 12: "Apache 2.0"
- Label 13: "Rust core, WebRTC built-in"
- Label 14: "Monthly pricing"
- Label 15: "Per-minute pricing"
- Label 16: "Full control, high cost"
- Label 17: "6+ months to production"
- Label 18: "SELECTED"

### Caption

Decision tree mapping the voice agent framework choice from build-vs-buy through open-source and managed options, with Pipecat selected as the recommended MVP framework for Python-native PydanticAI compatibility.

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

8. Pipecat MUST be visually distinguished from other options -- use `selected_option` semantic tag with accent treatment.
9. "Build from Scratch" must have a caution visual indicator -- it is explicitly NOT recommended.
10. Decision branch labels (on the connecting lines) must describe the selection criterion, not the option name.
11. Each leaf node should show 2-3 concise annotation bullets, not paragraphs of text.
12. Do NOT show pricing numbers -- just "monthly" vs "per-minute" as pricing model indicators.
13. Do NOT render company logos -- text labels only.

## Alt Text

Decision tree for voice agent framework selection comparing open-source (Pipecat, LiveKit), managed (Retell AI, Vapi), and custom options, with Pipecat highlighted as the recommended Python-native MVP choice for music attribution.

## Image Embed

![Decision tree for voice agent framework selection comparing open-source (Pipecat, LiveKit), managed (Retell AI, Vapi), and custom options, with Pipecat highlighted as the recommended Python-native MVP choice for music attribution.](docs/figures/repo-figures/assets/fig-voice-04-framework-landscape.jpg)

*Decision tree mapping the voice agent framework choice from build-vs-buy through open-source and managed options, with Pipecat selected as the recommended MVP framework for Python-native PydanticAI compatibility.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-04",
    "title": "Voice Agent Framework Decision",
    "audience": "L3",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "Pipecat is the recommended MVP framework -- Python-native, open-source, and compatible with PydanticAI.",
    "layout_flow": "top-to-bottom-tree",
    "key_structures": [
      {
        "name": "Root Decision",
        "role": "decision_node",
        "is_highlighted": false,
        "labels": ["VOICE FRAMEWORK?"]
      },
      {
        "name": "Pipecat",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["PIPECAT", "Python-native", "PydanticAI compatible", "Apache 2.0"]
      },
      {
        "name": "LiveKit Agents",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["LIVEKIT AGENTS", "Rust core", "WebRTC built-in"]
      },
      {
        "name": "Retell AI",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["RETELL AI", "Monthly pricing"]
      },
      {
        "name": "Vapi",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["VAPI", "Per-minute pricing"]
      },
      {
        "name": "Build from Scratch",
        "role": "caution_node",
        "is_highlighted": false,
        "labels": ["BUILD FROM SCRATCH", "Full control", "6+ months"]
      }
    ],
    "relationships": [
      {
        "from": "Root Decision",
        "to": "Open-Source",
        "type": "arrow",
        "label": "control + flexibility"
      },
      {
        "from": "Root Decision",
        "to": "Managed",
        "type": "arrow",
        "label": "speed to market"
      },
      {
        "from": "Root Decision",
        "to": "Custom",
        "type": "arrow",
        "label": "full control"
      },
      {
        "from": "Open-Source",
        "to": "Pipecat",
        "type": "arrow",
        "label": "Python-native"
      },
      {
        "from": "Open-Source",
        "to": "LiveKit Agents",
        "type": "arrow",
        "label": "Rust core"
      }
    ],
    "callout_boxes": [
      {
        "heading": "RECOMMENDATION: PIPECAT FOR MVP",
        "body_text": "Python-native framework, directly compatible with PydanticAI agent stack. Open-source (Apache 2.0). Supports Deepgram, Cartesia, ElevenLabs. WebRTC and WebSocket transports.",
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
- [ ] Layout template identified (C)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
