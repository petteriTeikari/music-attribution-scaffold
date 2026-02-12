# fig-hero-01: MFCC Landscape — Sculptural Audio Topography

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-hero-01 |
| **Title** | MFCC Landscape — Sound as Sculptural Terrain |
| **Audience** | General (landing page visitors) |
| **Complexity** | L3 (hero — highest visual impact) |
| **Location** | Landing page hero section (full-width background behind text) |
| **Priority** | P0 (Critical — first visual impression, defines the entire site feel) |
| **Dimensions** | 2400 x 900px (8:3 landscape ratio) |

## Purpose & Key Message

A stunning full-width hero image showing a **3D MFCC spectrogram rendered as a sculptural landscape** — as if sound had physical topography. The surface undulates with mel-frequency coefficient peaks and valleys, rendered with smooth gradients and soft depth rather than wireframe grids. Think the cover of Wallpaper* or Dezeen, not a matplotlib plot. The aesthetic is matte ceramic, Scandinavian minimalism, or architectural model photography.

**No text. No labels. No annotations. Pure visual.**

Communicates: "This is sound made physical. This is data made beautiful."

## Critical Layout Constraint: Left-to-Right Density Gradient

**This image sits BEHIND hero text on the left side.** The visual density MUST increase from left to right:

- **Left 30%**: Near-empty. The cream background (#f6f3e6) dominates. Only the faintest suggestion of the 3D surface beginning — like a flat plane starting to ripple. Very low opacity. Text overlay must be fully legible.
- **Middle 30%**: The surface begins to rise. Gentle undulations emerge. Color begins to appear — teal tones in the valleys, warm gray on the mid-slopes. The terrain gains subtle depth and shadow.
- **Right 40%**: Full sculptural intensity. Dramatic peaks and ridges. Rich color: teal valleys, coral ridgelines catching light, navy in the deep shadows. Soft ambient occlusion. The surface looks like it could be touched — matte, physical, real.

## Visual Concept: 3D Stylized MFCC Spectrogram

An MFCC (Mel-Frequency Cepstral Coefficient) spectrogram encodes audio as a matrix: time along one axis, mel-frequency bands along the other, energy as height. When rendered as a 3D surface, it becomes a landscape — ridges for formants, valleys for silence, peaks for transients.

**This is NOT**:
- A wireframe mesh (removed — too technical)
- A line chart or waveform
- A scatter plot with nodes
- A network graph

**This IS**:
- A smooth, continuous 3D surface — like terrain, like sand dunes, like ceramic
- Rendered with soft lighting and matte material — not glossy, not metallic
- Color-mapped by elevation: teal (#2E7D7B) in valleys → warm cream on mid-slopes → coral (#E84C4F) on ridgelines and peaks
- Viewed from a low oblique angle (15–25° elevation) to emphasize the terrain quality
- Subtle ambient occlusion and soft shadows for depth
- The underlying "data" nature is visible in the regularity of the ridges (mel bands create parallel undulations) but the rendering is artistic, not scientific

### ASCII Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         │                        │                      │
│  [TEXT OVERLAY ZONE]    │   Surface emerging     │  FULL SCULPTURAL     │
│                         │                        │                      │
│  Nearly flat plane.     │   ~~╱╲~~╱╲~~          │  ╱╲╱╲╱╲╱╲╱╲╱╲      │
│  Cream background       │  Gentle undulations    │ ╱  ╲╱╲  ╲╱╲  ╲     │
│  with faintest ripple.  │  Teal in valleys,      │╱    ╲  ╲  ╲   ╲    │
│                         │  warm gray slopes      │ Deep valleys, high   │
│  5-10% opacity max.     │                        │ peaks. Teal base,    │
│                         │  20-50% opacity        │ coral ridgelines,    │
│                         │                        │ navy shadows.        │
│                         │                        │ Matte, touchable.    │
│                         │                        │                      │
└─────────────────────────────────────────────────────────────────────────┘
  ← FLAT / EMPTY                                      SCULPTURAL / VIVID →
```

### Design Magazine References

The aesthetic should evoke:
- **Zaha Hadid Architects** parametric surfaces — smooth, flowing, computational geometry made physical
- **Olafur Eliasson** topographic installations — data as landscape, science as art
- **Junya Ishigami** architectural models — impossibly delicate terrain with soft natural light
- **Neri Oxman** material ecology — gradient color transitions that feel organic, not digital
- **Wallpaper* magazine** cover aesthetic — one hero object, vast negative space, matte finish, editorial restraint

### What Makes It MFCC (Not Generic Terrain)

The surface should have visible regularity that hints at its origin as audio data:
- **Parallel ridgelines** running roughly left-to-right (these are mel-frequency bands — each band is a horizontal strip of undulating surface)
- **Rhythmic peaks** along each ridge (these are temporal energy patterns — beats, transients, vocal onsets)
- **13–20 visible parallel ridges** in the right portion (MFCC typically uses 13–40 coefficients)
- The regularity should feel like dunes shaped by wind — natural-looking but with an underlying mathematical order
- Valleys between ridges are deeper on the right (more dynamic range where the data is rich)

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| 3D MFCC surface | `surface_primary` | Smooth continuous terrain with mel-band ridges and temporal peaks |
| Valley color | `color_teal` | Teal (#2E7D7B) in the lowest elevations — like water in a topographic map |
| Slope color | `color_cream` | Warm cream/off-white on mid-elevation slopes |
| Ridgeline color | `color_coral` | Coral (#E84C4F) along the highest ridgelines and peaks — like sunlit mountaintops |
| Shadow color | `color_navy` | Navy (#1E3A5F) in deep shadow areas between ridges |
| Ambient occlusion | `lighting_soft` | Soft shadows in concavities for depth — NOT harsh directional light |
| Left fade | `gradient_opacity` | Surface fades to near-invisible on the left 30% |
| Subtle grain | `texture_grain` | Very faint noise/grain overlay (3-5% opacity) for matte print feel |

## Color Palette (matching topic figures)

| Element | Color | Opacity Range |
|---------|-------|---------------|
| Background | #f6f3e6 (cream) | 100% everywhere |
| Valley / low elevation | #2E7D7B (teal) | 0% (left) → 70% (right) |
| Mid-slope | #f6f3e6 → #eeeadb (cream gradient) | Continuous |
| Ridgeline / peak | #E84C4F (coral) | 0% (left) → 90% (right) |
| Deep shadow | #1E3A5F (navy) | 0% (left) → 50% (right) |
| Warm shadow | #8B7E6A (warm gray) | 5% (left) → 30% (right) |

## Nano Banana Pro Prompts

### Style prompt
3D sculptural MFCC spectrogram rendered as smooth terrain landscape on warm cream background (#f6f3e6). Matte ceramic finish, soft ambient occlusion lighting, NOT wireframe, NOT glossy. Zaha Hadid parametric surface aesthetic. Neri Oxman organic color gradient. Wallpaper magazine cover quality. Low oblique camera angle (15-25 degrees elevation). Color-mapped by elevation: teal (#2E7D7B) in valleys, warm cream on slopes, coral red (#E84C4F) on ridgelines and peaks, navy (#1E3A5F) in deep shadows. Subtle halftone grain texture. Matte risograph print feel. Scandinavian minimalism. Ultra-wide landscape 8:3 ratio.

### Content prompt
Ultra-wide landscape composition (2400x900). A 3D surface representing an MFCC spectrogram rendered as sculptural terrain — NOT wireframe mesh, NOT engineering visualization. Smooth continuous surface with 13-20 parallel ridges running left to right (mel-frequency bands). Rhythmic peaks along each ridge from audio energy patterns. LEFT THIRD: nearly flat, the terrain barely emerges from the cream background at 5-10% opacity — just the faintest ripple. MIDDLE THIRD: gentle undulations rise, teal appears in forming valleys, warm gray shadows begin. RIGHT THIRD: dramatic sculptural peaks and deep valleys, rich teal in low areas, coral catching light on ridgelines, navy in deep shadow crevices. The surface looks like it could be a physical ceramic model photographed with soft studio lighting. Matte finish. No wireframe grid. No dots. No nodes. No connecting lines. No text. No labels. Pure sculptural surface.

### Negative prompt
--no wireframe, mesh grid, network graph, nodes, connecting lines, dots, scatter plot, text, labels, annotations, font names, bar chart, pie chart, UI elements, screenshots, neon glow, glossy finish, metallic, dark background, pure black, symmetric, centered, photorealistic faces, musical instruments, music notes, treble clef, stock photography, engineering plot, matplotlib, axes, tick marks, legend

## Anti-Hallucination Rules

These are INTERNAL instructions for the image generator. They must NEVER appear as visible text in the output:

1. **Font names are internal** — do NOT render any text whatsoever.
2. **Color names are internal** — "cream", "coral", "teal", "navy" are palette descriptions. Do NOT render them.
3. **Semantic tags are internal** — `surface_primary`, `color_teal`, etc. Do NOT render them.
4. **Technical terms are internal** — "MFCC", "spectrogram", "mel-frequency" are concept references. Do NOT render them.
5. **NO TEXT OF ANY KIND** — no Roman numerals, no labels, no markers, no annotations. This is a pure visual.
6. **Left 30% MUST be nearly empty** — this is non-negotiable. Text will overlay this area.
7. **NO wireframe, NO mesh, NO grid lines** — the surface must be smooth and continuous.
8. **Pixel sizes and rendering instructions are internal** — do NOT render.

## Alt Text

Wide landscape 3D surface resembling sculptural terrain, derived from an MFCC audio spectrogram. The smooth, matte surface features parallel ridges representing mel-frequency bands with rhythmic peaks from audio energy patterns. Visual density increases dramatically from left to right: the left portion is nearly empty cream, the middle shows gentle undulations with teal emerging in valleys, and the right builds to dramatic sculptural peaks with teal valleys, coral-highlighted ridgelines, and navy shadows in deep crevices. The rendering has a matte ceramic quality with soft ambient lighting, evoking architectural model photography rather than scientific visualization.
