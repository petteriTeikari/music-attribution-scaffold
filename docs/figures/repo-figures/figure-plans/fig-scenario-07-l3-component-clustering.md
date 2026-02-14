# fig-scenario-07: L3 Component Node Clustering

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-scenario-07 |
| **Title** | L3 Component Node Clustering |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Shows how the 24 L3_components nodes cluster into 5 functional groups, revealing the ecosystem's internal structure. This is distinct from the 14 L3_implementation nodes (which cover core infrastructure). This answers: "What is the functional taxonomy of ecosystem component decisions?"

## Key Message

24 L3 component nodes cluster into 5 functional groups -- TDA/Identification (4), Licensing (4), Platform/Commerce (4), Infrastructure (6), and Company-Specific (6) -- revealing the ecosystem's functional structure.

## Visual Concept

Five grouped panels arranged in a 2-3 or 3-2 layout, each containing the relevant nodes. Each panel uses a Roman numeral heading and lists the nodes within that functional group. Edges between panels show cross-group dependencies. Company-specific nodes (panel V) are visually distinguished as concrete partnership decisions versus abstract capability decisions.

```
+-----------------------------------------------------------------------+
|  L3 COMPONENT NODE CLUSTERING                                          |
|  ■ 24 Nodes in 5 Functional Groups                                    |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. TDA / IDENTIFICATION         II. LICENSING                         |
|  ───────────────────────         ──────────────                        |
|  ┌────────────────────────┐     ┌────────────────────────┐             |
|  │ tda_provider_integration│     │ cmo_licensing_integration│            |
|  │ content_id_system       │     │ rights_management_scope  │            |
|  │ watermark_detection     │     │ tdm_rights_reservation   │            |
|  │ attribution_eval_frmwk  │     │ compliance_framework_map │            |
|  └────────────────────────┘     └────────────────────────┘             |
|                                                                        |
|  III. PLATFORM / COMMERCE        IV. INFRASTRUCTURE                    |
|  ────────────────────────        ──────────────────                    |
|  ┌────────────────────────┐     ┌────────────────────────┐             |
|  │ ai_music_platform_conn  │     │ metadata_registry_integ │            |
|  │ agentic_commerce_proto  │     │ knowledge_graph_backend │            |
|  │ agent_interop_protocol  │     │ edge_inference_strategy │            |
|  │ agent_observability_otel│     │ external_registry_integ │            |
|  └────────────────────────┘     │ provenance_verification │            |
|                                  │ training_attrib_integ   │            |
|                                  └────────────────────────┘             |
|                                                                        |
|  V. COMPANY-SPECIFIC                                                   |
|  ───────────────────                                                   |
|  ┌────────────────────────────────────────────────────────────┐        |
|  │ musical_ai_partnership  │ sureel_ai_partnership            │        |
|  │ stim_cmo_pilot          │ soundexchange_registry           │        |
|  │ fairly_trained_cert     │ suno_udio_licensing              │        |
|  └────────────────────────────────────────────────────────────┘        |
|                                                                        |
+-----------------------------------------------------------------------+
|  NOTE: L3_implementation (14 nodes) not shown -- this figure focuses   |
|  on L3_components only                                                 |
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
    content: "L3 COMPONENT NODE CLUSTERING"
    role: title

  - id: panel_tda
    bounds: [60, 140, 880, 220]
    content: "I. TDA / IDENTIFICATION"
    role: content_area

  - id: panel_licensing
    bounds: [980, 140, 880, 220]
    content: "II. LICENSING"
    role: content_area

  - id: panel_platform
    bounds: [60, 380, 880, 220]
    content: "III. PLATFORM / COMMERCE"
    role: content_area

  - id: panel_infra
    bounds: [980, 380, 880, 260]
    content: "IV. INFRASTRUCTURE"
    role: content_area

  - id: panel_company
    bounds: [60, 660, 1800, 200]
    content: "V. COMPANY-SPECIFIC"
    role: content_area

  - id: footer_note
    bounds: [60, 880, 1800, 60]
    role: callout_bar

anchors:
  - id: tda_group
    position: [80, 180]
    size: [840, 160]
    role: decision_point

  - id: licensing_group
    position: [1000, 180]
    size: [840, 160]
    role: decision_point

  - id: platform_group
    position: [80, 420]
    size: [840, 160]
    role: decision_point

  - id: infra_group
    position: [1000, 420]
    size: [840, 200]
    role: decision_point

  - id: company_group
    position: [80, 700]
    size: [1760, 140]
    role: decision_point
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| TDA/Identification group (4) | `decision_point` | tda_provider_integration, content_id_system, watermark_detection, attribution_eval_framework |
| Licensing group (4) | `decision_point` | cmo_licensing_integration, rights_management_scope, tdm_rights_reservation, compliance_framework_mapping |
| Platform/Commerce group (4) | `decision_point` | ai_music_platform_connector, agentic_commerce_protocol, agent_interop_protocol, agent_observability_otel |
| Infrastructure group (6) | `decision_point` | metadata_registry_integration, knowledge_graph_backend, edge_inference_strategy, external_registry_integration, provenance_verification, training_attribution_integration |
| Company-Specific group (6) | `decision_point` | musical_ai_partnership, sureel_ai_partnership, stim_cmo_pilot, soundexchange_registry, fairly_trained_certification, suno_udio_licensing |
| Group headings | `label_editorial` | Roman numeral section headers |
| Footer note | `callout_bar` | Clarification that L3_implementation nodes are not included |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| TDA/ID group | Company group | dashed | "tda_provider gates musical_ai" |
| Licensing group | Company group | dashed | "cmo_licensing gates stim_cmo" |
| Platform group | Company group | dashed | "platform_connector gates suno_udio" |
| Infrastructure group | Company group | dashed | "registries gate soundexchange" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "CATEGORY vs COMPANY" | Groups I-IV are capability decisions (vendor-agnostic); Group V is concrete partnership decisions (vendor-specific) | top-right |
| "TOTAL L3" | L3 has 38 total nodes: 14 implementation + 24 components. This figure shows only the 24 components. | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I. TDA / Identification (4)"
- Label 2: "II. Licensing (4)"
- Label 3: "III. Platform / Commerce (4)"
- Label 4: "IV. Infrastructure (6)"
- Label 5: "V. Company-Specific (6)"
- Label 6: "24 L3_components nodes"
- Label 7: "Category vs Company split"
- Label 8: "14 L3_impl not shown"

### Caption (for embedding in documentation)

The 24 L3 component nodes cluster into 5 functional groups -- TDA/Identification, Licensing, Platform/Commerce, Infrastructure, and Company-Specific -- separating capability decisions from concrete partnership commitments.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `decision_point`, `label_editorial`, `callout_bar` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- use node names as-is since this is L3 audience. Module names and tool names are appropriate.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text.

### Figure-Specific Rules

9. L3 has two sublevel types in _network.yaml: L3_implementation (14 nodes: primary_database through mcp_production_deployment) and L3_components (24 nodes: 6 existing commercial + 12 new category + 6 new company).
10. The clustering into 5 groups is interpretive/functional grouping, NOT a formal classification in the YAML. These groups are based on functional similarity.
11. Total L3 = 38 nodes, but this figure focuses ONLY on the 24 L3_components nodes. Do NOT include L3_implementation nodes (primary_database, graph_strategy, vector_strategy, etc.) in this figure.
12. The 6 existing commercial landscape nodes (training_attribution_integration, rights_management_scope, provenance_verification, external_registry_integration, compliance_framework_mapping, tdm_rights_reservation) were added in v1.8-v2.0. The 18 new ecosystem nodes were added in v3.0.0.
13. The grouping placement of some nodes is debatable (e.g., training_attribution_integration could fit in TDA or Infrastructure). The chosen grouping is one reasonable interpretation.

## Alt Text

L3 component clustering: 24 nodes in TDA/ID, licensing, platform, infra, company groups

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "scenario-07",
    "title": "L3 Component Node Clustering",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "24 L3 component nodes cluster into 5 functional groups revealing the ecosystem's structure.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "TDA/Identification",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["4 nodes", "tda_provider", "content_id", "watermark", "eval_framework"]
      },
      {
        "name": "Licensing",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["4 nodes", "cmo_licensing", "rights_mgmt", "tdm_rights", "compliance"]
      },
      {
        "name": "Platform/Commerce",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["4 nodes", "ai_music_platform", "agentic_commerce", "agent_interop", "agent_otel"]
      },
      {
        "name": "Infrastructure",
        "role": "decision_point",
        "is_highlighted": false,
        "labels": ["6 nodes", "metadata_registry", "knowledge_graph", "edge_inference"]
      },
      {
        "name": "Company-Specific",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["6 nodes", "musical_ai", "sureel_ai", "stim_cmo", "soundexchange", "fairly_trained", "suno_udio"]
      }
    ],
    "relationships": [
      {
        "from": "Category groups (I-IV)",
        "to": "Company group (V)",
        "type": "dashed",
        "label": "capability decisions gate partnership decisions"
      }
    ],
    "callout_boxes": [
      {
        "heading": "CATEGORY vs COMPANY",
        "body_text": "Groups I-IV are vendor-agnostic; Group V is vendor-specific",
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
- [x] Audience level correct (L3)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
