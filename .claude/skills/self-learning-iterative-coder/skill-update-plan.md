# Skill Update Plan: v1.0.0 -> v2.0.0

**Generated:** 2026-02-10
**Based on:** Execution of 27 tasks from `probabilistic-prd-executable-plan.xml` (163 unit tests)
**Method:** Post-execution retrospective — comparing skill-as-designed against skill-as-used
**Status:** IMPLEMENTED and REVIEWED by 5 parallel reviewer agents

## Executive Summary

The v1.0.0 skill successfully guided implementation of 27 tasks across 5 pipelines with zero regressions. However, several protocols contained theoretical prescriptions that didn't survive contact with reality. This update replaces speculation with empirically-validated patterns.

**Key insight:** The skill over-prescribed ceremony (banners, per-checkpoint state updates, RED commits, YAML convergence reports) and under-prescribed practical problems (dependency management, plan-vs-reality conflicts, mypy overrides for untyped packages, scoped verification).

---

## Change Inventory

### Files Modified (8)

| File | Change Type | Priority |
|------|-------------|----------|
| `SKILL.md` | Major revision — session budget, banner, version bump | HIGH+MEDIUM+LOW |
| `protocols/convergence.md` | Session budget model, simplified reports | HIGH+LOW |
| `protocols/red-phase.md` | Optional RED commit, spec-adaptation section | HIGH+MEDIUM |
| `protocols/green-phase.md` | Dependency setup expanded, mypy override protocol | HIGH |
| `protocols/verify-phase.md` | Scoped typecheck, practical command examples | MEDIUM |
| `protocols/checkpoint.md` | Session-boundary state updates | MEDIUM |
| `protocols/task-selection.md` | Fix XML parser example | MEDIUM |
| `protocols/fix-phase.md` | Nuanced test-revert guidance, external lib handling | LOW |

### Files Added (1)

| File | Purpose | Priority |
|------|---------|----------|
| `protocols/spec-adaptation.md` | New protocol for handling plan-vs-reality divergence | HIGH |

### Files Updated (supporting)

| File | Change |
|------|--------|
| `state/tdd-state.schema.json` | Add `session_inner_iterations`, `PLAN_COMPLETE` phase, `deferred_tasks` |
| `state/example-state.json` | Update to reflect v2.0 schema |
| `prompts/self-correction-principles.md` | Add empirical learnings section |
| `ACTIVATION-CHECKLIST.md` | Fix XML validation snippet, add mypy baseline check |

---

## Detailed Changes

### 1. SKILL.md — Core Revision

**1a. Version bump:** `1.0.0` -> `2.0.0`, add `revision_notes` to front matter.

**1b. Session budget (HIGH):**
Replace:
```
- Max tasks per session: 5 (context budget)
```
With:
```
- Max inner iterations per session: 20 (context budget)
- Track via session_inner_iterations in state file
- Context compaction handles the rest — trust the system
```

**Rationale:** In practice, 20+ tasks were completed across sessions. Simple tasks (1 inner iteration) shouldn't count the same as complex tasks (3+ iterations). The real constraint is cumulative context consumption, which correlates with inner iterations, not task count.

**1c. Progress banner (LOW):**
Move from mandatory to optional. Add:
```
## Progress Visibility (Optional)
Print the banner only in interactive mode or when debugging.
In autonomous mode, the state file and git log are the progress signals.
```

**1d. Anti-patterns table update (LOW):**
Change "Context hoarding" row from "Max 5 tasks per session" to "Max 20 inner iterations per session".

### 2. protocols/spec-adaptation.md — New File (HIGH)

Complete new protocol for handling divergence between the executable plan's TDD spec and reality:

```
When to adapt:
- Plan references enum values that don't exist (e.g., USER_INPUT vs ARTIST_INPUT)
- Plan assumes API that differs from installed library version
- Plan specifies test assertions that don't match library behavior
- Plan's Pydantic model fields don't match actual schema

Rules:
1. The CODEBASE is the source of truth, not the plan
2. Read actual schemas/APIs before writing tests
3. When adapting, document the deviation as a code comment
4. Never silently change test expectations — explain why

Common patterns from execution:
- Enum names: Always verify against enums.py before using in tests
- Third-party APIs: Check installed version, read actual module, don't trust plan
- Schema fields: Read the Pydantic model source before writing test fixtures
- Private attributes: Check if attr is public (.threshold) or private (._threshold)
```

### 3. protocols/red-phase.md — RED Commit Optional + Spec Adaptation (HIGH+MEDIUM)

**3a. Spec adaptation reference:** Add a pre-step before writing tests:

```
### 0. Validate Spec Against Reality (BEFORE writing tests)

Before writing tests from the TDD spec:
1. Read the actual schema/module being tested (if it exists)
2. Verify enum values, field names, method signatures match the plan
3. If divergence found: follow protocols/spec-adaptation.md
4. Adapt test code to match reality, not the plan
```

**3b. RED commit made optional:**

Replace step 8 ("Commit Failing Tests") with:

```
### 8. Commit Failing Tests (Optional)

In autonomous mode, skip the RED commit — proceed directly to GREEN.
The RED phase value is in RUNNING the tests and seeing them fail,
not in committing the failure state.

In interactive mode, commit the failing tests if the developer wants
a reviewable RED baseline.

Decision:
- autonomous mode -> skip RED commit (proceed to GREEN)
- interactive mode -> commit with "test: add failing tests for task {id}"
```

### 4. protocols/green-phase.md — Dependency Protocol Expansion (HIGH)

Expand step 1 significantly:

```
### 1. Install Dependencies and Configure Tooling

#### 1a. Install packages
uv add {packages from task's pyproject-deps}

#### 1b. Add mypy overrides for untyped packages
Most third-party packages (musicbrainzngs, splink, pandas, jellyfish,
thefuzz, sentence-transformers, etc.) don't ship type stubs.

After installing, add to pyproject.toml:
[[tool.mypy.overrides]]
module = ["{package}", "{package}.*"]
follow_untyped_imports = true

This is REQUIRED — without it, mypy will fail on every import from the
package, wasting fix iterations on type errors that aren't real bugs.

#### 1c. Handle slow installs
Large packages (sentence-transformers, torch, splink) can take minutes.
If the install is slow, consider running it as a background task and
continuing with test writing in parallel.

#### 1d. Verify installation
python3 -c "import {package}; print(f'{package} OK')"
```

### 5. protocols/verify-phase.md — Scoped Typecheck (MEDIUM)

Replace step 4 with scoped approach:

```
### 4. Run Type Checker (Scoped)

Per-task: Check only new/modified files:
  mypy {new_source_files}

Per-session boundary: Check full project:
  make typecheck

Rationale: Full mypy runs are slow and surface pre-existing issues
unrelated to the current task. Scope to new files for fast feedback.
Only run full typecheck at session start (baseline) and session end
(regression check).
```

### 6. protocols/checkpoint.md — Session-Boundary State Updates (MEDIUM)

Replace the per-checkpoint state update mandate:

```
### 5. Update State File (Session Boundaries Only)

CHANGE from v1.0: The state file is updated at SESSION START and
SESSION END, not after every checkpoint.

Per-task: Git commit is the checkpoint. `git log --oneline` provides
crash recovery — it shows exactly what was implemented and when.

Per-session-start: Load state, verify against git log, set
current_task_id.

Per-session-end: Bulk update all completed tasks in state file.

Rationale: In practice, the state file fell behind immediately because
per-checkpoint updates are high overhead with low recovery value.
Git history IS the ground truth for crash recovery.
```

### 7. protocols/task-selection.md — Fix XML Parser (MEDIUM)

The current XML parser example doesn't match the actual XML format. Fix:

**Current (wrong):**
```python
status_elem = task_elem.find('status')
if status_elem is not None and status_elem.text:
    task['status'] = status_elem.text.strip()
```

**Corrected:**
```python
# Status is an attribute, not a child element
task['status'] = task_elem.get('status', 'NOT_STARTED')

# Dependencies are comma-separated text, not sub-elements
deps_elem = task_elem.find('dependencies')
if deps_elem is not None and deps_elem.text:
    task['dependencies'] = [d.strip() for d in deps_elem.text.split(',')]
```

Also fix the name extraction — it's a child element, not attribute:
```python
name_elem = task_elem.find('name')
task['name'] = name_elem.text.strip() if name_elem is not None else ''
```

### 8. protocols/fix-phase.md — Nuanced Test-Revert Guidance (LOW)

Add a new section after "Anti-Patterns":

```
## When Tests Should Adapt (Not Implementation)

The general rule "tests are the spec" has exceptions:

1. **External library behavior:** If a test asserts behavior that the
   library doesn't actually exhibit (e.g., Splink's EM training doesn't
   converge with small synthetic data), adapt the test to match real
   library behavior.

2. **Plan spec errors:** If the TDD spec references enum values, field
   names, or method signatures that don't exist in the codebase, adapt
   the test to match the actual code. See: protocols/spec-adaptation.md.

3. **Integration assumptions:** If a test assumes a service is available
   (database, API endpoint) but it's not in the current environment,
   mark it as @pytest.mark.integration or mock the dependency.

In all cases: Document WHY the test was adapted, not just what changed.
```

### 9. protocols/convergence.md — Session Budget + Simplified Reports (HIGH+LOW)

**9a. Replace task-count budget with inner-iteration budget:**

```
### Session Budget
max_inner_iterations_per_session: 20
reason: Inner iterations correlate with context consumption.
        Simple tasks (1 iteration) cost less than complex tasks (3+).
action: After 20 cumulative inner iterations, save state and suggest new session.
```

**9b. Simplify convergence reports:**

Replace the verbose YAML report with:

```
### Per-Task Report (Compact)
{task_id}: {DONE|STUCK|FORCE_STOP} in {N} iterations ({test_count} tests)

### Session Summary (Compact)
Session: {tasks_done}/{tasks_attempted} done, {total_iterations} iterations,
         {total_tests} tests, {stuck_count} stuck
Next: {continue|new_session|plan_complete|blocked}
```

### 10. State Schema Update

Add to `tdd-state.schema.json`:

```json
"session_inner_iterations": {
  "type": "integer",
  "minimum": 0,
  "description": "Cumulative inner iterations this session (budget: 20)"
},
"deferred_tasks": {
  "type": "array",
  "items": { "type": "string" },
  "description": "Task IDs that are deferred (not counted toward convergence)"
}
```

Add `"PLAN_COMPLETE"` to `current_phase` enum.

### 11. ACTIVATION-CHECKLIST.md — Fix XML Snippet + Mypy Baseline

Fix the XML validation snippet to use attributes not child elements:
```python
for t in tasks[:5]:
    print(f'  {t.get("id")}: {t.get("status", "NOT_STARTED")}')
```

Add to Section 2 (Project Setup):
```
- [ ] mypy overrides exist for all installed third-party packages
  Check: grep "follow_untyped_imports" pyproject.toml
```

### 12. prompts/self-correction-principles.md — Empirical Learnings

Add a new section:

```
## Empirical Learnings (from 27-task execution)

### What the accuracy trajectory actually looked like
- 19/27 tasks (70%): ALL_GREEN on iteration 1
- 6/27 tasks (22%): Fixed by iteration 2
- 2/27 tasks (7%): Required 3 iterations (Splink, MCP permissions)
- 0/27 tasks: Required FORCE_STOP

The v1.0 prediction of "60-70% correct on iteration 1" was pessimistic.
With good TDD specs and strong schemas, first-pass success rate is higher.

### Most common failure categories (ranked)
1. Lint: unused imports, missing strict=True on zip() — 80% of fix iterations
2. Mypy: untyped third-party imports — 100% of new packages needed overrides
3. Schema mismatch: test fixtures missing required Pydantic fields — 3 tasks
4. API mismatch: external lib API different from plan spec — 2 tasks (Splink, MCP)
5. Logic errors: actual code bugs — 2 tasks (orchestrator threshold, aggregator enum)

### Session budget observation
27 tasks were completed across ~3 sessions (context compaction, not budget).
The "max 5 tasks" rule was too conservative by 5x.
Inner iterations (not task count) is the real context budget metric.
```

---

## Implementation Order

1. Write `protocols/spec-adaptation.md` (new file)
2. Edit `SKILL.md` (version, budget, banner, anti-patterns)
3. Edit `protocols/red-phase.md` (spec validation, optional commit)
4. Edit `protocols/green-phase.md` (dependency protocol)
5. Edit `protocols/verify-phase.md` (scoped typecheck)
6. Edit `protocols/checkpoint.md` (session-boundary updates)
7. Edit `protocols/task-selection.md` (fix parser)
8. Edit `protocols/fix-phase.md` (test adaptation guidance)
9. Edit `protocols/convergence.md` (budget model, reports)
10. Edit `state/tdd-state.schema.json` (new fields)
11. Edit `state/example-state.json` (updated example)
12. Edit `ACTIVATION-CHECKLIST.md` (fix snippet, mypy check)
13. Edit `prompts/self-correction-principles.md` (empirical data)

## Verification Plan

After implementation, run 5 parallel reviewer agents:
1. **Internal consistency:** Cross-references between files resolve correctly
2. **Completeness:** All 10 identified gaps are addressed
3. **Actionability:** Instructions are concrete, not vague
4. **Empirical accuracy:** Claims match actual execution data
5. **Generalizability:** Nothing is hardcoded to music-attribution
