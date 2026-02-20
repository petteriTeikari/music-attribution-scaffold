# fig-voice-16: Ultravox v0.7: The Speech-Native Breakthrough

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-16 |
| **Title** | Ultravox v0.7: The Speech-Native Breakthrough |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | A (Hero) |

## Purpose

Showcase Ultravox v0.7's breakthrough achievement as the first speech-to-speech model to beat text-mode LLMs on production benchmarks, with its architecture and comparison metrics. Answers: "Why is Ultravox v0.7 a breakthrough, how does its architecture work, and how does it compare to GPT Realtime and Gemini Live?"

## Key Message

Ultravox v0.7 achieved 97.7% on production benchmarks -- the first S2S model to beat text-mode LLMs -- by processing audio directly through a multimodal LLM without an intermediate STT step, outperforming GPT Realtime (86.7%) and Gemini Live (86.0%).

## Visual Concept

Hero layout (Template A) with large "97.7%" as the dominant centerpiece element in display typography. Below the hero number, three horizontal comparison bars: Ultravox (97.7%), GPT Realtime (86.7%), Gemini Live (86.0%). To the right or below, a simplified architecture diagram: Audio waveform -> Multimodal LLM (direct, no STT step) -> Response. The "no STT step" is visually emphasized with a crossed-out STT box or bypass arrow. Bottom callout delivers the benchmark significance.

```
+-------------------------------------------------------------------+
|  ULTRAVOX v0.7                                             [sq]   |
|  THE SPEECH-NATIVE BREAKTHROUGH                                    |
|                                                                    |
|                                                                    |
|                      97.7%                                         |
|                                                                    |
|                   Production Benchmark                              |
|                                                                    |
|  ─────────────────────────────────────────────────────────────     |
|                                                                    |
|  Ultravox v0.7    ████████████████████████████████████████  97.7%  |
|  GPT Realtime     ████████████████████████████████░░░░░░░░  86.7%  |
|  Gemini Live      ███████████████████████████████░░░░░░░░░  86.0%  |
|                                                                    |
|  ─────────────────────────────────────────────────────────────     |
|                                                                    |
|  ARCHITECTURE:                                                     |
|                                                                    |
|  Audio ──> [Multimodal LLM] ──> Response                          |
|            (no STT step)                                           |
|            audio processed                                         |
|            directly                                                |
|                                                                    |
|  "FIRST S2S MODEL TO BEAT TEXT-MODE LLMs ON                [line] |
|   PRODUCTION BENCHMARK"                                            |
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
    content: "ULTRAVOX v0.7"
    role: title

  - id: hero_zone
    bounds: [480, 140, 960, 200]
    content: "97.7%"
    role: hero_metric

  - id: comparison_zone
    bounds: [120, 380, 1680, 240]
    role: content_area

  - id: architecture_zone
    bounds: [120, 660, 1680, 200]
    role: content_area

  - id: callout_zone
    bounds: [40, 900, 1840, 140]
    content: "FIRST S2S MODEL TO BEAT TEXT-MODE LLMs"
    role: callout_box

anchors:
  - id: hero_number
    position: [580, 160]
    size: [760, 180]
    role: hero_metric
    label: "97.7%"

  - id: bar_ultravox
    position: [400, 400]
    size: [1200, 60]
    role: data_bar
    label: "Ultravox v0.7 -- 97.7%"

  - id: bar_gpt_realtime
    position: [400, 480]
    size: [1066, 60]
    role: data_bar
    label: "GPT Realtime -- 86.7%"

  - id: bar_gemini_live
    position: [400, 560]
    size: [1057, 60]
    role: data_bar
    label: "Gemini Live -- 86.0%"

  - id: arch_audio_input
    position: [200, 700]
    size: [200, 80]
    role: data_flow
    label: "Audio"

  - id: arch_multimodal_llm
    position: [560, 680]
    size: [400, 120]
    role: processing_stage
    label: "Multimodal LLM"

  - id: arch_no_stt
    position: [560, 810]
    size: [400, 40]
    role: accent_indicator
    label: "(no STT step)"

  - id: arch_response
    position: [1120, 700]
    size: [200, 80]
    role: data_flow
    label: "Response"

  - id: flow_audio_to_llm
    from: arch_audio_input
    to: arch_multimodal_llm
    type: arrow
    label: "audio directly"

  - id: flow_llm_to_response
    from: arch_multimodal_llm
    to: arch_response
    type: arrow
    label: "text/audio response"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Hero Metric: 97.7% | `hero_metric` | Ultravox v0.7 production benchmark score -- the centerpiece visual |
| Ultravox Bar | `data_bar` | Comparison bar: 97.7%, highest of three models |
| GPT Realtime Bar | `data_bar` | Comparison bar: 86.7%, OpenAI's speech model |
| Gemini Live Bar | `data_bar` | Comparison bar: 86.0%, Google's speech model |
| Audio Input | `data_flow` | Raw audio waveform entering the model |
| Multimodal LLM | `processing_stage` | Core Ultravox architecture: processes audio directly without STT |
| No STT Indicator | `accent_indicator` | Visual emphasis that audio bypasses traditional STT pipeline |
| Response Output | `data_flow` | Generated text/audio response |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Audio Input | Multimodal LLM | arrow | "audio directly (no STT)" |
| Multimodal LLM | Response Output | arrow | "text/audio response" |
| Ultravox Bar | GPT Realtime Bar | dashed | "11% gap" |
| Ultravox Bar | Gemini Live Bar | dashed | "11.7% gap" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "FIRST S2S MODEL TO BEAT TEXT-MODE LLMs ON PRODUCTION BENCHMARK" | Ultravox v0.7 processes audio directly through a multimodal LLM without an intermediate STT step. This architecture achieves 97.7% on production benchmarks, surpassing both GPT Realtime (86.7%) and Gemini Live (86.0%). | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "97.7%"
- Label 2: "Production Benchmark"
- Label 3: "Ultravox v0.7"
- Label 4: "GPT Realtime"
- Label 5: "Gemini Live"
- Label 6: "86.7%"
- Label 7: "86.0%"
- Label 8: "Audio"
- Label 9: "Multimodal LLM"
- Label 10: "(no STT step)"
- Label 11: "Response"
- Label 12: "audio directly"
- Label 13: "ARCHITECTURE"

### Caption (for embedding in documentation)

Hero figure showing Ultravox v0.7 achieving 97.7% on production benchmarks -- the first speech-to-speech model to beat text-mode LLMs -- compared against GPT Realtime (86.7%) and Gemini Live (86.0%), with simplified architecture diagram.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `hero_metric`, `data_bar`, `processing_stage`, `data_flow`, `accent_indicator` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The 97.7% benchmark score is from Ultravox v0.7 evaluation by Fixie.ai. Do NOT alter this value.
10. GPT Realtime scored 86.7% on the same benchmark. Do NOT alter this value.
11. Gemini Live scored 86.0% on the same benchmark. Do NOT alter this value.
12. "Production benchmark" refers to Fixie.ai's evaluation methodology -- it is not a universally standardized test. Present as stated without inflating generalizability.
13. The "no STT step" is the architectural key insight -- Ultravox processes audio tokens directly through the LLM, bypassing traditional speech-to-text transcription. This must be visually prominent.
14. Ultravox uses an encoder-decoder architecture (Whisper encoder + Llama decoder) -- it is NOT a decoder-only model. Do not misrepresent the architecture.
15. The hero "97.7%" must be the largest visual element on the canvas -- this is Template A (Hero) layout.
16. Comparison bars must be proportional to scores (97.7 vs 86.7 vs 86.0 -- approximately 11% relative difference visible).
17. Do NOT add models not listed (Claude, GPT-4o, etc.) -- only these three are compared in this specific figure.

## Alt Text

Hero figure showing Ultravox v0.7 achieving 97.7% on production benchmarks as the first speech-to-speech model to beat text-mode LLMs, compared against GPT Realtime (86.7%) and Gemini Live (86.0%), with architecture diagram showing direct audio processing without STT step.

## Image Embed

![Hero figure showing Ultravox v0.7 achieving 97.7% on production benchmarks as the first speech-to-speech model to beat text-mode LLMs, compared against GPT Realtime (86.7%) and Gemini Live (86.0%), with architecture diagram showing direct audio processing without STT step.](docs/figures/repo-figures/assets/fig-voice-16-ultravox-breakthrough.jpg)

*Hero figure showing Ultravox v0.7 achieving 97.7% on production benchmarks -- the first speech-to-speech model to beat text-mode LLMs -- compared against GPT Realtime (86.7%) and Gemini Live (86.0%), with simplified architecture diagram.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-16",
    "title": "Ultravox v0.7: The Speech-Native Breakthrough",
    "audience": "L3",
    "layout_template": "A"
  },
  "content_architecture": {
    "primary_message": "Ultravox v0.7 achieved 97.7% on production benchmarks -- the first S2S model to beat text-mode LLMs -- by processing audio directly through a multimodal LLM.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Hero Metric",
        "role": "hero_metric",
        "is_highlighted": true,
        "labels": ["97.7%", "Production Benchmark"]
      },
      {
        "name": "Ultravox v0.7",
        "role": "data_bar",
        "is_highlighted": true,
        "labels": ["Ultravox v0.7", "97.7%"]
      },
      {
        "name": "GPT Realtime",
        "role": "data_bar",
        "is_highlighted": false,
        "labels": ["GPT Realtime", "86.7%"]
      },
      {
        "name": "Gemini Live",
        "role": "data_bar",
        "is_highlighted": false,
        "labels": ["Gemini Live", "86.0%"]
      },
      {
        "name": "Multimodal LLM",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Multimodal LLM", "(no STT step)"]
      }
    ],
    "relationships": [
      {
        "from": "Audio Input",
        "to": "Multimodal LLM",
        "type": "arrow",
        "label": "audio directly (no STT)"
      },
      {
        "from": "Multimodal LLM",
        "to": "Response",
        "type": "arrow",
        "label": "text/audio response"
      },
      {
        "from": "Ultravox v0.7",
        "to": "GPT Realtime",
        "type": "dashed",
        "label": "11% gap"
      },
      {
        "from": "Ultravox v0.7",
        "to": "Gemini Live",
        "type": "dashed",
        "label": "11.7% gap"
      }
    ],
    "callout_boxes": [
      {
        "heading": "FIRST S2S MODEL TO BEAT TEXT-MODE LLMs ON PRODUCTION BENCHMARK",
        "body_text": "Ultravox processes audio directly through a multimodal LLM without intermediate STT, achieving 97.7%.",
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
- [ ] Layout template identified (A)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
