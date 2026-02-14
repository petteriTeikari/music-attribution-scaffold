# fig-ecosystem-12: Compliance Reporting Pipeline

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-ecosystem-12 |
| **Title** | Compliance Reporting Pipeline |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/prd/decisions/REPORT.md, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Shows how the scaffold aggregates MCP audit logs, attribution confidence scores, and permission decision records into automated EU AI Act-compliant reports. Answers: "How do internal data flows produce the specific regulatory outputs required by the EU AI Act?"

## Key Message

The compliance reporting pipeline aggregates MCP audit logs, attribution confidence scores, and permission decisions into automated EU AI Act-compliant reports with Art. 12 logging and Art. 52 transparency.

## Visual Concept

Three input streams at the top feed into a central aggregation/formatting layer, which produces three distinct output report types at the bottom. The flow is top-to-bottom, emphasizing how diverse internal signals converge into structured regulatory outputs.

```
+---------------------------------------------------------------+
|  COMPLIANCE REPORTING PIPELINE                                 |
|  -- Internal Signals to Regulatory Outputs                     |
+---------------------------------------------------------------+
|                                                                |
|  INPUT STREAMS                                                 |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │ MCP AUDIT    │ │ ATTRIBUTION  │ │ PERMISSION   │          |
|  │ LOGS         │ │ SCORES       │ │ RECORDS      │          |
|  │              │ │              │ │              │          |
|  │ Tool calls   │ │ Per-field    │ │ Consent      │          |
|  │ Permission   │ │ confidence   │ │ decisions    │          |
|  │ queries      │ │ A0-A3 levels │ │ Grant/deny   │          |
|  └──────┬───────┘ └──────┬───────┘ └──────┬───────┘          |
|         │                │                │                   |
|         └────────────────┼────────────────┘                   |
|                          ▼                                    |
|  AGGREGATION + FORMATTING                                     |
|  ┌────────────────────────────────────────────────────────┐  |
|  │  Timestamp correlation, schema mapping, redaction       │  |
|  │  Template rendering, version control, audit trail       │  |
|  └────────┬───────────────┬───────────────┬───────────────┘  |
|           │               │               │                   |
|           ▼               ▼               ▼                   |
|  OUTPUT REPORTS                                               |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐         |
|  │ ART. 12      │ │ ART. 52      │ │ GPAI CODE OF │         |
|  │ LOGGING      │ │ TRANSPARENCY │ │ PRACTICE     │         |
|  │ REPORT       │ │ REPORT       │ │ REPORT       │         |
|  │              │ │              │ │              │         |
|  │ System event │ │ User-facing  │ │ Technical    │         |
|  │ logs, audit  │ │ disclosure,  │ │ documentation│         |
|  │ trails       │ │ AI markers   │ │ Art. 53      │         |
|  └──────────────┘ └──────────────┘ └──────────────┘         |
|                                                                |
+---------------------------------------------------------------+
|  Penalties: up to EUR 35M or 7% global turnover                |
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
    content: "COMPLIANCE REPORTING PIPELINE"
    role: title

  - id: input_zone
    bounds: [80, 150, 1760, 280]
    role: content_area

  - id: aggregation_zone
    bounds: [80, 470, 1760, 140]
    role: content_area

  - id: output_zone
    bounds: [80, 650, 1760, 300]
    role: content_area

  - id: penalty_zone
    bounds: [80, 980, 1760, 70]
    role: callout_box

anchors:
  - id: input_audit_logs
    position: [320, 280]
    size: [460, 220]
    role: api_endpoint
    label: "MCP Audit Logs"

  - id: input_attribution
    position: [960, 280]
    size: [460, 220]
    role: final_score
    label: "Attribution Scores"

  - id: input_permissions
    position: [1600, 280]
    size: [460, 220]
    role: security_layer
    label: "Permission Records"

  - id: aggregation
    position: [960, 540]
    size: [1600, 100]
    role: processing_stage
    label: "Aggregation + Formatting"

  - id: output_art12
    position: [320, 800]
    size: [460, 240]
    role: processing_stage
    label: "Art. 12 Logging Report"

  - id: output_art52
    position: [960, 800]
    size: [460, 240]
    role: processing_stage
    label: "Art. 52 Transparency Report"

  - id: output_gpai
    position: [1600, 800]
    size: [460, 240]
    role: processing_stage
    label: "GPAI Code of Practice Report"

  - id: flow_logs_to_agg
    from: input_audit_logs
    to: aggregation
    type: arrow
    label: "tool calls, permission queries"

  - id: flow_scores_to_agg
    from: input_attribution
    to: aggregation
    type: arrow
    label: "confidence scores, A0-A3"

  - id: flow_perms_to_agg
    from: input_permissions
    to: aggregation
    type: arrow
    label: "consent decisions"

  - id: flow_agg_to_art12
    from: aggregation
    to: output_art12
    type: arrow
    label: "logging output"

  - id: flow_agg_to_art52
    from: aggregation
    to: output_art52
    type: arrow
    label: "transparency output"

  - id: flow_agg_to_gpai
    from: aggregation
    to: output_gpai
    type: arrow
    label: "documentation output"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "COMPLIANCE REPORTING PIPELINE" with coral accent square |
| MCP Audit Logs input | `api_endpoint` | Tool calls, permission queries, timestamped events |
| Attribution Scores input | `final_score` | Per-field confidence scores, A0-A3 assurance levels |
| Permission Records input | `security_layer` | Consent decisions, grant/deny records |
| Aggregation layer | `processing_stage` | Timestamp correlation, schema mapping, redaction, template rendering |
| Art. 12 Logging Report | `processing_stage` | System event logs, audit trails per EU AI Act Art. 12 |
| Art. 52 Transparency Report | `processing_stage` | User-facing disclosure, AI content markers per Art. 52 |
| GPAI Code of Practice Report | `processing_stage` | Technical documentation per Art. 53, published July 2025 |
| Penalty callout | `data_mono` | "EUR 35M or 7% global turnover" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| MCP Audit Logs | Aggregation | arrow | "tool calls, permission queries" |
| Attribution Scores | Aggregation | arrow | "confidence scores, A0-A3" |
| Permission Records | Aggregation | arrow | "consent decisions" |
| Aggregation | Art. 12 Report | arrow | "logging output" |
| Aggregation | Art. 52 Report | arrow | "transparency output" |
| Aggregation | GPAI Report | arrow | "documentation output" |
| compliance_framework_mapping (parent) | compliance_reporting_pipeline | dashed | "strong" |
| regulatory_posture (parent) | compliance_reporting_pipeline | dashed | "strong" |
| ci_cd_pipeline (parent) | compliance_reporting_pipeline | dashed | "moderate" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "EU AI ACT ARTICLES" | Art. 12 = logging, Art. 52 = transparency, Art. 53 = technical documentation | right-margin |
| "PENALTY CONTEXT" | Non-compliance penalties up to EUR 35M or 7% global turnover | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "MCP AUDIT LOGS"
- Label 2: "ATTRIBUTION SCORES"
- Label 3: "PERMISSION RECORDS"
- Label 4: "AGGREGATION + FORMATTING"
- Label 5: "ART. 12 LOGGING REPORT"
- Label 6: "ART. 52 TRANSPARENCY REPORT"
- Label 7: "GPAI CODE OF PRACTICE REPORT"
- Label 8: "EUR 35M / 7% turnover"

### Caption (for embedding in documentation)

The compliance reporting pipeline aggregates MCP audit logs, attribution confidence scores, and permission decision records into three EU AI Act-compliant output reports -- Art. 12 logging, Art. 52 transparency, and GPAI Code of Practice technical documentation -- with penalties up to EUR 35M or 7% global turnover for non-compliance.

## Anti-Hallucination Rules

These are INTERNAL instructions for prompt construction. They MUST NEVER appear as visible text in the generated image.

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `api_endpoint`, `final_score` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- "Pydantic", "FastAPI", "Splink", "pgvector" should NOT appear unless the figure is L3/L4 audience.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. PRD node: `compliance_reporting_pipeline` (L4_deployment level).
10. Parent nodes: `compliance_framework_mapping` (strong), `regulatory_posture` (strong), `ci_cd_pipeline` (moderate).
11. EU AI Act Art. 12 = logging requirements for high-risk AI systems.
12. EU AI Act Art. 52 = transparency obligations (disclosure that content is AI-generated).
13. EU AI Act Art. 53 = technical documentation requirements for GPAI providers.
14. GPAI Code of Practice was published July 2025 -- do NOT use a different date.
15. Penalties are up to EUR 35M or 7% of global annual turnover, whichever is higher.
16. This pipeline is aspirational/planned -- do NOT imply it is currently fully implemented in the scaffold.

## Alt Text

Compliance pipeline: audit logs and confidence scores into EU AI Act reports

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "ecosystem-12",
    "title": "Compliance Reporting Pipeline",
    "audience": "L3",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "The compliance reporting pipeline aggregates MCP audit logs, attribution confidence scores, and permission decisions into automated EU AI Act-compliant reports with Art. 12 logging and Art. 52 transparency.",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "MCP Audit Logs",
        "role": "api_endpoint",
        "is_highlighted": false,
        "labels": ["MCP AUDIT LOGS", "Tool calls"]
      },
      {
        "name": "Attribution Scores",
        "role": "final_score",
        "is_highlighted": false,
        "labels": ["ATTRIBUTION SCORES", "A0-A3"]
      },
      {
        "name": "Permission Records",
        "role": "security_layer",
        "is_highlighted": false,
        "labels": ["PERMISSION RECORDS", "Consent"]
      },
      {
        "name": "Aggregation Layer",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["AGGREGATION + FORMATTING"]
      },
      {
        "name": "Art. 12 Logging Report",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["ART. 12 LOGGING REPORT"]
      },
      {
        "name": "Art. 52 Transparency Report",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["ART. 52 TRANSPARENCY REPORT"]
      },
      {
        "name": "GPAI Code of Practice Report",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["GPAI CODE OF PRACTICE REPORT"]
      }
    ],
    "relationships": [
      {
        "from": "MCP Audit Logs",
        "to": "Aggregation Layer",
        "type": "arrow",
        "label": "tool calls, permission queries"
      },
      {
        "from": "Attribution Scores",
        "to": "Aggregation Layer",
        "type": "arrow",
        "label": "confidence scores, A0-A3"
      },
      {
        "from": "Permission Records",
        "to": "Aggregation Layer",
        "type": "arrow",
        "label": "consent decisions"
      },
      {
        "from": "Aggregation Layer",
        "to": "Art. 12 Logging Report",
        "type": "arrow",
        "label": "logging output"
      },
      {
        "from": "Aggregation Layer",
        "to": "Art. 52 Transparency Report",
        "type": "arrow",
        "label": "transparency output"
      },
      {
        "from": "Aggregation Layer",
        "to": "GPAI Code of Practice Report",
        "type": "arrow",
        "label": "documentation output"
      }
    ],
    "callout_boxes": [
      {
        "heading": "EU AI ACT ARTICLES",
        "body_text": "Art. 12 = logging, Art. 52 = transparency, Art. 53 = technical documentation",
        "position": "right-margin"
      },
      {
        "heading": "PENALTY CONTEXT",
        "body_text": "Non-compliance penalties up to EUR 35M or 7% global turnover",
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
- [x] Audience level correct (L3)
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
