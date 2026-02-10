# Frontend, Auth & Styling Landscape Research -- February 2026

> Research conducted 2026-02-10 for the music-attribution-scaffold probabilistic PRD.
> Feeds into architectural decision nodes at PRD levels 2-4.

---

## Table of Contents

1. [Frontend Meta-Frameworks](#1-frontend-meta-frameworks)
2. [HTMX + Python (No-JS / Low-JS Path)](#2-htmx--python-no-js--low-js-path)
3. [React Ecosystem 2026](#3-react-ecosystem-2026)
4. [UI Component Libraries](#4-ui-component-libraries)
5. [Chat UI Components](#5-chat-ui-components)
6. [Auth Services (Managed)](#6-auth-services-managed)
7. [Auth Libraries (Self-Hosted)](#7-auth-libraries-self-hosted)
8. [Python Web Frameworks](#8-python-web-frameworks)
9. [Real-Time Features](#9-real-time-features)
10. [Design Systems & CSS](#10-design-systems--css)
11. [Suitability Matrix for Music Attribution Chat](#11-suitability-matrix)
12. [Probabilistic PRD Integration](#12-probabilistic-prd-integration)
13. [Sources](#13-sources)

---

## 1. Frontend Meta-Frameworks

### Next.js 16 (React) -- Current Stable

| Attribute | Detail |
|-----------|--------|
| **Version** | 16.1 (stable, Feb 2026) |
| **React version** | React 19.2 (canary channel) |
| **Bundler** | Turbopack (default; Rust-based, 5x faster cold builds vs Webpack, incremental builds 100x+ faster) |
| **Key 2026 features** | Cache Components via `use cache` directive + Partial Pre-Rendering (PPR); React Compiler 1.0 (auto-memoization); View Transitions API; filesystem caching for `next dev`; layout deduplication (60-80% prefetch reduction) |
| **RSC maturity** | Production-grade. RSC Payload is a compact binary. Prefetched & cached for instant navigation. |
| **Deployment** | Vercel-native, but works on any Node/Edge/serverless host |
| **Music attribution fit** | Strong. RSC for server-side confidence computation, streaming for chat, Vercel AI SDK integration is first-class. Heavy ecosystem means abundant talent. |

### SvelteKit 2 + Svelte 5 -- Compiler-First

| Attribute | Detail |
|-----------|--------|
| **Version** | Svelte 5 + SvelteKit 2 (stable) |
| **Key 2026 features** | Runes (`$state()`, `$derived()`, `$effect()`) for declarative reactivity; Snippets for reusable markup; improved CSP for hydration; enhanced Cloudflare adapters |
| **Performance** | No virtual DOM. Compiles to vanilla JS. Benchmarks: ~1200 req/s vs Next.js ~850. Near-zero TTI due to tiny bundle + SSR data preloading. |
| **SSR/SSG** | Full SSR, SSG, and hybrid rendering. Adapters for Node, serverless, edge, static. |
| **Music attribution fit** | Excellent for performance-sensitive UIs. Smaller bundle = faster mobile. Smaller ecosystem but rapidly growing. Good for teams wanting leaner stack. |

### Nuxt 4 (Vue)

| Attribute | Detail |
|-----------|--------|
| **Version** | Nuxt 4 (pre-release / early 2026) |
| **Key features** | Convention-based config; powerful SSG; Vue 3 Composition API; Nitro server engine |
| **Music attribution fit** | Natural choice for Vue.js teams. Strong if existing team has Vue expertise. Smaller chat-specific ecosystem than React. |

### Remix / React Router 7 (React)

| Attribute | Detail |
|-----------|--------|
| **Version** | React Router v7 (unified with Remix) |
| **Key 2026 features** | Single Fetch (default); progressive enhancement for forms (works without JS); nested routing with loader functions; web-standard request/response |
| **Music attribution fit** | Strong for form-heavy workflows (album metadata entry). Progressive enhancement means graceful degradation. Less ecosystem lock-in than Next.js. |

### Astro 5 / 6 -- Content-First

| Attribute | Detail |
|-----------|--------|
| **Version** | Astro 5.x stable; Astro 6 beta |
| **Key 2026 features** | Content Layer API (type-safe external CMS/API content); Server Islands (mix static + dynamic per-component); Live Content Collections (v5.10, stable in v6 -- real-time data without rebuild); Islands Architecture (zero JS by default) |
| **Music attribution fit** | Best for documentation / knowledge-base / landing pages. Server Islands could serve dynamic attribution widgets on static pages. Not ideal for heavy interactive chat. Can embed React/Svelte/Vue islands for interactive components. |

### SolidStart (SolidJS)

| Attribute | Detail |
|-----------|--------|
| **Version** | SolidStart 1.0 |
| **Key features** | Fine-grained reactivity (no virtual DOM); Single Flight Mutations; React-like component model with direct DOM updates |
| **Music attribution fit** | Highest raw performance. Smallest community. Good for teams wanting React mental model without React overhead. Limited chat component ecosystem. |

### Framework Selection Decision Factors

```
IF team has React experience AND wants largest ecosystem
  -> Next.js 16 (P=0.40)
  -> React Router 7 (P=0.15) if avoiding Vercel lock-in

IF team prioritizes performance AND smaller bundle
  -> SvelteKit 2 (P=0.25)

IF team is Python-first AND wants minimal JS
  -> HTMX path (see Section 2) (P=0.15)

IF content/docs heavy with interactive islands
  -> Astro 5 (P=0.05)
```

---

## 2. HTMX + Python (No-JS / Low-JS Path)

### HTMX 2.0

| Attribute | Detail |
|-----------|--------|
| **Version** | 2.0.8 (stable) |
| **Key changes from 1.x** | Head tag merging built-in; Shadow DOM support; configurable response code handling; `htmx.config.disableInheritance`; `inherit` keyword for `hx-include`/`hx-indicator`/`hx-disabled-elt`; extensions moved to separate repos with independent versioning |
| **Dropped** | IE support (1.x line maintained for IE) |
| **Roadmap** | HTMX 4.0 expected early-to-mid 2026, latest by early 2027 |

### FastHTML

| Attribute | Detail |
|-----------|--------|
| **Description** | Python library for building web apps with HTMX. Intuitive like FastAPI, HTML+HTMX structure. |
| **Key features** | Routes return lightweight DOM "partials" (no full page refresh); pure Python (no JS required); HTMX integration built-in |
| **Maturity** | Newer framework, growing community. Created by Jeremy Howard (fast.ai). |
| **Music attribution fit** | Ideal for Python-heavy teams (data scientists, ML engineers). Rapid prototyping. Chat interface via WebSocket extension possible but less polished than JS-based alternatives. |

### PyHAT Stack (Python + HTMX + ASGI + Tailwind)

| Attribute | Detail |
|-----------|--------|
| **Components** | Python backend + HTMX for interactivity + ASGI server + Tailwind CSS |
| **Proven results** | React-to-HTMX migration case study: 67% codebase reduction (21,500 to 7,200 LOC), 96% fewer JS dependencies (255 to 9), 50-60% faster TTI |
| **Variants** | Django + HTMX + django-htmx; FastAPI + Jinja2 + HTMX (via FastHX); Litestar + HTMX |

### Django + HTMX Chat Pattern

Working chat implementations exist using Django Channels (WebSockets) + HTMX for real-time messaging. HTMX abstracts away WebSocket usage so no JS needed in source code. Django Channels handles message persistence, room management, and broadcast.

### Music Attribution Fit

| Strength | Limitation |
|----------|-----------|
| Python team stays in Python | Chat UI less polished than Vercel AI SDK |
| Smaller attack surface (less JS) | Streaming AI responses need custom SSE/WS work |
| Faster prototyping for ML-heavy teams | Component ecosystem smaller |
| Lower hosting costs (no Node needed) | Real-time features require Django Channels or manual WebSocket setup |

---

## 3. React Ecosystem 2026

### React 19.2 (via Next.js 16)

| Feature | Status |
|---------|--------|
| **Server Components** | Production-grade. Render on server, zero client JS for server components. Direct DB/filesystem access. |
| **Server Actions** | Stable. Async functions executed on server, called from client components. No bespoke API endpoints needed. |
| **React Compiler 1.0** | Stable. Auto-memoization, zero manual `useMemo`/`useCallback`. |
| **View Transitions** | New in 19.2. Native page transition animations. |
| **useEffectEvent** | New in 19.2. Stable event handler references without stale closures. |
| **Activity** | New in 19.2. (Details emerging) |
| **Document metadata** | Native `<title>`, `<link>`, `<meta>` rendering with automatic `<head>` hoisting. |

### TanStack Router

| Attribute | Detail |
|-----------|--------|
| **Key feature** | First-class TypeScript: generates types for routes and params (compile-time error catching) |
| **Data loading** | Built-in data loaders with caching. Instant navigation on revisit. |
| **Integration** | Works with RTK Query, urql, Relay, Apollo, Zustand, Jotai, Recoil |
| **Music attribution fit** | Type-safe routing for album/track/artist pages. Data loaders for attribution confidence scores. |

### TanStack Query (React Query)

| Attribute | Detail |
|-----------|--------|
| **Role** | Server state management: caching, background updates, stale-time logic |
| **Integration** | `jotai-tanstack-query` for atomic state + server state sync; works with Zustand for client-side global state |
| **Music attribution fit** | Cache attribution API responses. Background refresh for live confidence updates. Optimistic updates for gap-filling. |

### State Management

| Library | Pattern | Use Case |
|---------|---------|----------|
| **Zustand** | Global store (flux-like, minimal API) | Client-side app state: current album, UI mode, user prefs |
| **Jotai** | Atomic state (bottom-up) | Fine-grained reactive state: individual field confidence scores |
| **Redux Toolkit** | Full flux + RTK Query | Large teams needing strict patterns. Overkill for MVP. |

### Recommended Stack for Music Attribution (React Path)

```
Next.js 16 + React 19.2
  + TanStack Query (server state / API caching)
  + Zustand OR Jotai (client state)
  + TanStack Router (if not using Next.js App Router)
```

---

## 4. UI Component Libraries

### Comparison Matrix

| Library | Framework Support | Styling | Accessibility | Components | Approach |
|---------|-------------------|---------|---------------|------------|----------|
| **shadcn/ui** | React, Svelte, Vue, Solid | Tailwind CSS | Radix primitives (ARIA) | ~50+ | Copy-paste source code; full ownership |
| **Radix UI** | React (primary) | Unstyled (headless) | First-class ARIA + keyboard | ~30 primitives | Headless primitives; BYO theme |
| **Headless UI** | React, Vue | Unstyled (headless) | ARIA + keyboard | ~10 components | By Tailwind Labs; minimal set |
| **DaisyUI** | Framework-agnostic (CSS) | Tailwind CSS + themes | Accessible | 63 components | Pre-styled; CSS variables for theming |
| **Park UI** | React, Solid, Vue (via Ark UI) | Tailwind or Panda CSS | Ark UI primitives | 45+ | Styled layer on headless Ark UI |
| **Ark UI** | React, Solid, Vue | Unstyled (headless) | First-class | 45+ | Headless; by Chakra UI team |

### Key Decisions for Music Attribution

| Decision | Recommendation |
|----------|---------------|
| **React + maximum flexibility** | shadcn/ui (copy-paste, full control, Radix underneath) |
| **React + fastest setup** | DaisyUI (pre-styled, CSS-only themes) |
| **Svelte** | shadcn-svelte (community port, actively maintained) |
| **Vue** | shadcn-vue or Park UI |
| **Multi-framework team** | Park UI / Ark UI (React + Vue + Solid) |
| **HTMX path** | DaisyUI (framework-agnostic CSS) or Tailwind utilities directly |

### shadcn/ui Ecosystem in 2026

- Now has official ports: shadcn-svelte, shadcn-vue
- Vercel AI Elements built on shadcn/ui
- 25+ purpose-built AI conversational components available via shadcn.io/ai
- De facto standard for new Next.js projects

---

## 5. Chat UI Components

### Vercel AI SDK 6 + Chat SDK

| Attribute | Detail |
|-----------|--------|
| **Version** | AI SDK 6 (latest, 2026) |
| **Key features** | `useChat` hook for streaming chat; agent abstraction (`ToolLoopAgent` class); tool execution approval (human-in-the-loop); multi-provider support (OpenAI, Anthropic, etc.) |
| **Chat SDK** | Full-featured: message persistence, auth, multimodal support, shareable chats, generative UI, customizable artifacts, in-browser code execution |
| **AI Elements** | New Vercel product: pre-built shadcn/ui components for message threads, input boxes, reasoning panels, response actions |
| **Python backend** | Vercel Python SDK (beta): deploy FastAPI/Flask on Vercel; Python AI SDK with streaming + tool-calling |
| **Music attribution fit** | Best-in-class for conversational gap-filling. Streaming confidence scores. Tool-calling for attribution lookups (ISRC, ISWC). Human-in-the-loop for review. |

### CopilotKit

| Attribute | Detail |
|-----------|--------|
| **Version** | Latest 2026 |
| **Key features** | AG-UI protocol (Agent-User Interaction); Generative UI (agents generate UI components at runtime); Shared State (bi-directional agent-UI sync); Human-in-the-loop; MCP App support |
| **AG-UI protocol** | Bi-directional connection between frontend and any agentic backend. Not tied to specific LLM provider. |
| **Architecture** | Slack-like conversational interface; generative UI appears inline as cards/blocks/tool responses |
| **Music attribution fit** | Excellent for agentic workflows. Agent could dynamically generate attribution forms, confidence visualizations. MCP integration aligns with paper's MCP consent infrastructure. |

### Stream Chat (GetStream)

| Attribute | Detail |
|-----------|--------|
| **SDK** | stream-chat-react, stream-chat-react-native |
| **Key features** | Rich message lists, reactions, threads, attachments, channel previews. Highly customizable via component overrides. |
| **Pricing** | Free for small usage; commercial plans for production |
| **Music attribution fit** | Overkill for attribution chat. Designed for multi-user messaging (Slack/Discord-like). Could work for collaborative attribution review but expensive for the use case. |

### Chat UI Decision Tree

```
IF primary interface is AI-assisted gap-filling conversation
  AND using React/Next.js
  -> Vercel AI SDK 6 + AI Elements (P=0.50)
  -> CopilotKit with AG-UI (P=0.25) if agent-heavy / MCP integration needed

IF primary interface is collaborative review (multiple users)
  -> Stream Chat (P=0.10)

IF using HTMX/Python path
  -> Custom SSE/WebSocket chat (P=0.15)
  -> Django Channels + HTMX (proven pattern)
```

---

## 6. Auth Services (Managed)

### Pricing Comparison for Small Apps (< 1000 MAU initially)

| Service | Free Tier MAU | Paid Starting Price | Key Strength | Key Limitation |
|---------|---------------|--------------------| -------------|----------------|
| **Clerk** | 50,000 MRU (updated Feb 2026) | $20/mo (Pro) | Best DX; pre-built UI components; 100 free orgs | JS/TS-first; Python backend needs API verification |
| **Supabase Auth** | 50,000 MAU | $25/mo (Pro, 100K MAU) | Bundled with Postgres + storage + realtime; cheapest full-stack | Projects pause after 7d inactivity on free tier |
| **Auth0** | 7,500 MAU | Not public above 10K | Enterprise standard; most providers | Expensive at scale; per-user cost *increases* with volume |
| **WorkOS** | N/A (per-connection) | $125/connection/mo (SSO) | B2B enterprise features (SSO, Directory Sync) | B2B focused; not for B2C consumer apps |
| **Stytch** | 5,000 MAU | $249/mo | Modern passwordless flows; clean APIs | Enterprise features feel like add-ons; expensive |

### Recommendation for Music Attribution MVP

| Scenario | Recommendation | Rationale |
|----------|---------------|-----------|
| **Next.js frontend + separate Python backend** | Clerk | Best DX, generous free tier, pre-built components |
| **Full-stack Python (Supabase as BaaS)** | Supabase Auth | Auth + DB + Realtime bundled; one platform |
| **Enterprise/B2B (label partnerships)** | WorkOS or Auth0 | SSO, directory sync for label IT systems |
| **Budget-constrained MVP** | Supabase Auth (free tier) | 50K MAU free; Postgres included |

---

## 7. Auth Libraries (Self-Hosted)

### Major Shift: Auth.js Merged into Better Auth

As of 2026, **Auth.js (formerly NextAuth.js) is now maintained by the Better Auth team**. The original main contributor (Balazs Orban) left in January 2025, and v5 remained in beta for an extended period. This merger means:

- **Better Auth** is now the recommended path for JS/TS self-hosted auth
- NextAuth v4 is legacy; migration to Better Auth is the forward path
- Better Auth provides email/password, OAuth providers (GitHub, Google, Discord, etc.), session management

### Comparison

| Library | Language | Status (2026) | Python Backend Support | Key Feature |
|---------|----------|---------------|----------------------|-------------|
| **Better Auth** (+ Auth.js) | TypeScript | Active, merged with Auth.js | Indirect (verify JWT/session from Python) | Now the unified JS auth library |
| **Lucia Auth** | TypeScript | Archived (educational project) | None | Was educational; recommend migration to Better Auth |
| **SuperTokens** | Multi-SDK | Active | **Yes** (Python SDK, FastAPI middleware) | Self-hosted or managed; email/password + social + MFA |
| **Authentik** | Python | Active | **Native** (Python-based IdP) | Full IdP: OIDC, OAuth2, SAML, LDAP, proxy mode |
| **Passport.js** | Node.js | Maintained | None (Node-only) | 500+ strategies; legacy but widely used |

### For Python-First Teams

| Option | Best For |
|--------|----------|
| **SuperTokens** | FastAPI/Django backend with self-hosted auth core; Python SDK with FastAPI middleware built-in |
| **Authentik** | Full self-hosted identity provider; Python-native; customizable flows; OIDC/SAML for enterprise |
| **FastAPI + PyJWT** | Minimal custom JWT auth; full control; no external dependency |
| **Django auth + django-allauth** | Django projects needing social login + email verification |

---

## 8. Python Web Frameworks

### Comparison Matrix

| Framework | Version (2026) | Async Support | Performance | Ecosystem | Use Case |
|-----------|---------------|---------------|-------------|-----------|----------|
| **FastAPI** | Latest stable | Async-first (Starlette + Pydantic v2) | High (near Starlette raw) | Largest (70K+ GitHub stars; OpenAI, Anthropic, Microsoft use it) | APIs, AI backends, microservices |
| **Litestar** | 3.x (LTS until 2026) | Async-first (msgspec) | Highest in micro-benchmarks | Smaller but growing; strict SemVer | High-perf APIs, enterprise teams wanting explicit architecture |
| **Django** | 6.0 (released) | Hybrid: async views + async ORM (5.2+); `AsyncPaginator` in 6.0 | Moderate (ORM still uses threadpool for some ops) | Massive (admin, ORM, auth, templates) | Full-stack apps, admin panels, content management |
| **Starlette** | Stable | Pure async ASGI | Highest raw | Minimal (by design) | Base layer for custom frameworks; used by FastAPI internally |

### Django Async Evolution (2026 Status)

- Django 5.2: Native async database connection pooling; async auth functions (`aauthenticate()`, `alogin()`, etc.)
- Django 6.0: `AsyncPaginator`, `AsyncPage`; async signal dispatch (`Signal.asend()`)
- ORM: Async operations stable but some sync-to-async context switches remain
- Real-world: Teams report scaling to 500K RPM with async Django

### Framework Selection for Music Attribution

```
IF building API-first backend for React/Svelte frontend
  -> FastAPI (P=0.50) -- largest ecosystem, AI company standard
  -> Litestar (P=0.15) -- if wanting stricter architecture + max perf

IF building full-stack with admin panel + content management
  -> Django 6 (P=0.20) -- admin for label/rights management

IF using HTMX path (server-rendered)
  -> Django + HTMX (P=0.10)
  -> FastAPI + Jinja + HTMX (P=0.05)
```

---

## 9. Real-Time Features

### Protocol Comparison

| Protocol | Direction | Use Case | Complexity |
|----------|-----------|----------|------------|
| **Server-Sent Events (SSE)** | Server -> Client (unidirectional) | Streaming AI responses, live confidence updates | Low (HTTP-based, reconnects automatically) |
| **WebSockets** | Bi-directional | Chat, collaborative editing, real-time notifications | Medium (connection management, heartbeats) |
| **WebTransport** | Bi-directional (HTTP/3) | Low-latency, unreliable streams | High (emerging, limited support) |

### Managed Real-Time Services

| Service | Protocol | Free Tier | Key Feature | Music Attribution Fit |
|---------|----------|-----------|-------------|----------------------|
| **Supabase Realtime** | WebSockets (Phoenix) | Included in free tier (50K MAU) | Broadcast + Presence + Postgres Changes; listen to DB row changes | Excellent: live attribution status updates when DB records change |
| **Ably** | WebSockets + fallbacks | 200 concurrent connections; 6M messages/mo | Global edge network; most WebSocket connections of any platform | Enterprise-grade; overkill for MVP |
| **Pusher** | WebSockets | 200K messages/day; 100 concurrent | Established; simple pub/sub | Good for basic notifications |

### For Music Attribution

| Feature | Recommended Approach |
|---------|---------------------|
| **Streaming AI chat responses** | SSE via Vercel AI SDK (React) or FastAPI `StreamingResponse` (Python) |
| **Live attribution confidence updates** | Supabase Realtime (Postgres Changes) or SSE from FastAPI |
| **Collaborative album review** | WebSockets via Django Channels or FastAPI WebSocket |
| **Simple notifications** | SSE (simplest, sufficient for most cases) |

### Architecture Note

For a chat interface with AI-assisted gap-filling:
- **AI response streaming**: SSE is sufficient and simpler than WebSockets
- **User input**: Standard HTTP POST (HTMX `hx-post` or React form submission)
- **Live updates**: Supabase Realtime if using Supabase; otherwise SSE polling

---

## 10. Design Systems & CSS

### Tailwind CSS 4

| Attribute | Detail |
|-----------|--------|
| **Version** | 4.1 (latest, early 2026) |
| **Performance** | New engine: 5x faster full builds, 100x+ faster incremental (microseconds) |
| **Key changes** | CSS-first config (`@import "tailwindcss"` -- one line, zero config); `@theme` directive for design tokens; `@utility` directive for custom utilities; native container queries; 3D transforms; cascade layers; `@property` registered custom properties; `color-mix()` |
| **v4.1 additions** | Text shadows, masking utilities, pointer-aware variants, browser compatibility fallbacks |
| **Music attribution fit** | De facto standard. Works with all frameworks. shadcn/ui + DaisyUI built on it. |

### Panda CSS

| Attribute | Detail |
|-----------|--------|
| **Approach** | CSS-in-JS with build-time extraction (zero runtime) |
| **Key features** | Type-safe tokens; multi-variant support; RSC compatible; clean JSX (no utility class clutter) |
| **Framework support** | React, Vue, Svelte, Solid, Astro |
| **Music attribution fit** | Good for teams wanting type-safe styling with RSC support. Smaller ecosystem than Tailwind. |

### StyleX (Meta)

| Attribute | Detail |
|-----------|--------|
| **Status** | Active development; 2026 roadmap: better ergonomics, new features, developer tooling |
| **Approach** | CSS-in-JS objects compiled to atomic CSS at build time. Zero-runtime. |
| **Key feature** | Used internally at Meta (Facebook, Instagram). Deterministic styles. |
| **Music attribution fit** | Overkill for MVP. Interesting for large-scale apps where deterministic styling matters. |

### Open Props

| Attribute | Detail |
|-----------|--------|
| **Approach** | CSS custom properties (design tokens) -- not a framework |
| **Key features** | Colors, typography, spacing, shadows, animations; built-in light/dark mode; OKLCH color spaces; container queries via Open Props UI |
| **Integration** | Non-intrusive; use individual properties without changing existing CSS |
| **Music attribution fit** | Complementary to any approach. Good for design-token-first teams. Can combine with Tailwind or use standalone. |

### CSS Decision

```
IF using shadcn/ui or DaisyUI
  -> Tailwind CSS 4 (P=0.80) -- required by these libraries

IF wanting type-safe CSS-in-JS with RSC
  -> Panda CSS (P=0.10)

IF wanting framework-agnostic design tokens
  -> Open Props + Tailwind (P=0.05)

IF Meta-scale deterministic styling
  -> StyleX (P=0.05)
```

---

## 11. Suitability Matrix

### Music Attribution Chat Interface Requirements

1. **Conversational gap-filling**: AI asks questions to fill missing album metadata
2. **Album workflow**: Multi-step structured data entry with validation
3. **Real-time updates**: Live confidence scores, attribution status changes
4. **Multi-format output**: Tables, forms, confidence visualizations, ISRC/ISWC lookups

### Technology Stack Rankings

| Stack | Gap-Filling Chat | Album Workflow | Real-Time | Team Fit | Overall |
|-------|-----------------|----------------|-----------|----------|---------|
| **Next.js 16 + AI SDK 6 + shadcn + Clerk** | 5/5 | 4/5 | 4/5 | React teams | Best for JS-heavy teams |
| **SvelteKit 2 + custom chat + shadcn-svelte + Supabase** | 3/5 | 4/5 | 4/5 | Svelte teams | Best performance/bundle |
| **Django + HTMX + DaisyUI + Supabase Auth** | 3/5 | 5/5 | 3/5 | Python teams | Best for Python-first |
| **FastAPI + React SPA + CopilotKit + Clerk** | 5/5 | 3/5 | 4/5 | Mixed teams | Best for agentic MCP |
| **Astro 5 + React islands + AI SDK** | 4/5 | 2/5 | 2/5 | Content teams | Best for docs + light chat |

### Stack Archetypes (aligned with paper's team archetypes)

**Engineer-Heavy Team (BYO archetype)**
```
Next.js 16 / SvelteKit 2
+ FastAPI or Litestar backend
+ Vercel AI SDK 6 or CopilotKit
+ shadcn/ui + Tailwind 4
+ Better Auth or SuperTokens (self-hosted)
+ Supabase Realtime or custom SSE
+ Hetzner / Render / Fly.io
```

**Musician-Heavy Team (Bowling-Shoe archetype)**
```
Django + HTMX + DaisyUI
OR low-code: Supabase (auth + DB + realtime) + Vercel (frontend)
+ Clerk (managed auth, pre-built UI)
+ Minimal custom code
+ Render or Railway for deployment
```

---

## 12. Probabilistic PRD Integration

### Decision Nodes This Research Feeds Into

| PRD Level | Decision | Options | Conditional Dependencies |
|-----------|----------|---------|--------------------------|
| **L2: Frontend approach** | SPA vs SSR vs Hybrid vs HTMX | Next.js / SvelteKit / Django+HTMX / Astro | Drives L3 component library + L4 deployment |
| **L2: Auth strategy** | Managed vs self-hosted | Clerk / Supabase / SuperTokens / Authentik | Drives L3 session management + L4 compliance |
| **L3: Component library** | Pre-styled vs headless | shadcn/ui / DaisyUI / Radix / Ark UI | Conditioned on L2 framework choice |
| **L3: Chat architecture** | AI SDK vs CopilotKit vs custom | Vercel AI SDK / CopilotKit / Django Channels + HTMX | Conditioned on L2 frontend + backend framework |
| **L3: State management** | Global vs atomic vs server-only | Zustand / Jotai / TanStack Query / Django sessions | Conditioned on L2 framework |
| **L3: Real-time transport** | SSE vs WebSocket vs managed | SSE / WS / Supabase Realtime / Ably | Conditioned on L2 backend + hosting |
| **L4: CSS approach** | Utility-first vs CSS-in-JS | Tailwind 4 / Panda CSS / StyleX | Conditioned on L3 component library |

### Key Conditional Probabilities

```
P(shadcn/ui | Next.js) = 0.70
P(DaisyUI | HTMX path) = 0.60
P(Vercel AI SDK | Next.js AND chat-primary) = 0.75
P(CopilotKit | FastAPI backend AND MCP integration) = 0.50
P(Clerk | Next.js frontend) = 0.45
P(Supabase Auth | Supabase DB already chosen) = 0.85
P(SuperTokens | Python self-hosted requirement) = 0.55
P(Tailwind 4 | any modern stack) = 0.80
P(SSE | AI chat streaming) = 0.70
P(Supabase Realtime | Supabase already in stack) = 0.90
```

### Volatility Markers (3-month horizon)

| Area | Stability | Watch For |
|------|-----------|-----------|
| Next.js / React | High | React Compiler adoption; View Transitions |
| Svelte / SvelteKit | High | Svelte 5 ecosystem maturation |
| HTMX | High | HTMX 4.0 release |
| Vercel AI SDK | Medium | AI SDK 6 GA; Python SDK maturation |
| CopilotKit / AG-UI | Medium-Low | AG-UI protocol adoption; A2UI (Google) competition |
| Auth landscape | Medium | Better Auth + Auth.js merger stabilization |
| Clerk pricing | Medium | New pricing just released Feb 2026; may adjust |
| Tailwind CSS | High | v4 stable; v4.1 incremental improvements |
| Supabase | High | Steady feature additions; pricing stable |

---

## 13. Sources

### Frontend Frameworks
- [Next.js 16 Official Blog](https://nextjs.org/blog/next-16)
- [Next.js 16.1 Release](https://nextjs.org/blog/next-16-1)
- [Next.js in 2026: RSC and Server Actions](https://medium.com/@Samira8872/next-js-in-2026-exploring-react-server-components-rsc-and-server-actions-in-depth-60f0478830af)
- [What's New in Next.js 16 (Syncfusion)](https://www.syncfusion.com/blogs/post/whats-new-in-next-js-16-turbo-builds-smart-caching-ai-debugging)
- [Svelte 5 & SvelteKit: Features, Pros, Cons (Naturaily)](https://naturaily.com/blog/why-svelte-is-next-big-thing-javascript-development)
- [What's new in Svelte: February 2026](https://svelte.dev/blog/whats-new-in-svelte-february-2026)
- [SvelteKit vs Next.js (Windframe)](https://windframe.dev/blog/sveltekit-vs-nextjs)
- [Top 10 Full Stack Frameworks in 2026 (Nucamp)](https://www.nucamp.co/blog/top-10-full-stack-frameworks-in-2026-next.js-remix-nuxt-sveltekit-and-more)
- [Top 10 Next.js Alternatives 2026 (BCMS)](https://thebcms.com/blog/nextjs-alternatives)
- [Astro 5.0 Official](https://astro.build/blog/astro-5/)
- [Astro 6 Beta](https://astro.build/blog/astro-6-beta/)
- [What's New in Astro January 2026](https://astro.build/blog/whats-new-january-2026/)

### HTMX + Python
- [HTMX 2.0.0 Release](https://htmx.org/posts/2024-06-17-htmx-2-0-0-is-released/)
- [HTMX in 2026: Why Hypermedia is Dominating](https://vibe.forem.com/del_rosario/htmx-in-2026-why-hypermedia-is-dominating-the-modern-web-41id)
- [FastHTML Official](https://www.fastht.ml/)
- [PyHAT Stack (GitHub)](https://github.com/PyHAT-stack/awesome-python-htmx)
- [FastHTML with HTMX in Python (Medium)](https://medium.com/techtrends-digest/fasthtml-with-htmx-in-python-build-interactive-web-apps-without-javascript-65b36a9ac7d5)
- [Django + HTMX Chat Application](https://www.meetgor.com/django-htmx-chat-app/)
- [Django WebSockets ChatGPT (SaaS Pegasus)](https://www.saaspegasus.com/guides/django-websockets-chatgpt-channels-htmx/)

### React Ecosystem
- [React v19 Official](https://react.dev/blog/2024/12/05/react-19)
- [React 19 Key Features for 2026 (ColorWhistle)](https://colorwhistle.com/latest-react-features/)
- [Future of React: Top Trends 2026 (Netguru)](https://www.netguru.com/blog/react-js-trends)
- [React Server Components Explained: 2026 Guide](https://www.grapestechsolutions.com/blog/react-server-components-explained/)
- [Jotai + TanStack Query (GitHub)](https://github.com/jotaijs/jotai-tanstack-query)

### UI Component Libraries
- [shadcn/ui Official](https://ui.shadcn.com/)
- [shadcn-svelte](https://www.shadcn-svelte.com/)
- [shadcn-vue](https://shadcn-vue.com/docs/introduction)
- [Radix UI vs shadcn/ui (ScratchDB)](https://scratchdb.com/compare/radix-ui-vs-shadcn-ui/)
- [shadcn/ui Alternative: DaisyUI](https://daisyui.com/alternative/shadcn/)
- [React UI Libraries 2025 Comparison (Makers Den)](https://makersden.io/blog/react-ui-libs-2025-comparing-shadcn-radix-mantine-mui-chakra)
- [shadcn Alternatives (Tailgrids)](https://tailgrids.com/blog/shadcn-alternatives)

### Chat UI Components
- [Vercel AI SDK 6](https://vercel.com/blog/ai-sdk-6)
- [Vercel AI SDK Introduction](https://ai-sdk.dev/docs/introduction)
- [Vercel Chat SDK](https://vercel.com/blog/introducing-chat-sdk)
- [Vercel AI Elements](https://vercel.com/changelog/introducing-ai-elements)
- [React Components for Conversational AI (shadcn.io)](https://www.shadcn.io/ai)
- [CopilotKit Official](https://www.copilotkit.ai/)
- [AG-UI Protocol](https://www.copilotkit.ai/ag-ui)
- [State of Agentic UI 2026 (CopilotKit)](https://www.copilotkit.ai/blog/the-state-of-agentic-ui-comparing-ag-ui-mcp-ui-and-a2ui-protocols)
- [Developer's Guide to Generative UI 2026 (CopilotKit)](https://www.copilotkit.ai/blog/the-developer-s-guide-to-generative-ui-in-2026)
- [Stream Chat React SDK](https://getstream.io/chat/sdk/react/)
- [Python AI SDK (GitHub)](https://github.com/python-ai-sdk/sdk)

### Auth Services
- [Clerk Pricing (Official)](https://clerk.com/pricing)
- [Clerk New Plans Feb 2026](https://clerk.com/changelog/2026-02-05-new-plans-more-value)
- [Clerk vs Supabase Auth](https://clerk.com/articles/clerk-vs-supabase-auth)
- [Supabase Pricing 2026 (Metacto)](https://www.metacto.com/blogs/the-true-cost-of-supabase-a-comprehensive-guide-to-pricing-integration-and-maintenance)
- [Supabase Pricing (Official)](https://supabase.com/pricing)
- [Auth Pricing Wars: Cognito vs Auth0 vs Firebase vs Supabase (Zuplo)](https://zuplo.com/learning-center/api-authentication-pricing)
- [WorkOS vs Auth0 vs Stytch](https://workos.com/blog/workos-vs-auth0-vs-stytch)
- [Stytch vs WorkOS (SSOJet)](https://ssojet.com/ciam-vendors/comparison/stytch-vs-workos/)
- [Comparing Auth Providers (Hyperknot)](https://blog.hyperknot.com/p/comparing-auth-providers)

### Auth Libraries (Self-Hosted)
- [Auth.js is now part of Better Auth (HN)](https://news.ycombinator.com/item?id=45389293)
- [Auth.js + Better Auth Discussion (GitHub)](https://github.com/nextauthjs/next-auth/discussions/13252)
- [Better Auth vs NextAuth vs Auth0 (Better Stack)](https://betterstack.com/community/guides/scaling-nodejs/better-auth-vs-nextauth-authjs-vs-autho/)
- [Better Auth Official](https://www.better-auth.com/)
- [Lucia Auth Official](https://lucia-auth.com/)
- [Node.js Auth Migration: Lucia to Better Auth](https://www.nodejs-security.com/blog/nodejs-authentication-migration-from-lucia-to-better-auth)
- [Best Open Source Auth Tools 2026 (Cerbos)](https://www.cerbos.dev/blog/best-open-source-auth-tools-and-software-for-enterprises-2026)
- [Authentication Providers 2026 (Xano)](https://www.xano.com/blog/top-10-authentication-providers/)
- [Top 7 Auth Providers 2026 (Logto)](https://blog.logto.io/top-7-auth-providers-2026)
- [SuperTokens FastAPI Integration (DeepWiki)](https://deepwiki.com/supertokens/supertokens-python/4.3-fastapi-integration)

### Python Web Frameworks
- [FastAPI vs Django vs Flask 2026 (DevelopersVoice)](https://developersvoice.com/blog/python/fastapi_django_flask_architecture_guide/)
- [Litestar vs FastAPI (Better Stack)](https://betterstack.com/community/guides/scaling-python/litestar-vs-fastapi/)
- [Async Django 2026: Benchmarks (Medium)](https://medium.com/@yogeshkrishnanseeniraj/async-django-2026-benchmarks-architecture-and-scaling-to-500k-rpm-c2479d7966ee)
- [Django 6.0 Release Notes](https://docs.djangoproject.com/en/6.0/releases/6.0/)
- [Working with Async Django (Kraken)](https://engineering.kraken.tech/news/2026/01/12/using-django-async.html)
- [FastAPI vs Litestar: Dominance (Medium)](https://medium.com/top-python-libraries/fastapi-vs-litestar-which-python-web-framework-will-dominate-2025-1e63428268f2)

### Real-Time Features
- [Supabase Realtime (Official)](https://supabase.com/realtime)
- [Supabase Realtime Protocol](https://supabase.com/docs/guides/realtime/protocol)
- [Pusher vs Supabase Realtime 2026 (Ably)](https://ably.com/compare/pusher-vs-supabase)
- [Real-Time Web Apps 2025 (Debut Infotech)](https://www.debutinfotech.com/blog/real-time-web-apps)

### Design Systems & CSS
- [Tailwind CSS v4.0 (Official)](https://tailwindcss.com/blog/tailwindcss-v4)
- [Tailwind CSS Guide 2026 (LogRocket)](https://blog.logrocket.com/tailwind-css-guide/)
- [Tailwind v4 vs v3 (Frontend Hero)](https://frontend-hero.com/tailwind-v4-vs-v3)
- [Tailwind CSS 4.1 (Medium)](https://medium.com/@roman_fedyskyi/tailwind-css-4-1-brings-text-shadows-and-css-first-setup-5d696aaf2a79)
- [StyleX vs Tailwind (The New Stack)](https://thenewstack.io/stylex-vs-tailwind-metas-take-on-css-in-js-maintainability/)
- [Panda CSS vs Tailwind (Oreate AI)](https://www.oreateai.com/blog/panda-css-vs-tailwind-a-new-era-in-frontend-styling/03c27b886df09502d0953f8bd00ea916)
- [Open Props Official](https://open-props.style/)
- [Open Props (CSS-Tricks)](https://css-tricks.com/open-props-and-custom-properties-as-a-system/)
