# CSS / Tailwind v4 Pitfalls — Metalearning Failure Doc

## The `text-[var()]` Ambiguity Trap (2026-02-11)

### What Happened

Every `text-[var(--text-*)]` class across 23 frontend files was silently broken.
Tailwind v4 generated `color: var(--text-2xl)` instead of `font-size: var(--text-2xl)`.
All font sizes fell back to the inherited 16px body default. No build error, no warning.

### Root Cause

In Tailwind v4, the `text-` prefix maps to **both** `font-size` and `color`.
When the value is a CSS variable like `var(--text-2xl)`, Tailwind cannot determine
the type at build time. It defaults to `color` for unknown types.

**Compiled CSS proof** (from `.next/static/css/`):
```css
/* BROKEN — Tailwind treats as color */
.text-\[var\(--text-2xl\)\] { color: var(--text-2xl); }
.text-\[var\(--text-sm\)\]  { color: var(--text-sm);  }

/* WORKING — Tailwind's built-in utility */
.text-2xl { font-size: var(--text-2xl); }
.text-sm  { font-size: var(--text-sm);  }
```

### Why It Went Undetected

1. No build error — Tailwind silently generates valid (but wrong) CSS
2. No runtime error — `color: var(--text-2xl)` resolves to `color: 1.5rem` which is invalid but browsers ignore it
3. Visual tests only checked component rendering, not computed styles
4. The developer (me) assumed `text-[var(--text-xl)]` would work like `text-xl`

### The Fix

1. **Removed** `--text-xs` through `--text-7xl` from `:root` (redundant with Tailwind v4 built-in scale)
2. **Replaced** all `text-[var(--text-SIZE)]` → `text-SIZE` across 23 files (151 replacements)
3. **Registered** custom `--line-height-tight` and `--line-height-snug` in `@theme` (our values differ from Tailwind defaults)
4. **Added** lint test to catch re-introduction of the broken pattern

### Rules to Prevent Recurrence

**NEVER use `text-[var(--anything)]` in Tailwind v4.**

The `text-` prefix is ambiguous. Instead:

| Want | Do | Don't |
|------|-----|-------|
| Font size | `text-xl`, `text-2xl` | `text-[var(--text-xl)]` |
| Text color | `text-heading`, `text-muted` | `text-[var(--color-heading)]` |
| Custom font size | `text-[length:var(--my-size)]` | `text-[var(--my-size)]` |

**Unambiguous prefixes that DO work with `var()`:**
- `bg-[var(--color-*)]` — always `background-color`
- `p-[var(--space-*)]`, `m-[var(--space-*)]` — always padding/margin
- `gap-[var(--space-*)]` — always gap
- `leading-[var(--leading-*)]` — always `line-height`
- `w-[var(--*)]`, `h-[var(--*)]` — always width/height
- `border-[var(--color-*)]` — BE CAREFUL, can be border-color OR border-width
- `duration-[var(--*)]` — always transition-duration

**Single Source of Truth principle:**
- Design tokens live in `globals.css` (`:root` block and `@theme` block)
- Components consume tokens via Tailwind utility classes, not via `var()` in arbitrary values
- If a Tailwind utility exists for your token, USE IT — don't wrap it in `[var()]`
- Only use `[var()]` for tokens that have NO Tailwind utility equivalent

### Broader Lesson: Style-Content Decoupling

The fundamental mistake was bypassing Tailwind's type system by using arbitrary values
everywhere. This created a shadow styling system where `globals.css` defined tokens that
Tailwind couldn't properly consume. The `@theme` block exists precisely to bridge CSS
custom properties into Tailwind's type-aware utility system — use it.

When you add a new design token to `:root`, ask: "Does Tailwind have a utility for this?"
- Yes → Register in `@theme` with the correct namespace (`--color-*`, `--font-size-*`, `--line-height-*`, `--spacing-*`)
- No → Use `[var()]` with a type hint if the prefix is ambiguous
