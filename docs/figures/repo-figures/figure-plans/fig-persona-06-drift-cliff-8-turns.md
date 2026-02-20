# fig-persona-06: Persona Drift Cliff at 8 Turns

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-06 |
| **Title** | Persona Drift Cliff at 8 Turns |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/knowledge-base/persona-engineering/, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | A (Hero) |

## Purpose

Visualizes the empirical finding that persona consistency drops sharply around conversation turn 8, with voice modality showing even faster drift around turns 4-5. Answers: "When does persona drift become a problem, and how urgent is the need for drift detection and repair?"

## Key Message

Significant persona drift occurs within 8 conversation turns -- voice modality drifts even faster at turns 4-5 -- driven by attention decay on persona tokens in the system prompt.

## Visual Concept

Hero layout (Template A) with a large line chart as the central element. X-axis shows conversation turns (1-20), Y-axis shows persona consistency score (0.0-1.0). The primary line (text modality) starts near 1.0 and shows a sharp cliff around turn 8, then plateaus around 0.5. A secondary line (voice modality) shows an earlier, steeper cliff around turns 4-5, plateauing around 0.4. A horizontal threshold line marks the "acceptable consistency" boundary. Annotations call out the cliff regions. Below the chart, a root cause annotation explains attention decay on persona tokens. An accent square marks the critical turn 8 boundary.

```
+-----------------------------------------------------------------------+
|  PERSONA DRIFT                                                  [sq]   |
|  CLIFF AT 8 TURNS                                                      |
+-----------------------------------------------------------------------+
|                                                                        |
|  1.0 ┬─────────────────────────────────────────────────────────────    |
|      │ ●━━━━━●━━━━●                                                    |
|  0.9 │              ●                                                  |
|      │               \         TEXT MODALITY                           |
|  0.8 │  ○─────○       \                                               |
|      │         \       ●                                               |
|  0.7 │ VOICE    \       \          ┌─────────────────────┐            |
|      │ MODALITY  ○       \         │ DRIFT CLIFF         │            |
|  0.6 │            \      ●────●    │ Turn 8 (text)       │            |
|      │             \          \    │ Turn 4-5 (voice)    │            |
|  0.5 │ ─ ─ ─ ─ ─ ─ ○─ ─ ─ ─ ─●━━━━●━━━━●━━━━●━━━━●     │            |
|      │  ACCEPTABLE   \               PLATEAU ~0.5  │     │            |
|  0.4 │  THRESHOLD     ○━━━○━━━○━━━○━━━○━━━○━━━○    │     │            |
|      │                       VOICE PLATEAU ~0.4     │     │            |
|  0.3 │                                              │     │            |
|      │                                              └─────┘            |
|  0.2 │                                                                 |
|      │                                                                 |
|  0.1 │                                                                 |
|      │                                                                 |
|  0.0 ┴──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──   |
|         1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20    |
|                           CONVERSATION TURNS                           |
|                                                                        |
|  ROOT CAUSE: Attention decay on persona tokens in system prompt.       |
|  As conversation grows, model attention shifts to recent user turns,   |
|  diluting persona instruction influence.                               |
|                                                                        |
|  SIGNIFICANT PERSONA DRIFT OCCURS WITHIN 8 TURNS --              [sq] |
|  VOICE IS FASTER                                                       |
+-----------------------------------------------------------------------+
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
    content: "PERSONA DRIFT CLIFF AT 8 TURNS"
    role: title

  - id: chart_zone
    bounds: [80, 140, 1500, 600]
    role: content_area
    label: "Drift Chart"

  - id: annotation_zone
    bounds: [1340, 340, 520, 200]
    role: content_area
    label: "Drift Cliff Annotation"

  - id: root_cause_zone
    bounds: [80, 780, 1760, 120]
    role: content_area
    label: "Root Cause Explanation"

  - id: callout_zone
    bounds: [80, 940, 1760, 100]
    content: "SIGNIFICANT PERSONA DRIFT OCCURS WITHIN 8 TURNS -- VOICE IS FASTER"
    role: callout_box

anchors:
  - id: text_line
    position: [160, 180]
    size: [1360, 500]
    role: confidence_high
    label: "Text modality consistency"

  - id: voice_line
    position: [160, 260]
    size: [1360, 500]
    role: confidence_medium
    label: "Voice modality consistency"

  - id: threshold_line
    position: [160, 480]
    size: [1360, 2]
    role: confidence_low
    label: "Acceptable threshold"

  - id: cliff_marker_text
    position: [760, 300]
    size: [40, 200]
    role: decision_point
    label: "Turn 8 cliff"

  - id: cliff_marker_voice
    position: [480, 280]
    size: [40, 200]
    role: decision_point
    label: "Turn 4-5 cliff"

  - id: x_axis
    position: [160, 700]
    size: [1360, 30]
    role: data_flow
    label: "Conversation turns 1-20"

  - id: y_axis
    position: [130, 180]
    size: [30, 520]
    role: data_flow
    label: "Persona consistency 0.0-1.0"

  - id: root_cause_block
    position: [100, 790]
    size: [1720, 100]
    role: processing_stage
    label: "ROOT CAUSE: Attention decay"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "PERSONA DRIFT CLIFF AT 8 TURNS" in editorial caps |
| Text modality line | `confidence_high` | Primary line showing text-based persona consistency declining from ~1.0 to ~0.5 with cliff at turn 8 |
| Voice modality line | `confidence_medium` | Secondary line showing voice-based persona consistency declining faster, cliff at turns 4-5, plateau ~0.4 |
| Acceptable threshold | `confidence_low` | Horizontal dashed line at consistency score where drift becomes unacceptable |
| Turn 8 cliff marker | `decision_point` | Annotation highlighting the sharp decline region for text modality |
| Turn 4-5 cliff marker | `decision_point` | Annotation highlighting the earlier sharp decline for voice modality |
| X-axis | `data_flow` | Conversation turns 1-20 |
| Y-axis | `data_flow` | Persona consistency score 0.0-1.0 |
| Root cause block | `processing_stage` | Explanation: attention decay on persona tokens as conversation grows |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| High consistency (turns 1-7) | Cliff region (turn 8) | arrow | "sharp decline" |
| Cliff region | Plateau (~0.5) | arrow | "stabilizes but degraded" |
| Voice cliff (turns 4-5) | Voice plateau (~0.4) | arrow | "voice drifts faster" |
| Attention decay | Cliff region | dashed | "root cause" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "DRIFT CLIFF" | Text modality: sharp decline at turn 8. Voice modality: even earlier cliff at turns 4-5. Both plateau at degraded consistency levels (0.5 and 0.4 respectively). | right of chart |
| "SIGNIFICANT PERSONA DRIFT OCCURS WITHIN 8 TURNS -- VOICE IS FASTER" | Attention decay on persona tokens in the system prompt causes the model to gradually lose persona alignment as conversation length grows. Voice interactions compound this with prosodic drift. | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "TEXT MODALITY"
- Label 2: "VOICE MODALITY"
- Label 3: "ACCEPTABLE THRESHOLD"
- Label 4: "DRIFT CLIFF"
- Label 5: "CONVERSATION TURNS"
- Label 6: "PERSONA CONSISTENCY"
- Label 7: "Turn 8 (text)"
- Label 8: "Turn 4-5 (voice)"
- Label 9: "Plateau ~0.5"
- Label 10: "Plateau ~0.4"
- Label 11: "ROOT CAUSE"
- Label 12: "Attention decay"
- Label 13: "Persona tokens diluted"

### Caption

Persona consistency score plotted over 20 conversation turns showing a sharp drift cliff at turn 8 for text modality and at turns 4-5 for voice modality, with both plateauing at degraded levels. Root cause is attention decay on persona tokens in the system prompt.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Engineering jargon** -- "attention decay", "system prompt", "persona tokens" are appropriate for L3 audience.
5. **Background MUST be warm cream (#f6f3e6)**.
6. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

9. The "8 turns" cliff is a synthesis across multiple papers -- do NOT attribute it to a single study.
10. The voice modality drift at turns 4-5 is based on the observation that voice interactions have shorter turns and compound prosodic drift -- do NOT claim exact turn numbers as universal.
11. The Y-axis values (1.0, 0.5, 0.4) are illustrative of the general pattern -- do NOT present them as exact measurements from a specific experiment.
12. The "acceptable threshold" line position is a design decision, NOT a universal standard.
13. Do NOT show confidence intervals or error bars -- this is a conceptual illustration, not a data plot.
14. The root cause (attention decay) is the primary mechanism but NOT the only one -- context window limits and instruction following degradation also contribute.
15. Do NOT imply that drift is linear -- the cliff shape (sharp decline then plateau) is the key insight.

## Alt Text

Line chart of persona consistency score over 20 conversation turns showing a sharp drift cliff at turn 8 for text modality and turns 4-5 for voice modality, both plateauing at degraded levels, with root cause analysis of attention decay on persona tokens in system prompts.

## Image Embed

![Line chart of persona consistency score over 20 conversation turns showing a sharp drift cliff at turn 8 for text modality and turns 4-5 for voice modality, both plateauing at degraded levels, with root cause analysis of attention decay on persona tokens in system prompts.](docs/figures/repo-figures/assets/fig-persona-06-drift-cliff-8-turns.jpg)

*Persona consistency score plotted over 20 conversation turns showing a sharp drift cliff at turn 8 for text modality and at turns 4-5 for voice modality, with both plateauing at degraded levels. Root cause is attention decay on persona tokens in the system prompt.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-06",
    "title": "Persona Drift Cliff at 8 Turns",
    "audience": "L3",
    "layout_template": "A"
  },
  "content_architecture": {
    "primary_message": "Significant persona drift occurs within 8 conversation turns, with voice modality drifting even faster at turns 4-5.",
    "layout_flow": "centered",
    "key_structures": [
      {
        "name": "Text Modality Line",
        "role": "confidence_high",
        "is_highlighted": true,
        "labels": ["TEXT MODALITY", "Cliff at turn 8", "Plateau ~0.5"]
      },
      {
        "name": "Voice Modality Line",
        "role": "confidence_medium",
        "is_highlighted": true,
        "labels": ["VOICE MODALITY", "Cliff at turns 4-5", "Plateau ~0.4"]
      },
      {
        "name": "Acceptable Threshold",
        "role": "confidence_low",
        "is_highlighted": false,
        "labels": ["ACCEPTABLE THRESHOLD"]
      },
      {
        "name": "Root Cause",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["ROOT CAUSE", "Attention decay on persona tokens"]
      }
    ],
    "relationships": [
      {
        "from": "High consistency",
        "to": "Cliff region",
        "type": "arrow",
        "label": "sharp decline"
      },
      {
        "from": "Cliff region",
        "to": "Plateau",
        "type": "arrow",
        "label": "stabilizes but degraded"
      },
      {
        "from": "Attention decay",
        "to": "Cliff region",
        "type": "dashed",
        "label": "root cause"
      }
    ],
    "callout_boxes": [
      {
        "heading": "SIGNIFICANT PERSONA DRIFT OCCURS WITHIN 8 TURNS -- VOICE IS FASTER",
        "body_text": "Attention decay on persona tokens causes progressive persona loss. Voice interactions compound with prosodic drift.",
        "position": "bottom-full-width"
      }
    ]
  }
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
- [x] Audience level correct (L3)
- [x] Layout template identified (A)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
