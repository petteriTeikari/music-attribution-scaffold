# fig-persona-09: Over-Personalization Failure Taxonomy

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-09 |
| **Title** | Over-Personalization Failure Taxonomy |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/knowledge-base/persona-engineering/, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Categorizes the three primary over-personalization failure modes -- irrelevance, repetition, and sycophancy -- with concrete examples and mitigations, showing that memory mechanisms substantially exacerbate these failures. Answers: "What goes wrong when personalization is taken too far, and how bad is the problem?"

## Key Message

Memory mechanisms substantially exacerbate over-personalization, causing 26.2-61.1% performance drops across three failure modes: irrelevance (injecting personal references when unneeded), repetition (reusing identical memories), and sycophancy (prioritizing agreement over accuracy).

## Visual Concept

Multi-panel layout (Template B) with three equal panels in a horizontal row, each representing one failure mode. Each panel has a Roman numeral header, a brief description, a concrete example in a callout-style quote, a mitigation strategy labeled "Self-ReCheck", and a severity indicator. Below the three panels, a stats bar shows the aggregate performance drop range (26.2-61.1%). A callout spans the bottom.

```
+-----------------------------------------------------------------------+
|  OVER-PERSONALIZATION                                           [sq]   |
|  FAILURE TAXONOMY                                                      |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐  |
|  │  I. IRRELEVANCE   │  │  II. REPETITION   │  │  III. SYCOPHANCY  │  |
|  │                   │  │                   │  │                   │  |
|  │  Injecting        │  │  Reusing          │  │  Prioritizing     │  |
|  │  personal refs    │  │  identical        │  │  agreement over   │  |
|  │  when not needed  │  │  memories         │  │  accuracy         │  |
|  │                   │  │                   │  │                   │  |
|  │  ┌─────────────┐ │  │  ┌─────────────┐ │  │  ┌─────────────┐ │  |
|  │  │ "You love   │ │  │  │ "As you     │ │  │  │ "You're     │ │  |
|  │  │  jazz, so   │ │  │  │  mentioned  │ │  │  │  absolutely  │ │  |
|  │  │  this C++   │ │  │  │  last time  │ │  │  │  right that  │ │  |
|  │  │  bug is     │ │  │  │  (x5)..."   │ │  │  │  2+2=5!"    │ │  |
|  │  │  like..."   │ │  │  │             │ │  │  │             │ │  |
|  │  └─────────────┘ │  │  └─────────────┘ │  │  └─────────────┘ │  |
|  │                   │  │                   │  │                   │  |
|  │  MITIGATION:      │  │  MITIGATION:      │  │  MITIGATION:      │  |
|  │  Self-ReCheck     │  │  Self-ReCheck     │  │  Self-ReCheck     │  |
|  │  relevance gate   │  │  novelty filter   │  │  accuracy check   │  |
|  └───────────────────┘  └───────────────────┘  └───────────────────┘  |
|                                                                        |
|  ──────────────────────────────────────────────────────────────────    |
|  PERFORMANCE DROP WITH MEMORY: 26.2% -- 61.1%                         |
|  ──────────────────────────────────────────────────────────────────    |
|                                                                        |
|  MEMORY MECHANISMS SUBSTANTIALLY EXACERBATE OVER-PERSONALIZATION [sq]  |
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
    content: "OVER-PERSONALIZATION FAILURE TAXONOMY"
    role: title

  - id: panels_zone
    bounds: [80, 140, 1760, 600]
    role: content_area

  - id: stats_bar
    bounds: [80, 770, 1760, 80]
    role: content_area
    label: "Performance Drop Stats"

  - id: callout_zone
    bounds: [80, 940, 1760, 100]
    content: "MEMORY MECHANISMS SUBSTANTIALLY EXACERBATE OVER-PERSONALIZATION"
    role: callout_box

anchors:
  - id: panel_irrelevance
    position: [100, 160]
    size: [540, 570]
    role: confidence_low
    label: "I. IRRELEVANCE"

  - id: panel_repetition
    position: [690, 160]
    size: [540, 570]
    role: confidence_low
    label: "II. REPETITION"

  - id: panel_sycophancy
    position: [1280, 160]
    size: [540, 570]
    role: confidence_low
    label: "III. SYCOPHANCY"

  - id: example_irrelevance
    position: [130, 380]
    size: [480, 120]
    role: problem_statement
    label: "Jazz/C++ example"

  - id: example_repetition
    position: [720, 380]
    size: [480, 120]
    role: problem_statement
    label: "Repeated memory x5"

  - id: example_sycophancy
    position: [1310, 380]
    size: [480, 120]
    role: problem_statement
    label: "2+2=5 agreement"

  - id: mitigation_irrelevance
    position: [130, 560]
    size: [480, 80]
    role: solution_component
    label: "Self-ReCheck relevance gate"

  - id: mitigation_repetition
    position: [720, 560]
    size: [480, 80]
    role: solution_component
    label: "Self-ReCheck novelty filter"

  - id: mitigation_sycophancy
    position: [1310, 560]
    size: [480, 80]
    role: solution_component
    label: "Self-ReCheck accuracy check"

  - id: stats_block
    position: [100, 780]
    size: [1720, 60]
    role: confidence_low
    label: "26.2% -- 61.1% performance drop"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "OVER-PERSONALIZATION FAILURE TAXONOMY" in editorial caps |
| I. Irrelevance panel | `confidence_low` | Failure mode: injecting personal references (e.g., music preferences) into unrelated contexts (e.g., debugging) |
| II. Repetition panel | `confidence_low` | Failure mode: reusing identical stored memories repeatedly, creating a stuck loop |
| III. Sycophancy panel | `confidence_low` | Failure mode: prioritizing agreement with user preferences/memories over factual accuracy |
| Irrelevance example | `problem_statement` | "You love jazz, so this C++ bug is like a jazz improvisation..." -- forced irrelevant personalization |
| Repetition example | `problem_statement` | "As you mentioned last time..." (x5) -- same memory surface repeatedly |
| Sycophancy example | `problem_statement` | "You're absolutely right that 2+2=5!" -- agreeing with user to maintain relationship |
| Irrelevance mitigation | `solution_component` | Self-ReCheck: relevance gate that checks if personalization is contextually appropriate before injecting |
| Repetition mitigation | `solution_component` | Self-ReCheck: novelty filter that tracks which memories have been recently surfaced and suppresses duplicates |
| Sycophancy mitigation | `solution_component` | Self-ReCheck: accuracy check that verifies factual claims regardless of user preferences |
| Stats bar | `confidence_low` | Performance drop range: 26.2-61.1% when memory mechanisms are activated |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| Memory activation | Irrelevance | arrow | "triggers inappropriate insertion" |
| Memory activation | Repetition | arrow | "causes stuck retrieval" |
| Memory activation | Sycophancy | arrow | "amplifies agreement bias" |
| Self-ReCheck | All three failures | dashed | "mitigation" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "MEMORY MECHANISMS SUBSTANTIALLY EXACERBATE OVER-PERSONALIZATION" | Across benchmarks, activating memory systems causes 26.2-61.1% performance degradation. All three failure modes (irrelevance, repetition, sycophancy) are amplified when the system has access to stored user preferences and interaction history. Self-ReCheck provides partial mitigation but does not fully solve the problem. | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I. IRRELEVANCE"
- Label 2: "II. REPETITION"
- Label 3: "III. SYCOPHANCY"
- Label 4: "Personal refs when unneeded"
- Label 5: "Identical memories reused"
- Label 6: "Agreement over accuracy"
- Label 7: "Self-ReCheck relevance"
- Label 8: "Self-ReCheck novelty"
- Label 9: "Self-ReCheck accuracy"
- Label 10: "MITIGATION"
- Label 11: "26.2-61.1% drop"
- Label 12: "PERFORMANCE DROP"

### Caption

Three over-personalization failure modes -- irrelevance (injecting personal references when not needed), repetition (reusing identical memories), and sycophancy (prioritizing agreement over accuracy) -- with Self-ReCheck mitigations and the finding that memory activation causes 26.2-61.1% performance drops.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Engineering jargon** -- use accessible terms for L2 audience. "Memory mechanisms" rather than "RAG pipeline" or "vector retrieval".
5. **Background MUST be warm cream (#f6f3e6)**.
6. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

9. The 26.2-61.1% performance drop range is from empirical studies -- do NOT round to "26-61%" or alter the precision.
10. Self-ReCheck is a specific mitigation technique name -- do NOT substitute generic terms like "self-check" or "verification".
11. The examples (jazz/C++ bug, "as you mentioned" x5, 2+2=5) are illustrative -- they are NOT from a specific published benchmark. Present them as representative examples.
12. Sycophancy in the context of personalization is specifically about memory-induced agreement bias, NOT general sycophancy in LLMs. The memory of user preferences amplifies the tendency to agree.
13. Do NOT imply Self-ReCheck fully solves the problem -- it provides partial mitigation, and the fundamental tension between personalization and accuracy remains open.
14. Do NOT rank the three failure modes by severity -- all three are significant and context-dependent.
15. Roman numerals (I, II, III) label the failure modes per the design system, NOT by severity ranking.

## Alt Text

Three-panel taxonomy of over-personalization failure modes in AI persona systems: irrelevance (injecting unneeded personal references), repetition (reusing identical memories), and sycophancy (prioritizing agreement over accuracy), with Self-ReCheck mitigations and 26.2-61.1% memory-induced performance drops.

## Image Embed

![Three-panel taxonomy of over-personalization failure modes in AI persona systems: irrelevance (injecting unneeded personal references), repetition (reusing identical memories), and sycophancy (prioritizing agreement over accuracy), with Self-ReCheck mitigations and 26.2-61.1% memory-induced performance drops.](docs/figures/repo-figures/assets/fig-persona-09-over-personalization-taxonomy.jpg)

*Three over-personalization failure modes -- irrelevance (injecting personal references when not needed), repetition (reusing identical memories), and sycophancy (prioritizing agreement over accuracy) -- with Self-ReCheck mitigations and the finding that memory activation causes 26.2-61.1% performance drops.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-09",
    "title": "Over-Personalization Failure Taxonomy",
    "audience": "L2",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Memory mechanisms cause 26.2-61.1% performance drops across three failure modes: irrelevance, repetition, and sycophancy.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "I. Irrelevance",
        "role": "confidence_low",
        "is_highlighted": true,
        "labels": ["I. IRRELEVANCE", "Personal refs when unneeded"]
      },
      {
        "name": "II. Repetition",
        "role": "confidence_low",
        "is_highlighted": true,
        "labels": ["II. REPETITION", "Identical memories reused"]
      },
      {
        "name": "III. Sycophancy",
        "role": "confidence_low",
        "is_highlighted": true,
        "labels": ["III. SYCOPHANCY", "Agreement over accuracy"]
      },
      {
        "name": "Self-ReCheck Mitigations",
        "role": "solution_component",
        "is_highlighted": false,
        "labels": ["Self-ReCheck relevance", "Self-ReCheck novelty", "Self-ReCheck accuracy"]
      },
      {
        "name": "Performance Drop Stats",
        "role": "confidence_low",
        "is_highlighted": true,
        "labels": ["26.2-61.1% drop"]
      }
    ],
    "relationships": [
      {
        "from": "Memory activation",
        "to": "Irrelevance",
        "type": "arrow",
        "label": "triggers"
      },
      {
        "from": "Memory activation",
        "to": "Repetition",
        "type": "arrow",
        "label": "triggers"
      },
      {
        "from": "Memory activation",
        "to": "Sycophancy",
        "type": "arrow",
        "label": "triggers"
      },
      {
        "from": "Self-ReCheck",
        "to": "All failures",
        "type": "dashed",
        "label": "partial mitigation"
      }
    ],
    "callout_boxes": [
      {
        "heading": "MEMORY MECHANISMS SUBSTANTIALLY EXACERBATE OVER-PERSONALIZATION",
        "body_text": "26.2-61.1% performance degradation when memory is activated. Self-ReCheck provides partial mitigation but the fundamental tension remains.",
        "position": "bottom-full-width"
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
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25
- [ ] Embedded in documentation
