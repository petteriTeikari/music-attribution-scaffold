# fig-frontend-02: Design System Token Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-02 |
| **Title** | Design System Token Architecture: CSS Custom Properties to Component Styles |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/frontend.md, docs/design-system.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows how the design token system enforces zero hardcoded hex values in component code. It traces the flow from CSS custom properties defined in globals.css, through Tailwind v4 utility classes and editorial utility classes, to component consumption via semantic CSS variables. The light/dark theme switch is shown as a single toggle point.

The key message is: "Every color in the UI flows from CSS custom properties in globals.css -- components reference semantic tokens like var(--color-confidence-high), never hex values. Theme switching changes only the :root variables."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  DESIGN TOKEN ARCHITECTURE                                             |
|  ■ Zero Hardcoded Hex                                                  |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. SOURCE OF TRUTH: globals.css                                       |
|  ─────────────────────────────                                         |
|                                                                        |
|  :root (light)           .dark (dark)                                  |
|  ┌────────────────────┐  ┌────────────────────┐                       |
|  │ --color-surface:   │  │ --color-surface:   │                       |
|  │   #f6f3e6          │  │   #1A1A2E          │                       |
|  │ --color-accent:    │  │ --color-accent:    │                       |
|  │   #E84C4F          │  │   #F06B6E          │                       |
|  │ --color-primary:   │  │ --color-primary:   │                       |
|  │   #1E3A5F          │  │   #7BA3D4          │                       |
|  │ ...60+ tokens      │  │ ...60+ tokens      │                       |
|  └────────┬───────────┘  └────────┬───────────┘                       |
|           │      ┌────────────────┘                                    |
|           └──────┤  Theme toggle                                       |
|                  ▼                                                      |
|  II. TOKEN CATEGORIES                                                  |
|  ────────────────────                                                  |
|  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐   |
|  │ Surface  │ │  Brand   │ │Confidence│ │Assurance │ │  Source   │   |
|  │ 4 tokens │ │ 6 tokens │ │ 3 tiers  │ │ A0-A3    │ │ 5 colors │   |
|  │ surface  │ │ primary  │ │ high     │ │ gray     │ │ purple   │   |
|  │ sec/tert │ │ accent   │ │ medium   │ │ amber    │ │ dark     │   |
|  │ elevated │ │ teal     │ │ low      │ │ blue     │ │ teal     │   |
|  │          │ │          │ │          │ │ green    │ │ gold     │   |
|  └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘   |
|                              │                                         |
|                              ▼                                         |
|  III. CONSUMPTION LAYERS                                               |
|  ───────────────────────                                               |
|  ┌─────────────────────┐  ┌─────────────────────┐                    |
|  │ Tailwind Utilities   │  │ Editorial Classes    │                    |
|  │ bg-surface           │  │ .editorial-display   │                    |
|  │ text-heading         │  │ .editorial-caps      │                    |
|  │ border-border        │  │ .data-mono           │                    |
|  └─────────┬───────────┘  └─────────┬───────────┘                    |
|            └──────────┬──────────────┘                                 |
|                       ▼                                                |
|  ┌─────────────────────────────────────────────┐                      |
|  │ COMPONENTS: style={{ color: var(...) }}      │                      |
|  │ Never: style={{ color: "#E84C4F" }}          │                      |
|  │ Enforced by: css-token-lint.test.ts          │                      |
|  └─────────────────────────────────────────────┘                      |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "DESIGN TOKEN ARCHITECTURE" in display font |
| Light theme block | `processing_stage` | :root with key CSS custom property examples |
| Dark theme block | `processing_stage` | .dark override with corresponding values |
| Theme toggle junction | `decision_point` | Where light/dark themes converge |
| Token category cards | `module_grid` | Five categories: Surface, Brand, Confidence, Assurance, Source |
| Tailwind utilities | `processing_stage` | Semantic class examples (bg-surface, text-heading) |
| Editorial classes | `processing_stage` | Custom utility classes (.editorial-display, .data-mono) |
| Component consumption | `final_score` | How components use var() references |
| Lint enforcement | `security_layer` | css-token-lint.test.ts enforces zero hex |
| Roman numerals I-III | `section_numeral` | Section identifiers |

## Anti-Hallucination Rules

1. All CSS custom properties are defined in `frontend/src/app/globals.css` -- there are 60+ tokens.
2. The light theme background is #f6f3e6 (warm cream), NOT white or yellow.
3. The dark theme background is #1A1A2E (dark navy), NOT pure black (#000).
4. The accent color is #E84C4F (coral red) in light mode, #F06B6E in dark mode.
5. The lint test at `frontend/src/__tests__/css-token-lint.test.ts` enforces zero hardcoded hex.
6. Confidence tiers: high (green #4A7C59), medium (amber #8B6914), low (red #C44536).
7. Assurance levels: A0 (gray #9E9E9E), A1 (amber #E09F3E), A2 (blue #5B9BD5), A3 (green #4A7C59).
8. NEVER use `text-[var(--anything)]` in Tailwind v4 -- this is a known pitfall documented in the project.

## Alt Text

Design system diagram showing CSS custom property token architecture for the music attribution scaffold: 60-plus color tokens in globals.css flow through Tailwind CSS v4 utilities and editorial classes to components with zero hardcoded hex values, enforced by automated lint tests for consistent confidence scoring and music metadata visualization.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Design system diagram showing CSS custom property token architecture for the music attribution scaffold: 60-plus color tokens in globals.css flow through Tailwind CSS v4 utilities and editorial classes to components with zero hardcoded hex values, enforced by automated lint tests for consistent confidence scoring and music metadata visualization.](docs/figures/repo-figures/assets/fig-frontend-02-design-token-architecture.jpg)

*Figure: Design token architecture enforcing zero hardcoded hex values across the music attribution UI, tracing the flow from CSS custom properties through Tailwind v4 utilities to component consumption with lint-test enforcement.*

### From this figure plan (relative)

![Design system diagram showing CSS custom property token architecture for the music attribution scaffold: 60-plus color tokens in globals.css flow through Tailwind CSS v4 utilities and editorial classes to components with zero hardcoded hex values, enforced by automated lint tests for consistent confidence scoring and music metadata visualization.](../assets/fig-frontend-02-design-token-architecture.jpg)
