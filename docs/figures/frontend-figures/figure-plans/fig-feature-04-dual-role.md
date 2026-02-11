# fig-feature-04: Dual-Role Interface

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-feature-04 |
| **Title** | Dual-Role — Artist Gold / Query Blue |
| **Audience** | General |
| **Complexity** | L1 (concept) |
| **Location** | Landing page, Feature IV section |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Split composition showing the two interface modes: warm gold (artist) vs cool blue (query). Asymmetric vertical split. Communicates: "one interface, two perspectives — creating and discovering music."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────┐
│                │                     │
│    ARTIST      │      QUERY          │
│    ■ gold      │      ■ blue         │
│                │                     │
│  Abstract      │    Abstract         │
│  waveform      │    frequency        │
│  flowing left  │    spectrum right   │
│  (warm tones)  │    (cool tones)     │
│                │                     │
│  EDIT          │    BROWSE           │
│  APPROVE       │    SEARCH           │
│  REVIEW        │    DISCOVER         │
│                │                     │
│                ▎coral accent line    │
│                │                     │
└──────────────────────────────────────┘
```

## Visual Direction — Music-Specific

The current generation used generic tech/science illustrations (node graphs, geometric circles) on the Query side. This does NOT match the music platform identity.

### What the figure SHOULD contain:

**Left panel (Artist / Gold):**
- Warm gold-tinted background (#D4A03C at 8-10% opacity)
- Abstract **audio waveform** flowing horizontally — organic, hand-drawn quality
- The waveform uses gold (#D4A03C) and navy (#1E3A5F) tones
- Suggests creation, editing, the artist's hand shaping sound
- Style reference: Warp Records album art, analog synthesizer readouts

**Right panel (Query / Blue):**
- Cool blue-tinted background (#5B9BD5 at 8-10% opacity)
- Abstract **frequency spectrum / equalizer bars** — vertical bars of varying heights
- The bars use blue (#5B9BD5) and navy (#1E3A5F) tones
- Suggests browsing, discovering, analyzing a music catalog
- Style reference: vintage spectrum analyzers, vinyl record grooves seen from above
- NOT: generic tech shapes, node/graph networks, molecular diagrams, circles/dots

**Divider:**
- Thin coral red (#E84C4F) vertical accent line, slightly off-center (40/60 split)

### Key aesthetic constraint:
Both sides should feel like they belong on a **music platform** — waveforms, frequencies, audio visualization — NOT on a generic tech/data science tool.

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Left panel | `surface_warm` | Gold-tinted background (#D4A03C at 10%) |
| Right panel | `surface_cool` | Blue-tinted background (#5B9BD5 at 10%) |
| Vertical divider | `line_accent` | Coral red accent line, slightly off-center |
| Artist label | `label_display` | "ARTIST" in large display serif |
| Query label | `label_display` | "QUERY" in large display serif |
| Action words | `label_editorial` | ALL-CAPS: EDIT, APPROVE, REVIEW / BROWSE, SEARCH, DISCOVER |
| Left art | `waveform_warm` | Abstract audio waveform in gold/navy tones |
| Right art | `spectrum_cool` | Abstract frequency bars/spectrum in blue/navy tones |
| Role indicators | `indicator_role` | Gold square (left), Blue square (right) |

## Anti-Hallucination Rules

These are INTERNAL instructions for the image generator. They must NEVER appear as visible text in the output:

1. **Font names are internal** — "Instrument Serif", "Plus Jakarta Sans" are CSS references. Do NOT render them as visible text.
2. **Semantic tags are internal** — `surface_warm`, `label_display`, etc. Do NOT render them.
3. **Hex codes are internal** — Color values like "#D4A03C" are for the generator's palette. Do NOT render them.
4. **Style references are internal** — "Warp Records", "Bauhaus" are aesthetic direction. Do NOT render them.
5. Only the following text should appear in the figure: "ARTIST", "QUERY", "EDIT", "APPROVE", "REVIEW", "BROWSE", "SEARCH", "DISCOVER".
6. **No generic tech shapes** — no molecular diagrams, no node-and-edge graphs, no circuit boards, no pie charts. Both panels must use MUSIC-related abstract art (waveforms, frequencies, equalizer bars, sound visualization).

## Alt Text

Split composition showing two interface modes: warm gold-tinted left panel labeled "Artist" with abstract audio waveform art and actions edit, approve, review; cool blue-tinted right panel labeled "Query" with abstract frequency spectrum visualization and actions browse, search, discover. A coral red vertical line divides the two perspectives.
