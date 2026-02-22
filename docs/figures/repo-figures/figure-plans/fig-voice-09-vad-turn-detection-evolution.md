# fig-voice-09: VAD and Turn Detection Evolution

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-09 |
| **Title** | VAD and Turn Detection Evolution |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Show the three-generation evolution of voice activity detection and turn detection, from naive silence thresholds through deep learning VAD to semantic endpointing. Answers: "How did turn detection evolve from dumb silence counters to intelligent semantic endpointing, and what are the concrete metrics at each stage?"

## Key Message

Turn detection evolved through three generations -- silence thresholds (WebRTC VAD, 50% TPR) to deep learning (Silero, 87.7% TPR, RTF 0.004) to semantic endpointing (Deepgram Flux 260ms, LiveKit <25ms, Pipecat Smart Turn) -- each generation reducing false interruptions and improving conversation quality for voice attribution agents.

## Visual Concept

Three-step vertical progression (Template E) with Roman numeral headers. Each generation occupies a horizontal band with key technology, metrics, and era. Evolution arrows connect generations top-to-bottom. Right-side callout warns about false interruptions destroying artist trust. Generation III is visually highlighted as the current state-of-the-art.

```
+-------------------------------------------+
|  TURN DETECTION EVOLUTION          [sq]   |
|                                           |
|  I   SILENCE THRESHOLD (2020-2023)        |
|      WebRTC VAD: GMM-based                |
|      50% TPR, many false cuts             |
|      Simple silence counter               |
|      ↓                                    |
|  II  DEEP LEARNING VAD (2023-2025)        |
|      Silero VAD: DNN                      |
|      87.7% TPR, RTF 0.004                |
|      Pre-trained, cross-lingual           |
|      ↓                                    |
|  III SEMANTIC ENDPOINTING (2025-2026)     |
|      Deepgram Flux: acoustic+semantic     |
|      ~260ms end-of-turn latency           |
|      LiveKit: <25ms CPU, 13 languages     |
|      Pipecat Smart Turn: open-source      |
|      30% fewer false interruptions        |
|                                           |
|  +-------------------------------------+ |
|  | "FALSE INTERRUPTIONS RUIN           | |
|  |  CONVERSATION FLOW -- cutting off   | |
|  |  an artist mid-sentence about       | |
|  |  credits destroys trust"            | |
|  +-------------------------------------+ |
+-------------------------------------------+
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
    content: "TURN DETECTION EVOLUTION"
    role: title

  - id: main_zone
    bounds: [80, 140, 1200, 800]
    role: content_area

  - id: callout_zone
    bounds: [1320, 600, 520, 280]
    role: callout_box

anchors:
  - id: gen_i_silence
    position: [160, 180]
    size: [1040, 200]
    role: processing_stage
    label: "I SILENCE THRESHOLD"

  - id: gen_ii_deep_learning
    position: [160, 420]
    size: [1040, 200]
    role: processing_stage
    label: "II DEEP LEARNING VAD"

  - id: gen_iii_semantic
    position: [160, 660]
    size: [1040, 220]
    role: processing_stage
    label: "III SEMANTIC ENDPOINTING"

  - id: problem_callout
    position: [1340, 620]
    size: [480, 260]
    role: problem_statement
    label: "FALSE INTERRUPTIONS"

  - id: flow_i_to_ii
    from: gen_i_silence
    to: gen_ii_deep_learning
    type: arrow
    label: "evolution: GMM to DNN"

  - id: flow_ii_to_iii
    from: gen_ii_deep_learning
    to: gen_iii_semantic
    type: arrow
    label: "evolution: acoustic to semantic"

  - id: problem_link
    from: problem_callout
    to: gen_iii_semantic
    type: dashed
    label: "solves"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Gen I: Silence Threshold | `processing_stage` | WebRTC VAD, GMM-based, simple silence counter, 50% TPR, era 2020-2023 |
| Gen II: Deep Learning VAD | `processing_stage` | Silero VAD, deep neural network, 87.7% TPR, RTF 0.004, pre-trained cross-lingual, era 2023-2025 |
| Gen III: Semantic Endpointing | `processing_stage` | Fused acoustic+semantic models: Deepgram Flux (~260ms), LiveKit (<25ms CPU, 13 langs), Pipecat Smart Turn (open-source), era 2025-2026 |
| False Interruption Problem | `problem_statement` | Why turn detection matters -- cutting off an artist mid-sentence about credits destroys trust in voice attribution agents |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Gen I: Silence Threshold | Gen II: Deep Learning VAD | arrow | "evolution: GMM to DNN" |
| Gen II: Deep Learning VAD | Gen III: Semantic Endpointing | arrow | "evolution: acoustic to semantic" |
| False Interruption Problem | Gen III: Semantic Endpointing | dashed | "solves" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "FALSE INTERRUPTIONS RUIN CONVERSATION FLOW" | Cutting off an artist mid-sentence about credits destroys trust. Each generation reduces false interruptions by 30%+. Semantic endpointing understands intent completion, not just silence gaps. | right-bottom |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I SILENCE THRESHOLD"
- Label 2: "II DEEP LEARNING VAD"
- Label 3: "III SEMANTIC ENDPOINTING"
- Label 4: "WebRTC VAD: GMM-based"
- Label 5: "50% TPR, many false cuts"
- Label 6: "Simple silence counter"
- Label 7: "Silero VAD: DNN"
- Label 8: "87.7% TPR, RTF 0.004"
- Label 9: "Pre-trained, cross-lingual"
- Label 10: "Deepgram Flux"
- Label 11: "~260ms end-of-turn"
- Label 12: "LiveKit: <25ms CPU"
- Label 13: "13 languages supported"
- Label 14: "Pipecat Smart Turn"
- Label 15: "30% fewer interruptions"
- Label 16: "2020-2023"
- Label 17: "2023-2025"
- Label 18: "2025-2026"

### Caption (for embedding in documentation)

Three-generation evolution of voice activity detection from silence thresholds (50% TPR) through deep learning VAD (87.7% TPR) to semantic endpointing (260ms, <25ms CPU), showing how each generation reduces false interruptions in voice agent conversations.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `problem_statement`, etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Roman numerals I, II, III must be used for generation headers, not Arabic numerals.
10. WebRTC VAD TPR is 50% -- this is from the Silero VAD benchmark comparison. Do not invent other metrics.
11. Silero VAD TPR is 87.7% with RTF 0.004 -- from official Silero benchmarks.
12. Deepgram Flux end-of-turn latency is ~260ms -- from Deepgram Nova-3 + Flux announcements.
13. LiveKit turn detection claims <25ms CPU overhead and 13 language support -- from LiveKit blog.
14. Pipecat Smart Turn is the open-source semantic turn detection from Daily/Pipecat -- do not confuse with proprietary systems.
15. The 30% reduction in false interruptions is the approximate improvement per generation, not a single study's exact figure.
16. Generation III should be visually highlighted as the current state-of-the-art (e.g., accent border or slightly larger panel).

## Alt Text

Three-generation evolution of voice activity detection and turn detection for voice agents: from silence thresholds (50% TPR) through deep learning VAD with Silero (87.7% TPR) to semantic endpointing achieving 260ms latency and 30% fewer false interruptions.

## Image Embed

![Three-generation evolution of voice activity detection and turn detection for voice agents: from silence thresholds (50% TPR) through deep learning VAD with Silero (87.7% TPR) to semantic endpointing achieving 260ms latency and 30% fewer false interruptions.](docs/figures/repo-figures/assets/fig-voice-09-vad-turn-detection-evolution.jpg)

*Three-generation evolution of voice activity detection from silence thresholds (50% TPR) through deep learning VAD (87.7% TPR) to semantic endpointing (260ms, <25ms CPU), showing how each generation reduces false interruptions in voice agent conversations.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-09",
    "title": "VAD and Turn Detection Evolution",
    "audience": "L3",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Turn detection evolved from silence thresholds to deep learning VAD to semantic endpointing, each generation reducing false interruptions by 30%+.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Gen I: Silence Threshold",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["I SILENCE THRESHOLD", "WebRTC VAD: GMM-based", "50% TPR", "2020-2023"]
      },
      {
        "name": "Gen II: Deep Learning VAD",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["II DEEP LEARNING VAD", "Silero VAD: DNN", "87.7% TPR, RTF 0.004", "2023-2025"]
      },
      {
        "name": "Gen III: Semantic Endpointing",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["III SEMANTIC ENDPOINTING", "Deepgram Flux", "~260ms", "LiveKit <25ms", "Pipecat Smart Turn", "2025-2026"]
      },
      {
        "name": "False Interruption Problem",
        "role": "problem_statement",
        "is_highlighted": true,
        "labels": ["FALSE INTERRUPTIONS RUIN CONVERSATION FLOW"]
      }
    ],
    "relationships": [
      {
        "from": "Gen I: Silence Threshold",
        "to": "Gen II: Deep Learning VAD",
        "type": "arrow",
        "label": "evolution: GMM to DNN"
      },
      {
        "from": "Gen II: Deep Learning VAD",
        "to": "Gen III: Semantic Endpointing",
        "type": "arrow",
        "label": "evolution: acoustic to semantic"
      },
      {
        "from": "False Interruption Problem",
        "to": "Gen III: Semantic Endpointing",
        "type": "dashed",
        "label": "solves"
      }
    ],
    "callout_boxes": [
      {
        "heading": "FALSE INTERRUPTIONS RUIN CONVERSATION FLOW",
        "body_text": "Cutting off an artist mid-sentence about credits destroys trust. Each generation reduces false interruptions by 30%+.",
        "position": "right-bottom"
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
