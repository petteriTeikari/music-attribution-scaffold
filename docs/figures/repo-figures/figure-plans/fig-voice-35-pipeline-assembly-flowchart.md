# fig-voice-35: Pipeline Assembly Flowchart

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-35 |
| **Title** | Pipeline Assembly Flowchart |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md, Section 2.1 |
| **Priority** | P1 (Important) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Show the build_pipecat_pipeline() decision tree: 5 factory functions, conditional drift monitor insertion, and final PipelineRunner assembly. The ASCII diagram in the doc shows structure; this shows the branching logic. Answers: "What decisions does the pipeline factory make during assembly?"

## Key Message

Pipeline assembly is a factory-of-factories: build_pipecat_pipeline() calls 5 creator functions (create_stt_service, create_tts_service, create_llm_service, create_transport, build_system_prompt) and conditionally inserts a DriftMonitorProcessor before wiring everything into a PipelineRunner.

## Visual Concept

Flowchart (Template C) top-to-bottom. Entry: build_pipecat_pipeline(config). Fan-out to 5 factory calls in parallel. Each returns a typed component. Components converge into a processors list. Decision diamond: "config.drift_monitoring?" If yes: insert DriftMonitorProcessor after LLM. Final: Pipeline(processors) into PipelineRunner. Coral accent squares mark entry and terminal nodes.

```
+-------------------------------------------------------------------+
|  PIPELINE ASSEMBLY FLOWCHART                             [coral sq] |
|  build_pipecat_pipeline() DECISION TREE                             |
+-------------------------------------------------------------------+
|                                                                     |
|              [build_pipecat_pipeline(config)]                       |
|                         |                                           |
|            +-----+------+------+------+                             |
|            |     |      |      |      |                             |
|            v     v      v      v      v                             |
|         create  create create create build_                         |
|         _stt_  _tts_  _llm_  _trans- system_                       |
|         service service service port  prompt                        |
|            |     |      |      |      |                             |
|            v     v      v      v      v                             |
|         [STT] [TTS]  [LLM]  [Trns] [Prompt]                        |
|            |     |      |      |      |                             |
|            +-----+------+------+------+                             |
|                         |                                           |
|                         v                                           |
|              [Build processors list]                                |
|                         |                                           |
|                    /----------\                                      |
|                   / drift_     \                                     |
|                  / monitoring?  \                                    |
|                  \    YES / NO  /                                    |
|                   \--------+--/                                      |
|                  YES |        | NO                                   |
|                      v        |                                     |
|          [Insert Drift        |                                     |
|           MonitorProcessor]   |                                     |
|                      |        |                                     |
|                      +--------+                                     |
|                         |                                           |
|                         v                                           |
|              [Pipeline(processors)]                                 |
|                         |                                           |
|                         v                                           |
|              [PipelineRunner]                            [coral sq] |
|                                                                     |
+-------------------------------------------------------------------+
|  ELI5: Like setting up a recording studio -- 5 specialists    [sq]  |
|  bring gear, optionally add a tuning meter, then patch bay.         |
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
    content: "PIPELINE ASSEMBLY FLOWCHART"
    role: title

  - id: flowchart_area
    bounds: [40, 140, 1840, 760]
    role: content_area

  - id: eli5_callout
    bounds: [40, 920, 1840, 120]
    role: callout_box

anchors:
  - id: entry_node
    position: [760, 160]
    size: [400, 50]
    role: processing_stage
    label: "build_pipecat_pipeline(config)"

  - id: factory_stt
    position: [160, 300]
    size: [280, 50]
    role: data_flow
    label: "create_stt_service(config)"

  - id: factory_tts
    position: [480, 300]
    size: [280, 50]
    role: data_flow
    label: "create_tts_service(config)"

  - id: factory_llm
    position: [800, 300]
    size: [280, 50]
    role: data_flow
    label: "create_llm_service()"

  - id: factory_transport
    position: [1120, 300]
    size: [280, 50]
    role: data_flow
    label: "create_transport(config)"

  - id: factory_prompt
    position: [1440, 300]
    size: [280, 50]
    role: data_flow
    label: "build_system_prompt(config)"

  - id: return_stt
    position: [220, 400]
    size: [160, 40]
    role: data_flow
    label: "STT service"

  - id: return_tts
    position: [540, 400]
    size: [160, 40]
    role: data_flow
    label: "TTS service"

  - id: return_llm
    position: [860, 400]
    size: [160, 40]
    role: data_flow
    label: "LLM service"

  - id: return_transport
    position: [1180, 400]
    size: [160, 40]
    role: data_flow
    label: "Transport"

  - id: return_prompt
    position: [1500, 400]
    size: [160, 40]
    role: data_flow
    label: "system prompt"

  - id: processors_list
    position: [760, 500]
    size: [400, 50]
    role: processing_stage
    label: "Build processors list"

  - id: drift_decision
    position: [810, 600]
    size: [300, 80]
    role: decision_point
    label: "config.drift_monitoring?"

  - id: drift_insert
    position: [560, 720]
    size: [320, 50]
    role: processing_stage
    label: "Insert DriftMonitorProcessor"

  - id: pipeline_node
    position: [760, 800]
    size: [400, 50]
    role: processing_stage
    label: "Pipeline(processors)"

  - id: runner_terminal
    position: [760, 880]
    size: [400, 50]
    role: processing_stage
    label: "PipelineRunner"

  - id: entry_to_fanout
    from: entry_node
    to: factory_stt
    type: arrow
    label: "fan-out"

  - id: fanout_converge
    from: return_stt
    to: processors_list
    type: arrow
    label: "converge"

  - id: processors_to_decision
    from: processors_list
    to: drift_decision
    type: arrow
    label: ""

  - id: decision_yes
    from: drift_decision
    to: drift_insert
    type: arrow
    label: "YES"

  - id: decision_no
    from: drift_decision
    to: pipeline_node
    type: arrow
    label: "NO"

  - id: drift_to_pipeline
    from: drift_insert
    to: pipeline_node
    type: arrow
    label: ""

  - id: pipeline_to_runner
    from: pipeline_node
    to: runner_terminal
    type: arrow
    label: ""
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| build_pipecat_pipeline(config) | `processing_stage` | Entry point -- accepts VoiceConfig, returns PipelineRunner |
| create_stt_service(config) | `data_flow` | Factory: selects STT provider from config enum |
| create_tts_service(config) | `data_flow` | Factory: selects TTS provider from config enum |
| create_llm_service() | `data_flow` | Factory: creates LLM service + registers domain tools |
| create_transport(config) | `data_flow` | Factory: creates transport from config enum |
| build_system_prompt(config) | `data_flow` | Factory: assembles 5-dimension persona prompt |
| Drift monitoring decision | `decision_point` | Conditional insertion of DriftMonitorProcessor |
| Pipeline(processors) | `processing_stage` | Assembled processor pipeline |
| PipelineRunner | `processing_stage` | Terminal node -- runs the assembled pipeline |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Entry | 5 factories | arrow | "fan-out" |
| 5 factories | Processors list | arrow | "converge" |
| Processors list | Drift decision | arrow | "" |
| Drift decision (YES) | Insert DriftMonitorProcessor | arrow | "YES" |
| Drift decision (NO) | Pipeline | arrow | "NO" |
| Insert DriftMonitorProcessor | Pipeline | arrow | "" |
| Pipeline | PipelineRunner | arrow | "" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Building the voice pipeline is like setting up a recording studio for a session: the session engineer (build_pipecat_pipeline) calls five specialists to bring their gear (STT, TTS, LLM, transport, persona prompt), optionally adds a tuning meter (drift monitor), then connects everything through the patch bay (PipelineRunner). | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "build_pipecat_pipeline(config)"
- Label 2: "create_stt_service(config)"
- Label 3: "create_tts_service(config)"
- Label 4: "create_llm_service()"
- Label 5: "create_transport(config)"
- Label 6: "build_system_prompt(config)"
- Label 7: "STT service"
- Label 8: "TTS service"
- Label 9: "LLM service"
- Label 10: "Transport"
- Label 11: "system prompt"
- Label 12: "Build processors list"
- Label 13: "config.drift_monitoring?"
- Label 14: "Insert DriftMonitorProcessor"
- Label 15: "Pipeline(processors)"
- Label 16: "PipelineRunner"
- Label 17: "YES"
- Label 18: "NO"

### Caption (for embedding in documentation)

Flowchart showing build_pipecat_pipeline() calling 5 factory functions in parallel, conditionally inserting a DriftMonitorProcessor, and assembling the final PipelineRunner.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `data_flow`, `decision_point` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pipecat", "PipelineRunner", "DriftMonitorProcessor" are appropriate for L3 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text in the figure.

### Figure-Specific Rules

9. The 5 factory functions must match actual function names in pipeline.py.
10. The conditional drift monitor insertion must be shown as a decision diamond.
11. Do NOT show the internal implementation of each factory -- just the function signature and return type.
12. The PipelineRunner must be shown as the terminal node.

## Alt Text

Flowchart of build_pipecat_pipeline calling 5 factory functions, conditional drift monitor insertion, and PipelineRunner assembly.

## Image Embed

![Flowchart of build_pipecat_pipeline calling 5 factory functions, conditional drift monitor insertion, and PipelineRunner assembly.](docs/figures/repo-figures/assets/fig-voice-35-pipeline-assembly-flowchart.jpg)

*Flowchart showing build_pipecat_pipeline() calling 5 factory functions in parallel, conditionally inserting a DriftMonitorProcessor, and assembling the final PipelineRunner.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-35",
    "title": "Pipeline Assembly Flowchart",
    "audience": "L3",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "Pipeline assembly is a factory-of-factories: build_pipecat_pipeline() calls 5 creator functions and conditionally inserts a DriftMonitorProcessor before wiring everything into a PipelineRunner.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Entry",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["build_pipecat_pipeline(config)"]
      },
      {
        "name": "Factory Functions",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["create_stt_service", "create_tts_service", "create_llm_service", "create_transport", "build_system_prompt"]
      },
      {
        "name": "Drift Decision",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["config.drift_monitoring?"]
      },
      {
        "name": "Terminal",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["PipelineRunner"]
      }
    ],
    "relationships": [
      {"from": "Entry", "to": "Factory Functions", "type": "arrow", "label": "fan-out"},
      {"from": "Factory Functions", "to": "Processors list", "type": "arrow", "label": "converge"},
      {"from": "Processors list", "to": "Drift Decision", "type": "arrow", "label": ""},
      {"from": "Drift Decision", "to": "DriftMonitorProcessor", "type": "arrow", "label": "YES"},
      {"from": "Drift Decision", "to": "Pipeline", "type": "arrow", "label": "NO"},
      {"from": "Pipeline", "to": "PipelineRunner", "type": "arrow", "label": ""}
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Building the voice pipeline is like setting up a recording studio for a session: the session engineer calls five specialists to bring their gear, optionally adds a tuning meter, then connects everything through the patch bay.",
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
- [ ] Audience level correct (L3)
- [ ] Layout template identified (C)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
