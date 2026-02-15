# fig-frontend-07: Work Detail Page Layout

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-07 |
| **Title** | Work Detail Page: Per-Field Confidence, Source Provenance, and Citation Panel |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/frontend.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the /works/[workId] detail page layout. The hero section features a large confidence gauge alongside the work title, artist, assurance badge, and conformal set statistics. Below, three sections separated by accent lines show the credit list (per-credit confidence and sources), the provenance panel (Perplexity-style source cards), and the provenance timeline.

The key message is: "The work detail page surfaces per-field confidence, source provenance, and conformal prediction statistics -- making the attribution scaffold's transparency philosophy visible at every level of detail."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  WORK DETAIL PAGE LAYOUT                                               |
|  ■ /works/[workId]                                                     |
+-----------------------------------------------------------------------+
|                                                                        |
|  Breadcrumb: Works / Hide and Seek                                     |
|                                                                        |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  HERO SECTION                                                     │  |
|  │  ┌─────────┐                                                     │  |
|  │  │  ╭───╮  │  HIDE AND SEEK                                     │  |
|  │  │  │ 92│  │  Imogen Heap                                       │  |
|  │  │  │   │  │                                                     │  |
|  │  │  ╰───╯  │  A3 -- Artist Verified   92% -- High Confidence    │  |
|  │  │  HIGH   │  Source agreement: 95%                              │  |
|  │  └─────────┘                                                     │  |
|  │               ┌ Needs Review ──────────────────────────────┐     │  |
|  │               │ Priority: 15% (only if needs_review=true)  │     │  |
|  │               └────────────────────────────────────────────┘     │  |
|  │                                                                   │  |
|  │  Conformal: coverage 95% at 90% level | cal error: 0.012 | v3   │  |
|  └──────────────────────────────────────────────────────────────────┘  |
|                                                                        |
|  ═══════════════════════ (accent line) ═══════════════════════════     |
|                                                                        |
|  CREDITS                                                               |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  CreditList component                                             │  |
|  │  ■ Per-credit: entity name, role, confidence, source tags         │  |
|  │  ■ Source tags colored by source (MusicBrainz purple, etc.)       │  |
|  └──────────────────────────────────────────────────────────────────┘  |
|                                                                        |
|  ═══════════════════════ (accent line) ═══════════════════════════     |
|                                                                        |
|  PROVENANCE PANEL (Perplexity-style source cards)                      |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  ProvenancePanel component                                        │  |
|  │  ■ Inline citation references [1] [2] [3]                        │  |
|  │  ■ Source cards with origin, timestamp, event type                │  |
|  └──────────────────────────────────────────────────────────────────┘  |
|                                                                        |
|  ═══════════════════════ (accent line) ═══════════════════════════     |
|                                                                        |
|  PROVENANCE TIMELINE                                                   |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  ProvenanceTimeline component                                     │  |
|  │  ■ Chronological event chain with source color indicators         │  |
|  └──────────────────────────────────────────────────────────────────┘  |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WORK DETAIL PAGE LAYOUT" in display font |
| Breadcrumb | `label_editorial` | Works / {work_title} navigation |
| Large confidence gauge | `confidence_high` | lg size (140px) gauge in hero |
| Work title | `heading_display` | Instrument Serif display heading |
| Assurance badge | `assurance_a3` | Color-underlined badge in hero |
| Confidence badge | `data_mono` | "92% -- High Confidence" inline badge |
| Conformal statistics | `data_mono` | Coverage, calibration error, version in monospace |
| Needs review banner | `callout_box` | Conditional amber-bordered alert with priority |
| Credits section | `processing_stage` | CreditList component with per-credit breakdowns |
| Provenance panel | `source_corroborate` | Perplexity-style inline citations and source cards |
| Provenance timeline | `data_flow` | Chronological provenance event chain |
| Accent line dividers | `accent_line` | Coral accent lines between sections (opacity 0.3) |

## Anti-Hallucination Rules

1. The route is /works/[workId] with the dynamic segment being `workId` (not `id`).
2. The hero uses the lg (140px) ConfidenceGauge, NOT md or sm.
3. Components imported: ConfidenceGauge, ConfidenceBadge, AssuranceBadge, CreditList, ProvenanceTimeline, ProvenancePanel.
4. Conformal set data is displayed: marginal_coverage, coverage_level, calibration_error, and version.
5. The "needs review" banner is conditional -- only shows when work.needs_review is true.
6. Accent line dividers use opacity 0.3, NOT full opacity.
7. The ProvenancePanel is described as "Perplexity-like" with inline citation references.
8. Loading state uses skeleton loaders (animate-pulse), NOT spinners.

## Alt Text

Interface mockup of the work detail page in the music attribution scaffold: hero section with large confidence gauge and conformal prediction statistics, per-credit music metadata scores with source tags, Perplexity-style provenance panel with inline citations, and chronological timeline for transparent confidence scoring of music credits provenance.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Interface mockup of the work detail page in the music attribution scaffold: hero section with large confidence gauge and conformal prediction statistics, per-credit music metadata scores with source tags, Perplexity-style provenance panel with inline citations, and chronological timeline for transparent confidence scoring of music credits provenance.](docs/figures/repo-figures/assets/fig-frontend-07-work-detail-layout.jpg)

*Figure: The /works/[workId] detail page surfaces per-field confidence, source provenance with inline citations, and conformal set statistics -- making the attribution scaffold's transparency philosophy visible at every level of musical credit detail.*

### From this figure plan (relative)

![Interface mockup of the work detail page in the music attribution scaffold: hero section with large confidence gauge and conformal prediction statistics, per-credit music metadata scores with source tags, Perplexity-style provenance panel with inline citations, and chronological timeline for transparent confidence scoring of music credits provenance.](../assets/fig-frontend-07-work-detail-layout.jpg)
