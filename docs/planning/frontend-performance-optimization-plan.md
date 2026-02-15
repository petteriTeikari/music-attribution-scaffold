# Frontend Performance Optimization Plan

> **Branch:** `fix/polish-ui-for-preprint-repo`
> **Date:** 2026-02-15
> **Status:** Investigation complete, ready for implementation
> **Symptom:** 16,917 modules, 13.5s initial compile, sluggish UI in dev mode

---

## Executive Summary

The frontend compiles **16,917 Webpack modules** on first load, taking 13.5s. The root causes fall into three categories:

| Category | Root Cause | Estimated Module Impact |
|----------|-----------|------------------------|
| **Bundle bloat** | PostHog pulls in @opentelemetry (42MB), CopilotKit eagerly loaded | ~9,000 modules (53%) |
| **Dev toolchain** | Webpack instead of Turbopack, no optimizePackageImports | ~2,000 modules (12%) |
| **Runtime perf** | SVG feTurbulence filter, 53 motion animations, unmemoized components | N/A (CPU/GPU bound) |

**Combined fix target: reduce modules from 16,917 to ~5,000-7,000 and eliminate runtime jank.**

---

## Part 1: Bundle Bloat (Dev Startup Speed)

### H1. PostHog OpenTelemetry Dependency Tree [CRITICAL]

**File:** `frontend/src/lib/analytics/posthog-provider.tsx:4`

```typescript
import posthog from "posthog-js";  // <-- Triggers 42MB @opentelemetry tree
```

**Impact:** posthog-js depends on `@opentelemetry/api`, `@opentelemetry/api-logs`, `@opentelemetry/exporter-logs-otlp-http`, `@opentelemetry/resources`, `@opentelemetry/sdk-logs` -- totaling 42MB and ~8,000-9,000 modules parsed by Webpack even though PostHog only initializes if `NEXT_PUBLIC_POSTHOG_KEY` is set.

**Fix:** Dynamic import PostHog on first use.

```typescript
"use client";

import { useEffect } from "react";

const POSTHOG_KEY = process.env.NEXT_PUBLIC_POSTHOG_KEY;
const POSTHOG_HOST = process.env.NEXT_PUBLIC_POSTHOG_HOST ?? "https://us.i.posthog.com";

let posthogPromise: Promise<typeof import("posthog-js")> | null = null;

function getPostHog() {
  if (!posthogPromise) {
    posthogPromise = import("posthog-js");
  }
  return posthogPromise;
}

export function PostHogProvider({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    if (!POSTHOG_KEY || typeof window === "undefined") return;
    getPostHog().then(({ default: posthog }) => {
      posthog.init(POSTHOG_KEY, {
        api_host: POSTHOG_HOST,
        person_profiles: "identified_only",
        capture_pageview: true,
        capture_pageleave: true,
      });
    });
  }, []);

  return <>{children}</>;
}

// Lazy export for consumers
export async function captureEvent(name: string, props?: Record<string, unknown>) {
  if (!POSTHOG_KEY) return;
  const { default: posthog } = await getPostHog();
  posthog.capture(name, props);
}
```

**Expected reduction:** 8,000-9,000 modules (50% of total).

---

### H2. CopilotKit Eagerly Loaded [HIGH]

**Files:**
- `frontend/src/lib/copilot/copilot-provider.tsx:1` -- imports `@copilotkit/react-core` (6.9MB, 190 files)
- `frontend/src/components/chat/copilot-sidebar.tsx:1` -- imports `@copilotkit/react-ui` (11MB, 160 files)

Both are imported at root layout level via `AppShell`, meaning the entire CopilotKit tree is parsed on every page even when `COPILOT_RUNTIME_URL` is not set.

**Fix:** Dynamic import CopilotKit.

```typescript
// copilot-provider.tsx
"use client";

import dynamic from "next/dynamic";
import { COPILOT_RUNTIME_URL } from "@/lib/config";

const CopilotKitLazy = dynamic(
  () => import("@copilotkit/react-core").then((mod) => ({ default: mod.CopilotKit })),
  { ssr: false }
);

export function CopilotProvider({ children }: { children: React.ReactNode }) {
  if (!COPILOT_RUNTIME_URL) {
    return <>{children}</>;
  }
  return <CopilotKitLazy runtimeUrl={COPILOT_RUNTIME_URL}>{children}</CopilotKitLazy>;
}
```

```typescript
// copilot-sidebar.tsx -- lazy load
import dynamic from "next/dynamic";

const AgentSidebar = dynamic(
  () => import("@/components/chat/copilot-sidebar"),
  { ssr: false, loading: () => null }
);
```

**Expected reduction:** 200-350 modules.

---

### H3. Missing optimizePackageImports [MEDIUM]

**File:** `frontend/next.config.ts`

Currently only `jotai` is optimized. Heavy packages are not listed.

**Fix:**

```typescript
experimental: {
  optimizePackageImports: [
    "jotai",
    "posthog-js",
    "@copilotkit/react-core",
    "@copilotkit/react-ui",
    "motion",
  ],
},
```

**Note:** When Turbopack is enabled (see H4), this optimization is applied automatically.

**Expected reduction:** 1,000-2,000 modules (Webpack mode only).

---

### H4. Webpack Instead of Turbopack [HIGH]

**File:** `frontend/package.json`

Currently: `"dev": "next dev"` (uses Webpack)

Turbopack is stable for development in Next.js 15.x with measured speedups of:
- Cold starts: up to 76.7% faster
- HMR/Fast Refresh: up to 96.3% faster
- Memory usage: 25-35% lower

**Fix:**

```json
"dev": "next dev --turbo"
```

**Expected improvement:** 2-5x faster initial compilation, near-instant HMR.

---

### H5. Multiple Jotai Instances [MEDIUM]

**Symptom:** Console warning: `"Detected multiple Jotai instances"`

**Cause:** No explicit Jotai `<Provider>` at root -- implicit global store gets duplicated between server and client in App Router.

**Fix:** Add explicit Jotai Provider.

```typescript
// frontend/src/lib/jotai-provider.tsx
"use client";

import { Provider } from "jotai";

export function JotaiProvider({ children }: { children: React.ReactNode }) {
  return <Provider>{children}</Provider>;
}
```

Wrap in `layout.tsx`:
```tsx
<JotaiProvider>
  <ThemeProvider>
    <AppShell>{children}</AppShell>
  </ThemeProvider>
</JotaiProvider>
```

---

## Part 2: Runtime Performance (UI Jank)

### H6. SVG feTurbulence Noise Overlay [CRITICAL]

**File:** `frontend/src/app/globals.css:230-240`

```css
body::before {
  content: "";
  position: fixed;
  inset: 0;
  z-index: 9999;
  pointer-events: none;
  opacity: 0.035;
  background-image: url("data:image/svg+xml,...feTurbulence...");
}
```

**Problem:** feTurbulence is CPU-rendered (not GPU-accelerated). Applied as a fixed pseudo-element covering the entire viewport, it recomputes on every scroll, animation, and repaint.

**Fix options (pick one):**

1. **Pre-render to a tiny tileable PNG** (recommended): Use [nnnoise](https://www.fffuel.co/nnnoise/) to generate a 256x256 noise tile PNG, replace the SVG data URI with `url('/noise.png')`. Eliminates runtime filter cost entirely.

2. **Add `will-change: opacity`** to the `::before` element to hint the browser to composite on a separate GPU layer.

3. **Disable in dev mode** with a CSS custom property toggle.

4. **Reduce numOctaves** from 4 to 2 (each octave doubles computation).

---

### H7. 53 Motion Animations with Intersection Observers [HIGH]

**File:** `frontend/src/app/page.tsx` (entire homepage)

The homepage has 53 `<motion.div>` elements with `whileInView` + `viewport={{ once: true }}`, each registering a separate IntersectionObserver.

**Fix:**

1. **Use LazyMotion** to reduce motion bundle from 34kB to 4.6kB:
```tsx
import { LazyMotion, domAnimation, m } from "motion/react";

<LazyMotion features={domAnimation}>
  <m.div animate={{ opacity: 1 }} />
</LazyMotion>
```

2. **Batch observers**: Group related animations under a single `whileInView` parent instead of per-element.

3. **Reduce animation count**: Many decorative animations (accent lines, dividers) can be CSS-only `@keyframes` without JS overhead.

---

### H8. Unmemoized Components in Lists [HIGH]

**Files and issues:**

| Component | File | Problem |
|-----------|------|---------|
| `ConfidenceGauge` | `confidence-gauge.tsx` | Not wrapped in `React.memo`. Every parent re-render restarts RAF animation loop. |
| `WorkCard` | `work-card.tsx:16-21` | Creates new `Set()` on every render to collect sources. |
| `CitationOverlay` | `citation-overlay.tsx` | Not memoized. Entire `CITATIONS` array (25+ items) passed as prop to each card. |
| `AgentReviewQueue` | `agent-review-queue.tsx:24-59` | `generateAgentSuggestions()` called in component body, not memoized. |

**Fix pattern:**

```typescript
// Wrap list-rendered components in React.memo
export const ConfidenceGauge = React.memo(function ConfidenceGauge({ ... }) {
  // ...
});

// Memoize expensive computations
const allSources = useMemo(() => {
  const set = new Set<Source>();
  for (const credit of work.credits) {
    for (const source of credit.sources) set.add(source);
  }
  return set;
}, [work.credits]);
```

---

### H9. Inline Style Objects Recreated Per Frame [MEDIUM]

**File:** `frontend/src/app/page.tsx:188-203`

```tsx
{Array.from({ length: 64 }).map((_, i) => (
  <div style={{
    width: 2,
    height: `${8 + Math.abs(Math.sin(i * 0.3)) * 24}px`,
    backgroundColor: i % 8 === 0 ? "var(--color-accent)" : "var(--color-border-strong)",
    opacity: 0.4 + Math.abs(Math.sin(i * 0.2)) * 0.6,
  }} />
))}
```

64 inline style objects created on every render. Math computed 64 times per frame.

**Fix:** Move to CSS classes or memoize the array outside the render function.

---

### H10. filteredWorksAtom Creates New Arrays [MEDIUM]

**File:** `frontend/src/lib/stores/works.ts:16-52`

The derived atom creates new arrays via `.filter()` and `[...spread].sort()` on every subscription update, even when underlying data hasn't changed.

**Fix:** This is inherent to Jotai's derived atoms -- ensure consumer components use `React.memo` or `useMemo` to avoid re-renders when the derived array is referentially equal.

---

### H11. Sticky Images Without CSS Containment [LOW]

**File:** `frontend/src/app/page.tsx:332-342`

`sticky top-8` on large images (600x1200) without `contain: layout` forces layout recalculation on every scroll.

**Fix:** Add `contain: layout` or `content-visibility: auto` to sticky image containers.

---

## Part 3: Dev Toolchain & CI

### H12. React Compiler (Auto-Memoization) [HIGH VALUE, LOW RISK]

React Compiler v1.0 (Oct 2025) automatically memoizes components and hooks at build time. Measured 25-40% reduction in unnecessary re-renders.

**Fix:**

```bash
cd frontend && npm install babel-plugin-react-compiler
```

```typescript
// next.config.ts
const nextConfig: NextConfig = {
  reactCompiler: true,
  // ...
};
```

**Caveat:** Test thoroughly with CopilotKit and Jotai hooks. Use opt-in mode (`compilationMode: "annotation"`) for gradual rollout.

---

### H13. CodSpeed Performance Benchmarks in CI

Track rendering performance regressions per PR using CodSpeed + Vitest benchmarks.

```bash
cd frontend && npm install -D @codspeed/vitest-plugin
```

```typescript
// vitest.config.ts
import codspeedPlugin from "@codspeed/vitest-plugin";

export default defineConfig({
  plugins: [codspeedPlugin()],
  test: {
    benchmark: { include: ["**/*.bench.{ts,tsx}"] },
  },
});
```

Benchmark files:
- `ConfidenceGauge` render time
- `WorkCard` list render with 10, 50, 100 items
- `filteredWorksAtom` sort/filter with 1000 works
- Homepage initial render

---

### H14. Grafana Frontend Observability

**Existing:** Grafana + Prometheus monitoring via `--profile monitoring` in docker-compose. Dashboard tracks API latency, confidence distribution, drift detection.

**Missing:** Frontend Web Vitals (LCP, CLS, INP, TTFB) are not collected.

**Option A: Grafana Faro Web SDK** (open source RUM)

```bash
cd frontend && npm install @grafana/faro-web-sdk
```

Sends Web Vitals + JS errors + user sessions to Grafana Cloud or self-hosted collector.

**Option B: PostHog Web Vitals** (already configured)

PostHog captures `web-vitals` automatically (it's a dependency of posthog-js). If PostHog is configured, LCP/CLS/INP are already being sent. Dashboard available in PostHog UI.

**Option C: Sentry** (via `@sentry/nextjs`)

Route-level Web Vitals tracking, automatic transaction tracing, dedicated performance dashboard.

**Recommendation for Grafana dashboard enhancement:**

Add frontend panels to existing `attribution-overview.json`:
- Web Vitals p50/p95 per route (LCP, INP, CLS, TTFB)
- JavaScript error rate
- Client-side API call latency (fetch to backend)

This requires either Faro SDK or a custom `/metrics` push from the frontend.

---

## Part 4: Infrastructure Performance

### H15. Frontend Uses Mock Data (No DB Bottleneck in Dev)

The frontend runs `make dev-frontend` which starts Next.js without a backend. When the FastAPI backend is not running, the API client falls back to **mock data** with simulated 200-500ms latency.

**Conclusion:** The sluggishness observed is NOT caused by database or network latency -- it is entirely bundle compilation and runtime rendering overhead.

### H16. PostgreSQL Performance (When Backend Is Running)

When running full stack (`make dev`):
- PostgreSQL has PgBouncer connection pooling (5-20 pool size)
- Prometheus scrapes `/metrics` every 15s
- Grafana dashboard shows latency p50/p95/p99

**No action needed for MVP** -- the backend is not the bottleneck.

---

## Implementation Priority

| # | Fix | Files Changed | Effort | Impact | Risk |
|---|-----|--------------|--------|--------|------|
| 1 | Enable Turbopack (`--turbo`) | `package.json` | 1 min | 2-5x faster dev startup | Low |
| 2 | Dynamic import PostHog | `posthog-provider.tsx`, `events.ts` | 20 min | -8,000 modules | Low |
| 3 | Add Jotai Provider | `jotai-provider.tsx`, `layout.tsx` | 10 min | Fixes state sync | Low |
| 4 | Replace feTurbulence with PNG | `globals.css`, `public/noise.png` | 30 min | Eliminates CPU filter | Low |
| 5 | Dynamic import CopilotKit | `copilot-provider.tsx`, `app-shell.tsx` | 20 min | -350 modules | Low |
| 6 | Expand optimizePackageImports | `next.config.ts` | 5 min | -1,000 modules (Webpack) | None |
| 7 | Memoize list components | `confidence-gauge.tsx`, `work-card.tsx`, `citation-overlay.tsx` | 30 min | Fewer re-renders | Low |
| 8 | LazyMotion for animations | `page.tsx` | 30 min | -30kB bundle | Medium |
| 9 | React Compiler | `next.config.ts`, `package.json` | 15 min | 25-40% fewer re-renders | Medium |
| 10 | CodSpeed benchmarks in CI | `vitest.config.ts`, `.github/`, bench files | 1 hr | Regression detection | None |
| 11 | Grafana Faro Web Vitals | `faro-provider.tsx`, `layout.tsx` | 2 hr | Production RUM | Low |

**Quick wins (items 1-6):** Implementable in under 2 hours, reduce dev startup from 13.5s to ~3-5s.

---

## Dependency Audit

| Package | Disk Size | Module Count | Used In | Lazy-Loadable? |
|---------|-----------|-------------|---------|----------------|
| `next` | 155 MB | 3,181 | Framework | No (core) |
| `@opentelemetry/*` | 42 MB | ~800 | PostHog transitive | Yes (via PostHog lazy) |
| `posthog-js` | 30 MB | 175 | Analytics | Yes (dynamic import) |
| `@copilotkit/react-ui` | 11 MB | 160 | Agent sidebar | Yes (next/dynamic) |
| `@copilotkit/react-core` | 6.9 MB | 190 | Agent provider | Yes (next/dynamic) |
| `react-dom` | 7.2 MB | 40 | Framework | No (core) |
| `jotai` | 1.3 MB | 60 | State management | No (lightweight) |
| `motion` | 720 KB | 16 | Animations | Partially (LazyMotion) |

---

## Verification

After implementing fixes 1-6:

```bash
# Dev startup time
time make dev-frontend
# Should drop from 13.5s to ~3-5s first compile

# Module count (check Next.js output)
# Target: < 7,000 modules

# Jotai warning should be gone
# No "Detected multiple Jotai instances" in console

# Web Vitals (Chrome DevTools > Lighthouse)
# LCP: < 2.5s
# CLS: < 0.1
# INP: < 200ms
```

---

## References

- [Turbopack Dev is Stable](https://nextjs.org/blog/turbopack-for-development-stable)
- [Next.js optimizePackageImports](https://nextjs.org/docs/app/api-reference/config/next-config-js/optimizePackageImports)
- [Jotai Next.js Guide](https://jotai.org/docs/guides/nextjs)
- [React Compiler v1.0](https://react.dev/blog/2025/10/07/react-compiler-1)
- [Motion Reduce Bundle Size](https://motion.dev/docs/react-reduce-bundle-size)
- [CodSpeed Vitest Plugin](https://codspeed.io/docs/benchmarks/nodejs/vitest)
- [Grafana Faro Web SDK](https://grafana.com/oss/faro/)
- [Sentry Frontend Performance](https://blog.sentry.io/frontend-javascript-performance-testing/)
- [nnnoise SVG Generator](https://www.fffuel.co/nnnoise/)
- [PostHog Bundle Size Discussion](https://github.com/PostHog/posthog-js/issues/1905)
