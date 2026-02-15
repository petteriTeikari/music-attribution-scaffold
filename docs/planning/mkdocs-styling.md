# MkDocs Styling Plan — Match Frontend Editorial Design

## Goal

Transform the MkDocs Material site from default indigo/deep-orange stock theme to match the frontend's editorial design system: warm cream surfaces, coral red accent, Instrument Serif display headings, Plus Jakarta Sans body, IBM Plex Mono code, noise grain overlay, accent lines/squares.

## Current State

- Stock Material theme with `primary: indigo`, `accent: deep-orange`
- Default Roboto/monospace fonts
- Minimal `extra.css` (coral accent var, 1440px grid, basic table/code tweaks)
- No template overrides (`overrides/` directory)
- No custom color schemes

## Target State

Match `frontend/src/app/globals.css` design tokens as closely as MkDocs Material allows:

| Element | Frontend | MkDocs Target |
|---------|----------|---------------|
| Surface (light) | `#f6f3e6` (warm cream) | Custom scheme `music-attribution` |
| Surface (dark) | `#1A1A2E` (deep blue) | Custom scheme `music-attribution-dark` |
| Primary | `#1E3A5F` (navy) | Header, sidebar, links |
| Accent | `#E84C4F` (coral red) | Hover, active, decorative |
| Display font | Instrument Serif | h1, h2 headings |
| Body font | Plus Jakarta Sans | `--md-text-font` |
| Code font | IBM Plex Mono | `--md-code-font` |
| Noise grain | SVG feTurbulence 3.5% | `body::before` overlay |
| Accent lines | 1px coral after h2 | `::after` pseudo-element |
| Accent squares | 28px coral before h1 | `::before` pseudo-element |
| Links | Underline with coral | `text-decoration` styling |
| Footer | Navy bg, coral accent | Custom scheme + CSS |
| Code blocks | Warm cream bg | `--md-code-bg-color` |
| Admonitions | Flat, no shadow, top border | CSS override |

## Implementation Steps

### Step 1: Update `mkdocs.yml` — Fonts & Custom Schemes

- Set `font: false` to disable auto Google Fonts loading
- Replace `primary: indigo` / `accent: deep-orange` with custom scheme names
- Add `custom_dir: overrides` for template overrides
- Add `navigation.footer` and `header.autohide` features
- Add copyright and `generator: false`

### Step 2: Rewrite `docs/site/stylesheets/extra.css`

Full custom CSS covering:
1. **Google Fonts import** — Instrument Serif, Plus Jakarta Sans, IBM Plex Mono
2. **Light color scheme** (`[data-md-color-scheme="music-attribution"]`) mapping all `--md-*` vars to frontend tokens
3. **Dark color scheme** (`[data-md-color-scheme="music-attribution-dark"]`)
4. **Font assignments** — `--md-text-font`, `--md-code-font`, `--font-display`
5. **Editorial typography** — h1 (Instrument Serif + accent square), h2 (Instrument Serif + accent line), body line-height
6. **Noise grain overlay** — `body::before` with SVG feTurbulence
7. **Editorial utilities** — `.editorial-caps`, `.editorial-display`, `.accent-line`, `.accent-square`
8. **Navigation sidebar** — background color, link styling, active state
9. **Header** — navy background, no shadow, coral bottom border
10. **Footer** — navy background, coral top border
11. **Links** — underline with coral accent, not pill buttons
12. **Admonitions** — flat style, top border, no shadow, no rounded corners
13. **Code blocks** — warm background, IBM Plex Mono
14. **Tables** — editorial styling, warm header background
15. **Reduced motion** — respect `prefers-reduced-motion`

### Step 3: Create `overrides/main.html`

- Announcement bar linking to SSRN paper
- `extrahead` block for Google Fonts preconnect
- Dismissible announcement

### Step 4: Create `overrides/partials/copyright.html`

- Custom copyright with paper reference and accent line

### Step 5: Update `mkdocs.yml` nav features

- Add `navigation.footer`, `navigation.instant`, `navigation.instant.prefetch`
- Add `announce.dismiss`, `header.autohide`

### Step 6: Verify

- `uv run mkdocs build --strict` passes
- Light and dark themes render correctly
- Fonts load properly
- Noise grain visible but subtle
- Accent elements (lines, squares) render on headings
- Admonitions styled correctly
- Code blocks use IBM Plex Mono with warm background

## Files Changed

| File | Action |
|------|--------|
| `mkdocs.yml` | Edit — fonts, schemes, custom_dir, features |
| `docs/site/stylesheets/extra.css` | Rewrite — full editorial CSS |
| `overrides/main.html` | Create — announcement bar, font preconnect |
| `overrides/partials/copyright.html` | Create — custom copyright |

## Anti-Patterns to Avoid

- Do NOT fork or modify the Material theme source
- Do NOT use SCSS (Material compiles it internally) — use plain CSS only
- Do NOT add CSS that conflicts with Material's `::before`/`::after` on `.md-content`
- Do NOT hardcode colors — use CSS custom properties throughout
- Do NOT override `base.html` — use `main.html` which extends it
