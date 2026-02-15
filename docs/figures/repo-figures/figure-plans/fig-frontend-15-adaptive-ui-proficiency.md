# fig-frontend-15: Adaptive UI / Proficiency Model

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-15 |
| **Title** | Adaptive UI: Proficiency Scoring, Feature Flags, and UI Density Adaptation |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/frontend.md |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows how the proficiency model drives adaptive UI behavior. It traces the flow from user interactions (review approvals, feedback submissions, confidence readings) through the Jotai proficiency store (persisted in localStorage), to the computeLevel() function that produces novice/intermediate/expert levels, and finally to the useFeatureFlags() hook that adjusts UI density, batch review availability, and adaptive tooltip visibility.

The key message is: "The proficiency model automatically adapts the UI as users gain experience -- novices see comfortable layouts with tooltips, experts get dense layouts with batch operations, and PostHog feature flags can override any default."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  ADAPTIVE UI / PROFICIENCY MODEL                                       |
|  ■ Experience-Driven Interface                                         |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. INPUT: USER INTERACTIONS                                           |
|  ────────────────────────────                                          |
|                                                                        |
|  ┌────────────────┐ ┌────────────────┐ ┌─────────────────────┐       |
|  │ Review actions  │ │ Feedback       │ │ Confidence reading  │       |
|  │ (approve,       │ │ submissions    │ │ (explain, explore)  │       |
|  │  batch approve) │ │                │ │                     │       |
|  └───────┬────────┘ └───────┬────────┘ └──────────┬──────────┘       |
|          │                  │                      │                   |
|          ▼                  ▼                      ▼                   |
|  II. PROFICIENCY STORE (Jotai + localStorage)                          |
|  ────────────────────────────────────────                              |
|                                                                        |
|  proficiencyStateAtom (key: "ma-proficiency")                          |
|  ┌──────────────────────────────────────────────────────────────┐     |
|  │  review:              { interactions: 23, successes: 18 }    │     |
|  │  feedback:            { interactions: 8,  successes: 7  }    │     |
|  │  confidence_reading:  { interactions: 45, successes: 38 }    │     |
|  └──────────────────────────────┬───────────────────────────────┘     |
|                                 │                                      |
|                                 ▼                                      |
|  III. computeLevel()                                                   |
|  ───────────────────                                                   |
|                                                                        |
|  ┌──────────────────────────────────────────────────────────────┐     |
|  │  novice:       < 10 interactions                             │     |
|  │  intermediate: 10-49 interactions + >= 60% success rate      │     |
|  │  expert:       50+ interactions + >= 75% success rate        │     |
|  └──────────────────────────────┬───────────────────────────────┘     |
|                                 │                                      |
|                                 ▼                                      |
|  IV. useFeatureFlags() OUTPUT                                          |
|  ────────────────────────────                                          |
|                                                                        |
|  ┌─────────────────────┬──────────┬──────────────┬────────────┐      |
|  │ Flag                │ Novice   │ Intermediate │ Expert     │      |
|  │─────────────────────┼──────────┼──────────────┼────────────│      |
|  │ uiDensity           │comfort.  │ compact      │ dense      │      |
|  │ showAdaptiveTooltips│ true     │ true         │ false      │      |
|  │ enableBatchReview   │ false    │ true         │ true       │      |
|  │ showAgentSidebar    │ true     │ true         │ true       │      |
|  └─────────────────────┴──────────┴──────────────┴────────────┘      |
|                                                                        |
|  POSTHOG OVERRIDE                                                      |
|  ────────────────                                                      |
|  ■ PostHog feature flags checked FIRST                                 |
|  ■ Falls back to proficiency-based defaults if PostHog unavailable     |
|  ■ Remote flags: show_agent_sidebar, ui_density, enable_batch_review,  |
|    show_adaptive_tooltips                                              |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "ADAPTIVE UI / PROFICIENCY MODEL" in display font |
| Interaction sources | `processing_stage` | Three skill categories as input |
| Proficiency store | `storage_layer` | atomWithStorage with sample metrics |
| computeLevel function | `decision_point` | Three-tier threshold logic |
| Feature flags table | `module_grid` | 4 flags x 3 proficiency levels matrix |
| PostHog override note | `callout_box` | Remote flag override mechanism |
| Data flow arrows | `data_flow` | Top-to-bottom from interactions to flags |
| Roman numerals I-IV | `section_numeral` | Section identifiers |

## Anti-Hallucination Rules

1. Three skills tracked: "review", "feedback", "confidence_reading" (exactly these names).
2. Proficiency thresholds: novice (<10), intermediate (10-49 + 60% success), expert (50+ + 75% success).
3. The proficiency state is persisted via atomWithStorage with key "ma-proficiency" in localStorage.
4. computeLevel() is a pure function (not an atom) that takes SkillMetrics and returns ProficiencyLevel.
5. Four feature flags: showAgentSidebar (default true), uiDensity (varies), enableBatchReview (varies), showAdaptiveTooltips (varies).
6. UI density values are exactly: "comfortable", "compact", "dense" (type UiDensity).
7. PostHog flags are checked FIRST via posthog.getFeatureFlag() -- local proficiency is the FALLBACK.
8. The useFeatureFlags hook is in `frontend/src/hooks/use-feature-flags.ts`.
9. overallProficiencyAtom returns the MAX of individual skill levels.

## Alt Text

Component diagram of the adaptive UI proficiency model for the music attribution scaffold: user interactions with music credits review, feedback, and confidence reading feed a Jotai store with localStorage persistence, computeLevel produces novice-intermediate-expert tiers, and useFeatureFlags adapts UI density, batch operations, and tooltip visibility for experience-driven transparent confidence scoring.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Component diagram of the adaptive UI proficiency model for the music attribution scaffold: user interactions with music credits review, feedback, and confidence reading feed a Jotai store with localStorage persistence, computeLevel produces novice-intermediate-expert tiers, and useFeatureFlags adapts UI density, batch operations, and tooltip visibility for experience-driven transparent confidence scoring.](docs/figures/repo-figures/assets/fig-frontend-15-adaptive-ui-proficiency.jpg)

*Figure: The proficiency model automatically adapts the music attribution UI as users gain experience -- novices see comfortable layouts with tooltips, experts unlock dense layouts with batch operations, and PostHog feature flags can remotely override any default.*

### From this figure plan (relative)

![Component diagram of the adaptive UI proficiency model for the music attribution scaffold: user interactions with music credits review, feedback, and confidence reading feed a Jotai store with localStorage persistence, computeLevel produces novice-intermediate-expert tiers, and useFeatureFlags adapts UI density, batch operations, and tooltip visibility for experience-driven transparent confidence scoring.](../assets/fig-frontend-15-adaptive-ui-proficiency.jpg)
