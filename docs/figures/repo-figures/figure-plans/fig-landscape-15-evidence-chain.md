# fig-landscape-15: Evidence Chain: Detection to Forensics to Legal Claim

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-15 |
| **Title** | Evidence Chain: Detection to Forensics to Legal Claim |
| **Audience** | L4 (AI/ML Researcher) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

Shows that attribution is not a single operation but a multi-stage evidence chain where confidence degrades at each stage. Clarifies that detection, source identification, attribution quantification, and legal proof are four distinct problems with different evidence standards. Answers: "Why doesn't high-accuracy AI detection automatically mean we can attribute and compensate?"

## Key Message

A multi-stage evidence chain where confidence degrades at each stage -- detection does not equal attribution, and attribution does not equal legal proof.

## Visual Concept

Left-to-right flowchart with four stages connected by arrows. Each arrow shows confidence degradation (a decreasing percentage). Each stage is a distinct box showing the question it answers, the method used, and the confidence level achievable. The visual rhythm communicates progressive narrowing: wide confidence at detection, narrow at legal claim. A prominent bottom callout states the key insight: "Detection ≠ Attribution ≠ Legal Proof." Each stage uses a different confidence tier color (semantic tag, not hex).

```
+-----------------------------------------------------------------------+
|  EVIDENCE CHAIN                                                        |
|  ■ Detection to Forensics to Legal Claim                               |
+-----------------------------------------------------------------------+
|                                                                        |
|  STAGE 1           STAGE 2           STAGE 3           STAGE 4         |
|  ┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐  |
|  │          │      │          │      │          │      │          │  |
|  │ AI       │ 99%  │ SOURCE   │ ~70% │ ATTRIB.  │ ~40% │ LEGAL    │  |
|  │DETECTION │─────►│ IDENTIF. │─────►│ QUANTIF. │─────►│ CLAIM    │  |
|  │          │      │          │      │          │      │          │  |
|  │ Question:│      │ Question:│      │ Question:│      │ Question:│  |
|  │ Is this  │      │ Which    │      │ How much │      │ Does     │  |
|  │ AI-      │      │ training │      │ influence│      │ this     │  |
|  │generated?│      │ data?    │      │ per      │      │ meet     │  |
|  │          │      │          │      │ source?  │      │ copyright│  |
|  │ Method:  │      │ Method:  │      │ Method:  │      │ thresh.? │  |
|  │ Binary   │      │ Embedding│      │ TDA      │      │          │  |
|  │ classif. │      │ + TDA    │      │ percent. │      │ Method:  │  |
|  │          │      │          │      │ alloc.   │      │ Legal    │  |
|  │ Afchar   │      │ Choi     │      │          │      │ analysis │  |
|  │ 99.8%    │      │ et al.   │      │ Mlodo-   │      │          │  |
|  │ (clean)  │      │          │      │ zeniec   │      │ Dornis   │  |
|  │          │      │          │      │          │      │ & Stober │  |
|  │ ■ High   │      │ ■ Medium │      │ ■ Low    │      │ ■ Low    │  |
|  │ confid.  │      │ confid.  │      │ confid.  │      │ confid.  │  |
|  └──────────┘      └──────────┘      └──────────┘      └──────────┘  |
|                                                                        |
|  ┌─────────────────────────────────────────────────────────────────┐  |
|  │  Detection ≠ Attribution ≠ Legal Proof                          │  |
|  │  Each stage requires DIFFERENT evidence standards                │  |
|  └─────────────────────────────────────────────────────────────────┘  |
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
    bounds: [0, 0, 1920, 100]
    content: "EVIDENCE CHAIN"
    role: title

  - id: subtitle_zone
    bounds: [0, 100, 1920, 40]
    content: "Detection to Forensics to Legal Claim"
    role: subtitle

  - id: flow_area
    bounds: [60, 180, 1800, 680]
    role: content_area
    label: "Evidence chain stages"

  - id: footer_callout
    bounds: [60, 900, 1800, 120]
    role: callout_bar
    label: "Detection ≠ Attribution ≠ Legal Proof"

anchors:
  - id: stage_1_detection
    position: [80, 220]
    size: [380, 560]
    role: processing_stage
    label: "AI Detection"

  - id: stage_2_source
    position: [540, 220]
    size: [380, 560]
    role: processing_stage
    label: "Source Identification"

  - id: stage_3_attribution
    position: [1000, 220]
    size: [380, 560]
    role: processing_stage
    label: "Attribution Quantification"

  - id: stage_4_legal
    position: [1460, 220]
    size: [380, 560]
    role: processing_stage
    label: "Legal Claim"

  - id: arrow_1_2
    from: stage_1_detection
    to: stage_2_source
    type: arrow
    label: "confidence degrades ~99% to ~70%"

  - id: arrow_2_3
    from: stage_2_source
    to: stage_3_attribution
    type: arrow
    label: "confidence degrades ~70% to ~40%"

  - id: arrow_3_4
    from: stage_3_attribution
    to: stage_4_legal
    type: arrow
    label: "confidence degrades further"

  - id: conf_high
    position: [80, 720]
    size: [380, 40]
    role: confidence_high
    label: "High confidence"

  - id: conf_medium
    position: [540, 720]
    size: [380, 40]
    role: confidence_medium
    label: "Medium confidence"

  - id: conf_low_1
    position: [1000, 720]
    size: [380, 40]
    role: confidence_low
    label: "Low confidence"

  - id: conf_low_2
    position: [1460, 720]
    size: [380, 40]
    role: confidence_low
    label: "Low confidence"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "EVIDENCE CHAIN" in editorial caps with accent square |
| Subtitle | `label_editorial` | "Detection to Forensics to Legal Claim" |
| Stage 1: AI Detection | `processing_stage` | Binary classification: is this AI-generated? Afchar et al. 99.8% (clean samples) |
| Stage 2: Source ID | `processing_stage` | Which training data contributed? Embedding similarity + TDA methods (Choi et al.) |
| Stage 3: Attribution Quantification | `processing_stage` | How much influence per source? Percentage allocation (Mlodozeniec) |
| Stage 4: Legal Claim | `processing_stage` | Does this meet copyright threshold? Legal analysis (Dornis & Stober TISMIR) |
| Confidence high indicator | `confidence_high` | Stage 1 confidence level -- highest |
| Confidence medium indicator | `confidence_medium` | Stage 2 confidence level -- medium |
| Confidence low indicator | `confidence_low` | Stages 3-4 confidence level -- lowest |
| Degradation arrows | `data_flow` | Arrows between stages showing confidence drops |
| Footer callout | `callout_bar` | "Detection ≠ Attribution ≠ Legal Proof -- each requires different evidence standards" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Stage 1 | Stage 2 | arrow | Confidence degrades: detection to source ID |
| Stage 2 | Stage 3 | arrow | Confidence degrades: source ID to quantification |
| Stage 3 | Stage 4 | arrow | Confidence degrades: quantification to legal proof |
| High confidence | Stage 1 | contains | AI detection can be highly accurate |
| Medium confidence | Stage 2 | contains | Source ID is moderately reliable |
| Low confidence | Stages 3-4 | contains | Quantification and legal proof have wide uncertainty |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "DETECTION ≠ ATTRIBUTION ≠ LEGAL PROOF" | Each stage answers a fundamentally different question and requires different evidence standards -- high detection accuracy does not imply attribution is solved | footer, full width |
| "CONFIDENCE DEGRADES" | Each stage compounds uncertainty -- 99.8% detection accuracy does not mean 99.8% attribution accuracy | between stages, along arrows |
| "DORNIS & STOBER" | Legal threshold for copyright infringement requires substantial similarity AND access -- TDA methods provide evidence for the "access" prong but not similarity judgment | Stage 4 inset |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Stage 1: AI Detection"
- Label 2: "Stage 2: Source ID"
- Label 3: "Stage 3: Attribution Quant."
- Label 4: "Stage 4: Legal Claim"
- Label 5: "Is This AI-Generated?"
- Label 6: "Which Training Data?"
- Label 7: "How Much Influence?"
- Label 8: "Copyright Threshold?"
- Label 9: "Binary Classification"
- Label 10: "Embedding + TDA"
- Label 11: "Percentage Allocation"
- Label 12: "Legal Analysis"
- Label 13: "Afchar 99.8% (clean)"
- Label 14: "Confidence Degrades"
- Label 15: "Detection ≠ Attribution"

### Caption (for embedding in documentation)

The evidence chain from AI detection to legal claim involves four distinct stages with degrading confidence: AI detection (binary, 99.8% on clean samples), source identification (which training data, ~70% reliable), attribution quantification (how much influence, ~40%), and legal claim (copyright threshold). Each stage requires different evidence standards; detection accuracy does not propagate to attribution or legal proof. Academic sources: Afchar et al. ICASSP 2025, Choi et al. 2025, Mlodozeniec 2024, Dornis & Stober TISMIR.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Background MUST be warm cream (#f6f3e6)**.
5. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
6. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
7. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

8. Afchar et al. 99.8% accuracy is specifically on CLEAN samples -- do NOT omit the "clean" qualifier.
9. The confidence degradation percentages (~70%, ~40%) are ILLUSTRATIVE, not measured -- do NOT present them as empirical results.
10. Dornis & Stober is published in TISMIR -- do NOT cite a different journal.
11. Do NOT claim this evidence chain is implemented in the scaffold -- it is a conceptual framework.
12. "Legal claim" refers to copyright threshold analysis -- do NOT simplify to "sue someone."
13. Mlodozeniec (2024) is the unlearning-based TDA reference for percentage allocation -- do NOT confuse with Koh & Liang (influence functions).
14. The four stages are SEQUENTIAL -- do NOT present them as parallel or interchangeable.
15. Do NOT imply any single method handles all four stages -- no such method exists.

## Alt Text

Four-stage evidence chain from AI detection to legal claim showing confidence degradation at each stage

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "landscape-15",
    "title": "Evidence Chain: Detection to Forensics to Legal Claim",
    "audience": "L4",
    "layout_template": "C"
  },
  "content_architecture": {
    "primary_message": "Detection does not equal attribution, and attribution does not equal legal proof -- confidence degrades at each stage.",
    "layout_flow": "left-to-right-flow",
    "key_structures": [
      {
        "name": "Stage 1: AI Detection",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["AI Detection", "Binary", "Afchar 99.8%"]
      },
      {
        "name": "Stage 2: Source Identification",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Source ID", "Embedding + TDA", "~70%"]
      },
      {
        "name": "Stage 3: Attribution Quantification",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Attribution Quant.", "Percentage", "~40%"]
      },
      {
        "name": "Stage 4: Legal Claim",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["Legal Claim", "Copyright threshold", "Dornis & Stober"]
      }
    ],
    "relationships": [
      {
        "from": "Stage 1",
        "to": "Stage 2",
        "type": "arrow",
        "label": "confidence degrades"
      },
      {
        "from": "Stage 2",
        "to": "Stage 3",
        "type": "arrow",
        "label": "confidence degrades"
      },
      {
        "from": "Stage 3",
        "to": "Stage 4",
        "type": "arrow",
        "label": "confidence degrades"
      }
    ],
    "callout_boxes": [
      {
        "heading": "DETECTION ≠ ATTRIBUTION ≠ LEGAL PROOF",
        "body_text": "Each stage requires different evidence standards",
        "position": "footer"
      },
      {
        "heading": "CONFIDENCE DEGRADES",
        "body_text": "99.8% detection does not mean 99.8% attribution accuracy",
        "position": "between-stages"
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
- [x] Audience level correct (L4)
- [x] Layout template identified (C)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
