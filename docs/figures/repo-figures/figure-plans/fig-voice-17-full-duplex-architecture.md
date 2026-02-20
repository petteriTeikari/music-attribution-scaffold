# fig-voice-17: Full-Duplex Voice: Listen While Speaking

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-17 |
| **Title** | Full-Duplex Voice: Listen While Speaking |
| **Audience** | L4 (Researcher / Deep Technical) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Show the fundamental architectural difference between half-duplex (traditional turn-based) and full-duplex (simultaneous listen+speak with backchanneling) voice interaction. Answers: "What does full-duplex voice interaction look like architecturally, and which models have achieved it?"

## Key Message

Full-duplex voice eliminates the walkie-talkie paradigm -- the agent can listen while speaking, enabling natural backchanneling ("mm-hmm"), mid-sentence corrections, and overlapping speech, with Moshi achieving 200ms round-trip as the first real-time full-duplex spoken LLM.

## Visual Concept

Split-panel (Template D). Left panel: "HALF-DUPLEX" showing a sequential timeline where User speaks then Agent speaks then User speaks -- a walkie-talkie pattern with visible gaps labeled "silence/wait." Right panel: "FULL-DUPLEX" showing overlapping timelines where both user and agent audio streams run simultaneously, with backchanneling signals ("mm-hmm", "right") interspersed. Below, model cards for Moshi (200ms, dual-stream), SALMONN-omni (codec-free), and PersonaPlex (NVIDIA multi-party).

```
+-------------------------------------------------------------------+
|  FULL-DUPLEX VOICE                                         [sq]   |
|  LISTEN WHILE SPEAKING                                            |
+-------------------------------+-----------------------------------+
|                               |                                   |
|  HALF-DUPLEX (traditional)    |  FULL-DUPLEX (simultaneous)       |
|                               |                                   |
|  User:  ████████░░░░░░░░░░   |  User:  ████████░░████░░████      |
|  Agent: ░░░░░░░░████████░░   |  Agent: ░░░░████████░░████░░      |
|         <wait>  <wait>        |         ^^    ^^                  |
|                               |         backchannel               |
|  ■ One speaks, other waits   |  ■ Both streams simultaneous      |
|  ■ Visible gaps / silence    |  ■ "mm-hmm", "right" overlaps     |
|  ■ Walkie-talkie paradigm    |  ■ Natural conversation flow      |
|  ■ 500ms+ turn gaps          |  ■ Mid-sentence correction        |
|                               |                                   |
+-------------------------------+-----------------------------------+
|  MODELS ACHIEVING FULL-DUPLEX                                     |
|  ■ Moshi (Kyutai): 200ms round-trip, dual-stream Mimi codec      |
|  ■ SALMONN-omni: codec-free, continuous audio tokens              |
|  ■ PersonaPlex (NVIDIA): multi-party full-duplex, interruption    |
+-------------------------------------------------------------------+
|  "MOSHI: 200ms ROUND-TRIP — first real-time full-duplex           |
|   spoken LLM"                                        [accent line] |
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
    content: "FULL-DUPLEX VOICE"
    role: title

  - id: left_panel
    bounds: [40, 140, 900, 480]
    content: "HALF-DUPLEX"
    role: content_area

  - id: right_panel
    bounds: [980, 140, 900, 480]
    content: "FULL-DUPLEX"
    role: content_area

  - id: divider
    bounds: [940, 140, 2, 480]
    role: accent_line_v

  - id: models_zone
    bounds: [40, 660, 1840, 220]
    content: "MODELS ACHIEVING FULL-DUPLEX"
    role: content_area

  - id: callout_zone
    bounds: [40, 920, 1840, 120]
    content: "MOSHI: 200ms ROUND-TRIP"
    role: callout_box

anchors:
  - id: half_duplex_user_timeline
    position: [80, 200]
    size: [820, 60]
    role: data_flow
    label: "User audio (sequential)"

  - id: half_duplex_agent_timeline
    position: [80, 300]
    size: [820, 60]
    role: data_flow
    label: "Agent audio (sequential)"

  - id: full_duplex_user_timeline
    position: [1020, 200]
    size: [860, 60]
    role: data_flow
    label: "User audio (continuous)"

  - id: full_duplex_agent_timeline
    position: [1020, 300]
    size: [860, 60]
    role: data_flow
    label: "Agent audio (continuous)"

  - id: backchannel_markers
    position: [1020, 360]
    size: [860, 40]
    role: annotation
    label: "Backchannel signals"

  - id: model_moshi
    position: [80, 700]
    size: [540, 140]
    role: processing_stage
    label: "Moshi (Kyutai)"

  - id: model_salmonn
    position: [660, 700]
    size: [540, 140]
    role: processing_stage
    label: "SALMONN-omni"

  - id: model_personaplex
    position: [1240, 700]
    size: [540, 140]
    role: processing_stage
    label: "PersonaPlex (NVIDIA)"

  - id: half_duplex_gap
    from: half_duplex_user_timeline
    to: half_duplex_agent_timeline
    type: dashed
    label: "wait / silence gap"

  - id: full_duplex_overlap
    from: full_duplex_user_timeline
    to: full_duplex_agent_timeline
    type: bidirectional
    label: "simultaneous streams"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Half-Duplex Panel | `branching_path` | Traditional turn-based: one speaks while other waits, walkie-talkie paradigm |
| Full-Duplex Panel | `selected_option` | Simultaneous listen+speak with backchanneling and overlap |
| User Timeline (half) | `data_flow` | Sequential user audio blocks with gaps |
| Agent Timeline (half) | `data_flow` | Sequential agent audio blocks with gaps |
| User Timeline (full) | `data_flow` | Continuous user audio with overlaps |
| Agent Timeline (full) | `data_flow` | Continuous agent audio with backchannels |
| Backchannel Markers | `annotation` | "mm-hmm", "right" signals during user speech |
| Moshi Card | `processing_stage` | Kyutai, 200ms round-trip, dual-stream Mimi codec |
| SALMONN-omni Card | `processing_stage` | Codec-free, continuous audio token approach |
| PersonaPlex Card | `processing_stage` | NVIDIA multi-party full-duplex with interruption handling |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| User Timeline (half) | Agent Timeline (half) | dashed | "wait / silence gap" |
| Agent Timeline (half) | User Timeline (half) | dashed | "wait / silence gap" |
| User Timeline (full) | Agent Timeline (full) | bidirectional | "simultaneous streams" |
| Backchannel Markers | Agent Timeline (full) | arrow | "backchannel overlay" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "MOSHI: 200ms ROUND-TRIP" | First real-time full-duplex spoken LLM. Dual-stream architecture with Mimi neural codec enables listening while generating speech, achieving 200ms end-to-end latency. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "HALF-DUPLEX"
- Label 2: "FULL-DUPLEX"
- Label 3: "User speaks"
- Label 4: "Agent speaks"
- Label 5: "wait / silence gap"
- Label 6: "simultaneous streams"
- Label 7: "backchannel: mm-hmm"
- Label 8: "mid-sentence correction"
- Label 9: "Moshi (Kyutai)"
- Label 10: "200ms round-trip"
- Label 11: "dual-stream Mimi codec"
- Label 12: "SALMONN-omni"
- Label 13: "codec-free audio tokens"
- Label 14: "PersonaPlex (NVIDIA)"
- Label 15: "multi-party full-duplex"
- Label 16: "walkie-talkie paradigm"

### Caption (for embedding in documentation)

Split-panel comparing half-duplex turn-based voice interaction with full-duplex simultaneous listen-and-speak architecture, featuring Moshi (200ms round-trip), SALMONN-omni (codec-free), and PersonaPlex (multi-party) as representative full-duplex models.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `data_flow`, `branching_path` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Moshi's 200ms round-trip latency is from Kyutai's published benchmarks (2024). Do NOT alter this value.
10. Moshi uses Mimi, a neural audio codec with dual-stream architecture (one for listening, one for generating). Do NOT describe it as a standard codec.
11. SALMONN-omni is codec-free -- it processes continuous audio tokens directly without a separate neural codec stage.
12. PersonaPlex is NVIDIA's multi-party full-duplex system -- it handles multiple simultaneous speakers, not just two-party.
13. The half-duplex panel must show visible gaps/silence between turns to emphasize the walkie-talkie problem.
14. The full-duplex panel must show overlapping audio blocks to visualize simultaneous operation.
15. Backchanneling ("mm-hmm", "right", "I see") is a key feature of full-duplex -- it must be visually labeled on the right panel.
16. Do NOT imply full-duplex is universally better -- it adds complexity and is harder to evaluate.

## Alt Text

Split-panel diagram comparing half-duplex turn-based voice interaction (walkie-talkie paradigm with silence gaps) versus full-duplex simultaneous listen-and-speak architecture with backchanneling, featuring Moshi (200ms round-trip), SALMONN-omni, and PersonaPlex models.

## Image Embed

![Split-panel diagram comparing half-duplex turn-based voice interaction (walkie-talkie paradigm with silence gaps) versus full-duplex simultaneous listen-and-speak architecture with backchanneling, featuring Moshi (200ms round-trip), SALMONN-omni, and PersonaPlex models.](docs/figures/repo-figures/assets/fig-voice-17-full-duplex-architecture.jpg)

*Split-panel comparing half-duplex turn-based voice interaction with full-duplex simultaneous listen-and-speak architecture, featuring Moshi (200ms round-trip), SALMONN-omni (codec-free), and PersonaPlex (multi-party) as representative full-duplex models.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-17",
    "title": "Full-Duplex Voice: Listen While Speaking",
    "audience": "L4",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Full-duplex voice eliminates the walkie-talkie paradigm, enabling simultaneous listen+speak with backchanneling, led by Moshi at 200ms round-trip.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Half-Duplex Panel",
        "role": "branching_path",
        "is_highlighted": false,
        "labels": ["HALF-DUPLEX", "walkie-talkie paradigm", "500ms+ turn gaps"]
      },
      {
        "name": "Full-Duplex Panel",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["FULL-DUPLEX", "simultaneous streams", "backchanneling"]
      },
      {
        "name": "Moshi",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Moshi (Kyutai)", "200ms round-trip", "dual-stream Mimi codec"]
      },
      {
        "name": "SALMONN-omni",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["SALMONN-omni", "codec-free audio tokens"]
      },
      {
        "name": "PersonaPlex",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["PersonaPlex (NVIDIA)", "multi-party full-duplex"]
      }
    ],
    "relationships": [
      {
        "from": "User Timeline (half)",
        "to": "Agent Timeline (half)",
        "type": "dashed",
        "label": "wait / silence gap"
      },
      {
        "from": "User Timeline (full)",
        "to": "Agent Timeline (full)",
        "type": "bidirectional",
        "label": "simultaneous streams"
      },
      {
        "from": "Backchannel Markers",
        "to": "Agent Timeline (full)",
        "type": "arrow",
        "label": "backchannel overlay"
      }
    ],
    "callout_boxes": [
      {
        "heading": "MOSHI: 200ms ROUND-TRIP",
        "body_text": "First real-time full-duplex spoken LLM. Dual-stream architecture with Mimi neural codec enables listening while generating speech.",
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
- [ ] Audience level correct (L4)
- [ ] Layout template identified (D)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
