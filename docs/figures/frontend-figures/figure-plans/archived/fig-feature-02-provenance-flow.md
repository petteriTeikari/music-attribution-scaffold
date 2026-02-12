# fig-feature-02: Provenance Flow

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-feature-02 |
| **Title** | Provenance Flow — Data Lineage as Art |
| **Audience** | General + Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Feature II section |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Constructivist-style data flow diagram showing how provenance events build confidence over time. Dots, lines, and nodes in red/navy/teal on cream. Communicates: "every step is tracked and auditable."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│  ● FETCH ──── ● RESOLVE ──── ●      │
│  │                            │      │
│  ● ─────────── ● SCORE ──── ●      │
│  │                            │      │
│  ● ─── ● REVIEW ── ● UPDATE │      │
│                                      │
│  ■────────────────────────────       │
│  confidence: 0% ──────── 95%        │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Source nodes | `node_source` | Small squares, colored by source |
| Process nodes | `node_process` | Coral red accent squares |
| Connecting lines | `line_accent` | Thin 1px lines |
| Confidence gradient | `data_primary` | Horizontal bar, low→high |
| Event labels | `label_editorial` | ALL-CAPS tracking, positioned near nodes |

## Anti-Hallucination Rules

These are INTERNAL instructions for the image generator. They must NEVER appear as visible text in the output:

1. **Font names are internal** — "IBM Plex Mono", "Plus Jakarta Sans", "Instrument Serif" are CSS font references. Do NOT render them as visible labels in the figure.
2. **Color tier names are internal** — "amber", "medium amber", "high confidence" are semantic descriptions. The confidence gradient bar should use only the hex colors (#C44536 → #E09F3E → #4A7C59) with percentage labels ("0%" and "95%"), NOT the word "amber".
3. **Semantic tags are internal** — `node_source`, `line_accent`, etc. are for the figure plan system. Do NOT render them.
4. Only the following text should appear in the figure: "PROVENANCE FLOW", "DATA LINEAGE AS ART", "FETCH", "RESOLVE", "SCORE", "REVIEW", "UPDATE", "0%", "95%", and Roman numerals I, II, III.

## Alt Text

Constructivist-style data flow diagram showing provenance events (fetch, resolve, score, review, update) connected by thin lines on a cream background. A horizontal confidence bar at the bottom shows progression from 0% to 95%.
