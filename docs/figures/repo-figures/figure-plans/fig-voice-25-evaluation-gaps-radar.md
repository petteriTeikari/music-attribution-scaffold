# fig-voice-25: What Voice Agent Leaderboards Miss

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-25 |
| **Title** | What Voice Agent Leaderboards Miss |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/tutorials/voice-agent-implementation.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Expose the blind spots in current voice agent evaluation frameworks by visualizing ten critical evaluation dimensions as a radar/spider chart. Current leaderboards (e.g., TTS Arena, Chatbot Arena Voice) test only 2-3 dimensions (WER, MOS, task completion), leaving 8 dimensions -- including accent bias, cost-quality trade-offs, safety, and graceful recovery -- completely untested. Answers: "Are current voice agent benchmarks sufficient for production deployment in music attribution?"

## Key Message

Current voice agent leaderboards cover only 2-3 of 10 critical evaluation dimensions. Eight dimensions essential for production voice agents -- accent bias, cross-session consistency, cost-quality Pareto efficiency, emotional appropriateness, safety/jailbreak resistance, multi-party handling, graceful recovery, and noise robustness -- are untested by any major benchmark.

## Visual Concept

Radar/spider chart with 10 axes radiating from center. A filled polygon covers the 2-3 axes that current leaderboards evaluate (WER, MOS, task completion) -- this area is small. The empty area reveals the 8 untested dimensions. Each axis is labeled. A second dashed polygon shows the "ideal evaluation coverage" at full extent. The contrast between the tiny filled area and the vast empty space is the visual argument.

```
+-------------------------------------------------------------------+
|  WHAT VOICE AGENT LEADERBOARDS MISS                         [sq]   |
|  -- Evaluation Coverage Gaps                                       |
+-------------------------------------------------------------------+
|                                                                    |
|                        NOISE ROBUSTNESS                            |
|                              |                                     |
|              GRACEFUL        |       WER / ACCURACY                |
|              RECOVERY    .../|\.....                                |
|                      ..'    |    '..                               |
|                   .'   ┌────┼────┐  '.                             |
|  MULTI-PARTY ----'     │////|////│    '--- MOS / QUALITY           |
|              \    ┌────│////|////│────┐   /                        |
|               \   │    │////|////│    │  /                          |
|                \  │    └────┼────┘    │ /                           |
|  SAFETY /       \ │        |         │/    TASK COMPLETION         |
|  JAILBREAK ------\│........|.........│                             |
|                   '\       |       /'                               |
|                     '.     |     .'                                 |
|  EMOTIONAL             '.. | ..'        COST-QUALITY               |
|  APPROPRIATENESS          \|/           TRADE-OFF                  |
|                             |                                      |
|                   CROSS-SESSION                                    |
|                   CONSISTENCY                                      |
|                                                                    |
|        ┌──────┐                                                    |
|        │//////│ = Current leaderboard coverage (2-3 dimensions)    |
|        └──────┘                                                    |
|        ┌──────┐                                                    |
|        │......│ = Ideal evaluation coverage (all 10 dimensions)    |
|        └──────┘                                                    |
|                                                                    |
+-------------------------------------------------------------------+
|  8 OF 10 CRITICAL DIMENSIONS ARE UNTESTED BY ANY LEADERBOARD       |
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
    content: "WHAT VOICE AGENT LEADERBOARDS MISS"
    role: title

  - id: radar_zone
    bounds: [200, 140, 1520, 720]
    role: content_area

  - id: legend_zone
    bounds: [80, 780, 600, 120]
    role: content_area

  - id: callout_zone
    bounds: [60, 940, 1800, 100]
    content: "8 OF 10 CRITICAL DIMENSIONS ARE UNTESTED"
    role: callout_box

anchors:
  - id: radar_center
    position: [960, 480]
    size: [40, 40]
    role: data_flow
    label: "center"

  - id: axis_wer
    position: [1120, 220]
    size: [200, 40]
    role: processing_stage
    label: "WER / Accuracy"

  - id: axis_mos
    position: [1340, 380]
    size: [200, 40]
    role: processing_stage
    label: "MOS / Quality"

  - id: axis_task
    position: [1340, 580]
    size: [200, 40]
    role: processing_stage
    label: "Task Completion"

  - id: axis_cost
    position: [1200, 720]
    size: [200, 40]
    role: warning_box
    label: "Cost-Quality Trade-off"

  - id: axis_cross_session
    position: [960, 780]
    size: [200, 40]
    role: warning_box
    label: "Cross-Session Consistency"

  - id: axis_emotional
    position: [680, 720]
    size: [200, 40]
    role: warning_box
    label: "Emotional Appropriateness"

  - id: axis_safety
    position: [540, 580]
    size: [200, 40]
    role: warning_box
    label: "Safety / Jailbreak"

  - id: axis_multi_party
    position: [540, 380]
    size: [200, 40]
    role: warning_box
    label: "Multi-Party Handling"

  - id: axis_recovery
    position: [680, 220]
    size: [200, 40]
    role: warning_box
    label: "Graceful Recovery"

  - id: axis_noise
    position: [960, 160]
    size: [200, 40]
    role: warning_box
    label: "Noise Robustness"

  - id: covered_polygon
    position: [960, 480]
    size: [300, 300]
    role: selected_option
    label: "Current coverage (filled)"

  - id: ideal_polygon
    position: [960, 480]
    size: [600, 600]
    role: deferred_option
    label: "Ideal coverage (dashed)"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "WHAT VOICE AGENT LEADERBOARDS MISS" with coral accent square |
| Radar chart | `module_grid` | 10-axis spider chart centered in canvas |
| Covered polygon (filled) | `selected_option` | Small filled area covering WER, MOS, task completion axes only |
| Ideal polygon (dashed) | `deferred_option` | Full dashed polygon extending to all 10 axes |
| WER axis | `processing_stage` | Word Error Rate -- tested by leaderboards |
| MOS axis | `processing_stage` | Mean Opinion Score -- tested by leaderboards |
| Task Completion axis | `processing_stage` | Task success rate -- tested by leaderboards |
| Cost-Quality axis | `warning_box` | Cost-quality Pareto efficiency -- UNTESTED |
| Cross-Session axis | `warning_box` | Consistency across multiple sessions -- UNTESTED |
| Emotional axis | `warning_box` | Emotional tone appropriateness -- UNTESTED |
| Safety axis | `warning_box` | Jailbreak and safety resistance -- UNTESTED |
| Multi-Party axis | `warning_box` | Multi-speaker conversation handling -- UNTESTED |
| Recovery axis | `warning_box` | Graceful error recovery and fallback -- UNTESTED |
| Noise axis | `warning_box` | Robustness to background noise -- UNTESTED |
| Legend | `label_editorial` | Two legend entries: filled = current, dashed = ideal |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Covered polygon | WER axis | arrow | "tested" |
| Covered polygon | MOS axis | arrow | "tested" |
| Covered polygon | Task Completion axis | arrow | "tested" |
| Ideal polygon | All 10 axes | dashed | "required for production" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "8 OF 10 CRITICAL DIMENSIONS ARE UNTESTED BY ANY LEADERBOARD" | Current benchmarks (TTS Arena, Chatbot Arena Voice) focus on quality and accuracy. Production voice agents require evaluation of cost, safety, robustness, and social dimensions. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "WER / ACCURACY"
- Label 2: "MOS / QUALITY"
- Label 3: "TASK COMPLETION"
- Label 4: "COST-QUALITY TRADE-OFF"
- Label 5: "CROSS-SESSION CONSISTENCY"
- Label 6: "EMOTIONAL APPROPRIATENESS"
- Label 7: "SAFETY / JAILBREAK"
- Label 8: "MULTI-PARTY HANDLING"
- Label 9: "GRACEFUL RECOVERY"
- Label 10: "NOISE ROBUSTNESS"
- Label 11: "Current coverage"
- Label 12: "Ideal coverage"

### Caption (for embedding in documentation)

Radar chart showing 10 critical evaluation dimensions for voice agents, revealing that current leaderboards cover only WER, MOS, and task completion while 8 production-critical dimensions remain untested.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `selected_option`, `warning_box`, `processing_stage` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. WER (Word Error Rate) and MOS (Mean Opinion Score) are standard speech evaluation metrics. They ARE covered by existing leaderboards.
10. Task completion rate is measured by some benchmarks (e.g., ToolBench for function calling). It IS partially covered.
11. The 8 untested dimensions are derived from production deployment challenges documented in the knowledge base -- they are NOT hypothetical.
12. TTS Arena (Hugging Face) and Chatbot Arena Voice (LMSYS) are the two most prominent leaderboards as of Feb 2026.
13. Accent bias refers to disproportionate WER for non-standard English accents -- this is a documented equity concern, not speculation.
14. Cross-session consistency means the agent maintains persona, memory, and behavior quality across multiple independent sessions.
15. "Multi-party handling" refers to conversations with 3+ participants, not just 1:1 -- this is largely untested.
16. The filled polygon must be visually SMALL compared to the dashed ideal polygon -- the gap is the visual argument.

## Alt Text

Radar chart displaying 10 critical voice agent evaluation dimensions where current leaderboards cover only WER, MOS, and task completion, leaving 8 production-critical gaps including accent bias, safety, cost-quality tradeoff, and noise robustness untested.

## Image Embed

![Radar chart displaying 10 critical voice agent evaluation dimensions where current leaderboards cover only WER, MOS, and task completion, leaving 8 production-critical gaps including accent bias, safety, cost-quality tradeoff, and noise robustness untested.](docs/figures/repo-figures/assets/fig-voice-25-evaluation-gaps-radar.jpg)

*Radar chart showing 10 critical evaluation dimensions for voice agents, revealing that current leaderboards cover only WER, MOS, and task completion while 8 production-critical dimensions remain untested.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-25",
    "title": "What Voice Agent Leaderboards Miss",
    "audience": "L2",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Current voice agent leaderboards cover only 2-3 of 10 critical evaluation dimensions, leaving accent bias, cost-quality, safety, and 5 other dimensions untested.",
    "layout_flow": "radial",
    "key_structures": [
      {
        "name": "WER / Accuracy",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["WER / ACCURACY", "tested"]
      },
      {
        "name": "MOS / Quality",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["MOS / QUALITY", "tested"]
      },
      {
        "name": "Task Completion",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["TASK COMPLETION", "tested"]
      },
      {
        "name": "Cost-Quality Trade-off",
        "role": "warning_box",
        "is_highlighted": false,
        "labels": ["COST-QUALITY TRADE-OFF", "untested"]
      },
      {
        "name": "Cross-Session Consistency",
        "role": "warning_box",
        "is_highlighted": false,
        "labels": ["CROSS-SESSION CONSISTENCY", "untested"]
      },
      {
        "name": "Emotional Appropriateness",
        "role": "warning_box",
        "is_highlighted": false,
        "labels": ["EMOTIONAL APPROPRIATENESS", "untested"]
      },
      {
        "name": "Safety / Jailbreak",
        "role": "warning_box",
        "is_highlighted": false,
        "labels": ["SAFETY / JAILBREAK", "untested"]
      },
      {
        "name": "Multi-Party Handling",
        "role": "warning_box",
        "is_highlighted": false,
        "labels": ["MULTI-PARTY HANDLING", "untested"]
      },
      {
        "name": "Graceful Recovery",
        "role": "warning_box",
        "is_highlighted": false,
        "labels": ["GRACEFUL RECOVERY", "untested"]
      },
      {
        "name": "Noise Robustness",
        "role": "warning_box",
        "is_highlighted": false,
        "labels": ["NOISE ROBUSTNESS", "untested"]
      }
    ],
    "relationships": [
      {
        "from": "Covered polygon",
        "to": "WER, MOS, Task Completion",
        "type": "arrow",
        "label": "currently tested"
      },
      {
        "from": "Ideal polygon",
        "to": "All 10 axes",
        "type": "dashed",
        "label": "required for production"
      }
    ],
    "callout_boxes": [
      {
        "heading": "8 OF 10 CRITICAL DIMENSIONS ARE UNTESTED BY ANY LEADERBOARD",
        "body_text": "Current benchmarks focus on quality and accuracy. Production voice agents require evaluation of cost, safety, robustness, and social dimensions.",
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
- [x] Anti-hallucination rules listed (8 default + 8 figure-specific)
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L2)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
