# fig-voice-23: The Fragmented Leaderboard Landscape

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-23 |
| **Title** | The Fragmented Leaderboard Landscape |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Show the fragmentation of voice agent evaluation across separate, disconnected leaderboards for STT, TTS, end-to-end systems, and voice cloning. Answers: "Why is there no unified voice agent leaderboard, and where do the current leaderboards fall short?"

## Key Message

No single leaderboard captures the full voice agent experience -- evaluation is fragmented across STT, TTS, end-to-end, and voice cloning leaderboards, each measuring different dimensions, with no unified benchmark that tests the complete pipeline from speech input to speech output with tool use.

## Visual Concept

Four-panel grid (Template B) with a central gap statement. Panel I (top-left): STT Leaderboard -- HuggingFace Open ASR, top models, WER metrics. Panel II (top-right): TTS Leaderboard -- TTS Arena, Artificial Analysis, MOS metrics. Panel III (bottom-left): End-to-End -- aiewf-eval, tool use + conversation. Panel IV (bottom-right): Voice Cloning -- ClonEval, speaker similarity metrics. Center: bold text "NO UNIFIED VOICE AGENT LEADERBOARD EXISTS" spanning all four quadrants.

```
+-------------------------------------------------------------------+
|  THE FRAGMENTED LEADERBOARD LANDSCAPE                      [sq]   |
|                                                                    |
+-------------------------------+-----------------------------------+
|                               |                                   |
|  I   STT LEADERBOARD          |  II  TTS LEADERBOARD              |
|      HuggingFace Open ASR     |      TTS Arena (Hugging Face)     |
|                               |      Artificial Analysis           |
|  Measures: WER, CER           |                                   |
|  Top: Whisper v3 turbo,       |  Measures: MOS, naturalness       |
|       Universal-2, Canary     |  Top: ElevenLabs, Cartesia,       |
|  Missing: latency, streaming  |       PlayHT                      |
|                               |  Missing: expressiveness,         |
|                               |           prosody control          |
+-------------------------------+-----------------------------------+
|                                                                    |
|       NO UNIFIED VOICE AGENT LEADERBOARD EXISTS                    |
|                                                                    |
+-------------------------------+-----------------------------------+
|                               |                                   |
|  III END-TO-END               |  IV  VOICE CLONING                |
|      aiewf-eval               |      ClonEval                     |
|      VoiceAgentBench          |                                   |
|                               |  Measures: speaker similarity,    |
|  Measures: tool_use, kb_      |            MOS, intelligibility   |
|    grounding, instruction     |  Top: ElevenLabs, PlayHT,         |
|  Top: Ultravox, GPT Realtime  |       F5-TTS                      |
|  Missing: latency, cost,      |  Missing: emotional range,        |
|           real-time perf      |           cross-lingual quality   |
+-------------------------------+-----------------------------------+
|  "NO SINGLE LEADERBOARD CAPTURES THE FULL VOICE AGENT             |
|   EXPERIENCE"                                        [accent line] |
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
    content: "THE FRAGMENTED LEADERBOARD LANDSCAPE"
    role: title

  - id: grid_zone
    bounds: [40, 140, 1840, 700]
    role: content_area

  - id: center_statement
    bounds: [400, 460, 1120, 80]
    content: "NO UNIFIED VOICE AGENT LEADERBOARD EXISTS"
    role: problem_statement

  - id: callout_zone
    bounds: [40, 880, 1840, 100]
    content: "NO SINGLE LEADERBOARD"
    role: callout_box

anchors:
  - id: panel_i_stt
    position: [60, 160]
    size: [880, 280]
    role: processing_stage
    label: "I STT LEADERBOARD"

  - id: panel_ii_tts
    position: [980, 160]
    size: [880, 280]
    role: processing_stage
    label: "II TTS LEADERBOARD"

  - id: panel_iii_e2e
    position: [60, 560]
    size: [880, 280]
    role: processing_stage
    label: "III END-TO-END"

  - id: panel_iv_cloning
    position: [980, 560]
    size: [880, 280]
    role: processing_stage
    label: "IV VOICE CLONING"

  - id: center_gap
    position: [400, 470]
    size: [1120, 60]
    role: problem_statement
    label: "NO UNIFIED LEADERBOARD"

  - id: gap_to_stt
    from: center_gap
    to: panel_i_stt
    type: dashed
    label: "measures WER only"

  - id: gap_to_tts
    from: center_gap
    to: panel_ii_tts
    type: dashed
    label: "measures MOS only"

  - id: gap_to_e2e
    from: center_gap
    to: panel_iii_e2e
    type: dashed
    label: "closest but incomplete"

  - id: gap_to_cloning
    from: center_gap
    to: panel_iv_cloning
    type: dashed
    label: "niche dimension"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Panel I: STT Leaderboard | `processing_stage` | HuggingFace Open ASR -- WER/CER metrics, Whisper v3 turbo, Universal-2, Canary; missing latency and streaming evaluation |
| Panel II: TTS Leaderboard | `processing_stage` | TTS Arena, Artificial Analysis -- MOS/naturalness metrics, ElevenLabs, Cartesia, PlayHT; missing expressiveness and prosody control |
| Panel III: End-to-End | `processing_stage` | aiewf-eval, VoiceAgentBench -- tool use, knowledge grounding, instruction following; Ultravox, GPT Realtime; missing latency and cost evaluation |
| Panel IV: Voice Cloning | `processing_stage` | ClonEval -- speaker similarity, MOS, intelligibility; ElevenLabs, PlayHT, F5-TTS; missing emotional range and cross-lingual quality |
| Center Statement | `problem_statement` | "NO UNIFIED VOICE AGENT LEADERBOARD EXISTS" -- the gap spanning all four quadrants |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Center Gap | Panel I: STT | dashed | "measures WER only" |
| Center Gap | Panel II: TTS | dashed | "measures MOS only" |
| Center Gap | Panel III: End-to-End | dashed | "closest but incomplete" |
| Center Gap | Panel IV: Voice Cloning | dashed | "niche dimension" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "NO SINGLE LEADERBOARD CAPTURES THE FULL VOICE AGENT EXPERIENCE" | Each leaderboard measures one slice of the voice agent stack. A team choosing components must consult four separate leaderboards, none of which test the integrated experience of speech-in -> reasoning -> tool use -> speech-out at production latencies. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I STT LEADERBOARD"
- Label 2: "II TTS LEADERBOARD"
- Label 3: "III END-TO-END"
- Label 4: "IV VOICE CLONING"
- Label 5: "HuggingFace Open ASR"
- Label 6: "TTS Arena"
- Label 7: "Artificial Analysis"
- Label 8: "aiewf-eval"
- Label 9: "VoiceAgentBench"
- Label 10: "ClonEval"
- Label 11: "Measures: WER, CER"
- Label 12: "Measures: MOS, naturalness"
- Label 13: "Measures: tool_use"
- Label 14: "Measures: speaker similarity"
- Label 15: "Missing: latency"
- Label 16: "Missing: expressiveness"
- Label 17: "Missing: cost"
- Label 18: "Missing: emotional range"
- Label 19: "NO UNIFIED LEADERBOARD"

### Caption (for embedding in documentation)

Four-panel diagram showing the fragmented voice agent leaderboard landscape across STT, TTS, end-to-end, and voice cloning evaluation, with no unified benchmark capturing the full voice agent experience.

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

9. HuggingFace Open ASR Leaderboard is a real public leaderboard at huggingface.co/spaces. Do NOT invent URL or claim it measures anything beyond ASR accuracy.
10. TTS Arena is hosted on HuggingFace Spaces for human preference evaluation. Artificial Analysis tracks TTS provider quality metrics. Both are real.
11. aiewf-eval (AI Engineering World's Fair evaluation) uses 30-turn conversations with Claude as judge. VoiceAgentBench tests agentic voice capabilities. Both are real benchmarks.
12. ClonEval evaluates voice cloning quality on speaker similarity, MOS, and intelligibility. It is a real evaluation framework.
13. The "NO UNIFIED LEADERBOARD" statement must be visually prominent in the center -- it is the key insight of the figure.
14. The "Missing" notes for each leaderboard are genuine gaps: STT leaderboards do not test streaming latency, TTS leaderboards do not evaluate prosody control, etc.
15. Roman numerals I-IV must be used for panel headers.
16. Do NOT present any of these leaderboards as comprehensive -- the entire point is that each measures only one dimension.
17. F5-TTS is a real open-source TTS model. Do NOT confuse with other naming conventions.

## Alt Text

Four-panel diagram showing fragmented voice agent evaluation landscape across STT, TTS, end-to-end, and voice cloning leaderboards, revealing no unified benchmark exists for full pipeline assessment from speech input to speech output with tool use.

## Image Embed

![Four-panel diagram showing fragmented voice agent evaluation landscape across STT, TTS, end-to-end, and voice cloning leaderboards, revealing no unified benchmark exists for full pipeline assessment from speech input to speech output with tool use.](docs/figures/repo-figures/assets/fig-voice-23-leaderboard-landscape-fragmentation.jpg)

*Four-panel diagram showing the fragmented voice agent leaderboard landscape across STT, TTS, end-to-end, and voice cloning evaluation, with no unified benchmark capturing the full voice agent experience.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-23",
    "title": "The Fragmented Leaderboard Landscape",
    "audience": "L2",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "No single leaderboard captures the full voice agent experience -- evaluation is fragmented across STT, TTS, end-to-end, and voice cloning benchmarks.",
    "layout_flow": "grid-2x2",
    "key_structures": [
      {
        "name": "Panel I: STT Leaderboard",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["I STT LEADERBOARD", "HuggingFace Open ASR", "WER, CER"]
      },
      {
        "name": "Panel II: TTS Leaderboard",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["II TTS LEADERBOARD", "TTS Arena", "Artificial Analysis", "MOS"]
      },
      {
        "name": "Panel III: End-to-End",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["III END-TO-END", "aiewf-eval", "VoiceAgentBench", "tool_use"]
      },
      {
        "name": "Panel IV: Voice Cloning",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["IV VOICE CLONING", "ClonEval", "speaker similarity"]
      },
      {
        "name": "Center Gap Statement",
        "role": "problem_statement",
        "is_highlighted": true,
        "labels": ["NO UNIFIED VOICE AGENT LEADERBOARD EXISTS"]
      }
    ],
    "relationships": [
      {
        "from": "Center Gap",
        "to": "Panel I: STT",
        "type": "dashed",
        "label": "measures WER only"
      },
      {
        "from": "Center Gap",
        "to": "Panel II: TTS",
        "type": "dashed",
        "label": "measures MOS only"
      },
      {
        "from": "Center Gap",
        "to": "Panel III: End-to-End",
        "type": "dashed",
        "label": "closest but incomplete"
      },
      {
        "from": "Center Gap",
        "to": "Panel IV: Voice Cloning",
        "type": "dashed",
        "label": "niche dimension"
      }
    ],
    "callout_boxes": [
      {
        "heading": "NO SINGLE LEADERBOARD CAPTURES THE FULL VOICE AGENT EXPERIENCE",
        "body_text": "Each leaderboard measures one slice. Teams must consult four separate leaderboards, none of which test the integrated speech-in -> reasoning -> speech-out experience.",
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
- [ ] Audience level correct (L2)
- [ ] Layout template identified (B)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
