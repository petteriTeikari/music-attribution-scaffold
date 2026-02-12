# fig-section-assurance-levels: A0–A3 Assurance Framework

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-section-assurance-levels |
| **Title** | A0–A3 Assurance Levels — Four-Tier Attribution Framework |
| **Audience** | General + Technical |
| **Complexity** | L2 (overview with detail) |
| **Location** | Landing page, Assurance Levels section (full-width below table) |
| **Priority** | P1 (High — core framework of the paper) |
| **Dimensions** | 1800 x 600px (3:1 wide landscape ratio) |

## Purpose & Key Message

A wide landscape infographic showing the A0–A3 assurance levels as a horizontal progression from left (no provenance) to right (full identity-verified chain). Each level maps to specific identifiers (ISRC, ISWC, ISNI) and shows what becomes possible at each tier. This is the core framework of the SSRN paper — the single most important diagram on the landing page.

Communicates: "attribution is not binary — it's a spectrum from self-declared to identity-verified, with each level unlocking new capabilities."

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  A0               A1                A2                 A3                    │
│  SELF-DECLARED    RECORDED          COMPOSED           IDENTITY-VERIFIED     │
│                                                                              │
│  ┌─────────┐     ┌─────────┐      ┌─────────┐        ┌─────────┐          │
│  │         │     │         │      │         │        │         │          │
│  │   ?     │ ──► │  ISRC   │ ──►  │  ISWC   │  ──►  │  ISNI   │          │
│  │         │     │         │      │         │        │         │          │
│  └─────────┘     └─────────┘      └─────────┘        └─────────┘          │
│                                                                              │
│  "I wrote this"  Recording code    Composition code   Creator identifier    │
│  No machine-     One recording     Links recordings   Links across          │
│  readable proof  identified        to compositions    all databases         │
│                                                                              │
│  No permissions  Opt-in/out per    Composition-level  Full provenance:      │
│  possible        recording         rights queryable   voice, style, splits  │
│                                                                              │
│  ■ grey          ■ amber           ■ blue             ■ green               │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Design Notes

- **Wide landscape 3:1** — spans full page width under the assurance levels table
- **Left-to-right progression**: A0 (empty/grey) → A1 (amber, ISRC) → A2 (blue, ISWC) → A3 (green, ISNI)
- **Four columns** with connecting arrows showing progression
- **Each column has**: level badge (A0/A1/A2/A3), type label, identifier code/icon, what it enables
- **Color coding matches CSS tokens**: `--color-assurance-a0` (gray), `--color-assurance-a1` (amber), `--color-assurance-a2` (blue), `--color-assurance-a3` (green)
- **Progressive visual density**: A0 column is sparse/empty, A3 column is rich/full
- **The arrow chain** is the key visual — each step adds a layer of verifiable identity
- **"Oracle Boundary"** subtle note near A3: even A3 cannot fully verify in adversarial settings

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| A0 badge | `assurance_a0` | Gray badge: "A0" |
| A1 badge | `assurance_a1` | Amber badge: "A1" |
| A2 badge | `assurance_a2` | Blue badge: "A2" |
| A3 badge | `assurance_a3` | Green badge: "A3" |
| Progression arrows | `line_flow` | Connecting arrows between levels |
| Type labels | `label_editorial` | "SELF-DECLARED", "RECORDED", "COMPOSED", "IDENTITY-VERIFIED" |
| Identifier codes | `typography_mono` | "ISRC", "ISWC", "ISNI" |
| Capability descriptions | `label_subtle` | What each level enables |
| Oracle boundary note | `data_warning` | Small orange note at A3 about adversarial limits |
| Background | `background` | Cream (#f6f3e6) |

## Color Palette

| Element | Color |
|---------|-------|
| Background | #f6f3e6 (cream) |
| A0 (self-declared) | #8B7E6A (warm gray) — no assurance |
| A1 (recorded) | #D4A03C (amber) — ISRC level |
| A2 (composed) | #5B9BD5 (blue) — ISWC level |
| A3 (identity-verified) | #2E7D7B (teal/green) — ISNI level |
| Arrows | #1E3A5F (navy) |
| Labels | #1E3A5F (navy) |
| Oracle boundary | #E76F51 (orange) |

## Nano Banana Pro Prompts

### Style prompt
Flat 2D editorial infographic on warm cream background (#f6f3e6). Wide landscape format 3:1 ratio. Constructivist design with clean geometric shapes. Flat fills, no shadows, no gradients, no 3D. Risograph halftone grain. Colors: warm gray (#8B7E6A), amber (#D4A03C), blue (#5B9BD5), teal-green (#2E7D7B), navy (#1E3A5F), orange (#E76F51). Horizontal progression left to right. Bold typography.

### Content prompt
Wide landscape composition (1800x600px). A horizontal four-stage progression from left to right showing attribution assurance levels. COLUMN 1 (leftmost, gray): Large "A0" badge in warm gray. Label: "SELF-DECLARED". Below: a question mark icon. Description: "I wrote this" — no machine-readable proof. Sparse, empty feeling. COLUMN 2 (amber): Large "A1" badge. Label: "RECORDED". Below: "ISRC" in monospace. Description: one recording identified, opt-in/out possible. COLUMN 3 (blue): Large "A2" badge. Label: "COMPOSED". Below: "ISWC" in monospace. Description: composition-level rights queryable, links recordings to compositions. COLUMN 4 (rightmost, teal-green): Large "A3" badge. Label: "IDENTITY-VERIFIED". Below: "ISNI" in monospace. Description: full provenance — voice, style, splits. Rich, detailed. Bold navy arrows connecting A0→A1→A2→A3 showing progression. Visual density increases left to right — A0 column is sparse, A3 column is richest. Small orange note near A3: "Oracle boundary: adversarial limits remain". Halftone grain overlay.

### Negative prompt
--no 3D, shadows, gradients, photorealistic, vertical layout, portrait orientation, dense paragraph text, scatter plot, pie chart, dark background, neon, wireframe, pyramid, stacked layers, complex icons, photographs

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render.
2. **Semantic tags are internal** — do NOT render.
3. **Pixel sizes are internal** — do NOT render.
4. Only render: "A0", "A1", "A2", "A3", "SELF-DECLARED", "RECORDED", "COMPOSED", "IDENTITY-VERIFIED", "ISRC", "ISWC", "ISNI", capability descriptions (1 line each), "Oracle boundary" note, "?" for A0.
5. **Wide landscape** — width is THREE TIMES the height. Non-negotiable.
6. **Left-to-right progression** — A0 on left, A3 on right. Arrows connect them.
7. **Progressive density** — A0 sparse, A3 rich.

## Alt Text

Wide landscape infographic showing the A0–A3 assurance level progression from left to right. A0 (gray, self-declared) has no machine-readable proof. A1 (amber, ISRC) identifies individual recordings with opt-in/out permissions. A2 (blue, ISWC) links recordings to compositions enabling composition-level rights queries. A3 (green, ISNI) provides full identity-verified provenance including voice, style, and split information. Arrows connect each level showing progressive capability. Visual density increases from sparse (A0) to rich (A3). A small orange note near A3 flags the Oracle boundary — adversarial verification limits remain even at the highest assurance level.
