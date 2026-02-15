# fig-landscape-10: Post-hoc vs By-Design: Two Paradigms Converging

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-10 |
| **Title** | Post-hoc vs By-Design: Two Paradigms Converging |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | D (Split-Panel) |

## Purpose

Shows that the attribution field is not monolithic but consists of two fundamentally different paradigms -- post-hoc analysis of existing models and by-design provenance built into new models -- and that the most important unsolved problems live in the hybrid zone where they converge. Answers: "Where should research effort focus to advance music attribution?"

## Key Message

The field is converging toward hybrid attribution -- the hybrid zone where post-hoc meets by-design is where all the unsolved problems live.

## Visual Concept

Classic split-panel with left side (post-hoc) and right side (by-design) connected by a central convergence zone rendered as an overlapping region. The convergence zone is visually emphasized with an accent border to show it as the area of active research. Below, A0-A3 assurance levels bridge both paradigms as a unifying framework. The left panel is denser (more existing work); the right panel is sparser (emerging).

```
+-----------------------------------------------------------------------+
|  TWO PARADIGMS CONVERGING                                              |
|  ■ Post-hoc Analysis vs Attribution-by-Design                          |
+-----------------------------------------------------------------------+
|                                                                        |
|  POST-HOC TDA              HYBRID ZONE           BY-DESIGN             |
|  ════════════              ═══════════           ═════════             |
|                                                                        |
|  ┌───────────────┐    ┌─────────────────┐    ┌───────────────┐        |
|  │               │    │                 │    │               │        |
|  │ Works on      │    │  OPEN RESEARCH  │    │ Requires new  │        |
|  │ existing      │    │  PROBLEMS       │    │ architecture  │        |
|  │ models        │    │  ─────────────  │    │ adoption      │        |
|  │               │    │                 │    │               │        |
|  │ Sony NeurIPS  │    │  How to combine │    │ Morreale      │        |
|  │ influence     │◄──►│  post-hoc       │◄──►│ et al. 2025   │        |
|  │ functions     │    │  evidence with  │    │               │        |
|  │               │    │  by-design      │    │ Inference-    │        |
|  │ Computa-      │    │  provenance?    │    │ time          │        |
|  │ tionally      │    │                 │    │ provenance    │        |
|  │ expensive     │    │  Calibration    │    │               │        |
|  │               │    │  across methods │    │ Scalable      │        |
|  │ Retroactive   │    │                 │    │ but requires  │        |
|  │ only          │    │  Legal standard │    │ adoption      │        |
|  │               │    │  alignment      │    │               │        |
|  └───────────────┘    └─────────────────┘    └───────────────┘        |
|                                                                        |
|  ─────────────────────────────────────────────────────────────────     |
|  ASSURANCE LEVELS BRIDGE BOTH PARADIGMS                                |
|  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐                          |
|  │ A0    │──│ A1    │──│ A2    │──│ A3    │                          |
|  │ None  │  │Single │  │Multi  │  │Artist │                          |
|  │       │  │source │  │source │  │verify │                          |
|  └───────┘  └───────┘  └───────┘  └───────┘                          |
|  Post-hoc can reach A1-A2     By-design can reach A2-A3               |
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
    content: "TWO PARADIGMS CONVERGING"
    role: title

  - id: subtitle_zone
    bounds: [0, 100, 1920, 40]
    content: "Post-hoc Analysis vs Attribution-by-Design"
    role: subtitle

  - id: left_panel
    bounds: [60, 180, 540, 520]
    role: content_area
    label: "POST-HOC TDA"

  - id: center_hybrid
    bounds: [660, 180, 600, 520]
    role: content_area
    label: "HYBRID ZONE"

  - id: right_panel
    bounds: [1320, 180, 540, 520]
    role: content_area
    label: "BY-DESIGN"

  - id: accent_divider
    bounds: [60, 740, 1800, 2]
    role: accent_line

  - id: assurance_bridge
    bounds: [60, 780, 1800, 260]
    role: content_area
    label: "ASSURANCE LEVELS BRIDGE BOTH PARADIGMS"

anchors:
  - id: posthoc_block
    position: [80, 200]
    size: [500, 480]
    role: problem_statement
    label: "Post-hoc TDA"

  - id: hybrid_block
    position: [680, 200]
    size: [560, 480]
    role: problem_statement
    label: "Open Research Problems"

  - id: bydesign_block
    position: [1340, 200]
    size: [500, 480]
    role: solution_component
    label: "Attribution-by-Design"

  - id: assurance_a0
    position: [120, 820]
    size: [160, 120]
    role: assurance_a0
    label: "A0 None"

  - id: assurance_a1
    position: [340, 820]
    size: [160, 120]
    role: assurance_a1
    label: "A1 Single Source"

  - id: assurance_a2
    position: [560, 820]
    size: [160, 120]
    role: assurance_a2
    label: "A2 Multi-Source"

  - id: assurance_a3
    position: [780, 820]
    size: [160, 120]
    role: assurance_a3
    label: "A3 Artist-Verified"

  - id: convergence_left
    from: posthoc_block
    to: hybrid_block
    type: bidirectional_arrow
    label: "evidence flows"

  - id: convergence_right
    from: hybrid_block
    to: bydesign_block
    type: bidirectional_arrow
    label: "provenance flows"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "TWO PARADIGMS CONVERGING" in editorial caps with accent square |
| Subtitle | `label_editorial` | "Post-hoc Analysis vs Attribution-by-Design" |
| Post-hoc panel | `problem_statement` | Left panel: Sony NeurIPS, influence functions, computationally expensive, retroactive only |
| Hybrid zone | `problem_statement` | Center panel: open research problems -- combining evidence, calibration, legal alignment |
| By-design panel | `solution_component` | Right panel: Morreale et al. 2025, inference-time provenance, scalable, requires adoption |
| Assurance bridge | `data_flow` | A0-A3 levels shown as progression, bridging both paradigms |
| A0 level | `assurance_a0` | No provenance data |
| A1 level | `assurance_a1` | Single source attestation |
| A2 level | `assurance_a2` | Multiple independent sources agree |
| A3 level | `assurance_a3` | Artist-verified provenance |
| Accent divider | `callout_bar` | Horizontal accent line above assurance section |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Post-hoc panel | Hybrid zone | bidirectional | Evidence flows into hybrid |
| By-design panel | Hybrid zone | bidirectional | Provenance flows into hybrid |
| Post-hoc | A1-A2 | arrow | Can reach A1-A2 assurance |
| By-design | A2-A3 | arrow | Can reach A2-A3 assurance |
| A0 | A1 | progression | Assurance increases |
| A1 | A2 | progression | Assurance increases |
| A2 | A3 | progression | Assurance increases |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "OPEN PROBLEMS" | How to calibrate confidence when combining post-hoc evidence (correlation) with by-design provenance (causal) into a single score? | center hybrid zone |
| "RETROACTIVE LIMIT" | Post-hoc methods can never fully prove causation for existing closed-source models -- only approximate it | bottom of left panel |
| "ADOPTION BARRIER" | By-design requires model developers to opt in -- economic incentives must align with technical capability | bottom of right panel |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "Post-hoc TDA"
- Label 2: "Attribution-by-Design"
- Label 3: "Hybrid Zone"
- Label 4: "Open Research Problems"
- Label 5: "Sony NeurIPS"
- Label 6: "Influence Functions"
- Label 7: "Morreale et al. 2025"
- Label 8: "Inference-Time Provenance"
- Label 9: "Computationally Expensive"
- Label 10: "Requires Adoption"
- Label 11: "A0 None"
- Label 12: "A1 Single Source"
- Label 13: "A2 Multi-Source"
- Label 14: "A3 Artist-Verified"

### Caption (for embedding in documentation)

Two attribution paradigms -- post-hoc analysis of existing models and attribution-by-design in new architectures -- are converging toward a hybrid zone where the hardest open problems live: calibrating confidence across fundamentally different evidence types. A0-A3 assurance levels provide a unifying framework that spans both paradigms.

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

8. "Sony NeurIPS" refers to Choi et al. (2025) work on unlearning-based TDA presented at NeurIPS -- do NOT invent a different venue.
9. Attribution-by-Design is specifically from Morreale et al. (2025) -- do NOT attribute it to other authors.
10. A0-A3 assurance levels are from Teikari (2026) -- they are NOT an industry standard.
11. The hybrid zone is speculative/aspirational -- do NOT present it as an existing system.
12. Do NOT claim post-hoc methods can reach A3 (artist-verified) -- that requires by-design cooperation.
13. Do NOT claim by-design alone can reach A3 without artist participation.
14. The convergence is a research direction, not a deployed system.

## Alt Text

Split panel showing post-hoc and by-design attribution paradigms converging toward hybrid zone with A0-A3 bridge

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "landscape-10",
    "title": "Post-hoc vs By-Design: Two Paradigms Converging",
    "audience": "L2",
    "layout_template": "D"
  },
  "content_architecture": {
    "primary_message": "The hybrid zone where post-hoc meets by-design is where all the unsolved problems live.",
    "layout_flow": "left-center-right",
    "key_structures": [
      {
        "name": "Post-hoc TDA",
        "role": "problem_statement",
        "is_highlighted": true,
        "labels": ["Post-hoc TDA", "Sony NeurIPS", "Retroactive"]
      },
      {
        "name": "Hybrid Zone",
        "role": "problem_statement",
        "is_highlighted": true,
        "labels": ["Open Research Problems", "Calibration", "Legal alignment"]
      },
      {
        "name": "Attribution-by-Design",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["Morreale et al. 2025", "Inference-time provenance"]
      },
      {
        "name": "Assurance Bridge",
        "role": "data_flow",
        "is_highlighted": false,
        "labels": ["A0 None", "A1 Single", "A2 Multi", "A3 Verified"]
      }
    ],
    "relationships": [
      {
        "from": "Post-hoc",
        "to": "Hybrid Zone",
        "type": "bidirectional",
        "label": "evidence flows"
      },
      {
        "from": "By-design",
        "to": "Hybrid Zone",
        "type": "bidirectional",
        "label": "provenance flows"
      },
      {
        "from": "Post-hoc",
        "to": "A1-A2",
        "type": "arrow",
        "label": "reachable assurance"
      },
      {
        "from": "By-design",
        "to": "A2-A3",
        "type": "arrow",
        "label": "reachable assurance"
      }
    ],
    "callout_boxes": [
      {
        "heading": "OPEN PROBLEMS",
        "body_text": "How to calibrate confidence across fundamentally different evidence types?",
        "position": "center"
      },
      {
        "heading": "RETROACTIVE LIMIT",
        "body_text": "Post-hoc can never fully prove causation for closed-source models",
        "position": "bottom-left"
      },
      {
        "heading": "ADOPTION BARRIER",
        "body_text": "By-design requires model developers to opt in",
        "position": "bottom-right"
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
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
