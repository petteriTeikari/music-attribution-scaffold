# fig-topic-06: Entity Resolution

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-06 |
| **Title** | Entity Resolution — Fragmented Identity Network |
| **Audience** | General + Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Topic Card VI (Pipeline & Data group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Network graph showing fragmented artist names being resolved into unified entities. Communicates: "the same artist appears differently across databases — we link them."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│  FRAGMENTED              RESOLVED    │
│                                      │
│  ○ Imogen Heap  ─╲                  │
│  ○ iMi           ─── ● HEAP, I.    │
│  ○ Frou Frou    ─╱        ╲         │
│  ○ I Megaphone  ─╱         ╲        │
│                              ╲       │
│  ○ Deadmau5     ─╲           ╲      │
│  ○ deadmau5      ─── ● ZIMMERMAN   │
│  ○ Joel Z.      ─╱                  │
│                                      │
│  ── string sim  ─── identifier      │
│  ··· embedding  ─·─ graph           │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Fragmented nodes | `data_warning` | Orange small circles, disconnected |
| Resolved nodes | `data_primary` | Teal larger circles, unified clusters |
| String similarity edges | `line_solid` | Solid thin lines |
| Identifier edges | `line_dashed` | Dashed lines |
| Embedding edges | `line_dotted` | Dotted lines |
| Graph edges | `line_dash_dot` | Dash-dot lines |
| Labels | `label_editorial` | ALL-CAPS "FRAGMENTED" / "RESOLVED" headers |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. Only the following text should appear: "FRAGMENTED", "RESOLVED", artist name examples, edge type legend labels.

## Alt Text

Network graph showing fragmented artist names as small orange nodes on the left (Imogen Heap, iMi, Frou Frou, I Megaphone) being resolved via different matching strategies (string similarity, identifier, embedding, graph) into unified teal entity nodes on the right.
