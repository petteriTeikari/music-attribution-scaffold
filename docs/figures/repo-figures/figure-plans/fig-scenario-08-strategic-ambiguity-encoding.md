# fig-scenario-08: Strategic Ambiguity Encoding

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-scenario-08 |
| **Title** | Strategic Ambiguity Encoding |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P2 (Medium) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Contrasts core infrastructure nodes (which have selected options with low "none" prior probabilities of 0.05-0.20) against ecosystem nodes (which deliberately preserve 0.40-0.55 "none" priors). This demonstrates that high "none" priors are a feature, not a bug -- they encode strategic ambiguity as deliberate optionality. This answers: "Why do so many ecosystem nodes have 'none' as the highest-probability option?"

## Key Message

Core infrastructure nodes have selected options with low "none" priors (0.05-0.20), while ecosystem nodes deliberately preserve 0.40-0.55 "none" priors -- encoding strategic ambiguity as a feature of the probabilistic PRD.

## Visual Concept

Left panel shows 5-6 core infrastructure nodes with their selected options and low "none" probabilities, visualized as small bar charts or probability strips. Right panel shows 5-6 ecosystem nodes with their high "none" probabilities dominating. A bottom spectrum connects the two panels from "committed" (left) to "deliberately open" (right), with a gradient or transition zone.

```
+-----------------------------------------------------------------------+
|  STRATEGIC AMBIGUITY ENCODING                                          |
|  ■ Committed Decisions vs Deliberate Optionality                       |
+-----------------------------------------------------------------------+
|                                                                        |
|  CORE INFRASTRUCTURE                  ECOSYSTEM INTEGRATION            |
|  ═══════════════════                  ═══════════════════              |
|  Selected options, low "none"         High "none" priors = open        |
|                                                                        |
|  primary_database                     musical_ai_partnership           |
|  ├─ postgresql_unified  P=0.45        ├─ none              P=0.45     |
|  ├─ supabase           P=0.25        ├─ integration_pilot  P=0.25     |
|  └─ none               P=0.05        └─ certification      P=0.15     |
|                                                                        |
|  ai_framework_strategy                stim_cmo_pilot                   |
|  ├─ pydantic_ai        P=0.40        ├─ none              P=0.50     |
|  ├─ no_llm_baseline    P=0.25        ├─ pilot_integration  P=0.25     |
|  └─ none               P=0.10        └─ full_license       P=0.10     |
|                                                                        |
|  agentic_ui_framework                sureel_ai_partnership             |
|  ├─ copilotkit_agui    P=0.45        ├─ none              P=0.45     |
|  ├─ vercel_ai_sdk      P=0.20        ├─ api_evaluation     P=0.25     |
|  └─ none               P=0.10        └─ deep_integration   P=0.10     |
|                                                                        |
|  llm_provider                         tda_provider_integration         |
|  ├─ anthropic_primary  P=0.35        ├─ none              P=0.40     |
|  ├─ openai_primary     P=0.25        ├─ musical_ai_cert   P=0.25     |
|  └─ none               P=0.10        └─ self_hosted        P=0.15     |
|                                                                        |
|  compute_platform                     fairly_trained_certification     |
|  ├─ render_paas        P=0.35        ├─ none              P=0.45     |
|  ├─ hetzner            P=0.20        ├─ pursue_cert       P=0.30     |
|  └─ none               P=0.05        └─ audit_only        P=0.15     |
|                                                                        |
|  ◄──── COMMITTED ────────────── DELIBERATELY OPEN ────►               |
|  none: 0.05-0.10                none: 0.40-0.55                        |
|  Decisions made                 Optionality preserved                  |
|                                                                        |
+-----------------------------------------------------------------------+
|  High "none" priors = honest uncertainty, resource constraints,        |
|  and sequential strategy -- not indecision or failure                  |
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
    content: "STRATEGIC AMBIGUITY ENCODING"
    role: title

  - id: left_panel
    bounds: [60, 140, 880, 680]
    content: "CORE INFRASTRUCTURE"
    role: content_area

  - id: right_panel
    bounds: [980, 140, 880, 680]
    content: "ECOSYSTEM INTEGRATION"
    role: content_area

  - id: spectrum_bar
    bounds: [60, 840, 1800, 60]
    role: data_flow

  - id: footer_callout
    bounds: [60, 920, 1800, 100]
    role: callout_bar

anchors:
  - id: core_node_1
    position: [80, 200]
    size: [840, 80]
    role: selected_option

  - id: core_node_2
    position: [80, 300]
    size: [840, 80]
    role: selected_option

  - id: core_node_3
    position: [80, 400]
    size: [840, 80]
    role: selected_option

  - id: core_node_4
    position: [80, 500]
    size: [840, 80]
    role: selected_option

  - id: core_node_5
    position: [80, 600]
    size: [840, 80]
    role: selected_option

  - id: eco_node_1
    position: [1000, 200]
    size: [840, 80]
    role: deferred_option

  - id: eco_node_2
    position: [1000, 300]
    size: [840, 80]
    role: deferred_option

  - id: eco_node_3
    position: [1000, 400]
    size: [840, 80]
    role: deferred_option

  - id: eco_node_4
    position: [1000, 500]
    size: [840, 80]
    role: deferred_option

  - id: eco_node_5
    position: [1000, 600]
    size: [840, 80]
    role: deferred_option

  - id: spectrum
    position: [60, 860]
    size: [1800, 40]
    role: data_flow
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Core node probability strips (5) | `selected_option` | Each shows node name, selected option with P value, and low "none" P |
| Ecosystem node probability strips (5) | `deferred_option` | Each shows node name, "none" as top option with P=0.40-0.55 |
| Committed-to-Open spectrum | `data_flow` | Gradient bar from committed (left) to deliberately open (right) |
| Left panel heading | `label_editorial` | "CORE INFRASTRUCTURE: Selected options, low 'none'" |
| Right panel heading | `label_editorial` | "ECOSYSTEM INTEGRATION: High 'none' priors = open" |
| Footer insight | `callout_bar` | Framing of strategic ambiguity as positive design choice |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Core panel | Ecosystem panel | dashed | "commitment spectrum" |
| Low "none" | High "none" | bidirectional | "design continuum" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "STRATEGIC AMBIGUITY" | High "none" priors encode honest uncertainty, resource constraints, and sequential strategy -- not indecision | bottom-center |
| "COMMITTED" | Core nodes: decisions made, options selected, "none" at 0.05-0.20 | left-margin |
| "DELIBERATELY OPEN" | Ecosystem nodes: optionality preserved, "none" at 0.40-0.55, future partnerships gated by evidence | right-margin |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Core: none P=0.05-0.20"
- Label 2: "Ecosystem: none P=0.40-0.55"
- Label 3: "Committed decisions"
- Label 4: "Deliberate optionality"
- Label 5: "postgresql P=0.45"
- Label 6: "pydantic_ai P=0.40"
- Label 7: "copilotkit P=0.45"
- Label 8: "anthropic P=0.35"

### Caption (for embedding in documentation)

Core infrastructure nodes have committed to specific options with "none" priors of 0.05-0.20, while ecosystem nodes deliberately preserve 0.40-0.55 "none" priors -- encoding strategic ambiguity as a first-class feature of the probabilistic PRD.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `selected_option`, `deferred_option`, `data_flow` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text.

### Figure-Specific Rules

9. Core nodes with selected options (verified from decision YAMLs or REPORT.md): primary_database (postgresql_unified P=0.45), ai_framework_strategy (pydantic_ai P=0.40), agentic_ui_framework (copilotkit_agui P=0.45), llm_provider (anthropic_primary P=0.35). Exact probabilities should be verified from the individual .decision.yaml files.
10. Ecosystem "none" priors are in the 0.40-0.55 range per the expand-prd document Section 5.1. Individual node "none" priors should be verified from the ecosystem .decision.yaml files if they exist.
11. This is "Strategic Ambiguity by Design" -- the three drivers are: honest uncertainty about which partnerships will materialize, resource constraints preventing simultaneous exploration, and sequential strategy where core must be proven before ecosystem engagement.
12. Do NOT frame high "none" priors as failure, indecision, or incompleteness. Frame them positively as deliberate optionality.
13. The specific probability values shown are approximate/representative. They illustrate the pattern, not exact verified values.
14. Some ecosystem .decision.yaml files may not exist yet (they may be stubs). The probability ranges are from the expand-prd design document.

## Alt Text

Strategic ambiguity: core nodes committed vs ecosystem nodes preserving 0.40-0.55 optionality

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "scenario-08",
    "title": "Strategic Ambiguity Encoding",
    "audience": "L2",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "Core infrastructure has low 'none' priors (committed) while ecosystem nodes preserve high 'none' priors (deliberately open).",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Core Infrastructure Panel",
        "role": "selected_option",
        "is_highlighted": true,
        "labels": ["none P=0.05-0.20", "Options selected", "5 example nodes"]
      },
      {
        "name": "Ecosystem Panel",
        "role": "deferred_option",
        "is_highlighted": true,
        "labels": ["none P=0.40-0.55", "Optionality preserved", "5 example nodes"]
      },
      {
        "name": "Commitment Spectrum",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["Committed", "Deliberately Open"]
      }
    ],
    "relationships": [
      {
        "from": "Core (committed)",
        "to": "Ecosystem (open)",
        "type": "dashed",
        "label": "design continuum from certainty to strategic ambiguity"
      }
    ],
    "callout_boxes": [
      {
        "heading": "STRATEGIC AMBIGUITY",
        "body_text": "High 'none' priors encode honest uncertainty, resource constraints, and sequential strategy",
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
- [x] Layout template identified (D)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
