# fig-frontend-13: Accessibility Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-13 |
| **Title** | Accessibility Architecture: Two Testing Layers for WCAG 2.1 AA Compliance |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/frontend.md, docs/testing.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the two-layer accessibility testing strategy and the key ARIA patterns used in the frontend. Layer 1 (component-level) uses Vitest + vitest-axe for fast per-component WCAG checks. Layer 2 (browser-level) uses Playwright + @axe-core/playwright for real-rendering E2E checks. The figure also catalogs the specific ARIA patterns implemented: role="meter" on confidence gauges, aria-current="page" on navigation, aria-label on all interactive elements, and prefers-reduced-motion respect.

The key message is: "Accessibility is tested at two layers -- fast component-level axe checks run on every test, while browser-level Playwright axe checks validate real rendering -- targeting WCAG 2.1 AA compliance."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  ACCESSIBILITY ARCHITECTURE                                            |
|  ■ WCAG 2.1 AA Target                                                 |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. TWO TESTING LAYERS                                                 |
|  ─────────────────────                                                 |
|                                                                        |
|  Layer 1: Component (Fast)         Layer 2: Browser (Real)             |
|  ┌──────────────────────────┐     ┌──────────────────────────┐        |
|  │  Vitest + vitest-axe      │     │  Playwright + axe-core   │        |
|  │                           │     │                          │        |
|  │  ■ Runs every test suite  │     │  ■ E2E test suite        │        |
|  │  ■ JSDOM rendering        │     │  ■ Real browser engine   │        |
|  │  ■ Per-component checks   │     │  ■ Full page rendering   │        |
|  │  ■ Fast feedback (<1s)    │     │  ■ Cross-browser         │        |
|  │                           │     │                          │        |
|  │  Catches:                 │     │  Catches:                │        |
|  │  ■ Missing ARIA labels    │     │  ■ Color contrast fails  │        |
|  │  ■ Invalid role usage     │     │  ■ Focus order issues    │        |
|  │  ■ Form accessibility     │     │  ■ Keyboard navigation   │        |
|  │  ■ Heading hierarchy      │     │  ■ Dynamic state a11y    │        |
|  └──────────────────────────┘     └──────────────────────────┘        |
|                                                                        |
|  II. ARIA PATTERNS IN USE                                              |
|  ────────────────────────                                              |
|                                                                        |
|  ┌──────────────────────────────────────────────────────────────────┐ |
|  │ Component            ARIA Pattern                                │ |
|  │ ────────────────────────────────────────────────────────────     │ |
|  │ ConfidenceGauge      role="meter"                                │ |
|  │                      aria-valuenow, aria-valuemin, aria-valuemax │ |
|  │                      aria-label="Confidence: 92% -- High"       │ |
|  │ ────────────────────────────────────────────────────────────     │ |
|  │ Navigation           aria-label="Main navigation"               │ |
|  │                      aria-current="page" on active link          │ |
|  │ ────────────────────────────────────────────────────────────     │ |
|  │ Mobile menu          aria-expanded on hamburger                  │ |
|  │                      aria-label="Open menu" / "Close menu"      │ |
|  │ ────────────────────────────────────────────────────────────     │ |
|  │ Agent toggle         aria-label="Open/Close agent chat"         │ |
|  │ ────────────────────────────────────────────────────────────     │ |
|  │ Decorative elements  aria-hidden="true" on accent squares       │ |
|  │                      aria-hidden="true" on SVG icons            │ |
|  └──────────────────────────────────────────────────────────────────┘ |
|                                                                        |
|  III. KEY STANDARDS                                                    |
|  ──────────────────                                                    |
|  ■ Color contrast: 4.5:1 (normal text), 3:1 (large text)              |
|  ■ Touch targets: 44x44px minimum on mobile                           |
|  ■ Focus indicators: visible, high-contrast focus rings                |
|  ■ prefers-reduced-motion: animations skip to final state              |
|  ■ Keyboard: all interactive elements reachable via Tab                |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "ACCESSIBILITY ARCHITECTURE" in display font |
| Layer 1 panel | `processing_stage` | Vitest + vitest-axe: fast, component-level, JSDOM |
| Layer 2 panel | `processing_stage` | Playwright + axe-core: real browser, E2E |
| ARIA patterns table | `module_grid` | Component-to-ARIA-pattern mapping |
| ConfidenceGauge ARIA | `data_mono` | role="meter" with aria-valuenow/min/max |
| Navigation ARIA | `data_mono` | aria-label, aria-current="page" |
| Mobile menu ARIA | `data_mono` | aria-expanded on hamburger |
| Decorative elements | `data_mono` | aria-hidden="true" on accent squares and SVGs |
| Standards list | `feature_list` | Color contrast, touch targets, focus, motion, keyboard |
| Roman numerals I-III | `section_numeral` | Section identifiers |

## Anti-Hallucination Rules

1. Layer 1 testing uses Vitest + vitest-axe (NOT Jest).
2. Layer 2 testing uses Playwright + @axe-core/playwright (NOT Cypress).
3. The ConfidenceGauge uses role="meter" (NOT role="progressbar" or role="slider").
4. aria-valuenow is the percentage (0-100), not the raw score (0.0-1.0).
5. prefers-reduced-motion is explicitly checked in the ConfidenceGauge mount animation.
6. Accent squares use aria-hidden="true" because they are decorative.
7. The target standard is WCAG 2.1 AA (not AAA, not WCAG 2.0).
8. Focus indicators, keyboard navigation, and touch targets (44x44px) are documented requirements.
9. The frontend has 265 Vitest tests passing (including accessibility checks).

## Alt Text

Two-layer accessibility architecture: Vitest plus vitest-axe for component checks, Playwright plus axe-core for browser checks, with ARIA pattern catalog.
