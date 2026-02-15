# fig-frontend-14: PostHog Analytics Events

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-14 |
| **Title** | PostHog Analytics: Typed Event Taxonomy for Attribution Workflow Tracking |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/frontend.md |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure maps the 12 typed PostHog events defined in events.ts, organized by category (review, agent, UI, feedback). Each event shows its name, typed properties, and where in the UI it fires. The PostHogProvider wrapper and graceful degradation (no-op when PostHog not initialized) are shown.

The key message is: "12 typed events capture the complete attribution workflow -- from review approvals through agent interactions to proficiency changes -- with graceful no-op when PostHog is not configured."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  POSTHOG ANALYTICS EVENTS                                              |
|  ■ Typed Event Taxonomy                                                |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. PROVIDER ARCHITECTURE                                              |
|  ────────────────────────                                              |
|                                                                        |
|  layout.tsx                                                            |
|    └─ PostHogProvider (wraps entire app)                               |
|         └─ posthog-provider.tsx                                        |
|              ■ Initializes PostHog client                              |
|              ■ No-op export when env vars missing                      |
|              ■ posthog.capture() for all events                        |
|                                                                        |
|  II. EVENT TAXONOMY (12 events)                                        |
|  ───────────────────────────                                           |
|                                                                        |
|  REVIEW EVENTS                                                         |
|  ┌────────────────────────────────────────────────────────────┐       |
|  │  review_approved          { attribution_id, confidence }    │       |
|  │  review_batch_approved    { count }                         │       |
|  └────────────────────────────────────────────────────────────┘       |
|                                                                        |
|  AGENT EVENTS                                                          |
|  ┌────────────────────────────────────────────────────────────┐       |
|  │  agent_suggestion_accepted  { attribution_id, field }       │       |
|  │  agent_suggestion_rejected  { attribution_id, field }       │       |
|  │  agent_chat_opened          {}                              │       |
|  │  agent_chat_closed          { messages_exchanged }          │       |
|  │  agent_message_sent         { message_length }              │       |
|  └────────────────────────────────────────────────────────────┘       |
|                                                                        |
|  UI EVENTS                                                             |
|  ┌────────────────────────────────────────────────────────────┐       |
|  │  tooltip_shown              { tooltip_id, skill }           │       |
|  │  tooltip_dismissed          { tooltip_id, skill }           │       |
|  │  work_selected              { attribution_id }              │       |
|  └────────────────────────────────────────────────────────────┘       |
|                                                                        |
|  FEEDBACK / PROFICIENCY EVENTS                                         |
|  ┌────────────────────────────────────────────────────────────┐       |
|  │  feedback_submitted         { attribution_id,               │       |
|  │                               overall_assessment,           │       |
|  │                               center_bias }                 │       |
|  │  confidence_explained       { attribution_id,               │       |
|  │                               confidence_score }            │       |
|  │  proficiency_level_changed  { skill, old_level, new_level } │       |
|  └────────────────────────────────────────────────────────────┘       |
|                                                                        |
|  III. TYPE SAFETY                                                      |
|  ────────────────                                                      |
|  ■ EVENTS const object maps names to snake_case strings                |
|  ■ EventProperties interface types each event's payload                |
|  ■ trackEvent<E> generic function ensures type safety                  |
|  ■ All event names validated as snake_case in integration tests        |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "POSTHOG ANALYTICS EVENTS" in display font |
| Provider chain | `processing_stage` | PostHogProvider wrapping app, graceful no-op |
| Review events | `module_grid` | 2 events: review_approved, review_batch_approved |
| Agent events | `module_grid` | 5 events: suggestion accepted/rejected, chat open/close, message sent |
| UI events | `module_grid` | 3 events: tooltip shown/dismissed, work_selected |
| Feedback events | `module_grid` | 3 events: feedback_submitted, confidence_explained, proficiency_level_changed |
| Property types | `data_mono` | Typed properties per event in monospace |
| Type safety notes | `callout_box` | EVENTS const, EventProperties interface, trackEvent generic |

## Anti-Hallucination Rules

1. There are exactly 12 events defined in the EVENTS const object.
2. Event names are all snake_case strings (validated by integration tests).
3. The trackEvent function is generic: `trackEvent<E extends EventName>(event, properties)`.
4. PostHog is initialized via PostHogProvider in layout.tsx -- graceful no-op when env vars missing.
5. The analytics files are: `frontend/src/lib/analytics/events.ts` and `posthog-provider.tsx`.
6. feedback_submitted includes center_bias boolean (detects 0.45-0.55 range).
7. proficiency_level_changed tracks skill, old_level, and new_level.
8. All properties are typed via the EventProperties interface -- not Record<string, any>.

## Alt Text

Component diagram of the PostHog analytics event taxonomy for the music attribution scaffold: 12 type-safe events across review, agentic UI, interaction, and feedback categories track the complete music credits workflow from approval through agent chat to proficiency changes, with graceful no-op fallback for transparent confidence scoring analytics.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Component diagram of the PostHog analytics event taxonomy for the music attribution scaffold: 12 type-safe events across review, agentic UI, interaction, and feedback categories track the complete music credits workflow from approval through agent chat to proficiency changes, with graceful no-op fallback for transparent confidence scoring analytics.](docs/figures/repo-figures/assets/fig-frontend-14-posthog-analytics.jpg)

*Figure: Typed PostHog event taxonomy capturing the complete music attribution workflow, from review approvals and AG-UI agent interactions to proficiency-level transitions, with TypeScript generics ensuring compile-time safety for all 12 events.*

### From this figure plan (relative)

![Component diagram of the PostHog analytics event taxonomy for the music attribution scaffold: 12 type-safe events across review, agentic UI, interaction, and feedback categories track the complete music credits workflow from approval through agent chat to proficiency changes, with graceful no-op fallback for transparent confidence scoring analytics.](../assets/fig-frontend-14-posthog-analytics.jpg)
