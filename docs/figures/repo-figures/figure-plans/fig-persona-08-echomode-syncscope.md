# fig-persona-08: EchoMode SyncScope Drift Detection System

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-08 |
| **Title** | EchoMode SyncScope Drift Detection System |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/knowledge-base/persona-engineering/, docs/planning/ |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Shows the EchoMode SyncScope system for real-time persona drift detection, with the SyncScore EWMA time series on the left and the Behavioral State Model on the right. Answers: "How does a production drift detection system work in practice, and how does it avoid false positives while catching sustained drift?"

## Key Message

EWMA smoothing of the SyncScore prevents false positive drift alerts from single-turn anomalies while reliably catching sustained persona drift, triggering repair through a four-state behavioral model.

## Visual Concept

Split-panel layout (Template D). Left panel: A time series chart showing raw SyncScore values (noisy) overlaid with an EWMA-smoothed line. A horizontal threshold line marks the drift detection boundary. When the smoothed line crosses below the threshold, a vertical marker indicates the "drift detection point". Single-turn anomalies in the raw score stay above the smoothed threshold, demonstrating false positive prevention. Right panel: A state machine diagram with four states arranged in a cycle: Sync (normal operation) -> Resonance (deep engagement) -> Insight (creative exploration) -> Calm (low energy). A repair trigger arrow connects the drift detection from the left panel to a "re-injection" action that pushes the state back toward Sync.

```
+-----------------------------------------------------------------------+
|  ECHOMODE SYNCSCOPE                                             [sq]   |
|  DRIFT DETECTION SYSTEM                                                |
+-----------------------------------------------------------------------+
|                                                                        |
|  SYNCSCORE TIME SERIES          │  BEHAVIORAL STATE MODEL              |
|  ═════════════════════          │  ══════════════════════              |
|                                 │                                      |
|  1.0 ┬──────────────────────   │       ┌──────────┐                   |
|      │  ╱╲  raw SyncScore      │  ┌───>│  SYNC    │───┐               |
|  0.9 │ ╱  ╲  ╱╲                │  │    │ (normal) │   │               |
|      │╱    ╲╱  ╲  ╱╲           │  │    └──────────┘   │               |
|  0.8 │──────────────── EWMA    │  │         ▲         ▼               |
|      │          ╲  ╱   ╲       │  │    ┌──────────┐ ┌─────────┐      |
|  0.7 │           ╲╱     ╲      │  │    │  CALM    │ │RESONANCE│      |
|      │                   ╲     │  │    │(low      │ │(deep    │      |
|  0.6 │─ ─ ─ ─THRESHOLD─ ─╲─   │  │    │ energy)  │ │engage)  │      |
|      │                    ╲    │  │    └──────────┘ └─────────┘      |
|  0.5 │                     ●   │  │         ▲         │               |
|      │              DRIFT  │   │  │    ┌──────────┐   │               |
|  0.4 │              DETECTED   │  └────│ INSIGHT  │<──┘               |
|      │                         │       │(creative)│                    |
|  0.3 │                         │       └──────────┘                    |
|      ├──┬──┬──┬──┬──┬──┬──┬── │                                      |
|         1  2  3  4  5  6  7  8 │  REPAIR TRIGGER:                     |
|            Turns               │  Drift detected → re-inject          |
|                                │  persona tokens → push to SYNC       |
|                                │                                      |
|  EWMA SMOOTHING PREVENTS FALSE POSITIVES WHILE CATCHING          [sq] |
|  SUSTAINED DRIFT                                                       |
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
    content: "ECHOMODE SYNCSCOPE DRIFT DETECTION SYSTEM"
    role: title

  - id: left_panel
    bounds: [80, 140, 860, 720]
    role: content_area
    label: "SyncScore Time Series"

  - id: panel_divider
    bounds: [960, 140, 2, 720]
    role: accent_line

  - id: right_panel
    bounds: [980, 140, 860, 720]
    role: content_area
    label: "Behavioral State Model"

  - id: callout_zone
    bounds: [80, 940, 1760, 100]
    content: "EWMA SMOOTHING PREVENTS FALSE POSITIVES WHILE CATCHING SUSTAINED DRIFT"
    role: callout_box

anchors:
  - id: raw_syncscore
    position: [120, 180]
    size: [780, 440]
    role: data_flow
    label: "Raw SyncScore"

  - id: ewma_line
    position: [120, 220]
    size: [780, 400]
    role: confidence_high
    label: "EWMA smoothed"

  - id: threshold
    position: [120, 460]
    size: [780, 2]
    role: confidence_low
    label: "Threshold"

  - id: drift_point
    position: [700, 460]
    size: [20, 100]
    role: decision_point
    label: "Drift detected"

  - id: state_sync
    position: [1120, 200]
    size: [240, 120]
    role: confidence_high
    label: "SYNC"

  - id: state_resonance
    position: [1440, 340]
    size: [240, 120]
    role: processing_stage
    label: "RESONANCE"

  - id: state_insight
    position: [1440, 540]
    size: [240, 120]
    role: processing_stage
    label: "INSIGHT"

  - id: state_calm
    position: [1120, 540]
    size: [240, 120]
    role: processing_stage
    label: "CALM"

  - id: flow_sync_to_resonance
    from: state_sync
    to: state_resonance
    type: arrow
    label: "deepen"

  - id: flow_resonance_to_insight
    from: state_resonance
    to: state_insight
    type: arrow
    label: "explore"

  - id: flow_insight_to_calm
    from: state_insight
    to: state_calm
    type: arrow
    label: "settle"

  - id: flow_calm_to_sync
    from: state_calm
    to: state_sync
    type: arrow
    label: "return"

  - id: repair_trigger
    from: drift_point
    to: state_sync
    type: arrow
    label: "repair: re-inject persona"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "ECHOMODE SYNCSCOPE DRIFT DETECTION SYSTEM" in editorial caps |
| Raw SyncScore line | `data_flow` | Noisy per-turn synchronization score showing turn-by-turn variability |
| EWMA smoothed line | `confidence_high` | Exponentially Weighted Moving Average of SyncScore, smoothing out noise |
| Threshold line | `confidence_low` | Horizontal drift detection boundary |
| Drift detection point | `decision_point` | The moment when EWMA-smoothed SyncScore crosses below threshold |
| SYNC state | `confidence_high` | Normal operation -- persona is consistent and engaged |
| RESONANCE state | `processing_stage` | Deep engagement -- persona is performing optimally |
| INSIGHT state | `processing_stage` | Creative exploration -- persona is generating novel responses |
| CALM state | `processing_stage` | Low energy -- persona is in maintenance mode |
| Repair trigger | `feedback_loop` | Connection from drift detection to persona re-injection |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| SYNC | RESONANCE | arrow | "deepen engagement" |
| RESONANCE | INSIGHT | arrow | "explore creatively" |
| INSIGHT | CALM | arrow | "settle down" |
| CALM | SYNC | arrow | "return to normal" |
| Drift detection point | SYNC state | arrow | "repair: re-inject persona tokens" |
| Raw SyncScore | EWMA line | dashed | "smoothing" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "EWMA SMOOTHING PREVENTS FALSE POSITIVES WHILE CATCHING SUSTAINED DRIFT" | Single-turn anomalies in the raw SyncScore (e.g., a user asking an out-of-character question) do NOT trigger drift alerts because EWMA smoothing absorbs transient dips. Only sustained drift -- where multiple consecutive turns show declining consistency -- causes the smoothed score to cross the threshold and trigger persona repair. | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "SYNCSCORE TIME SERIES"
- Label 2: "BEHAVIORAL STATE MODEL"
- Label 3: "Raw SyncScore"
- Label 4: "EWMA smoothed"
- Label 5: "THRESHOLD"
- Label 6: "DRIFT DETECTED"
- Label 7: "SYNC (normal)"
- Label 8: "RESONANCE (deep engage)"
- Label 9: "INSIGHT (creative)"
- Label 10: "CALM (low energy)"
- Label 11: "REPAIR TRIGGER"
- Label 12: "Re-inject persona tokens"
- Label 13: "False positive absorbed"

### Caption

EchoMode SyncScope system with EWMA-smoothed SyncScore time series (left) detecting sustained drift while absorbing single-turn anomalies, and a four-state behavioral model (Sync, Resonance, Insight, Calm) with repair trigger re-injecting persona tokens on drift detection (right).

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Engineering jargon** -- EWMA, SyncScore, state machine are appropriate for L3 audience.
5. **Background MUST be warm cream (#f6f3e6)**.
6. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

9. EchoMode and SyncScope are specific system names -- do NOT substitute generic terms.
10. EWMA (Exponentially Weighted Moving Average) is a standard statistical technique -- do NOT confuse with simple moving average or other smoothing methods.
11. The four behavioral states (Sync, Resonance, Insight, Calm) are from the EchoMode framework -- do NOT add or rename states.
12. The repair mechanism is "re-inject persona tokens" -- this means repeating or strengthening persona instructions mid-conversation, NOT restarting the conversation.
13. The threshold line position is a tunable parameter, NOT a fixed constant -- do NOT present a specific numeric threshold as universal.
14. The time series chart is illustrative -- do NOT show specific numeric values on the Y-axis that imply experimental data.
15. Do NOT show the EWMA formula (that level of detail belongs in documentation, not the figure).

## Alt Text

Split-panel diagram of the EchoMode SyncScope drift detection system showing EWMA-smoothed SyncScore time series with threshold-based drift detection (left) and a four-state behavioral model (Sync, Resonance, Insight, Calm) with persona repair trigger for maintaining persona coherence (right).

## Image Embed

![Split-panel diagram of the EchoMode SyncScope drift detection system showing EWMA-smoothed SyncScore time series with threshold-based drift detection (left) and a four-state behavioral model (Sync, Resonance, Insight, Calm) with persona repair trigger for maintaining persona coherence (right).](docs/figures/repo-figures/assets/fig-persona-08-echomode-syncscope.jpg)

*EchoMode SyncScope system with EWMA-smoothed SyncScore time series (left) detecting sustained drift while absorbing single-turn anomalies, and a four-state behavioral model (Sync, Resonance, Insight, Calm) with repair trigger re-injecting persona tokens on drift detection (right).*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-08",
    "title": "EchoMode SyncScope Drift Detection System",
    "audience": "L3",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "EWMA smoothing prevents false positive drift alerts while reliably catching sustained persona drift through a four-state behavioral model.",
    "layout_flow": "left-right-split",
    "key_structures": [
      {
        "name": "Raw SyncScore",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["Raw SyncScore", "Noisy per-turn"]
      },
      {
        "name": "EWMA Smoothed Line",
        "role": "confidence_high",
        "is_highlighted": true,
        "labels": ["EWMA smoothed", "Absorbs anomalies"]
      },
      {
        "name": "Drift Detection Point",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["DRIFT DETECTED"]
      },
      {
        "name": "SYNC State",
        "role": "confidence_high",
        "is_highlighted": true,
        "labels": ["SYNC (normal)"]
      },
      {
        "name": "RESONANCE State",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["RESONANCE (deep engage)"]
      },
      {
        "name": "INSIGHT State",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["INSIGHT (creative)"]
      },
      {
        "name": "CALM State",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["CALM (low energy)"]
      }
    ],
    "relationships": [
      {
        "from": "SYNC",
        "to": "RESONANCE",
        "type": "arrow",
        "label": "deepen"
      },
      {
        "from": "RESONANCE",
        "to": "INSIGHT",
        "type": "arrow",
        "label": "explore"
      },
      {
        "from": "INSIGHT",
        "to": "CALM",
        "type": "arrow",
        "label": "settle"
      },
      {
        "from": "CALM",
        "to": "SYNC",
        "type": "arrow",
        "label": "return"
      },
      {
        "from": "Drift Detection",
        "to": "SYNC",
        "type": "arrow",
        "label": "repair: re-inject persona"
      }
    ],
    "callout_boxes": [
      {
        "heading": "EWMA SMOOTHING PREVENTS FALSE POSITIVES WHILE CATCHING SUSTAINED DRIFT",
        "body_text": "Single-turn anomalies are absorbed by smoothing. Only sustained multi-turn drift crosses the threshold and triggers persona repair.",
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
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
