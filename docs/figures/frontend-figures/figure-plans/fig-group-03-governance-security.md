# fig-group-03: Governance & Security (Group Overview)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-group-03 |
| **Title** | Governance & Security — Group Overview |
| **Audience** | General (landing page visitors) |
| **Complexity** | L1 (overview — bold visual, minimal text) |
| **Location** | Landing page, Key Concepts section — right of "Governance & Security" topic cards |
| **Priority** | P1 (High) |
| **Dimensions** | 600 x 1200px (1:2 narrow portrait ratio) |

## Purpose & Key Message

A narrow portrait sidebar figure summarizing the five concepts in the Governance & Security group: drift detection, provenance lineage, MCP permissions, voice cloning protection, and MLSecOps. Functions as a visual table of contents for Topics VIII–XII.

Communicates: "the system monitors for drift, records provenance, enforces permissions, protects voices, and runs on enterprise security."

## Covers Topics

- VIII: Drift Detection (diverging distributions)
- IX: Provenance & Attribution-by-Design (solid chain vs. broken chain)
- X: MCP Permission Infrastructure (consent matrix)
- XI: Voice Cloning Protection (waveform → shield)
- XII: MLSecOps & Trust Centers (security pyramid)

## Visual Concept (ASCII Layout)

```
┌──────────────┐
│              │
│ VIII  DRIFT  │
│              │
│  ──────      │
│       ╲──── │
│  ═══ alert  │
│              │
│ ─────────── │
│              │
│  IX  CHAIN   │
│              │
│  ●──●──●    │
│  solid chain │
│  ○ · · ? ·  │
│  broken      │
│              │
│ ─────────── │
│              │
│  X   CONSENT │
│              │
│  ■ ■ □      │
│  □ ■ ■      │
│  ■ □ ◧      │
│  matrix      │
│              │
│ ─────────── │
│              │
│  XI  VOICE   │
│              │
│  ∿∿∿ → 🛡   │
│  3 sec       │
│              │
│ ─────────── │
│              │
│  XII SECURE  │
│              │
│    ╱╲        │
│   ╱──╲       │
│  ╱────╲      │
│  pyramid     │
│              │
└──────────────┘
```

## Design Notes

- **Narrow portrait 1:2** — sidebar next to topic cards
- **Five stacked vignettes** (~20% each), compressed but readable
- **Vignette VIII (Drift)**: Two lines diverging — teal stable line going flat, orange drifting line pulling away. A coral alert threshold horizontal line. Simplest possible "something changed" visual.
- **Vignette IX (Provenance)**: Top row: solid teal chain of connected circles (attribution-by-design). Bottom row: broken orange dotted chain with gaps and question mark (post-hoc). Side by side contrast.
- **Vignette X (MCP Consent)**: Small 3×3 grid of squares — teal filled (allow), orange filled (deny), half-filled (conditional). The consent matrix as a tiny visual pattern.
- **Vignette XI (Voice Cloning)**: A small waveform shape on left, arrow pointing right to a shield/lock icon. "3s" label. Voice cloning threat → protection.
- **Vignette XII (MLSecOps)**: Simple layered pyramid/triangle — base in warm gray, middle teal, top navy. Three tiers of security.
- **Roman numerals VIII–XII** as small labels
- **Minimal text**: only numerals and maybe "3s" at voice cloning.

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Stable line | `data_primary` | Teal flat horizontal line (no drift) |
| Drifting line | `data_warning` | Orange line diverging upward |
| Alert threshold | `line_accent` | Coral horizontal dashed line |
| Solid chain | `data_primary` | Connected teal circles (provenance) |
| Broken chain | `data_warning` | Disconnected orange dots with gaps |
| Consent grid | `data_primary` + `data_warning` | 3×3 grid: teal allow, orange deny, amber conditional |
| Waveform | `data_primary` | Small teal audio waveform shape |
| Shield/lock | `data_accent` | Coral shield icon (protection) |
| Security pyramid | `data_primary` | Three-tier layered triangle |
| Section dividers | `line_subtle` | Thin warm gray lines between vignettes |
| Roman numerals | `label_editorial` | VIII, IX, X, XI, XII |
| Background | `background` | Cream (#f6f3e6) |

## Color Palette

| Element | Color |
|---------|-------|
| Background | #f6f3e6 (cream) |
| Stable/chain/allow/waveform | #2E7D7B (teal) |
| Drifting/broken/deny | #E76F51 (orange) |
| Alert/shield/threshold | #E84C4F (coral) |
| Conditional consent | #D4A03C (amber) |
| Pyramid base | #8B7E6A (warm gray) |
| Pyramid middle | #2E7D7B (teal) |
| Pyramid top | #1E3A5F (navy) |
| Numerals, dividers | #8B7E6A (warm gray) |

## Nano Banana Pro Prompts

### Style prompt
Flat 2D editorial illustration on warm cream background (#f6f3e6). Narrow portrait format 1:2 ratio. Constructivist design language. Flat fills, thin lines, no shadows, no gradients, no 3D. Risograph halftone grain. Colors: teal (#2E7D7B), orange (#E76F51), coral (#E84C4F), amber (#D4A03C), navy (#1E3A5F), warm gray (#8B7E6A). Five stacked compact vignettes as one unified composition. Very minimal text.

### Content prompt
Narrow portrait composition (600x1200px). Five stacked visual vignettes separated by thin warm gray dividers, each with a small Roman numeral label. VIGNETTE VIII (top ~20%): Two lines — a flat teal horizontal line (stable) and an orange line diverging away from it (drift). A coral dashed horizontal line as alert threshold. Simplest "divergence" visual. VIGNETTE IX (~20%): Two rows. Top: three teal circles connected by solid lines forming a chain (solid provenance). Bottom: three orange circles connected by dotted lines with gaps and a question mark (broken post-hoc chain). VIGNETTE X (~20%): A small 3×3 grid of squares. Some filled teal (allow), some filled orange (deny), one or two half-filled amber (conditional). A tiny consent matrix pattern. VIGNETTE XI (~20%): A small teal audio waveform shape on the left, an arrow pointing right, and a coral shield icon on the right. Small "3s" label. Voice cloning protection. VIGNETTE XII (bottom ~20%): A simple three-tier pyramid/triangle. Base layer warm gray, middle layer teal, top layer navy. Security layers. Generous whitespace within each vignette. Halftone grain. One unified composition flowing vertically.

### Negative prompt
--no 3D, shadows, gradients, photorealistic, dense text, formula, paragraph text, bar chart, pie chart, dark background, neon, wireframe, horizontal layout, separate bordered panels, photographs, faces, complex icons

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render.
2. **Semantic tags are internal** — do NOT render.
3. **Pixel sizes are internal** — do NOT render.
4. Only render: Roman numerals "VIII", "IX", "X", "XI", "XII", "3s", and "?" on broken chain. NO other text.
5. **Narrow portrait** — width is HALF the height. Non-negotiable.
6. **One composition** — five vignettes flow vertically as a single piece.
7. **Five vignettes, not three or four** — all five governance topics must appear.

## Alt Text

Narrow portrait overview of the Governance & Security concept group. Five stacked visual vignettes: (VIII) two lines diverging — teal stable and orange drifting — with a coral alert threshold; (IX) a solid teal provenance chain versus a broken orange dotted chain with gaps; (X) a 3×3 consent matrix grid with teal allow, orange deny, and amber conditional squares; (XI) a teal waveform with arrow pointing to a coral shield icon — voice cloning protection from 3 seconds of audio; (XII) a three-tier security pyramid in warm gray, teal, and navy.
