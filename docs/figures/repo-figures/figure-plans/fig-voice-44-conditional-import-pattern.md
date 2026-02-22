# fig-voice-44: Conditional Import Pattern

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-44 |
| **Title** | Conditional Import Pattern |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md, cross-cutting (new subsection) |
| **Priority** | P2 (Nice-to-have) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Show `try: import pipecat; PIPECAT_AVAILABLE=True` -> branch: real services vs config-only stubs. Shows why tests pass without pipecat installed. Answers: "Why does the voice module work (and tests pass) without Pipecat installed?"

## Key Message

The voice module uses conditional imports so that VoiceConfig and configuration logic work without Pipecat installed. Only build_pipecat_pipeline() requires the actual library -- everything else (config, persona, drift, tools schema) works standalone.

## Visual Concept

Flowchart (Template C). Entry: `import voice module`. Decision diamond: "try: import pipecat". Left branch (ImportError): PIPECAT_AVAILABLE = False -> config-only mode (VoiceConfig, persona.py, drift.py math, tool schemas). Right branch (success): PIPECAT_AVAILABLE = True -> full pipeline mode (all config-only features PLUS build_pipecat_pipeline, real services, PipelineRunner). Below: "Tests pass in both modes" callout with test file icons.

```
+-------------------------------------------------------------------+
|  CONDITIONAL IMPORT PATTERN                                [sq]    |
|  -- Graceful Degradation Without Pipecat                           |
+-------------------------------------------------------------------+
|                                                                    |
|                   [import voice module]                             |
|                          |                                         |
|                          v                                         |
|                  /---------------\                                  |
|                 / try: import     \                                 |
|                |    pipecat        |                                |
|                 \                 /                                  |
|                  \---------------/                                  |
|                   /            \                                    |
|          ImportError         success                                |
|              /                    \                                 |
|             v                      v                               |
|  PIPECAT_AVAILABLE          PIPECAT_AVAILABLE                      |
|      = False                    = True                             |
|        |                          |                                |
|  CONFIG-ONLY MODE          FULL PIPELINE MODE                      |
|  ────────────────          ──────────────────                      |
|  [config.py]               [config.py]                             |
|  [persona.py]              [persona.py]                            |
|  [drift.py math]           [drift.py math]                         |
|  [tools.py schemas]        [tools.py schemas]                      |
|  [protocols.py]            [protocols.py]                          |
|  [mem0_integration.py]     [mem0_integration.py]                   |
|  [guardrails_integ.py]     [guardrails_integ.py]                   |
|                            +                                       |
|                            [build_pipecat_pipeline]                 |
|                            [server.py WS endpoint]                  |
|                            [DriftMonitorProcessor]                  |
|                            [PipelineRunner]                         |
|        \                        /                                  |
|         \                      /                                   |
|          v                    v                                    |
|  +---------------------------------------------+                   |
|  |  TESTS PASS IN BOTH MODES                   |                   |
|  +---------------------------------------------+                   |
|                                                                    |
+-------------------------------------------------------------------+
|  ELI5: Acoustic or electric -- the sheet music works with   [sq]   |
|  either instrument; only the performance needs specific gear.      |
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
    content: "CONDITIONAL IMPORT PATTERN"
    role: title

  - id: flowchart_zone
    bounds: [40, 140, 1840, 700]
    role: content_area

  - id: eli5_callout
    bounds: [40, 920, 1840, 120]
    role: callout_box

anchors:
  - id: entry_point
    position: [960, 180]
    size: [360, 50]
    role: processing_stage
    label: "import voice module"

  - id: decision_diamond
    position: [960, 290]
    size: [300, 100]
    role: decision_point
    label: "try: import pipecat"

  - id: false_branch_label
    position: [460, 340]
    size: [200, 30]
    role: data_flow
    label: "ImportError"

  - id: true_branch_label
    position: [1460, 340]
    size: [200, 30]
    role: data_flow
    label: "success"

  - id: false_flag
    position: [460, 420]
    size: [360, 40]
    role: security_layer
    label: "PIPECAT_AVAILABLE = False"

  - id: true_flag
    position: [1460, 420]
    size: [360, 40]
    role: processing_stage
    label: "PIPECAT_AVAILABLE = True"

  - id: config_only_heading
    position: [460, 480]
    size: [300, 30]
    role: heading_display
    label: "CONFIG-ONLY MODE"

  - id: config_only_files
    position: [460, 560]
    size: [360, 200]
    role: data_flow
    label: "config, persona, drift..."

  - id: full_pipeline_heading
    position: [1460, 480]
    size: [300, 30]
    role: heading_display
    label: "FULL PIPELINE MODE"

  - id: full_pipeline_files
    position: [1460, 560]
    size: [360, 200]
    role: data_flow
    label: "all config-only + pipeline"

  - id: pipeline_extras
    position: [1460, 700]
    size: [360, 100]
    role: processing_stage
    label: "build_pipecat_pipeline"

  - id: tests_pass
    position: [960, 830]
    size: [500, 50]
    role: feedback_loop
    label: "TESTS PASS IN BOTH MODES"

  - id: entry_to_decision
    from: entry_point
    to: decision_diamond
    type: arrow
    label: ""

  - id: decision_to_false
    from: decision_diamond
    to: false_flag
    type: arrow
    label: "ImportError"

  - id: decision_to_true
    from: decision_diamond
    to: true_flag
    type: arrow
    label: "success"

  - id: false_to_tests
    from: config_only_files
    to: tests_pass
    type: arrow
    label: ""

  - id: true_to_tests
    from: pipeline_extras
    to: tests_pass
    type: arrow
    label: ""
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Entry point | `processing_stage` | `import voice module` -- the initial module load |
| Decision diamond | `decision_point` | `try: import pipecat` -- conditional import check |
| PIPECAT_AVAILABLE = False | `security_layer` | Module-level boolean set on ImportError |
| PIPECAT_AVAILABLE = True | `processing_stage` | Module-level boolean set on successful import |
| Config-only mode | `data_flow` | config.py, persona.py, drift.py math, tools.py schemas, protocols.py, mem0_integration.py, guardrails_integration.py |
| Full pipeline mode | `data_flow` | All config-only files PLUS build_pipecat_pipeline, server.py, DriftMonitorProcessor, PipelineRunner |
| Tests pass badge | `feedback_loop` | "TESTS PASS IN BOTH MODES" -- key takeaway |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Entry point | Decision diamond | arrow | "" |
| Decision diamond | PIPECAT_AVAILABLE = False | arrow | "ImportError" |
| Decision diamond | PIPECAT_AVAILABLE = True | arrow | "success" |
| Config-only mode | Tests pass | arrow | "7 files work standalone" |
| Full pipeline mode | Tests pass | arrow | "all files + pipeline" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Like a musician who can play either acoustic or electric -- the code checks which instrument (library) is available and adapts accordingly. The sheet music (config, persona, tools) works with either instrument; only the actual performance (pipeline) needs the specific gear. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "import voice module"
- Label 2: "try: import pipecat"
- Label 3: "ImportError"
- Label 4: "success"
- Label 5: "PIPECAT_AVAILABLE = False"
- Label 6: "PIPECAT_AVAILABLE = True"
- Label 7: "CONFIG-ONLY MODE"
- Label 8: "FULL PIPELINE MODE"
- Label 9: "config.py"
- Label 10: "persona.py"
- Label 11: "drift.py (math only)"
- Label 12: "tools.py (schemas only)"
- Label 13: "protocols.py"
- Label 14: "mem0_integration.py"
- Label 15: "guardrails_integration.py"
- Label 16: "build_pipecat_pipeline"
- Label 17: "server.py (WS endpoint)"
- Label 18: "DriftMonitorProcessor"
- Label 19: "TESTS PASS IN BOTH MODES"

### Caption (for embedding in documentation)

Conditional import flowchart showing how the voice module branches on PIPECAT_AVAILABLE: config-only mode (7 files work standalone) vs full pipeline mode (all files + Pipecat pipeline), with tests passing in both modes.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `decision_point`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon is ALLOWED** -- this is an L3 figure. PIPECAT_AVAILABLE, ImportError, build_pipecat_pipeline are appropriate.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text in the figure.

### Figure-Specific Rules

9. PIPECAT_AVAILABLE must be shown as a module-level boolean, not a runtime check.
10. The two branches must clearly show which files work in each mode.
11. Do NOT show pip/uv installation commands -- just the import result.
12. Test files must be shown as working in BOTH modes.

## Alt Text

Flowchart: try import pipecat branches to config-only mode (7 files) or full pipeline mode (all files), tests pass in both.

## Image Embed

![Flowchart: try import pipecat branches to config-only mode (7 files) or full pipeline mode (all files), tests pass in both.](docs/figures/repo-figures/assets/fig-voice-44-conditional-import-pattern.jpg)

*Conditional import flowchart showing how the voice module branches on PIPECAT_AVAILABLE: config-only mode (7 files work standalone) vs full pipeline mode (all files + Pipecat pipeline), with tests passing in both modes.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-44",
    "title": "Conditional Import Pattern",
    "audience": "L3",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "The voice module uses conditional imports so config/persona/drift/tools work without Pipecat; only build_pipecat_pipeline() requires it.",
    "layout_flow": "top-to-bottom-branching",
    "key_structures": [
      {
        "name": "Import Decision",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["try: import pipecat", "ImportError", "success"]
      },
      {
        "name": "Config-Only Mode",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["PIPECAT_AVAILABLE = False", "CONFIG-ONLY MODE"]
      },
      {
        "name": "Full Pipeline Mode",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["PIPECAT_AVAILABLE = True", "FULL PIPELINE MODE"]
      },
      {
        "name": "Config-Only Files",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["config.py", "persona.py", "drift.py", "tools.py", "protocols.py", "mem0_integration.py", "guardrails_integration.py"]
      },
      {
        "name": "Pipeline-Only Files",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["build_pipecat_pipeline", "server.py", "DriftMonitorProcessor"]
      },
      {
        "name": "Tests Pass Badge",
        "role": "feedback_loop",
        "is_highlighted": true,
        "labels": ["TESTS PASS IN BOTH MODES"]
      }
    ],
    "relationships": [
      {"from": "Import Decision", "to": "Config-Only Mode", "type": "arrow", "label": "ImportError"},
      {"from": "Import Decision", "to": "Full Pipeline Mode", "type": "arrow", "label": "success"},
      {"from": "Config-Only Mode", "to": "Tests Pass", "type": "arrow", "label": "7 files standalone"},
      {"from": "Full Pipeline Mode", "to": "Tests Pass", "type": "arrow", "label": "all files + pipeline"}
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Like a musician who can play acoustic or electric -- the sheet music works with either instrument; only the performance needs the specific gear.",
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
- [ ] Anti-hallucination rules listed (8 default + 4 figure-specific)
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
