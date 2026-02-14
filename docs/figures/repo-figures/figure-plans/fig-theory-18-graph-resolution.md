# fig-theory-18: Graph-Based Resolution

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-18 |
| **Title** | Graph-Based Resolution |
| **Audience** | L4 (AI/ML Architect) |
| **Complexity** | L4 (graph theory, community detection) |
| **Location** | docs/theory/entity-resolution.md |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows how entity resolution can be modeled as a graph problem where entity mentions are nodes and evidence of co-reference forms weighted edges. It answers: "How does graph-based community detection help resolve entities at scale?"

The key message is: "Entity mentions form a graph where edges represent evidence of co-reference -- community detection algorithms identify clusters of mentions that likely refer to the same real-world entity."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  GRAPH-BASED RESOLUTION                                        |
|  ■ Community Detection for Entity Clustering                   |
+---------------------------------------------------------------+
|                                                                |
|  ENTITY MENTION GRAPH                                          |
|  ────────────────────                                          |
|                                                                |
|       ●─────────0.95────────●                                  |
|  "Imogen Heap"          "I. Heap"                              |
|       │  \                  │                                  |
|       │   \                 │                                  |
|      0.92  \0.88           0.90                                |
|       │     \               │                                  |
|       │      \              │                                  |
|       ●       ●─────0.87───●                                  |
|  "HEAP,    "Imogen       "Heap,                                |
|   IMOGEN"   J. Heap"     Imogen"                               |
|                                                                |
|   ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ 0.08 (weak)          |
|                                                                |
|       ▲─────────0.93────────▲                                  |
|  "Brian Eno"            "B. Eno"                               |
|       │                     │                                  |
|      0.91                  0.89                                |
|       │                     │                                  |
|       ▲─────────0.94────────▲                                  |
|  "Eno, Brian"          "Brian Peter                            |
|                         George Eno"                            |
|                                                                |
+---------------------------------------------------------------+
|                                                                |
|  COMMUNITY DETECTION                                           |
|  ───────────────────                                           |
|                                                                |
|  ┌─────────────────────┐  ┌─────────────────────┐             |
|  │  Community 1         │  │  Community 2         │             |
|  │  ─────────           │  │  ─────────           │             |
|  │  ● Imogen Heap       │  │  ▲ Brian Eno         │             |
|  │  ● I. Heap           │  │  ▲ B. Eno            │             |
|  │  ● HEAP, IMOGEN      │  │  ▲ Eno, Brian        │             |
|  │  ● Imogen J. Heap    │  │  ▲ Brian P. G. Eno   │             |
|  │  ● Heap, Imogen      │  │                      │             |
|  │                      │  │  Resolved ISNI:       │             |
|  │  Resolved ISNI:       │  │  0000 0001 xxxx xxxx │             |
|  │  0000 0001 xxxx xxxx │  │                      │             |
|  └─────────────────────┘  └─────────────────────┘             |
|                                                                |
|  ■ Edge weights from cascade steps (string sim, embedding,     |
|    LLM). Weak cross-community edges (< 0.3) = different       |
|    entities.                                                   |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "GRAPH-BASED RESOLUTION" with coral accent square |
| Subtitle | `label_editorial` | "Community Detection for Entity Clustering" |
| Entity mention nodes (Heap cluster) | `source_artist` | Five circular nodes for Imogen Heap name variants |
| Entity mention nodes (Eno cluster) | `source_artist` | Four triangular nodes for Brian Eno name variants |
| Strong edges (within community) | `data_flow` | Solid lines with weights 0.85-0.95 |
| Weak edge (between communities) | `data_flow` | Dashed line with weight 0.08 |
| Edge weight labels | `data_mono` | Numerical weights on each edge in monospace |
| Community 1 box | `entity_resolve` | Cluster containing all Imogen Heap mentions with resolved ISNI |
| Community 2 box | `entity_resolve` | Cluster containing all Brian Eno mentions with resolved ISNI |
| ISNI identifiers | `data_mono` | Illustrative ISNIs per community |
| Footer callout | `callout_box` | Edge weights from cascade steps; weak cross-community edges = different entities |

## Anti-Hallucination Rules

1. Edge weights are ILLUSTRATIVE (0.85-0.95 within, 0.08 between) -- do NOT present as computed values.
2. Community detection resolves clusters -- do NOT specify a particular algorithm (Louvain, Leiden, etc.) as the only option.
3. Edge weights come from the resolution cascade (fig-theory-16) -- string similarity, embeddings, LLM. Do NOT invent other sources.
4. ISNI numbers shown are ILLUSTRATIVE ("xxxx xxxx") -- do NOT claim they are real ISNIs for these artists.
5. The weak edge between communities (0.08) demonstrates that the graph correctly separates distinct entities.
6. Do NOT show edges from audio content similarity -- this graph is about NAME/METADATA resolution.
7. Two communities are shown for clarity -- real graphs may have thousands.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Theory visualization: graph-based entity resolution for music attribution showing mention nodes for Imogen Heap and Brian Eno name variants connected by weighted edges from cascade scoring -- community detection identifies two clusters each resolving to a single ISNI identifier, with strong within-cluster edges above 0.85 and weak cross-community edges at 0.08 confirming distinct entities in the music metadata graph.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Theory visualization: graph-based entity resolution for music attribution showing mention nodes for Imogen Heap and Brian Eno name variants connected by weighted edges from cascade scoring -- community detection identifies two clusters each resolving to a single ISNI identifier, with strong within-cluster edges above 0.85 and weak cross-community edges at 0.08 confirming distinct entities in the music metadata graph.](docs/figures/repo-figures/assets/fig-theory-18-graph-resolution.jpg)

*Figure 18. Graph-based entity resolution: entity mentions form a weighted graph where edge weights come from the resolution cascade (string similarity, embeddings, LLM judgment), and community detection algorithms identify clusters of mentions that resolve to the same real-world artist with an ISNI identifier.*

### From this figure plan (relative)

![Theory visualization: graph-based entity resolution for music attribution showing mention nodes for Imogen Heap and Brian Eno name variants connected by weighted edges from cascade scoring -- community detection identifies two clusters each resolving to a single ISNI identifier, with strong within-cluster edges above 0.85 and weak cross-community edges at 0.08 confirming distinct entities in the music metadata graph.](../assets/fig-theory-18-graph-resolution.jpg)
