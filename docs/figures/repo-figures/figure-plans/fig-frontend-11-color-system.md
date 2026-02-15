# fig-frontend-11: Color System (Light/Dark)

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-11 |
| **Title** | Color System: Light and Dark Mode Side-by-Side with Token Mapping |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/design-system.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the complete color system in light and dark modes side by side. Each token category (surface, brand, confidence, assurance, source, role) is displayed with its light-mode value and dark-mode override. The warm cream (#f6f3e6) vs dark navy (#1A1A2E) base contrast is the anchoring visual.

The key message is: "The light theme uses warm cream (#f6f3e6) as its foundation -- not white -- creating an editorial, paper-like feel. Dark mode switches to deep navy (#1A1A2E) -- not pure black -- maintaining warmth across both modes."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  COLOR SYSTEM                                                          |
|  ■ Light / Dark Mode                                                   |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌────────────────────────────┐  ┌────────────────────────────┐       |
|  │  LIGHT MODE (:root)        │  │  DARK MODE (.dark)         │       |
|  │                            │  │                            │       |
|  │  SURFACE                   │  │  SURFACE                   │       |
|  │  ██ #f6f3e6 (warm cream)   │  │  ██ #1A1A2E (dark navy)    │       |
|  │  ██ #eeeadb (secondary)    │  │  ██ #16213E (secondary)    │       |
|  │  ██ #e6e1d0 (tertiary)     │  │  ██ #0F1A30 (tertiary)     │       |
|  │  ██ #FFFFFF (elevated)     │  │  ██ #1F2A44 (elevated)     │       |
|  │                            │  │                            │       |
|  │  BRAND                     │  │  BRAND                     │       |
|  │  ██ #1E3A5F (primary)      │  │  ██ #7BA3D4 (primary)      │       |
|  │  ██ #E84C4F (accent/coral) │  │  ██ #F06B6E (accent/coral) │       |
|  │  ██ #2E7D7B (teal)         │  │  ██ #4EC4C1 (teal)         │       |
|  │                            │  │                            │       |
|  │  CONFIDENCE TIERS          │  │  CONFIDENCE TIERS          │       |
|  │  ██ #4A7C59 (high/green)   │  │  (same semantic intent)    │       |
|  │  ██ #8B6914 (medium/amber) │  │                            │       |
|  │  ██ #C44536 (low/red)      │  │                            │       |
|  │                            │  │                            │       |
|  │  ASSURANCE LEVELS          │  │  ASSURANCE LEVELS          │       |
|  │  ██ #9E9E9E (A0/gray)      │  │  (same semantic intent)    │       |
|  │  ██ #E09F3E (A1/amber)     │  │                            │       |
|  │  ██ #5B9BD5 (A2/blue)      │  │                            │       |
|  │  ██ #4A7C59 (A3/green)     │  │                            │       |
|  │                            │  │                            │       |
|  │  DATA SOURCES              │  │  DATA SOURCES              │       |
|  │  ██ #BA478F (MusicBrainz)  │  │  (same semantic intent)    │       |
|  │  ██ #333333 (Discogs)      │  │                            │       |
|  │  ██ #2E7D7B (AcoustID)     │  │                            │       |
|  │  ██ #D4A03C (Artist)       │  │                            │       |
|  │  ██ #666666 (File)         │  │                            │       |
|  │                            │  │                            │       |
|  │  ROLE ACCENTS              │  │  ROLE ACCENTS              │       |
|  │  ██ #D4A03C (artist/gold)  │  │  (same semantic intent)    │       |
|  │  ██ #5B9BD5 (query/blue)   │  │                            │       |
|  └────────────────────────────┘  └────────────────────────────┘       |
|                                                                        |
|  THEME SWITCHING                                                       |
|  ───────────────                                                       |
|  ■ ThemeProvider in layout.tsx                                          |
|  ■ .dark class on <html> via inline <script> (prevents flash)          |
|  ■ themeAtom: "light" | "dark" | "system"                              |
|  ■ Light is primary; dark mode exists but is NOT dark-mode-first       |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "COLOR SYSTEM" in display font |
| Light mode panel | `processing_stage` | All token categories with hex values |
| Dark mode panel | `processing_stage` | Dark overrides with corresponding hex values |
| Surface swatches | `primary_background` | Cream vs navy base colors |
| Brand swatches | `processing_stage` | Primary, accent, teal in both modes |
| Confidence swatches | `confidence_high`, `confidence_medium`, `confidence_low` | Three-tier colors |
| Assurance swatches | `assurance_a0` through `assurance_a3` | Four-level colors |
| Source swatches | `source_musicbrainz`, `source_discogs`, etc. | Five source colors |
| Role swatches | `stakeholder_artist` / query | Gold and blue role accents |
| Theme switching notes | `callout_box` | How theme switching works |

## Anti-Hallucination Rules

1. Light mode background is #f6f3e6 (warm cream), NOT #FFFFFF or any gray.
2. Dark mode background is #1A1A2E (dark navy), NOT #000000 (pure black is BANNED).
3. The accent color is #E84C4F (coral red) in light, #F06B6E in dark.
4. Primary is #1E3A5F (dark blue) in light, #7BA3D4 (light blue) in dark.
5. Theme is set via .dark class on <html>, with an inline script in layout.tsx to prevent flash.
6. Light mode is primary; dark-mode-first design is explicitly BANNED in the design system rules.
7. Sidebar uses its own color: #F8F6F0 (light) -- separate from main surface.
8. All hex values shown here are from globals.css :root and .dark selectors.

## Alt Text

Design system diagram showing the complete light and dark mode color palettes for the open-source music attribution scaffold: warm cream and dark navy surface foundations, coral red brand accent, three-tier confidence scoring colors, A0-A3 assurance level colors, five music metadata source colors, and role accent tokens for artist and query modes.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Design system diagram showing the complete light and dark mode color palettes for the open-source music attribution scaffold: warm cream and dark navy surface foundations, coral red brand accent, three-tier confidence scoring colors, A0-A3 assurance level colors, five music metadata source colors, and role accent tokens for artist and query modes.](docs/figures/repo-figures/assets/fig-frontend-11-color-system.jpg)

*Figure: Side-by-side light and dark color systems with six token categories, anchored by warm cream (#f6f3e6) and dark navy (#1A1A2E) foundations that create an editorial, paper-like feel for music attribution workflows.*

### From this figure plan (relative)

![Design system diagram showing the complete light and dark mode color palettes for the open-source music attribution scaffold: warm cream and dark navy surface foundations, coral red brand accent, three-tier confidence scoring colors, A0-A3 assurance level colors, five music metadata source colors, and role accent tokens for artist and query modes.](../assets/fig-frontend-11-color-system.jpg)
