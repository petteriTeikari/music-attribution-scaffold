# fig-voice-08: STT: Accuracy vs Latency Tradeoff

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-08 |
| **Title** | STT: Accuracy vs Latency Tradeoff |
| **Audience** | L4 (Researcher / Deep Technical) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P2 |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | A (Hero) |

## Purpose

Visualize the accuracy-latency tradeoff as a scatter plot with models positioned by their real-time factor (RTFx) and word error rate (WER), revealing the Pareto frontier where no model dominates another on both axes simultaneously. Answers: "Which models offer the best accuracy-latency tradeoff, and where is the Pareto frontier?"

## Key Message

The Pareto frontier shifted dramatically in 2025-2026 -- Canary-Qwen achieves 5.63% WER at 418x real-time, defining a new best-case tradeoff boundary.

## Visual Concept

Hero layout (Template A) dominated by a large scatter plot. X-axis: Latency expressed as RTFx (real-time factor, higher = faster, log scale). Y-axis: Accuracy expressed as inverse WER (higher = better accuracy, or equivalently lower WER on a reversed axis). Models appear as positioned circular nodes with names and key metrics. A coral accent line traces the Pareto frontier -- the boundary where no model simultaneously improves on both axes. Models on the frontier are highlighted with `selected_option` semantic. Models below the frontier are dimmed. An annotation arrow points to Canary-Qwen as the frontier leader. The background uses subtle grid lines for readability. A callout at the bottom summarizes the frontier shift.

```
+---------------------------------------------------------------------+
|  STT: ACCURACY vs LATENCY                                    [sq]   |
|  PARETO FRONTIER                                                    |
|                                                                     |
|  ACCURACY                                                           |
|  (low WER)                                                          |
|       |                                                             |
|       |                         * Canary-Qwen                       |
|       |                           (5.63%, 418x)                     |
|       |              * Nova-3  /                                     |
|       |             /         /                                      |
|       |  * Voxtral /         / <-- PARETO FRONTIER                  |
|       |          /          /      (coral line)                     |
|       |         /          /                                        |
|       |  * Speechmatics   /                                         |
|       |       /          /                                          |
|       |      /   * Faster-Whisper                                   |
|       |     /                                                       |
|       |    /  * Whisper v3-turbo                                    |
|       |   /                                                         |
|       |  /              * Moonshine                                 |
|       | /                 (17ms, edge)                               |
|       +-----------------------------------------------------       |
|                          LATENCY (RTFx, log scale) -->              |
|                                                                     |
|  THE PARETO FRONTIER SHIFTED -- CANARY-QWEN: 5.63% WER      [line] |
|  AT 418x REAL-TIME                                                  |
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
    content: "STT: ACCURACY VS LATENCY"
    role: title

  - id: plot_zone
    bounds: [120, 140, 1680, 700]
    role: content_area

  - id: callout_zone
    bounds: [80, 880, 1760, 160]
    content: "THE PARETO FRONTIER SHIFTED"
    role: callout_box

anchors:
  - id: y_axis
    position: [200, 160]
    size: [2, 680]
    role: accent_line
    label: "Accuracy (inverse WER)"

  - id: x_axis
    position: [200, 820]
    size: [1560, 2]
    role: accent_line
    label: "Latency (RTFx, log scale)"

  - id: pareto_frontier
    position: [280, 200]
    size: [1400, 580]
    role: accent_line
    label: "Pareto frontier"

  - id: node_canary_qwen
    position: [1480, 200]
    size: [200, 70]
    role: selected_option
    label: "CANARY-QWEN"

  - id: node_canary_qwen_metrics
    position: [1480, 270]
    size: [200, 30]
    role: annotation
    label: "5.63% WER, 418x RTFx"

  - id: node_deepgram_nova3
    position: [1100, 280]
    size: [200, 70]
    role: selected_option
    label: "DEEPGRAM NOVA-3"

  - id: node_voxtral
    position: [600, 340]
    size: [200, 70]
    role: processing_stage
    label: "VOXTRAL"

  - id: node_speechmatics
    position: [800, 420]
    size: [200, 70]
    role: processing_stage
    label: "SPEECHMATICS"

  - id: node_faster_whisper
    position: [1000, 520]
    size: [200, 70]
    role: selected_option
    label: "FASTER-WHISPER"

  - id: node_whisper
    position: [700, 600]
    size: [200, 70]
    role: processing_stage
    label: "WHISPER V3-TURBO"

  - id: node_moonshine
    position: [1400, 660]
    size: [200, 70]
    role: selected_option
    label: "MOONSHINE"

  - id: node_moonshine_metrics
    position: [1400, 730]
    size: [200, 30]
    role: annotation
    label: "17ms/chunk, edge"

  - id: frontier_annotation
    position: [1200, 360]
    size: [300, 40]
    role: annotation
    label: "PARETO FRONTIER"

  - id: callout_bar
    position: [80, 900]
    size: [1760, 120]
    role: callout_box
    label: "THE PARETO FRONTIER SHIFTED"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Y-Axis (Accuracy) | `accent_line` | Vertical axis: inverse WER, higher = more accurate |
| X-Axis (Latency) | `accent_line` | Horizontal axis: RTFx on log scale, higher = faster |
| Pareto Frontier Line | `accent_line` | Coral line connecting models where no other model dominates on both axes |
| Canary-Qwen Node | `selected_option` | Frontier leader: 5.63% WER at 418x real-time |
| Deepgram Nova-3 Node | `selected_option` | Production frontier: strong accuracy with streaming API |
| Voxtral Node | `processing_stage` | Mistral 7B model, competitive but off-frontier |
| Speechmatics Node | `processing_stage` | Enterprise API, moderate position |
| Faster-Whisper Node | `selected_option` | Self-hosted frontier: CTranslate2 optimized |
| Whisper v3-turbo Node | `processing_stage` | Open-source baseline, below frontier |
| Moonshine Node | `selected_option` | Edge frontier: extreme latency, lower accuracy |
| Frontier Annotation | `annotation` | Label identifying the Pareto frontier line |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| Canary-Qwen | Deepgram Nova-3 | frontier_line | "Pareto frontier segment" |
| Deepgram Nova-3 | Faster-Whisper | frontier_line | "Pareto frontier segment" |
| Faster-Whisper | Moonshine | frontier_line | "Pareto frontier segment" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "THE PARETO FRONTIER SHIFTED" | Canary-Qwen defines the new upper-right frontier at 5.63% WER and 418x real-time factor. Previous leader (Whisper v3-turbo) is now dominated. The frontier spans from Moonshine (edge, high RTFx, lower accuracy) through Faster-Whisper and Deepgram to Canary-Qwen (highest accuracy, highest throughput). | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "ACCURACY vs LATENCY"
- Label 2: "PARETO FRONTIER"
- Label 3: "ACCURACY (inverse WER)"
- Label 4: "LATENCY (RTFx, log scale)"
- Label 5: "CANARY-QWEN"
- Label 6: "5.63% WER, 418x RTFx"
- Label 7: "DEEPGRAM NOVA-3"
- Label 8: "VOXTRAL"
- Label 9: "SPEECHMATICS"
- Label 10: "FASTER-WHISPER"
- Label 11: "WHISPER V3-TURBO"
- Label 12: "MOONSHINE"
- Label 13: "17ms/chunk, edge"
- Label 14: "PARETO FRONTIER"
- Label 15: "Frontier shifted 2025-2026"

### Caption

Scatter plot showing STT models positioned by accuracy (inverse WER) versus latency (RTFx), with a coral Pareto frontier line connecting models where no alternative dominates on both axes simultaneously.

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

8. This is a SCATTER PLOT concept, not a flowchart -- models are positioned by two quantitative axes.
9. The Pareto frontier MUST be a single continuous coral accent line connecting frontier models -- not a shaded area.
10. RTFx axis should use log scale conceptually (labels suggest orders of magnitude, not linear spacing).
11. Models ON the frontier use `selected_option` semantic; models below use `processing_stage`.
12. WER values and RTFx values must be visible as metric annotations next to model nodes where known.
13. Do NOT fabricate exact WER or RTFx numbers for models where they are not provided -- use approximate positioning.
14. Canary-Qwen must be positioned in the upper-right corner (best accuracy AND best throughput) to show why it shifted the frontier.
15. Moonshine must be positioned far right (extreme speed) but lower on accuracy -- it is the edge deployment leader.
16. Subtle grid lines are allowed for readability but must not dominate the visual.

## Alt Text

Scatter plot of speech-to-text models positioned by accuracy (inverse WER) versus latency (RTFx), with a Pareto frontier connecting Canary-Qwen (5.63% WER, 418x), Deepgram Nova-3, Faster-Whisper, and Moonshine as tradeoff leaders.

## Image Embed

<!-- NOTE: fig-voice-08 PNG was not generated. Image embed placeholder only. -->
![Scatter plot of speech-to-text models positioned by accuracy (inverse WER) versus latency (RTFx), with a Pareto frontier connecting Canary-Qwen (5.63% WER, 418x), Deepgram Nova-3, Faster-Whisper, and Moonshine as tradeoff leaders.](docs/figures/repo-figures/assets/fig-voice-08-stt-accuracy-vs-latency.jpg)

*Scatter plot showing STT models positioned by accuracy (inverse WER) versus latency (RTFx), with a coral Pareto frontier line connecting models where no alternative dominates on both axes simultaneously.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-08",
    "title": "STT: Accuracy vs Latency Tradeoff",
    "audience": "L4",
    "layout_template": "A"
  },
  "content_architecture": {
    "primary_message": "The Pareto frontier shifted -- Canary-Qwen achieves 5.63% WER at 418x real-time, defining a new best-case tradeoff boundary.",
    "layout_flow": "scatter-plot",
    "key_structures": [
      {
        "name": "Canary-Qwen",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["CANARY-QWEN", "5.63% WER", "418x RTFx"],
        "position_concept": "upper-right (best accuracy + best speed)"
      },
      {
        "name": "Deepgram Nova-3",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["DEEPGRAM NOVA-3"],
        "position_concept": "upper-middle (high accuracy, production API)"
      },
      {
        "name": "Voxtral",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["VOXTRAL"],
        "position_concept": "middle-left (moderate accuracy, moderate speed)"
      },
      {
        "name": "Speechmatics",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["SPEECHMATICS"],
        "position_concept": "middle (moderate accuracy, moderate speed)"
      },
      {
        "name": "Faster-Whisper",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["FASTER-WHISPER"],
        "position_concept": "center-right (moderate accuracy, good speed, self-hosted)"
      },
      {
        "name": "Whisper v3-turbo",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["WHISPER V3-TURBO"],
        "position_concept": "below frontier (dominated by Faster-Whisper)"
      },
      {
        "name": "Moonshine",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["MOONSHINE", "17ms/chunk"],
        "position_concept": "lower-right (lower accuracy, extreme speed, edge)"
      },
      {
        "name": "Pareto Frontier",
        "role": "accent_line",
        "is_highlighted": true,
        "labels": ["PARETO FRONTIER"],
        "position_concept": "connecting Canary-Qwen -> Nova-3 -> Faster-Whisper -> Moonshine"
      }
    ],
    "relationships": [
      {
        "from": "Canary-Qwen",
        "to": "Deepgram Nova-3",
        "type": "frontier_line",
        "label": "Pareto frontier"
      },
      {
        "from": "Deepgram Nova-3",
        "to": "Faster-Whisper",
        "type": "frontier_line",
        "label": "Pareto frontier"
      },
      {
        "from": "Faster-Whisper",
        "to": "Moonshine",
        "type": "frontier_line",
        "label": "Pareto frontier"
      }
    ],
    "callout_boxes": [
      {
        "heading": "THE PARETO FRONTIER SHIFTED",
        "body_text": "Canary-Qwen defines the new upper-right frontier at 5.63% WER and 418x real-time. Previous leader (Whisper v3-turbo) is now dominated.",
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
- [ ] Audience level correct (L4)
- [ ] Layout template identified (A)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
