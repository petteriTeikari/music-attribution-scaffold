# fig-tech-06: Single vs Multi-Agent Decision

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-tech-06 |
| **Title** | Single vs Multi-Agent Architecture Decision |
| **Audience** | Technical (developers) |
| **Complexity** | L2 (overview) |
| **Location** | docs/architecture/adr/0005-single-agent-architecture.md, docs/knowledge-base/technical/agentic-systems/SYNTHESIS.md |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |

## Purpose

Justify the single-agent architecture choice for the system attribution pipeline using quantitative research data, showing when single-agent outperforms multi-agent systems.

## Key Message

"Sequential tasks amplify errors 17.2x in multi-agent systems—single-agent with tool orchestration is correct for the system attribution pipeline."

## Visual Concept

Decision tree with research evidence leading to architecture recommendation.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT ARCHITECTURE DECISION                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                        ┌─────────────────┐                                  │
│                        │  Task Analysis  │                                  │
│                        │  Sequential?    │                                  │
│                        └────────┬────────┘                                  │
│                                 │                                           │
│            ┌────────────────────┼────────────────────┐                      │
│            │                    │                    │                      │
│            ▼                    ▼                    ▼                      │
│   ┌────────────────┐  ┌────────────────┐  ┌────────────────┐               │
│   │   PARALLEL     │  │   SEQUENTIAL   │  │   ATTRIBUTION     │               │
│   │   Tasks        │  │   Tasks        │  │   Pipeline     │               │
│   │                │  │                │  │                │               │
│   │ Multi-agent    │  │ Single-agent   │  │ Fetch→Resolve  │               │
│   │ can help       │  │ preferred      │  │ →Score         │               │
│   └────────────────┘  └────────────────┘  └───────┬────────┘               │
│                                                   │                         │
│   ┌─────────────────────────────────────────────────┐                      │
│   │                                                 │                       │
│   │  RESEARCH EVIDENCE                              │                       │
│   │  ────────────────                               │                       │
│   │  • 17.2x error amplification (sequential MAS)   │                       │
│   │  • 45% accuracy threshold (single-agent)        │                       │
│   │  • Exponential communication overhead (>7 agents)│                      │
│   │                                                 │                       │
│   └─────────────────────────────────────────────────┘                      │
│                                                   │                         │
│                                                   ▼                         │
│                              ┌─────────────────────────────┐               │
│                              │  RECOMMENDATION:            │               │
│                              │  Single-Agent + Tool        │               │
│                              │  Orchestration              │               │
│                              │  (async parallel tools)     │               │
│                              └─────────────────────────────┘               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Task Analysis | `decision_node` | Entry point for decision |
| Parallel Tasks | `decision_branch` | Multi-agent scenario |
| Sequential Tasks | `decision_branch` | Single-agent scenario |
| Attribution Pipeline | `primary_pathway` | Our specific case |
| Research Evidence | `evidence_box` | Supporting data |
| Recommendation | `solution_component` | Final architecture choice |

### Relationships/Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Task Analysis | Parallel Tasks | arrow | "yes" |
| Task Analysis | Sequential Tasks | arrow | "yes" |
| Task Analysis | Attribution Pipeline | arrow | "evaluate" |
| Attribution Pipeline | Recommendation | arrow | "sequential" |
| Research Evidence | Recommendation | arrow | "supports" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "RESEARCH EVIDENCE" | 17.2x error amplification, 45% accuracy threshold, exponential overhead | Center |

## Text Content

### Labels (Max 30 chars each)

- "Task Analysis"
- "Parallel Tasks"
- "Sequential Tasks"
- "Attribution"
- "Fetch → Resolve → Score"
- "17.2x Error Amplification"
- "45% Accuracy Threshold"
- "Single-Agent + Tools"
- "Async Parallel Tools"

### Caption (for embedding)

Agent architecture decision tree: Sequential tasks (like the attribution pipeline) perform better with single-agent architecture due to 17.2x error amplification in multi-agent systems on sequential workloads (Google Research 2025).

## Prompts for Nano Banana Pro

### Style Prompt

Clean decision tree diagram on warm off-white background (#F8F6F0).
Medical illustration quality, Economist-style data visualization.
Clear hierarchy flowing top-to-bottom with decision branches.
Evidence box with bold statistics (17.2x, 45%) highlighted.
Recommendation box emphasized with deep blue system branding.
Professional technical documentation aesthetic.

### Content Prompt

Create a decision tree diagram showing:
- TOP: "Task Analysis" decision node
- MIDDLE ROW: Three branches
  - Left: "Parallel Tasks" → "Multi-agent can help"
  - Center: "Sequential Tasks" → "Single-agent preferred"
  - Right: "Attribution Pipeline" → "Fetch→Resolve→Score"
- EVIDENCE BOX (center, prominent):
  - "17.2x error amplification" statistic
  - "45% accuracy threshold" statistic
  - "Exponential communication overhead"
- BOTTOM: "Recommendation" box with "Single-Agent + Tool Orchestration"
- Arrows showing the system pipeline leads to single-agent choice
- Evidence box supports recommendation

### Refinement Notes

- Statistics (17.2x, 45%) should be visually prominent
- The system pipeline branch should be highlighted as the evaluated case
- Recommendation should feel conclusive, well-supported
- Decision tree should be clear and readable

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "tech-06",
    "title": "Single vs Multi-Agent Architecture Decision",
    "audience": "technical"
  },
  "content_architecture": {
    "primary_message": "Sequential tasks require single-agent architecture; 17.2x error amplification in multi-agent",
    "layout_flow": "top-to-bottom",
    "key_structures": [
      {
        "name": "Task Analysis",
        "role": "decision_node",
        "is_highlighted": false,
        "labels": ["Sequential?", "Parallel?"]
      },
      {
        "name": "Parallel Tasks",
        "role": "decision_branch",
        "is_highlighted": false,
        "labels": ["Multi-agent", "Can help"]
      },
      {
        "name": "Sequential Tasks",
        "role": "decision_branch",
        "is_highlighted": false,
        "labels": ["Single-agent", "Preferred"]
      },
      {
        "name": "Attribution Pipeline",
        "role": "primary_pathway",
        "is_highlighted": true,
        "labels": ["Fetch", "Resolve", "Score", "Sequential"]
      },
      {
        "name": "Research Evidence",
        "role": "evidence_box",
        "is_highlighted": true,
        "labels": ["17.2x error amp", "45% threshold", "Exponential overhead"]
      },
      {
        "name": "Recommendation",
        "role": "solution_component",
        "is_highlighted": true,
        "labels": ["Single-Agent", "Tool Orchestration", "Async parallel tools"]
      }
    ],
    "relationships": [
      {"from": "Task Analysis", "to": "Parallel Tasks", "type": "arrow", "label": "parallel?"},
      {"from": "Task Analysis", "to": "Sequential Tasks", "type": "arrow", "label": "sequential?"},
      {"from": "Task Analysis", "to": "Attribution Pipeline", "type": "arrow", "label": "evaluate"},
      {"from": "Attribution Pipeline", "to": "Recommendation", "type": "arrow", "label": "sequential"},
      {"from": "Research Evidence", "to": "Recommendation", "type": "arrow", "label": "supports"}
    ],
    "callout_boxes": [
      {
        "heading": "RESEARCH EVIDENCE",
        "body_text": "• 17.2x error amplification on sequential MAS\n• 45% accuracy threshold for single-agent\n• Exponential overhead beyond 7 agents",
        "position": "center"
      }
    ]
  }
}
```

## Alt Text

Decision tree: Task analysis leads to parallel or sequential classification. The system pipeline is sequential, leading to single-agent recommendation supported by 17.2x error amplification research.

## Research Basis

- **[Google DeepMind & MIT (2025)](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)**: "Towards a Science of Scaling Agent Systems" - 17.2x error amplification finding ([arXiv:2512.08296](https://arxiv.org/abs/2512.08296))
- **[Towards Data Science analysis](https://towardsdatascience.com/why-your-multi-agent-system-is-failing-escaping-the-17x-error-trap-of-the-bag-of-agents/)**: "Why Your Multi-Agent System is Failing"
- **[agentic-systems-research-2026-02-03.md](../../knowledge-base/technical/agentic-systems-research-2026-02-03.md)**: Section 3.2

## Status

- [x] Draft created
- [x] Content reviewed
- [x] Generated via Nano Banana Pro
- [x] Embedded in documentation
