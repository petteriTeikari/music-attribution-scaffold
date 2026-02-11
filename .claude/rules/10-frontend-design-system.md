# Frontend Design System Rules

## Color Token System

ALL colors are defined as CSS custom properties in `frontend/src/app/globals.css`.
Component code MUST reference tokens — **zero hardcoded hex values** in any `.tsx` file.

### Surface Colors
| Token | Light | Dark | Usage |
|-------|-------|------|-------|
| `--color-surface` | #f6f3e6 | #1A1A2E | Main background (matched to Nano Banana Pro output) |
| `--color-surface-secondary` | #eeeadb | #16213E | Panel backgrounds |
| `--color-surface-tertiary` | #e6e1d0 | #0F1A30 | Nested panels |
| `--color-surface-elevated` | #FFFFFF | #1F2A44 | Cards, modals |
| `--color-sidebar` | #F8F6F0 | #16162C | Sidebar — old surface color, cooler contrast |

### Brand Colors
| Token | Light | Dark | Meaning |
|-------|-------|------|---------|
| `--color-primary` | #1E3A5F | #7BA3D4 | Trust, authority |
| `--color-accent` | #E84C4F | #F06B6E | **Coral red** — primary graphic accent (lines, squares, highlights) |
| `--color-accent-square` | #E84C4F | #F06B6E | IZUM-style floating accent squares |
| `--color-teal` | #2E7D7B | #4EC4C1 | Innovation, technology |

### Confidence Tier Colors (Critical)
| Token | Color | Threshold |
|-------|-------|-----------|
| `--color-confidence-high` | Green | >= 0.85 |
| `--color-confidence-medium` | Amber | 0.50-0.84 |
| `--color-confidence-low` | Red | < 0.50 |

### Assurance Level Colors (A0-A3)
| Token | Level | Meaning |
|-------|-------|---------|
| `--color-assurance-a3` | Green | Artist-verified |
| `--color-assurance-a2` | Blue | Multiple sources agree |
| `--color-assurance-a1` | Amber | Single source |
| `--color-assurance-a0` | Gray | No data |

### Data Source Colors
| Token | Source |
|-------|--------|
| `--color-source-musicbrainz` | MusicBrainz (purple) |
| `--color-source-discogs` | Discogs (dark gray) |
| `--color-source-acoustid` | AcoustID (teal) |
| `--color-source-artist` | Artist input (gold) |
| `--color-source-file` | File metadata (gray) |

### Role Accent Colors
| Token | Role |
|-------|------|
| `--color-role-artist` | Gold #D4A03C — Artist mode indicator only |
| `--color-role-query` | Blue #5B9BD5 — Query mode |

## Typography

| Role | Font | Usage |
|------|------|-------|
| **Display** | Instrument Serif (Regular + Italic) | Hero headings, section titles, 48-96px, often ALL-CAPS with letter-spacing |
| **Body/UI** | Plus Jakarta Sans (Variable 200-800) | Navigation, body text, labels, badges, 12-18px |
| **Mono** | IBM Plex Mono (400, 500) | Data tables, confidence scores, JSON, code |

CSS tokens: `--font-display`, `--font-sans`, `--font-mono`

Font sizes use Tailwind v4 built-in scale: `text-xs` through `text-7xl`.
**NEVER** use `text-[var(--text-xl)]` — this generates `color:` not `font-size:` in Tailwind v4.
See `.claude/memory/css-tailwind-v4-pitfalls.md` for details.

### Editorial Typography Classes

| Class | Effect |
|-------|--------|
| `.editorial-display` | Instrument Serif, font-weight 400, tight leading |
| `.editorial-display-italic` | Same but italic |
| `.editorial-caps` | Uppercase, 0.15em letter-spacing, Plus Jakarta Sans 500 |
| `.data-mono` | IBM Plex Mono, tabular-nums |

## Spacing

4px base grid. All spacing via `--space-{n}` tokens. Scale includes `--space-24` (96px) for large editorial sections.

## Layout Architecture

**Fixed left sidebar** (60px width, `--sidebar-width`), not horizontal top nav.

| Element | Desktop | Mobile |
|---------|---------|--------|
| Navigation | Fixed left sidebar, rotated text links | Top bar + hamburger overlay |
| Main content | `margin-left: var(--sidebar-width)` | Full width, `padding-top: 48px` |
| Footer | Sidebar-offset, rotated text + accent line | Full width |

### Sidebar Anatomy
- Top: "MA" logo link
- Middle: Rotated text nav links (vertical-rl, rotate 180deg)
- Bottom: Role toggle (A/Q), notifications, theme toggle, accent square

## Graphic Elements (Pure CSS)

1. **Accent squares**: `28x28px` (`.accent-square`) and `16x16px` (`.accent-square-sm`) solid coral blocks
2. **Accent lines**: 1px horizontal (`.accent-line`) and vertical (`.accent-line-v`) in coral
3. **Noise grain overlay**: SVG feTurbulence on `body::before` at opacity 0.035
4. **ALL-CAPS tracking**: `.editorial-caps` utility class

## Component Patterns

1. **Bold editorial feel** — asymmetric layouts, generous whitespace, not dense dashboards
2. **Typography-driven** — Instrument Serif headings as hero elements
3. **Horizontal rows over cards** — divider lines between items, not shadow-box cards
4. **Accent line dividers** — coral accent lines as section separators
5. **Underline tabs** — editorial underline tabs with accent color, not pill-style
6. **Text links** — underline with accent color decoration, not pill buttons
7. **Square markers** — accent squares as visual punctuation
8. **Stagger reveals** — `motion/react` scroll animations with `staggerChildren`

## Motion (motion/react)

- Staggered scroll reveals: `whileInView` with `staggerChildren: 0.12`
- Hero entrance: heading slides up with mask reveal
- Page transitions: opacity fade
- Respect `prefers-reduced-motion` throughout
- Simple easing only — **no bouncing, no elastic, no spring physics**

## Mood Board Reference

Design references in `docs/figures/visual-references/`:
- **IZUM (website-example1.jpg)**: Asymmetric grids, bold red accent squares, rotated vertical nav
- **Zajno/Brightmark (typography-example1.jpg)**: MASSIVE display type as hero, B&W + single red accent
- **Postevand (ui-example2.jpg)**: Ultra-minimal Scandinavian, ALL-CAPS labels, whitespace as design element
- **Warp Records (audio-example.jpg)**: Waveform data as abstract art, Roman numerals, pale pink
- **Constructivist (icons-example2.jpg)**: Red/blue/black geometric compositions
- **Bauhaus (icons-example3.jpg)**: Bold shapes, halftone textures, primary colors

## BANNED Aesthetics

The following are COMPLETELY BANNED in all frontend code:

- Corporate SaaS gradient backgrounds
- Sci-fi neon / glow effects
- Tech bro startup aesthetic (Lovable/v0 defaults)
- Stock photography
- Generic rounded-everything pill shapes
- Dark-mode-first design (dark mode exists but light is primary)
- Dense dashboard layouts (spacing must breathe)
- Pure black backgrounds (#000)
- Holographic / plasma effects
- Oversaturated colors
- `max-w-4xl mx-auto` centered containers (use full-width editorial grids)
- Numbered step circles (use accent squares + editorial caps)
- Shadow-sm box cards (use horizontal rows with divider lines)
- Symmetric 2-column grids (use asymmetric layouts)
- Inter font (replaced by Plus Jakarta Sans)
- `text-[var(--text-*)]` (Tailwind v4 treats as color, not font-size — use `text-xl` etc.)
- `--text-*` custom properties in `:root` (conflicts with Tailwind v4 built-in scale)
