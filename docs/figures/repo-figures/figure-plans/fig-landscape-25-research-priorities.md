# fig-landscape-25: Research Priority Forecast 2026-2028

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-25 |
| **Title** | Research Priority Forecast 2026-2028 |
| **Audience** | L4 (AI/ML) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

This figure maps the four research priorities that will dominate music attribution from 2026-2028, highlighting the gap between what academia studies and what industry needs. It provides a research planning roadmap for teams deciding where to invest technical effort.

## Key Message

Four research priorities will dominate 2026-2028 -- multimodal attribution, real-time streaming attribution, AI-assisted music analysis, and federated attribution -- each representing a gap between what academia studies and what industry needs.

## Visual Concept

A 2x2 multi-panel layout where each panel represents one research priority. Each panel contains the priority name, a current-state indicator, an academia-industry gap bar, and an estimated timeline. A coral accent line runs horizontally between the top and bottom rows. Each panel uses a structured internal layout: current state (left), gap analysis (center), and timeline (right). The panels progress from most immediately actionable (top-left) to most structurally challenging (bottom-right).

```
+---------------------------------------------------------------+
|  RESEARCH PRIORITY FORECAST 2026-2028                          |
|  ■ Four Frontiers Where Academia Meets Industry Need           |
+---------------------------------------------------------------+
|                               |                                |
|  I. MULTIMODAL ATTRIBUTION    |  II. REAL-TIME STREAMING       |
|  ─────────────────────        |  ──────────────────            |
|  Beyond audio-only TDA        |  Attribution at inference      |
|                               |                                |
|  Current: audio fingerprint   |  Current: batch post-hoc       |
|  Gap: lyrics, video, style    |  Gap: latency < 100ms          |
|  Timeline: 2026 H2            |  Timeline: 2027 H1             |
|  Refs: CLAP, MusicLIME        |  Refs: Vovk conformal          |
|                               |                                |
|───────────────── ■ ───────────────────────────────────────────|
|                               |                                |
|  III. AI-ASSISTED ANALYSIS    |  IV. FEDERATED ATTRIBUTION     |
|  ──────────────────           |  ─────────────────────         |
|  LLMs explain attribution     |  Multi-CMO coordination        |
|                               |                                |
|  Current: numeric scores      |  Current: siloed registries    |
|  Gap: natural language why    |  Gap: privacy-preserving       |
|  Timeline: 2027 H2            |  Timeline: 2028                |
|  Refs: AudioGenX, Beigi UQ    |  Refs: STIM pilot, FL          |
|                               |                                |
+---------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: warm_cream

title_block:
  position: [60, 40]
  width: 1800
  height: 80
  elements:
    - type: heading_display
      text: "RESEARCH PRIORITY FORECAST 2026-2028"
    - type: label_editorial
      text: "Four Frontiers Where Academia Meets Industry Need"

panel_multimodal:
  position: [60, 140]
  width: 880
  height: 380
  label: "I. MULTIMODAL ATTRIBUTION"
  elements:
    - { type: label_editorial, text: "Beyond audio-only TDA" }
    - { type: data_mono, text: "Current: audio fingerprint + embedding" }
    - { type: callout_bar, text: "Gap: lyrics, video, style transfer unaddressed" }
    - { type: data_mono, text: "Timeline: 2026 H2" }
    - { type: label_editorial, text: "Refs: CLAP, MusicLIME, multimodal SHAP" }

panel_streaming:
  position: [960, 140]
  width: 880
  height: 380
  label: "II. REAL-TIME STREAMING"
  elements:
    - { type: label_editorial, text: "Attribution at inference time" }
    - { type: data_mono, text: "Current: batch post-hoc processing" }
    - { type: callout_bar, text: "Gap: latency < 100ms for streaming platforms" }
    - { type: data_mono, text: "Timeline: 2027 H1" }
    - { type: label_editorial, text: "Refs: Vovk conformal prediction, online calibration" }

divider:
  position: [60, 530]
  width: 1800
  type: accent_line_horizontal

panel_ai_analysis:
  position: [60, 560]
  width: 880
  height: 380
  label: "III. AI-ASSISTED ANALYSIS"
  elements:
    - { type: label_editorial, text: "LLMs explain attribution decisions" }
    - { type: data_mono, text: "Current: numeric scores only" }
    - { type: callout_bar, text: "Gap: natural language explanations for non-experts" }
    - { type: data_mono, text: "Timeline: 2027 H2" }
    - { type: label_editorial, text: "Refs: AudioGenX, Beigi UQ taxonomy" }

panel_federated:
  position: [960, 560]
  width: 880
  height: 380
  label: "IV. FEDERATED ATTRIBUTION"
  elements:
    - { type: label_editorial, text: "Multi-CMO coordination without data sharing" }
    - { type: data_mono, text: "Current: siloed registries per CMO" }
    - { type: callout_bar, text: "Gap: privacy-preserving cross-registry resolution" }
    - { type: data_mono, text: "Timeline: 2028" }
    - { type: label_editorial, text: "Refs: STIM pilot, federated learning, secure MPC" }
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "RESEARCH PRIORITY FORECAST 2026-2028" with coral accent square |
| Subtitle | `label_editorial` | "Four Frontiers Where Academia Meets Industry Need" |
| Multimodal panel | `solution_component` | Extending TDA beyond audio to lyrics, video, style |
| Streaming panel | `solution_component` | Attribution at inference time, not post-hoc batch |
| AI analysis panel | `solution_component` | LLMs explaining attribution to non-experts |
| Federated panel | `solution_component` | Multi-CMO coordination without sharing proprietary data |
| Gap indicators | `problem_statement` | Academia-industry gap description per panel |
| Timeline markers | `data_mono` | Estimated delivery timeline per priority |
| Panel divider | `callout_bar` | Coral accent line between top and bottom rows |
| Panel numerals | `section_numeral` | Roman numerals I-IV for each panel |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Multimodal | Streaming | sequential | "Multimodal enables richer real-time signals" |
| AI Analysis | Multimodal | dependency | "Explanations require multimodal understanding" |
| Federated | All panels | enabling | "Federation unlocks cross-registry scale" |
| Vovk conformal | Streaming | theoretical | "Online conformal prediction enables real-time UQ" |
| Beigi UQ taxonomy | AI Analysis | theoretical | "Uncertainty taxonomy structures explanations" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Academia-Industry Gap | "Academic MIR focuses on retrieval; industry needs attribution with confidence" | Top-right corner |
| Key Dependency | "All four priorities depend on A0-A3 assurance levels as shared evaluation framework" | Bottom center |

## Text Content

### Labels (Max 30 chars each)

- Multimodal Attribution
- Real-Time Streaming
- AI-Assisted Analysis
- Federated Attribution
- Current State
- Academia-Industry Gap
- Timeline
- Audio-Only TDA
- Batch Post-Hoc
- Numeric Scores Only
- Siloed Registries
- Vovk Conformal Prediction
- Beigi UQ Taxonomy
- AudioGenX
- MusicLIME

### Caption (for embedding in documentation)

Four research priorities will shape music attribution from 2026-2028: multimodal attribution extending TDA beyond audio-only methods, real-time streaming attribution replacing batch processing, AI-assisted analysis using LLMs to explain decisions to non-experts, and federated attribution enabling multi-CMO coordination without sharing proprietary data. Each priority maps a specific gap between academic research focus and industry deployment needs.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)**.
5. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

1. There are exactly FOUR research priorities -- do NOT add or remove any.
2. Timelines are ESTIMATES, not commitments -- do NOT present as definitive dates.
3. The academia-industry gap is STRUCTURAL, not a criticism -- do NOT frame as "academia is behind."
4. Vovk conformal prediction and Beigi UQ taxonomy are SPECIFIC references -- do NOT generalize to "machine learning methods."
5. Federated attribution means PRIVACY-PRESERVING coordination -- do NOT conflate with blockchain or decentralization.
6. Do NOT imply any single company or product solves all four priorities.
7. Do NOT render timeline bars as Gantt charts -- use text-based timeline indicators.

## Alt Text

Four-panel research priority forecast: multimodal, streaming, AI-assisted, and federated attribution for 2026-2028.

## JSON Export Block

```json
{
  "id": "fig-landscape-25",
  "title": "Research Priority Forecast 2026-2028",
  "audience": "L4",
  "priority": "P0",
  "layout": "B",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Speculate",
  "novelty": 4,
  "priorities": [
    {
      "name": "Multimodal Attribution",
      "current_state": "Audio-only TDA (fingerprinting, embeddings)",
      "gap": "Lyrics, video, style transfer unaddressed",
      "timeline": "2026 H2",
      "references": ["CLAP", "MusicLIME", "multimodal SHAP"]
    },
    {
      "name": "Real-Time Streaming Attribution",
      "current_state": "Batch post-hoc processing",
      "gap": "Latency < 100ms for streaming platforms",
      "timeline": "2027 H1",
      "references": ["Vovk conformal prediction", "online calibration"]
    },
    {
      "name": "AI-Assisted Music Analysis",
      "current_state": "Numeric confidence scores only",
      "gap": "Natural language explanations for non-experts",
      "timeline": "2027 H2",
      "references": ["AudioGenX", "Beigi UQ taxonomy", "MusicLIME"]
    },
    {
      "name": "Federated Attribution",
      "current_state": "Siloed registries per CMO",
      "gap": "Privacy-preserving cross-registry resolution",
      "timeline": "2028",
      "references": ["STIM pilot", "federated learning", "secure MPC"]
    }
  ],
  "semantic_tags_used": [
    "heading_display", "label_editorial", "solution_component",
    "problem_statement", "data_mono", "callout_bar", "section_numeral"
  ]
}
```

## Quality Checklist

- [x] Primary message clear in one sentence
- [x] Semantic tags used (no colors, hex codes, or font names in content spec)
- [x] ASCII layout sketched
- [x] Spatial anchors defined in YAML
- [x] Labels under 30 characters
- [x] Anti-hallucination rules listed
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L1/L2/L3/L4)
- [x] Layout template identified (A/B/C/D/E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
