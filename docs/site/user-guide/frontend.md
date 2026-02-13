# Frontend Guide

## Tech Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Next.js** | 15 (App Router) | React framework with server components |
| **React** | 19 | UI library |
| **TypeScript** | 5.8 (strict) | Type safety |
| **Tailwind CSS** | 4 | Utility-first CSS with design tokens |
| **Jotai** | 2.12 | Atomic state management |
| **motion** | 12 | Scroll-triggered animations (motion/react) |
| **CopilotKit** | 1.51 | AG-UI agent sidebar integration |
| **PostHog** | posthog-js | Product analytics with typed events |
| **Vitest** | 3.2 | Unit + component testing |
| **React Testing Library** | 16.3 | Component test utilities |
| **vitest-axe** | 1.0-pre | WCAG accessibility assertions |
| **Playwright** | 1.58 | End-to-end browser testing |

## Page Structure

The frontend uses Next.js 15 App Router. All pages live under `frontend/src/app/`:

```
frontend/src/app/
├── layout.tsx              # Root layout — fonts, providers, AppShell
├── globals.css             # Design token system (CSS custom properties)
├── page.tsx                # / — Landing page (hero, how-it-works, assurance levels)
├── works/
│   ├── page.tsx            # /works — Work catalog with search, sort, filter
│   └── [workId]/
│       └── page.tsx        # /works/:id — Work detail (gauge, credits, provenance)
├── permissions/
│   └── page.tsx            # /permissions — Permission matrix, MCP query demo, audit log
└── review/
    └── page.tsx            # /review — Agent-assisted review queue (artist mode only)
```

### Layout Architecture

The root layout (`layout.tsx`) loads three Google Fonts, then wraps the application in a provider chain:

```
PostHogProvider → CopilotProvider → ThemeProvider → AppShell
```

`AppShell` provides the persistent layout shell:

- **Desktop**: Fixed left sidebar (60px, `--sidebar-width`) with rotated text navigation, role toggle (A/Q), theme toggle, notification badge, and accent square
- **Mobile**: Top bar with hamburger menu that opens a slide-over overlay
- **Agent chat**: Floating coral button (bottom-right) toggles the CopilotKit sidebar
- **Footer**: Sidebar-offset, rotated text + accent line

### Page Descriptions

| Route | Component | Description |
|-------|-----------|-------------|
| `/` | `HomePage` | Editorial landing page with hero image, four-step process diagram, 12 citation topic cards, A0-A3 assurance table, and references section |
| `/works` | `WorksPage` | Searchable, sortable catalog of attribution records. Loads works via API client, stores in Jotai. Shows `WorkCard` rows with confidence badges |
| `/works/:id` | `WorkDetailPage` | Full attribution detail: large confidence gauge, assurance badge, credit list, provenance sources panel, and provenance timeline |
| `/permissions` | `PermissionsPage` | Three tabs (Permission Matrix, MCP Query Demo, Audit Log) with category cards and delegation chain display |
| `/review` | `ReviewPage` | Artist-mode-only review queue with approve/approve-all, agent feedback flow, and CopilotKit context sharing. Redirects non-artist users |

## Design System

### Color Tokens

All colors are defined as CSS custom properties in `frontend/src/app/globals.css`. Component code references tokens only -- zero hardcoded hex values in `.tsx` files.

**Surface palette (light theme default):**

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-surface` | `#f6f3e6` | Main background (warm cream) |
| `--color-surface-secondary` | `#eeeadb` | Panel backgrounds |
| `--color-surface-tertiary` | `#e6e1d0` | Nested panels |
| `--color-surface-elevated` | `#FFFFFF` | Cards, modals |
| `--color-sidebar` | `#F8F6F0` | Sidebar background |

**Brand colors:**

| Token | Hex | Meaning |
|-------|-----|---------|
| `--color-primary` | `#1E3A5F` | Trust, authority |
| `--color-accent` | `#E84C4F` | Coral red -- primary graphic accent |
| `--color-teal` | `#2E7D7B` | Innovation, technology |

**Confidence tiers:**

| Token | Color | Threshold |
|-------|-------|-----------|
| `--color-confidence-high` | Green (`#4A7C59`) | >= 0.85 |
| `--color-confidence-medium` | Amber (`#8B6914`) | 0.50 - 0.84 |
| `--color-confidence-low` | Red (`#C44536`) | < 0.50 |

**Assurance levels (A0-A3):**

| Token | Color | Level |
|-------|-------|-------|
| `--color-assurance-a3` | Green (`#4A7C59`) | Artist-verified |
| `--color-assurance-a2` | Blue (`#5B9BD5`) | Multiple sources agree |
| `--color-assurance-a1` | Amber (`#E09F3E`) | Single source |
| `--color-assurance-a0` | Gray (`#9E9E9E`) | No data |

**Data source colors:**

| Token | Source |
|-------|--------|
| `--color-source-musicbrainz` | MusicBrainz (purple `#BA478F`) |
| `--color-source-discogs` | Discogs (dark gray `#333333`) |
| `--color-source-acoustid` | AcoustID (teal `#2E7D7B`) |
| `--color-source-artist` | Artist input (gold `#D4A03C`) |
| `--color-source-file` | File metadata (gray `#666666`) |

Dark theme overrides are defined in a `.dark` selector block in the same file.

### Typography

Three typefaces loaded via `next/font/google` in the root layout:

| Font | CSS Variable | Role | Sizes |
|------|-------------|------|-------|
| **Instrument Serif** (Regular + Italic) | `--font-display` | Hero headings, section titles | 48-96px, often ALL-CAPS with letter-spacing |
| **Plus Jakarta Sans** (Variable 200-800) | `--font-sans` | Navigation, body text, labels, badges | 12-18px |
| **IBM Plex Mono** (400, 500) | `--font-mono` | Data tables, confidence scores, code | Tabular numerals |

Editorial utility classes defined in `globals.css`:

| Class | Effect |
|-------|--------|
| `.editorial-display` | Instrument Serif, font-weight 400, tight leading |
| `.editorial-display-italic` | Same but italic |
| `.editorial-caps` | Uppercase, 0.15em letter-spacing, Plus Jakarta Sans 500 |
| `.data-mono` | IBM Plex Mono, tabular-nums |

### Confidence Gauge

The `ConfidenceGauge` component (`frontend/src/components/confidence/confidence-gauge.tsx`) renders an SVG arc meter:

- Three sizes: `sm` (48px), `md` (80px), `lg` (140px)
- 270-degree arc with mount animation (ease-out cubic, 800ms)
- Respects `prefers-reduced-motion` -- skips animation when set
- Uses `role="meter"` with `aria-valuenow`, `aria-valuemin`, `aria-valuemax` for accessibility
- Color from CSS custom properties via `getConfidenceCssVar()` helper

Tier logic from `frontend/src/lib/theme/confidence.ts`:

```typescript
export function getConfidenceTier(score: number): ConfidenceTier {
  if (score >= 0.85) return "high";    // green
  if (score >= 0.5) return "medium";   // amber
  return "low";                         // red
}
```

### Assurance Badge

The `AssuranceBadge` component (`frontend/src/components/works/assurance-badge.tsx`) displays a colored underline badge:

| Level | Label | Color |
|-------|-------|-------|
| `LEVEL_3` | A3 -- Artist Verified | Green |
| `LEVEL_2` | A2 -- Multi-Source | Blue |
| `LEVEL_1` | A1 -- Single Source | Amber |
| `LEVEL_0` | A0 -- No Data | Gray |

## Component Architecture

```
frontend/src/components/
├── attribution/
│   └── credit-list.tsx             # Credit rows with role, confidence, source tags
├── chat/
│   └── copilot-sidebar.tsx         # CopilotKit agent sidebar panel
├── citations/
│   ├── citation-overlay.tsx        # Expandable citation topic cards
│   ├── citation-ref.tsx            # Citation reference list
│   ├── inline-citation.tsx         # Inline [N] citation markers
│   └── provenance-panel.tsx        # Perplexity-style source overview
├── confidence/
│   ├── confidence-gauge.tsx        # SVG arc meter + badge variant
│   └── confidence-explanation.tsx  # Confidence score breakdown
├── editor/
│   └── credit-editor.tsx           # Inline credit editing
├── feedback/
│   ├── feedback-panel.tsx          # Structured feedback form
│   └── agent-feedback-flow.tsx     # Multi-step agent-guided feedback
├── layout/
│   ├── app-shell.tsx               # Root shell (sidebar + main + footer)
│   └── navigation.tsx              # Desktop sidebar + mobile hamburger
├── mcp/
│   └── mcp-query-mockup.tsx        # MCP permission query simulation
├── mode/
│   └── role-toggle.tsx             # Artist/Query role switch (A/Q)
├── notifications/
│   └── notification-badge.tsx      # Notification indicator
├── permissions/
│   ├── permission-matrix.tsx       # Permission grid (allow/deny/ask)
│   └── audit-log.tsx               # Permission change history
├── pro/
│   └── voice-agent-banner.tsx      # Voice agent upsell (Pro tier)
├── provenance/
│   └── provenance-timeline.tsx     # Vertical event timeline
├── review/
│   └── agent-review-queue.tsx      # Review queue with approve/batch actions
├── states/
│   ├── empty-state.tsx             # Illustrated empty states
│   ├── error-boundary.tsx          # Error boundary with retry
│   └── skeleton.tsx                # Shimmer skeleton loaders
├── theme/
│   ├── theme-provider.tsx          # Dark/light theme context
│   └── theme-toggle.tsx            # Theme switch button
├── ui/
│   └── adaptive-tooltip.tsx        # Proficiency-aware tooltips
└── works/
    ├── assurance-badge.tsx          # A0-A3 colored badge
    ├── source-tag.tsx              # Data source indicator
    └── work-card.tsx               # Work row in catalog list
```

### Custom Hooks

```
frontend/src/hooks/
├── use-attribution-context.ts    # Feeds selected work to CopilotKit via useCopilotReadable
├── use-agent-actions.ts          # Wires CopilotKit actions to UI (navigate, highlight, feedback)
└── use-feature-flags.ts          # Feature flag checks for progressive rollout
```

## State Management

State is managed with Jotai atoms in `frontend/src/lib/stores/`. Each store file exports related atoms:

### Theme Store (`stores/theme.ts`)

```typescript
themeAtom          // atom<"light" | "dark" | "system"> — user preference
resolvedThemeAtom  // derived — resolves "system" to actual light/dark
```

### Mode Store (`stores/mode.ts`)

```typescript
userRoleAtom       // atom<"artist" | "query"> — controls UI visibility
```

The role atom controls navigation visibility (Review page is artist-only) and the sidebar shows an A/Q toggle.

### Works Store (`stores/works.ts`)

```typescript
worksAtom          // atom<AttributionRecord[]> — loaded catalog
worksLoadingAtom   // atom<boolean> — loading state
selectedWorkAtom   // atom<AttributionRecord | null> — currently viewed
searchQueryAtom    // atom<string> — search filter text
sortFieldAtom      // atom<"confidence" | "title" | "updated">
sortDirectionAtom  // atom<"asc" | "desc">
filteredWorksAtom  // derived — filters + sorts worksAtom
```

### Proficiency Store (`stores/proficiency.ts`)

```typescript
proficiencyStateAtom   // atomWithStorage — persisted per-skill interaction counts
proficiencyLevelsAtom  // derived — novice/intermediate/expert per skill
overallProficiencyAtom // derived — max proficiency across skills
```

Proficiency levels drive adaptive UI: tooltips become less verbose as users gain experience. Levels are computed from interaction counts and success rates:

- **novice**: < 10 interactions
- **intermediate**: 10-50 interactions + 60% success rate
- **expert**: 50+ interactions + 75% success rate

### Type System

Frontend types in `frontend/src/lib/types/` mirror the Python Pydantic schemas:

```
frontend/src/lib/types/
├── index.ts           # Barrel export
├── enums.ts           # Source, AssuranceLevel, CreditRole, ProvenanceEventType
├── attribution.ts     # AttributionRecord, Credit, ConformalSet, ProvenanceEvent
├── permissions.ts     # PermissionBundle, PermissionRule, AuditLogEntry
├── feedback.ts        # FeedbackCard types
├── uncertainty.ts     # StepUncertainty, UncertaintyAwareProvenance
└── resolved.ts        # ResolvedEntity types
```

## Running the Frontend

```bash
# Development server on localhost:3000
make dev-frontend

# Run Vitest tests (265 tests)
make test-frontend

# ESLint + TypeScript checks
make lint-frontend

# Production build
make build-frontend

# Start both agent backend (port 8000) and frontend (port 3000)
make dev-agent
```

For the agent chat to work, the frontend needs the backend running. Set the API URL in `frontend/.env.local`:

```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Or start both together with `make dev-agent`.

## Testing

### Test Framework

Tests use Vitest with jsdom environment and React Testing Library. Configuration is in `frontend/vitest.config.ts`:

```typescript
export default defineConfig({
  plugins: [react()],
  resolve: { alias: { "@": resolve(__dirname, "./src") } },
  test: {
    environment: "jsdom",
    globals: true,
    setupFiles: ["./src/__tests__/setup.ts"],
    include: ["src/**/*.test.{ts,tsx}"],
    coverage: { provider: "v8", reporter: ["text", "html"] },
  },
});
```

### Test Coverage

265 Vitest tests covering:

- **Component rendering**: Confidence gauges, assurance badges, permission matrix, work cards
- **WCAG accessibility**: vitest-axe assertions on components (`role="meter"`, ARIA attributes, contrast)
- **State management**: Jotai atom behavior, derived atom computation, proficiency levels
- **Type validation**: Enum correctness, mock data consistency
- **Agent integration**: 11 tests for CopilotKit hooks and agent action wiring
- **CSS token lint**: Enforces zero hardcoded hex values and catches Tailwind v4 pitfalls

### Running Tests

```bash
# Run all tests once
cd frontend && npm test

# Watch mode
cd frontend && npm run test:watch

# With coverage report
cd frontend && npm run test:coverage

# End-to-end (Playwright)
cd frontend && npm run test:e2e
```

### Accessibility Testing

Two layers of accessibility testing:

1. **Component-level** (every test run): Vitest + vitest-axe for fast WCAG checks
2. **Browser-level** (E2E suite): Playwright + `@axe-core/playwright` for real rendering validation

Key accessibility patterns in the codebase:

- `ConfidenceGauge` uses `role="meter"` with full ARIA value attributes
- Navigation uses `aria-current="page"` for active route
- Mobile hamburger uses `aria-expanded` state
- All interactive elements have visible focus indicators
- `prefers-reduced-motion` is checked before any animation
