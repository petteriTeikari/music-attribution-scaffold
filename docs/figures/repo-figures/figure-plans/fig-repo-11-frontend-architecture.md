# fig-repo-11: Frontend Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-repo-11 |
| **Title** | Frontend Architecture: Next.js 15 Page Tree + Component Modules |
| **Audience** | Technical (frontend contributors) |
| **Complexity** | L2 (architecture) |
| **Location** | docs/architecture/frontend.md, README.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

The frontend is a Next.js 15 App Router application with 19 component modules organized by domain. This figure shows the page routing tree (what URLs exist), the component module organization (how they group), and the state/styling layers (Jotai atoms, Tailwind v4 tokens, CopilotKit). It helps frontend contributors understand where to add new pages and components.

The key message is: "Four route groups, 19 component modules, and three cross-cutting layers (Jotai state, Tailwind tokens, CopilotKit agent) -- organized by domain, not by technical role."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  FRONTEND ARCHITECTURE                                                 |
|  ■ Next.js 15 App Router + 19 Component Modules                       |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. PAGE TREE (App Router)                                             |
|  ─────────────────────────                                             |
|                                                                        |
|  frontend/src/app/                                                     |
|  ├── page.tsx              /              Landing (hero + dashboard)    |
|  ├── works/                /works         Works catalog + detail        |
|  ├── review/               /review        Attribution review queue      |
|  └── permissions/          /permissions   MCP consent management        |
|                                                                        |
|  II. COMPONENT MODULES (19)                                            |
|  ──────────────────────────                                            |
|                                                                        |
|  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐         |
|  │attribution │ │ confidence │ │ provenance │ │   works    │         |
|  │            │ │ gauges +   │ │ citations  │ │ catalog +  │         |
|  │ cards +    │ │ tiers      │ │ + badges   │ │ detail     │         |
|  │ diffs      │ │            │ │            │ │            │         |
|  └────────────┘ └────────────┘ └────────────┘ └────────────┘         |
|  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐         |
|  │   chat     │ │permissions │ │   review   │ │   editor   │         |
|  │ CopilotKit │ │ MCP toggle │ │  queue +   │ │ inline     │         |
|  │ sidebar    │ │ + cards    │ │  batch     │ │ edit       │         |
|  └────────────┘ └────────────┘ └────────────┘ └────────────┘         |
|  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐         |
|  │  layout    │ │   theme    │ │   mode     │ │  landing   │         |
|  │ sidebar +  │ │ toggle +   │ │ artist/    │ │ hero +     │         |
|  │ footer     │ │ provider   │ │ query role │ │ features   │         |
|  └────────────┘ └────────────┘ └────────────┘ └────────────┘         |
|  + ui, states, feedback, pro, notifications, mcp, citations           |
|                                                                        |
|  III. CROSS-CUTTING LAYERS                                             |
|  ─────────────────────────                                             |
|  ■ Jotai atoms (theme, role, works)                                    |
|  ■ Tailwind v4 CSS custom properties (zero hardcoded hex)              |
|  ■ CopilotKit AG-UI (useCopilotReadable/Action hooks)                 |
|  ■ PostHog analytics (typed events)                                    |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title | `heading_display` | "FRONTEND ARCHITECTURE" Instrument Serif ALL-CAPS |
| Page tree | `data_mono` | IBM Plex Mono tree structure with route paths |
| Route descriptions | `label_editorial` | Plus Jakarta Sans, what each route renders |
| Component module grid | `module_grid` | 4x3 grid of component module cards |
| Module names | `data_mono` | IBM Plex Mono module names |
| Module descriptions | `label_editorial` | Brief description inside each card |
| Cross-cutting list | `feature_list` | Four items with accent square bullets |
| Roman numerals I-III | `section_numeral` | Section identifiers |
| Horizontal dividers | `accent_line` | Coral lines between sections |
| Accent squares | `accent_square` | Coral squares as bullets and markers |

## Anti-Hallucination Rules

1. App Router pages exist at: / (page.tsx), /works, /review, /permissions -- no other routes.
2. There are exactly 19 component modules under `frontend/src/components/`: attribution, chat, citations, confidence, editor, feedback, landing, layout, mcp, mode, notifications, permissions, pro, provenance, review, states, theme, ui, works.
3. State management is Jotai (not Redux, Zustand, or React Context).
4. CopilotKit is the AG-UI integration, using useCopilotReadable and useCopilotAction hooks.
5. Styling is Tailwind CSS v4 with CSS custom properties -- zero hardcoded hex in .tsx files.
6. Analytics is PostHog with typed events in `frontend/src/lib/analytics/events.ts`.
7. The design system uses Instrument Serif (display), Plus Jakarta Sans (body), IBM Plex Mono (data).
8. Do NOT show a /dashboard or /settings route -- they do not exist.
9. The framework is Next.js 15 (not 13 or 14), using App Router (not Pages Router).

## Alt Text

Frontend architecture: four App Router pages, 19 component modules in domain-organized grid, three cross-cutting layers for state, styling, and agent integration.
