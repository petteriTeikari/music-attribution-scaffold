# fig-persona-05: Cognitive Memory Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-persona-05 |
| **Title** | Cognitive Memory Architecture |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Location** | docs/knowledge-base/persona-engineering/, docs/planning/ |
| **Priority** | P0 (Critical) |
| **Aspect Ratio** | 16:9 |
| **Layout Template** | B (Multi-Panel) |

## Purpose

Maps the Atkinson-Shiffrin cognitive memory model to LLM memory implementations, showing how sensory memory, short-term memory, and long-term memory (episodic and semantic) have direct computational analogues. Answers: "How should we structure memory in a persona-driven LLM system, and what can cognitive science tell us?"

## Key Message

Memory enables relationship, relationship enables trust -- a three-tier implementation (session, episodic, semantic) maps directly to the Atkinson-Shiffrin cognitive model and gives persona systems the ability to maintain meaningful user relationships over time.

## Visual Concept

Multi-panel layout (Template B) with two horizontal rows. The top row shows the cognitive model: four panels flowing left to right (Sensory Register, Short-Term Store, Long-Term Episodic, Long-Term Semantic) connected by arrows with decay/transfer labels. The bottom row shows the implementation mapping: four corresponding panels (Conversation Buffer, Session Context, Vector DB with 90-day retention, Persistent User Profile). Vertical dashed lines connect each cognitive concept to its implementation. A horizontal accent line separates the two rows. The callout spans the bottom.

```
+-----------------------------------------------------------------------+
|  COGNITIVE MEMORY                                               [sq]   |
|  ARCHITECTURE                                                          |
+-----------------------------------------------------------------------+
|                                                                        |
|  ATKINSON-SHIFFRIN MODEL (COGNITIVE)                                   |
|  ════════════════════════════════════                                   |
|                                                                        |
|  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐  ┌───────────┐  |
|  │ SENSORY     │──>│ SHORT-TERM  │──>│ LONG-TERM   │  │ LONG-TERM │  |
|  │ REGISTER    │   │ STORE       │   │ EPISODIC    │  │ SEMANTIC  │  |
|  │             │   │             │   │             │  │           │  |
|  │ ~250ms      │   │ ~20s        │   │ Events,     │  │ Facts,    │  |
|  │ decay       │   │ 7+/-2 items │   │ experiences │  │ concepts  │  |
|  └─────────────┘   └─────────────┘   └──────┬──────┘  └─────┬─────┘  |
|        :                  :                  :               :         |
|        :                  :                  :               :         |
|  ─────────────── IMPLEMENTATION MAPPING ──────────────────────         |
|        :                  :                  :               :         |
|        :                  :                  :               :         |
|  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐  ┌───────────┐  |
|  │ CONVERSATION│   │ SESSION     │   │ EPISODIC    │  │ SEMANTIC  │  |
|  │ BUFFER      │   │ CONTEXT     │   │ MEMORY      │  │ MEMORY    │  |
|  │             │   │             │   │             │  │           │  |
|  │ In-memory   │   │ In-memory   │   │ Vector DB   │  │ Persistent│  |
|  │ Current     │   │ Window of   │   │ 90-day      │  │ User      │  |
|  │ turn only   │   │ recent turns│   │ retention   │  │ Profile   │  |
|  └─────────────┘   └─────────────┘   └─────────────┘  └───────────┘  |
|                                                                        |
|  MEMORY ENABLES RELATIONSHIP -- RELATIONSHIP ENABLES TRUST       [sq]  |
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
    content: "COGNITIVE MEMORY ARCHITECTURE"
    role: title

  - id: cognitive_label
    bounds: [80, 130, 600, 30]
    content: "ATKINSON-SHIFFRIN MODEL (COGNITIVE)"
    role: label_editorial

  - id: cognitive_row
    bounds: [80, 160, 1760, 300]
    role: content_area

  - id: mapping_divider
    bounds: [80, 480, 1760, 2]
    role: accent_line

  - id: impl_label
    bounds: [80, 500, 600, 30]
    content: "IMPLEMENTATION MAPPING"
    role: label_editorial

  - id: impl_row
    bounds: [80, 530, 1760, 300]
    role: content_area

  - id: callout_zone
    bounds: [80, 960, 1760, 100]
    content: "MEMORY ENABLES RELATIONSHIP -- RELATIONSHIP ENABLES TRUST"
    role: callout_box

anchors:
  - id: sensory_register
    position: [100, 180]
    size: [380, 260]
    role: processing_stage
    label: "SENSORY REGISTER"

  - id: short_term_store
    position: [540, 180]
    size: [380, 260]
    role: processing_stage
    label: "SHORT-TERM STORE"

  - id: long_term_episodic
    position: [980, 180]
    size: [380, 260]
    role: processing_stage
    label: "LONG-TERM EPISODIC"

  - id: long_term_semantic
    position: [1420, 180]
    size: [380, 260]
    role: processing_stage
    label: "LONG-TERM SEMANTIC"

  - id: conversation_buffer
    position: [100, 550]
    size: [380, 260]
    role: processing_stage
    label: "CONVERSATION BUFFER"

  - id: session_context
    position: [540, 550]
    size: [380, 260]
    role: processing_stage
    label: "SESSION CONTEXT"

  - id: episodic_memory
    position: [980, 550]
    size: [380, 260]
    role: storage_layer
    label: "EPISODIC MEMORY"

  - id: semantic_memory
    position: [1420, 550]
    size: [380, 260]
    role: storage_layer
    label: "SEMANTIC MEMORY"

  - id: flow_sensory_to_short
    from: sensory_register
    to: short_term_store
    type: arrow
    label: "attention"

  - id: flow_short_to_episodic
    from: short_term_store
    to: long_term_episodic
    type: arrow
    label: "rehearsal"

  - id: flow_episodic_to_semantic
    from: long_term_episodic
    to: long_term_semantic
    type: arrow
    label: "consolidation"

  - id: mapping_sensory
    from: sensory_register
    to: conversation_buffer
    type: dashed
    label: "maps to"

  - id: mapping_short
    from: short_term_store
    to: session_context
    type: dashed
    label: "maps to"

  - id: mapping_episodic
    from: long_term_episodic
    to: episodic_memory
    type: dashed
    label: "maps to"

  - id: mapping_semantic
    from: long_term_semantic
    to: semantic_memory
    type: dashed
    label: "maps to"
```

## Content Elements

### Primary Structures

| Name | Semantic Tag | Description |
|------|--------------|-------------|
| Title block | `heading_display` | "COGNITIVE MEMORY ARCHITECTURE" in editorial caps |
| Cognitive model label | `label_editorial` | "ATKINSON-SHIFFRIN MODEL (COGNITIVE)" section header |
| Implementation label | `label_editorial` | "IMPLEMENTATION MAPPING" section header |
| Sensory Register | `processing_stage` | Cognitive: ~250ms decay, raw perceptual input |
| Short-Term Store | `processing_stage` | Cognitive: ~20s retention, 7 +/- 2 items capacity |
| Long-Term Episodic | `processing_stage` | Cognitive: events and experiences, autobiographical |
| Long-Term Semantic | `processing_stage` | Cognitive: facts, concepts, general knowledge |
| Conversation Buffer | `processing_stage` | Implementation: in-memory, current turn only |
| Session Context | `processing_stage` | Implementation: in-memory, sliding window of recent turns |
| Episodic Memory | `storage_layer` | Implementation: vector DB with semantic search, 90-day retention |
| Semantic Memory | `storage_layer` | Implementation: persistent user profile, preferences, long-term facts |
| Mapping divider | `accent_line` | Horizontal accent line between cognitive model and implementation |

### Relationships / Flows

| From | To | Type | Label |
|------|----|------|-------|
| Sensory Register | Short-Term Store | arrow | "attention" |
| Short-Term Store | Long-Term Episodic | arrow | "rehearsal" |
| Long-Term Episodic | Long-Term Semantic | arrow | "consolidation" |
| Sensory Register | Conversation Buffer | dashed | "maps to" |
| Short-Term Store | Session Context | dashed | "maps to" |
| Long-Term Episodic | Episodic Memory | dashed | "maps to" |
| Long-Term Semantic | Semantic Memory | dashed | "maps to" |
| Session Context | Episodic Memory | arrow | "persist important interactions" |

### Callout Boxes

| Title | Content | Position |
|-------|---------|----------|
| "MEMORY ENABLES RELATIONSHIP -- RELATIONSHIP ENABLES TRUST" | Without memory, every conversation starts from zero. Three-tier memory (session, episodic, semantic) gives persona systems the ability to build and maintain meaningful user relationships over time, which is the foundation for trust in AI-assisted attribution workflows. | bottom-full-width |

## Text Content

### Labels (Max 30 chars each)

- Label 1: "SENSORY REGISTER"
- Label 2: "SHORT-TERM STORE"
- Label 3: "LONG-TERM EPISODIC"
- Label 4: "LONG-TERM SEMANTIC"
- Label 5: "CONVERSATION BUFFER"
- Label 6: "SESSION CONTEXT"
- Label 7: "EPISODIC MEMORY"
- Label 8: "SEMANTIC MEMORY"
- Label 9: "~250ms decay"
- Label 10: "~20s, 7+/-2 items"
- Label 11: "Events, experiences"
- Label 12: "Facts, concepts"
- Label 13: "In-memory, current turn"
- Label 14: "In-memory, recent turns"
- Label 15: "Vector DB, 90-day"
- Label 16: "Persistent user profile"

### Caption

Cognitive memory architecture mapping the Atkinson-Shiffrin model (Sensory Register, Short-Term Store, Long-Term Episodic, Long-Term Semantic) to LLM implementation tiers (Conversation Buffer, Session Context, Vector DB with 90-day retention, Persistent User Profile).

## Anti-Hallucination Rules

### Default Rules (always include)

1. **Font names are INTERNAL** -- do NOT render them as labels.
2. **Semantic tags are INTERNAL** -- do NOT render them as visible text.
3. **Hex codes are INTERNAL** -- do NOT render them.
4. **Engineering jargon** -- "vector DB", "RAG" should be used sparingly for L2 audience with brief context.
5. **Background MUST be warm cream (#f6f3e6)**.
6. **No generic flowchart aesthetics** -- no thick block arrows, no PowerPoint look.
7. **No figure captions** -- do NOT render "Figure 1.", "Fig.", or numbered caption.
8. **No prompt leakage** -- do NOT render style keywords as visible text.

### Figure-Specific Rules

9. The Atkinson-Shiffrin model is from Atkinson & Shiffrin (1968) -- do NOT attribute it to other researchers.
10. The mapping from cognitive science to LLM memory is an analogy, NOT a claim of identical mechanisms -- do NOT imply LLMs have human-like memory.
11. The "90-day retention" for episodic memory is a design choice, NOT a universal standard -- present it as one implementation option.
12. "7 +/- 2 items" in short-term memory is Miller's Law (1956) -- this is well-established cognitive science.
13. Do NOT show specific database products (e.g., Pinecone, Weaviate) -- keep the implementation generic at L2 level.
14. The three-tier implementation (session, episodic, semantic) is a common pattern across multiple persona frameworks -- it is NOT unique to one system.

## Alt Text

Dual-row mapping diagram of the Atkinson-Shiffrin cognitive memory model to LLM persona memory implementation, showing Sensory Register, Short-Term Store, Long-Term Episodic, and Long-Term Semantic tiers mapped to Conversation Buffer, Session Context, Vector DB, and Persistent User Profile for persona coherence.

## Image Embed

![Dual-row mapping diagram of the Atkinson-Shiffrin cognitive memory model to LLM persona memory implementation, showing Sensory Register, Short-Term Store, Long-Term Episodic, and Long-Term Semantic tiers mapped to Conversation Buffer, Session Context, Vector DB, and Persistent User Profile for persona coherence.](docs/figures/repo-figures/assets/fig-persona-05-memory-architecture-cognitive.jpg)

*Cognitive memory architecture mapping the Atkinson-Shiffrin model (Sensory Register, Short-Term Store, Long-Term Episodic, Long-Term Semantic) to LLM implementation tiers (Conversation Buffer, Session Context, Vector DB with 90-day retention, Persistent User Profile).*

## JSON Export Block

```json
{
  "meta": {
    "figure_id": "persona-05",
    "title": "Cognitive Memory Architecture",
    "audience": "L2",
    "layout_template": "B"
  },
  "content_architecture": {
    "primary_message": "Memory enables relationship, relationship enables trust -- three-tier memory maps to the Atkinson-Shiffrin cognitive model.",
    "layout_flow": "left-to-right-dual-row",
    "key_structures": [
      {
        "name": "Sensory Register",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["SENSORY REGISTER", "~250ms decay"]
      },
      {
        "name": "Short-Term Store",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["SHORT-TERM STORE", "~20s, 7+/-2 items"]
      },
      {
        "name": "Long-Term Episodic",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["LONG-TERM EPISODIC", "Events, experiences"]
      },
      {
        "name": "Long-Term Semantic",
        "role": "processing_stage",
        "is_highlighted": true,
        "labels": ["LONG-TERM SEMANTIC", "Facts, concepts"]
      },
      {
        "name": "Conversation Buffer",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["CONVERSATION BUFFER", "In-memory, current turn"]
      },
      {
        "name": "Session Context",
        "role": "processing_stage",
        "is_highlighted": false,
        "labels": ["SESSION CONTEXT", "In-memory, recent turns"]
      },
      {
        "name": "Episodic Memory",
        "role": "storage_layer",
        "is_highlighted": true,
        "labels": ["EPISODIC MEMORY", "Vector DB, 90-day"]
      },
      {
        "name": "Semantic Memory",
        "role": "storage_layer",
        "is_highlighted": true,
        "labels": ["SEMANTIC MEMORY", "Persistent user profile"]
      }
    ],
    "relationships": [
      {
        "from": "Sensory Register",
        "to": "Short-Term Store",
        "type": "arrow",
        "label": "attention"
      },
      {
        "from": "Short-Term Store",
        "to": "Long-Term Episodic",
        "type": "arrow",
        "label": "rehearsal"
      },
      {
        "from": "Long-Term Episodic",
        "to": "Long-Term Semantic",
        "type": "arrow",
        "label": "consolidation"
      },
      {
        "from": "Sensory Register",
        "to": "Conversation Buffer",
        "type": "dashed",
        "label": "maps to"
      },
      {
        "from": "Short-Term Store",
        "to": "Session Context",
        "type": "dashed",
        "label": "maps to"
      },
      {
        "from": "Long-Term Episodic",
        "to": "Episodic Memory",
        "type": "dashed",
        "label": "maps to"
      },
      {
        "from": "Long-Term Semantic",
        "to": "Semantic Memory",
        "type": "dashed",
        "label": "maps to"
      }
    ],
    "callout_boxes": [
      {
        "heading": "MEMORY ENABLES RELATIONSHIP -- RELATIONSHIP ENABLES TRUST",
        "body_text": "Three-tier memory gives persona systems the ability to maintain meaningful user relationships over time.",
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
