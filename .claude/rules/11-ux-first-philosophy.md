# UX-First Philosophy

## Core Principle

**"Premium UX first"** — UX quality is non-negotiable. Attribution is inherently tedious work; the UI must make it feel effortless and even delightful.

## Editorial Boldness

The interface is **not a generic SaaS dashboard**. It is an editorial experience:

1. **Instrument Serif headings** at 48-96px are the primary visual element
2. **Asymmetric layouts** — never perfectly centered, never symmetric grids
3. **Fixed left sidebar** with rotated text — not a horizontal top nav
4. **Coral red accent** (#E84C4F) as single bold accent against warm neutrals
5. **Accent squares and lines** as pure CSS graphic elements
6. **Text links with underlines** — not pill buttons
7. **Horizontal rows with dividers** — not shadow-box cards
8. **Stagger reveal animations** — scroll-triggered, motion/react
9. **Roman numerals** for sequential elements (Warp Records homage)

## Interaction Design Standards

1. **Every click feels considered** — no gratuitous steps, no pointless modals
2. **Smart defaults** — pre-fill what we can, suggest what we think, let the user correct
3. **Batch operations** — never make users do one-at-a-time what could be done in bulk
4. **Progressive disclosure** — show the essential, reveal the complex on demand
5. **Direct manipulation** — click-to-edit, drag-to-reorder, inline everything possible

## Animation Philosophy

- **Subtle and purposeful** — animations communicate state change, not decoration
- **Fast** — 150–200ms for micro-interactions, 300ms max for transitions
- **`prefers-reduced-motion` respected** — ALWAYS check and disable animations if set
- **No bouncing, no elastic, no spring physics** — simple easing only
- **Mount animations** for gauges and meters (they "fill up" on first render)

## State Design (First-Class Work)

### Empty States
- Illustrated, warm, helpful — not just "No data"
- Clear call-to-action for what to do next
- Match the editorial tone of the rest of the UI

### Loading States
- Skeleton loaders that match content shapes (not spinners)
- Shimmer animation on skeletons (respecting reduced-motion)
- Optimistic updates where possible

### Error States
- Friendly, never technical jargon
- Always suggest a recovery action
- Error boundaries with retry buttons

## Voice Agent = Pro Feature

- Voice is a premium/Pro tier upsell — higher cost tier
- In MVP: show aspirational UI only (mic animation, example queries, "Upgrade to Pro")
- Do NOT implement actual voice processing — just the upsell surface
- The banner is **subtle and aspirational**, never pushy or interruptive

## Attribution Workflow

The review queue is the **key friction reducer**:
- AI suggestions appear as diffs (before/after)
- "Approve All" for batch acceptance
- Progress counter shows momentum
- Smart sorting by review priority
- Tab between fields like a spreadsheet

## Accessibility (WCAG 2.1 AA)

Accessibility is a UX feature, not an afterthought:

1. **Color contrast**: All text meets 4.5:1 (normal) or 3:1 (large) ratio
2. **Keyboard navigation**: Every interactive element reachable via Tab
3. **ARIA on custom components**: ConfidenceGauge uses `role="meter"`, toggles use `role="radio"`
4. **Focus indicators**: Visible, high-contrast focus rings
5. **Screen reader support**: Meaningful labels, not just visual
6. **Touch targets**: Minimum 44×44px on mobile
7. **Two testing layers**:
   - Component-level: Vitest + `vitest-axe` (fast, every test run)
   - Browser-level: Playwright + `@axe-core/playwright` (real rendering, E2E suite)

## Design Decision Framework

When in doubt about a design choice, ask:

1. Would this feel at home in a premium music platform? (Not a dev tool)
2. Does this respect the user's time? (No unnecessary steps)
3. Is this warm? (Cream backgrounds, editorial typography, coral red accent)
4. Does this communicate confidence clearly? (Green/amber/red is instant)
5. Would Imogen Heap enjoy using this? (Our persona — technically savvy artist who cares deeply about attribution)
