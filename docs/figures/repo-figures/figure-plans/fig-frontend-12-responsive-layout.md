# fig-frontend-12: Responsive Layout Strategy

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-12 |
| **Title** | Responsive Layout: Desktop Sidebar to Mobile Top Bar Transformation |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/design-system.md, docs/architecture/frontend.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows how the layout transforms across three breakpoints: desktop (sidebar + offset content), tablet (same but tighter), and mobile (top bar + full-width content + hamburger slide-over). The Navigation component's dual rendering paths (md:flex sidebar vs md:hidden top bar) and the mobile slide-over overlay are illustrated.

The key message is: "The layout pivots at the md breakpoint -- desktop uses a fixed 60px left sidebar with rotated text, mobile replaces it with a 48px top bar and hamburger-triggered slide-over panel."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  RESPONSIVE LAYOUT STRATEGY                                            |
|  ■ Desktop / Tablet / Mobile                                           |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. DESKTOP (md+)                                                      |
|  ─────────────────                                                     |
|                                                                        |
|  ┌────┐ ┌─────────────────────────────────────────┐                   |
|  │ MA │ │                                          │                   |
|  │    │ │  Main content area                       │                   |
|  │ W  │ │  margin-left: var(--sidebar-width)       │                   |
|  │ O  │ │  60px sidebar                            │                   |
|  │ R  │ │                                          │                   |
|  │ K  │ │  Full-width editorial grids              │                   |
|  │ S  │ │  (NOT max-w-4xl mx-auto)                 │                   |
|  │    │ │                                          │                   |
|  │────│ │                                          │  Agent toggle     |
|  │ A/Q│ │                                          │  fixed BR         |
|  │ 🔔 │ │                                          │  ┌──┐            |
|  │ ☀️ │ └─────────────────────────────────────────┘  │💬│            |
|  │ ■  │                                              └──┘            |
|  └────┘                                                                |
|                                                                        |
|  II. MOBILE (<md)                                                      |
|  ─────────────────                                                     |
|                                                                        |
|  ┌──────────────────────────┐                                         |
|  │ MA                    ☰  │  48px top bar (fixed)                   |
|  └──────────────────────────┘                                         |
|  ┌──────────────────────────┐                                         |
|  │                          │  Full-width content                     |
|  │  padding-top: 48px       │  No sidebar offset                     |
|  │                          │                                         |
|  │  Content adapts to       │                                         |
|  │  full viewport width     │                                         |
|  │                          │                                         |
|  └──────────────────────────┘                                         |
|                                                                        |
|  III. MOBILE SLIDE-OVER (hamburger open)                               |
|  ────────────────────────────────────────                              |
|                                                                        |
|  ┌──────────────────┐ ┌────────────────┐                              |
|  │                  │ │ ✕              │                              |
|  │  Backdrop        │ │                │  w-64 slide-over             |
|  │  (black/30)      │ │ WORKS          │  right-aligned              |
|  │                  │ │ REVIEW         │  editorial-caps links        |
|  │                  │ │ PERMISSIONS    │                              |
|  │                  │ │                │                              |
|  │                  │ │ ─────────     │                              |
|  │                  │ │ Role toggle   │                              |
|  │                  │ │ Theme toggle  │                              |
|  └──────────────────┘ └────────────────┘                              |
|                                                                        |
|  BREAKPOINT: md (768px)                                                |
|  Desktop sidebar: hidden below md (md:flex)                            |
|  Mobile top bar: hidden at md+ (md:hidden)                             |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "RESPONSIVE LAYOUT STRATEGY" in display font |
| Desktop layout | `module_grid` | Fixed sidebar + offset main content |
| Sidebar detail | `processing_stage` | 60px wide, rotated nav links, MA logo, controls, accent square |
| Mobile top bar | `processing_stage` | 48px high, MA logo left, hamburger right |
| Mobile content | `processing_stage` | Full-width, padding-top 48px |
| Slide-over panel | `processing_stage` | w-64, right-aligned, backdrop overlay |
| Agent toggle button | `api_endpoint` | Fixed bottom-right, 48x48px coral square |
| Breakpoint label | `data_mono` | md (768px) pivot point |
| Roman numerals I-III | `section_numeral` | Section identifiers |

## Anti-Hallucination Rules

1. The breakpoint pivot is at `md` (768px) -- not sm, lg, or a custom breakpoint.
2. Desktop sidebar is 60px (var(--sidebar-width)), position fixed, full height.
3. Mobile top bar is 48px high (py-3 px-4), position fixed, full width.
4. The slide-over is w-64 (256px), right-aligned, with bg-black/30 backdrop overlay.
5. Navigation links in sidebar use vertical-rl writing mode with rotate(180deg).
6. Main content uses margin-left: var(--sidebar-width) on desktop, NO margin on mobile.
7. Mobile content uses pt-[48px] to clear the fixed top bar.
8. `max-w-4xl mx-auto` centered containers are BANNED -- the design uses full-width editorial grids.
9. The agent toggle button is fixed bottom-right (bottom-6 right-6), 48x48px, bg-accent.

## Alt Text

UI wireframe showing the responsive layout strategy for the music attribution scaffold: desktop view with fixed 60px left sidebar and editorial content grid, mobile view with 48px top bar, and hamburger-triggered slide-over navigation panel, all built with Tailwind CSS v4 breakpoints for accessible music credits and transparent confidence scoring on any device.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![UI wireframe showing the responsive layout strategy for the music attribution scaffold: desktop view with fixed 60px left sidebar and editorial content grid, mobile view with 48px top bar, and hamburger-triggered slide-over navigation panel, all built with Tailwind CSS v4 breakpoints for accessible music credits and transparent confidence scoring on any device.](docs/figures/repo-figures/assets/fig-frontend-12-responsive-layout.jpg)

*Figure: Responsive layout transformation at the md (768px) breakpoint, pivoting from a fixed left sidebar with rotated text navigation on desktop to a top bar with hamburger slide-over on mobile for consistent music attribution access.*

### From this figure plan (relative)

![UI wireframe showing the responsive layout strategy for the music attribution scaffold: desktop view with fixed 60px left sidebar and editorial content grid, mobile view with 48px top bar, and hamburger-triggered slide-over navigation panel, all built with Tailwind CSS v4 breakpoints for accessible music credits and transparent confidence scoring on any device.](../assets/fig-frontend-12-responsive-layout.jpg)
