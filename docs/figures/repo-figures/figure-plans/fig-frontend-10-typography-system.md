# fig-frontend-10: Typography System

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-10 |
| **Title** | Typography System: Three Font Families with Editorial, Body, and Data Roles |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/design-system.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure presents the three-font typography system: Instrument Serif for display/editorial headings, Plus Jakarta Sans for body/UI text, and IBM Plex Mono for data values. Each font is shown with its CSS variable, weight range, typical sizes, and the editorial utility classes that apply them. Usage examples from the actual UI are included.

The key message is: "Three font families serve distinct roles -- Instrument Serif creates editorial gravitas for headings, Plus Jakarta Sans handles all body/UI text, and IBM Plex Mono makes confidence scores and data values instantly scannable."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  TYPOGRAPHY SYSTEM                                                     |
|  ■ Three Font Families                                                 |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. INSTRUMENT SERIF — Display                                         |
|  ──────────────────────────────                                        |
|                                                                        |
|  CSS var: --font-display                                               |
|  Weights: 400 (Regular, Italic)                                        |
|  Sizes: 48-96px (hero), 24-36px (section), 18-24px (subsection)       |
|                                                                        |
|  ┌──────────────────────────────────────────────┐                     |
|  │                                               │                     |
|  │  HIDE AND SEEK                                │ → Display           |
|  │  (large editorial heading, tight leading)     │                     |
|  │                                               │                     |
|  │  MUSIC ATTRIBUTION SCAFFOLD                   │ → Display           |
|  │  (hero title, ALL-CAPS)                       │ + uppercase         |
|  │                                               │                     |
|  └──────────────────────────────────────────────┘                     |
|                                                                        |
|  II. PLUS JAKARTA SANS — Body/UI                                       |
|  ────────────────────────────────                                      |
|                                                                        |
|  CSS var: --font-sans                                                  |
|  Weights: 200-800 (Variable)                                           |
|  Sizes: 12-18px (body), 10-12px (labels/caps)                         |
|                                                                        |
|  ┌──────────────────────────────────────────────┐                     |
|  │                                               │                     |
|  │  WORKS  REVIEW  PERMISSIONS                   │ → Caps              |
|  │  (nav links, uppercase, 0.15em tracking)      │ 500 weight          |
|  │                                               │                     |
|  │  Imogen Heap — artist name body text          │ text-sm/text-base   |
|  │  (regular body, 400-500 weight)               │                     |
|  │                                               │                     |
|  │  APPROVE ALL                                  │ → Caps              |
|  │  (action text, uppercase, accent underline)   │                     |
|  │                                               │                     |
|  └──────────────────────────────────────────────┘                     |
|                                                                        |
|  III. IBM PLEX MONO — Data                                             |
|  ──────────────────────────                                            |
|                                                                        |
|  CSS var: --font-mono                                                  |
|  Weights: 400, 500                                                     |
|  Sizes: 12-16px (inline data)                                          |
|  Feature: tabular-nums                                                 |
|                                                                        |
|  ┌──────────────────────────────────────────────┐                     |
|  │                                               │                     |
|  │  92%  0.87  3/8  v3                           │ → Mono              |
|  │  (confidence scores, counters, versions)      │                     |
|  │                                               │                     |
|  │  Source agreement: 95%                        │ → Mono              |
|  │  (conformal statistics, calibration error)    │                     |
|  │                                               │                     |
|  └──────────────────────────────────────────────┘                     |
|                                                                        |
|  UTILITY CLASSES                                                       |
|  ───────────────                                                       |
|  Display → Serif, weight 400, tight leading                            |
|  Display Italic → Same but italic                                      |
|  Caps → Uppercase, 0.15em letter-spacing, sans 500                     |
|  Mono → Monospace, tabular-nums                                        |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "TYPOGRAPHY SYSTEM" in display font |
| Instrument Serif section | `heading_display` | Font name, CSS var, weights, sizes, examples |
| Plus Jakarta Sans section | `label_editorial` | Font name, CSS var, weight range, examples |
| IBM Plex Mono section | `data_mono` | Font name, CSS var, weights, tabular-nums, examples |
| Example panels | `processing_stage` | Actual UI text examples for each font |
| CSS variable labels | `data_mono` | --font-display, --font-sans, --font-mono |
| Utility class table | `module_grid` | Four classes with their definitions |
| Roman numerals I-III | `section_numeral` | Section identifiers |

## Anti-Hallucination Rules

1. The three fonts are: Instrument Serif (display), Plus Jakarta Sans (body), IBM Plex Mono (data).
2. Loaded via next/font/google in layout.tsx with CSS variables --font-display, --font-sans, --font-mono.
3. Instrument Serif: weight 400 only, both normal and italic styles.
4. Plus Jakarta Sans: variable weight 200-800.
5. IBM Plex Mono: weights 400 and 500 only.
6. The font is NOT Inter (replaced by Plus Jakarta Sans in this project).
7. Four utility classes: .editorial-display, .editorial-display-italic, .editorial-caps, .data-mono.
8. NEVER use `text-[var(--text-*)]` -- this is a Tailwind v4 pitfall that generates color instead of font-size.
9. Font sizes use Tailwind built-in scale (text-xs through text-7xl), not custom properties.

## Alt Text

Design system diagram of the three-font typography system for the music attribution scaffold: Instrument Serif for editorial display headings, Plus Jakarta Sans for body and UI text, and IBM Plex Mono for transparent confidence scoring data values, with four CSS utility classes enabling consistent music metadata presentation.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Design system diagram of the three-font typography system for the music attribution scaffold: Instrument Serif for editorial display headings, Plus Jakarta Sans for body and UI text, and IBM Plex Mono for transparent confidence scoring data values, with four CSS utility classes enabling consistent music metadata presentation.](docs/figures/repo-figures/assets/fig-frontend-10-typography-system.jpg)

*Figure: Three font families serve distinct roles in the music attribution UI -- Instrument Serif creates editorial gravitas for headings, Plus Jakarta Sans handles body text and navigation, and IBM Plex Mono with tabular-nums makes confidence scores instantly scannable.*

### From this figure plan (relative)

![Design system diagram of the three-font typography system for the music attribution scaffold: Instrument Serif for editorial display headings, Plus Jakarta Sans for body and UI text, and IBM Plex Mono for transparent confidence scoring data values, with four CSS utility classes enabling consistent music metadata presentation.](../assets/fig-frontend-10-typography-system.jpg)
