# fig-landscape-32: From Landscape to Product: The Meta-Loop

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-32 |
| **Title** | From Landscape to Product: The Meta-Loop |
| **Audience** | L3 (Engineer) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | C (Flowchart) |

## Purpose

This figure closes the loop between landscape analysis and product development, showing that the probabilistic PRD is a living document continuously refined by market intelligence. It demonstrates the meta-process: landscape scanning feeds market intelligence, which updates PRD priors (probability weights on decision nodes), which drives architecture decisions, which shapes the product, which changes the landscape -- creating a feedback loop that makes the scaffold's probabilistic PRD uniquely adaptive.

## Key Message

Landscape scanning feeds market intelligence, which updates PRD priors, which drives architecture decisions, which shapes the product, which changes the landscape -- this is the meta-loop that makes the probabilistic PRD a living document.

## Visual Concept

A circular flowchart with six steps arranged clockwise around a central artifact -- the probabilistic PRD. Each step is a labeled node connected by directional arrows forming a continuous loop. The PRD sits in the center, visually receiving inputs from and sending outputs to all six steps. Coral accent lines highlight the feedback arrows (steps 5-6 feeding back to step 1). The visual emphasizes CONTINUOUS UPDATING, not a one-time linear process.

```
+---------------------------------------------------------------+
|  FROM LANDSCAPE TO PRODUCT                                     |
|  ■ The Meta-Loop: Continuous PRD Updating                      |
+---------------------------------------------------------------+
|                                                                |
|             ┌──────────────────────┐                           |
|             │  I. LANDSCAPE        │                           |
|             │     SCANNING         │                           |
|             │  This document,      │                           |
|             │  competitors,        │                           |
|             │  regulation          │◀─────────────────┐        |
|             └──────────┬───────────┘                  │        |
|                        │                              │        |
|                        ▼                              │        |
|             ┌──────────────────────┐                  │        |
|             │  II. MARKET          │                  │        |
|             │      INTELLIGENCE    │                  │        |
|             │  Patterns, gaps,     │                  │        |
|             │  trend analysis      │                  │        |
|             └──────────┬───────────┘                  │        |
|                        │                              │        |
|                        ▼                              │        |
|             ┌──────────────────────┐                  │        |
|             │  III. PRD PRIOR      │                  │        |
|             │       UPDATES        │     ┌────────┐   │        |
|             │  Update probability  │◀───▶│  PRD   │   │        |
|             │  weights on decision │     │(center)│   │        |
|             │  nodes               │     └────────┘   │        |
|             └──────────┬───────────┘                  │        |
|                        │                              │        |
|                        ▼                              │        |
|             ┌──────────────────────┐                  │        |
|             │  IV. ARCHITECTURE    │                  │        |
|             │      DECISIONS       │                  │        |
|             │  Choose impl paths   │                  │        |
|             │  based on priors     │                  │        |
|             └──────────┬───────────┘                  │        |
|                        │                              │        |
|                        ▼                              │        |
|             ┌──────────────────────┐                  │        |
|             │  V. PRODUCT          │                  │        |
|             │     EVOLUTION        │                  │        |
|             │  Build features,     │                  │        |
|             │  ship code           │                  │        |
|             └──────────┬───────────┘                  │        |
|                        │                              │        |
|                        ▼                              │        |
|             ┌──────────────────────┐                  │        |
|             │  VI. MARKET          │                  │        |
|             │      RESPONSE        │──────────────────┘        |
|             │  User feedback,      │                           |
|             │  competitive resp,   │                           |
|             │  regulatory changes  │                           |
|             └──────────────────────┘                           |
|                                                                |
|  ■ The probabilistic PRD is designed for exactly this          |
|    continuous updating — each scan refines decision priors     |
+---------------------------------------------------------------+
```

## Spatial Anchors

```yaml
canvas:
  width: 1920
  height: 1080
  background: warm_cream

title_block:
  position: [60, 40]
  width: 1800
  height: 80
  elements:
    - type: heading_display
      text: "FROM LANDSCAPE TO PRODUCT"
    - type: label_editorial
      text: "The Meta-Loop: Continuous PRD Updating"

center_prd:
  position: [960, 540]
  width: 300
  height: 200
  label: "PROBABILISTIC PRD"
  elements:
    - { type: heading_display, text: "PRD" }
    - { type: data_mono, text: "30 decision nodes" }
    - { type: data_mono, text: "5 levels" }
    - { type: data_mono, text: "Probability weights" }
    - { type: label_editorial, text: "The Living Document" }

step_1_scanning:
  position: [960, 140]
  width: 400
  height: 120
  label: "I. LANDSCAPE SCANNING"
  elements:
    - { type: processing_stage, text: "Monitor competitors" }
    - { type: processing_stage, text: "Track regulation" }
    - { type: processing_stage, text: "Survey academic publications" }
    - { type: label_editorial, text: "This document is one scan cycle" }

step_2_intelligence:
  position: [1400, 280]
  width: 400
  height: 120
  label: "II. MARKET INTELLIGENCE"
  elements:
    - { type: processing_stage, text: "Extract patterns from landscape" }
    - { type: processing_stage, text: "Identify gaps and opportunities" }
    - { type: processing_stage, text: "Trend analysis and forecasting" }

step_3_priors:
  position: [1400, 480]
  width: 400
  height: 120
  label: "III. PRD PRIOR UPDATES"
  elements:
    - { type: decision_point, text: "Update probability weights" }
    - { type: data_mono, text: "Bayesian updating on decision nodes" }
    - { type: data_mono, text: "Shift selected/deferred options" }

step_4_architecture:
  position: [1400, 680]
  width: 400
  height: 120
  label: "IV. ARCHITECTURE DECISIONS"
  elements:
    - { type: decision_point, text: "Choose implementation paths" }
    - { type: data_mono, text: "Based on updated priors" }
    - { type: data_mono, text: "Archetype-specific overlays" }

step_5_product:
  position: [960, 820]
  width: 400
  height: 120
  label: "V. PRODUCT EVOLUTION"
  elements:
    - { type: solution_component, text: "Build features" }
    - { type: solution_component, text: "Ship code" }
    - { type: solution_component, text: "Deploy to users" }

step_6_response:
  position: [520, 680]
  width: 400
  height: 120
  label: "VI. MARKET RESPONSE"
  elements:
    - { type: data_flow, text: "User feedback" }
    - { type: data_flow, text: "Competitive response" }
    - { type: data_flow, text: "Regulatory changes" }

feedback_arrow:
  from: step_6_response
  to: step_1_scanning
  type: feedback
  label: "Loop closes — market response triggers next scan"
  style: accent_line

insight_callout:
  position: [60, 980]
  width: 1800
  height: 50
  elements:
    - type: callout_bar
      text: "The probabilistic PRD is designed for exactly this continuous updating — each scan refines decision priors"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "FROM LANDSCAPE TO PRODUCT" with coral accent square |
| Subtitle | `label_editorial` | "The Meta-Loop: Continuous PRD Updating" |
| Center PRD | `selected_option` | Probabilistic PRD as the central living artifact (30 nodes, 5 levels) |
| Step 1 | `processing_stage` | Landscape Scanning: monitoring competitors, regulation, academia |
| Step 2 | `processing_stage` | Market Intelligence: extracting patterns, identifying gaps |
| Step 3 | `decision_point` | PRD Prior Updates: Bayesian updating on decision node weights |
| Step 4 | `decision_point` | Architecture Decisions: choosing implementation paths from updated priors |
| Step 5 | `solution_component` | Product Evolution: building features, shipping code |
| Step 6 | `data_flow` | Market Response: user feedback, competitive response, regulatory changes |
| Feedback arrow | `callout_bar` | Visual arrow from Step 6 back to Step 1, closing the loop |
| Step numerals | `section_numeral` | Roman numerals I-VI for each step |
| Insight callout | `callout_bar` | "Designed for continuous updating" at bottom |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Landscape Scanning | Market Intelligence | sequential | "Raw data becomes patterns" |
| Market Intelligence | PRD Prior Updates | sequential | "Patterns become probability updates" |
| PRD Prior Updates | Center PRD | bidirectional | "Read current priors, write updated priors" |
| PRD Prior Updates | Architecture Decisions | sequential | "Updated priors drive decisions" |
| Architecture Decisions | Product Evolution | sequential | "Decisions become code" |
| Product Evolution | Market Response | sequential | "Product meets market" |
| Market Response | Landscape Scanning | feedback | "Response triggers next scan cycle" |
| Center PRD | All steps | reference | "PRD is consulted and updated throughout" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Why Probabilistic | "Fixed PRDs become stale; probabilistic PRDs adapt -- each landscape scan is a Bayesian update" | Right of center PRD |
| This Document | "This landscape analysis is Step 1 of the meta-loop -- it feeds directly into PRD prior updates" | Below Step 1 |
| Continuous, Not One-Time | "The loop has no end -- market response from shipped features triggers the next scan cycle" | Below feedback arrow |

## Text Content

### Labels (Max 30 chars each)

- Landscape Scanning
- Market Intelligence
- PRD Prior Updates
- Architecture Decisions
- Product Evolution
- Market Response
- Probabilistic PRD
- 30 Decision Nodes
- 5 Levels
- Probability Weights
- Bayesian Updating
- Monitor Competitors
- Track Regulation
- Extract Patterns
- Identify Gaps
- Choose Impl Paths
- Build Features
- Ship Code
- User Feedback
- Competitive Response

### Caption (for embedding in documentation)

The meta-loop connects landscape analysis to product development through six continuous steps: landscape scanning (monitoring competitors, regulation, and academia) feeds market intelligence (pattern extraction and gap analysis), which triggers PRD prior updates (Bayesian updating on the probabilistic PRD's 30 decision nodes), driving architecture decisions (choosing implementation paths based on updated probability weights), shaping product evolution (building and shipping features), and generating market response (user feedback, competitive dynamics, regulatory changes) that feeds back into the next landscape scan. The probabilistic PRD sits at the center as a living document, continuously refined by this loop.

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

1. There are exactly SIX steps in the loop -- do NOT add or remove steps.
2. The loop is CIRCULAR (step 6 feeds back to step 1) -- do NOT render as linear.
3. The PRD is at the CENTER, not as one of the six steps -- it is the ARTIFACT being updated, not a step.
4. "Probabilistic PRD" means decision nodes with PROBABILITY WEIGHTS -- do NOT reduce to "a document."
5. "Bayesian updating" is the specific method for prior updates -- do NOT generalize to "updating."
6. Do NOT imply the loop runs on a fixed schedule -- it is EVENT-DRIVEN (triggered by significant landscape changes).
7. Do NOT show this as a sprint/agile cycle -- it operates at a STRATEGIC level, not sprint level.
8. The feedback arrow (step 6 to step 1) is the KEY VISUAL ELEMENT -- it must be prominent.
9. "30 decision nodes, 5 levels" refers to the scaffold's actual PRD structure -- do NOT change these numbers.
10. Do NOT include specific PRD node names -- keep the figure at the meta-process level.

## Alt Text

Six-step circular meta-loop: landscape scan to market intel to PRD update to architecture to product to response.

## JSON Export Block

```json
{
  "id": "fig-landscape-32",
  "title": "From Landscape to Product: The Meta-Loop",
  "audience": "L3",
  "priority": "P1",
  "layout": "C",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Speculate",
  "novelty": 3,
  "loop_steps": [
    {
      "step": 1,
      "name": "Landscape Scanning",
      "activities": ["Monitor competitors", "Track regulation", "Survey academic publications"],
      "output": "Raw landscape data"
    },
    {
      "step": 2,
      "name": "Market Intelligence",
      "activities": ["Extract patterns", "Identify gaps", "Trend analysis"],
      "output": "Structured market insights"
    },
    {
      "step": 3,
      "name": "PRD Prior Updates",
      "activities": ["Bayesian updating on decision nodes", "Shift selected/deferred options"],
      "output": "Updated probability weights"
    },
    {
      "step": 4,
      "name": "Architecture Decisions",
      "activities": ["Choose implementation paths", "Apply archetype overlays"],
      "output": "Technical decisions"
    },
    {
      "step": 5,
      "name": "Product Evolution",
      "activities": ["Build features", "Ship code", "Deploy"],
      "output": "Shipped product"
    },
    {
      "step": 6,
      "name": "Market Response",
      "activities": ["User feedback", "Competitive response", "Regulatory changes"],
      "output": "Feedback signal (triggers next scan)"
    }
  ],
  "central_artifact": {
    "name": "Probabilistic PRD",
    "nodes": 30,
    "levels": 5,
    "update_method": "Bayesian"
  },
  "semantic_tags_used": [
    "heading_display", "label_editorial", "processing_stage", "decision_point",
    "solution_component", "data_flow", "selected_option", "callout_bar", "section_numeral"
  ]
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
- [x] Audience level correct (L1/L2/L3/L4)
- [x] Layout template identified (A/B/C/D/E)

## Status

- [x] Draft created
- [ ] Content reviewed
- [ ] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
