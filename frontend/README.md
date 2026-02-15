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
