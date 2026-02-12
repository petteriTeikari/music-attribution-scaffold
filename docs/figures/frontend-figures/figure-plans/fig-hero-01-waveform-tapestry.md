# fig-hero-01: MFCC Ridgeplot — Stacked Audio Topography

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-hero-01 |
| **Title** | MFCC Ridgeplot — Sound as Stacked Terrain |
| **Audience** | General (landing page visitors) |
| **Complexity** | L3 (hero — highest visual impact) |
| **Location** | Landing page hero section (full-width background behind text) |
| **Priority** | P0 (Critical — first visual impression, defines the entire site feel) |
| **Dimensions** | 2400 x 900px (8:3 landscape ratio) |

## Purpose & Key Message

A full-width hero image showing a **flat, 2D ridgeplot-style MFCC spectrogram** — stacked horizontal waveform bands representing mel-frequency coefficients, rendered in the same flat editorial illustration style as all topic figures. Think Joy Division's *Unknown Pleasures* album cover reinterpreted in the project's teal/coral/navy palette on cream, with constructivist accent elements (coral squares, thin accent lines).

**No text. No labels. No annotations. Pure visual.**

The style must be **identical to the topic figures**: flat illustration, thin line work, flat color fills, halftone grain texture, cream background, coral accent squares. It must look like it belongs on the same page as fig-topic-05 (Data Harmonization) and fig-topic-07 (Active Learning) — not like a different tool generated it.

Communicates: "This is sound data, visualized with editorial craft."

## Critical Layout Constraint: Left-to-Right Density Gradient

**This image sits BEHIND hero text on the left side.** The visual density MUST increase from left to right:

- **Left 30%**: Near-empty. The cream background (#f6f3e6) dominates. Only the faintest ghost of 1–2 waveform lines at very low opacity. Text overlay must be fully legible.
- **Middle 30%**: Waveform bands begin to appear — thin line outlines emerge, some with light flat fills. 5–8 bands visible. Sparse coral accent dots or small squares start appearing.
- **Right 40%**: Full density. 13–20 stacked waveform bands, each with distinct amplitude patterns. Rich flat fills in teal, coral, navy, warm gray. Bands overlap slightly. Coral accent squares punctuate peaks. Thin accent lines thread through. Dense, layered, editorial.

## Visual Concept: Flat 2D MFCC Ridgeplot

An MFCC spectrogram encodes audio as a matrix: time (x-axis), mel-frequency bands (stacked y-axis), energy as amplitude of each band's waveform. A ridgeplot renders each frequency band as a separate horizontal waveform line, stacked vertically with slight overlap — creating a mountain-range effect from pure 2D line art.

### What This IS (matching the topic figures)

- **Flat 2D illustration** — same style as fig-topic-05 and fig-topic-07
- **Thin line outlines** (1–2px weight) defining each waveform band
- **Flat color fills** below the waveform lines — no gradients, no shadows, no ambient occlusion
- **Stacked horizontal bands** — each mel-frequency coefficient is one horizontal waveform strip
- **Selective color**: most bands in navy or warm gray outline; a few key bands filled with teal, coral, or orange flat fill (like the topic figures use selective color highlighting)
- **Coral accent squares** (the project's signature graphic element) placed at peak amplitude points
- **Thin coral horizontal accent lines** running through the composition
- **Halftone grain texture** at 3–5% opacity (matching all topic figures)
- **Cream background** showing through between bands

### What This is NOT

- NOT a 3D render or sculptural surface (too photorealistic for the page)
- NOT a wireframe mesh (previous version — too engineering)
- NOT a network graph with nodes and connecting lines
- NOT a glossy, metallic, or lit surface
- NOT a gradient-heavy illustration

### ASCII Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         │                        │                      │
│  [TEXT OVERLAY ZONE]    │   Bands emerging       │  FULL DENSITY        │
│                         │                        │                      │
│                         │   ~~~~~~~~~~~~~~~      │  ~~╱╲~~╱╲~~╱╲~~~   │
│  Nearly empty.          │   ~~~~~~~~~~           │  ■ ╱╲╱╲╱╲╱╲╱╲~~   │
│  Ghost of 1-2 lines     │   ~~~~~~~~~~~~~        │  ~~~╱╲~~╱╲~~╱╲~~   │
│  at 5% opacity.         │   ~~~~~~~~             │  ~~╱╲╱╲╱╲╱╲~~~~~   │
│                         │   ~~~~~~~~~~~~         │  ■~~╱╲~~╱╲~~╱╲~~   │
│  Cream dominates.       │   Thin outlines,       │  ~~~╱╲╱╲╱╲╱╲~~~~   │
│                         │   light fills begin    │  Dense stacked bands │
│                         │                        │  Teal/coral/navy     │
│                         │                        │  fills. ■ squares.   │
│                         │                        │                      │
└─────────────────────────────────────────────────────────────────────────┘
  ← SPARSE / GHOST                                     DENSE / VIVID →
```

### Visual Language (same as topic figures)

The hero must share these exact traits with fig-topic-05/07/08:
- **Cream background** (#f6f3e6) — the paper stock
- **Flat fills**: teal (#2E7D7B), coral (#E84C4F), navy (#1E3A5F), orange (#E76F51), warm gray (#8B7E6A)
- **Thin line work**: 1–2px strokes, no variable-width brushes
- **Coral accent squares**: 16–28px solid blocks as visual punctuation (`.accent-square`)
- **Halftone grain overlay**: feTurbulence SVG texture at 3–5% opacity
- **No gradients**: all color transitions are hard edges between flat fills
- **Overlapping elements**: bands can overlap, with the cream showing through gaps — creates depth from layering, not from 3D rendering
- **Risograph print feel**: slightly imperfect registration, matte, tactile

### MFCC-Specific Details

Each stacked band represents one mel-frequency coefficient over time:
- **Lower bands** (bottom of stack): broader, smoother undulations — low-frequency energy (bass, drums)
- **Upper bands** (top of stack): sharper, more jagged — high-frequency detail (consonants, cymbals, harmonics)
- **13–20 bands** visible in the dense right portion
- **Peak amplitudes** correspond to sonic events — a vocal onset creates peaks across multiple bands simultaneously, visible as vertical alignment of peaks
- **Band spacing**: slight vertical offset between bands, with partial overlap creating the ridgeplot mountain-range effect

### Color Strategy for Bands

Not all bands should be the same color — selective color creates hierarchy:
- **2–3 bands**: filled with teal (these are the "signal" — the formant bands that carry the melody)
- **1–2 bands**: filled with coral (accent — a transient-heavy band, percussion)
- **1 band**: filled with navy (the fundamental, the bass)
- **Remaining bands**: warm gray outline only, no fill (context, not emphasis)
- This mirrors how the topic figures use selective color: not everything is colored, the color draws your eye to what matters

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Waveform bands (outline) | `line_waveform` | Thin line outlines, warm gray or navy, each band a mel-frequency coefficient |
| Teal-filled bands | `fill_teal` | 2–3 bands with flat teal fill — signal/formant emphasis |
| Coral-filled bands | `fill_coral` | 1–2 bands with flat coral fill — transient/accent emphasis |
| Navy-filled band | `fill_navy` | 1 band with flat navy fill — fundamental/bass |
| Coral accent squares | `accent_square` | Small solid coral blocks at peak amplitude points |
| Thin accent lines | `line_accent` | 1–2 thin coral horizontal lines running full width |
| Left fade | `gradient_opacity` | Bands fade to near-invisible on the left 30% |
| Halftone grain | `texture_grain` | Faint noise overlay (3–5% opacity) matching topic figures |
| Background | `background` | Cream (#f6f3e6) showing through between bands |

## Color Palette (identical to topic figures)

| Element | Color | Notes |
|---------|-------|-------|
| Background | #f6f3e6 (cream) | Same as all topic figures |
| Primary fill | #2E7D7B (teal) | Signal bands — same as topic figure teal elements |
| Accent fill | #E84C4F (coral) | Accent bands + squares — same as accent squares in all figures |
| Foundation fill | #1E3A5F (navy) | Bass band — same as navy text in topic figures |
| Context outline | #8B7E6A (warm gray) | Unfilled bands — background structure |
| Secondary fill | #E76F51 (orange) | Optional 1 band — same orange as topic figure warnings |

## Nano Banana Pro Prompts

### Style prompt
Flat 2D ridgeplot illustration on warm cream background (#f6f3e6). Stacked horizontal waveform bands in the style of Joy Division Unknown Pleasures but reinterpreted as flat editorial illustration. Same visual language as constructivist data infographics: thin line outlines, flat color fills (no gradients), small solid coral red accent squares as graphic punctuation. Halftone grain texture. Risograph print aesthetic. Matte, flat, tactile. NOT 3D, NOT glossy, NOT photorealistic. Colors: teal (#2E7D7B), coral red (#E84C4F), navy (#1E3A5F), warm gray (#8B7E6A), orange (#E76F51) — all flat, no gradients. Ultra-wide landscape 8:3 ratio.

### Content prompt
Ultra-wide landscape composition (2400x900). Flat 2D MFCC ridgeplot: 13-20 horizontal waveform bands stacked vertically with slight overlap, each band representing a mel-frequency coefficient over time. Rendered as flat editorial illustration, NOT 3D. Each band is a thin outline with selective flat color fill. Most bands are warm gray outline only. 2-3 bands filled with flat teal. 1-2 bands filled with flat coral red. 1 band filled with navy. Small coral accent squares (16-28px solid blocks) placed at peak amplitude points. 1-2 thin coral horizontal accent lines running full width. LEFT THIRD: nearly empty cream, only the ghost of 1-2 faint waveform lines at 5% opacity. MIDDLE THIRD: 5-8 bands emerging as thin outlines with light fills. RIGHT THIRD: full density, all 13-20 bands visible with rich flat fills, overlapping bands creating layered depth, coral squares punctuating peaks. Lower bands have broader undulations (bass energy), upper bands are sharper and more jagged (high-frequency detail). Cream background shows between bands. Halftone grain overlay. No text. No labels.

### Negative prompt
--no 3D render, 3D surface, sculptural, ceramic, ambient occlusion, shadows, glossy, metallic, gradients, smooth shading, photorealistic, wireframe mesh, network graph, nodes, connecting lines, dots, scatter plot, text, labels, annotations, font names, bar chart, pie chart, UI elements, screenshots, neon glow, dark background, pure black, symmetric, centered, faces, musical instruments, music notes, treble clef, stock photography, engineering plot, matplotlib, axes, tick marks, legend

## Anti-Hallucination Rules

These are INTERNAL instructions for the image generator. They must NEVER appear as visible text in the output:

1. **Font names are internal** — do NOT render any text whatsoever.
2. **Color names are internal** — "cream", "coral", "teal", "navy" are palette descriptions. Do NOT render them.
3. **Semantic tags are internal** — `line_waveform`, `fill_teal`, etc. Do NOT render them.
4. **Technical terms are internal** — "MFCC", "spectrogram", "mel-frequency", "ridgeplot" are concept references. Do NOT render them.
5. **NO TEXT OF ANY KIND** — no Roman numerals, no labels, no markers, no annotations. This is a pure visual.
6. **Left 30% MUST be nearly empty** — this is non-negotiable. Text will overlay this area.
7. **NO 3D rendering** — this is flat 2D illustration. No perspective, no shadows, no ambient occlusion.
8. **Pixel sizes and rendering instructions are internal** — do NOT render.
9. **Style must match topic figures** — if this looks like a different tool/style generated it, the image fails.

## Alt Text

Wide landscape flat illustration showing a ridgeplot-style MFCC spectrogram: 13–20 horizontal waveform bands stacked vertically with slight overlap, each representing a mel-frequency coefficient over time. Rendered as flat 2D editorial illustration with thin line outlines and selective flat color fills — teal for signal bands, coral for accent bands, navy for the fundamental, warm gray outlines for context. Small coral accent squares punctuate peak amplitudes. Visual density increases from left to right: the left is nearly empty cream with ghost lines, the middle shows bands emerging, and the right is densely layered with all bands visible and richly colored. The style matches the flat, constructivist aesthetic of the accompanying topic figure infographics — cream background, halftone grain, risograph print feel.
