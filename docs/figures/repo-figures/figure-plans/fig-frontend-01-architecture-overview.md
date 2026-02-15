# fig-frontend-01: Frontend Architecture Overview

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-01 |
| **Title** | Frontend Architecture: Next.js 15 App Router, Components, Lib, and Hooks |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 |
| **Location** | docs/architecture/frontend.md, README.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure provides the high-level mental model of how the frontend is organized. It shows the four-layer architecture: App Router pages at the top, 19 component modules grouped by domain, the lib layer (stores, analytics, copilot, theme, API, types), and the hooks layer that bridges components to state and agent actions. The fixed sidebar layout is shown as a spatial reference.

The key message is: "The frontend is a four-layer Next.js 15 application -- pages compose components, components consume lib utilities, and hooks wire everything to Jotai state and CopilotKit agent context."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  FRONTEND ARCHITECTURE OVERVIEW                                        |
|  ■ Next.js 15 App Router                                              |
+-----------------------------------------------------------------------+
|                                                                        |
|  ┌──────────────────────────────────────────────────────────────────┐  |
|  │  layout.tsx (RootLayout)                                         │  |
|  │  PostHogProvider > CopilotProvider > ThemeProvider > AppShell     │  |
|  └──────────────────────────────────────────────────────────────────┘  |
|                           │                                            |
|  ┌─────────┐  ┌──────────┼────────────────────────────────────────┐   |
|  │ SIDEBAR │  │  APP ROUTER PAGES                                 │   |
|  │ ─────── │  │  ┌──────┐ ┌──────────┐ ┌────────┐ ┌───────────┐ │   |
|  │ MA logo │  │  │  /   │ │ /works   │ │/review │ │/permissions│ │   |
|  │ Works   │  │  │ hero │ │ catalog  │ │ queue  │ │ MCP mgmt  │ │   |
|  │ Review  │  │  │ dash │ │ + detail │ │ batch  │ │ consent   │ │   |
|  │ Perms   │  │  └──────┘ └──────────┘ └────────┘ └───────────┘ │   |
|  │ ─────── │  └──────────────────────────────────────────────────┘   |
|  │ A/Q     │                      │                                    |
|  │ Bell    │  ┌───────────────────┼──────────────────────────────┐    |
|  │ Theme   │  │  19 COMPONENT MODULES (by domain)                │    |
|  │ ■       │  │  attribution | confidence | works | review       │    |
|  └─────────┘  │  chat | layout | theme | mode | permissions      │    |
|               │  landing | provenance | citations | editor       │    |
|               │  pro | states | feedback | notifications | ui | mcp│   |
|               └──────────────────────────────────────────────────┘    |
|                               │                                        |
|               ┌───────────────┼──────────────────────────────────┐    |
|               │  LIB LAYER                                        │    |
|               │  stores/  analytics/  copilot/  theme/  api/      │    |
|               │  types/   data/       config.ts                   │    |
|               └──────────────────────────────────────────────────┘    |
|                               │                                        |
|               ┌───────────────┼──────────────────────────────────┐    |
|               │  HOOKS                                            │    |
|               │  useAgentActions  useAttributionContext            │    |
|               │  useFeatureFlags                                  │    |
|               └──────────────────────────────────────────────────┘    |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "FRONTEND ARCHITECTURE OVERVIEW" in display font |
| RootLayout provider chain | `processing_stage` | PostHogProvider > CopilotProvider > ThemeProvider > AppShell |
| Sidebar diagram | `module_grid` | Fixed left sidebar with MA logo, nav links, role toggle, theme toggle, accent square |
| App Router pages | `api_endpoint` | Four route boxes: /, /works, /review, /permissions |
| Component modules block | `module_grid` | 19 modules listed by domain grouping |
| Lib layer block | `storage_layer` | stores, analytics, copilot, theme, api, types, data, config |
| Hooks block | `processing_stage` | Three custom hooks connecting to state and agent |
| Vertical flow arrows | `data_flow` | Top-to-bottom composition hierarchy |
| Accent square in sidebar | `accent_square` | Coral square at sidebar bottom |

## Anti-Hallucination Rules

1. The frontend uses Next.js 15 App Router (not Pages Router, not Next.js 13/14).
2. There are exactly 4 routes: /, /works (+ /works/[workId]), /review, /permissions.
3. There are exactly 19 component directories: attribution, chat, citations, confidence, editor, feedback, landing, layout, mcp, mode, notifications, permissions, pro, provenance, review, states, theme, ui, works.
4. The provider chain order is: PostHogProvider > CopilotProvider > ThemeProvider > AppShell.
5. State management is Jotai (not Redux, Zustand, or Context API).
6. There are exactly 3 custom hooks: useAgentActions, useAttributionContext, useFeatureFlags.
7. The sidebar is fixed left (60px), not a horizontal top nav on desktop.
8. Do NOT show any routes that do not exist (/dashboard, /settings, /profile).

## Alt Text

Architecture diagram showing the four-layer Next.js 15 frontend for the open-source music attribution scaffold: App Router pages compose 19 domain-organized component modules, lib utilities including Jotai state and CopilotKit agent context, and three custom hooks bridging transparent confidence scoring UI to agentic workflows.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture diagram showing the four-layer Next.js 15 frontend for the open-source music attribution scaffold: App Router pages compose 19 domain-organized component modules, lib utilities including Jotai state and CopilotKit agent context, and three custom hooks bridging transparent confidence scoring UI to agentic workflows.](docs/figures/repo-figures/assets/fig-frontend-01-architecture-overview.jpg)

*Figure: High-level frontend architecture of the Music Attribution Scaffold, illustrating how four composition layers -- pages, components, lib, and hooks -- organize a Next.js 15 App Router application for transparent music credits and confidence-scored attribution workflows.*

### From this figure plan (relative)

![Architecture diagram showing the four-layer Next.js 15 frontend for the open-source music attribution scaffold: App Router pages compose 19 domain-organized component modules, lib utilities including Jotai state and CopilotKit agent context, and three custom hooks bridging transparent confidence scoring UI to agentic workflows.](../assets/fig-frontend-01-architecture-overview.jpg)
