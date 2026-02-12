# fig-topic-03: Uncertainty Propagation

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-03 |
| **Title** | Uncertainty Propagation — Pipeline Confidence Ribbons |
| **Audience** | Technical |
| **Complexity** | L3 (detailed) |
| **Location** | Landing page, Topic Card III (Confidence & Uncertainty group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Pipeline flow diagram with uncertainty ribbons that widen and narrow at each processing stage. Communicates: "uncertainty propagates through the pipeline — we track it at every step."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│  ETL     ENTITY      SOURCE    FINAL │
│  ──>     RESOLVE     CORR      SCORE │
│                                      │
│  ╔═╗     ╔════╗     ╔══╗     ╔═══╗  │
│  ║ ║     ║    ║     ║  ║     ║   ║  │
│  ║ ║ ──> ║    ║ ──> ║  ║ ──> ║ ● ║  │
│  ║ ║     ║    ║     ║  ║     ║   ║  │
│  ╚═╝     ╚════╝     ╚══╝     ╚═══╝  │
│  narrow   wider     narrows   final  │
│  ±0.05    ±0.15     ±0.08    ±0.10  │
│                                      │
│  ── uncertainty ribbon ──            │
│  ── point estimate ──                │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Pipeline stages | `data_primary` | Teal boxes connected by arrows |
| Uncertainty ribbons | `data_secondary` | Semi-transparent teal bands, varying width |
| Point estimate line | `line_accent` | Coral center line through ribbon |
| Stage labels | `label_editorial` | ALL-CAPS stage names above each box |
| Confidence intervals | `typography_mono` | ±values in IBM Plex Mono below each stage |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. Only the following text should appear: "ETL", "ENTITY RESOLUTION", "SOURCE CORROBORATION", "FINAL SCORE", numeric intervals.

## Alt Text

Horizontal pipeline flow diagram showing four processing stages connected by arrows. Each stage has an uncertainty ribbon whose width varies: narrow at ETL extraction, widening at entity resolution, narrowing again at source corroboration, and settling at the final confidence score with interval.
