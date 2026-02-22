# fig-voice-33: Voice Module File Map

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-voice-33 |
| **Title** | Voice Module File Map |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/tutorials/voice-agent-implementation.md, Section 2.2 |
| **Priority** | P1 (Important) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Show the 11-file voice module layout with dependency arrows between files. No prose can convey the import graph spatially. Answers: "Which files depend on which, and where do I start reading?"

## Key Message

The voice module is 11 focused files with a clear dependency hierarchy: config.py is the root, pipeline.py orchestrates, and specialized files (persona.py, drift.py, tools.py) are leaves.

## Visual Concept

Multi-panel layout showing 11 files as nodes arranged in a dependency tree. config.py at top center (root). pipeline.py below it (orchestrator). Leaf nodes fanned below: persona.py, tools.py, drift.py, server.py, protocols.py, letta_integration.py, mem0_integration.py, guardrails_integration.py, __init__.py. Arrows show import relationships flowing downward from root. Coral accent squares mark the 3 core files (config, pipeline, server).

```
+-------------------------------------------------------------------+
|  VOICE MODULE FILE MAP                                   [coral sq] |
|  11-FILE DEPENDENCY HIERARCHY                                       |
+-------------------------------------------------------------------+
|                                                                     |
|                      [config.py]  <-- ROOT                          |
|                     /  |   |   \                                    |
|                    /   |   |    \                                    |
|          [pipeline.py] |   |   [server.py]                          |
|          /  |  |  \    |   |      |                                 |
|         /   |  |   \   |   |      |                                 |
|  [persona] [tools] [drift] [protocols]                              |
|                                                                     |
|  [letta_integ] [mem0_integ] [guardrails_integ] [__init__]           |
|                                                                     |
+-------------------------------------------------------------------+
|  ELI5: Like instruments in a band -- config.py is the       [sq]    |
|  conductor's score, pipeline.py the stage manager.                  |
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
    content: "VOICE MODULE FILE MAP"
    role: title

  - id: dependency_tree
    bounds: [40, 140, 1840, 760]
    role: content_area

  - id: eli5_callout
    bounds: [40, 920, 1840, 120]
    role: callout_box

anchors:
  - id: config_root
    position: [860, 180]
    size: [200, 60]
    role: processing_stage
    label: "config.py"

  - id: pipeline_orchestrator
    position: [460, 340]
    size: [200, 60]
    role: processing_stage
    label: "pipeline.py"

  - id: server_entry
    position: [1260, 340]
    size: [200, 60]
    role: processing_stage
    label: "server.py"

  - id: persona_leaf
    position: [120, 520]
    size: [200, 60]
    role: data_flow
    label: "persona.py"

  - id: tools_leaf
    position: [380, 520]
    size: [200, 60]
    role: data_flow
    label: "tools.py"

  - id: drift_leaf
    position: [640, 520]
    size: [200, 60]
    role: data_flow
    label: "drift.py"

  - id: protocols_leaf
    position: [900, 520]
    size: [200, 60]
    role: data_flow
    label: "protocols.py"

  - id: letta_leaf
    position: [200, 700]
    size: [240, 60]
    role: data_flow
    label: "letta_integration.py"

  - id: mem0_leaf
    position: [520, 700]
    size: [240, 60]
    role: data_flow
    label: "mem0_integration.py"

  - id: guardrails_leaf
    position: [840, 700]
    size: [280, 60]
    role: data_flow
    label: "guardrails_integration.py"

  - id: init_leaf
    position: [1200, 700]
    size: [200, 60]
    role: data_flow
    label: "__init__.py"

  - id: config_to_pipeline
    from: config_root
    to: pipeline_orchestrator
    type: arrow
    label: "imports VoiceConfig"

  - id: config_to_server
    from: config_root
    to: server_entry
    type: arrow
    label: "imports VoiceConfig"

  - id: pipeline_to_persona
    from: pipeline_orchestrator
    to: persona_leaf
    type: arrow
    label: "build_system_prompt"

  - id: pipeline_to_tools
    from: pipeline_orchestrator
    to: tools_leaf
    type: arrow
    label: "register_domain_tools"

  - id: pipeline_to_drift
    from: pipeline_orchestrator
    to: drift_leaf
    type: arrow
    label: "DriftMonitorProcessor"

  - id: config_to_protocols
    from: config_root
    to: protocols_leaf
    type: arrow
    label: "structural types"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| config.py | `processing_stage` | VoiceConfig Pydantic Settings -- root dependency, imported by all |
| pipeline.py | `processing_stage` | Pipeline factory -- orchestrates assembly of all components |
| server.py | `processing_stage` | FastAPI WebSocket router -- entry point for client connections |
| persona.py | `data_flow` | 5-dimension prompt builder for system prompt construction |
| tools.py | `data_flow` | PydanticAI-to-Pipecat tool bridge for domain tool registration |
| drift.py | `data_flow` | DriftDetector + DriftMonitorProcessor for persona coherence |
| protocols.py | `data_flow` | Structural typing protocols for STT/TTS/transport interfaces |
| letta_integration.py | `data_flow` | Letta/MemGPT persona memory integration |
| mem0_integration.py | `data_flow` | Mem0 user preferences + safety gate |
| guardrails_integration.py | `data_flow` | NeMo Guardrails + regex fallback |
| __init__.py | `data_flow` | Module exports and public API surface |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| config.py | pipeline.py | arrow | "imports VoiceConfig" |
| config.py | server.py | arrow | "imports VoiceConfig" |
| pipeline.py | persona.py | arrow | "build_system_prompt" |
| pipeline.py | tools.py | arrow | "register_domain_tools" |
| pipeline.py | drift.py | arrow | "DriftMonitorProcessor" |
| config.py | protocols.py | arrow | "structural types" |
| pipeline.py | letta_integration.py | arrow | "persona memory" |
| pipeline.py | mem0_integration.py | arrow | "user preferences" |
| pipeline.py | guardrails_integration.py | arrow | "content guardrails" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ELI5" | Think of these 11 files like instruments in a band: config.py is the conductor's score, pipeline.py is the stage manager connecting everyone, and each specialized file is an instrumentalist who reads from the same score. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "config.py"
- Label 2: "pipeline.py"
- Label 3: "server.py"
- Label 4: "persona.py"
- Label 5: "tools.py"
- Label 6: "drift.py"
- Label 7: "protocols.py"
- Label 8: "letta_integration.py"
- Label 9: "mem0_integration.py"
- Label 10: "guardrails_integration.py"
- Label 11: "__init__.py"
- Label 12: "ROOT"
- Label 13: "ORCHESTRATOR"
- Label 14: "ENTRY POINT"

### Caption (for embedding in documentation)

Dependency tree of the 11-file voice module showing config.py as root, pipeline.py as orchestrator, and specialized leaf files for persona, tools, drift, protocols, and third-party integrations.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Pipecat" are appropriate for L3 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text in the figure.

### Figure-Specific Rules

9. File names must exactly match the actual source files: __init__.py, config.py, pipeline.py, persona.py, tools.py, drift.py, server.py, protocols.py, letta_integration.py, mem0_integration.py, guardrails_integration.py.
10. Dependency arrows must reflect real import relationships, not hypothetical ones.
11. Core files (config, pipeline, server) must be visually distinguished from leaf files.
12. Do NOT show external dependencies (pipecat, fastapi) -- only internal module graph.

## Alt Text

Dependency tree of 11 voice module files with config.py as root, pipeline.py as orchestrator, and specialized leaf nodes for tools and integrations.

## Image Embed

![Dependency tree of 11 voice module files with config.py as root, pipeline.py as orchestrator, and specialized leaf nodes for tools and integrations.](docs/figures/repo-figures/assets/fig-voice-33-voice-module-file-map.jpg)

*Dependency tree of the 11-file voice module showing config.py as root, pipeline.py as orchestrator, and specialized leaf files for persona, tools, drift, protocols, and third-party integrations.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "voice-33",
    "title": "Voice Module File Map",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "The voice module is 11 focused files with a clear dependency hierarchy: config.py is the root, pipeline.py orchestrates, and specialized files are leaves.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "config.py",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["config.py", "ROOT"]
      },
      {
        "name": "pipeline.py",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["pipeline.py", "ORCHESTRATOR"]
      },
      {
        "name": "server.py",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["server.py", "ENTRY POINT"]
      },
      {
        "name": "Leaf Files",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["persona.py", "tools.py", "drift.py", "protocols.py"]
      },
      {
        "name": "Integration Files",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["letta_integration.py", "mem0_integration.py", "guardrails_integration.py"]
      }
    ],
    "relationships": [
      {"from": "config.py", "to": "pipeline.py", "type": "arrow", "label": "imports VoiceConfig"},
      {"from": "config.py", "to": "server.py", "type": "arrow", "label": "imports VoiceConfig"},
      {"from": "pipeline.py", "to": "persona.py", "type": "arrow", "label": "build_system_prompt"},
      {"from": "pipeline.py", "to": "tools.py", "type": "arrow", "label": "register_domain_tools"},
      {"from": "pipeline.py", "to": "drift.py", "type": "arrow", "label": "DriftMonitorProcessor"}
    ],
    "callout_boxes": [
      {
        "heading": "ELI5",
        "body_text": "Think of these 11 files like instruments in a band: config.py is the conductor's score, pipeline.py is the stage manager connecting everyone, and each specialized file is an instrumentalist who reads from the same score.",
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
- [ ] Layout template identified (B)

## Status

- [ ] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
