# fig-persona-22: PRD Expansion -- 5 Persona Decision Nodes

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-22 |
| **Title** | PRD Expansion -- 5 Persona Decision Nodes |
| **Audience** | L2 (PhD/Policy) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Shows how 5 new PRD decision nodes form a "persona pillar" that extends the existing decision network. Answers: "How do persona decisions integrate with the existing PRD architecture, and which existing nodes do they depend on?"

## Key Message

Five new decision nodes -- persona_coherence_strategy, user_modeling_strategy, voice_persona_management, cross_channel_state_strategy, and persona_drift_monitoring -- form a coherent persona pillar that mirrors the provenance pillar, with clear dependency arrows to existing nodes.

## Visual Concept

Left side shows three existing PRD nodes (ui_adaptation_strategy, voice_agent_stack, ml_monitoring) as established context. Right side introduces 5 new nodes with dependency arrows flowing from existing to new. Nodes are arranged by level (L2 at top, L5 at bottom). A callout emphasizes the structural parallel with the provenance pillar.

```
+---------------------------------------------------------------+
|  PRD EXPANSION -- 5 PERSONA DECISION NODES                     |
+---------------------------------------------------------------+
|                                                                |
|  EXISTING NODES              NEW PERSONA PILLAR                |
|  (context)                   (5 additions)                     |
|                                                                |
|  Level 2                                                       |
|  ┌──────────────────┐       ┌──────────────────────┐          |
|  │ ui_adaptation_    │──────>│ persona_coherence_    │          |
|  │ strategy          │       │ strategy (L2)         │          |
|  └──────────────────┘       └──────────┬───────────┘          |
|                                        │                       |
|  Level 2/3                             ▼                       |
|                              ┌──────────────────────┐          |
|                              │ user_modeling_         │          |
|                              │ strategy (L2/L3)      │          |
|                              └──────────┬───────────┘          |
|                                        │                       |
|  Level 3                               ▼                       |
|  ┌──────────────────┐       ┌──────────────────────┐          |
|  │ voice_agent_      │──────>│ voice_persona_        │          |
|  │ stack             │       │ management (L3)       │          |
|  └──────────────────┘       └──────────┬───────────┘          |
|                                        │                       |
|                                        ▼                       |
|                              ┌──────────────────────┐          |
|                              │ cross_channel_state_  │          |
|                              │ strategy (L3)         │          |
|                              └──────────┬───────────┘          |
|                                        │                       |
|  Level 5                               ▼                       |
|  ┌──────────────────┐       ┌──────────────────────┐          |
|  │ ml_monitoring     │──────>│ persona_drift_        │          |
|  └──────────────────┘       │ monitoring (L5)       │          |
|                              └──────────────────────┘          |
|                                                                |
+---------------------------------------------------------------+
|  5 NEW DECISION NODES FORM A PERSONA PILLAR MIRRORING THE     |
|  PROVENANCE PILLAR                                             |
+---------------------------------------------------------------+
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
    content: "PRD EXPANSION -- 5 PERSONA DECISION NODES"
    role: title

  - id: existing_column
    bounds: [80, 160, 700, 700]
    role: content_area

  - id: new_column
    bounds: [900, 160, 940, 700]
    role: content_area

  - id: callout_zone
    bounds: [80, 920, 1760, 120]
    role: callout_box

anchors:
  - id: existing_ui_adaptation
    position: [400, 260]
    size: [500, 100]
    role: decision_point
    label: "ui_adaptation_strategy"

  - id: existing_voice_stack
    position: [400, 520]
    size: [500, 100]
    role: decision_point
    label: "voice_agent_stack"

  - id: existing_ml_monitoring
    position: [400, 780]
    size: [500, 100]
    role: decision_point
    label: "ml_monitoring"

  - id: new_persona_coherence
    position: [1350, 260]
    size: [500, 100]
    role: selected_option
    label: "persona_coherence_strategy (L2)"

  - id: new_user_modeling
    position: [1350, 390]
    size: [500, 100]
    role: selected_option
    label: "user_modeling_strategy (L2/L3)"

  - id: new_voice_persona
    position: [1350, 520]
    size: [500, 100]
    role: selected_option
    label: "voice_persona_management (L3)"

  - id: new_cross_channel
    position: [1350, 650]
    size: [500, 100]
    role: selected_option
    label: "cross_channel_state_strategy (L3)"

  - id: new_drift_monitoring
    position: [1350, 780]
    size: [500, 100]
    role: selected_option
    label: "persona_drift_monitoring (L5)"

  - id: dep_ui_to_coherence
    from: existing_ui_adaptation
    to: new_persona_coherence
    type: arrow
    label: "depends on"

  - id: dep_coherence_to_modeling
    from: new_persona_coherence
    to: new_user_modeling
    type: arrow
    label: "informs"

  - id: dep_modeling_to_voice
    from: new_user_modeling
    to: new_voice_persona
    type: arrow
    label: "feeds"

  - id: dep_voice_stack_to_voice_persona
    from: existing_voice_stack
    to: new_voice_persona
    type: arrow
    label: "depends on"

  - id: dep_voice_to_cross_channel
    from: new_voice_persona
    to: new_cross_channel
    type: arrow
    label: "requires"

  - id: dep_cross_channel_to_drift
    from: new_cross_channel
    to: new_drift_monitoring
    type: arrow
    label: "monitored by"

  - id: dep_ml_to_drift
    from: existing_ml_monitoring
    to: new_drift_monitoring
    type: arrow
    label: "extends"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "PRD EXPANSION -- 5 PERSONA DECISION NODES" with accent square |
| ui_adaptation_strategy | `decision_point` | Existing L2 node -- how UI adapts to user proficiency |
| voice_agent_stack | `decision_point` | Existing L3 node -- Pipecat vs alternatives |
| ml_monitoring | `decision_point` | Existing L5 node -- model performance tracking |
| persona_coherence_strategy | `selected_option` | NEW L2 node -- how persona consistency is maintained |
| user_modeling_strategy | `selected_option` | NEW L2/L3 node -- how user proficiency is tracked |
| voice_persona_management | `selected_option` | NEW L3 node -- how voice characteristics map to persona |
| cross_channel_state_strategy | `selected_option` | NEW L3 node -- how state syncs across channels |
| persona_drift_monitoring | `selected_option` | NEW L5 node -- how persona drift is detected and corrected |
| Callout bar | `callout_bar` | Structural parallel with provenance pillar |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| ui_adaptation_strategy | persona_coherence_strategy | arrow | "depends on" |
| persona_coherence_strategy | user_modeling_strategy | arrow | "informs" |
| user_modeling_strategy | voice_persona_management | arrow | "feeds" |
| voice_agent_stack | voice_persona_management | arrow | "depends on" |
| voice_persona_management | cross_channel_state_strategy | arrow | "requires" |
| cross_channel_state_strategy | persona_drift_monitoring | arrow | "monitored by" |
| ml_monitoring | persona_drift_monitoring | arrow | "extends" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "PERSONA PILLAR" | 5 new decision nodes form a persona pillar mirroring the provenance pillar -- persona coherence sits at the same structural level as source corroboration | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "ui_adaptation_strategy"
- Label 2: "voice_agent_stack"
- Label 3: "ml_monitoring"
- Label 4: "persona_coherence (L2)"
- Label 5: "user_modeling (L2/L3)"
- Label 6: "voice_persona_mgmt (L3)"
- Label 7: "cross_channel_state (L3)"
- Label 8: "persona_drift_monitor (L5)"
- Label 9: "EXISTING NODES"
- Label 10: "NEW PERSONA PILLAR"

### Caption (for embedding in documentation)

PRD expansion showing 5 new persona decision nodes (persona_coherence_strategy, user_modeling_strategy, voice_persona_management, cross_channel_state_strategy, persona_drift_monitoring) forming a persona pillar with dependency arrows to existing nodes ui_adaptation_strategy, voice_agent_stack, and ml_monitoring.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `decision_point`, `selected_option`, `callout_bar` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience. This figure is L2 so use plain node names only.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Existing nodes MUST be visually distinct from new nodes -- existing are context, new are the subject.
10. The 5 new nodes are: persona_coherence_strategy (L2), user_modeling_strategy (L2/L3), voice_persona_management (L3), cross_channel_state_strategy (L3), persona_drift_monitoring (L5).
11. Level numbers (L2, L3, L5) MUST appear next to each node -- they indicate PRD decision network depth.
12. Dependency arrows flow from existing to new AND between new nodes in a chain.
13. Do NOT add nodes that are not specified -- exactly 3 existing + 5 new = 8 total.
14. The "pillar" metaphor means vertical stacking by level, not a literal column shape.
15. Do NOT imply these nodes have been implemented -- they are proposed additions.
16. "Mirroring the provenance pillar" means structural parallel, not content duplication.

## Alt Text

PRD decision network expansion showing five new persona coherence nodes forming a persona pillar with dependency arrows to three existing nodes, spanning levels L2 through L5 of the probabilistic product requirements decision network for music attribution

## Image Embed

![PRD decision network expansion showing five new persona coherence nodes forming a persona pillar with dependency arrows to three existing nodes, spanning levels L2 through L5 of the probabilistic product requirements decision network for music attribution](docs/figures/repo-figures/assets/fig-persona-22-prd-expansion-5-nodes.jpg)

*PRD expansion showing 5 new persona decision nodes (persona_coherence_strategy, user_modeling_strategy, voice_persona_management, cross_channel_state_strategy, persona_drift_monitoring) forming a persona pillar with dependency arrows to existing nodes ui_adaptation_strategy, voice_agent_stack, and ml_monitoring.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-22",
    "title": "PRD Expansion -- 5 Persona Decision Nodes",
    "audience": "L2",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "Five new decision nodes form a coherent persona pillar mirroring the provenance pillar, with clear dependency arrows to existing PRD nodes.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "ui_adaptation_strategy",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["ui_adaptation_strategy", "EXISTING"]
      },
      {
        "name": "voice_agent_stack",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["voice_agent_stack", "EXISTING"]
      },
      {
        "name": "ml_monitoring",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["ml_monitoring", "EXISTING"]
      },
      {
        "name": "persona_coherence_strategy",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["persona_coherence_strategy", "L2", "NEW"]
      },
      {
        "name": "user_modeling_strategy",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["user_modeling_strategy", "L2/L3", "NEW"]
      },
      {
        "name": "voice_persona_management",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["voice_persona_management", "L3", "NEW"]
      },
      {
        "name": "cross_channel_state_strategy",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["cross_channel_state_strategy", "L3", "NEW"]
      },
      {
        "name": "persona_drift_monitoring",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["persona_drift_monitoring", "L5", "NEW"]
      }
    ],
    "relationships": [
      {
        "from": "ui_adaptation_strategy",
        "to": "persona_coherence_strategy",
        "type": "arrow",
        "label": "depends on"
      },
      {
        "from": "persona_coherence_strategy",
        "to": "user_modeling_strategy",
        "type": "arrow",
        "label": "informs"
      },
      {
        "from": "user_modeling_strategy",
        "to": "voice_persona_management",
        "type": "arrow",
        "label": "feeds"
      },
      {
        "from": "voice_agent_stack",
        "to": "voice_persona_management",
        "type": "arrow",
        "label": "depends on"
      },
      {
        "from": "voice_persona_management",
        "to": "cross_channel_state_strategy",
        "type": "arrow",
        "label": "requires"
      },
      {
        "from": "cross_channel_state_strategy",
        "to": "persona_drift_monitoring",
        "type": "arrow",
        "label": "monitored by"
      },
      {
        "from": "ml_monitoring",
        "to": "persona_drift_monitoring",
        "type": "arrow",
        "label": "extends"
      }
    ],
    "callout_boxes": [
      {
        "heading": "PERSONA PILLAR",
        "body_text": "5 new decision nodes form a persona pillar mirroring the provenance pillar",
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
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
