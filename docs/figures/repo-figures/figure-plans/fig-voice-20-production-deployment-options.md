# fig-voice-20: Voice Agent Deployment Options

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-20 |
| **Title** | Voice Agent Deployment Options |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Present a decision tree for choosing a voice agent deployment strategy, from fully managed platforms through framework-based approaches to fully self-hosted stacks. Answers: "How much control do I need, and what deployment path matches my team's constraints?"

## Key Message

Path B (Framework + Cloud APIs) is the sweet spot for most teams -- it provides framework flexibility with API simplicity, costing $0.05-0.10/min without the DevOps burden of self-hosting or the vendor lock-in of managed platforms.

## Visual Concept

Flowchart (Template C) starting with the decision question "How much control do you need?" branching into four paths. Path A (Managed): Retell/Vapi, fastest to market, $0.07-0.14/min. Path B (Framework + APIs): Pipecat/LiveKit + Deepgram/ElevenLabs, $0.05-0.10/min, highlighted as sweet spot. Path C (Self-Hosted): Pipecat + faster-whisper + Orpheus, $0.01-0.02/min, DevOps required. Path D (Hybrid): Cloud LLM + on-device STT/TTS, lowest cost at scale. Path B is visually highlighted with accent treatment.

```
+-------------------------------------------------------------------+
|  VOICE AGENT DEPLOYMENT OPTIONS                            [sq]   |
|                                                                    |
|           "How much control do you need?"                          |
|                    ↓                                               |
|    ┌───────────┬───────────┬───────────┬───────────┐              |
|    ↓           ↓           ↓           ↓           |              |
|  PATH A      PATH B      PATH C      PATH D                       |
|  MANAGED     FRAMEWORK   SELF-       HYBRID                       |
|              + APIs      HOSTED                                    |
|                                                                    |
|  Retell      Pipecat     Pipecat     Cloud LLM                    |
|  Vapi        LiveKit     faster-     + on-device                   |
|  Bland       + Deepgram  whisper     STT/TTS                      |
|              + ElevenLabs + Orpheus                                |
|              + Cartesia   + vLLM                                   |
|                                                                    |
|  $0.07-      $0.05-      $0.01-      Variable                     |
|  0.14/min    0.10/min    0.02/min    (lowest at                   |
|                                       scale)                       |
|                                                                    |
|  Fastest     SWEET       Full        Edge                          |
|  to market   SPOT ■      control     deployment                   |
|  Locked in   Flexible    DevOps      Complex                       |
|              ^^^^^^^^^^^^            setup                          |
|              RECOMMENDED                                           |
|                                                                    |
+-------------------------------------------------------------------+
|  "PATH B IS THE SWEET SPOT — framework flexibility                |
|   with API simplicity"                               [accent line] |
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
    content: "VOICE AGENT DEPLOYMENT OPTIONS"
    role: title

  - id: decision_zone
    bounds: [700, 140, 520, 60]
    content: "How much control do you need?"
    role: decision_point

  - id: paths_zone
    bounds: [40, 240, 1840, 660]
    role: content_area

  - id: callout_zone
    bounds: [40, 940, 1840, 100]
    content: "PATH B IS THE SWEET SPOT"
    role: callout_box

anchors:
  - id: decision_node
    position: [760, 140]
    size: [400, 60]
    role: decision_point
    label: "How much control?"

  - id: path_a_managed
    position: [60, 260]
    size: [420, 620]
    role: branching_path
    label: "PATH A MANAGED"

  - id: path_b_framework
    position: [520, 260]
    size: [420, 620]
    role: selected_option
    label: "PATH B FRAMEWORK + APIs"

  - id: path_c_selfhosted
    position: [980, 260]
    size: [420, 620]
    role: branching_path
    label: "PATH C SELF-HOSTED"

  - id: path_d_hybrid
    position: [1440, 260]
    size: [420, 620]
    role: branching_path
    label: "PATH D HYBRID"

  - id: flow_decision_to_a
    from: decision_node
    to: path_a_managed
    type: arrow
    label: "none (outsource)"

  - id: flow_decision_to_b
    from: decision_node
    to: path_b_framework
    type: arrow
    label: "moderate"

  - id: flow_decision_to_c
    from: decision_node
    to: path_c_selfhosted
    type: arrow
    label: "full"

  - id: flow_decision_to_d
    from: decision_node
    to: path_d_hybrid
    type: arrow
    label: "edge + cloud"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Decision Node | `decision_point` | "How much control do you need?" -- the root question |
| Path A: Managed | `branching_path` | Retell, Vapi, Bland -- fully managed, $0.07-0.14/min, fastest to market, vendor lock-in |
| Path B: Framework + APIs | `selected_option` | Pipecat/LiveKit + Deepgram/ElevenLabs/Cartesia -- $0.05-0.10/min, flexible, recommended sweet spot |
| Path C: Self-Hosted | `branching_path` | Pipecat + faster-whisper + Orpheus + vLLM -- $0.01-0.02/min, full control, DevOps required |
| Path D: Hybrid | `branching_path` | Cloud LLM + on-device STT/TTS -- variable cost, lowest at scale, complex setup |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Decision Node | Path A: Managed | arrow | "none (outsource everything)" |
| Decision Node | Path B: Framework + APIs | arrow | "moderate (choose components)" |
| Decision Node | Path C: Self-Hosted | arrow | "full (own everything)" |
| Decision Node | Path D: Hybrid | arrow | "edge + cloud mix" |
| Path B: Framework + APIs | Path C: Self-Hosted | dashed | "migrate as volume grows" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "PATH B IS THE SWEET SPOT" | Framework flexibility with API simplicity. Start with Pipecat or LiveKit + cloud STT/TTS APIs. Migrate individual components to self-hosted as volume grows and team matures. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "How much control do you need?"
- Label 2: "PATH A: MANAGED"
- Label 3: "PATH B: FRAMEWORK + APIs"
- Label 4: "PATH C: SELF-HOSTED"
- Label 5: "PATH D: HYBRID"
- Label 6: "Retell / Vapi / Bland"
- Label 7: "Pipecat / LiveKit"
- Label 8: "Deepgram / ElevenLabs"
- Label 9: "faster-whisper / Orpheus"
- Label 10: "Cloud LLM + on-device"
- Label 11: "$0.07-0.14/min"
- Label 12: "$0.05-0.10/min"
- Label 13: "$0.01-0.02/min"
- Label 14: "Fastest to market"
- Label 15: "SWEET SPOT"
- Label 16: "Full control"
- Label 17: "Edge deployment"
- Label 18: "Vendor lock-in"
- Label 19: "DevOps required"

### Caption (for embedding in documentation)

Decision tree for voice agent deployment showing four paths from fully managed ($0.07-0.14/min) through framework + APIs ($0.05-0.10/min, recommended sweet spot) to self-hosted ($0.01-0.02/min) and hybrid edge + cloud approaches.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `decision_point`, `branching_path`, `selected_option` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Cost ranges are approximate industry averages as of early 2026. Managed: $0.07-0.14/min includes Retell and Vapi pricing. Framework + APIs: $0.05-0.10/min based on Deepgram + ElevenLabs + Claude API costs. Self-hosted: $0.01-0.02/min based on GPU amortization. Do NOT present as exact quotes.
10. Retell, Vapi, and Bland are the three major managed voice agent platforms. Do NOT add others to this list.
11. faster-whisper is a CTranslate2-based Whisper implementation for self-hosted STT. Orpheus is an open-source TTS model. These are real projects.
12. Path B must be visually highlighted as the recommended option -- it is the "sweet spot" for most teams.
13. The migration path from B to C is deliberate -- teams start with APIs and move to self-hosted as they scale. This progression arrow must be visible.
14. Path D (Hybrid) is the most architecturally complex. It involves running STT/TTS on device while using cloud LLMs. Do NOT simplify this.
15. vLLM is the self-hosted LLM serving solution referenced in Path C. It is a real open-source project.
16. Do NOT imply any path is "wrong" -- each suits different constraints (time, budget, team, scale).

## Alt Text

Decision tree flowchart for voice agent deployment showing four paths: managed platforms (Retell/Vapi, $0.07-0.14/min), framework + cloud APIs (Pipecat/LiveKit, $0.05-0.10/min, highlighted as sweet spot), self-hosted open-source ($0.01-0.02/min), and hybrid edge + cloud approaches.

## Image Embed

![Decision tree flowchart for voice agent deployment showing four paths: managed platforms (Retell/Vapi, $0.07-0.14/min), framework + cloud APIs (Pipecat/LiveKit, $0.05-0.10/min, highlighted as sweet spot), self-hosted open-source ($0.01-0.02/min), and hybrid edge + cloud approaches.](docs/figures/repo-figures/assets/fig-voice-20-production-deployment-options.jpg)

*Decision tree for voice agent deployment showing four paths from fully managed ($0.07-0.14/min) through framework + APIs ($0.05-0.10/min, recommended sweet spot) to self-hosted ($0.01-0.02/min) and hybrid edge + cloud approaches.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-20",
    "title": "Voice Agent Deployment Options",
    "audience": "L3",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "Path B (Framework + APIs) is the sweet spot -- framework flexibility with API simplicity, $0.05-0.10/min, with a clear migration path to self-hosted as volume grows.",
    "layout_flow": "top-to-bottom-branching",
    "key_structures": [
      {
        "name": "Decision Node",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["How much control do you need?"]
      },
      {
        "name": "Path A: Managed",
        "role": "branching_path",
        "is_highlighted": false,
        "labels": ["PATH A: MANAGED", "Retell / Vapi / Bland", "$0.07-0.14/min"]
      },
      {
        "name": "Path B: Framework + APIs",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["PATH B: FRAMEWORK + APIs", "Pipecat / LiveKit", "$0.05-0.10/min", "SWEET SPOT"]
      },
      {
        "name": "Path C: Self-Hosted",
        "role": "branching_path",
        "is_highlighted": false,
        "labels": ["PATH C: SELF-HOSTED", "faster-whisper / Orpheus", "$0.01-0.02/min"]
      },
      {
        "name": "Path D: Hybrid",
        "role": "branching_path",
        "is_highlighted": false,
        "labels": ["PATH D: HYBRID", "Cloud LLM + on-device", "variable cost"]
      }
    ],
    "relationships": [
      {
        "from": "Decision Node",
        "to": "Path A: Managed",
        "type": "arrow",
        "label": "outsource everything"
      },
      {
        "from": "Decision Node",
        "to": "Path B: Framework + APIs",
        "type": "arrow",
        "label": "choose components"
      },
      {
        "from": "Decision Node",
        "to": "Path C: Self-Hosted",
        "type": "arrow",
        "label": "own everything"
      },
      {
        "from": "Decision Node",
        "to": "Path D: Hybrid",
        "type": "arrow",
        "label": "edge + cloud"
      },
      {
        "from": "Path B: Framework + APIs",
        "to": "Path C: Self-Hosted",
        "type": "dashed",
        "label": "migrate as volume grows"
      }
    ],
    "callout_boxes": [
      {
        "heading": "PATH B IS THE SWEET SPOT",
        "body_text": "Framework flexibility with API simplicity. Start with Pipecat or LiveKit + cloud APIs, migrate to self-hosted as volume grows.",
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
- [ ] Layout template identified (C)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
