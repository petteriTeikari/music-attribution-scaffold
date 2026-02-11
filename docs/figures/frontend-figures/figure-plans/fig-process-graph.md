# fig-process-graph: Attribution Pipeline as Signal Chain

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-process-graph |
| **Title** | From Raw Data to Trusted Credits — The Attribution Signal Chain |
| **Audience** | Musicians, producers, record label professionals (NOT engineers) |
| **Complexity** | L2 (overview) |
| **Location** | Landing page, "How It Works" / Process section (right column) |
| **Priority** | P1 (High) |
| **Dimensions** | 900 x 1200px (3:4 portrait ratio) |

## Purpose & Key Message

A portrait-mode figure showing the 4-stage attribution pipeline as an **audio signal chain** metaphor — data flows top-to-bottom through processing stages, like audio through a mixing console channel strip. Multiple source signals enter at the top, get merged and cleaned, then emerge at the bottom as confidence-scored credits. A feedback arrow loops back up, showing the system improves with artist input.

Communicates: "Your music's identity flows through four stages and gets more trustworthy at each one. You can correct the system at any point, and it learns."

## Visual Concept (ASCII Layout)

```
┌────────────────────────────────────────┐
│                                        │
│  ● MB  ● DC  ● AI  ● FM  ● YOU       │
│  │     │     │     │     │            │
│  └──┬──┘  ┌──┘     └──┬──┘            │
│     └─────┤           │               │
│           └─────┬─────┘               │
│                 ↓                      │
│  ┌──────────────────────┐              │
│  │  FETCH & NORMALIZE   │ ← Stage 1   │
│  │  ━━━━━━━━━━━━━━━━━━  │              │
│  │  Quality gate, field │              │
│  │  standardization     │              │
│  └──────────┬───────────┘              │
│             ↓                          │
│  ┌──────────────────────┐              │
│  │  RESOLVE ENTITIES    │ ← Stage 2   │
│  │  ━━━━━━━━━━━━━━━━━━  │              │
│  │  Match, merge,       │              │
│  │  deduplicate         │              │
│  └──────────┬───────────┘              │
│             ↓                          │
│  ┌──────────────────────┐              │
│  │  SCORE & CALIBRATE   │ ← Stage 3   │
│  │  ━━━━━━━━━━━━━━━━━━  │              │
│  │  Confidence bands,   │              │
│  │  assurance levels    │              │
│  └──────────┬───────────┘              │
│             ↓                          │
│  ┌──────────────────────┐              │
│  │  REVIEW & IMPROVE    │ ← Stage 4   │
│  │  ━━━━━━━━━━━━━━━━━━  │              │
│  │  Expert feedback,    │              │
│  │  corrections         │              │
│  └──────────┬───────────┘              │
│             │                          │
│       ╭─────┴─────╮                    │
│       │  TRUSTED   │                   │
│       │  CREDITS   │                   │
│       ╰────────────╯                   │
│             │                          │
│             └─── feedback ──→ (loops   │
│                               back up) │
│                                        │
└────────────────────────────────────────┘
```

## Visual Direction — Audio Signal Chain Metaphor

This figure should look like it belongs in a **recording studio control room poster** or a **vinyl pressing plant diagram** — not in an engineering whitepaper.

### Overall Composition

The figure uses a **mixing console channel strip** as its organizing metaphor:
- Signal enters from 5 source "inputs" at the top (like 5 audio channels being summed)
- Each processing stage is a horizontal band that the signal passes through (like EQ, compression, etc.)
- The stages are connected by vertical lines (the signal path)
- At the bottom, the processed signal emerges as "trusted credits"
- A thin feedback line arcs back up from bottom to top along the right edge

### Source Inputs (Top)

5 distinct input lines converging into the first stage:
- **MusicBrainz**: Purple dot/line
- **Discogs**: Dark gray dot/line
- **AcoustID**: Teal dot/line
- **File Metadata**: Warm gray dot/line
- **Artist (You)**: Gold dot/line — thicker, emphasized as the highest-authority source

The converging lines should feel organic, not rigid — like audio cables being patched into a mixer.

### Processing Stages (Middle)

Each of the 4 stages is a horizontal band/zone:

**Stage 1 — Fetch & Normalize** (top zone):
- Abstract representation of data being cleaned and standardized
- Chaotic lines entering, orderly lines exiting
- Thin horizontal rules (like EQ frequency bands)
- Coral red accent square as stage marker

**Stage 2 — Resolve Entities** (second zone):
- Overlapping circles or converging node clusters being merged into single entities
- Lines crossing and reconnecting (like a patchbay)
- Constructivist connecting lines between nodes
- Multiple paths resolving into fewer, thicker paths

**Stage 3 — Score & Calibrate** (third zone):
- Small confidence arc/gauge motif (echoes the fig-feature-01 style)
- Horizontal gradient band showing low→high confidence
- A0-A3 level indicators as colored markers (gray, amber, blue, green)
- Numbers or tick marks suggesting measurement and precision

**Stage 4 — Review & Improve** (bottom zone):
- Human hand/pen motif (abstract, not literal — a mark or checkmark)
- Correction arrows showing adjustments
- The feedback loop arrow arcing upward along the right edge
- Suggests the system learns and improves

### Output (Bottom)

A stylized output icon — could be a vinyl record shape, a waveform resolved into a clean signal, or simply the word "CREDITS" in editorial typography.

### Feedback Loop (Right Edge)

A thin teal line arcs from the bottom-right back up to the top-right, with small coral squares marking feedback points (REFETCH, RECALIBRATE, DISPUTE signals). This communicates the system is not one-shot — it continuously improves.

### Color Scheme

| Element | Color | Purpose |
|---------|-------|---------|
| Background | #f6f3e6 (cream) | Matches page background |
| Stage bands | Navy (#1E3A5F) at varying opacity | Processing zones |
| Source lines | Source-specific colors (purple, gray, teal, gold) | Data provenance |
| Stage markers | Coral red (#E84C4F) squares | Visual anchors matching design system |
| Feedback loop | Teal (#2E7D7B) | Innovation, continuous improvement |
| Confidence indicators | Green/amber/gray | A0-A3 levels |
| Connecting lines | Warm gray (#8B7E6A) | Signal paths |

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Source input dots | `node_source` | 5 colored dots at top, one per data source |
| Converging input lines | `line_input` | Lines from sources merging into Stage 1 |
| Stage 1 band | `zone_etl` | Horizontal processing zone — chaotic→orderly |
| Stage 2 band | `zone_resolution` | Horizontal zone — many→few (merging entities) |
| Stage 3 band | `zone_scoring` | Horizontal zone — gauge/spectrum motif |
| Stage 4 band | `zone_review` | Horizontal zone — human correction marks |
| Vertical signal path | `line_signal` | Central vertical line connecting all stages |
| Stage markers | `marker_accent` | Small coral squares at each stage (4 total) |
| Feedback arc | `line_feedback` | Teal arc on right edge from bottom to top |
| Feedback nodes | `node_feedback` | Small coral squares on the feedback arc |
| Output icon | `output_credits` | Stylized resolved-signal or record icon at bottom |
| Stage labels | `label_editorial` | Optional faint ALL-CAPS labels if space permits |

## Nano Banana Pro Prompts

### Style prompt

Audio signal chain diagram as constructivist art on warm cream background (#f6f3e6). Mixing console channel strip metaphor — signal flows vertically from top to bottom through four processing stages. Warp Records aesthetic meets vintage recording studio diagram. Thin connecting lines between colored source dots at top. Four horizontal processing bands in navy at varying opacity. Coral red squares as stage markers. Teal feedback arc along right edge. Matte finish, risograph print quality. Editorial art direction. Portrait composition 3:4 ratio. NOT a generic flowchart — feels like a studio control room poster.

### Content prompt

Portrait composition (900x1200). Five colored dots at top representing data sources (purple, dark gray, teal, warm gray, gold) with thin lines converging downward into the first of four horizontal processing bands. Each band represents a pipeline stage — the top band shows chaotic lines becoming orderly (normalization), the second shows overlapping clusters merging (entity resolution), the third shows a small confidence gauge/spectrum with colored level indicators (scoring), the fourth shows correction marks and a checkmark (review). A thin vertical signal line connects all four bands centrally. On the right edge, a teal line arcs from bottom back to top with small coral red squares marking feedback points. At the bottom, a simple resolved-signal output icon. Each stage has a small coral red square as its marker. Roman numerals I-IV as very faint labels. The overall feel is an audio mixing process — messy signal in, clean confident output out.

### Negative prompt

--no generic flowchart, corporate diagram, PowerPoint arrows, neon glow, dark background, photorealistic, 3D render, text labels, font names, literal screenshots, UI mockup, symmetric layout, centered composition, thick arrows, drop shadows, gradient fills, pie charts, bar charts

## Anti-Hallucination Rules

These are INTERNAL instructions for the image generator. They must NEVER appear as visible text in the output:

1. **Font names are internal** — "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them.
2. **Technical terms are internal** — "ETL", "entity resolution", "conformal prediction", "Bayesian" are engineering terms. Do NOT render them as visible labels.
3. **Color names are internal** — "coral red", "navy", "teal" are palette descriptions. Do NOT render them.
4. **Semantic tags are internal** — `zone_etl`, `line_signal`, etc. Do NOT render them.
5. The only text that MAY appear: Roman numerals I-IV as very small, faint stage markers. All other text is BANNED.
6. **NO generic flowchart aesthetics** — no thick block arrows, no rounded rectangles, no PowerPoint look. This must feel like analog audio equipment documentation or a constructivist art poster.
7. **Background MUST be #f6f3e6** — exact match to page surface color. No off-white, no pure white, no gray.

## Alt Text

Portrait-mode constructivist diagram showing four stages of a music attribution pipeline as an audio signal chain. Five colored source dots at top converge through horizontal processing bands representing data normalization, entity resolution, confidence scoring, and expert review. A teal feedback arc on the right edge loops from bottom to top, showing continuous improvement. Coral red squares mark each stage. The composition flows from messy input at top to confident output at bottom.
