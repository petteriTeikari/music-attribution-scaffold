# fig-frontend-04: Confidence Gauge Component

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-04 |
| **Title** | Confidence Gauge: Three-Tier SVG Arc with ARIA Meter Role |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 |
| **Location** | docs/architecture/frontend.md, docs/design-system.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure explains the ConfidenceGauge component -- the primary visual indicator for attribution confidence. It shows the three-tier color system (green/amber/red), the three size variants (sm/md/lg), the 270-degree SVG arc construction, and the ARIA accessibility attributes. The mount animation with prefers-reduced-motion respect is also noted.

The key message is: "The confidence gauge uses a 270-degree SVG arc with three semantic color tiers -- green (>=0.85), amber (0.50-0.84), red (<0.50) -- and exposes role='meter' with aria-valuenow for screen readers."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  CONFIDENCE GAUGE COMPONENT                                            |
|  ■ Three-Tier SVG Arc                                                  |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. THREE TIERS                                                        |
|  ──────────────                                                        |
|                                                                        |
|     ╭───╮           ╭───╮           ╭───╮                             |
|    ╱     ╲         ╱     ╲         ╱     ╲                            |
|   │  92   │       │  67   │       │  31   │                           |
|   │  HIGH │       │MEDIUM │       │  LOW  │                           |
|    ╲     ╱         ╲     ╱         ╲     ╱                            |
|     ╰───╯           ╰───╯           ╰───╯                             |
|                                                                        |
|   >= 0.85           0.50-0.84       < 0.50                            |
|   Green             Amber           Red                                |
|   "High Confidence" "Medium"        "Low Confidence"                   |
|                                                                        |
|  II. SIZE VARIANTS                                                     |
|  ─────────────────                                                     |
|                                                                        |
|   sm (48px)     md (80px)      lg (140px)                             |
|   stroke: 3     stroke: 4      stroke: 5                              |
|   Work rows     Default        Detail page hero                       |
|                                                                        |
|  III. ANATOMY                                                          |
|  ────────────                                                          |
|                                                                        |
|  ┌─────────────────────────────────────────────┐                      |
|  │  <div role="meter"                          │                      |
|  │       aria-valuenow={92}                    │                      |
|  │       aria-valuemin={0}                     │                      |
|  │       aria-valuemax={100}                   │                      |
|  │       aria-label="Confidence: 92% -- High"> │                      |
|  │                                              │                      |
|  │    <svg> 270° arc background track           │                      |
|  │           270° arc filled (score * arcLen)   │                      |
|  │                                              │                      |
|  │    Center: "92" (editorial-display font)     │                      |
|  │    Below:  "HIGH CONFIDENCE" (editorial-caps)│                      |
|  │  </div>                                      │                      |
|  └─────────────────────────────────────────────┘                      |
|                                                                        |
|  IV. ANIMATION                                                         |
|  ─────────────                                                         |
|  ■ Mount: 800ms ease-out cubic fill-up animation                       |
|  ■ prefers-reduced-motion: skip to final value instantly               |
|  ■ hasAnimated ref prevents re-animation on re-render                  |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "CONFIDENCE GAUGE COMPONENT" in display font |
| Three gauge examples | `confidence_high`, `confidence_medium`, `confidence_low` | Visual gauge at each tier |
| Threshold labels | `data_mono` | Score thresholds (>=0.85, 0.50-0.84, <0.50) |
| Tier names | `label_editorial` | "High Confidence", "Medium Confidence", "Low Confidence" |
| Size variants row | `module_grid` | sm (48px), md (80px), lg (140px) with usage context |
| Anatomy diagram | `processing_stage` | SVG structure with ARIA attributes |
| ARIA attributes | `security_layer` | role="meter", aria-valuenow, aria-valuemin, aria-valuemax, aria-label |
| Animation notes | `callout_box` | Mount animation behavior and reduced-motion respect |
| Roman numerals I-IV | `section_numeral` | Section identifiers |

## Anti-Hallucination Rules

1. Confidence tiers: HIGH >= 0.85 (green), MEDIUM 0.50-0.84 (amber), LOW < 0.50 (red).
2. The arc spans 270 degrees (3/4 circle), NOT a full circle or semicircle.
3. Three sizes: sm (48px, stroke 3), md (80px, stroke 4), lg (140px, stroke 5).
4. The ARIA role is "meter" (not "progressbar" or "slider").
5. Mount animation is 800ms ease-out cubic, NOT spring or elastic.
6. prefers-reduced-motion is respected by skipping directly to the final score value.
7. The center text uses the "editorial-display" CSS class (Instrument Serif font).
8. The label below uses the "editorial-caps" CSS class (uppercase Plus Jakarta Sans).
9. Colors come from CSS variables: var(--color-confidence-high), var(--color-confidence-medium), var(--color-confidence-low).

## Alt Text

UI component diagram of the ConfidenceGauge used in the music attribution scaffold: a 270-degree SVG arc with three transparent confidence scoring tiers -- green for high, amber for medium, red for low -- shown in three size variants with ARIA meter role accessibility attributes and motion-safe mount animation for music credits visualization.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![UI component diagram of the ConfidenceGauge used in the music attribution scaffold: a 270-degree SVG arc with three transparent confidence scoring tiers -- green for high, amber for medium, red for low -- shown in three size variants with ARIA meter role accessibility attributes and motion-safe mount animation for music credits visualization.](docs/figures/repo-figures/assets/fig-frontend-04-confidence-gauge.jpg)

*Figure: Anatomy of the ConfidenceGauge component, the primary visual indicator for music attribution confidence, illustrating tier thresholds (0.85/0.50), size variants, SVG arc construction, and WCAG 2.1 AA accessibility via role="meter".*

### From this figure plan (relative)

![UI component diagram of the ConfidenceGauge used in the music attribution scaffold: a 270-degree SVG arc with three transparent confidence scoring tiers -- green for high, amber for medium, red for low -- shown in three size variants with ARIA meter role accessibility attributes and motion-safe mount animation for music credits visualization.](../assets/fig-frontend-04-confidence-gauge.jpg)
