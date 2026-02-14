# fig-choice-14: Observability -- PostHog + Sentry vs Alternatives

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-14 |
| **Title** | Observability: PostHog + Sentry vs Alternatives |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/prd/decisions/L5-operations/observability-stack.decision.yaml |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains the observability stack decision. The scaffold uses PostHog for product analytics (typed events, user journeys, feature flags) and Sentry for error tracking. This was originally planned as Highlight.io (combined solution) but Highlight.io shut down. Shows comparison against Datadog (expensive enterprise), Grafana (self-hosted), and the previous Highlight.io plan.

The key message is: "PostHog (product analytics) + Sentry (error tracking) provides the best cost-effective observability split after Highlight.io's shutdown -- separate tools for separate concerns."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  OBSERVABILITY: POSTHOG + SENTRY                               |
|  ■ Product Analytics + Error Tracking                          |
+---------------------------------------------------------------+
|                                                                |
|  CONTEXT: Highlight.io shut down → needed replacement          |
|                                                                |
|  ┌─────────────────────────────────────────────────────────┐   |
|  │  SELECTED STACK                                         │   |
|  │  ┌─────────────────┐    ┌──────────────────┐           │   |
|  │  │ PostHog          │    │ Sentry            │           │   |
|  │  │ ───────          │    │ ──────            │           │   |
|  │  │ Product analytics│    │ Error tracking    │           │   |
|  │  │ Feature flags    │    │ Performance       │           │   |
|  │  │ Session replay   │    │ Release health    │           │   |
|  │  │ Typed events     │    │ Stack traces      │           │   |
|  │  │ User journeys    │    │ Issue grouping    │           │   |
|  │  │ posthog-js lib   │    │ sentry SDK        │           │   |
|  │  │ Free: 1M events  │    │ Free: 5K errors   │           │   |
|  │  └─────────────────┘    └──────────────────┘           │   |
|  └─────────────────────────────────────────────────────────┘   |
|                                                                |
|  vs ALTERNATIVES                                               |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │ DATADOG      │ │ GRAFANA +    │ │ HIGHLIGHT.IO │          |
|  │              │ │ PROMETHEUS   │ │ (DEAD)       │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ Enterprise   │ │ Self-hosted  │ │ All-in-one   │          |
|  │ all-in-one   │ │ open-source  │ │ open-source  │          |
|  │              │ │              │ │              │          |
|  │ $15/host/mo  │ │ Free (infra  │ │ Shut down    │          |
|  │ + per metric │ │ cost only)   │ │ 2025         │          |
|  │              │ │              │ │              │          |
|  │ Overkill for │ │ Operational  │ │ Was the      │          |
|  │ scaffold     │ │ burden       │ │ ideal choice │          |
|  └──────────────┘ └──────────────┘ └──────────────┘          |
|                                                                |
+---------------------------------------------------------------+
|  Archetype: Engineer (Grafana 0.40) | Musician (Minimal 0.50)  |
|  Solo (Minimal 0.65) | Well-Funded (Datadog 0.35)             |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "OBSERVABILITY: POSTHOG + SENTRY" with coral accent square |
| Context note | `label_editorial` | Highlight.io shutdown context |
| PostHog card | `selected_option` | Product analytics, feature flags, typed events, free tier |
| Sentry card | `selected_option` | Error tracking, performance, release health, free tier |
| Datadog alternative | `deferred_option` | Enterprise, expensive, overkill |
| Grafana alternative | `deferred_option` | Self-hosted, operational burden |
| Highlight.io (dead) | `deferred_option` | Was ideal, shut down |
| Archetype footer | `callout_bar` | Per-archetype observability preferences |

## Anti-Hallucination Rules

1. PostHog is used for product analytics with typed events in `frontend/src/lib/analytics/events.ts`.
2. The posthog-js library is the frontend integration.
3. Highlight.io shut down -- this is why the scaffold moved to PostHog + Sentry. Per MEMORY.md: "posthog_sentry option added (Highlight.io dead)".
4. Archetype preferences from REPORT.md: Engineer Grafana 0.40, Musician Minimal 0.50, Solo Minimal 0.65, Well-Funded Datadog 0.35.
5. PostHog free tier includes 1 million events/month.
6. Sentry free tier includes error tracking.
7. Datadog pricing starts at $15/host/month plus per-metric charges.
8. Grafana + Prometheus is self-hosted and free but requires infrastructure management.
9. Background must be warm cream (#f6f3e6).

## Alt Text

Architecture decision: PostHog plus Sentry selected for music attribution observability, providing typed product analytics and error tracking for confidence scoring workflows, compared against Datadog, Grafana, and defunct Highlight.io in the open-source attribution scaffold.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture decision: PostHog plus Sentry selected for music attribution observability, providing typed product analytics and error tracking for confidence scoring workflows, compared against Datadog, Grafana, and defunct Highlight.io in the open-source attribution scaffold.](docs/figures/repo-figures/assets/fig-choice-14-observability-posthog-sentry.jpg)

*PostHog (product analytics with typed events and feature flags) paired with Sentry (error tracking and performance monitoring) provides cost-effective observability for the music attribution scaffold after Highlight.io's shutdown, with separate tools for separate concerns.*

### From this figure plan (relative)

![Architecture decision: PostHog plus Sentry selected for music attribution observability, providing typed product analytics and error tracking for confidence scoring workflows, compared against Datadog, Grafana, and defunct Highlight.io in the open-source attribution scaffold.](../assets/fig-choice-14-observability-posthog-sentry.jpg)
