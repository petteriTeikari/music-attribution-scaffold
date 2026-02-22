# fig-voice-22: Voice Agent Evaluation: 2024 to 2026

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-22 |
| **Title** | Voice Agent Evaluation: 2024 to 2026 |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

Show the rapid evolution of voice agent evaluation from simple component metrics (WER, MOS) to multi-dimensional, agentic, production-oriented benchmarks. Answers: "How has voice agent evaluation evolved from 2024 to 2026, and what paradigm shifts occurred?"

## Key Message

Voice agent evaluation evolved from WER-only single-utterance metrics to multi-dimensional production benchmarks in just two years, with each phase adding critical dimensions: audio-native evaluation, agentic task completion, LLM-as-judge paradigms, and safety/emotion assessment.

## Visual Concept

Horizontal timeline (Template E adapted) flowing left to right across five phases. Phase I (2024): Component metrics -- WER, MOS, single utterance, English only. Phase II (Early 2025): Multi-dimensional -- Full-Duplex-Bench, VocalBench, audio-native. Phase III (Mid 2025): Agentic -- VoiceAgentBench, aiewf-eval, production-oriented. Phase IV (Late 2025): LLM-as-Judge -- SpeechLLM-as-Judges, TRACE, automated assessment. Phase V (Early 2026): Safety + Emotion -- LALM-as-Judge, HumDial, Audio MultiChallenge. Each phase shows representative benchmarks and what they added.

```
+-------------------------------------------------------------------+
|  VOICE AGENT EVALUATION                                    [sq]   |
|  2024 → 2026                                                      |
+-------------------------------------------------------------------+
|                                                                    |
|  I           II            III           IV            V           |
|  2024        EARLY 2025    MID 2025      LATE 2025     EARLY 2026 |
|                                                                    |
|  COMPONENT   MULTI-DIM     AGENTIC       LLM-AS-      SAFETY +   |
|  METRICS     AUDIO-NATIVE  PRODUCTION    JUDGE         EMOTION    |
|                                                                    |
|  ■ WER       ■ Full-Duplex ■ VoiceAgent  ■ SpeechLLM  ■ LALM-as- |
|  ■ MOS         -Bench        Bench         -as-Judges    Judge    |
|  ■ Single    ■ VocalBench  ■ aiewf-eval  ■ TRACE      ■ HumDial  |
|    utterance ■ Audio-native■ Tool use    ■ Automated   ■ Audio    |
|  ■ English     scoring       scoring       grading      Multi-   |
|    only      ■ Multilingual■ 30-turn    ■ Reference-    Challenge |
|                               convos       free        ■ Emotion  |
|                                                          safety   |
|  ──────→──────→──────→──────→──────→                              |
|                                                                    |
+-------------------------------------------------------------------+
|  "FROM WER-ONLY TO MULTI-DIMENSIONAL — evaluation caught up       |
|   with production reality"                           [accent line] |
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
    content: "VOICE AGENT EVALUATION 2024-2026"
    role: title

  - id: timeline_zone
    bounds: [40, 140, 1840, 760]
    role: content_area

  - id: callout_zone
    bounds: [40, 940, 1840, 100]
    content: "FROM WER-ONLY TO MULTI-DIMENSIONAL"
    role: callout_box

anchors:
  - id: phase_i_component
    position: [60, 180]
    size: [320, 700]
    role: processing_stage
    label: "I COMPONENT METRICS"

  - id: phase_ii_multidim
    position: [420, 180]
    size: [320, 700]
    role: processing_stage
    label: "II MULTI-DIMENSIONAL"

  - id: phase_iii_agentic
    position: [780, 180]
    size: [320, 700]
    role: processing_stage
    label: "III AGENTIC"

  - id: phase_iv_llmjudge
    position: [1140, 180]
    size: [320, 700]
    role: processing_stage
    label: "IV LLM-AS-JUDGE"

  - id: phase_v_safety
    position: [1500, 180]
    size: [360, 700]
    role: processing_stage
    label: "V SAFETY + EMOTION"

  - id: timeline_arrow
    position: [60, 860]
    size: [1800, 20]
    role: data_flow
    label: "Timeline progression"

  - id: flow_i_to_ii
    from: phase_i_component
    to: phase_ii_multidim
    type: arrow
    label: "adds audio-native"

  - id: flow_ii_to_iii
    from: phase_ii_multidim
    to: phase_iii_agentic
    type: arrow
    label: "adds tool use"

  - id: flow_iii_to_iv
    from: phase_iii_agentic
    to: phase_iv_llmjudge
    type: arrow
    label: "adds automated judging"

  - id: flow_iv_to_v
    from: phase_iv_llmjudge
    to: phase_v_safety
    type: arrow
    label: "adds safety + emotion"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Phase I: Component Metrics (2024) | `processing_stage` | WER, MOS, single utterance, English only -- the baseline era |
| Phase II: Multi-Dimensional (Early 2025) | `processing_stage` | Full-Duplex-Bench, VocalBench -- audio-native, multilingual scoring |
| Phase III: Agentic (Mid 2025) | `processing_stage` | VoiceAgentBench, aiewf-eval -- tool use, 30-turn conversations, production-oriented |
| Phase IV: LLM-as-Judge (Late 2025) | `processing_stage` | SpeechLLM-as-Judges, TRACE -- automated grading, reference-free evaluation |
| Phase V: Safety + Emotion (Early 2026) | `processing_stage` | LALM-as-Judge, HumDial, Audio MultiChallenge -- emotion recognition, safety testing |
| Timeline Arrow | `data_flow` | Horizontal progression line connecting all five phases |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Phase I | Phase II | arrow | "adds audio-native scoring" |
| Phase II | Phase III | arrow | "adds tool use + multi-turn" |
| Phase III | Phase IV | arrow | "adds automated LLM judging" |
| Phase IV | Phase V | arrow | "adds safety + emotion" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "FROM WER-ONLY TO MULTI-DIMENSIONAL" | Evaluation caught up with production reality. In 2024, WER was the only metric. By early 2026, benchmarks test tool use, conversation flow, knowledge grounding, safety, and emotional intelligence -- all evaluated by LLM judges. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I COMPONENT METRICS"
- Label 2: "II MULTI-DIMENSIONAL"
- Label 3: "III AGENTIC"
- Label 4: "IV LLM-AS-JUDGE"
- Label 5: "V SAFETY + EMOTION"
- Label 6: "2024"
- Label 7: "Early 2025"
- Label 8: "Mid 2025"
- Label 9: "Late 2025"
- Label 10: "Early 2026"
- Label 11: "WER"
- Label 12: "MOS"
- Label 13: "Full-Duplex-Bench"
- Label 14: "VocalBench"
- Label 15: "VoiceAgentBench"
- Label 16: "aiewf-eval"
- Label 17: "SpeechLLM-as-Judges"
- Label 18: "TRACE"
- Label 19: "LALM-as-Judge"
- Label 20: "HumDial"
- Label 21: "Audio MultiChallenge"

### Caption (for embedding in documentation)

Timeline showing voice agent evaluation evolution from WER-only component metrics (2024) through multi-dimensional audio-native benchmarks, agentic production evaluations, LLM-as-judge paradigms, to safety and emotion assessment (early 2026).

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `data_flow`, etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. WER (Word Error Rate) and MOS (Mean Opinion Score) are the traditional speech metrics. They are still used but no longer sufficient alone.
10. Full-Duplex-Bench is a benchmark for evaluating full-duplex conversation capabilities. VocalBench evaluates vocal instruction following.
11. VoiceAgentBench tests agentic capabilities (tool use, knowledge grounding). aiewf-eval is a production voice agent benchmark using 30-turn conversations with Claude as judge.
12. SpeechLLM-as-Judges uses speech LLMs to evaluate other speech LLMs. TRACE is a reference-free automated evaluation framework.
13. LALM-as-Judge evaluates large audio-language models. HumDial focuses on human-like dialogue quality. Audio MultiChallenge tests multi-modal audio understanding.
14. The timeline progression must be clearly left-to-right with visible dates.
15. Roman numerals I-V must be used for phase headers.
16. Each phase ADDS to previous capabilities -- later phases do not replace earlier metrics, they supplement them.
17. Do NOT imply these are the only benchmarks in each phase -- they are representative examples.

## Alt Text

Timeline showing voice agent evaluation benchmark evolution across five phases from 2024 to 2026: component metrics (WER, MOS), multi-dimensional audio-native scoring (Full-Duplex-Bench, VocalBench), agentic production benchmarks (VoiceAgentBench), LLM-as-judge paradigms, and safety + emotion assessment.

## Image Embed

![Timeline showing voice agent evaluation benchmark evolution across five phases from 2024 to 2026: component metrics (WER, MOS), multi-dimensional audio-native scoring (Full-Duplex-Bench, VocalBench), agentic production benchmarks (VoiceAgentBench), LLM-as-judge paradigms, and safety + emotion assessment.](docs/figures/repo-figures/assets/fig-voice-22-evaluation-evolution-timeline.jpg)

*Timeline showing voice agent evaluation evolution from WER-only component metrics (2024) through multi-dimensional audio-native benchmarks, agentic production evaluations, LLM-as-judge paradigms, to safety and emotion assessment (early 2026).*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-22",
    "title": "Voice Agent Evaluation: 2024 to 2026",
    "audience": "L2",
    "layout_template": "E"
  },
  "content_architecture": {
    "primary_message": "Voice agent evaluation evolved from WER-only to multi-dimensional production benchmarks in two years, with each phase adding audio-native, agentic, LLM-judge, and safety dimensions.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Phase I: Component Metrics",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["I COMPONENT METRICS", "2024", "WER", "MOS", "single utterance"]
      },
      {
        "name": "Phase II: Multi-Dimensional",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["II MULTI-DIMENSIONAL", "Early 2025", "Full-Duplex-Bench", "VocalBench"]
      },
      {
        "name": "Phase III: Agentic",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["III AGENTIC", "Mid 2025", "VoiceAgentBench", "aiewf-eval"]
      },
      {
        "name": "Phase IV: LLM-as-Judge",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["IV LLM-AS-JUDGE", "Late 2025", "SpeechLLM-as-Judges", "TRACE"]
      },
      {
        "name": "Phase V: Safety + Emotion",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["V SAFETY + EMOTION", "Early 2026", "LALM-as-Judge", "HumDial", "Audio MultiChallenge"]
      }
    ],
    "relationships": [
      {
        "from": "Phase I",
        "to": "Phase II",
        "type": "arrow",
        "label": "adds audio-native scoring"
      },
      {
        "from": "Phase II",
        "to": "Phase III",
        "type": "arrow",
        "label": "adds tool use + multi-turn"
      },
      {
        "from": "Phase III",
        "to": "Phase IV",
        "type": "arrow",
        "label": "adds automated LLM judging"
      },
      {
        "from": "Phase IV",
        "to": "Phase V",
        "type": "arrow",
        "label": "adds safety + emotion"
      }
    ],
    "callout_boxes": [
      {
        "heading": "FROM WER-ONLY TO MULTI-DIMENSIONAL",
        "body_text": "Evaluation caught up with production reality. Benchmarks now test tool use, conversation flow, knowledge grounding, safety, and emotional intelligence.",
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
- [ ] Layout template identified (E)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
