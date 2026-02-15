# fig-choice-07: Why Next.js 15 App Router?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-07 |
| **Title** | Why Next.js 15 App Router? |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/planning/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains the frontend framework decision. Next.js 15 with App Router was selected primarily because CopilotKit requires React, and Next.js provides the most mature React framework with server components, layouts, and streaming. App Router (not Pages Router) enables server-side rendering with React Server Components, nested layouts, and streaming SSR.

The key message is: "CopilotKit requires React -- Next.js 15 App Router provides the most mature React framework with server components, streaming, and nested layouts."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WHY NEXT.JS 15 APP ROUTER?                                   |
|  ■ Frontend Framework: nextjs (selected)                       |
+---------------------------------------------------------------+
|                                                                |
|  CONSTRAINT: CopilotKit requires React/Next.js                 |
|                                                                |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │ NEXT.JS 15   │ │ SVELTEKIT    │ │ HTMX +       │          |
|  │ APP ROUTER   │ │              │ │ JINJA         │          |
|  │ ■ SELECTED   │ │              │ │              │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ React Server │ │ Svelte 5     │ │ Server-      │          |
|  │ Components   │ │ runes        │ │ rendered     │          |
|  │              │ │              │ │ HTML         │          |
|  │ Nested       │ │ Nested       │ │ No SPA       │          |
|  │ layouts      │ │ layouts      │ │              │          |
|  │              │ │              │ │              │          |
|  │ Streaming    │ │ Streaming    │ │ HTMX partial │          |
|  │ SSR          │ │ SSR          │ │ updates      │          |
|  │              │ │              │ │              │          |
|  │ CopilotKit   │ │ No CopilotKit│ │ No CopilotKit│          |
|  │ COMPATIBLE   │ │ incompatible │ │ incompatible │          |
|  │              │ │              │ │              │          |
|  │ Vercel/self- │ │ Vercel/self- │ │ Any server   │          |
|  │ hosted       │ │ hosted       │ │              │          |
|  │              │ │              │ │              │          |
|  │ TypeScript   │ │ TypeScript   │ │ Python +     │          |
|  │ strict       │ │ strict       │ │ HTML         │          |
|  │              │ │              │ │              │          |
|  │ P=0.35-0.45  │ │ P(~0.15)    │ │ P(~0.20)    │          |
|  └──────────────┘ └──────────────┘ └──────────────┘          |
|                                                                |
|  APP ROUTER vs PAGES ROUTER                                    |
|  ┌──────────────────────┐  ┌──────────────────────┐          |
|  │ App Router (selected)│  │ Pages Router (legacy) │          |
|  │ /app directory       │  │ /pages directory      │          |
|  │ Server Components    │  │ getServerSideProps    │          |
|  │ Nested layouts       │  │ _app.tsx wrapper      │          |
|  │ Streaming            │  │ No streaming          │          |
|  └──────────────────────┘  └──────────────────────┘          |
|                                                                |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WHY NEXT.JS 15 APP ROUTER?" with coral accent square |
| CopilotKit constraint banner | `callout_bar` | Hard dependency: CopilotKit requires React/Next.js |
| Next.js card | `selected_option` | RSC, nested layouts, streaming, CopilotKit compatible |
| SvelteKit card | `deferred_option` | Similar features but CopilotKit incompatible |
| HTMX+Jinja card | `deferred_option` | Server-rendered, no SPA, CopilotKit incompatible |
| App vs Pages comparison | `branching_path` | App Router (/app) vs Pages Router (/pages) feature comparison |

## Anti-Hallucination Rules

1. CopilotKit requires React/Next.js -- this is a hard constraint from the agentic_ui_framework decision node.
2. P(CopilotKit | Next.js) = 0.50 and P(CopilotKit | SvelteKit) = 0.05 -- from conditional tables.
3. The frontend uses Next.js 15 with App Router, TypeScript strict, Tailwind CSS v4.
4. Frontend framework archetype probabilities from REPORT.md: Engineer Next.js 0.35, Musician Next.js 0.45, Solo No Frontend 0.35, Well-Funded Next.js 0.45.
5. All pages are in `frontend/src/app/` directory (App Router convention).
6. The scaffold does NOT use Pages Router (/pages directory).
7. SvelteKit and HTMX+Jinja are viable alternatives for teams that do NOT need CopilotKit.
8. Background must be warm cream (#f6f3e6).

## Alt Text

Architecture decision: Next.js 15 App Router selected for music attribution frontend, driven by CopilotKit React dependency for agentic UI, compared against SvelteKit and HTMX alternatives, with server components and streaming SSR enabling transparent confidence display in the open-source attribution scaffold.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture decision: Next.js 15 App Router selected for music attribution frontend, driven by CopilotKit React dependency for agentic UI, compared against SvelteKit and HTMX alternatives, with server components and streaming SSR enabling transparent confidence display in the open-source attribution scaffold.](docs/figures/repo-figures/assets/fig-choice-07-nextjs-app-router.jpg)

*Next.js 15 with App Router was selected as the frontend framework for the music attribution scaffold primarily because CopilotKit requires React, providing server components, nested layouts, and streaming SSR for real-time confidence scoring display.*

### From this figure plan (relative)

![Architecture decision: Next.js 15 App Router selected for music attribution frontend, driven by CopilotKit React dependency for agentic UI, compared against SvelteKit and HTMX alternatives, with server components and streaming SSR enabling transparent confidence display in the open-source attribution scaffold.](../assets/fig-choice-07-nextjs-app-router.jpg)
