# fig-hero-01: Waveform Tapestry — Spectrogram Meets Provenance

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-hero-01 |
| **Title** | Waveform Tapestry — Where Sound Data Meets Attribution |
| **Audience** | General (landing page visitors) |
| **Complexity** | L3 (hero — highest visual impact) |
| **Location** | Landing page hero section (full-width background behind text) |
| **Priority** | P0 (Critical — first visual impression, defines the entire site feel) |
| **Dimensions** | 2400 x 900px (8:3 landscape ratio) |

## Purpose & Key Message

A stunning full-width hero image that communicates the core concept: **stylized audio waveforms meeting data attribution networks**. The image blends three visual languages — vintage Phonodeik-style oscilloscope waveforms, old-school wireframe 3D spectrograms, and constructivist provenance flow lines — into a single mixed-media composition.

Communicates: "Music data is beautiful. Attribution is an art form. This is serious science with soul."

## Critical Layout Constraint: Left-to-Right Opacity Gradient

**This image sits BEHIND hero text on the left side.** The visual density MUST increase from left to right:

- **Left 30%**: Near-empty. Faint hints only — ghostly wireframe grid lines, sparse dots, very low opacity. The cream background (#f6f3e6) must dominate so overlaid text is fully legible.
- **Middle 30%**: Transitional. Waveform shapes begin to emerge. Thin provenance connection lines appear. Medium opacity — the transition zone.
- **Right 40%**: Full intensity. Dense, vivid, stunning. 3D wireframe spectrogram peaks, rich Phonodeik-style waveform bands, coral red accent lines, constructivist flow nodes. This is the visual payoff.

## Visual Concept (ASCII Layout)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         │                        │                      │
│  [TEXT OVERLAY ZONE]    │   Waveforms emerging   │  FULL INTENSITY      │
│                         │                        │                      │
│  Nearly empty.          │   ···═══~~~═══···     │  ╔══╗  ┌──┐          │
│  Ghost wireframe grid   │   Thin flow lines     │  ║3D║══╡••╞══●──●   │
│  at 5-10% opacity.      │   connecting nodes     │  ║SP║  └──┘  │  │   │
│  Scattered dots.        │   Vintage waveform     │  ╚══╝  ~~~~  ●──●   │
│                         │   oscillations          │  Phonodeik bands    │
│  Cream background       │                        │  Coral accent lines │
│  must dominate.         │                        │  Dense, vivid       │
│                         │                        │                      │
└─────────────────────────────────────────────────────────────────────────┘
  ← LOW CONTRAST                                      HIGH CONTRAST →
```

## Visual References & Synthesis

### Source 1: Old-school wireframe 3D spectrogram (Image #13)
- Isometric wireframe mesh surface with peaks and valleys
- Layered stacked planes with dot-matrix texture beneath
- Monochrome warm tone on cream
- **Use**: The wireframe grid as ghostly background structure (left side fading in), building to visible 3D peaks (right side)

### Source 2: Vintage Phonodeik waveforms (Image #14)
- Oscilloscope-captured sound traces on dark strips
- Dense, organic waveform patterns — voice, orchestra, bell
- Scientific/archival quality — hand-labeled, precise time markers
- **Use**: Horizontal waveform bands running across the composition as the primary foreground motif. On the right side these are vivid and detailed; on the left they dissolve into faint traces.

### Source 3: Constructivist provenance flow (existing fig-feature-02)
- Connected nodes with thin lines representing data lineage
- Coral red squares as process markers
- **Use**: Provenance connection lines threading through and between the waveform layers, suggesting that the audio data is being tracked, attributed, scored. Small coral squares as attribution nodes.

### Synthesis / "Latent Space Interpolation"

The three visual languages should feel like they **bleed into each other**, not like separate layers pasted together:

- The wireframe grid lines of the spectrogram morph into the connection lines of the provenance flow
- The 3D spectrogram peaks are made of the same material as the Phonodeik waveform oscillations
- Dots from the wireframe dot-matrix become attribution nodes
- The vintage waveform bands slice horizontally through the 3D wireframe space
- Color transitions: faint warm gray (left) → navy and warm gray (middle) → coral red, navy, teal accents (right)

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Wireframe grid | `structure_grid` | Isometric wireframe mesh, ghostly on left, visible on right |
| 3D spectrogram peaks | `data_spectrogram` | Wireframe surface with audio-frequency peaks, right half |
| Phonodeik waveform bands | `data_waveform` | 2-3 horizontal bands of vintage oscilloscope-style waveforms |
| Provenance flow lines | `line_provenance` | Thin connecting lines between attribution nodes |
| Attribution nodes | `node_attribution` | Small coral red squares at connection points |
| Dot-matrix texture | `texture_dots` | Scattered dots beneath wireframe layers |
| Coral accent lines | `line_accent` | 1-2 thin horizontal coral lines running full width |
| Roman numerals | `label_editorial` | Optional: I-VIII as faint markers along bottom edge (tracks) |

## Color Palette (for this figure)

| Element | Color | Opacity Range |
|---------|-------|---------------|
| Background | #f6f3e6 (cream) | 100% everywhere |
| Wireframe grid | #8B7E6A (warm gray) | 5% (left) → 40% (right) |
| Spectrogram peaks | #1E3A5F (navy) | 0% (left) → 80% (right) |
| Waveform bands | #1E3A5F (navy) + #8B7E6A (warm gray) | 8% (left) → 90% (right) |
| Provenance lines | #2E7D7B (teal) | 0% (left) → 60% (right) |
| Attribution nodes | #E84C4F (coral red) | 0% (left) → 100% (right) |
| Accent lines | #E84C4F (coral red) | 15% (left) → 80% (right) |

## Nano Banana Pro Prompts

### Style prompt
Old-school wireframe 3D spectrogram meets vintage Phonodeik oscilloscope waveforms meets constructivist data flow diagram. Mixed media composition on warm cream background (#f6f3e6). Warp Records aesthetic meets scientific data visualization. Halftone grain texture. Isometric wireframe mesh with peaks. Dense vintage audio waveform oscillation bands. Thin connecting lines between small red square nodes. Matte finish, editorial art direction. Duotone navy (#1E3A5F) and coral red (#E84C4F) with warm gray. NOT digital, NOT glossy — feels like a risograph print of analog instruments. Ultra-wide landscape composition 8:3 ratio.

### Content prompt
Ultra-wide landscape composition (2400x900). Left-to-right density gradient: LEFT THIRD is nearly empty cream with only the faintest ghost of a wireframe grid at 5% opacity and scattered dots. MIDDLE THIRD has vintage audio waveforms beginning to emerge as horizontal bands, thin provenance lines connecting sparse nodes. RIGHT THIRD is the visual climax: vivid 3D wireframe spectrogram peaks rising from an isometric grid, dense Phonodeik-style oscilloscope waveform bands in navy and warm gray, coral red squares marking attribution nodes connected by teal lines, thin coral horizontal accent lines threading through. The three visual languages (wireframe spectrogram, vintage waveform, provenance flow) should morph into each other — grid lines becoming flow lines, spectrogram peaks made of waveform oscillations, dots becoming nodes. Roman numerals I-VIII as very faint markers along the bottom right.

### Negative prompt
--no text labels, font names, generic bar chart, symmetric layout, centered composition, gradient fills, neon glow, dark background, photorealistic, 3D render, glossy finish, stock photography, music notes, treble clef, musical instruments, faces, screenshots, UI elements, pure black, uniform density across width

## Anti-Hallucination Rules

These are INTERNAL instructions for the image generator. They must NEVER appear as visible text in the output:

1. **Font names are internal** — "Instrument Serif", "Plus Jakarta Sans", "IBM Plex Mono" are CSS references. Do NOT render them.
2. **Color names are internal** — "cream", "coral red", "navy" are palette descriptions. Do NOT render them as labels.
3. **Semantic tags are internal** — `data_spectrogram`, `line_provenance`, etc. Do NOT render them.
4. **Technical terms are internal** — "Phonodeik", "provenance", "attribution" are concept references. Do NOT render them.
5. The only text that MAY appear: Roman numerals I-VIII as very small, faint markers. All other text is BANNED.
6. **Left 30% MUST be nearly empty** — this is non-negotiable. Text will overlay this area. If the left side has dense visual elements, the image fails its purpose.

## Alt Text

Wide landscape mixed-media composition blending three visual languages: a ghostly wireframe 3D spectrogram grid, vintage oscilloscope-style audio waveform bands, and constructivist data flow connections with coral red nodes. Visual density increases dramatically from left to right — the left side is nearly empty cream, while the right side builds to a vivid climax of intersecting waveforms, wireframe peaks, and attribution flow lines in navy, warm gray, and coral red.
