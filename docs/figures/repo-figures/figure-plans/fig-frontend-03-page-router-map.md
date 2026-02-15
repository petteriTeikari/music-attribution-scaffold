# fig-frontend-03: Page Router Map

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-03 |
| **Title** | App Router Tree: Page Hierarchy and Layout Nesting |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/frontend.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows the Next.js 15 App Router page tree with its layout nesting. It maps each file-system path to its URL, the page component it renders, and the key child components each page composes. The layout hierarchy (RootLayout wrapping all pages) and the dynamic route segment (/works/[workId]) are highlighted.

The key message is: "Five page files under frontend/src/app/ produce four URL paths, with a shared RootLayout providing sidebar navigation, theme, and agent context to all pages."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  PAGE ROUTER MAP                                                       |
|  ■ Next.js 15 App Router                                              |
+-----------------------------------------------------------------------+
|                                                                        |
|  frontend/src/app/                                                     |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  layout.tsx  ──  RootLayout (wraps ALL pages)                    │  |
|  │  ┌──────────────────────────────────────────────────────────┐    │  |
|  │  │  PostHogProvider > CopilotProvider > ThemeProvider        │    │  |
|  │  │  > AppShell (Sidebar + Main + Footer + Agent toggle)     │    │  |
|  │  └──────────────────────────────────────────────────────────┘    │  |
|  └──────────┬───────────────────────────────────────────────────────┘  |
|             │                                                          |
|  ┌──────────┼──────────┬──────────────┬──────────────┐                |
|  │          │          │              │              │                  |
|  ▼          ▼          ▼              ▼              ▼                  |
|  /          /works     /works/[id]    /review        /permissions      |
|  page.tsx   page.tsx   page.tsx       page.tsx       page.tsx          |
|  ─────────  ─────────  ─────────     ─────────      ─────────         |
|  Landing    Works      Work Detail   Review Queue   Permission        |
|  Hero       Catalog    Page          AI Batch       Consent Mgmt      |
|                                                                        |
|  Composes:  Composes:  Composes:     Composes:      Composes:          |
|  ■ Hero     ■ WorkCard ■ Confidence  ■ AgentReview  ■ Permission      |
|    sections ■ Search     Gauge (lg)    Queue           Cards           |
|  ■ Feature  ■ Sort     ■ Assurance   ■ Confidence   ■ MCP toggle      |
|    grid     ■ Filter     Badge         Gauge (sm)                     |
|  ■ Voice    ■ Confid.  ■ CreditList  ■ Assurance                     |
|    banner     Gauge    ■ Provenance    Badge                          |
|             ■ Assur.     Timeline    ■ Suggestions                    |
|               Badge    ■ Provenance    (diff view)                    |
|                          Panel       ■ Approve All                    |
|                                      ■ Progress bar                   |
|                                                                        |
|  ROUTE VISIBILITY                                                      |
|  ────────────────                                                      |
|  /review only visible in artist role (artistOnly: true)                |
|  All other routes visible in both artist and query roles               |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "PAGE ROUTER MAP" in display font |
| RootLayout box | `processing_stage` | Provider chain and AppShell wrapping all pages |
| Route tree | `data_flow` | Branching from layout.tsx to five page.tsx files |
| Route labels | `data_mono` | URL paths in monospace (/, /works, /works/[id], /review, /permissions) |
| Page descriptions | `label_editorial` | What each page renders (Landing Hero, Works Catalog, etc.) |
| Component composition lists | `feature_list` | Bullet lists of key child components per page |
| Role visibility note | `callout_box` | /review route is artist-only |
| Dynamic segment highlight | `decision_point` | [workId] dynamic route parameter |

## Anti-Hallucination Rules

1. There are exactly 5 page.tsx files: app/page.tsx, app/works/page.tsx, app/works/[workId]/page.tsx, app/review/page.tsx, app/permissions/page.tsx.
2. The dynamic segment is [workId] (not [id] or [slug]).
3. The /review route has `artistOnly: true` in the NAV_ITEMS array -- it is hidden in query mode.
4. Layout nesting is single-level: only one layout.tsx at the app root, no nested layouts.
5. The provider chain order is: PostHogProvider > CopilotProvider > ThemeProvider > AppShell.
6. The Work Detail page imports: ConfidenceGauge, ConfidenceBadge, AssuranceBadge, CreditList, ProvenanceTimeline, ProvenancePanel.
7. The Review page uses AgentReviewQueue component with AI suggestion diffs.
8. Do NOT show /dashboard, /settings, /profile, or /api routes -- they do not exist in the App Router.

## Alt Text

Component diagram mapping the Next.js 15 App Router page tree for the open-source music attribution scaffold: five page files branch from a shared RootLayout with provider chain, rendering works catalog, work detail with transparent confidence scoring, AI-assisted review queue, and MCP permission consent management routes.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Component diagram mapping the Next.js 15 App Router page tree for the open-source music attribution scaffold: five page files branch from a shared RootLayout with provider chain, rendering works catalog, work detail with transparent confidence scoring, AI-assisted review queue, and MCP permission consent management routes.](docs/figures/repo-figures/assets/fig-frontend-03-page-router-map.jpg)

*Figure: App Router page hierarchy showing how five route segments compose domain-specific components for music metadata browsing, attribution review, and permission management under a shared layout with CopilotKit agent context.*

### From this figure plan (relative)

![Component diagram mapping the Next.js 15 App Router page tree for the open-source music attribution scaffold: five page files branch from a shared RootLayout with provider chain, rendering works catalog, work detail with transparent confidence scoring, AI-assisted review queue, and MCP permission consent management routes.](../assets/fig-frontend-03-page-router-map.jpg)
