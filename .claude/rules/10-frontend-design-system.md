# Frontend Design System Rules

## Color Token System

ALL colors are defined as CSS custom properties in `frontend/src/app/globals.css`.
Component code MUST reference tokens — **zero hardcoded hex values** in any `.tsx` file.

### Surface Colors
| Token | Light | Dark | Usage |
|-------|-------|------|-------|
| `--color-surface` | #F8F6F0 | #1A1A2E | Main background |
| `--color-surface-secondary` | #F0EDE5 | #16213E | Panel backgrounds |
| `--color-surface-tertiary` | #E8E4DA | #0F1A30 | Nested panels |
| `--color-surface-elevated` | #FFFFFF | #1F2A44 | Cards, modals |

### Brand Colors
| Token | Light | Dark | Meaning |
|-------|-------|------|---------|
| `--color-primary` | #1E3A5F | #7BA3D4 | Trust, authority |
| `--color-accent` | #D4A03C | #E8B94A | Music/creativity warmth |
| `--color-teal` | #2E7D7B | #4EC4C1 | Innovation, technology |

### Confidence Tier Colors (Critical)
| Token | Color | Threshold |
|-------|-------|-----------|
| `--color-confidence-high` | Green | ≥ 0.85 |
| `--color-confidence-medium` | Amber | 0.50–0.84 |
| `--color-confidence-low` | Red | < 0.50 |

### Assurance Level Colors (A0–A3)
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
| `--color-role-artist` | Gold — Artist mode |
| `--color-role-query` | Blue — Query mode |

## Typography

- **Font stack**: Inter → system-ui → sans-serif
- **Headings**: Bold (700), `--color-heading`
- **Body**: Regular (400), `--color-body`
- **Labels**: Regular (400), `--color-label`
- Scale defined in CSS vars: `--text-xs` through `--text-4xl`

## Spacing

4px base grid. All spacing via `--space-{n}` tokens.

## Component Patterns

1. **Warm editorial feel** — generous whitespace, not dense dashboards
2. **Typography-driven** — headings are hero elements, not decoration
3. **Cards over tables** — use card layouts for browse views
4. **Inline editing** — click-to-edit, not modal forms
5. **Subtle animations** — purposeful, never decorative

## Mood Board Reference

Design references in `docs/figures/visual-references/`:
- Postevand: Ultra-minimal Scandinavian whitespace
- Zajno/Brightmark: Bold display typography
- Fashion portfolio: Warm cream, thin accent lines
- Warp Records: Waveform-as-data-art
- Eden festival: Organic editorial, music heritage

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
