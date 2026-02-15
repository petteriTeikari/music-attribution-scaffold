# fig-landscape-06: Founder Decision Framework: Which Attribution Approach

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-landscape-06 |
| **Title** | Founder Decision Framework: Which Attribution Approach |
| **Audience** | L3 (Engineer) |
| **Location** | docs/planning/music-tech-landscape/, docs/planning/music-tech-figure-coverage-plan.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | E (Steps) |

## Purpose

This figure provides a practical decision framework for founders and engineers choosing an attribution approach. It applies four constraint filters to seven attribution methods, progressively eliminating options until 1-2 viable choices remain. It answers: "Given my startup's constraints, which attribution method should I actually build?"

## Key Message

Your constraints (model access, compute budget, IP strategy) narrow 7 attribution methods down to 1-2 viable options for any given startup.

## Visual Concept

A top-to-bottom funnel/steps layout. The top row shows all 7 methods as equal-width boxes. Four horizontal filter bars cross the figure, each eliminating methods that fail the constraint. Methods that are eliminated get visually muted (faded). By the bottom, only 1-2 methods remain highlighted per constraint path. The figure reads like a progressive sieve.

```
+---------------------------------------------------------------+
|  FOUNDER DECISION FRAMEWORK                                    |
|  ■ Which Attribution Approach Fits Your Constraints?           |
+---------------------------------------------------------------+
|                                                                |
|  ALL 7 METHODS                                                 |
|  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐   |
|  │Unlrn│ │InfFn│ │Embed│ │Wmrk │ │Token│ │Repli│ │Infr-│   |
|  │ TDA │ │     │ │Simil│ │     │ │Flow │ │Detct│ │time │   |
|  └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘   |
|     │       │       │       │       │       │       │        |
|  ■ FILTER 1: Do you have model access?                        |
|  ───────────────────────────────────────                       |
|  YES: ──────────────────────────────────  NO: ───────────     |
|  │Unlrn│ │InfFn│         │Wmrk │ │Token│      │Embed│ │Repli│|
|     │       │               │       │           │       │    |
|  ■ FILTER 2: Can you afford retraining?                       |
|  ──────────────────────────────────────                        |
|  YES: ──────  NO: ──────────────────────                      |
|  │Unlrn│      │InfFn│ │Wmrk │ │Token│ │Embed│ │Repli│       |
|     │           │       │       │       │       │            |
|  ■ FILTER 3: Do you need real-time?                           |
|  ─────────────────────────────────                             |
|  YES: ──────────────────  NO: ──────                          |
|  │Wmrk │ │Embed│ │Infr-│  │InfFn│ │Unlrn│                   |
|     │       │       │                                         |
|  ■ FILTER 4: What is your IP strategy?                        |
|  ─────────────────────────────────────                         |
|  Open: ─────  Proprietary: ─────  Defensive: ─────           |
|  │Embed│      │Wmrk │ │Token│     │InfFn│ │Repli│           |
|                                                                |
+---------------------------------------------------------------+
|  ■ Your constraints determine your method.                     |
|    No single approach is universally best.                     |
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
      text: "FOUNDER DECISION FRAMEWORK"
    - type: label_editorial
      text: "Which Attribution Approach Fits Your Constraints?"

methods_row:
  position: [60, 140]
  width: 1800
  height: 100
  methods:
    - { label: "Unlearning TDA", short: "Unlrn", x: 0 }
    - { label: "Influence Functions", short: "InfFn", x: 1 }
    - { label: "Embedding Similarity", short: "Embed", x: 2 }
    - { label: "Watermarking", short: "Wmrk", x: 3 }
    - { label: "Token Flow", short: "Token", x: 4 }
    - { label: "Replication Detection", short: "Repli", x: 5 }
    - { label: "Inference-time", short: "Infr-time", x: 6 }

filter_1:
  position: [60, 260]
  width: 1800
  height: 140
  label: "FILTER 1: Do you have model access?"
  branches:
    yes: ["Unlrn", "InfFn", "Wmrk", "Token"]
    no: ["Embed", "Repli", "Infr-time"]

filter_2:
  position: [60, 420]
  width: 1800
  height: 140
  label: "FILTER 2: Can you afford retraining?"
  branches:
    yes: ["Unlrn"]
    no: ["InfFn", "Wmrk", "Token", "Embed", "Repli"]

filter_3:
  position: [60, 580]
  width: 1800
  height: 140
  label: "FILTER 3: Do you need real-time?"
  branches:
    yes: ["Wmrk", "Embed", "Infr-time"]
    no: ["InfFn", "Unlrn", "Repli"]

filter_4:
  position: [60, 740]
  width: 1800
  height: 140
  label: "FILTER 4: What is your IP strategy?"
  branches:
    open: ["Embed"]
    proprietary: ["Wmrk", "Token"]
    defensive: ["InfFn", "Repli"]

callout_bottom:
  position: [60, 920]
  width: 1800
  height: 100
  elements:
    - type: callout_bar
      text: "Your constraints determine your method."
    - type: label_editorial
      text: "No single approach is universally best."
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "FOUNDER DECISION FRAMEWORK" with coral accent square |
| Subtitle | `label_editorial` | "Which Attribution Approach Fits Your Constraints?" |
| Methods row | `solution_component` | Seven equal-width boxes showing all attribution methods |
| Filter 1 bar | `decision_point` | "Do you have model access?" with yes/no branching |
| Filter 2 bar | `decision_point` | "Can you afford retraining?" with yes/no branching |
| Filter 3 bar | `decision_point` | "Do you need real-time?" with yes/no branching |
| Filter 4 bar | `decision_point` | "What is your IP strategy?" with three-way branching |
| Active method boxes | `selected_option` | Methods that pass each filter, fully visible |
| Eliminated method boxes | `deferred_option` | Methods eliminated by a filter, visually muted |
| Filter labels | `label_editorial` | Filter question text with accent square marker |
| Bottom callout | `callout_bar` | "Your constraints determine your method" |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Methods row | Filter 1 | narrows | "Model access requirement" |
| Filter 1 | Filter 2 | narrows | "Compute budget requirement" |
| Filter 2 | Filter 3 | narrows | "Latency requirement" |
| Filter 3 | Filter 4 | narrows | "IP strategy requirement" |
| Filter 4 | Final selection | narrows | "1-2 viable methods" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| Filter 1 | "Model access: white-box vs black-box" | First filter bar |
| Filter 2 | "Retraining: GPU cost, dataset size" | Second filter bar |
| Filter 3 | "Real-time: inference latency requirement" | Third filter bar |
| Filter 4 | "IP: open-source, proprietary, defensive" | Fourth filter bar |
| Bottom | "No single approach is universally best" | Bottom callout |

## Text Content

### Labels (Max 30 chars each)

- FOUNDER DECISION FRAMEWORK
- Which Approach Fits You?
- Unlearning TDA
- Influence Functions
- Embedding Similarity
- Watermarking
- Token Flow
- Replication Detection
- Inference-time
- Do you have model access?
- Can you afford retraining?
- Do you need real-time?
- What is your IP strategy?
- Open
- Proprietary
- Defensive
- YES
- NO

### Caption (for embedding in documentation)

Founder decision framework: seven attribution methods (unlearning TDA, influence functions, embedding similarity, watermarking, token flow, replication detection, inference-time conditioning) filtered through four constraints (model access, retraining budget, real-time requirement, IP strategy) to narrow down to 1-2 viable options for any given startup.

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

1. There are exactly 7 methods and 4 filters -- do NOT add or remove any.
2. The filter branching is ILLUSTRATIVE -- real decisions involve nuance, not binary yes/no for all filters.
3. Filter 4 has THREE branches (open/proprietary/defensive), not two.
4. Do NOT name specific companies as examples of any method.
5. "Unlearning TDA" refers to training data attribution via machine unlearning -- do NOT confuse with GDPR right-to-erasure.
6. "Token Flow" refers to attention-based attribution tracing -- do NOT confuse with tokenomics.
7. Eliminated methods should be visually muted but still readable -- do NOT hide them completely.
8. The framework is a STARTING POINT, not a definitive recommendation -- do NOT imply guaranteed outcomes.
9. Do NOT add cost estimates or timelines to the filters.

## Alt Text

Decision funnel: 7 attribution methods filtered by 4 constraints to find 1-2 viable approaches per startup.

## JSON Export Block

```json
{
  "id": "fig-landscape-06",
  "title": "Founder Decision Framework: Which Attribution Approach",
  "audience": "L3",
  "priority": "P1",
  "layout": "E",
  "aspect_ratio": "16:9",
  "group": "landscape",
  "markov_phase": "Explain",
  "methods": [
    "Unlearning TDA",
    "Influence Functions",
    "Embedding Similarity",
    "Watermarking",
    "Token Flow",
    "Replication Detection",
    "Inference-time"
  ],
  "filters": [
    { "question": "Do you have model access?", "branches": ["yes", "no"] },
    { "question": "Can you afford retraining?", "branches": ["yes", "no"] },
    { "question": "Do you need real-time?", "branches": ["yes", "no"] },
    { "question": "What is your IP strategy?", "branches": ["open", "proprietary", "defensive"] }
  ],
  "semantic_tags_used": [
    "heading_display", "label_editorial", "decision_point", "selected_option",
    "deferred_option", "solution_component", "callout_bar"
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
