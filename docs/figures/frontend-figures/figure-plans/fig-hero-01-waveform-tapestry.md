# fig-hero-01: Spectral Tapestry — Mixed-Media Audio Composition

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-hero-01 |
| **Title** | Spectral Tapestry — Layered Audio as Editorial Art |
| **Audience** | General (landing page visitors) |
| **Complexity** | L3 (hero — highest visual impact) |
| **Location** | Landing page hero section (full-width background behind text) |
| **Priority** | P0 (Critical — first visual impression, defines the entire site feel) |
| **Dimensions** | 2400 x 900px (8:3 landscape ratio) |

## Purpose & Key Message

A full-width hero image that layers **multiple scales and textures of audio visualization** into a single editorial composition — not a single chart repeated, but a collage of visual languages that all say "sound data." The composition should feel like a constructivist poster designed by someone who loves both Warp Records and El Lissitzky.

**No text. No labels. No annotations. Pure visual.**

Communicates: "This is serious science with soul. Sound data is beautiful."

## Why the Previous Versions Failed

| Version | Problem |
|---------|---------|
| Wireframe mesh + provenance nodes | Too engineering — looked like a matplotlib plot |
| 3D sculptural MFCC | Too photorealistic — clashed with flat topic figures |
| Uniform ridgeplot bands | Too uniform — read as a scientific chart, not a hero image |

The fix: **mix scales, mix textures, break regularity, create a crescendo.** A hero image needs dramatic visual energy that pulls the eye across the composition — not uniform repetition.

## Critical Layout Constraint: Left-to-Right Crescendo

**This image sits BEHIND hero text on the left side.** Visual density MUST increase from left to right:

- **Left 30%**: Near-empty. Cream (#f6f3e6) dominates. Only the faintest traces — ghost hairlines, a few scattered dots, maybe one very faint large waveform arc. Text overlay must be fully legible.
- **Middle 30%**: Elements emerge at different scales. Some thin waveform lines start. A few geometric shapes (circles, rectangles) appear. The composition begins to layer.
- **Right 40%**: Full visual crescendo. Dense, aggressive, layered. This is the payoff.

## Visual Concept: Mixed-Media Audio Collage

The key insight: **a hero image is not a chart — it's a poster.** It should mix multiple visual representations of sound at different scales, overlapping and interacting, creating a rich texture that rewards close inspection while reading as a bold graphic from a distance.

### Three Visual Layers (all flat 2D, all overlapping)

**LAYER 1 — MACRO: Large waveform silhouettes (background)**
Big, bold, filled waveform shapes spanning the full height. Like the silhouette of a mountain range but made from an audio waveform envelope. 2–3 of these, overlapping, in different colors (one teal, one coral, one navy). Semi-transparent where they overlap, creating color mixing areas. These are the dominant visual mass — seen from across the room.

**LAYER 2 — MESO: MFCC ridgeplot bands (midground)**
The stacked mel-frequency bands from the previous version, but now with **dramatic variation**: some bands are thick and bold (4–6px), others are hairline thin (1px). Spacing is irregular — clusters of dense bands, then gaps. Some bands curve slightly instead of running perfectly horizontal. These weave through and around the macro silhouettes. 8–15 bands, NOT uniformly spaced.

**LAYER 3 — MICRO: Fine details and accents (foreground)**
- **Coral accent squares** in varied sizes (8px, 16px, 28px) — scattered at peak points and intersections
- **Tiny circles** (like dot-matrix or halftone elements) clustered in dense areas
- **Hair-thin horizontal accent lines** in coral, running full width
- **Small geometric fragments** — rectangles, chevrons — like torn pieces of a larger chart
- **Vertical tick marks** in warm gray — suggesting a time axis without labeling it

### Compositional Dynamics (what makes it NOT a chart)

1. **Dramatic scale variation**: The large waveform silhouettes are 200–400px tall. The fine ridgeplot lines are 1–4px. The accent dots are 3–8px. This 100:1 scale range creates visual richness.
2. **Irregular spacing**: Nothing is evenly distributed. Dense clusters of lines alternate with breathing room. The eye moves unpredictably.
3. **Aggressive layering**: Elements overlap freely. A teal silhouette sits behind coral ridgeplot lines which sit behind navy accent squares. At least 3–4 layers deep in the right portion.
4. **Broken edges**: Waveform shapes don't have to be complete. Some can be cropped by the frame edge. Some ridgeplot lines can start mid-composition. This creates a sense of a larger world beyond the frame.
5. **Diagonal energy**: While most elements run roughly horizontal, a few elements can tilt slightly (5–15°) to break the horizontal monotony and create visual movement.
6. **Color clustering**: Not every area uses all colors. The top-right might be predominantly teal + coral. The bottom-right might be navy + warm gray. This creates "neighborhoods" of color.

### ASCII Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         │                        │    ■                  │
│  [TEXT OVERLAY ZONE]    │                        │  ╱╲╱╲   ■   ■       │
│                         │         ╱╲             │ ╱╲╱╲╱╲╱╲╱╲╱╲      │
│           ·             │ ╱~~~~~~~~~~~~~~╲       │╱  ██████  ╲╱╲      │
│                         │╱    ~~~~~~~~~~~~╲      │ ───────────────      │
│      ·        ·         │  ~~╱╲~~╱╲~~      ╲    │■╱╲╱╲  ╱╲╱╲  ╱╲    │
│                         │  ~~~~~~~~╱╲        ╲   │ ╱╲╱╲╱╲╱╲╱╲╱╲╱╲   │
│  ·                      │  ████████   ~~~~      │ ·····■·····          │
│                         │  ■   ~~╱╲~~╱╲~~      │ ╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲ │
│         ·               │                        │ dense, layered,      │
│                         │  Elements emerge at    │ mixed scales,        │
│  Ghost traces only.     │  different scales.     │ visual crescendo.    │
│                         │                        │                      │
└─────────────────────────────────────────────────────────────────────────┘
  ← NEAR-EMPTY                EMERGING                 DENSE CRESCENDO →
```

### What This Should Feel Like

- **From a distance (thumbnail)**: A bold asymmetric composition with warm colors building from left to right. Reads as "editorial poster" not "data chart."
- **At medium view (landing page)**: Layered audio shapes — clearly sound/data related. The large waveform silhouettes give mass and drama. The fine lines give texture and detail.
- **Up close**: Rich detail — individual ridgeplot bands with their own waveform patterns, tiny accent squares, dot clusters, hairline accent lines. Rewards zooming in.

### Reference: What Made the Original Wireframe Hero Work

The original wireframe hero (before this rewrite) had real visual energy because:
- Large and small elements coexisted (macro wireframe peaks + tiny provenance nodes)
- Colors overlapped (navy behind coral behind teal)
- The right side felt like an explosion of layered data
- It wasn't a single chart type — it mixed visual languages

**This new version should achieve the same energy level** but with flat 2D illustration instead of wireframe, and without the provenance network nodes.

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Large waveform silhouettes | `shape_macro` | 2–3 bold filled waveform envelopes, 200–400px tall, overlapping |
| MFCC ridgeplot bands | `line_meso` | 8–15 waveform bands at varying thickness (1–6px) and irregular spacing |
| Coral accent squares | `accent_square` | Varied sizes (8/16/28px), scattered at peaks and intersections |
| Dot clusters | `texture_dots` | Tiny circles clustered in dense areas, like halftone |
| Hairline accent lines | `line_accent` | 1–2 thin coral lines running full width |
| Geometric fragments | `shape_fragment` | Small rectangles, chevrons — editorial collage elements |
| Vertical tick marks | `line_subtle` | Warm gray ticks suggesting time axis |
| Left fade | `gradient_opacity` | All elements fade to near-invisible on the left 30% |
| Halftone grain | `texture_grain` | Faint noise overlay (3–5% opacity) |
| Background | `background` | Cream (#f6f3e6) visible in gaps between layers |

## Color Palette (identical to topic figures)

| Element | Color | Notes |
|---------|-------|-------|
| Background | #f6f3e6 (cream) | Same as all topic figures |
| Macro silhouette 1 | #2E7D7B (teal) | Largest waveform shape — dominant mass |
| Macro silhouette 2 | #E84C4F (coral) | Second waveform — accent mass |
| Macro silhouette 3 | #1E3A5F (navy) | Third waveform — depth |
| Ridgeplot lines | #1E3A5F (navy) + #8B7E6A (warm gray) | Mix of navy and gray lines |
| Ridgeplot fills | #2E7D7B (teal) + #E84C4F (coral) | Selective fill on key bands |
| Accent squares | #E84C4F (coral) | Signature graphic element |
| Dots + ticks | #8B7E6A (warm gray) | Fine texture elements |
| Fragments | #E76F51 (orange) | Occasional geometric fragments |

## Nano Banana Pro Prompts

### Style prompt
Flat 2D mixed-media audio visualization collage on warm cream background (#f6f3e6). Constructivist poster aesthetic meets Warp Records album art. Multiple overlapping layers: large bold waveform silhouette shapes (teal, coral, navy), thin ridgeplot-style waveform bands at varying thicknesses, small coral red accent squares, tiny dot clusters, hairline accent lines. Aggressive layering with 3-4 depth levels. Dramatic scale variation from 400px waveform shapes to 1px hairlines. Risograph print feel with halftone grain. NOT 3D. NOT uniform or evenly spaced. NOT a single chart type repeated. Flat color fills, no gradients, no shadows. Colors: teal (#2E7D7B), coral red (#E84C4F), navy (#1E3A5F), warm gray (#8B7E6A), orange (#E76F51). Ultra-wide landscape 8:3 ratio.

### Content prompt
Ultra-wide landscape composition (2400x900px). Mixed-media audio collage, NOT a single chart. THREE OVERLAPPING LAYERS: LAYER 1 (background): 2-3 large bold waveform envelope silhouettes spanning 200-400px in height, filled with flat teal (#2E7D7B), coral (#E84C4F), and navy (#1E3A5F). Semi-transparent where overlapping. These give the composition its visual mass. LAYER 2 (midground): 8-15 ridgeplot-style waveform bands with DRAMATICALLY VARYING thickness (some 6px bold, some 1px hairline) and IRREGULAR spacing (clustered in some areas, sparse in others). Some curve slightly. Selective flat fills on a few key bands. LAYER 3 (foreground): Small coral accent squares in varied sizes (8px, 16px, 28px) at peak points. Tiny dot clusters like halftone. Hairline coral horizontal accent lines. Small geometric rectangle fragments. Warm gray vertical tick marks. LEFT THIRD: near-empty cream with only ghost traces — a few faint dots, one barely-visible waveform arc at 5% opacity. MIDDLE THIRD: elements emerge at different scales, layering begins. RIGHT THIRD: full visual crescendo — dense, aggressive layering, all three layers visible and overlapping, rich color, 3-4 elements deep. The right side should feel like a visual explosion of layered sound data. No text. No labels. Halftone grain overlay.

### Negative prompt
--no 3D render, sculptural, ceramic, ambient occlusion, shadows, glossy, metallic, gradients, smooth shading, photorealistic, wireframe mesh, network graph, nodes, connecting lines, scatter plot, text, labels, annotations, font names, bar chart, pie chart, UI elements, screenshots, neon glow, dark background, pure black, symmetric, centered, uniform spacing, evenly distributed elements, faces, musical instruments, music notes, treble clef, stock photography, engineering plot, matplotlib, axes, legend, single chart type

## Anti-Hallucination Rules

These are INTERNAL instructions for the image generator. They must NEVER appear as visible text in the output:

1. **Font names are internal** — do NOT render any text whatsoever.
2. **Color names are internal** — "cream", "coral", "teal", "navy" are palette descriptions. Do NOT render them.
3. **Semantic tags are internal** — `shape_macro`, `line_meso`, etc. Do NOT render them.
4. **Technical terms are internal** — "MFCC", "spectrogram", "ridgeplot", "mel-frequency" are concept references. Do NOT render them.
5. **NO TEXT OF ANY KIND** — this is a pure visual. No labels, no annotations, no markers.
6. **Left 30% MUST be nearly empty** — text will overlay this area. Non-negotiable.
7. **NO 3D rendering** — flat 2D illustration only. No perspective, no shadows.
8. **NO uniform spacing** — if elements are evenly distributed, the image fails as a hero. Irregularity and clustering are essential.
9. **Pixel sizes and rendering instructions are internal** — do NOT render.
10. **Must match topic figure style** — flat fills, thin lines, coral squares, cream background, halftone grain.

## Alt Text

Wide landscape mixed-media audio collage in flat 2D editorial illustration style. Three overlapping visual layers build from left to right: large bold waveform envelope silhouettes in teal, coral, and navy provide visual mass; irregularly-spaced ridgeplot-style waveform bands at varying thicknesses (hairline to bold) weave through the midground; and small coral accent squares, dot clusters, and hairline accent lines add fine foreground detail. Visual density increases dramatically — the left is nearly empty cream, the middle shows elements emerging at different scales, and the right builds to an aggressive visual crescendo with 3–4 layers of overlapping sound data. The composition reads as a constructivist poster at a distance and reveals rich detail up close, matching the flat editorial style of accompanying topic infographics.
