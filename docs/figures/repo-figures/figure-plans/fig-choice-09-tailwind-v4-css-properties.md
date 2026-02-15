# fig-choice-09: Why Tailwind v4 + CSS Custom Properties?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-09 |
| **Title** | Why Tailwind v4 + CSS Custom Properties? |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/planning/, .claude/rules/10-frontend-design-system.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains the styling strategy: CSS custom properties for all design tokens (colors, spacing, typography) combined with Tailwind v4 utility classes. This enables theming (light/dark mode via token swap) while keeping the utility-first development experience. Shows the critical Tailwind v4 pitfall: `text-[var(--anything)]` is treated as color, not font-size.

The key message is: "CSS custom properties own the design tokens, Tailwind v4 provides the utility classes -- zero hardcoded hex values in any .tsx file."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WHY TAILWIND V4 + CSS CUSTOM PROPERTIES?                      |
|  ■ Design Token Architecture                                   |
+---------------------------------------------------------------+
|                                                                |
|  TOKEN FLOW                                                    |
|  globals.css → CSS Custom Properties → Tailwind Utilities      |
|                                                                |
|  :root {                           .tsx files use:             |
|    --color-surface: #f6f3e6;       bg-[var(--color-surface)]   |
|    --color-accent: #E84C4F;        text-xl (NOT text-[var()])  |
|    --color-confidence-high: green; border-[var(--color-accent)]|
|  }                                                             |
|                                                                |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │ CSS Props +  │ │ CSS Modules  │ │ styled-      │          |
|  │ TAILWIND V4  │ │              │ │ components   │          |
|  │ ■ SELECTED   │ │              │ │              │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ Themeable    │ │ Scoped       │ │ CSS-in-JS    │          |
|  │ via token    │ │ by default   │ │ Runtime cost │          |
|  │ swap         │ │              │ │              │          |
|  │              │ │ No utility   │ │ No utility   │          |
|  │ Utility-     │ │ classes      │ │ classes      │          |
|  │ first DX     │ │              │ │              │          |
|  │              │ │ Verbose for  │ │ Bundle size  │          |
|  │ Zero runtime │ │ responsive   │ │ overhead     │          |
|  │ cost         │ │              │ │              │          |
|  │              │ │ Theme via    │ │ Theme via    │          |
|  │ Dark mode    │ │ imports      │ │ ThemeProvider │          |
|  │ via class    │ │              │ │              │          |
|  └──────────────┘ └──────────────┘ └──────────────┘          |
|                                                                |
|  ┌─────────────────────────────────────────────────────────┐   |
|  │  PITFALL: NEVER use text-[var(--anything)]              │   |
|  │  Tailwind v4 treats this as COLOR, not FONT-SIZE        │   |
|  │  CORRECT: text-xl, text-2xl (built-in scale)            │   |
|  │  WRONG: text-[var(--text-xl)] (generates color prop)    │   |
|  └─────────────────────────────────────────────────────────┘   |
|                                                                |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WHY TAILWIND V4 + CSS CUSTOM PROPERTIES?" with coral accent square |
| Token flow diagram | `data_flow` | globals.css -> CSS custom properties -> Tailwind utilities |
| Code examples | `data_mono` | :root declarations and .tsx usage patterns |
| CSS Props + Tailwind card | `selected_option` | Themeable, utility-first, zero runtime cost |
| CSS Modules card | `deferred_option` | Scoped, verbose for responsive |
| styled-components card | `deferred_option` | CSS-in-JS, runtime cost, bundle overhead |
| Pitfall warning box | `problem_statement` | Critical Tailwind v4 text-[var()] pitfall |

## Anti-Hallucination Rules

1. All colors are CSS custom properties in `frontend/src/app/globals.css` -- zero hardcoded hex in .tsx files.
2. The Tailwind v4 pitfall is real and documented in `.claude/memory/css-tailwind-v4-pitfalls.md`.
3. `text-[var(--anything)]` is treated as COLOR in Tailwind v4, not font-size.
4. The correct pattern is `text-xl`, `text-2xl` etc. (Tailwind built-in scale).
5. A lint test enforces this: `frontend/src/__tests__/css-token-lint.test.ts`.
6. Dark mode works via CSS custom property swap (`:root` vs `.dark` class).
7. The surface color `--color-surface: #f6f3e6` is the warm cream background.
8. The accent color `--color-accent: #E84C4F` is coral red.
9. Background must be warm cream (#f6f3e6).

## Alt Text

Design token architecture: CSS custom properties flowing through Tailwind v4 utilities for music attribution UI theming, showing zero-hardcoded-hex color tokens for confidence scoring tiers and music credits display, with critical text-var pitfall warning for the open-source attribution scaffold.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Design token architecture: CSS custom properties flowing through Tailwind v4 utilities for music attribution UI theming, showing zero-hardcoded-hex color tokens for confidence scoring tiers and music credits display, with critical text-var pitfall warning for the open-source attribution scaffold.](docs/figures/repo-figures/assets/fig-choice-09-tailwind-v4-css-properties.jpg)

*CSS custom properties define all design tokens for the music attribution scaffold's confidence tier colors, assurance levels, and data source indicators, consumed via Tailwind v4 utility classes with a documented pitfall: `text-[var(--anything)]` is treated as color, not font-size.*

### From this figure plan (relative)

![Design token architecture: CSS custom properties flowing through Tailwind v4 utilities for music attribution UI theming, showing zero-hardcoded-hex color tokens for confidence scoring tiers and music credits display, with critical text-var pitfall warning for the open-source attribution scaffold.](../assets/fig-choice-09-tailwind-v4-css-properties.jpg)
