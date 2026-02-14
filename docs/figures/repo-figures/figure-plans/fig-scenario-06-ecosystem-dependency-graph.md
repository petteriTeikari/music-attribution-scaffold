# fig-scenario-06: Ecosystem Node Dependency Graph

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-scenario-06 |
| **Title** | Ecosystem Node Dependency Graph |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Shows the internal dependency chains among the 28 ecosystem nodes added in v3.0.0. Key chains: partnership_model gates 6+ downstream company/category nodes, cmo_licensing_integration gates stim_cmo_pilot, tda_provider_integration gates musical_ai_partnership. This answers: "How do ecosystem nodes depend on each other?"

## Key Message

Ecosystem nodes form internal dependency chains -- partnership_model gates company nodes, cmo_licensing_integration gates stim_cmo_pilot, and tda_provider_integration gates musical_ai_partnership -- creating conditional activation cascades.

## Visual Concept

A directed graph flowchart focused exclusively on the 28 ecosystem nodes and their internal edges. Nodes are grouped into tiers: L2 architecture nodes (platform_strategy, partnership_model) at top, L3 category nodes in the middle, L3 company nodes below, and L4/L5 ecosystem nodes at the bottom. Key gating chains are highlighted with stronger edge treatments. Edges show influence strength labels.

```
+-----------------------------------------------------------------------+
|  ECOSYSTEM NODE DEPENDENCY GRAPH                                       |
|  ■ 28 Nodes, Internal Chains                                          |
+-----------------------------------------------------------------------+
|                                                                        |
|  L2 ARCHITECTURE (ECOSYSTEM)                                           |
|  ┌─────────────────┐    ┌─────────────────┐                           |
|  │ platform_strategy│    │ partnership_model│                           |
|  └────┬───┬───┬────┘    └──┬──┬──┬──┬──┬──┘                           |
|       │   │   │            │  │  │  │  │                               |
|  L3 CATEGORY NODES         │  │  │  │  │                               |
|  ┌────┴──┐ ┌──┴────┐ ┌───┴┐ │  │  │  │                               |
|  │ai_musc│ │agentc_│ │cmo_│ │  │  │  │                                |
|  │platfrm│ │commrce│ │lic │ │  │  │  │                                |
|  └───┬───┘ └───────┘ └─┬──┘ │  │  │  │                               |
|      │                  │    │  │  │  │                                |
|  ┌───┴────┐  ┌─────┐ ┌─┴───┐│  │  │  │                               |
|  │content_│  │water-│ │tda_ ││  │  │  │                               |
|  │id_sys  │  │mark  │ │provd││  │  │  │                               |
|  └───┬────┘  └──────┘ └──┬──┘│  │  │  │                               |
|      │                    │   │  │  │  │                               |
|  L3 COMPANY NODES         │   │  │  │  │                               |
|  ┌───┴────┐ ┌─────┴───┐ ┌┴───┴┐ │  │  │                               |
|  │sureel_ │ │musical_ │ │stim_│ │  │  │                               |
|  │ai      │ │ai       │ │cmo  │ │  │  │                               |
|  └────────┘ └─────────┘ └─────┘ │  │  │                               |
|                                  │  │  │                               |
|  ┌──────────┐  ┌──────────┐  ┌──┴──┴──┴─┐                             |
|  │soundexch │  │suno_udio │  │fairly_   │                              |
|  │_registry │  │_licensing│  │trained   │                              |
|  └──────────┘  └──────────┘  └──────────┘                              |
|                                                                        |
|  L4/L5 ECOSYSTEM OPERATIONS                                           |
|  [compliance_rpt] [provenance_store] [golden_dataset] [edge_deploy]   |
|  [regulatory_mon] [market_intel] [accuracy_mon] [partner_health]      |
|                                                                        |
+-----------------------------------------------------------------------+
|  KEY CHAINS: partnership_model → 6+ company nodes                     |
|  cmo_licensing → stim_cmo (strong) | tda_provider → musical_ai (str)  |
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
    content: "ECOSYSTEM NODE DEPENDENCY GRAPH"
    role: title

  - id: l2_tier
    bounds: [60, 140, 1800, 120]
    role: content_area

  - id: l3_category_tier
    bounds: [60, 280, 1800, 240]
    role: content_area

  - id: l3_company_tier
    bounds: [60, 540, 1800, 180]
    role: content_area

  - id: l4_l5_tier
    bounds: [60, 740, 1800, 140]
    role: content_area

  - id: key_chains_bar
    bounds: [60, 900, 1800, 100]
    role: callout_bar

anchors:
  - id: platform_strategy
    position: [200, 170]
    size: [260, 60]
    role: decision_point

  - id: partnership_model
    position: [600, 170]
    size: [260, 60]
    role: decision_point

  - id: cmo_licensing
    position: [400, 320]
    size: [240, 60]
    role: decision_point

  - id: tda_provider
    position: [700, 320]
    size: [240, 60]
    role: decision_point

  - id: musical_ai
    position: [700, 580]
    size: [240, 60]
    role: decision_point

  - id: stim_cmo
    position: [400, 580]
    size: [240, 60]
    role: decision_point

  - id: edge_partnership_cmo
    from: partnership_model
    to: cmo_licensing
    type: arrow
    label: "strong"

  - id: edge_tda_musical
    from: tda_provider
    to: musical_ai
    type: arrow
    label: "strong"

  - id: edge_cmo_stim
    from: cmo_licensing
    to: stim_cmo
    type: arrow
    label: "strong"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| platform_strategy | `decision_point` | L2 node: determines platform vs tool positioning |
| partnership_model | `decision_point` | L2 node: gates downstream company nodes (6+ edges) |
| cmo_licensing_integration | `decision_point` | L3 category: CMO licensing approach |
| tda_provider_integration | `decision_point` | L3 category: Training data attribution provider |
| content_id_system | `decision_point` | L3 category: Content identification |
| ai_music_platform_connector | `decision_point` | L3 category: AI music platform integration |
| musical_ai_partnership | `decision_point` | L3 company: Musical AI engagement |
| sureel_ai_partnership | `decision_point` | L3 company: Sureel AI engagement |
| stim_cmo_pilot | `decision_point` | L3 company: STIM CMO pilot |
| soundexchange_registry | `decision_point` | L3 company: SoundExchange integration |
| fairly_trained_certification | `decision_point` | L3 company: Fairly Trained certification |
| suno_udio_licensing | `decision_point` | L3 company: Suno/Udio licensing |
| L4/L5 ecosystem nodes (8) | `decision_point` | Deployment and operations ecosystem nodes |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| partnership_model | cmo_licensing_integration | arrow | "strong" |
| partnership_model | tda_provider_integration | arrow | "moderate" |
| partnership_model | musical_ai_partnership | arrow | "moderate" |
| partnership_model | sureel_ai_partnership | arrow | "moderate" |
| tda_provider_integration | musical_ai_partnership | arrow | "strong" |
| cmo_licensing_integration | sureel_ai_partnership | arrow | "moderate" |
| cmo_licensing_integration | stim_cmo_pilot | arrow | "strong" |
| content_id_system | sureel_ai_partnership | arrow | "moderate" |
| external_registry_integration | soundexchange_registry | arrow | "moderate" |
| metadata_registry_integration | soundexchange_registry | arrow | "strong" |
| compliance_framework_mapping | fairly_trained_certification | arrow | "moderate" |
| ai_music_platform_connector | suno_udio_licensing | arrow | "strong" |
| rights_management_scope | suno_udio_licensing | arrow | "moderate" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "GATING NODE" | partnership_model has edges to 6+ downstream ecosystem nodes -- the ecosystem's primary orchestrator | top-right |
| "STRONG CHAINS" | tda_provider to musical_ai (strong), cmo_licensing to stim_cmo (strong), ai_music_platform to suno_udio (strong) | bottom-center |
| "CONDITIONAL CASCADES" | Ecosystem activation is sequential: L2 gates L3 categories, categories gate company nodes | left-margin |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "partnership_model: 6+ edges"
- Label 2: "tda_provider to musical_ai"
- Label 3: "cmo_licensing to stim_cmo"
- Label 4: "content_id to sureel_ai"
- Label 5: "platform_connector to suno"
- Label 6: "28 ecosystem nodes total"
- Label 7: "L2 gates L3 categories"
- Label 8: "Categories gate companies"

### Caption (for embedding in documentation)

The 28 ecosystem nodes form internal dependency chains with partnership_model as the primary gating node, creating conditional activation cascades from L2 architecture through L3 category and company nodes to L4/L5 ecosystem operations.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `decision_point`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- use node names as-is since this is L3 audience. Module names and tool names are appropriate.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text.

### Figure-Specific Rules

9. Internal ecosystem edges verified from _network.yaml v3.0.0: partnership_model to cmo_licensing (strong), partnership_model to tda_provider (moderate), partnership_model to musical_ai (moderate), partnership_model to sureel_ai (moderate), tda_provider to musical_ai (strong), cmo_licensing to sureel_ai (moderate), cmo_licensing to stim_cmo (strong), content_id to sureel_ai (moderate), external_registry to soundexchange (moderate), metadata_registry to soundexchange (strong), compliance_framework to fairly_trained (moderate), ai_music_platform_connector to suno_udio (strong), rights_management to suno_udio (moderate).
10. partnership_model also receives edges from target_market_segment (strong), revenue_model (moderate), and regulatory_posture (moderate). These are inbound from core nodes, not internal ecosystem edges.
11. platform_strategy receives edges from build_vs_buy (strong), target_market (moderate), revenue_model (moderate). Also inbound from core.
12. The figure should focus on edges BETWEEN ecosystem nodes, though showing the L2 gateway nodes (platform_strategy, partnership_model) as entry points from the core network.
13. Do NOT include all 181 network edges -- only show the ecosystem-internal and ecosystem-gateway edges.

## Alt Text

Ecosystem dependency graph: partnership_model gating company nodes in activation chains

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "scenario-06",
    "title": "Ecosystem Node Dependency Graph",
    "audience": "L3",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "Ecosystem nodes form internal dependency chains with partnership_model as primary gating node.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "L2 Gateway Nodes",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["platform_strategy", "partnership_model"]
      },
      {
        "name": "L3 Category Nodes",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["cmo_licensing", "tda_provider", "content_id", "ai_music_platform"]
      },
      {
        "name": "L3 Company Nodes",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["musical_ai", "sureel_ai", "stim_cmo", "soundexchange", "fairly_trained", "suno_udio"]
      },
      {
        "name": "L4/L5 Ecosystem Ops",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["compliance_rpt", "provenance_store", "golden_dataset", "edge_deploy"]
      }
    ],
    "relationships": [
      {
        "from": "partnership_model",
        "to": "6+ downstream nodes",
        "type": "arrow",
        "label": "primary ecosystem gating"
      },
      {
        "from": "tda_provider_integration",
        "to": "musical_ai_partnership",
        "type": "arrow",
        "label": "strong dependency"
      },
      {
        "from": "cmo_licensing_integration",
        "to": "stim_cmo_pilot",
        "type": "arrow",
        "label": "strong dependency"
      }
    ],
    "callout_boxes": [
      {
        "heading": "GATING NODE",
        "body_text": "partnership_model orchestrates 6+ downstream ecosystem nodes",
        "position": "top-right"
      },
      {
        "heading": "STRONG CHAINS",
        "body_text": "tda_provider->musical_ai, cmo_licensing->stim_cmo, platform_connector->suno_udio",
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
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
