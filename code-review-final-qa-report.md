# Final QA Deep Code Review Report — v1.0 Zenodo Freeze

**Branch**: `fix/qa-final-check`
**Date**: 2026-02-22
**Reviewers**: 6 parallel agents (Config Duplication, Backend Quality, Frontend Quality, Test Quality, Security, Docs/Build)
**Total findings**: 128 unique (after deduplication across agents)

---

## Executive Summary

The codebase is architecturally sound with good test coverage (~1,300 tests), proper SQL parameterization, and well-secured production Docker images. However, there are significant **config duplication** and **decoupling** issues — the primary concern the user raised. Confidence thresholds, tool logic, and DB credentials are duplicated across multiple files instead of importing from canonical sources.

### Severity Distribution

| Severity | Count | Action |
|----------|-------|--------|
| **CRITICAL** | 12 | Must fix before Zenodo freeze |
| **WARNING** | 38 | Should fix — meaningful quality improvement |
| **INFO** | 78 | Nice to have — defer post-freeze |

---

## CRITICAL Findings (Must Fix)

### C1. API version mismatch: `app.py` says "0.1.0", package says "1.0.0"
- **Files**: `src/music_attribution/api/app.py:109`, `src/music_attribution/__init__.py:11`, `pyproject.toml:3`
- **Fix**: Import `__version__` from `music_attribution` and use it in `create_app()`
- **Agents**: Config, Backend

### C2. `acoustid_fingerprint` vs `acoustid` field name — silently breaks AcoustID matching
- **File**: `src/music_attribution/resolution/orchestrator.py:265,566`
- **Issue**: `getattr(ids, "acoustid_fingerprint", None)` always returns `None` because the field is named `acoustid` on `IdentifierBundle`
- **Fix**: Change `"acoustid_fingerprint"` to `"acoustid"` in both locations
- **Agent**: Backend

### C3. Confidence thresholds (0.85/0.50) duplicated in 9+ files
- **Files**: `seed/imogen_heap.py`, `resolution/orchestrator.py`, `resolution/splink_linkage.py`, `resolution/string_similarity.py`, `chat/agent.py`, `voice/tools.py`, `frontend/confidence.ts`, `frontend/confidence-explanation.tsx`, `frontend/agent-review-queue.tsx`
- **Canonical source**: `src/music_attribution/constants.py:38,41`
- **Fix**: Import from `constants.py` in Python; import from `lib/theme/confidence.ts` in frontend
- **Agents**: Config, Frontend

### C4. Center-bias threshold (0.45-0.55) reimplemented in 3 files
- **Files**: `chat/agent.py:476`, `voice/tools.py:382`, `schemas/feedback.py:189`
- **Fix**: Delete manual checks in agent/voice; rely on `FeedbackCard.validate_center_bias()`
- **Agent**: Config

### C5. Resolution orchestrator fallback weights duplicate `_DEFAULT_WEIGHTS`
- **File**: `src/music_attribution/resolution/orchestrator.py:53-60,442-450`
- **Fix**: Use `self._weights.get(key)` with `_DEFAULT_WEIGHTS[key]` as fallback
- **Agent**: Config

### C6. `ConfidencePopover` inaccessible to keyboard users (WCAG violation)
- **File**: `frontend/src/components/works/confidence-popover.tsx:50-54`
- **Issue**: Only `onMouseEnter`/`onMouseLeave`, no keyboard/focus handlers
- **Fix**: Add `onFocus`/`onBlur` and `tabIndex={0}`
- **Agent**: Frontend

### C7. D3 consent graph triggers 180+ React re-renders in 3 seconds
- **File**: `frontend/src/components/permissions/consent-graph.tsx:136-145`
- **Issue**: `setPositions(new Map(...))` on every D3 tick (60fps x 3s)
- **Fix**: Batch with `requestAnimationFrame` or direct DOM manipulation during simulation
- **Agent**: Frontend

### C8. `getConfidenceTier()` duplicated with independent thresholds
- **Files**: `frontend/src/lib/theme/confidence.ts:12`, `frontend/src/components/confidence/confidence-explanation.tsx:46`
- **Fix**: Import from canonical `confidence.ts`
- **Agent**: Frontend

### C9. Tests that test local data, not production code
- **Files**: `tests/unit/test_chat_agent.py:110-176`
- **Issue**: `TestExplainConfidenceLogic` and `TestCenterBiasDetection` test operations on local mock dicts, never invoke actual tool functions
- **Fix**: Test actual agent tool functions with mocked DB sessions
- **Agent**: Tests

### C10. AST-only violation: `"HALFVEC" in source` string check on Python code
- **File**: `tests/unit/test_migration_002_structure.py:95-100`
- **Fix**: Use `ast.parse()` + `ast.walk()` to find `ast.Name` nodes
- **Agent**: Tests

### C11. Zenodo DOI badge is a placeholder
- **File**: `README.md:15`
- **Fix**: Update after Zenodo deposit or remove badge
- **Agent**: Docs

### C12. Sample data count mismatch: README says 9 works, backend seed has 8
- **File**: `README.md:336` vs `src/music_attribution/seed/imogen_heap.py`
- **Fix**: Add 9th work to backend seed or correct README
- **Agent**: Docs

---

## WARNING Findings (Should Fix)

### Config & Coupling

| ID | Finding | Files |
|----|---------|-------|
| W1 | DB credentials hardcoded in 4 files | Makefile:134, setup.sh:154, alembic.ini:3, docker-compose.dev.yml:60 |
| W2 | Port 8000 hardcoded in 6+ files instead of `${API_PORT}` | Makefile, Dockerfiles, entrypoint.sh |
| W3 | `pgvector/pgvector:pg17` image tag repeated in 7 files | compose, 5 integration tests, setup.sh |
| W4 | `all-MiniLM-L6-v2` model name hardcoded in 3 files | embedding_service, embedding_match, drift.py |
| W5 | `Settings` has 3 overlapping LLM config fields | config.py:110-114 |
| W6 | `MAX_VOICE_CONNECTIONS=10` hardcoded, not in VoiceConfig | voice/server.py:49 |
| W7 | `uv:latest` tag in all 4 Dockerfiles — not reproducible | Dockerfile, Dockerfile.test, Dockerfile.dev, Dockerfile.prod |

### Backend Code Quality

| ID | Finding | Files |
|----|---------|-------|
| W8 | `_get_session()` copy-pasted in 2 route modules; `dependencies.py` unused | attribution.py:35-50, permissions.py:78-93 |
| W9 | Union-find pattern duplicated in 3 locations | orchestrator, identifier_match, splink_linkage |
| W10 | `_agent` singleton not thread-safe | chat/agui_endpoint.py:50 |
| W11 | `Settings()` instantiated twice in `create_app` | api/app.py:57,104 |
| W12 | `assurance_level` filter applied in Python, not SQL | api/routes/attribution.py:136-138 |
| W13 | Duplicate tool logic: `explain_confidence` in agent + voice | chat/agent.py:295-331, voice/tools.py:238-273 |
| W14 | Duplicate tool logic: `submit_feedback` in agent + voice | chat/agent.py:474-517, voice/tools.py:374-408 |
| W15 | `(TimeoutError, Exception)` — TimeoutError branch unreachable | resolution/llm_disambiguation.py:148 |

### Frontend Code Quality

| ID | Finding | Files |
|----|---------|-------|
| W16 | `formatRole()` duplicated in credit-list + credit-editor | 2 files |
| W17 | `formatTimestamp()` duplicated in 3 files with different formats | audit-log, provenance-timeline, provenance-panel |
| W18 | `isAllowValue()` duplicated in consent-profile + consent-graph | 2 files |
| W19 | Permission result-to-color mapping duplicated in 3 components | audit-log, consent-graph, mcp-query-mockup |
| W20 | Inline skeleton loaders duplicated across 5 pages; existing Skeleton components unused | works, detail, permissions, review pages |
| W21 | PostHog env vars bypass `config.ts` single-source-of-truth | posthog-provider.tsx:6 |
| W22 | `generateAgentSuggestions()` called inside render loop | agent-review-queue.tsx:157 |
| W23 | ConsentGraph overlay shows zero counts — props never passed | permissions/page.tsx:167 |
| W24 | 6+ dead components with `// TODO: not yet integrated` | skeleton, error-boundary, empty-state, confidence-explanation, etc. |
| W25 | `FeedbackPanel` dead code parallels active `AgentFeedbackFlow` | feedback-panel.tsx |
| W26 | `useFeatureFlags` hook defined but never called | use-feature-flags.ts |
| W27 | NotificationBadge dropdown missing Escape key + aria-expanded | notification-badge.tsx |
| W28 | Permission tabs incomplete ARIA (tab role without tablist/tabpanel) | permissions/page.tsx:120-138 |
| W29 | Hardcoded `rgba()` box-shadows bypass shadow token system (4 instances) | consent-profile, inline-citation |
| W30 | MCP query mockup uses banned `rounded-lg/md` classes | mcp-query-mockup.tsx |

### Test Quality

| ID | Finding | Files |
|----|---------|-------|
| W31 | `_make_attribution()` helper copy-pasted in 6+ test files | Multiple test modules |
| W32 | No concurrent access tests for repositories | persistence tests |
| W33 | No None/null tests for MCP server tools | test_mcp_server.py |
| W34 | Integration test_agent_e2e still mocks the agent | test_agent_e2e.py |

### Security

| ID | Finding | Files |
|----|---------|-------|
| W35 | CORS `allow_methods` and `allow_headers` are wildcarded | api/app.py:118-119 |
| W36 | Search query `q` has no `max_length` limit | api/routes/attribution.py:201 |
| W37 | `PermissionTypeEnum` ValueError causes 500 error (not 400) | api/routes/permissions.py:124 |
| W38 | CopilotKit endpoint accepts raw unvalidated JSON | chat/agui_endpoint.py:218 |
| W39 | `database_url` is plain `str`, not `SecretStr` | config.py:97 |
| W40 | Voice API keys are plain strings, not SecretStr | voice/config.py:161-234 |
| W41 | Grafana anonymous Admin access in dev compose | docker-compose.dev.yml:113-114 |

### Docs & Build

| ID | Finding | Files |
|----|---------|-------|
| W42 | 6 unused production dependencies: loguru, pandera, polars, valkey, sse-starlette, asyncpg | pyproject.toml |
| W43 | `psycopg` driver only in dev group, not production deps | pyproject.toml |
| W44 | Test counts stale across README (1304 badge, 744 backend, 54 voice) | README.md |
| W45 | PRD node counts inconsistent (23, 40+, 79) across docs | CLAUDE.md, README.md, REPORT.md |
| W46 | `validate-guardrails` CI job references non-existent script | .github/workflows/ci.yml:173-197 |
| W47 | Missing gitignore entries: benchmark-results.json, *.zip, test-results/ | .gitignore |

---

## INFO Findings (Defer Post-Freeze)

<details>
<summary>78 INFO-level findings (click to expand)</summary>

### Dead Code (Backend)
- I1: Empty `core.py` module
- I2: Empty `confidence/__init__.py`
- I3: `if TYPE_CHECKING: pass` in metrics.py
- I4: 5 unused metric string constants in metrics.py
- I5: Unused optional imports (guardrails, letta, mem0 availability checks)

### Type Safety (Backend)
- I6: `_agent` module global has no type annotation
- I7: `session_factory` typed as `Any`
- I8: `self._model: Any` in embedding_match and splink_linkage
- I9: Voice pipeline factory functions return `Any`
- I10: `SOURCE_RELIABILITY_WEIGHTS` is mutable dict (use MappingProxyType)

### Error Handling
- I11: Silent `except Exception: pass` in drift metrics
- I12: WebSocket error doesn't send error frame before disconnect
- I13: `contextlib.suppress(Exception)` swallows all EM estimation errors

### Naming
- I14: `EdgeModel.metadata_` inconsistent naming
- I15: `get_tool_schemas()` vs `get_function_schemas()` naming confusion

### Database
- I16: `# type: ignore[arg-type]` on ORM-to-enum conversions (6 instances)
- I17: `schema_version = "1.0.0"` repeated in 5+ schemas

### Frontend State
- I18: `selectedWorkAtom` defined but never used
- I19: `resolvedThemeAtom` defined but never used (SSR hazard if used)
- I20: Works data fetched independently in works page vs review page

### Frontend Accessibility
- I21: Decorative accent lines missing `aria-hidden="true"`
- I22: Mobile menu missing focus trap and Escape key
- I23: CountBucket listbox options not keyboard-accessible

### Frontend Dead Code
- I24: `VoiceButton`, `AudioVisualizer`, voice store atoms unused
- I25: `ConfidenceExplanation` component never imported
- I26: `CreditEditor` component never imported
- I27: `VoiceAgentBanner` never imported

### Frontend CSS
- I28: Dead components use banned `rounded-*` classes
- I29: `accent-primary` utility in FeedbackPanel may not compile

### Test Quality
- I30: `test_empty_evidence_produces_wide_set` tautological assertion (`>= 0`)
- I31: `test_app_lifespan_disposes_engine` has no assertion on disposal
- I32: `test_db_session_closes_after_request` weak OR assertion
- I33: Agent tests access private PydanticAI attributes
- I34: No boundary value tests for priority queue
- I35: `_register_sqlite_type_compilers` permanently patches HALFVEC
- I36: Root conftest `sample_data` fixture unused
- I37: SSE event parsing duplicated in 2 test files
- I38: `_make_record` helper duplicated in 2 test files
- I39: 10+ untested frontend components

### Security
- I40: LIKE metacharacters not escaped in text search
- I41: `FileMetadataReader.read()` no path validation
- I42: `source_id` stores raw filesystem path in DB
- I43: No `.env.example` file
- I44: Test/dev Dockerfiles run as root

### Docs
- I45: 6 modules lack READMEs
- I46: `loguru`, `pandera`, `polars`, `asyncpg` never imported (forward-looking?)
- I47-I78: Various minor documentation, magic number, and style issues

</details>

---

## Fix Plan — TDD Tasks (Ordered by Impact)

Priority batch targeting CRITICAL + high-impact WARNING items:

### Batch 1: Config Single-Source-of-Truth (Python)
1. **T01**: Fix API version — import `__version__` in `app.py`
2. **T02**: Fix `acoustid_fingerprint` → `acoustid` field name in orchestrator
3. **T03**: Import confidence thresholds from `constants.py` everywhere
4. **T04**: Remove duplicate center-bias checks; rely on Pydantic validator
5. **T05**: Fix orchestrator fallback weights to reference `_DEFAULT_WEIGHTS`
6. **T06**: Extract shared tool logic (`explain_confidence`, `submit_feedback`) to `chat/tool_logic.py`
7. **T07**: Use `dependencies.get_db_session` in routes, delete `_get_session()` copies

### Batch 2: Frontend Deduplication
8. **T08**: Import `getConfidenceTier()` from canonical `confidence.ts`
9. **T09**: Add keyboard accessibility to `ConfidencePopover`
10. **T10**: Fix D3 consent graph re-render storm
11. **T11**: Extract shared `formatRole()`, `formatTimestamp()`, `isAllowValue()` utils

### Batch 3: Security & Validation
12. **T12**: Add `max_length` to search query parameter
13. **T13**: Handle `PermissionTypeEnum` ValueError → 400 (not 500)
14. **T14**: Restrict CORS methods/headers
15. **T15**: Fix `Settings()` double instantiation in `create_app`

### Batch 4: Test Quality
16. **T16**: Fix AST-only violation in `test_migration_002_structure.py`
17. **T17**: Rewrite tautological agent tests to call actual tool functions
18. **T18**: Extract shared `_make_attribution()` factory to `tests/factories.py`

### Batch 5: Docs & Build
19. **T19**: Remove 6 unused production dependencies from pyproject.toml
20. **T20**: Move `psycopg[binary]` to production deps
21. **T21**: Remove no-op `validate-guardrails` CI job
22. **T22**: Update test counts and sample data count in README
23. **T23**: Add missing gitignore entries
24. **T24**: Fix PRD node count references

---

## Methodology

Six specialized agents conducted parallel deep reviews:

1. **Config Duplication & Coupling** — Single-source-of-truth violations, config drift
2. **Backend Code Quality** — Dead code, type safety, error handling, API consistency
3. **Frontend Code Quality** — Component duplication, state management, accessibility, CSS compliance
4. **Test Quality & Coverage** — Tautological tests, missing edge cases, AST-only compliance
5. **Security & Input Validation** — SQL injection, XSS, path traversal, CORS, secret handling
6. **Documentation & Build Consistency** — README accuracy, dependency hygiene, CI/CD, gitignore

Each agent independently reviewed the codebase without knowledge of other agents' findings. Findings were then deduplicated and cross-referenced for the final report.
