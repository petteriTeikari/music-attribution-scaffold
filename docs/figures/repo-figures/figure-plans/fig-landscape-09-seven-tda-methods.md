# fig-landscape-09: Seven TDA Methods: What Each Actually Measures

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-09 |
| **Title** | Seven TDA Methods: What Each Actually Measures |
| **Audience** | L4 (AI/ML Researcher) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Disambiguates seven distinct training data attribution methods by showing what each fundamentally measures, what model access it requires, and how it scales. Answers: "Why can't I just use any TDA method interchangeably -- what are the differences that matter?"

## Key Message

Confusing "similarity" with "causal contribution" is the most common error in attribution -- 7 methods measure fundamentally different quantities.

## Visual Concept

Seven panels arranged in a 4-over-3 grid. Each panel is a compact card showing method name, what it measures, access requirement, and scalability. A horizontal axis at the top classifies them on a spectrum from "causal" to "corroborative" to "proactive." Color-coded semantic tags distinguish white-box (model internals required) from black-box (output only) methods. An accent line separates the two rows.

```
+-----------------------------------------------------------------------+
|  SEVEN TDA METHODS                                                     |
|  ■ What Each Actually Measures                                         |
+-----------------------------------------------------------------------+
|  CAUSAL ◄────────────────────────────────────────► CORROBORATIVE       |
|                                                                        |
|  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌────────────┐ |
|  │ 1. UNLEARNING │  │ 2. INFLUENCE │  │ 3. TOKEN     │  │ 4. INFER-  │ |
|  │   -BASED TDA  │  │   FUNCTIONS  │  │   FLOW       │  │   TIME     │ |
|  │               │  │              │  │   TRACKING   │  │   COND.    │ |
|  │ Measures:     │  │ Measures:    │  │ Measures:    │  │ Measures:  │ |
|  │ Causal        │  │ Approx.      │  │ Activation   │  │ Direct     │ |
|  │ contribution  │  │ counterfact. │  │ patterns     │  │ causal     │ |
|  │               │  │              │  │              │  │ link       │ |
|  │ ■ White-box   │  │ ■ White-box  │  │ ■ White-box  │  │ ■ By-      │ |
|  │ ■ O(n) costly │  │ ■ O(1) appr. │  │ ■ Mechanist. │  │   design   │ |
|  └──────────────┘  └──────────────┘  └──────────────┘  └────────────┘ |
|  ─────────────────────────────────────────────────────────────────     |
|  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                 |
|  │ 5. EMBEDDING │  │ 6. REPLICA-  │  │ 7. WATER-    │                 |
|  │   SIMILARITY  │  │   TION DET.  │  │   MARKING    │                 |
|  │               │  │              │  │              │                 |
|  │ Measures:     │  │ Measures:    │  │ Measures:    │                 |
|  │ Perceptual    │  │ Exact        │  │ Binary       │                 |
|  │ similarity    │  │ memorization │  │ presence     │                 |
|  │               │  │              │  │              │                 |
|  │ ■ Black-box   │  │ ■ Black-box  │  │ ■ Proactive  │                 |
|  │ ■ Scalable    │  │ ■ Forensic   │  │ ■ Embedded   │                 |
|  └──────────────┘  └──────────────┘  └──────────────┘                 |
|                                                                        |
|  ■ "Similar" ≠ "caused by" -- each method answers a different question |
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
    content: "SEVEN TDA METHODS"
    role: title

  - id: subtitle_zone
    bounds: [0, 100, 1920, 40]
    content: "What Each Actually Measures"
    role: subtitle

  - id: spectrum_axis
    bounds: [60, 160, 1800, 40]
    role: data_flow
    label: "CAUSAL to CORROBORATIVE"

  - id: row_1
    bounds: [60, 220, 1800, 340]
    role: content_area
    label: "Methods 1-4"

  - id: accent_divider
    bounds: [60, 570, 1800, 2]
    role: accent_line

  - id: row_2
    bounds: [60, 590, 1360, 340]
    role: content_area
    label: "Methods 5-7"

  - id: footer_callout
    bounds: [60, 960, 1800, 80]
    role: callout_bar
    label: "Similar ≠ caused by"

anchors:
  - id: panel_unlearning
    position: [60, 220]
    size: [420, 320]
    role: solution_component
    label: "Unlearning-Based TDA"

  - id: panel_influence
    position: [510, 220]
    size: [420, 320]
    role: solution_component
    label: "Influence Functions"

  - id: panel_token_flow
    position: [960, 220]
    size: [420, 320]
    role: solution_component
    label: "Token Flow Tracking"

  - id: panel_inference_time
    position: [1410, 220]
    size: [420, 320]
    role: solution_component
    label: "Inference-Time Conditioning"

  - id: panel_embedding
    position: [60, 590]
    size: [420, 320]
    role: solution_component
    label: "Embedding Similarity"

  - id: panel_replication
    position: [510, 590]
    size: [420, 320]
    role: solution_component
    label: "Replication Detection"

  - id: panel_watermarking
    position: [960, 590]
    size: [420, 320]
    role: solution_component
    label: "Watermarking"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "SEVEN TDA METHODS" in editorial caps with accent square |
| Subtitle | `label_editorial` | "What Each Actually Measures" |
| Causal-Corroborative axis | `data_flow` | Horizontal spectrum from causal to corroborative |
| Unlearning-Based TDA panel | `solution_component` | Counterfactual, white-box, measures causal contribution, O(n) retrain cost |
| Influence Functions panel | `solution_component` | Counterfactual approximation, white-box, Hessian-based, O(1) per query |
| Token Flow Tracking panel | `solution_component` | Mechanistic, white-box, activation pattern tracing |
| Inference-Time Conditioning panel | `solution_component` | By-design, direct causal link, requires architecture change |
| Embedding Similarity panel | `solution_component` | Corroborative, black-box, perceptual similarity, scalable |
| Replication Detection panel | `solution_component` | Forensic, black-box, exact memorization detection (MiRA/SSIMuse) |
| Watermarking panel | `solution_component` | Proactive, embedded signal, binary presence/absence |
| Accent divider | `callout_bar` | Horizontal accent line separating rows |
| Footer callout | `callout_bar` | "Similar ≠ caused by -- each method answers a different question" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Causal end | Unlearning-Based TDA | position | Strongest causal claim |
| Causal end | Influence Functions | position | Approximate causal claim |
| Causal end | Inference-Time Cond. | position | Direct causal by design |
| Corroborative end | Embedding Similarity | position | Correlation, not causation |
| Corroborative end | Replication Detection | position | Memorization evidence |
| Proactive category | Watermarking | position | Embedded, not inferred |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "SIMILARITY ≠ CAUSATION" | Embedding similarity shows two things sound alike but cannot prove one caused the other -- this is the most common conflation in attribution discourse | footer bar |
| "WHITE-BOX BARRIER" | Methods 1-3 require access to model internals -- impossible for closed-source generative models like Suno, Udio | top-right margin |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Unlearning-Based TDA"
- Label 2: "Influence Functions"
- Label 3: "Token Flow Tracking"
- Label 4: "Inference-Time Conditioning"
- Label 5: "Embedding Similarity"
- Label 6: "Replication Detection"
- Label 7: "Watermarking"
- Label 8: "Causal Contribution"
- Label 9: "Approx. Counterfactual"
- Label 10: "Perceptual Similarity"
- Label 11: "Binary Presence"
- Label 12: "Activation Patterns"
- Label 13: "Exact Memorization"
- Label 14: "Direct Causal Link"
- Label 15: "White-box Required"
- Label 16: "Black-box Compatible"

### Caption (for embedding in documentation)

Seven training data attribution methods compared by what they fundamentally measure (causal contribution vs perceptual similarity vs binary presence), what model access they require (white-box vs black-box), and how they scale. The most common error in attribution discourse is conflating similarity with causation.

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

8. There are exactly 7 methods. Do NOT add or remove any.
9. Unlearning-based TDA is from Mlodozeniec (2024) -- do NOT attribute it to other authors.
10. Influence functions originate from Koh & Liang (2017) -- do NOT cite a different year.
11. MiRA is a specific replication detection method -- do NOT conflate it with general similarity search.
12. Inference-time conditioning is from Morreale et al. (2025) -- do NOT describe it as post-hoc.
13. Do NOT claim any method "solves" attribution -- each measures a different quantity.
14. Token flow tracking is mechanistic interpretability applied to attribution -- do NOT describe it as a loss function.
15. Embedding similarity (CLAP, CLMR) is corroborative ONLY -- it cannot prove causal contribution.

## Alt Text

Seven TDA methods compared: what each measures, model access needed, and scalability on causal-to-corroborative axis

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "landscape-09",
    "title": "Seven TDA Methods: What Each Actually Measures",
    "audience": "L4",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Confusing similarity with causal contribution is the most common error -- 7 methods measure fundamentally different quantities.",
    "layout_flow": "grid-4-over-3",
    "key_structures": [
      {
        "name": "Unlearning-Based TDA",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["Causal contribution", "White-box", "O(n) retrain"]
      },
      {
        "name": "Influence Functions",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["Approx. counterfactual", "White-box", "Hessian-based"]
      },
      {
        "name": "Token Flow Tracking",
        "role": "solution_component",
        "is_highlighted": false,
        "labels": ["Activation patterns", "White-box", "Mechanistic"]
      },
      {
        "name": "Inference-Time Conditioning",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["Direct causal link", "By-design", "Requires adoption"]
      },
      {
        "name": "Embedding Similarity",
        "role": "solution_component",
        "is_highlighted": false,
        "labels": ["Perceptual similarity", "Black-box", "Scalable"]
      },
      {
        "name": "Replication Detection",
        "role": "solution_component",
        "is_highlighted": false,
        "labels": ["Exact memorization", "Black-box", "Forensic"]
      },
      {
        "name": "Watermarking",
        "role": "solution_component",
        "is_highlighted": false,
        "labels": ["Binary presence", "Proactive", "Embedded"]
      }
    ],
    "relationships": [
      {
        "from": "Causal end",
        "to": "Unlearning-Based TDA",
        "type": "position",
        "label": "strongest causal claim"
      },
      {
        "from": "Corroborative end",
        "to": "Embedding Similarity",
        "type": "position",
        "label": "correlation only"
      }
    ],
    "callout_boxes": [
      {
        "heading": "SIMILARITY ≠ CAUSATION",
        "body_text": "Embedding similarity cannot prove one thing caused another",
        "position": "footer"
      },
      {
        "heading": "WHITE-BOX BARRIER",
        "body_text": "Methods 1-3 require model internals -- impossible for closed-source models",
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
- [x] Audience level correct (L4)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
