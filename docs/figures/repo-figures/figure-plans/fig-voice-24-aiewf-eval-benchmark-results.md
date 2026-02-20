# fig-voice-24: aiewf-eval: Production Voice Agent Benchmark

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-24 |
| **Title** | aiewf-eval: Production Voice Agent Benchmark |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Present the aiewf-eval benchmark results showing the intelligence-latency tradeoff between text-mode LLMs (perfect scores but high latency) and speech-to-speech models (lower scores but production-viable latency). Answers: "How do text-mode LLMs compare to speech-to-speech models on production voice agent tasks, and what is the intelligence-latency tradeoff?"

## Key Message

The intelligence-latency tradeoff is the central challenge: text-mode LLMs achieve 100% on aiewf-eval but are too slow for real-time voice, while production speech-to-speech models run 18-month-old model weights and score 86-98%, revealing the gap between what is possible and what is deployable.

## Visual Concept

Two-panel layout (Template B). Left panel: "TEXT-MODE LLMs" showing a bar/ranking chart with GPT-5.1 (100%), Claude Sonnet 4.5 (100%), Gemini 3 Flash (100%) -- all perfect scores but high latency. Right panel: "SPEECH-TO-SPEECH" showing Ultravox (97.7%), GPT Realtime (86.7%), Gemini Live (86.0%) -- lower but production-viable. Below the panels, a three-column evaluation dimensions row: tool_use_correct, instruction_following, kb_grounding. Bottom callout on the intelligence-latency tradeoff.

```
+-------------------------------------------------------------------+
|  AIEWF-EVAL                                                [sq]   |
|  PRODUCTION VOICE AGENT BENCHMARK                                  |
+-------------------------------+-----------------------------------+
|                               |                                   |
|  TEXT-MODE LLMs               |  SPEECH-TO-SPEECH                 |
|  (high accuracy, high latency)|  (production-viable latency)      |
|                               |                                   |
|  GPT-5.1          ████ 100%  |  Ultravox       ████████ 97.7%   |
|  Claude Sonnet 4.5 ████ 100%  |  GPT Realtime   ██████░░ 86.7%   |
|  Gemini 3 Flash   ████ 100%  |  Gemini Live    ██████░░ 86.0%   |
|                               |                                   |
|  ■ Perfect scores             |  ■ 86-98% range                   |
|  ■ 500ms+ response time       |  ■ <300ms response time           |
|  ■ Text pipeline overhead     |  ■ Direct audio processing        |
|  ■ NOT viable for real-time   |  ■ Production-deployable          |
|                               |                                   |
+-------------------------------+-----------------------------------+
|  EVALUATION DIMENSIONS (30-turn conversations, Claude as judge)    |
|  ┌──────────────┬──────────────────┬────────────────────┐         |
|  │ tool_use_    │ instruction_     │ kb_grounding       │         |
|  │ correct      │ following        │ (knowledge base)   │         |
|  └──────────────┴──────────────────┴────────────────────┘         |
+-------------------------------------------------------------------+
|  "THE INTELLIGENCE-LATENCY TRADEOFF: 100% models are too slow;    |
|   production runs 18-month-old models"               [accent line] |
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
    content: "AIEWF-EVAL"
    role: title

  - id: left_panel
    bounds: [40, 140, 900, 520]
    content: "TEXT-MODE LLMs"
    role: content_area

  - id: right_panel
    bounds: [980, 140, 900, 520]
    content: "SPEECH-TO-SPEECH"
    role: content_area

  - id: divider
    bounds: [940, 140, 2, 520]
    role: accent_line_v

  - id: dimensions_zone
    bounds: [40, 700, 1840, 120]
    content: "EVALUATION DIMENSIONS"
    role: content_area

  - id: callout_zone
    bounds: [40, 860, 1840, 120]
    content: "THE INTELLIGENCE-LATENCY TRADEOFF"
    role: callout_box

anchors:
  - id: text_gpt51
    position: [80, 200]
    size: [820, 80]
    role: data_row
    label: "GPT-5.1: 100%"

  - id: text_claude
    position: [80, 300]
    size: [820, 80]
    role: data_row
    label: "Claude Sonnet 4.5: 100%"

  - id: text_gemini
    position: [80, 400]
    size: [820, 80]
    role: data_row
    label: "Gemini 3 Flash: 100%"

  - id: s2s_ultravox
    position: [1020, 200]
    size: [860, 80]
    role: data_row
    label: "Ultravox: 97.7%"

  - id: s2s_gpt_realtime
    position: [1020, 300]
    size: [860, 80]
    role: data_row
    label: "GPT Realtime: 86.7%"

  - id: s2s_gemini_live
    position: [1020, 400]
    size: [860, 80]
    role: data_row
    label: "Gemini Live: 86.0%"

  - id: dim_tool_use
    position: [80, 720]
    size: [540, 80]
    role: processing_stage
    label: "tool_use_correct"

  - id: dim_instruction
    position: [660, 720]
    size: [540, 80]
    role: processing_stage
    label: "instruction_following"

  - id: dim_kb
    position: [1240, 720]
    size: [540, 80]
    role: processing_stage
    label: "kb_grounding"

  - id: text_to_s2s_gap
    from: left_panel
    to: right_panel
    type: dashed
    label: "intelligence-latency gap"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Text-Mode LLMs Panel | `branching_path` | GPT-5.1, Claude Sonnet 4.5, Gemini 3 Flash -- all 100% accuracy but high latency, not viable for real-time |
| Speech-to-Speech Panel | `selected_option` | Ultravox (97.7%), GPT Realtime (86.7%), Gemini Live (86.0%) -- production-viable latency |
| GPT-5.1 Bar | `data_row` | 100% score, text-mode, high latency |
| Claude Sonnet 4.5 Bar | `data_row` | 100% score, text-mode, high latency |
| Gemini 3 Flash Bar | `data_row` | 100% score, text-mode, high latency |
| Ultravox Bar | `data_row` | 97.7% score, speech-to-speech, production latency |
| GPT Realtime Bar | `data_row` | 86.7% score, speech-to-speech, production latency |
| Gemini Live Bar | `data_row` | 86.0% score, speech-to-speech, production latency |
| tool_use_correct Dimension | `processing_stage` | Evaluates correct tool invocation in voice conversations |
| instruction_following Dimension | `processing_stage` | Evaluates adherence to conversation instructions |
| kb_grounding Dimension | `processing_stage` | Evaluates knowledge base grounding accuracy |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Text-Mode LLMs Panel | Speech-to-Speech Panel | dashed | "intelligence-latency gap" |
| Evaluation Dimensions | Both Panels | arrow | "30-turn conversations scored" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "THE INTELLIGENCE-LATENCY TRADEOFF" | 100% models are too slow for real-time voice interaction. Production voice agents run speech-to-speech models with 18-month-old weights, scoring 86-98%. The gap between what is possible (text LLMs) and what is deployable (S2S models) defines the frontier. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "TEXT-MODE LLMs"
- Label 2: "SPEECH-TO-SPEECH"
- Label 3: "GPT-5.1"
- Label 4: "Claude Sonnet 4.5"
- Label 5: "Gemini 3 Flash"
- Label 6: "Ultravox"
- Label 7: "GPT Realtime"
- Label 8: "Gemini Live"
- Label 9: "100%"
- Label 10: "97.7%"
- Label 11: "86.7%"
- Label 12: "86.0%"
- Label 13: "tool_use_correct"
- Label 14: "instruction_following"
- Label 15: "kb_grounding"
- Label 16: "30-turn conversations"
- Label 17: "Claude as judge"
- Label 18: "high latency"
- Label 19: "production-viable"

### Caption (for embedding in documentation)

Two-panel comparison of aiewf-eval benchmark results showing text-mode LLMs (GPT-5.1, Claude Sonnet 4.5, Gemini 3 Flash at 100%) versus speech-to-speech models (Ultravox 97.7%, GPT Realtime 86.7%, Gemini Live 86.0%), evaluated on tool use, instruction following, and knowledge grounding in 30-turn conversations.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `data_row`, `processing_stage`, `branching_path` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. aiewf-eval scores are from the AI Engineering World's Fair evaluation benchmark. The specific scores cited (GPT-5.1 100%, Claude Sonnet 4.5 100%, Gemini 3 Flash 100%, Ultravox 97.7%, GPT Realtime 86.7%, Gemini Live 86.0%) are from the benchmark results. Do NOT alter these values.
10. The benchmark uses 30-turn conversations with Claude as the judge model. These are factual details of the evaluation methodology.
11. The three evaluation dimensions are tool_use_correct, instruction_following, and kb_grounding. These are the actual metric names used by aiewf-eval.
12. Text-mode LLMs achieve 100% because they process text transcripts with full reasoning capability. The latency cost of STT -> LLM -> TTS makes them impractical for real-time voice.
13. Speech-to-speech models score lower because they use older model weights optimized for audio-native processing. The "18-month-old models" observation reflects the gap between latest text LLM capabilities and what has been distilled into S2S models.
14. Ultravox at 97.7% is the highest-scoring S2S model. It uses a hybrid architecture (text LLM with audio adapter). Do NOT describe it as pure end-to-end S2S.
15. Do NOT claim these scores are static -- benchmarks evolve and model capabilities improve. Present as a snapshot.
16. The intelligence-latency tradeoff is the central message -- both panels are valid, neither is "wrong."

## Alt Text

Two-panel aiewf-eval benchmark comparison of text-mode LLMs scoring 100% versus speech-to-speech models at 86-98%, illustrating the intelligence-latency tradeoff in voice agent evaluation across tool use, instruction following, and knowledge grounding dimensions.

## Image Embed

![Two-panel aiewf-eval benchmark comparison of text-mode LLMs scoring 100% versus speech-to-speech models at 86-98%, illustrating the intelligence-latency tradeoff in voice agent evaluation across tool use, instruction following, and knowledge grounding dimensions.](docs/figures/repo-figures/assets/fig-voice-24-aiewf-eval-benchmark-results.jpg)

*Two-panel comparison of aiewf-eval benchmark results showing text-mode LLMs (GPT-5.1, Claude Sonnet 4.5, Gemini 3 Flash at 100%) versus speech-to-speech models (Ultravox 97.7%, GPT Realtime 86.7%, Gemini Live 86.0%), evaluated on tool use, instruction following, and knowledge grounding in 30-turn conversations.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-24",
    "title": "aiewf-eval: Production Voice Agent Benchmark",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "The intelligence-latency tradeoff: text LLMs score 100% but are too slow, while production S2S models score 86-98% with viable latency.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Text-Mode LLMs Panel",
        "role": "branching_path",
        "is_highlighted": false,
        "labels": ["TEXT-MODE LLMs", "GPT-5.1: 100%", "Claude Sonnet 4.5: 100%", "Gemini 3 Flash: 100%"]
      },
      {
        "name": "Speech-to-Speech Panel",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["SPEECH-TO-SPEECH", "Ultravox: 97.7%", "GPT Realtime: 86.7%", "Gemini Live: 86.0%"]
      },
      {
        "name": "tool_use_correct",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["tool_use_correct"]
      },
      {
        "name": "instruction_following",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["instruction_following"]
      },
      {
        "name": "kb_grounding",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["kb_grounding"]
      }
    ],
    "relationships": [
      {
        "from": "Text-Mode LLMs Panel",
        "to": "Speech-to-Speech Panel",
        "type": "dashed",
        "label": "intelligence-latency gap"
      }
    ],
    "callout_boxes": [
      {
        "heading": "THE INTELLIGENCE-LATENCY TRADEOFF",
        "body_text": "100% models are too slow; production runs 18-month-old models. The gap between possible and deployable defines the frontier.",
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
- [ ] Layout template identified (B)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
