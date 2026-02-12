# fig-topic-05: ETL Pipelines

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-05 |
| **Title** | ETL Pipelines — Multi-Source Data Convergence |
| **Audience** | General + Technical |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, Topic Card V (Pipeline & Data group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Five data sources converging through a normalization funnel into clean records. Communicates: "fragmented music metadata from five sources gets unified into a common schema."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                                      │
│  ● MusicBrainz    ──╲               │
│  ● Discogs         ──╲              │
│  ● AcoustID        ───►  NORMALIZE  │
│  ● Streaming       ──╱   ──────►    │
│  ● File Metadata   ──╱   Records    │
│                                      │
│  quality:  ████ ███ ██ ██ █          │
│            high          low         │
│                                      │
│  ■ CLEAN  ■ NOISY  ■ MISSING       │
│                                      │
└──────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Source dots | `data_sources` | Five colored dots (teal gradient by quality) |
| Convergence arrows | `line_flow` | Thin navy arrows converging to funnel |
| Funnel | `data_primary` | Teal trapezoid shape |
| Quality bars | `data_gradient` | Horizontal bars, teal (clean) to orange (noisy) |
| Output records | `data_accent` | Coral square markers for normalized records |
| Source labels | `label_editorial` | ALL-CAPS source names |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. Only the following text should appear: "MUSICBRAINZ", "DISCOGS", "ACOUSTID", "STREAMING", "FILE METADATA", "NORMALIZE", "CLEAN", "NOISY", "MISSING".

## Alt Text

Five colored source dots representing MusicBrainz, Discogs, AcoustID, streaming platforms, and file metadata converging through arrows into a normalization funnel. Quality indicator bars show data reliability ranging from high (teal) to low (orange) for each source.
