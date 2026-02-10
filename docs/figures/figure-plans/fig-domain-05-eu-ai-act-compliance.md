# fig-domain-05: EU AI Act Compliance for Music AI

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-domain-05 |
| **Title** | EU AI Act Compliance for Music AI |
| **Audience** | Domain (music industry) |
| **Complexity** | L2 (overview) |
| **Location** | docs/prd/vision-v1.md, docs/knowledge-base/domain/legal/eu-ai-act-2025.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |

## Purpose

Show the EU AI Act compliance timeline and the system's role in helping music AI platforms meet regulatory requirements, emphasizing the €35M penalty context.

## Key Message

"EU AI Act requires training data transparency from August 2025—The system provides the provenance tracking that music AI platforms need for compliance."

## Visual Concept

Timeline with regulatory milestones and the system compliance value proposition.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  EU AI ACT COMPLIANCE FOR MUSIC AI                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   TIMELINE                                                                  │
│   ────────                                                                  │
│                                                                             │
│   Aug 2024        Aug 2025           Aug 2026          Aug 2027            │
│      │               │                  │                 │                 │
│      ▼               ▼                  ▼                 ▼                 │
│   ┌──────┐       ┌──────────┐      ┌──────────┐     ┌──────────┐          │
│   │ Law  │       │ GPAI     │      │ High-Risk│     │ Regulated │          │
│   │Enters│       │Providers │      │ AI       │     │ Products  │          │
│   │Force │       │ Active   │      │ Systems  │     │           │          │
│   └──────┘       └──────────┘      └──────────┘     └──────────┘          │
│                       │                                                     │
│                       ▼                                                     │
│              ┌────────────────────────────────────┐                        │
│              │                                    │                         │
│              │  GPAI OBLIGATIONS (Music AI)       │                         │
│              │  ────────────────────────          │                         │
│              │  • Training data transparency      │                         │
│              │  • Copyright compliance summary    │                         │
│              │  • Data provenance documentation   │                         │
│              │                                    │                         │
│              └────────────────────────────────────┘                        │
│                       │                                                     │
│                       ▼                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                                                                     │  │
│   │  ATTRIBUTION VALUE: Provides L3 traceability for compliance            │  │
│   │  • Attribution data with provenance                                 │  │
│   │  • Permission registry (artist consent)                             │  │
│   │  • Audit trail for transparency requirements                        │  │
│   │                                                                     │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ NON-COMPLIANCE PENALTY: Up to €35M or 7% of global annual turnover  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Law Entry | `regulatory_milestone` | August 2024 law enters force |
| GPAI Active | `regulatory_milestone` | August 2025 GPAI obligations |
| High-Risk | `regulatory_milestone` | August 2026 high-risk systems |
| Regulated Products | `regulatory_milestone` | August 2027 full scope |
| GPAI Obligations | `compliance_requirement` | What music AI must do |
| System Value | `solution_component` | How the system helps |
| Penalty Warning | `risk_indicator` | €35M penalty exposure |

### Relationships/Flows

| From | To | Type | Label |
|------|-----|------|-------|
| GPAI Active | GPAI Obligations | arrow | "requires" |
| GPAI Obligations | System Value | arrow | "solved by" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "NON-COMPLIANCE PENALTY" | Up to €35M or 7% of global annual turnover | Bottom center |

## Text Content

### Labels (Max 30 chars each)

- "Law Enters Force"
- "GPAI Providers Active"
- "High-Risk AI Systems"
- "Regulated Products"
- "Training Data Transparency"
- "Copyright Compliance"
- "Data Provenance"
- "the system L3 Traceability"
- "€35M Penalty"

### Caption (for embedding)

EU AI Act compliance timeline for music AI: GPAI obligations (training data transparency) active from August 2025. The system provides L3 traceability enabling compliance. Non-compliance penalties up to €35M (DLA Piper 2025).

## Prompts for Nano Banana Pro

### Style Prompt

Professional regulatory timeline diagram on warm off-white background (#F8F6F0).
Economist-style data visualization with clear date markers.
Timeline flows left-to-right with milestone boxes.
GPAI obligations section uses teal (compliance color).
The system value proposition uses deep blue (brand color).
Penalty warning uses gold/amber for attention without alarm.
Clean, authoritative, suitable for executive presentations.

### Content Prompt

Create a regulatory compliance diagram showing:
- TOP: Timeline from Aug 2024 to Aug 2027
  - Aug 2024: "Law Enters Force" (gray)
  - Aug 2025: "GPAI Providers Active" (emphasized, teal)
  - Aug 2026: "High-Risk AI Systems" (gray)
  - Aug 2027: "Regulated Products" (gray)
- CENTER: "GPAI Obligations" box listing:
  - Training data transparency
  - Copyright compliance summary
  - Data provenance documentation
- LOWER: "System Value" box showing:
  - L3 traceability
  - Attribution data with provenance
  - Permission registry
  - Audit trail
- BOTTOM: Penalty callout "€35M or 7% global turnover"
- Arrow from GPAI milestone down to obligations, then to the system value

### Refinement Notes

- August 2025 milestone should be emphasized (current focus)
- The system value should clearly connect to GPAI requirements
- Penalty should be visible but not alarming
- Overall tone: authoritative, helpful, not fear-based

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "domain-05",
    "title": "EU AI Act Compliance for Music AI",
    "audience": "domain"
  },
  "content_architecture": {
    "primary_message": "EU AI Act requires training data transparency from August 2025; The system provides compliance pathway",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Law Entry",
        "role": "regulatory_milestone",
        "is_highlighted": false,
        "labels": ["Aug 2024", "Law Enters Force"]
      },
      {
        "name": "GPAI Active",
        "role": "regulatory_milestone",
        "is_highlighted": true,
        "labels": ["Aug 2025", "GPAI Providers", "Music AI"]
      },
      {
        "name": "High-Risk",
        "role": "regulatory_milestone",
        "is_highlighted": false,
        "labels": ["Aug 2026", "High-Risk AI"]
      },
      {
        "name": "Regulated Products",
        "role": "regulatory_milestone",
        "is_highlighted": false,
        "labels": ["Aug 2027", "Full Scope"]
      },
      {
        "name": "GPAI Obligations",
        "role": "compliance_requirement",
        "is_highlighted": true,
        "labels": ["Training transparency", "Copyright compliance", "Provenance"]
      },
      {
        "name": "System Value",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["L3 Traceability", "Permission registry", "Audit trail"]
      },
      {
        "name": "Penalty Warning",
        "role": "risk_indicator",
        "is_highlighted": true,
        "labels": ["€35M", "7% turnover"]
      }
    ],
    "relationships": [
      {"from": "GPAI Active", "to": "GPAI Obligations", "type": "arrow", "label": "requires"},
      {"from": "GPAI Obligations", "to": "System Value", "type": "arrow", "label": "solved by"}
    ],
    "callout_boxes": [
      {
        "heading": "NON-COMPLIANCE PENALTY",
        "body_text": "Up to €35M or 7% of global annual turnover",
        "position": "bottom-center"
      }
    ]
  }
}
```

## Alt Text

Timeline diagram: EU AI Act milestones from Aug 2024 to Aug 2027. August 2025 GPAI obligations require training data transparency. The system provides L3 traceability for compliance. Penalty up to €35M.

## Research Basis

- **[DLA Piper (August 2025)](https://www.dlapiper.com/en-us/insights/publications/2025/08/latest-wave-of-obligations-under-the-eu-ai-act-take-effect)**: "Latest wave of obligations under the EU AI Act take effect"
- **[EU AI Act Article 99](https://artificialintelligenceact.eu/article/99/)**: Official penalty provisions (€35M or 7% turnover)
- **[agentic-systems-research-2026-02-03.md](../../knowledge-base/technical/agentic-systems-research-2026-02-03.md)**: Section 4.1

## Status

- [x] Draft created
- [x] Content reviewed
- [x] Generated via Nano Banana Pro
- [x] Embedded in documentation
