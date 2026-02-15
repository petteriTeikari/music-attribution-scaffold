# fig-trends-08: Scaffold-to-Trend Implication Matrix

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-trends-08 |
| **Title** | Scaffold-to-Trend Implication Matrix |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/planning/tech-trends-agentic-infrastructure-2026.md, README.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | A (Hero) |

## Purpose

Maps 10 technology trends to their specific PRD node impacts and volatility reclassifications. This is the summary figure for the entire tech trends report -- showing at a glance which trends stabilize the scaffold's architecture and which remain volatile. Answers: "How do current technology trends affect our architectural decisions?"

## Key Message

10 technology trends map to specific PRD node impacts -- 5 volatility reclassifications (2 stabilizing, 3 remaining volatile) reflect the rapidly evolving agentic infrastructure landscape.

## Visual Concept

Hero layout with a large matrix as the primary visual element. Rows are 10 trends, columns are affected PRD nodes. Cells indicate impact level. A side column shows volatility change indicators with arrows.

```
+-----------------------------------------------------------------------+
|  SCAFFOLD-TO-TREND IMPLICATION MATRIX                                  |
|  ■ 10 trends, 5 volatility reclassifications                          |
+-----------------------------------------------------------------------+
|                                                                        |
|                          AFFECTED PRD NODES                            |
|                    ┌────┬────┬────┬────┬────┬────┐  VOLATILITY        |
|   TRENDS           │api │ai_ │agen│reg │grph│eval│  CHANGE            |
|                    │prot│frmw│_ui │_pos│_rag│_frm│                     |
|  ──────────────────┼────┼────┼────┼────┼────┼────┤  ──────────        |
|  PydanticAI consol │    │ ●● │ ●  │    │    │ ●  │  Shifting→Stable   |
|  pgvector maturity │    │    │    │    │ ●  │    │  (validates)        |
|  MCP governance    │ ●●●│    │    │ ●  │    │    │  Shifting→Stable   |
|  A2A coordination  │ ●● │    │ ●  │    │    │    │  (new node)        |
|  Music rights infra│    │    │    │ ●● │    │    │  (validates)        |
|  Edge AI           │    │    │    │    │    │    │  (future)           |
|  OTel agents       │    │ ●  │    │    │    │    │  (new node)        |
|  Eval frameworks   │    │    │    │    │    │ ●● │  (new node)        |
|  Graph KBs         │    │    │    │    │ ●●●│    │  remains Volatile   |
|  EU AI Act         │    │    │    │ ●●●│    │    │  remains Volatile   |
|  ──────────────────┼────┼────┼────┼────┼────┼────┤                     |
|                    └────┴────┴────┴────┴────┴────┘                     |
|                                                                        |
|  ●●● = strong impact   ●● = moderate   ● = minor                      |
|                                                                        |
|  VOLATILITY RECLASSIFICATIONS                                          |
|  ──────────────────────────────                                        |
|  ■ api_protocol: Shifting → Stable (MCP dominance)                     |
|  ■ ai_framework_strategy: Volatile → Shifting (PydanticAI consolidation|
|  ■ agentic_ui_framework: Volatile → Shifting (AG-UI maturation)        |
|  ■ regulatory_posture: remains Volatile (EU AI Act evolving)           |
|  ■ graph_rag_engine: remains Volatile (no clear winner)                |
|                                                                        |
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
    content: "SCAFFOLD-TO-TREND IMPLICATION MATRIX"
    role: title

  - id: matrix_zone
    bounds: [60, 160, 1500, 540]
    content: "Trend x Node matrix"
    role: content_area

  - id: volatility_column
    bounds: [1580, 160, 280, 540]
    content: "Volatility changes"
    role: content_area

  - id: legend_zone
    bounds: [60, 720, 600, 60]
    content: "Impact legend"
    role: content_area

  - id: reclassification_zone
    bounds: [60, 800, 1800, 220]
    content: "Volatility reclassifications"
    role: callout_box

anchors:
  - id: matrix_header
    position: [360, 180]
    size: [1180, 60]
    role: data_flow

  - id: trend_row_1
    position: [60, 260]
    size: [1480, 40]
    role: data_flow

  - id: trend_row_2
    position: [60, 300]
    size: [1480, 40]
    role: data_flow

  - id: trend_row_3
    position: [60, 340]
    size: [1480, 40]
    role: data_flow

  - id: trend_row_4
    position: [60, 380]
    size: [1480, 40]
    role: data_flow

  - id: trend_row_5
    position: [60, 420]
    size: [1480, 40]
    role: data_flow

  - id: trend_row_6
    position: [60, 460]
    size: [1480, 40]
    role: data_flow

  - id: trend_row_7
    position: [60, 500]
    size: [1480, 40]
    role: data_flow

  - id: trend_row_8
    position: [60, 540]
    size: [1480, 40]
    role: data_flow

  - id: trend_row_9
    position: [60, 580]
    size: [1480, 40]
    role: data_flow

  - id: trend_row_10
    position: [60, 620]
    size: [1480, 40]
    role: data_flow

  - id: stabilizing_indicator
    position: [1600, 260]
    size: [240, 120]
    role: confidence_high

  - id: volatile_indicator
    position: [1600, 580]
    size: [240, 80]
    role: confidence_low
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Trend-node matrix | `data_flow` | 10 rows x 6+ columns matrix with impact dots |
| Impact legend | `data_flow` | Three-level impact key: strong, moderate, minor |
| Volatility column | `decision_point` | Side column showing volatility change for each trend |
| Reclassification summary | `callout_box` | Five specific volatility changes listed |
| Stabilizing indicators | `confidence_high` | Green-coded "Shifting to Stable" markers |
| Volatile indicators | `confidence_low` | Red-coded "remains Volatile" markers |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Each trend row | Affected PRD columns | arrow | "impact level" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "VOLATILITY RECLASSIFICATIONS" | 5 changes: api_protocol Shifting to Stable, ai_framework Volatile to Shifting, agentic_ui Volatile to Shifting, regulatory remains Volatile, graph_rag remains Volatile | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "PydanticAI consolidation"
- Label 2: "pgvector maturity"
- Label 3: "MCP governance"
- Label 4: "A2A coordination"
- Label 5: "Music rights infrastructure"
- Label 6: "Edge AI"
- Label 7: "OTel agents"
- Label 8: "Eval frameworks"
- Label 9: "Graph KBs"
- Label 10: "EU AI Act"
- Label 11: "api_protocol"
- Label 12: "ai_framework_strategy"
- Label 13: "agentic_ui_framework"
- Label 14: "regulatory_posture"
- Label 15: "graph_rag_engine"
- Label 16: "eval_framework"

### Caption (for embedding in documentation)

Scaffold-to-trend implication matrix: 10 technology trends mapped to PRD node impacts with 5 volatility reclassifications -- 2 stabilizing, 3 remaining volatile or shifting.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `data_flow`, `decision_point`, `confidence_high` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Volatility reclassifications are from tech-trends report Section 8.1: api_protocol Shifting to Stable, ai_framework_strategy Volatile to Shifting, agentic_ui_framework Volatile to Shifting, regulatory_posture remains Volatile, graph_rag_engine remains Volatile.
10. The 10 trends are from docs/planning/tech-trends-agentic-infrastructure-2026.md -- do NOT invent additional trends.
11. Do NOT invent trend impacts not discussed in the source report.
12. PRD node names in the matrix columns must match actual node IDs from the decision network YAML.
13. Impact levels (strong/moderate/minor) are editorial assessments from the report, not computed values.
14. This is L2 audience -- use accessible academic language, not raw code identifiers where possible.
15. The matrix is a summary visualization -- do NOT add detail that goes beyond the source report's conclusions.

## Alt Text

Trend-to-scaffold matrix: 10 tech trends mapped to PRD node impacts and reclassifications

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "trends-08",
    "title": "Scaffold-to-Trend Implication Matrix",
    "audience": "L2",
    "layout_template": "A"
  },
  "content_architecture": {
    "primary_message": "10 technology trends map to specific PRD node impacts with 5 volatility reclassifications.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Trend-Node Matrix",
        "role": "data_flow",
        "is_highlighted": true,
        "labels": ["10 trends", "6+ PRD nodes", "Impact dots"]
      },
      {
        "name": "Volatility Column",
        "role": "decision_point",
        "is_highlighted": true,
        "labels": ["Shifting to Stable", "Volatile to Shifting", "remains Volatile"]
      },
      {
        "name": "Reclassification Summary",
        "role": "callout_box",
        "is_highlighted": true,
        "labels": ["2 stabilizing", "3 remaining volatile/shifting"]
      }
    ],
    "relationships": [
      {
        "from": "Trend Rows",
        "to": "PRD Node Columns",
        "type": "arrow",
        "label": "impact level (strong/moderate/minor)"
      }
    ],
    "callout_boxes": [
      {
        "heading": "VOLATILITY RECLASSIFICATIONS",
        "body_text": "api_protocol: Shifting to Stable. ai_framework: Volatile to Shifting. agentic_ui: Volatile to Shifting. regulatory_posture: remains Volatile. graph_rag_engine: remains Volatile.",
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
- [x] Layout template identified (A)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
