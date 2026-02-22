# fig-voice-47: Evaluation Metrics & Traces

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-47 |
| **Title** | Evaluation Metrics & Traces |
| **Audience** | L4 (AI/ML Architect) |
| **Location** | docs/tutorials/voice-agent-implementation.md, Section 10.1 |
| **Priority** | P2 (Nice-to-have) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Show 4 G-Eval dimensions with target scores, and a PersonaGym multi-turn trace showing drift over 20 turns. Show how CI integrates evaluation. Answers: "How do we measure voice agent quality, and when does persona degrade?"

## Key Message

Voice agent quality is measured across 4 G-Eval dimensions (Task Completion >90%, Confidence Communication >85%, Persona Consistency >90%, Voice-Appropriateness >80%), with PersonaGym providing multi-turn drift traces that reveal the 8-turn cliff.

## Visual Concept

Split-panel (Template D). Left panel: "G-EVAL DIMENSIONS" showing 4 horizontal bar gauges with target thresholds marked as vertical lines. Right panel: "PERSONAGYM TRACE" showing a line graph of persona consistency over 20 turns, with the 8-turn cliff annotated and a reference to Li et al., 2024. Below both panels: CI integration flow showing cadence for each evaluation type.

```
+-----------------------------------------------------------------------+
|  EVALUATION METRICS & TRACES                                     [sq]  |
|  -- G-Eval Dimensions + PersonaGym Multi-Turn Drift                    |
+-----------------------------------------------------------------------+
|                                                                        |
|  G-EVAL DIMENSIONS                  PERSONAGYM TRACE                   |
|  ─────────────────                  ────────────────                   |
|                                                                        |
|  Task Completion                    1.0 ┐                              |
|  ████████████████████░░ >90%             │ ─────────\                  |
|                                     0.9 ┤           \  8-turn cliff   |
|  Confidence Communication                │            \ (Li et al.)   |
|  ██████████████████░░░░ >85%        0.8 ┤             \────           |
|                                          │                  \──        |
|  Persona Consistency                0.7 ┤                     ──      |
|  ████████████████████░░ >90%             │                      ──    |
|                                     0.6 ┤                        ─── |
|  Voice-Appropriateness                   │                            |
|  ████████████████░░░░░░ >80%        0.5 ┤─────────────────────────   |
|                                          1  4  8  12  16  20          |
|                                          Turn Number                  |
|                                                                        |
|  ─────────────────────────────────────────── [accent line]            |
|                                                                        |
|  CI INTEGRATION CADENCE                                                |
|  Every push: unit tests (config, persona, drift)                      |
|  Weekly:     G-Eval persona evaluation (requires API key)             |
|  Monthly:    PersonaGym multi-turn (requires API key)                 |
|                                                                        |
+-----------------------------------------------------------------------+
|  ELI5: A music teacher's report card with four grades --         [sq]  |
|  right notes, dynamics, staying in character, projecting.              |
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
    content: "EVALUATION METRICS & TRACES"
    role: title

  - id: left_panel
    bounds: [40, 140, 880, 520]
    content: "G-EVAL DIMENSIONS"
    role: content_area

  - id: right_panel
    bounds: [960, 140, 920, 520]
    content: "PERSONAGYM TRACE"
    role: content_area

  - id: ci_zone
    bounds: [40, 720, 1840, 180]
    content: "CI INTEGRATION CADENCE"
    role: content_area

  - id: callout_zone
    bounds: [40, 940, 1840, 100]
    content: "ELI5: A music teacher's report card"
    role: callout_box

anchors:
  - id: geval_heading
    position: [440, 170]
    size: [400, 40]
    role: heading_display
    label: "G-EVAL DIMENSIONS"

  - id: bar_task
    position: [440, 260]
    size: [700, 50]
    role: data_flow
    label: "Task Completion >90%"

  - id: bar_confidence
    position: [440, 340]
    size: [700, 50]
    role: data_flow
    label: "Confidence Comm. >85%"

  - id: bar_persona
    position: [440, 420]
    size: [700, 50]
    role: data_flow
    label: "Persona Consistency >90%"

  - id: bar_voice
    position: [440, 500]
    size: [700, 50]
    role: data_flow
    label: "Voice-Appropriateness >80%"

  - id: personagym_heading
    position: [1400, 170]
    size: [400, 40]
    role: heading_display
    label: "PERSONAGYM TRACE"

  - id: trace_graph
    position: [1400, 400]
    size: [800, 360]
    role: data_flow
    label: "Persona consistency over 20 turns"

  - id: cliff_annotation
    position: [1440, 320]
    size: [200, 40]
    role: callout_box
    label: "8-turn cliff (Li et al.)"

  - id: divider_ci
    position: [40, 700]
    size: [1840, 2]
    role: accent_line

  - id: ci_push
    position: [300, 780]
    size: [400, 40]
    role: processing_stage
    label: "Every push: unit tests"

  - id: ci_weekly
    position: [800, 780]
    size: [400, 40]
    role: processing_stage
    label: "Weekly: G-Eval"

  - id: ci_monthly
    position: [1300, 780]
    size: [400, 40]
    role: processing_stage
    label: "Monthly: PersonaGym"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "EVALUATION METRICS & TRACES" with coral accent square |
| G-Eval heading | `heading_display` | "G-EVAL DIMENSIONS" left panel header |
| Task Completion bar | `data_flow` | Horizontal bar gauge, target >90% |
| Confidence Communication bar | `data_flow` | Horizontal bar gauge, target >85% |
| Persona Consistency bar | `data_flow` | Horizontal bar gauge, target >90% |
| Voice-Appropriateness bar | `data_flow` | Horizontal bar gauge, target >80% |
| PersonaGym heading | `heading_display` | "PERSONAGYM TRACE" right panel header |
| Trace line graph | `data_flow` | Persona consistency score (0-1) over 20 turns |
| 8-turn cliff annotation | `callout_box` | Annotation marking degradation start at turn ~8, citing Li et al., 2024 |
| CI integration section | `processing_stage` | Three cadence levels: every push, weekly, monthly |
| Divider line | `accent_line` | Coral accent line separating panels from CI section |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Unit tests | Every push | arrow | "config, persona, drift" |
| G-Eval | Weekly | arrow | "requires API key" |
| PersonaGym | Monthly | arrow | "requires API key" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Evaluation is like a music teacher's report card with four grades: Did the student play the right notes (task completion)? Did they express dynamics correctly (confidence)? Did they stay in character for the whole recital (persona consistency)? Were they projecting to the back row (voice-appropriateness)? | bottom-center |
| "8-TURN CLIFF" | PersonaGym traces show persona consistency degrades sharply after ~8 turns without reinforcement (Li et al., 2024) | right-panel-annotation |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "G-EVAL DIMENSIONS"
- Label 2: "PERSONAGYM TRACE"
- Label 3: "Task Completion >90%"
- Label 4: "Confidence Comm. >85%"
- Label 5: "Persona Consistency >90%"
- Label 6: "Voice-Appropriateness >80%"
- Label 7: "8-turn cliff (Li et al.)"
- Label 8: "Persona consistency score"
- Label 9: "Turn Number (1-20)"
- Label 10: "Every push: unit tests"
- Label 11: "Weekly: G-Eval"
- Label 12: "Monthly: PersonaGym"
- Label 13: "CI INTEGRATION CADENCE"
- Label 14: "requires API key"

### Caption (for embedding in documentation)

Split-panel evaluation overview showing 4 G-Eval dimensions (Task Completion >90%, Confidence Communication >85%, Persona Consistency >90%, Voice-Appropriateness >80%) alongside a PersonaGym multi-turn trace revealing the 8-turn persona consistency cliff, with CI cadence for each evaluation tier.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `data_flow`, `callout_box` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon is ALLOWED** -- "G-Eval", "PersonaGym", "EWMA", "conformal prediction" are appropriate for L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text in the figure.

### Figure-Specific Rules

9. Target scores must match values from Section 10.1: Task Completion >90%, Confidence Communication >85%, Persona Consistency >90%, Voice-Appropriateness >80%.
10. The PersonaGym trace should show a conceptual drift pattern with visible degradation, not fabricated experimental data points.
11. The 8-turn cliff annotation must reference Li et al., 2024.
12. CI cadence (every push / weekly / monthly) must match Section 10.3 of the implementation guide.

## Alt Text

Split-panel: four G-Eval bars with targets plus PersonaGym 20-turn trace showing 8-turn persona cliff, with CI cadence below.

## Image Embed

![Split-panel: four G-Eval bars with targets plus PersonaGym 20-turn trace showing 8-turn persona cliff, with CI cadence below.](docs/figures/repo-figures/assets/fig-voice-47-evaluation-metrics-traces.jpg)

*Split-panel evaluation overview showing 4 G-Eval dimensions (Task Completion >90%, Confidence Communication >85%, Persona Consistency >90%, Voice-Appropriateness >80%) alongside a PersonaGym multi-turn trace revealing the 8-turn persona consistency cliff, with CI cadence for each evaluation tier.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-47",
    "title": "Evaluation Metrics & Traces",
    "audience": "L4",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Voice agent quality is measured across 4 G-Eval dimensions with PersonaGym multi-turn traces revealing the 8-turn persona consistency cliff.",
    "layout_flow": "left-right-split",
    "key_structures": [
      {
        "name": "Task Completion",
        "role": "data_flow",
        "is_highlighted": true,
        "labels": ["Task Completion >90%"]
      },
      {
        "name": "Confidence Communication",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["Confidence Comm. >85%"]
      },
      {
        "name": "Persona Consistency",
        "role": "data_flow",
        "is_highlighted": true,
        "labels": ["Persona Consistency >90%"]
      },
      {
        "name": "Voice-Appropriateness",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["Voice-Appropriateness >80%"]
      },
      {
        "name": "PersonaGym Trace",
        "role": "data_flow",
        "is_highlighted": true,
        "labels": ["Persona consistency over 20 turns", "8-turn cliff"]
      },
      {
        "name": "CI Integration",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["Every push: unit tests", "Weekly: G-Eval", "Monthly: PersonaGym"]
      }
    ],
    "relationships": [
      {"from": "Unit tests", "to": "Every push", "type": "arrow", "label": "config, persona, drift"},
      {"from": "G-Eval", "to": "Weekly", "type": "arrow", "label": "requires API key"},
      {"from": "PersonaGym", "to": "Monthly", "type": "arrow", "label": "requires API key"}
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Evaluation is like a music teacher's report card with four grades: Did the student play the right notes (task completion)? Did they express dynamics correctly (confidence)? Did they stay in character for the whole recital (persona consistency)? Were they projecting to the back row (voice-appropriateness)?",
        "position": "bottom-center"
      },
      {
        "heading": "8-TURN CLIFF",
        "body_text": "PersonaGym traces show persona consistency degrades sharply after ~8 turns without reinforcement (Li et al., 2024)",
        "position": "right-panel"
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
- [x] Anti-hallucination rules listed (8 default + 4 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L4)
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
