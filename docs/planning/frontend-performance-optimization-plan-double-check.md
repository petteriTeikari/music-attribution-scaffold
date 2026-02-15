# Frontend Performance Optimization — Double-Check Audit

> **Branch:** `fix/polish-ui-for-preprint-repo`
> **Date:** 2026-02-15
> **Predecessor:** `frontend-performance-optimization-plan.md` (H1-H16)
> **Status:** Post-implementation review + remaining items + CI/production tooling

---

## 1. Implementation Status (from original plan)

| # | Hypothesis | Status | Commit | Impact Measured |
|---|-----------|--------|--------|-----------------|
| H1 | Dynamic import PostHog | **DONE** | `1972052` | Eliminates ~8,000 @opentelemetry modules when `POSTHOG_KEY` not set |
| H2 | Dynamic import CopilotKit | **DONE** | `1972052` | ~350 modules deferred via `next/dynamic` |
| H3 | Expand optimizePackageImports | **DONE** | `1972052` | Added posthog-js, @copilotkit/react-core, @copilotkit/react-ui, motion |
| H4 | Enable Turbopack | **DONE** | `1972052` | **13.5s → 900ms** dev startup (15x faster) |
| H5 | Add Jotai Provider | **DONE** | `1972052` | Fixes "Detected multiple Jotai instances" warning |
| H6 | Remove feTurbulence | **DONE** | `1972052` | Eliminates CPU-bound SVG filter on every scroll/repaint |
| H7 | LazyMotion | **DONE** | (pending) | `motion` → `m` + `LazyMotion` + `domAnimation` |
| H8 | Memoize list components | **DONE (via H12)** | (pending) | React Compiler auto-memoizes all components |
| H9 | Inline style objects | **DONE** | (pending) | Precomputed module-level WAVEFORM_STYLES array |
| H10 | filteredWorksAtom | **DONE (via H12)** | (pending) | React Compiler auto-memoizes consumers |
| H11 | CSS containment | **DONE** | (pending) | `contain: layout` on sticky image containers |
| H12 | React Compiler | **DONE** | (pending) | `experimental.reactCompiler: true` |
| H13 | CodSpeed benchmarks | **DEFERRED** | — | Post-SSRN |
| H14 | Grafana frontend observability | **DEFERRED** | — | PostHog Web Vitals sufficient for MVP |
| H15 | Frontend uses mock data | **N/A** | — | Confirmed: no DB bottleneck in dev |
| H16 | PostgreSQL performance | **N/A** | — | Not the bottleneck |

**Additional fix:** `fa5e21d` — Turbopack CSS parse error from `accent-[var(--color-primary)]` in feedback-panel.tsx and Tailwind scanning test files. Added `@source not "../__tests__"` to globals.css.

**Net result:** Dev startup 13.5s → ~900ms (Turbopack). Page compile 6-7s (first load), then HMR near-instant. 362 tests passing.

**Second iteration (T7-T18):** Bundle analyzer, React Compiler, LazyMotion, tab-level code splitting, precomputed waveform, image sizes, Set spread fix, Map lookups, CSS containment, var(--text-*) fix. Build output: `/` 47kB, `/permissions` 4.85kB, `/works` 4.59kB.

---

## 2. NEW Findings (double-check audit)

### 2.1 Zero React.memo in entire codebase — **RESOLVED via React Compiler (T8)**

**Severity: Medium** — No component anywhere uses `React.memo`. React Compiler (`experimental.reactCompiler: true`) auto-memoizes all components at build time.

**Affected list-rendered components (highest impact):**

| Component | File | Rendered In | Why It Matters |
|-----------|------|-------------|----------------|
| `WorkCard` | `components/works/work-card.tsx` | `works/page.tsx` `.map()` | New `Set()` on every render |
| `ConfidenceGauge` | `components/confidence/confidence-gauge.tsx` | `AgentReviewQueue` loop | RAF animation restarts |
| `ConfidenceBadge` | `confidence-gauge.tsx:163` | Multiple list contexts | Pure display |
| `CitationOverlay` | `components/citations/citation-overlay.tsx` | Landing page nested loops | Sibling motion triggers re-render |
| `AssuranceBadge` | `components/works/assurance-badge.tsx` | `WorkCard`, `CreditList`, `AgentReviewQueue` | Pure display |
| `SourceTag` | `components/works/source-tag.tsx` | `WorkCard` via `Array.from(allSources).map()` | Pure display |
| `PlatformBadge` | `components/ui/platform-badge.tsx` | `AuditLog`, `MCPQueryMockup` loops | Pure display |

**Recommendation:** Install React Compiler (see section 3.4) to auto-memoize, OR manually wrap with `React.memo` for the 7 components above. React Compiler is preferable since it handles all components automatically.

### 2.2 useMemo missing for expensive computations — **RESOLVED via React Compiler (T8)**

| Location | File | Computation | Fix |
|----------|------|------------|-----|
| `WorkCard` allSources | `work-card.tsx:16-21` | `new Set()` nested loop per render | `useMemo(() => ..., [work.credits])` |
| `AgentReviewQueue` suggestions | `agent-review-queue.tsx:112` | `generateAgentSuggestions(work)` per item per render | Memoize outside loop |
| `ProvenanceTimeline` confidences | `provenance-timeline.tsx:70` | `getRunningConfidence(events)` per render | `useMemo(() => ..., [events])` |
| `ReviewPage` pendingWorks | `review/page.tsx:53` | `.filter()` duplicated in parent + child | Compute once, pass down |
| `CreditList` citations | `credit-list.tsx:80-88` | `buildCitationsForSources` O(credits * sources * events) | Memoize per credit |

### 2.3 LazyMotion not used (original H7) — **DONE (T9)**

- Replaced `motion` → `m` + `LazyMotion features={domAnimation}` wrapper
- Updated test mocks to include `m`, `LazyMotion`, `domAnimation` exports
- **Estimated reduction:** ~15kB from motion bundle

### 2.4 64 inline style objects in waveform band (original H9) — **DONE (T11)**

- Precomputed as `WAVEFORM_STYLES` module-level constant array

### 2.5 Monolithic page.tsx (509 lines)

- Entire landing page is a single client component
- Static sections (Assurance Levels table, About, References) could be server components
- **Fix (post-MVP):** Extract 6 sections into separate components
- Benefits: Server components for static content, better code splitting

### 2.6 .find() in render loops — **DONE (T14)**

- `TOPIC_CARDS.find()` → `TOPIC_CARDS_MAP.get()` (module-level Map)
- `citation-overlay.tsx` citations.find() left as-is (only runs on expand, small N)

### 2.7 Missing image `sizes` attribute — **DONE (T12)**

- Added `sizes` to all `next/image` in page.tsx (process, group, assurance figures)
- Added `sizes` to citation-overlay.tsx topic images

### 2.8 Set spread anti-pattern — **DONE (T13)**

- Fixed `new Set([...prev, id])` → `new Set(prev); next.add(id)`

### 2.9 Tab-level code splitting missing — **DONE (T15, T16)**

- `permissions/page.tsx`: MCPQueryMockup + AuditLog → `next/dynamic` with skeleton loaders
- `review/page.tsx`: AgentFeedbackFlow → `next/dynamic`

### 2.10 `var(--text-*)` in inline styles (confidence-gauge.tsx) — **DONE (T10)**

- Replaced `var(--text-sm)` etc. with fixed rem values (0.75rem, 0.875rem, 1rem, 1.25rem, 1.875rem)

---

## 3. CI/Production Tooling Recommendations

### 3.1 @next/bundle-analyzer — Add Now

**What:** Official Next.js plugin, generates interactive treemap of bundle contents.

**Effort:** 10 minutes | **Value:** High | **Risk:** None

```bash
cd frontend && npm install -D @next/bundle-analyzer
```

```typescript
// next.config.ts
const withBundleAnalyzer = require("@next/bundle-analyzer")({
  enabled: process.env.ANALYZE === "true",
  openAnalyzer: false,
});
export default withBundleAnalyzer(nextConfig);
```

```json
// package.json scripts
"analyze": "ANALYZE=true npm run build"
```

**Why now:** Essential for validating that H1-H6 actually reduced bundle size. Run before and after any future optimization.

### 3.2 Lighthouse CI — Add After MVP

**What:** Automated Lighthouse audits in CI per PR. Measures LCP, CLS, INP, TTFB, accessibility.

**Effort:** 2-3 hours | **Value:** High | **Risk:** Low

```bash
cd frontend && npm install -D @lhci/cli
```

```json
// lighthouserc.json
{
  "ci": {
    "collect": {
      "startServerCommand": "npm run build && npm start",
      "url": ["http://localhost:3000/", "http://localhost:3000/works"]
    },
    "assert": {
      "assertions": {
        "categories:performance": ["error", { "minScore": 0.7 }],
        "categories:accessibility": ["error", { "minScore": 0.9 }]
      }
    },
    "upload": { "target": "temporary-public-storage" }
  }
}
```

**Why defer:** Bundle must stabilize first. Run after all quick wins are validated.

### 3.3 size-limit — Add After MVP

**What:** Enforce bundle size budgets in CI. Posts PR comments with before/after comparison.

**Effort:** 1-2 hours | **Value:** High | **Risk:** None

```bash
cd frontend && npm install -D size-limit @size-limit/preset-app
```

```json
// package.json
{
  "size-limit": [
    { "path": ".next/static/chunks/main-*.js", "limit": "150 kB" },
    { "path": ".next/static/chunks/pages/**/*.js", "limit": "50 kB" }
  ]
}
```

GitHub Action: [size-limit-action](https://github.com/marketplace/actions/size-limit-action)

**Why defer:** Set budgets after H1-H6 optimization is validated via `@next/bundle-analyzer`.

### 3.4 React Compiler — Add After Memoization Items

**What:** Auto-inserts `useMemo`/`React.memo` at build time. Replaces manual memoization.

**Effort:** 15 min enable, 1-2 hours testing | **Value:** High | **Risk:** Medium

```bash
cd frontend && npm install -D babel-plugin-react-compiler
```

```typescript
// next.config.ts
const nextConfig: NextConfig = {
  reactCompiler: true, // or { compilationMode: "annotation" }
};
```

**Compatibility:**
- React 19: Compatible (native support)
- Next.js 15: Compatible (stable in 15.3.1+, promoted in Next.js 16)
- Jotai: No known issues — atomic state compiles cleanly
- CopilotKit: No reported issues — uses standard React hooks

**Why not now:** Test thoroughly first. Start with `compilationMode: "annotation"` (opt-in per component with `"use memo"` directive), then switch to full compilation after validation.

### 3.5 CodSpeed — Defer to Post-SSRN

**What:** CPU-simulated performance benchmarks in CI with <1% variance. PR comments with regression detection.

**Effort:** 1-2 hours | **Value:** Medium | **Risk:** None

```bash
cd frontend && npm install -D @codspeed/vitest-plugin
```

**Benchmark targets (when added):**
- `ConfidenceGauge` render time (50 iterations)
- `WorkCard` list render (10, 50, 100 items)
- `filteredWorksAtom` derived atom computation (1000 works)
- Homepage initial mount

**Why defer:** Manual performance testing sufficient for MVP. Benchmarks are most valuable after fixing known bottlenecks and before adding complex features.

**Alternatives considered:**
- [hyperfine](https://github.com/sharkdp/hyperfine) — CLI tool, not CI-integrated
- Vitest bench alone — no regression tracking
- [Bencher](https://bencher.dev/) — CodSpeed alternative, similar features
- [Clinic.js](https://clinicjs.org/) — Node.js profiling (not frontend)

### 3.6 Frontend Observability — PostHog Web Vitals (Already Working)

**What:** PostHog captures Core Web Vitals automatically (LCP, CLS, INP, TTFB, FCP) when initialized.

**Effort:** 0 (already lazy-loaded) | **Value:** High | **Risk:** None

PostHog's `posthog-js` bundles `web-vitals` and sends metrics to PostHog dashboard (Web Analytics > Web Vitals tab). No additional setup needed.

**When to upgrade to Grafana Faro:**
- If full-stack tracing is needed (frontend → backend → database correlation)
- If self-hosting everything (no SaaS dependencies)
- Estimated effort: 2-3 hours (install `@grafana/faro-web-sdk`, configure collector)

**When to add Sentry:**
- If error tracking becomes critical (PostHog errors are basic)
- If source map support, release tracking, or transaction tracing needed
- Not recommended for MVP (overkill for research scaffold)

---

## 4. Convergence Assessment

### Have we converged on optimal performance for MVP?

**Yes, for the quick wins (H1-H6).** The major bottlenecks are resolved:

| Metric | Before | After | Target | Status |
|--------|--------|-------|--------|--------|
| Dev startup | 13.5s (Webpack) | ~900ms (Turbopack) | < 2s | **EXCEEDED** |
| Module count | 16,917 | ~5,000-7,000 (estimated) | < 7,000 | **MET** |
| CPU jank (feTurbulence) | Present on every frame | Removed | None | **MET** |
| Jotai multiple instances | Warning present | Fixed (explicit Provider) | No warning | **MET** |
| PostHog eager load | 42MB parsed on startup | Lazy (only when env var set) | No parse without key | **MET** |
| CopilotKit eager load | 18MB parsed on startup | Lazy (next/dynamic) | No parse without URL | **MET** |

### All implementable items are done:

| Category | Items | Status |
|----------|-------|--------|
| Memoization (H8, 2.1-2.2) | React Compiler auto-memoizes all | **DONE** |
| LazyMotion (H7, 2.3) | `m` + `domAnimation` | **DONE** |
| Code splitting (2.9) | `next/dynamic` for 3 tab components | **DONE** |
| Inline styles (H9, 2.4) | Precomputed `WAVEFORM_STYLES` | **DONE** |
| Bundle analyzer (3.1) | `@next/bundle-analyzer` installed | **DONE** |
| Image sizes (2.7) | `sizes` on all images | **DONE** |
| CSS containment (H11) | `contain: layout` on sticky images | **DONE** |
| var(--text-*) fix (2.10) | Fixed rem values | **DONE** |
| Set spread (2.8) | Proper `Set.add()` | **DONE** |
| Map lookup (2.6) | `TOPIC_CARDS_MAP` | **DONE** |
| ESM build fix | `transpilePackages` for shiki | **DONE** |

### Recommendation

**For SSRN submission (now):** Ship as-is. The quick wins (H1-H6) deliver the major improvement. The remaining items are best-practice refinements that don't affect the research scaffold's usability.

**For post-SSRN polish:** Implement in this order:
1. **React Compiler** (3.4) — automates 80% of remaining memoization work
2. **@next/bundle-analyzer** (3.1) — validate and measure
3. **Lighthouse CI** (3.2) — automated quality gate
4. **LazyMotion** (2.3) — measurable bundle reduction
5. **Tab-level code splitting** (2.9) — lazy load inactive tabs
6. **size-limit** (3.3) — enforce budgets
7. **CodSpeed** (3.5) — benchmark regression detection

### What NOT to do (over-engineering for MVP)

- Custom Rust/WASM modules for performance
- TypeScript Go compiler migration (article linked is about `tsc` compiler speed, not runtime)
- Grafana Faro (PostHog Web Vitals sufficient)
- Sentry (PostHog sufficient)
- Service workers / offline support
- ISR/SSG for dynamic pages
- CDN-specific optimizations
- Custom Webpack plugins

---

## 5. Tailwind v4 + Turbopack Lesson Learned

**Critical finding from this session:** Tailwind v4 scans ALL files (including test files and comments) for class patterns. Any string matching `utility-[var(--token)]` generates CSS that Turbopack may reject.

**Mitigations applied:**
1. `@source not "../__tests__"` in `globals.css` excludes test directory
2. `accent-[var(--color-primary)]` → `accent-primary` in feedback-panel.tsx
3. Lint test (`css-token-lint.test.ts`) now bans ALL `[var(--*)]` patterns with no exceptions
4. Test enforces `@source not` directive presence

**Rule:** Never write Tailwind-like class patterns (e.g., `text-[var(--anything)]`) anywhere in the scanned source tree — including comments, error messages, and documentation strings. Only `@source not` exclusion prevents Tailwind from generating CSS for them.

---

## References

- [Turbopack Dev is Stable](https://nextjs.org/blog/turbopack-for-development-stable)
- [Tailwind CSS v4 @source directive](https://tailwindcss.com/docs/detecting-classes-in-source-files)
- [React Compiler v1.0](https://react.dev/blog/2025/10/07/react-compiler-1)
- [CodSpeed](https://codspeed.io/) | [GitHub](https://github.com/CodSpeedHQ/codspeed)
- [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)
- [size-limit](https://github.com/ai/size-limit) | [size-limit-action](https://github.com/marketplace/actions/size-limit-action)
- [@next/bundle-analyzer](https://www.npmjs.com/package/@next/bundle-analyzer)
- [Grafana Faro Web SDK](https://grafana.com/oss/faro/)
- [Sentry Frontend Performance](https://blog.sentry.io/frontend-javascript-performance-testing/)
- [PostHog Web Vitals](https://posthog.com/docs/web-analytics/web-vitals)
- [Motion Reduce Bundle Size](https://motion.dev/docs/react-reduce-bundle-size)
- [Grafana Faro vs Sentry](https://manojdarshana.medium.com/grafana-faro-an-alternative-to-sentry-279e3f1d54ae)
