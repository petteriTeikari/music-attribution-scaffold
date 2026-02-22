# fig-voice-37: EWMA Drift State Machine

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-37 |
| **Title** | EWMA Drift State Machine |
| **Audience** | L4 (AI/ML Architect) |
| **Location** | docs/tutorials/voice-agent-implementation.md, Section 9.2 |
| **Priority** | P1 (Important) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Show three states (sync/drift/desync) with transition thresholds, EWMA formula, and restoring force arrows. State machines demand visual representation -- prose cannot convey bidirectional transitions and threshold boundaries simultaneously. Answers: "How does the drift detector decide when the agent has strayed too far, and what pulls it back?"

## Key Message

The drift detector implements a three-state bounded equilibrium: sync (>=0.85) <-> drift (0.70-0.85) <-> desync (<0.70), with EWMA smoothing preventing false alarms and periodic reinforcement providing the restoring force.

## Visual Concept

Flowchart (Template C). Three large state circles arranged horizontally: SYNC (left), DRIFT (center), DESYNC (right). Bidirectional arrows between adjacent states with threshold labels on each arrow. Above the states: the EWMA formula (score_t = alpha * raw_t + (1 - alpha) * score_{t-1}). Below DRIFT state: "RESTORING FORCE: Inject reinforcement prompt" with a curved arrow pointing back toward SYNC. Callout box with the ELI5 explanation at bottom.

```
+-------------------------------------------------------------------+
|  EWMA DRIFT STATE MACHINE                                    [sq]   |
|  -- Three-State Bounded Equilibrium                                |
+-------------------------------------------------------------------+
|                                                                    |
|  EWMA FORMULA                                                      |
|  score_t = alpha * raw_t + (1 - alpha) * score_{t-1}               |
|  alpha = 0.3 (smoothing factor)                                    |
|                                                                    |
|  ─────────────────────────────────────────────── [accent line]     |
|                                                                    |
|      SYNC               DRIFT               DESYNC                |
|   (>= 0.85)          (0.70-0.85)           (< 0.70)              |
|  ┌──────────┐       ┌──────────┐        ┌──────────┐             |
|  │           │       │           │        │           │             |
|  │  Agent    │ <0.85 │  Warning  │ <0.70  │  Alert    │             |
|  │  on-      │──────>│  inject   │──────> │  full     │             |
|  │  persona  │       │  reinforce│        │  context   │             |
|  │  no action│<──────│  prompt   │<────── │  recalib.  │             |
|  │           │ >0.85 │           │ >0.70  │           │             |
|  └──────────┘       └──────────┘        └──────────┘             |
|                            │                                       |
|                            │                                       |
|                     ┌──────┴──────┐                                |
|                     │  RESTORING   │                                |
|                     │  FORCE:      │                                |
|                     │  Inject      │                                |
|                     │  reinforcement                                |
|                     │  prompt      │───────> (curves to SYNC)      |
|                     └─────────────┘                                |
|                                                                    |
+-------------------------------------------------------------------+
|  ELI5: Like a click track nudging a session musician back to       |
|  the chart when they drift into jazz improvisation                 |
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
    content: "EWMA DRIFT STATE MACHINE"
    role: title

  - id: formula_zone
    bounds: [60, 140, 1800, 100]
    content: "score_t = alpha * raw_t + (1 - alpha) * score_{t-1}"
    role: content_area

  - id: states_zone
    bounds: [60, 280, 1800, 400]
    role: content_area

  - id: restoring_zone
    bounds: [560, 700, 600, 140]
    role: content_area

  - id: callout_zone
    bounds: [60, 940, 1800, 100]
    content: "ELI5: Like a click track nudging a session musician back"
    role: callout_box

anchors:
  - id: formula_display
    position: [960, 180]
    size: [1000, 60]
    role: data_mono
    label: "score_t = alpha * raw_t + (1-alpha) * score_{t-1}"

  - id: state_sync
    position: [320, 460]
    size: [340, 280]
    role: processing_stage
    label: "SYNC (>= 0.85)"

  - id: state_drift
    position: [860, 460]
    size: [340, 280]
    role: processing_stage
    label: "DRIFT (0.70-0.85)"

  - id: state_desync
    position: [1400, 460]
    size: [340, 280]
    role: security_layer
    label: "DESYNC (< 0.70)"

  - id: arrow_sync_to_drift
    from: state_sync
    to: state_drift
    type: arrow
    label: "EWMA < 0.85"

  - id: arrow_drift_to_sync
    from: state_drift
    to: state_sync
    type: arrow
    label: "EWMA > 0.85"

  - id: arrow_drift_to_desync
    from: state_drift
    to: state_desync
    type: arrow
    label: "EWMA < 0.70"

  - id: arrow_desync_to_drift
    from: state_desync
    to: state_drift
    type: arrow
    label: "EWMA > 0.70"

  - id: restoring_force
    position: [860, 760]
    size: [400, 100]
    role: feedback_loop
    label: "RESTORING FORCE"

  - id: restoring_curve
    from: restoring_force
    to: state_sync
    type: curved_arrow
    label: "inject reinforcement prompt"

  - id: divider_formula_states
    position: [60, 250]
    size: [1800, 2]
    role: accent_line
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "EWMA DRIFT STATE MACHINE" with coral accent square |
| EWMA formula | `data_mono` | score_t = alpha * raw_t + (1 - alpha) * score_{t-1}, alpha = 0.3 |
| SYNC state | `processing_stage` | >= 0.85. Agent on-persona, no action needed. |
| DRIFT state | `processing_stage` | 0.70-0.85. Warning state, inject reinforcement prompt. |
| DESYNC state | `security_layer` | < 0.70. Alert state, full context recalibration. |
| Restoring force box | `feedback_loop` | "Inject reinforcement prompt" with curved arrow back to SYNC |
| Formula divider | `accent_line` | Coral line separating formula from state diagram |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| SYNC | DRIFT | arrow | "EWMA drops below 0.85" |
| DRIFT | SYNC | arrow | "EWMA rises above 0.85" |
| DRIFT | DESYNC | arrow | "EWMA drops below 0.70" |
| DESYNC | DRIFT | arrow | "EWMA rises above 0.70" |
| Restoring force | SYNC | curved_arrow | "inject reinforcement prompt" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Imagine a session musician who starts playing your song but gradually drifts into jazz improvisation. The drift detector is like a click track -- it notices when the player strays too far from the chart and gives them a nudge back to the arrangement. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "SYNC (>= 0.85)"
- Label 2: "DRIFT (0.70-0.85)"
- Label 3: "DESYNC (< 0.70)"
- Label 4: "EWMA drops below 0.85"
- Label 5: "EWMA rises above 0.85"
- Label 6: "EWMA drops below 0.70"
- Label 7: "EWMA rises above 0.70"
- Label 8: "Agent on-persona, no action"
- Label 9: "Warning, inject reinforce"
- Label 10: "Alert, full recalibration"
- Label 11: "RESTORING FORCE"
- Label 12: "Inject reinforcement prompt"
- Label 13: "alpha = 0.3"

### Caption (for embedding in documentation)

Three-state EWMA drift detector for voice agent persona monitoring -- sync (>=0.85), drift (0.70-0.85), and desync (<0.70) with bidirectional transitions, exponentially weighted moving average smoothing, and a restoring force that injects reinforcement prompts to pull drifting agents back on-persona.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `security_layer`, `feedback_loop` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon is ALLOWED** -- this is an L4 figure targeting AI/ML architects. EWMA, alpha, state machine, recalibration are appropriate.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. The three states must be labeled sync/drift/desync matching the DriftState enum in the codebase.
10. Threshold values (0.85, 0.70) must be shown on transition arrows, not inside states.
11. The EWMA formula must use Greek alpha (alpha), not the word "alpha" -- render as the mathematical symbol.
12. The restoring force arrow must visually indicate that drift to sync transitions are actively assisted by reinforcement prompts, not just passive threshold crossing.
13. Bidirectional arrows between adjacent states must be visually distinct (not overlapping single lines).
14. The DESYNC state must appear visually more severe than DRIFT (different semantic weight).

## Alt Text

Three-state EWMA drift detector: sync at 0.85 threshold, drift with reinforcement restoring force, desync at 0.70 triggering full recalibration.

## Image Embed

![Three-state EWMA drift detector: sync at 0.85 threshold, drift with reinforcement restoring force, desync at 0.70 triggering full recalibration.](docs/figures/repo-figures/assets/fig-voice-37-ewma-drift-state-machine.jpg)

*Three-state EWMA drift detector for voice agent persona monitoring -- sync (>=0.85), drift (0.70-0.85), and desync (<0.70) with bidirectional transitions, exponentially weighted moving average smoothing, and a restoring force that injects reinforcement prompts to pull drifting agents back on-persona.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-37",
    "title": "EWMA Drift State Machine",
    "audience": "L4",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "The drift detector implements a three-state bounded equilibrium: sync (>=0.85), drift (0.70-0.85), desync (<0.70), with EWMA smoothing and reinforcement-prompt restoring force.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "EWMA Formula",
        "role": "data_mono",
        "is_highlighted": false,
        "labels": ["score_t = alpha * raw_t + (1-alpha) * score_{t-1}", "alpha = 0.3"]
      },
      {
        "name": "SYNC State",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["SYNC (>= 0.85)", "Agent on-persona", "No action"]
      },
      {
        "name": "DRIFT State",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["DRIFT (0.70-0.85)", "Warning", "Inject reinforcement"]
      },
      {
        "name": "DESYNC State",
        "role": "security_layer",
        "is_highlighted": false,
        "labels": ["DESYNC (< 0.70)", "Alert", "Full recalibration"]
      },
      {
        "name": "Restoring Force",
        "role": "feedback_loop",
        "is_highlighted": true,
        "labels": ["RESTORING FORCE", "Inject reinforcement prompt"]
      }
    ],
    "relationships": [
      {
        "from": "SYNC",
        "to": "DRIFT",
        "type": "arrow",
        "label": "EWMA < 0.85"
      },
      {
        "from": "DRIFT",
        "to": "SYNC",
        "type": "arrow",
        "label": "EWMA > 0.85"
      },
      {
        "from": "DRIFT",
        "to": "DESYNC",
        "type": "arrow",
        "label": "EWMA < 0.70"
      },
      {
        "from": "DESYNC",
        "to": "DRIFT",
        "type": "arrow",
        "label": "EWMA > 0.70"
      },
      {
        "from": "Restoring Force",
        "to": "SYNC",
        "type": "curved_arrow",
        "label": "reinforcement prompt"
      }
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Like a click track nudging a session musician back to the chart when they drift into jazz improvisation.",
        "position": "bottom-center"
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
- [x] Anti-hallucination rules listed (8 default + 6 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L4)
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
