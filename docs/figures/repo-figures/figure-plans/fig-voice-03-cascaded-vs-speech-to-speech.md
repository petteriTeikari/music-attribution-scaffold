# fig-voice-03: Cascaded vs Speech-to-Speech Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-03 |
| **Title** | Cascaded vs Speech-to-Speech Architecture |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Compare the two fundamental voice agent architectures side by side: the modular cascaded pipeline (STT->LLM->TTS) versus the emerging speech-to-speech single-model approach, and introduce the tandem hybrid pattern. Answers: "Should we build modular or end-to-end, and is there a middle ground?"

## Key Message

Cascaded pipelines offer best-of-breed modularity while speech-to-speech models minimize latency -- the tandem pattern (Kame) combines both for optimal production tradeoffs.

## Visual Concept

Split-panel layout (Template D). Left panel shows the cascaded architecture as three distinct boxes connected by arrows (STT -> LLM -> TTS), with labels emphasizing modularity, swap-ability, and best-of-breed selection. Right panel shows a single monolithic block labeled "S2S Model" with audio-in and audio-out ports, emphasizing minimal latency and prosody preservation. Below the split, a horizontal callout bar shows the tandem/Kame pattern: a fast S2S front-end streaming preliminary responses while a cloud LLM generates the authoritative answer, with a reconciliation step. Coral accent squares at the boundary between left and right panels.

```
+----------------------------------+----------------------------------+
|  CASCADED                  [sq]  |  SPEECH-TO-SPEECH          [sq]  |
|  MODULAR PIPELINE                |  END-TO-END MODEL                |
|                                  |                                  |
|  +--------+                      |                                  |
|  |  STT   | --transcript-->      |     +---------------------+     |
|  +--------+                      |     |                     |     |
|        |                         |     |    S2S MODEL        |     |
|  +--------+                      |     |                     |     |
|  |  LLM   | --response-->       |     | audio-in  audio-out |     |
|  +--------+                      |     +---------------------+     |
|        |                         |                                  |
|  +--------+                      |  + Lowest latency                |
|  |  TTS   | --audio-->          |  + Preserves prosody              |
|  +--------+                      |  - Single vendor lock-in         |
|                                  |  - No intermediate text          |
|  + Best-of-breed per stage       |                                  |
|  + Swap any component            |                                  |
|  + Debuggable (text checkpoints) |                                  |
|  - Higher total latency          |                                  |
+----------------------------------+----------------------------------+
|  THE TANDEM PATTERN (KAME)                                          |
|  Fast S2S front-end + Cloud LLM back-end + Reconciliation    [line] |
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
    content: "CASCADED VS SPEECH-TO-SPEECH"
    role: title

  - id: left_panel
    bounds: [40, 140, 900, 700]
    content: "Cascaded Pipeline"
    role: content_area

  - id: right_panel
    bounds: [980, 140, 900, 700]
    content: "Speech-to-Speech Model"
    role: content_area

  - id: callout_zone
    bounds: [40, 880, 1840, 160]
    content: "THE TANDEM PATTERN (KAME)"
    role: callout_box

anchors:
  - id: stt_box
    position: [120, 220]
    size: [280, 120]
    role: processing_stage
    label: "STT"

  - id: llm_box
    position: [120, 400]
    size: [280, 120]
    role: processing_stage
    label: "LLM"

  - id: tts_box
    position: [120, 580]
    size: [280, 120]
    role: processing_stage
    label: "TTS"

  - id: cascaded_pros
    position: [480, 220]
    size: [400, 500]
    role: annotation
    label: "Modularity advantages"

  - id: s2s_block
    position: [1060, 280]
    size: [440, 340]
    role: processing_stage
    label: "S2S MODEL"

  - id: s2s_pros_cons
    position: [1060, 660]
    size: [440, 160]
    role: annotation
    label: "Latency vs lock-in"

  - id: tandem_bar
    position: [80, 900]
    size: [1760, 120]
    role: callout_box
    label: "THE TANDEM PATTERN (KAME)"

  - id: divider_line
    position: [960, 140]
    size: [2, 700]
    role: accent_line

  - id: flow_stt_to_llm
    from: stt_box
    to: llm_box
    type: arrow
    label: "transcript"

  - id: flow_llm_to_tts
    from: llm_box
    to: tts_box
    type: arrow
    label: "response text"

  - id: s2s_audio_in
    position: [1060, 400]
    size: [40, 40]
    role: input_port
    label: "audio in"

  - id: s2s_audio_out
    position: [1460, 400]
    size: [40, 40]
    role: output_port
    label: "audio out"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| STT Box | `processing_stage` | Speech-to-text stage in cascaded pipeline |
| LLM Box | `processing_stage` | Language model reasoning stage in cascaded pipeline |
| TTS Box | `processing_stage` | Text-to-speech synthesis stage in cascaded pipeline |
| Cascaded Advantages | `annotation` | Bullet list: best-of-breed, swappable, debuggable text checkpoints |
| S2S Model Block | `processing_stage` | Single end-to-end speech model (audio-in, audio-out) |
| S2S Pros/Cons | `annotation` | Lowest latency, prosody preserved vs vendor lock-in, no text |
| Tandem Pattern | `callout_box` | Hybrid: fast S2S front-end + cloud LLM back-end with reconciliation |
| Panel Divider | `accent_line` | Vertical coral line separating the two architectures |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| STT Box | LLM Box | arrow | "transcript" |
| LLM Box | TTS Box | arrow | "response text" |
| Audio Input | S2S Model | arrow | "raw audio" |
| S2S Model | Audio Output | arrow | "synthesized audio" |
| S2S Front-End | Cloud LLM | dashed | "tandem reconciliation" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "THE TANDEM PATTERN (KAME)" | Fast S2S front-end streams preliminary responses while a cloud LLM generates the authoritative answer. Reconciliation step merges both. Best of both worlds: low perceived latency with full reasoning depth. | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "CASCADED"
- Label 2: "MODULAR PIPELINE"
- Label 3: "STT"
- Label 4: "LLM"
- Label 5: "TTS"
- Label 6: "SPEECH-TO-SPEECH"
- Label 7: "END-TO-END MODEL"
- Label 8: "S2S MODEL"
- Label 9: "Best-of-breed per stage"
- Label 10: "Swap any component"
- Label 11: "Debuggable text checkpoints"
- Label 12: "Higher total latency"
- Label 13: "Lowest latency"
- Label 14: "Preserves prosody"
- Label 15: "Single vendor lock-in"
- Label 16: "No intermediate text"
- Label 17: "THE TANDEM PATTERN (KAME)"
- Label 18: "S2S front-end"
- Label 19: "Cloud LLM back-end"
- Label 20: "Reconciliation"

### Caption

Split-panel comparison of cascaded modular pipeline versus speech-to-speech end-to-end architecture, with the tandem pattern combining both approaches for optimal latency and reasoning depth.

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

8. The cascaded side must show THREE distinct boxes (STT, LLM, TTS) -- never merge them into one.
9. The S2S side must show ONE monolithic block -- never decompose it into sub-stages.
10. Pros/cons must appear as concise bullet text, not as separate boxes or cards.
11. The tandem pattern callout must span the full width below both panels.
12. No specific provider names (GPT-4o, Gemini, Moshi, etc.) in the main panels -- those belong in the tutorial text.
13. "Kame" is a reference name for the tandem pattern -- render it in parentheses only.

## Alt Text

Split-panel comparison of cascaded voice agent pipeline (STT, LLM, TTS modules) versus monolithic speech-to-speech model, with the tandem Kame pattern combining both for optimal latency and reasoning in music attribution workflows.

## Image Embed

![Split-panel comparison of cascaded voice agent pipeline (STT, LLM, TTS modules) versus monolithic speech-to-speech model, with the tandem Kame pattern combining both for optimal latency and reasoning in music attribution workflows.](docs/figures/repo-figures/assets/fig-voice-03-cascaded-vs-speech-to-speech.jpg)

*Split-panel comparison of cascaded modular pipeline versus speech-to-speech end-to-end architecture, with the tandem pattern combining both approaches for optimal latency and reasoning depth.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-03",
    "title": "Cascaded vs Speech-to-Speech Architecture",
    "audience": "L3",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Cascaded pipelines offer modularity while S2S models minimize latency -- the tandem pattern combines both.",
    "layout_flow": "side-by-side",
    "key_structures": [
      {
        "name": "Cascaded Pipeline",
        "role": "content_area",
        "is_highlighted": true,
        "labels": ["CASCADED", "MODULAR PIPELINE", "STT", "LLM", "TTS"]
      },
      {
        "name": "S2S Model",
        "role": "content_area",
        "is_highlighted": true,
        "labels": ["SPEECH-TO-SPEECH", "END-TO-END MODEL", "S2S MODEL"]
      },
      {
        "name": "Tandem Pattern",
        "role": "callout_box",
        "is_highlighted": true,
        "labels": ["THE TANDEM PATTERN (KAME)", "S2S front-end", "Cloud LLM back-end", "Reconciliation"]
      }
    ],
    "relationships": [
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
        "label": "response text"
      },
      {
        "from": "Audio Input",
        "to": "S2S Model",
        "type": "arrow",
        "label": "raw audio"
      },
      {
        "from": "S2S Model",
        "to": "Audio Output",
        "type": "arrow",
        "label": "synthesized audio"
      },
      {
        "from": "S2S Front-End",
        "to": "Cloud LLM",
        "type": "dashed",
        "label": "tandem reconciliation"
      }
    ],
    "callout_boxes": [
      {
        "heading": "THE TANDEM PATTERN (KAME)",
        "body_text": "Fast S2S front-end streams preliminary responses while cloud LLM generates the authoritative answer. Reconciliation merges both.",
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
