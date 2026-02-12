# fig-topic-09: Provenance & Attribution-by-Design

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-09 |
| **Title** | Provenance Lineage — Attribution-by-Design vs. Post-Hoc |
| **Audience** | General + Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Topic Card IX (Governance & Security group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Side-by-side comparison of attribution-by-design (solid provenance chain) versus post-hoc attribution (broken chain). Communicates: "embed provenance at creation — post-hoc attribution hits the Oracle Problem."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│  ATTRIBUTION         POST-HOC        │
│  BY DESIGN           ATTRIBUTION     │
│                                      │
│  ● create     ─╲     ○ · · · · ○    │
│  │              ╲                    │
│  ● resolve    ── ╲    ○ · · ○       │
│  │              ║  ╲                 │
│  ● corroborate  ║   ╲  ○ · ?       │
│  │              ║                    │
│  ● verify    ── ║    ORACLE          │
│                 ║    BOUNDARY         │
│  solid chain    ║    broken chain     │
│                 ║                     │
│  ■ RECORDED  ■ INFERRED  ? UNKNOWN  │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| By-design chain | `data_primary` | Teal solid vertical line with event dots |
| Post-hoc chain | `data_warning` | Orange dotted line with gaps |
| Oracle boundary | `line_accent` | Coral vertical divider between approaches |
| Event markers | `data_accent` | Filled circles (by-design) vs. hollow (post-hoc) |
| Unknown marker | `data_error` | Red question mark |
| Labels | `label_editorial` | ALL-CAPS approach names |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. Only the following text should appear: "ATTRIBUTION-BY-DESIGN", "POST-HOC", "ORACLE BOUNDARY", "CREATE", "RESOLVE", "CORROBORATE", "VERIFY", "RECORDED", "INFERRED", "UNKNOWN".

## Alt Text

Side-by-side comparison with a coral Oracle Boundary dividing two approaches. Left: attribution-by-design shown as a solid teal vertical chain of four provenance events. Right: post-hoc attribution shown as a broken orange dotted chain with gaps and a red question mark for unknown provenance.
