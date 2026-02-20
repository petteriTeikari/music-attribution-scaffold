# fig-persona-11: Memory System Comparison

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-11 |
| **Title** | Memory System Comparison: Letta, Zep, Mem0, MemoryOS |
| **Audience** | L3 (Software Engineer) |
| **Location** | docs/knowledge-base/, docs/planning/ |
| **Priority** | P1 (High) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Compares four leading agent memory systems -- Letta/MemGPT, Zep/Graphiti, Mem0, and MemoryOS -- across architecture, performance metrics, and design philosophy. Answers: "Which memory system best fits a persona-driven attribution agent, and what are the trade-offs?"

## Key Message

Memory systems are converging on temporal knowledge graphs, but differ sharply in abstraction level: from Letta's OS-like hierarchy to Mem0's three-line integration.

## Visual Concept

Four equal panels in a 2x2 grid, each showing one memory system. Each panel contains an architecture sketch (storage hierarchy or graph structure), three key metrics (accuracy improvement, latency, token savings), and a one-line positioning statement. A shared callout bar at the bottom unifies the convergence insight.

```
+-----------------------------------------------------------------------+
|  MEMORY SYSTEM COMPARISON                                              |
|  -- Four Architectures for Agent Persona Memory                        |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
|  I. LETTA / MEMGPT               |  II. ZEP / GRAPHITI              |
|  ─────────────────                |  ─────────────────               |
|                                   |                                   |
|  ┌─────────────────┐             |  ┌─────────────────┐             |
|  │ Core Memory      │             |  │ Temporal KG       │             |
|  │ (system prompt)  │             |  │ (bi-temporal)     │             |
|  ├─────────────────┤             |  │  nodes ── edges   │             |
|  │ Recall Memory    │             |  │  ↕ time layers    │             |
|  │ (conversations)  │             |  └─────────────────┘             |
|  ├─────────────────┤             |                                   |
|  │ Archival Memory  │             |  Accuracy: +26.1% (InCharacter)  |
|  │ (context repos)  │             |  Latency: <100ms p95 retrieval   |
|  └─────────────────┘             |  Token savings: 67% context      |
|                                   |                                   |
|  Accuracy: +23% persona recall   |  Philosophy: Graph-first,        |
|  Latency: variable (LLM-gated)  |  time as first-class dimension   |
|  Token savings: 80% via paging   |                                   |
|                                   |                                   |
|  Philosophy: OS-like memory      |                                   |
|  management with self-editing    |                                   |
|                                   |                                   |
+-----------------------------------+-----------------------------------+
|                                   |                                   |
|  III. MEM0                        |  IV. MEMORYOS                    |
|  ─────────────────                |  ─────────────────               |
|                                   |                                   |
|  ┌─────────────────┐             |  ┌─────────────────┐             |
|  │ Universal Layer  │             |  │ Sensory Buffer    │             |
|  │ ┌─────┐ 3 LOC   │             |  ├─────────────────┤             |
|  │ │ add │→│search│ │             |  │ Short-Term Store  │             |
|  │ └─────┘ └──────┘ │             |  ├─────────────────┤             |
|  └─────────────────┘             |  │ Long-Term Store   │             |
|                                   |  │ (hierarchical)    │             |
|  Accuracy: +26% over base        |  └─────────────────┘             |
|  Latency: <50ms (graph + vector) |                                   |
|  Token savings: 72% dedup        |  Accuracy: +37.1% (LongMemEval)  |
|                                   |  Latency: adaptive retrieval     |
|  Philosophy: Simplest possible   |  Token savings: 56% compression  |
|  API, memory as infrastructure   |                                   |
|                                   |  Philosophy: Cognitive science   |
|                                   |  hierarchy, EMNLP 2025 Oral      |
|                                   |                                   |
+-----------------------------------+-----------------------------------+
|  -- MEMORY SYSTEMS ARE CONVERGING ON TEMPORAL KNOWLEDGE GRAPHS         |
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
    content: "MEMORY SYSTEM COMPARISON"
    role: title

  - id: panel_i
    bounds: [40, 140, 920, 380]
    content: "I. LETTA / MEMGPT"
    role: content_area

  - id: panel_ii
    bounds: [960, 140, 920, 380]
    content: "II. ZEP / GRAPHITI"
    role: content_area

  - id: panel_iii
    bounds: [40, 540, 920, 380]
    content: "III. MEM0"
    role: content_area

  - id: panel_iv
    bounds: [960, 540, 920, 380]
    content: "IV. MEMORYOS"
    role: content_area

  - id: callout_zone
    bounds: [40, 940, 1840, 100]
    content: "MEMORY SYSTEMS ARE CONVERGING ON TEMPORAL KNOWLEDGE GRAPHS"
    role: callout_box

anchors:
  - id: letta_hierarchy
    position: [120, 200]
    size: [340, 220]
    role: processing_stage
    label: "OS-like memory hierarchy"

  - id: letta_metrics
    position: [500, 200]
    size: [380, 220]
    role: data_mono
    label: "Performance metrics"

  - id: zep_graph
    position: [1040, 200]
    size: [340, 220]
    role: processing_stage
    label: "Temporal knowledge graph"

  - id: zep_metrics
    position: [1420, 200]
    size: [380, 220]
    role: data_mono
    label: "Performance metrics"

  - id: mem0_api
    position: [120, 600]
    size: [340, 220]
    role: processing_stage
    label: "Universal memory layer"

  - id: mem0_metrics
    position: [500, 600]
    size: [380, 220]
    role: data_mono
    label: "Performance metrics"

  - id: memoryos_hierarchy
    position: [1040, 600]
    size: [340, 220]
    role: processing_stage
    label: "Hierarchical storage"

  - id: memoryos_metrics
    position: [1420, 600]
    size: [380, 220]
    role: data_mono
    label: "Performance metrics"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Letta/MemGPT panel | `processing_stage` | OS-like memory hierarchy: core (system prompt), recall (conversations), archival (context repos) |
| Zep/Graphiti panel | `processing_stage` | Temporal knowledge graph with bi-temporal edges, time as first-class dimension |
| Mem0 panel | `processing_stage` | Universal memory layer with minimal API surface (add, search, get) |
| MemoryOS panel | `processing_stage` | Cognitive-science-inspired hierarchical storage: sensory buffer, short-term, long-term |
| Metric blocks | `data_mono` | Accuracy improvement, latency, token savings for each system |
| Convergence callout | `callout_box` | Shared insight about temporal KG convergence |

### Relationships / Flows

| From | To | Type | Label |
|------|-----|------|-------|
| Letta core memory | Letta recall memory | arrow | "overflow paging" |
| Letta recall memory | Letta archival memory | arrow | "context eviction" |
| Zep nodes | Zep edges | bidirectional | "temporal relationships" |
| Mem0 add | Mem0 search | arrow | "store and retrieve" |
| MemoryOS sensory | MemoryOS short-term | arrow | "consolidation" |
| MemoryOS short-term | MemoryOS long-term | arrow | "hierarchical storage" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "CONVERGENCE" | "MEMORY SYSTEMS ARE CONVERGING ON TEMPORAL KNOWLEDGE GRAPHS" | bottom-center |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "I. LETTA / MEMGPT"
- Label 2: "II. ZEP / GRAPHITI"
- Label 3: "III. MEM0"
- Label 4: "IV. MEMORYOS"
- Label 5: "Core Memory"
- Label 6: "Recall Memory"
- Label 7: "Archival Memory"
- Label 8: "Temporal KG"
- Label 9: "Universal Layer"
- Label 10: "Sensory Buffer"
- Label 11: "Short-Term Store"
- Label 12: "Long-Term Store"
- Label 13: "+23% persona recall"
- Label 14: "+26.1% InCharacter"
- Label 15: "+26% over base"
- Label 16: "+37.1% LongMemEval"

### Caption (for embedding in documentation)

Four leading agent memory systems compared across architecture and performance: Letta's OS-like hierarchy, Zep's temporal knowledge graph, Mem0's three-line universal layer, and MemoryOS's cognitive-science-inspired storage -- all converging on temporal knowledge graphs as the dominant paradigm.

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them as labels in the image.
2. **Semantic tags are INTERNAL** -- `processing_stage`, `data_mono`, `callout_box` etc. Do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- `#E84C4F`, `#1E3A5F`, `#2E7D7B`, `#f6f3e6` are palette references. Do NOT render them.
4. **Engineering jargon** -- Module names and library internals are appropriate for L3 audience but keep within named systems.
5. **Background MUST be warm cream (#f6f3e6)** -- exact match to frontend surface color. No pure white, no gray, no yellow.
6. **No generic flowchart aesthetics** -- no thick block arrows, no rounded rectangles, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or any numbered academic caption. The editorial display title is allowed.
8. **No prompt leakage** -- do NOT render style keywords ("matte", "asymmetric", "editorial", "constructivist") as visible text in the figure.

### Figure-Specific Rules

9. Letta/MemGPT uses three-tier memory: core (in-context), recall (conversation search), archival (external storage). Do NOT invent additional tiers.
10. Zep/Graphiti uses bi-temporal knowledge graphs -- valid_time and transaction_time on edges. Do NOT confuse with simple vector stores.
11. Mem0 API is genuinely minimal: `m.add()`, `m.search()`, `m.get_all()`. Do NOT overcomplicate the interface.
12. MemoryOS was presented as an EMNLP 2025 Oral paper. Do NOT claim it is a commercial product.
13. Performance metrics are approximate ranges from published benchmarks. Do NOT present as exact universal numbers.
14. All four panels must be visually equal in size and weight -- no system should appear visually preferred.

## Alt Text

Multi-panel comparison of four agent memory systems for persona coherence -- Letta, Zep, Mem0, and MemoryOS -- showing architecture diagrams, performance metrics, and convergence on temporal knowledge graphs for music attribution agents.

## Image Embed

![Multi-panel comparison of four agent memory systems for persona coherence -- Letta, Zep, Mem0, and MemoryOS -- showing architecture diagrams, performance metrics, and convergence on temporal knowledge graphs for music attribution agents.](docs/figures/repo-figures/assets/fig-persona-11-memory-system-comparison.jpg)

*Four leading agent memory systems compared across architecture and performance: Letta's OS-like hierarchy, Zep's temporal knowledge graph, Mem0's three-line universal layer, and MemoryOS's cognitive-science-inspired storage -- all converging on temporal knowledge graphs as the dominant paradigm.*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-11",
    "title": "Memory System Comparison: Letta, Zep, Mem0, MemoryOS",
    "audience": "L3",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Memory systems are converging on temporal knowledge graphs, differing in abstraction level from OS-like hierarchy to three-line API.",
    "layout_flow": "left-to-right",
    "key_structures": [
      {
        "name": "Letta/MemGPT Panel",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["I. LETTA / MEMGPT", "OS-like hierarchy", "+23% persona recall"]
      },
      {
        "name": "Zep/Graphiti Panel",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["II. ZEP / GRAPHITI", "Temporal KG", "+26.1% InCharacter"]
      },
      {
        "name": "Mem0 Panel",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["III. MEM0", "Universal Layer", "+26% over base"]
      },
      {
        "name": "MemoryOS Panel",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["IV. MEMORYOS", "Hierarchical Storage", "+37.1% LongMemEval"]
      }
    ],
    "relationships": [
      {
        "from": "Core Memory",
        "to": "Recall Memory",
        "type": "arrow",
        "label": "overflow paging"
      },
      {
        "from": "Recall Memory",
        "to": "Archival Memory",
        "type": "arrow",
        "label": "context eviction"
      },
      {
        "from": "Sensory Buffer",
        "to": "Long-Term Store",
        "type": "arrow",
        "label": "hierarchical consolidation"
      }
    ],
    "callout_boxes": [
      {
        "heading": "CONVERGENCE",
        "body_text": "MEMORY SYSTEMS ARE CONVERGING ON TEMPORAL KNOWLEDGE GRAPHS",
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
- [x] Audience level correct (L3)
- [x] Layout template identified (B)

## Status

- [x] Draft created
- [ ] Content reviewed
- [x] Generated via Nano Banana Pro
- [ ] Quality score >= 21/25 (see STYLE-GUIDE-REPO.md v2.0)
- [ ] Embedded in documentation
