# fig-group-01: Confidence & Uncertainty (Group Overview)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-group-01 |
| **Title** | Confidence & Uncertainty — Group Overview |
| **Audience** | General (landing page visitors) |
| **Complexity** | L1 (overview — bold visual, minimal text) |
| **Location** | Landing page, Key Concepts section — right of "Confidence & Uncertainty" topic cards |
| **Priority** | P1 (High) |
| **Dimensions** | 600 x 1200px (1:2 narrow portrait ratio) |

## Purpose & Key Message

A narrow portrait sidebar figure summarizing the four concepts in the Confidence & Uncertainty group: calibration, uncertainty types, propagation, and conformal prediction. Functions as a visual table of contents for Topics I–IV. Should read as one unified vertical composition, not four separate charts.

Communicates: "confidence is calibrated, uncertainty is tracked, and the system knows when to ask a human."

## Covers Topics

- I: Calibrated Confidence (calibration curve)
- II: Uncertainty vs. Confidence (reducible vs. irreducible)
- III: Uncertainty Propagation (pipeline ribbon)
- IV: Conformal & Selective Prediction (prediction set + abstention)

## Visual Concept (ASCII Layout)

```
┌──────────────┐
│              │
│  I  CALIBRATE│
│              │
│   1.0 ┤  /  │
│       │ / . │
│       │//   │
│   0.0 ├──── │
│              │
│ ─────────── │
│              │
│  II  TYPES   │
│              │
│  ┌──┐ ┌───┐ │
│  │  │ │   │ │
│  └──┘ │   │ │
│   ↓   │   │ │
│  ┌┐   └───┘ │
│  └┘         │
│ shrinks stays│
│              │
│ ─────────── │
│              │
│  III FLOW    │
│              │
│    │ │       │
│   │   │      │
│    │ │       │
│     ●        │
│   0.91       │
│              │
│ ─────────── │
│              │
│  IV  PREDICT │
│              │
│   ╭───╮     │
│   │ ● │     │
│   ╰───╯     │
│  ═══════    │
│  predict    │
│  abstain    │
│              │
└──────────────┘
```

## Design Notes

- **Narrow portrait 1:2** — this sits beside a column of topic cards, not full-width
- **Four stacked mini-vignettes** separated by thin accent lines, flowing as one vertical composition
- **Each vignette is ~25% of height**: just ONE key visual from each topic — no text explanations
- **Vignette I**: Three-line calibration curve (ideal dashed, calibrated teal, overconfident orange)
- **Vignette II**: Two columns — teal block shrinks, orange block stays (with down arrow)
- **Vignette III**: Vertical uncertainty ribbon (narrow → wide → narrow) with final score dot
- **Vignette IV**: Concentric teal arcs around coral dot, coral threshold line below
- **Roman numerals I–IV** as small labels in warm gray at each section
- **Minimal text**: only Roman numerals and "0.91" score. Everything else is visual.
- **Cream background, halftone grain** — matches all other figures

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Calibration curve | `data_primary` | Three lines: dashed ideal, teal calibrated, orange overconfident |
| Uncertainty columns | `data_primary` + `data_warning` | Teal shrinking block, orange stable block |
| Propagation ribbon | `data_primary` | Teal ribbon varying width vertically |
| Prediction arcs | `data_primary` | Concentric teal arcs around coral point |
| Threshold line | `line_accent` | Coral horizontal line |
| Section dividers | `line_subtle` | Thin warm gray horizontal lines between vignettes |
| Roman numerals | `label_editorial` | I, II, III, IV in warm gray |
| Score | `typography_mono` | "0.91" at propagation output |
| Background | `background` | Cream (#f6f3e6) |

## Color Palette

| Element | Color |
|---------|-------|
| Background | #f6f3e6 (cream) |
| Primary data (calibrated, ribbon, arcs) | #2E7D7B (teal) |
| Warning data (overconfident, irreducible) | #E76F51 (orange) |
| Accent (point estimates, threshold) | #E84C4F (coral) |
| Reference lines, labels | #1E3A5F (navy) |
| Dividers, numerals | #8B7E6A (warm gray) |

## Nano Banana Pro Prompts

### Style prompt
Flat 2D editorial illustration on warm cream background (#f6f3e6). Narrow portrait format 1:2 ratio. Constructivist visual language. Thin lines, flat fills, no shadows, no gradients, no 3D. Risograph halftone grain. Colors: teal (#2E7D7B), coral (#E84C4F), orange (#E76F51), navy (#1E3A5F), warm gray (#8B7E6A). Four stacked visual vignettes flowing as one unified vertical composition. Minimal text — mostly visual symbols and shapes.

### Content prompt
Narrow portrait composition (600x1200px). Four stacked visual vignettes separated by thin warm gray divider lines, each labeled with a small Roman numeral (I, II, III, IV). VIGNETTE I (top 25%): Simple calibration curve — three clean lines: dashed navy diagonal (ideal), solid teal curve close to diagonal (calibrated), solid orange curve pulling away (overconfident). Minimal axes, no labels except 0 and 1. VIGNETTE II (25%): Two side-by-side columns. Left: teal filled rectangle, down arrow, smaller teal rectangle (uncertainty shrinks). Right: orange filled rectangle same size top and bottom (uncertainty stays). VIGNETTE III (25%): Vertical teal ribbon flowing top to bottom — narrow, then widens (tinted orange where widest), then narrows again. A small dot at the bottom labeled "0.91". VIGNETTE IV (bottom 25%): Concentric teal arcs (3 nested bands) around a coral center dot. Below the arcs, a coral horizontal threshold line. Above line: small teal square. Below line: small orange square. Generous whitespace. Halftone grain overlay. The four vignettes should feel like ONE composition, not four separate images.

### Negative prompt
--no 3D, shadows, gradients, photorealistic, dense text, formula, equation, multiple words, paragraph text, labels longer than 5 characters, scatter plot, bar chart, pie chart, dark background, neon, wireframe, horizontal layout, separate panels with borders

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render.
2. **Semantic tags are internal** — do NOT render.
3. **Pixel sizes are internal** — do NOT render.
4. Only render: Roman numerals "I", "II", "III", "IV", score "0.91", axis markers "0" and "1". NO other text.
5. **Narrow portrait** — width is HALF the height. Non-negotiable.
6. **One composition** — four vignettes flow as a single vertical piece, not four separate boxed images.

## Alt Text

Narrow portrait overview of the Confidence & Uncertainty concept group. Four stacked visual vignettes: (I) a calibration curve with ideal diagonal, calibrated teal line, and overconfident orange line; (II) two columns showing reducible uncertainty shrinking (teal) versus irreducible uncertainty staying the same (orange); (III) a vertical uncertainty ribbon that widens at entity resolution and narrows to a final score of 0.91; (IV) concentric teal prediction set arcs around a point estimate with a coral abstention threshold line.
