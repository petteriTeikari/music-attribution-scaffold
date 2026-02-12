# fig-group-02: Pipeline & Data (Group Overview)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-group-02 |
| **Title** | Pipeline & Data — Group Overview |
| **Audience** | General (landing page visitors) |
| **Complexity** | L1 (overview — bold visual, minimal text) |
| **Location** | Landing page, Key Concepts section — right of "Pipeline & Data" topic cards |
| **Priority** | P1 (High) |
| **Dimensions** | 600 x 1200px (1:2 narrow portrait ratio) |

## Purpose & Key Message

A narrow portrait sidebar figure summarizing the three concepts in the Pipeline & Data group: ETL from multiple sources, entity resolution linking fragmented identities, and active learning prioritizing human review. Functions as a visual table of contents for Topics V–VII.

Communicates: "data flows in from five sources, identities are resolved, and humans review where it matters most."

## Covers Topics

- V: ETL Pipelines (five sources converging)
- VI: Entity Resolution (fragmented → unified)
- VII: Active Learning & Feedback Cards (decision boundary + review queue)

## Visual Concept (ASCII Layout)

```
┌──────────────┐
│              │
│  V   ETL     │
│              │
│  ● ● ● ● ●  │
│  │ │ │ │ │   │
│  ╲ │ │ │ ╱   │
│   ╲│ │ │╱    │
│    ▼ ▼ ▼     │
│   ┌─────┐    │
│   │     │    │
│   └─────┘    │
│              │
│ ─────────── │
│              │
│  VI  RESOLVE │
│              │
│  ○  ○  ○    │
│   ╲ │ ╱     │
│    ╲│╱      │
│     ●       │
│  ○ → ●     │
│              │
│ ─────────── │
│              │
│  VII REVIEW  │
│              │
│  ●●●●       │
│  ●●● ●      │
│  ── boundary │
│     ○○○     │
│     → human  │
│              │
└──────────────┘
```

## Design Notes

- **Narrow portrait 1:2** — sidebar next to topic cards
- **Three stacked vignettes** (~33% each), separated by thin accent lines
- **Vignette V (ETL)**: Five colored dots at top (matching source colors: purple MusicBrainz, dark gray Discogs, teal AcoustID, blue streaming, gray file) converging through lines into a single teal box (normalized record). The classic "funnel" simplified to dots + lines.
- **Vignette VI (Entity Resolution)**: Orange disconnected dots (fragmented identities) on top, lines converging into a teal dot (resolved entity). Simple network: scattered → clustered.
- **Vignette VII (Active Learning)**: Dots scattered around a coral decision boundary line. Teal dots (confident) above the line, orange dots (uncertain) below — routed to a small human icon or "review" label. The boundary shifts with each review.
- **Roman numerals V–VII** as small labels
- **Minimal text**: only numerals and maybe "5 sources" at ETL. Everything visual.

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Five source dots | `data_sources` | Five colored dots (purple, gray, teal, blue, gray) |
| Funnel lines | `line_flow` | Lines converging from 5 dots to 1 box |
| Normalized record | `data_primary` | Single teal rectangle |
| Fragmented dots | `data_warning` | Orange scattered dots (disconnected) |
| Resolved dot | `data_primary` | Teal center dot with convergence lines |
| Decision boundary | `line_accent` | Coral horizontal boundary line |
| Confident dots | `data_primary` | Teal dots above boundary (auto-approved) |
| Uncertain dots | `data_warning` | Orange dots below boundary (review queue) |
| Section dividers | `line_subtle` | Thin warm gray lines between vignettes |
| Roman numerals | `label_editorial` | V, VI, VII |
| Background | `background` | Cream (#f6f3e6) |

## Color Palette

| Element | Color |
|---------|-------|
| Background | #f6f3e6 (cream) |
| MusicBrainz source | #6B3FA0 (purple) |
| Discogs source | #444444 (dark gray) |
| AcoustID source | #2E7D7B (teal) |
| Streaming source | #5B9BD5 (blue) |
| File metadata source | #8B7E6A (warm gray) |
| Resolved/confident | #2E7D7B (teal) |
| Fragmented/uncertain | #E76F51 (orange) |
| Decision boundary | #E84C4F (coral) |
| Numerals, dividers | #8B7E6A (warm gray) |

## Nano Banana Pro Prompts

### Style prompt
Flat 2D editorial illustration on warm cream background (#f6f3e6). Narrow portrait format 1:2 ratio. Constructivist design language. Flat fills, thin lines, no shadows, no gradients, no 3D. Risograph halftone grain. Colors: teal (#2E7D7B), orange (#E76F51), coral (#E84C4F), purple (#6B3FA0), dark gray (#444444), blue (#5B9BD5), warm gray (#8B7E6A). Three stacked vignettes as one unified composition. Minimal text.

### Content prompt
Narrow portrait composition (600x1200px). Three stacked visual vignettes separated by thin warm gray dividers, each with a small Roman numeral label. VIGNETTE V (top 33%): Five colored dots at top (purple, dark gray, teal, blue, warm gray — representing five data sources) with thin lines converging downward into a single teal rectangle (normalized record). Classic data funnel simplified to dots and lines. VIGNETTE VI (middle 33%): Three orange dots scattered (disconnected fragmented identities), with thin lines converging to a single teal dot in the center (resolved entity). Below: another orange dot with an arrow pointing to the teal center. Network resolution: fragmented to unified. VIGNETTE VII (bottom 33%): A coral horizontal line (decision boundary). Above the line: several teal dots clustered together (high-confidence, auto-approved). Below the line: several orange dots (uncertain, near boundary). A small arrow from the orange dots pointing right toward a simple human-review icon or small square. The boundary visually separates automatic from human-reviewed. Generous whitespace. Halftone grain. One unified vertical composition.

### Negative prompt
--no 3D, shadows, gradients, photorealistic, dense text, formula, paragraph text, bar chart, pie chart, dark background, neon, wireframe, horizontal layout, separate bordered panels, photographs, faces

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render.
2. **Semantic tags are internal** — do NOT render.
3. **Pixel sizes are internal** — do NOT render.
4. Only render: Roman numerals "V", "VI", "VII". NO other text.
5. **Narrow portrait** — width is HALF the height. Non-negotiable.
6. **One composition** — three vignettes flow vertically, not as separate images.

## Alt Text

Narrow portrait overview of the Pipeline & Data concept group. Three stacked visual vignettes: (V) five colored source dots (purple MusicBrainz, gray Discogs, teal AcoustID, blue streaming, gray file metadata) converging through a funnel into a single normalized record; (VI) scattered orange dots representing fragmented artist identities converging into a single teal resolved entity; (VII) a coral decision boundary separating teal confident dots (auto-approved above) from orange uncertain dots (routed to human review below).
