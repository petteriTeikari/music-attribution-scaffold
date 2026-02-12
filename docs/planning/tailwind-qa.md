# Tailwind v4 Anti-Pattern QA — Systematic Fix

**Branch**: `fix/tailwind-qa`
**Closes**: #47
**Skill**: `self-learning-iterative-coder`

## Problem

Tailwind CSS v4 cannot disambiguate arbitrary value syntax `[var(--*)]` as color vs font-size vs spacing. The codebase has **~387 instances** across **24+ component files** using `[var(--*)]` instead of native Tailwind utility classes.

This is not just a style issue — `text-[var(--color-heading)]` can silently generate `font-size` instead of `color` in Tailwind v4.

## Root Cause

The `@theme` block in `globals.css` registers color tokens as Tailwind utilities, but component authors used the verbose `[var(--*)]` syntax anyway. Spacing, radius, and transition tokens were **never registered** in `@theme` — but they map 1:1 to Tailwind's built-in scale, so `@theme` registration is unnecessary.

## Anti-Pattern Categories & Fix Strategy

| Category | Count | Anti-Pattern Example | Correct Utility | Strategy |
|----------|-------|---------------------|-----------------|----------|
| **Spacing** | ~215 | `px-[var(--space-8)]` | `px-8` | Direct replacement — Tailwind built-in scale matches exactly |
| **Text colors** | ~95 | `text-[var(--color-heading)]` | `text-heading` | Direct replacement — already in `@theme` |
| **Background colors** | ~35 | `bg-[var(--color-surface)]` | `bg-surface` | Direct replacement — already in `@theme` |
| **Border colors** | ~30 | `border-[var(--color-border)]` | `border-border` | Direct replacement — already in `@theme` |
| **Border radius** | ~20 | `rounded-[var(--radius-md)]` | `rounded-md` | Direct replacement — Tailwind built-in |
| **Transitions** | ~15 | `duration-[var(--transition-fast)]` | `duration-150` | Direct replacement — Tailwind built-in |
| **Shadows** | ~3 | `shadow-[var(--shadow-md)]` | `shadow-md` | Add to `@theme` or use Tailwind built-in |
| **Hover/focus states** | ~20 | `hover:text-[var(--color-accent)]` | `hover:text-accent` | Same as base pattern with prefix |
| **Sidebar color** | 1 | `bg-[var(--color-sidebar)]` | `bg-sidebar` | Add `--color-sidebar` to `@theme` |
| **Divide colors** | ~3 | `divide-[var(--color-border)]` | `divide-border` | Already in `@theme` via border |
| **Decoration colors** | ~5 | `decoration-[var(--color-accent)]` | `decoration-accent` | Already in `@theme` |
| **Ring colors** | ~2 | `ring-[var(--color-accent)]` | `ring-accent` | Already in `@theme` |
| **Placeholder colors** | ~3 | `placeholder:text-[var(--color-muted)]` | `placeholder:text-muted` | Already in `@theme` |

## Spacing Token Mapping

| Custom Property | Value | Tailwind Built-in |
|----------------|-------|-------------------|
| `--space-1` | 4px | `1` (0.25rem = 4px) |
| `--space-2` | 8px | `2` (0.5rem = 8px) |
| `--space-3` | 12px | `3` (0.75rem = 12px) |
| `--space-4` | 16px | `4` (1rem = 16px) |
| `--space-5` | 20px | `5` (1.25rem = 20px) |
| `--space-6` | 24px | `6` (1.5rem = 24px) |
| `--space-8` | 32px | `8` (2rem = 32px) |
| `--space-10` | 40px | `10` (2.5rem = 40px) |
| `--space-12` | 48px | `12` (3rem = 48px) |
| `--space-16` | 64px | `16` (4rem = 64px) |
| `--space-20` | 80px | `20` (5rem = 80px) |
| `--space-24` | 96px | `24` (6rem = 96px) |

Note: px vs rem difference is cosmetic — these values are identical at default 16px root font-size.

## Radius Mapping

| Custom Property | Value | Tailwind Built-in |
|----------------|-------|-------------------|
| `--radius-sm` | 4px | `rounded` (0.25rem) |
| `--radius-md` | 8px | `rounded-md` (0.375rem) — close but NOT exact (6px vs 8px) |
| `--radius-lg` | 12px | `rounded-lg` (0.5rem) — close but NOT exact (8px vs 12px) |
| `--radius-xl` | 16px | `rounded-xl` (0.75rem) — NOT exact (12px vs 16px) |
| `--radius-full` | 9999px | `rounded-full` (exact match) |

**Decision**: Radius values don't map cleanly. Register in `@theme` instead:
```css
@theme {
  --radius-sm: var(--radius-sm);
  --radius-md: var(--radius-md);
  --radius-lg: var(--radius-lg);
  --radius-xl: var(--radius-xl);
}
```

## Shadow Mapping

Tailwind v4 built-in shadows don't match our custom values (ours use `rgba(30, 58, 95, ...)` tint). Register in `@theme`:
```css
@theme {
  --shadow-sm: var(--shadow-sm);
  --shadow-md: var(--shadow-md);
  --shadow-lg: var(--shadow-lg);
  --shadow-xl: var(--shadow-xl);
}
```

## Transition Mapping

| Custom Property | Value | Tailwind Built-in |
|----------------|-------|-------------------|
| `--transition-fast` | 150ms ease | `duration-150` |
| `--transition-base` | 200ms ease | `duration-200` |
| `--transition-slow` | 300ms ease | `duration-300` |

Note: `duration-*` only sets duration, not easing. Ensure `ease` is default or add `transition-ease` class.

## Plan (7 Tasks, 3 Phases)

### Phase 0: Expand @theme & Strengthen Lint

**Task 0.1: Expand @theme block with missing tokens**
- Add `--color-sidebar` to `@theme` (1 usage in navigation.tsx)
- Add `--radius-sm`, `--radius-md`, `--radius-lg`, `--radius-xl` to `@theme`
- Add `--shadow-sm`, `--shadow-md`, `--shadow-lg`, `--shadow-xl` to `@theme`
- Files: `frontend/src/app/globals.css`
- TDD: Verify build still works, new utilities generate correctly

**Task 0.2: Strengthen css-token-lint test**
- Extend lint test to catch ALL `[var(--` patterns in .tsx files
- Hard error on ANY `[var(--` in className strings (not just `text-[var(--text-*)]`)
- Keep existing tests, add comprehensive pattern detection
- Files: `frontend/src/__tests__/css-token-lint.test.ts`
- TDD: Test must FAIL against current codebase (proves detection works), then pass after fixes

### Phase 1: Systematic Replacement (by category)

**Task 1.1: Replace all spacing anti-patterns (~215 instances)**
- `{prefix}-[var(--space-N)]` → `{prefix}-N` for all spacing utilities
- Prefixes: `p`, `px`, `py`, `pt`, `pb`, `pl`, `pr`, `m`, `mx`, `my`, `mt`, `mb`, `ml`, `mr`, `gap`, `space-x`, `space-y`, `top`, `right`, `bottom`, `left`
- Files: all 24 component files
- TDD: Run lint test to verify count decreases to 0 for spacing patterns

**Task 1.2: Replace all color anti-patterns (~165 instances)**
- `text-[var(--color-X)]` → `text-X`
- `bg-[var(--color-X)]` → `bg-X`
- `border-[var(--color-X)]` → `border-X`
- `divide-[var(--color-X)]` → `divide-X`
- `decoration-[var(--color-X)]` → `decoration-X`
- `ring-[var(--color-X)]` → `ring-X`
- `placeholder:text-[var(--color-X)]` → `placeholder:text-X`
- `accent-[var(--color-X)]` → TBD (CSS accent-color)
- Also handle hover/focus variants: `hover:text-[var(--color-X)]` → `hover:text-X`
- Files: all 24 component files
- TDD: Run lint test to verify 0 color pattern violations

**Task 1.3: Replace radius, transition, and shadow anti-patterns (~38 instances)**
- `rounded-[var(--radius-X)]` → `rounded-X` (using @theme registered tokens)
- `duration-[var(--transition-fast)]` → `duration-150`
- `duration-[var(--transition-base)]` → `duration-200`
- `duration-[var(--transition-slow)]` → `duration-300`
- `shadow-[var(--shadow-X)]` → `shadow-X` (using @theme registered tokens)
- Files: affected component files
- TDD: Run lint test to verify 0 remaining violations

### Phase 2: Verification

**Task 2.1: Final verification — zero violations**
- Run `grep -r "\[var(--" frontend/src --include="*.tsx" | wc -l` → must be 0
- Run css-token-lint test → must pass
- Run full frontend test suite → all 273+ tests pass
- Run `npm run build` → production build succeeds
- Visual spot-check: ensure no style regressions (colors, spacing, radius look correct)
- Files: none (verification only)

## Dependency DAG

```
0.1 (@theme expand) ──┐
0.2 (lint test)  ─────┤
                       │
1.1 (spacing)    ◄─── 0.1
1.2 (colors)     ◄─── 0.1
1.3 (radius/transition/shadow) ◄── 0.1
                       │
2.1 (verification) ◄── 1.1, 1.2, 1.3, 0.2
```

## Key Risks

| Risk | Mitigation |
|------|-----------|
| Spacing px→rem shift | Tailwind uses rem but our --space-* used px. At 16px root, 1rem=16px=--space-4. Values match exactly. |
| Radius mismatch | Register custom values in @theme instead of using Tailwind built-ins |
| Shadow mismatch | Register custom values in @theme instead of using Tailwind built-ins |
| `accent-[var(--color-X)]` (CSS accent-color) | This is a valid use of arbitrary values — may need to keep as-is |
| Inline `style={{ color: "var(--color-X)" }}` | These are NOT Tailwind classes — leave as-is, they work fine |
| Dark mode regression | All tokens already have dark mode variants in `.dark` class — no change needed |

## Verification Commands

```bash
# Count remaining violations (target: 0)
grep -r "\[var(--" frontend/src --include="*.tsx" | wc -l

# Lint test
cd frontend && npx vitest run src/__tests__/css-token-lint.test.ts

# Full frontend test suite
cd frontend && npm test

# Production build
cd frontend && npm run build
```
