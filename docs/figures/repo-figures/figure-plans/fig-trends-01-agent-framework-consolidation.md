# fig-trends-01: Agent Framework Consolidation 2025-2026

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-trends-01 |
| **Title** | Agent Framework Consolidation 2025-2026 |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/planning/tech-trends-agentic-infrastructure-2026.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Shows how the agent framework landscape has consolidated into three distinct tiers by early 2026, and where the music attribution scaffold sits within that landscape. Answers: "Which agent framework should I use for what?"

## Key Message

Agent framework landscape has consolidated into three tiers -- PydanticAI (type-safe production), LangGraph (orchestration), CrewAI/AG2 (multi-agent) -- with the scaffold using PydanticAI as its foundation.

## Visual Concept

Three-column layout with each tier as a distinct panel. The left column (PydanticAI) is highlighted as the scaffold's selected framework. Each column lists key capabilities. A bottom bar marks the scaffold's position on PydanticAI.

```
+-----------------------------------------------------------------------+
|  AGENT FRAMEWORK CONSOLIDATION 2025-2026                               |
|  ■ Three tiers, one scaffold choice                                    |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. TYPE-SAFE PRODUCTION   II. ORCHESTRATION      III. MULTI-AGENT     |
|  ──────────────────────    ─────────────────      ────────────────     |
|                                                                        |
|  ┌───────────────────┐    ┌──────────────────┐   ┌─────────────────┐  |
|  │  PydanticAI       │    │  LangGraph       │   │  CrewAI         │  |
|  │  ─────────        │    │  ─────────       │   │  ─────          │  |
|  │  FallbackModel    │    │  interrupt()     │   │  Role-based     │  |
|  │  RunContext DI    │    │  Checkpointing   │   │  team agents    │  |
|  │  AG-UI bridge     │    │  CoAgents        │   │  Task routing   │  |
|  │  Typed end-to-end │    │  Graph state     │   │                 │  |
|  │                   │    │                  │   │  AG2 (AutoGen)  │  |
|  │  ■ SCAFFOLD USES  │    │                  │   │  ─────────────  │  |
|  └───────────────────┘    └──────────────────┘   │  OTel-native    │  |
|                                                   │  Multi-runtime  │  |
|                                                   └─────────────────┘  |
|                                                                        |
+-----------------------------------------------------------------------+
|  SCAFFOLD POSITION  ■ PydanticAI (PRD: ai_framework_strategy)          |
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
    content: "AGENT FRAMEWORK CONSOLIDATION 2025-2026"
    role: title

  - id: panel_1
    bounds: [60, 160, 580, 680]
    content: "TYPE-SAFE PRODUCTION"
    role: selected_option

  - id: panel_2
    bounds: [670, 160, 580, 680]
    content: "ORCHESTRATION"
    role: deferred_option

  - id: panel_3
    bounds: [1280, 160, 580, 680]
    content: "MULTI-AGENT"
    role: deferred_option

  - id: scaffold_bar
    bounds: [60, 880, 1800, 80]
    content: "SCAFFOLD POSITION"
    role: callout_box

anchors:
  - id: pydanticai_block
    position: [120, 280]
    size: [460, 480]
    role: selected_option

  - id: langgraph_block
    position: [730, 280]
    size: [460, 480]
    role: processing_stage

  - id: crewai_block
    position: [1340, 280]
    size: [460, 280]
    role: processing_stage

  - id: ag2_block
    position: [1340, 580]
    size: [460, 180]
    role: processing_stage

  - id: scaffold_marker
    position: [120, 900]
    size: [460, 40]
    role: selected_option
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| PydanticAI panel | `selected_option` | Type-safe production tier -- FallbackModel, RunContext DI, AG-UI bridge |
| LangGraph panel | `deferred_option` | Orchestration tier -- interrupt(), checkpointing, CoAgents |
| CrewAI panel | `deferred_option` | Multi-agent tier -- role-based team definitions, task routing |
| AG2 panel | `deferred_option` | Multi-agent tier -- OTel-native, multi-runtime (formerly AutoGen) |
| Scaffold position bar | `callout_box` | Bottom bar indicating PydanticAI as the scaffold's chosen framework |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Scaffold position bar | PydanticAI panel | arrow | "selected" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "SCAFFOLD POSITION" | PydanticAI selected via PRD node ai_framework_strategy | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "TYPE-SAFE PRODUCTION"
- Label 2: "ORCHESTRATION"
- Label 3: "MULTI-AGENT"
- Label 4: "FallbackModel"
- Label 5: "RunContext DI"
- Label 6: "AG-UI bridge"
- Label 7: "interrupt() primitive"
- Label 8: "Checkpointing"
- Label 9: "CoAgents"
- Label 10: "Role-based teams"
- Label 11: "OTel-native"
- Label 12: "SCAFFOLD USES"

### Caption (for embedding in documentation)

Agent framework consolidation into three tiers: PydanticAI for type-safe production (scaffold's choice), LangGraph for stateful orchestration, and CrewAI/AG2 for multi-agent coordination.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `selected_option`, `deferred_option`, `processing_stage` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PydanticAI v0.2+ has FallbackModel and RunContext DI -- these are real, shipped features.
10. LangGraph 0.3+ has the interrupt() primitive -- this is a real, shipped feature.
11. AG2 (formerly AutoGen) integrated OTel Feb 2026 -- use "AG2" as the primary name, not "AutoGen".
12. CrewAI uses role-based agent definitions -- do NOT conflate with LangGraph's graph-based approach.
13. The scaffold uses PydanticAI -- this is SELECTED in the PRD (ai_framework_strategy = direct_api_pydantic).
14. Do NOT claim PydanticAI is "better" -- each framework serves different use cases and tiers.
15. Do NOT show version numbers in the figure unless they are critical to the tier distinction.

## Alt Text

Agent framework consolidation: PydanticAI, LangGraph, and CrewAI/AG2 in three tiers

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "trends-01",
    "title": "Agent Framework Consolidation 2025-2026",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Agent framework landscape has consolidated into three tiers with the scaffold using PydanticAI as its foundation.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "PydanticAI Panel",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["TYPE-SAFE PRODUCTION", "FallbackModel", "RunContext DI", "AG-UI bridge"]
      },
      {
        "name": "LangGraph Panel",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["ORCHESTRATION", "interrupt()", "Checkpointing", "CoAgents"]
      },
      {
        "name": "CrewAI Panel",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["MULTI-AGENT", "Role-based teams", "Task routing"]
      },
      {
        "name": "AG2 Panel",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["OTel-native", "Multi-runtime"]
      }
    ],
    "relationships": [
      {
        "from": "Scaffold Position Bar",
        "to": "PydanticAI Panel",
        "type": "arrow",
        "label": "selected framework"
      }
    ],
    "callout_boxes": [
      {
        "heading": "SCAFFOLD POSITION",
        "body_text": "PydanticAI selected via PRD node ai_framework_strategy = direct_api_pydantic",
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
- [x] Anti-hallucination rules listed
- [x] Alt text provided (125 chars max)
- [x] JSON export block included
- [x] Audience level correct (L3)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
