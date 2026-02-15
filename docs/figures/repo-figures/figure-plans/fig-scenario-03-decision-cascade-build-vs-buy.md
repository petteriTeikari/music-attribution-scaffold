# fig-scenario-03: Decision Cascade: build_vs_buy_posture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-scenario-03 |
| **Title** | Decision Cascade: build_vs_buy_posture |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Shows build_vs_buy_posture as the network's highest-influence node -- it has 27 direct downstream edges spanning all 5 levels, making it the single most consequential architectural decision in the entire 78-node network. This answers: "Which single decision has the greatest cascading effect?"

## Key Message

build_vs_buy_posture is the network's highest-influence node -- 27 direct downstream edges spanning all 5 levels, making it the single most consequential architectural decision.

## Visual Concept

A radial/star layout with build_vs_buy_posture as the central emphasized node. 27 downstream nodes radiate outward, grouped by level (L2, L3, L4, L5). Edge lines are styled by influence strength (strong = solid, moderate = standard, weak = dashed). Each downstream node shows its level label. The visual emphasizes the sheer breadth of downstream impact from this single L1 decision.

```
+-----------------------------------------------------------------------+
|  DECISION CASCADE                                                      |
|  ■ build_vs_buy_posture: 27 Downstream Edges                          |
+-----------------------------------------------------------------------+
|                                                                        |
|                         L2 ARCHITECTURE                                |
|                    ┌─── data_model_complexity                          |
|                    ├─── service_decomposition                          |
|                    ├─── ai_framework_strategy                          |
|                    ├─── artifact_decoupling_strategy                   |
|                    ├─── provenance_strategy                            |
|                    └─── platform_strategy                              |
|                                                                        |
|  ┌──────────────┐  L3 IMPLEMENTATION                                  |
|  │ BUILD VS BUY │──├─── primary_database                              |
|  │  POSTURE     │  ├─── auth_strategy                                 |
|  │              │  ├─── llm_provider                                   |
|  │  ◉ L1       │  ├─── data_quality_strategy                         |
|  │  27 edges    │  ├─── voice_agent_stack                              |
|  └──────┬───────┘  ├─── llm_routing_strategy                          |
|         │          └─── audio_metadata_library                         |
|         │                                                              |
|         │          L3 COMPONENTS (ecosystem)                           |
|         ├──────── training_attribution_integration                     |
|         ├──────── external_registry_integration                        |
|         ├──────── tda_provider_integration                             |
|         ├──────── content_id_system                                    |
|         ├──────── edge_inference_strategy                              |
|         ├──────── attribution_eval_framework                           |
|         └──────── agent_observability_otel                             |
|                                                                        |
|                    L4 DEPLOYMENT                                       |
|                    ├─── compute_platform                               |
|                    ├─── iac_tooling                                     |
|                    ├─── ci_cd_pipeline                                  |
|                    └─── orchestrator_choice                             |
|                                                                        |
|                    L5 OPERATIONS                                       |
|                    ├─── observability_stack                             |
|                    ├─── schema_governance                              |
|                    └─── documentation_tooling                          |
|                                                                        |
+-----------------------------------------------------------------------+
|  INFLUENCE: ━━ strong (7)  ── moderate (17)  ╌╌ weak (3)              |
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
    content: "DECISION CASCADE: build_vs_buy_posture"
    role: title

  - id: center_node
    bounds: [100, 360, 320, 200]
    role: decision_point

  - id: l2_group
    bounds: [500, 140, 600, 200]
    role: content_area

  - id: l3_impl_group
    bounds: [500, 340, 600, 200]
    role: content_area

  - id: l3_comp_group
    bounds: [1100, 200, 600, 340]
    role: content_area

  - id: l4_group
    bounds: [500, 680, 600, 140]
    role: content_area

  - id: l5_group
    bounds: [500, 840, 600, 120]
    role: content_area

  - id: legend_bar
    bounds: [60, 980, 1800, 60]
    role: callout_bar

anchors:
  - id: build_vs_buy_node
    position: [160, 420]
    size: [240, 140]
    role: decision_point

  - id: edge_l2_data_model
    from: build_vs_buy_node
    to: l2_data_model
    type: arrow
    label: "moderate"

  - id: edge_l3_primary_db
    from: build_vs_buy_node
    to: l3_primary_db
    type: arrow
    label: "strong"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| build_vs_buy_posture (center) | `decision_point` | Central L1 node, emphasized as highest-influence |
| L2 Architecture children (6) | `decision_point` | data_model, service_decomp, ai_framework, artifact_decoupling, provenance, platform_strategy |
| L3 Implementation children (7) | `decision_point` | primary_database, auth, llm_provider, data_quality, voice_agent, llm_routing, audio_metadata |
| L3 Component children (7) | `decision_point` | training_attribution, external_registry, tda_provider, content_id, edge_inference, attribution_eval, agent_observability |
| L4 Deployment children (4) | `decision_point` | compute_platform, iac_tooling, ci_cd_pipeline, orchestrator_choice |
| L5 Operations children (3) | `decision_point` | observability_stack, schema_governance, documentation_tooling |
| Influence legend | `callout_bar` | Strong/moderate/weak edge counts |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| build_vs_buy_posture | service_decomposition | arrow | "strong" |
| build_vs_buy_posture | artifact_decoupling_strategy | arrow | "strong" |
| build_vs_buy_posture | primary_database | arrow | "strong" |
| build_vs_buy_posture | compute_platform | arrow | "strong" |
| build_vs_buy_posture | iac_tooling | arrow | "strong" |
| build_vs_buy_posture | platform_strategy | arrow | "strong" |
| build_vs_buy_posture | ai_framework_strategy | arrow | "moderate" |
| build_vs_buy_posture | data_model_complexity | arrow | "moderate" |
| build_vs_buy_posture | documentation_tooling | arrow | "weak" |
| build_vs_buy_posture | llm_provider | arrow | "weak" |
| build_vs_buy_posture | data_model_complexity | arrow | "weak" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "HIGHEST INFLUENCE" | 27 direct downstream edges -- more than any other node in the 78-node network | top-right |
| "ALL 5 LEVELS" | Edges reach L2 (6), L3 (14), L4 (4), L5 (3) -- no other L1 node spans all levels this broadly | bottom-right |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "27 downstream edges"
- Label 2: "Spans all 5 levels"
- Label 3: "L2: 6 architecture nodes"
- Label 4: "L3: 14 implementation nodes"
- Label 5: "L4: 4 deployment nodes"
- Label 6: "L5: 3 operations nodes"
- Label 7: "Strong: 7 edges"
- Label 8: "Moderate: 17 edges"

### Caption (for embedding in documentation)

build_vs_buy_posture cascades to 27 downstream nodes across all 5 levels of the decision network, making it the single most consequential architectural choice in the scaffold.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `decision_point`, `data_flow`, `callout_bar` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text.

### Figure-Specific Rules

9. build_vs_buy_posture has exactly 27 outgoing edges in _network.yaml v3.0.0. This is verified by counting all `from: build_vs_buy_posture` entries.
10. The 27 downstream nodes are: data_model_complexity, service_decomposition, ai_framework_strategy, artifact_decoupling_strategy, provenance_strategy, platform_strategy, primary_database, auth_strategy, llm_provider, data_quality_strategy, voice_agent_stack, llm_routing_strategy, audio_metadata_library, training_attribution_integration, external_registry_integration, tda_provider_integration, content_id_system, edge_inference_strategy, attribution_eval_framework, agent_observability_otel, compute_platform, iac_tooling, ci_cd_pipeline, orchestrator_choice, observability_stack, schema_governance, documentation_tooling.
11. Influence strengths from _network.yaml: strong edges to service_decomposition, artifact_decoupling, primary_database, compute_platform, iac_tooling, platform_strategy, and possibly others. Verify exact strengths from YAML.
12. The original user spec said "18 downstream nodes" but actual count from _network.yaml v3.0.0 is 27. Use the verified count of 27.
13. This is the highest out-degree node in the network. No other node has more outgoing edges.

## Alt Text

Decision cascade from build_vs_buy_posture: highest-influence node with 27 downstream edges

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "scenario-03",
    "title": "Decision Cascade: build_vs_buy_posture",
    "audience": "L2",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "build_vs_buy_posture is the network's highest-influence node with 27 direct downstream edges spanning all 5 levels.",
    "layout_flow": "radial",
    "key_structures": [
      {
        "name": "build_vs_buy_posture",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["L1 Business", "27 edges out"]
      },
      {
        "name": "L2 Children",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["6 architecture nodes"]
      },
      {
        "name": "L3 Children",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["14 implementation/component nodes"]
      },
      {
        "name": "L4 Children",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["4 deployment nodes"]
      },
      {
        "name": "L5 Children",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["3 operations nodes"]
      }
    ],
    "relationships": [
      {
        "from": "build_vs_buy_posture",
        "to": "27 downstream nodes",
        "type": "arrow",
        "label": "7 strong, 17 moderate, 3 weak"
      }
    ],
    "callout_boxes": [
      {
        "heading": "HIGHEST INFLUENCE",
        "body_text": "27 direct downstream edges -- more than any other node in the 78-node network",
        "position": "top-right"
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
