# fig-agent-10: Agent Testing Strategy

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-agent-10 |
| **Title** | Agent Testing Strategy: Mock Agent, Integration Tests, and Coverage Map |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/agent.md, docs/testing.md |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure shows how the agentic UI layer is tested without requiring a running LLM backend. It covers three test categories in the agent-integration.test.tsx file: proficiency model tests (7 tests), PostHog event schema tests (3 tests), and feature flag default tests (1 test). The mock strategy (@patch on _get_agent for backend tests) and the principle of testing behavior (not LLM output) are highlighted.

The key message is: "Agent integration tests validate the proficiency model thresholds, event schema correctness, and feature flag mappings -- testing the deterministic behavior around the agent, not the non-deterministic LLM responses."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  AGENT TESTING STRATEGY                                                |
|  ■ Deterministic Tests Around Non-Deterministic AI                     |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. TEST FILE: agent-integration.test.tsx                              |
|  ────────────────────────────────────────                              |
|                                                                        |
|  11 integration tests (no LLM required)                                |
|                                                                        |
|  PROFICIENCY MODEL (7 tests)                                           |
|  ┌──────────────────────────────────────────────────────────────────┐ |
|  │  ■ novice: fewer than 10 interactions                            │ |
|  │  ■ novice: 10+ interactions but low success rate                 │ |
|  │  ■ intermediate: 10-49 interactions with 60%+ success            │ |
|  │  ■ expert: 50+ interactions with 75%+ success                    │ |
|  │  ■ expert threshold: exactly 50 at exactly 75%                   │ |
|  │  ■ zero interactions defaults to novice                          │ |
|  │  ■ 50+ interactions but low success stays intermediate           │ |
|  │                                                                   │ |
|  │  Tests: computeLevel() pure function with SkillMetrics input     │ |
|  └──────────────────────────────────────────────────────────────────┘ |
|                                                                        |
|  POSTHOG EVENT SCHEMA (3 tests)                                        |
|  ┌──────────────────────────────────────────────────────────────────┐ |
|  │  ■ all event names are snake_case strings                        │ |
|  │  ■ has expected event names (spot-check 5 specific events)       │ |
|  │  ■ has at least 10 distinct events                               │ |
|  └──────────────────────────────────────────────────────────────────┘ |
|                                                                        |
|  FEATURE FLAG DEFAULTS (1 test)                                        |
|  ┌──────────────────────────────────────────────────────────────────┐ |
|  │  ■ density mapping covers all proficiency levels                 │ |
|  │    (novice→comfortable, intermediate→compact, expert→dense)      │ |
|  └──────────────────────────────────────────────────────────────────┘ |
|                                                                        |
|  II. BACKEND AGENT MOCKING                                             |
|  ─────────────────────────                                             |
|                                                                        |
|  ┌──────────────────────────────────────────────────────────────────┐ |
|  │  @patch("music_attribution.chat.agui_endpoint._get_agent")       │ |
|  │                                                                   │ |
|  │  ■ Mock the lazy singleton agent for endpoint tests              │ |
|  │  ■ Inject mock agent that returns controlled responses            │ |
|  │  ■ Test SSE event sequence without LLM calls                     │ |
|  │  ■ Test error handling paths (no DB, no record)                  │ |
|  └──────────────────────────────────────────────────────────────────┘ |
|                                                                        |
|  III. WHAT IS NOT TESTED                                               |
|  ───────────────────────                                               |
|                                                                        |
|  ■ LLM response quality (non-deterministic — validated by humans)      |
|  ■ Actual AG-UI protocol compliance (would need CopilotKit harness)    |
|  ■ Voice agent (Pro feature — UI only, no backend)                     |
|                                                                        |
|  TESTING PRINCIPLE                                                     |
|  ─────────────────                                                     |
|  Test the deterministic ring around the non-deterministic core.        |
|  Proficiency thresholds, event schemas, state shapes, tool contracts.  |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "AGENT TESTING STRATEGY" in display font |
| Proficiency model tests | `module_grid` | 7 tests covering all threshold boundaries |
| PostHog schema tests | `module_grid` | 3 tests validating event naming and count |
| Feature flag tests | `module_grid` | 1 test for density mapping coverage |
| Backend mocking | `processing_stage` | @patch strategy for _get_agent singleton |
| Not tested list | `callout_box` | LLM quality, protocol compliance, voice agent |
| Testing principle | `callout_box` | "Deterministic ring around non-deterministic core" |
| Test counts | `data_mono` | 7 + 3 + 1 = 11 integration tests |

## Anti-Hallucination Rules

1. The test file is `frontend/src/__tests__/agent-integration.test.tsx` (exactly this path).
2. There are exactly 11 tests in the file: 7 proficiency, 3 PostHog, 1 feature flag.
3. Tests use Vitest (describe/it/expect), NOT Jest.
4. The proficiency tests call computeLevel() directly (imported from stores/proficiency).
5. Backend mocking uses @patch("music_attribution.chat.agui_endpoint._get_agent") (Python unittest.mock).
6. The 265 total frontend Vitest tests include these 11 agent integration tests.
7. LLM response quality is explicitly NOT tested (non-deterministic by nature).
8. Voice agent testing is explicitly NOT included (Pro feature, UI-only surface).
9. The testing principle is: test deterministic behavior (thresholds, schemas, contracts), not LLM output.

## Alt Text

Agent testing strategy: 11 frontend integration tests covering proficiency model, event schema, and feature flags, plus backend mock agent for endpoint tests.
