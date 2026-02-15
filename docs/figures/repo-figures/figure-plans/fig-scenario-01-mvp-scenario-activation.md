# fig-scenario-01: MVP Scenario Activation Path

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-scenario-01 |
| **Title** | MVP Scenario Activation Path |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Shows that the MVP scenario activates 23 of 78 nodes in the probabilistic PRD network, with joint probability approximately 0.0012 -- the highest-probability path through the entire network. This answers the question: "What does the simplest viable instantiation of the scaffold look like?"

## Key Message

The MVP scenario activates 23 of 78 nodes with joint probability approximately 0.0012 -- the highest-probability path through the network, selecting PostgreSQL Unified, PydanticAI, CopilotKit, and Render with minimal ecosystem engagement.

## Visual Concept

A network diagram showing 78 nodes arranged in level bands (L1-L5). 23 nodes are rendered as solid/active with connecting edges highlighted, while 55 nodes appear as dashed/muted outlines. The active path traces from build_vs_buy through core infrastructure to deployment. A side panel lists the activated nodes with their selected options and individual probabilities.

```
+-----------------------------------------------------------------------+
|  MVP SCENARIO ACTIVATION PATH                                          |
|  ■ 23 of 78 Nodes Active -- Highest Probability Path                  |
+-----------------------------------------------------------------------+
|                                                                        |
|  L1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                   |
|  [Build/Buy]  [Market]  [Revenue]  [Regulatory]                        |
|       ◉          ◉         ◉          ◉          ← all 4 active       |
|       │          │                                                     |
|  L2 ━━┿━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                    |
|  [DataMdl] [API] [Svc] [AIFwk] [Artf] [UI] [Prov]  ○ ○              |
|     ◉       ◉     ◉      ◉      ◉     ◉     ◉    muted              |
|       │            │                                                   |
|  L3 ━━┿━━━━━━━━━━━━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                   |
|  [DB] [Grph] [Vec] [LLM] [Frnt] [Auth] [DQ] [AgUI] ...              |
|   ◉    ◉     ◉     ◉      ◉      ◉     ◉     ◉                      |
|  ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○ ○  (ecosystem     |
|                                                        nodes muted)   |
|  L4 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                  |
|  [Compute] [DBHost] [CI/CD] [IaC] [Container]  ○ ○ ○ ○               |
|     ◉        ◉        ◉      ◉       ◉                               |
|                                                                        |
|  L5 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                  |
|  [Observ] [Scale] [Backup] [Secret] [Schema]  ○ ○ ○ ○ ○ ○ ○ ○ ○     |
|                                                                        |
+-------------------------------+---------------------------------------+
|  ACTIVATED NODE PANEL         |  JOINT PROBABILITY                    |
|  PostgreSQL+pgvector  P=0.45  |  ~0.0012                              |
|  PydanticAI           P=0.40  |  Product of 23 selected-option        |
|  CopilotKit AG-UI     P=0.45  |  probabilities                        |
|  Render PaaS          P=0.35  |  Highest among 4 reference scenarios  |
|  GitHub Actions       P=0.50  |                                       |
+-------------------------------+---------------------------------------+
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
    content: "MVP SCENARIO ACTIVATION PATH"
    role: title

  - id: network_zone
    bounds: [60, 140, 1360, 740]
    role: content_area

  - id: side_panel
    bounds: [1440, 140, 440, 540]
    role: callout_box

  - id: probability_zone
    bounds: [1440, 700, 440, 180]
    role: callout_box

anchors:
  - id: l1_band
    position: [60, 160]
    size: [1340, 100]
    role: decision_point

  - id: l2_band
    position: [60, 280]
    size: [1340, 100]
    role: decision_point

  - id: l3_band
    position: [60, 400]
    size: [1340, 160]
    role: decision_point

  - id: l4_band
    position: [60, 580]
    size: [1340, 100]
    role: decision_point

  - id: l5_band
    position: [60, 700]
    size: [1340, 100]
    role: decision_point

  - id: active_node_list
    position: [1460, 160]
    size: [400, 500]
    role: data_mono

  - id: probability_callout
    position: [1460, 720]
    size: [400, 160]
    role: callout_box
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Active nodes (23) | `selected_option` | Solid-fill nodes representing MVP-selected decisions |
| Inactive nodes (55) | `deferred_option` | Dashed/muted outlines representing unactivated decisions |
| L1-L5 level bands | `processing_stage` | Horizontal level separators with labels |
| Active edge paths | `data_flow` | Highlighted connections between activated nodes |
| Inactive edge paths | `data_flow` | Muted/dashed connections between inactive nodes |
| Side panel | `data_mono` | List of activated nodes with option names and probabilities |
| Probability callout | `callout_bar` | Joint probability calculation summary |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| build_vs_buy_posture | primary_database | arrow | "strong influence" |
| build_vs_buy_posture | compute_platform | arrow | "platform choice" |
| primary_database | database_hosting | arrow | "hosting constraint" |
| ai_framework_strategy | llm_provider | arrow | "provider selection" |
| frontend_framework | agentic_ui_framework | arrow | "UI framework" |
| Ecosystem nodes (28) | (none) | dashed | "not activated in MVP" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "ACTIVATED NODES" | 23 nodes listed with selected options and per-node probabilities | right-panel |
| "JOINT PROBABILITY" | ~0.0012 -- product of 23 selected-option probabilities; highest among reference scenarios | bottom-right |
| "ECOSYSTEM GAP" | 28 ecosystem nodes have "none" selected in MVP -- deliberate deferral | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "23 of 78 nodes active"
- Label 2: "Joint P ~ 0.0012"
- Label 3: "55 nodes deferred"
- Label 4: "Highest-probability path"
- Label 5: "PostgreSQL + pgvector"
- Label 6: "PydanticAI native"
- Label 7: "CopilotKit AG-UI"
- Label 8: "Render PaaS"

### Caption (for embedding in documentation)

The MVP scenario traces the highest-probability path through the 78-node decision network, activating 23 core infrastructure nodes while deferring all 28 ecosystem integration nodes.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `selected_option`, `deferred_option`, `decision_point`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text.

### Figure-Specific Rules

9. MVP activates approximately 23 nodes. The exact count depends on which L5 operational nodes are included in the MVP path.
10. Joint probability ~0.0012 is approximate -- it is the product of selected-option probabilities for the 23 activated nodes. Do NOT claim this is exact.
11. MVP stack selections: PostgreSQL+pgvector (P=0.45), PydanticAI (P=0.40), CopilotKit AG-UI (P=0.45), Render PaaS, GitHub Actions.
12. Most ecosystem nodes (28 new in v3.0.0) have "none" selected in MVP. This is deliberate, not an oversight.
13. The 4 existing REPORT.md scenarios are: MVP Reference, Enterprise CMO, Research Lab, Solo Hacker. Do NOT invent additional scenarios.
14. Do NOT claim exact joint probability -- use "approximately" or "~".
15. The network has 78 nodes and 131 edges per the v3.0.0 description (actual YAML count may differ).

## Alt Text

MVP scenario: 23 of 78 nodes activated as highest-probability path through PRD network

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "scenario-01",
    "title": "MVP Scenario Activation Path",
    "audience": "L2",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "The MVP scenario activates 23 of 78 nodes with joint probability ~0.0012 -- the highest-probability path through the network.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Active Nodes",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["23 of 78 active", "PostgreSQL", "PydanticAI", "CopilotKit", "Render"]
      },
      {
        "name": "Inactive Nodes",
        "role": "deferred_option",
        "is_highlighted": false,
        "labels": ["55 nodes deferred", "Ecosystem muted"]
      },
      {
        "name": "Side Panel",
        "role": "data_mono",
        "is_highlighted": true,
        "labels": ["Activated node list", "Per-node probabilities"]
      },
      {
        "name": "Probability Callout",
        "role": "callout_bar",
        "is_highlighted": true,
        "labels": ["Joint P ~ 0.0012"]
      }
    ],
    "relationships": [
      {
        "from": "build_vs_buy_posture",
        "to": "primary_database",
        "type": "arrow",
        "label": "strongest influence on DB choice"
      },
      {
        "from": "build_vs_buy_posture",
        "to": "compute_platform",
        "type": "arrow",
        "label": "platform selection driver"
      },
      {
        "from": "Ecosystem Nodes",
        "to": "(none)",
        "type": "dashed",
        "label": "not activated in MVP"
      }
    ],
    "callout_boxes": [
      {
        "heading": "JOINT PROBABILITY",
        "body_text": "~0.0012 -- product of 23 selected-option probabilities",
        "position": "bottom-right"
      },
      {
        "heading": "ECOSYSTEM GAP",
        "body_text": "28 ecosystem nodes deferred in MVP",
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
- [x] Audience level correct (L2)
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
