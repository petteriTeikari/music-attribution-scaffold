# Music Attribution Frontend

Editorial-design frontend for the Music Attribution Scaffold. Built with Next.js 15 (App Router), React 19, Tailwind CSS v4, and CopilotKit for agentic sidebar interaction.

## Prerequisites

- Node.js 22+
- Backend API running at `http://localhost:8000` (or set `NEXT_PUBLIC_API_URL`)

## Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Or from the project root:
make dev-frontend
```

The frontend runs at `http://localhost:3000`.

## Pages

| Route | Page | Description |
|---|---|---|
| `/` | Home | Landing page with project overview |
| `/works` | Works List | Browse attribution records with confidence badges and assurance indicators |
| `/works/[workId]` | Work Detail | Full attribution record with provenance timeline, confidence breakdown, and uncertainty visualization |
| `/permissions` | Permissions | Permission patchbay -- view and manage AI training consent per entity |
| `/review` | Review Queue | Active learning review queue sorted by priority score |

## Design System

The UI follows an editorial design language inspired by Warp Records, IZUM, and Bauhaus constructivism. Key principles:

- **Typography-driven**: Instrument Serif (display headings at 48-96px), Plus Jakarta Sans (body/UI), IBM Plex Mono (data/scores)
- **Zero hardcoded hex**: All colors are CSS custom properties defined in `src/app/globals.css`
- **Coral red accent**: `#E84C4F` as the single bold graphic accent against warm neutrals
- **Confidence tiers**: Green (>= 0.85), Amber (0.50-0.84), Red (< 0.50) for instant readability
- **Assurance colors**: A3 green, A2 blue, A1 amber, A0 gray
- **Fixed left sidebar**: Rotated vertical text navigation, not a horizontal top nav
- **Horizontal rows with dividers**: Not shadow-box cards

See `.claude/rules/10-frontend-design-system.md` for the full design token reference.

## Dependencies

| Package | Purpose |
|---|---|
| `next` 15.x | App Router framework |
| `react` 19.x | UI library |
| `@copilotkit/react-core` + `@copilotkit/react-ui` | Agentic sidebar (AG-UI protocol) |
| `jotai` | Atomic state management (theme, role mode, works) |
| `motion` | Scroll-triggered stagger reveal animations |
| `posthog-js` | Product analytics (typed events) |
| `tailwindcss` v4 | Utility CSS with custom property tokens |

## Testing

```bash
# Run all 265 Vitest tests
npm run test

# Watch mode
npm run test:watch

# Coverage report
npm run test:coverage

# E2E tests with Playwright
npm run test:e2e

# E2E tests with UI
npm run test:e2e:ui
```

Tests use Vitest + React Testing Library. Component-level WCAG accessibility checks use `vitest-axe`. Browser-level accessibility tests use `@axe-core/playwright`.

## CopilotKit Integration

The sidebar provides an agentic chat experience powered by PydanticAI on the backend:

- Backend streams AG-UI events via SSE from `/api/v1/copilotkit`
- `useCopilotReadable` hooks expose current work context to the agent
- `useCopilotAction` hooks allow the agent to trigger UI actions
- Agent state (current work, confidence score, pending corrections) syncs via StateSnapshot events

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `NEXT_PUBLIC_API_URL` | `http://localhost:8000` | Backend API base URL |
| `NEXT_PUBLIC_POSTHOG_KEY` | -- | PostHog project API key (optional) |
| `NEXT_PUBLIC_POSTHOG_HOST` | -- | PostHog host URL (optional) |

## Tailwind v4 Pitfall

Never use `text-[var(--anything)]` in Tailwind v4. The framework cannot disambiguate font-size from color in arbitrary value syntax. Use Tailwind's built-in scale (`text-xl`, `text-2xl`, etc.) instead. A lint test enforces this rule. See `.claude/memory/css-tailwind-v4-pitfalls.md` for full details.

## Visual Documentation

<details>
<summary>Click to expand visual documentation</summary>

![Frontend architecture overview showing Next.js App Router, CopilotKit, Jotai state, and API integration](docs/figures/repo-figures/assets/fig-frontend-01-architecture-overview.jpg)
*Frontend architecture -- Next.js 15 App Router, CopilotKit sidebar, Jotai atoms, and backend API integration.*

![Design token architecture showing CSS custom properties flowing from globals.css to components](docs/figures/repo-figures/assets/fig-frontend-02-design-token-architecture.jpg)
*Design token architecture -- CSS custom properties in globals.css providing zero-hardcoded-hex theming.*

![Page router map showing all routes, layouts, and page components](docs/figures/repo-figures/assets/fig-frontend-03-page-router-map.jpg)
*Page router map -- App Router routes for home, works list, work detail, permissions, and review queue.*

![Confidence gauge component showing green/amber/red tiers with animated fill](docs/figures/repo-figures/assets/fig-frontend-04-confidence-gauge.jpg)
*ConfidenceGauge component -- tier-colored meter with mount animation and ARIA role="meter".*

![Assurance badge system showing A0-A3 level indicators with corresponding colors](docs/figures/repo-figures/assets/fig-frontend-05-assurance-badge-system.jpg)
*Assurance badge system -- A0 gray, A1 amber, A2 blue, A3 green level indicators.*

![Works list layout showing horizontal rows with dividers, confidence badges, and assurance indicators](docs/figures/repo-figures/assets/fig-frontend-06-works-list-layout.jpg)
*Works list page -- editorial horizontal rows with confidence badges and assurance level indicators.*

![Work detail layout showing provenance timeline, confidence breakdown, and uncertainty visualization](docs/figures/repo-figures/assets/fig-frontend-07-work-detail-layout.jpg)
*Work detail page -- full attribution record with provenance timeline and confidence breakdown.*

![Review queue workflow showing priority-sorted list with batch approval actions](docs/figures/repo-figures/assets/fig-frontend-08-review-queue-workflow.jpg)
*Review queue -- active learning workflow with priority sorting and batch approval.*

![Jotai state architecture showing atoms for theme, role mode, and works data](docs/figures/repo-figures/assets/fig-frontend-09-jotai-state-architecture.jpg)
*Jotai state architecture -- atomic state management for theme, role mode, and works data.*

![Typography system showing Instrument Serif, Plus Jakarta Sans, and IBM Plex Mono usage](docs/figures/repo-figures/assets/fig-frontend-10-typography-system.jpg)
*Typography system -- Instrument Serif (display), Plus Jakarta Sans (body/UI), IBM Plex Mono (data).*

![Color system showing surface, brand, confidence, assurance, and source colors with light/dark variants](docs/figures/repo-figures/assets/fig-frontend-11-color-system.jpg)
*Color system -- surface, brand, confidence tier, assurance level, and data source color tokens.*

![Responsive layout showing fixed sidebar on desktop and top bar with hamburger on mobile](docs/figures/repo-figures/assets/fig-frontend-12-responsive-layout.jpg)
*Responsive layout -- fixed left sidebar (desktop) to top bar with hamburger overlay (mobile).*

![Accessibility architecture showing vitest-axe component checks and Playwright axe-core browser checks](docs/figures/repo-figures/assets/fig-frontend-13-accessibility-architecture.jpg)
*Accessibility architecture -- two-layer WCAG testing with vitest-axe and @axe-core/playwright.*

![PostHog analytics showing typed event tracking and user flow analysis](docs/figures/repo-figures/assets/fig-frontend-14-posthog-analytics.jpg)
*PostHog analytics integration -- typed events for attribution workflow tracking.*

![Adaptive UI proficiency model showing experience-based progressive disclosure](docs/figures/repo-figures/assets/fig-frontend-15-adaptive-ui-proficiency.jpg)
*Adaptive UI -- proficiency model with experience-based tooltips and progressive feature disclosure.*

</details>
