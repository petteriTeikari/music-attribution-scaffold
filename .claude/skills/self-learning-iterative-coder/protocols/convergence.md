# Protocol: Convergence (Quality Gate Check)

## Purpose

Determine whether the current task is DONE (all quality gates passed) or needs another iteration. Also checks plan-level convergence (all tasks done) and session-level budgets.

## Per-Task Convergence (Inner Loop)

### Hard Gates (ALL must be true)

| Gate | Condition | Source |
|------|-----------|--------|
| Tests pass | All tests for this task pass | `pytest {test_file}` |
| No regressions | Previously passing tests still pass | `make test` full suite |
| Lint clean | No new lint errors introduced | `make lint` |
| Typecheck clean | No new type errors introduced | `make typecheck` |

### Soft Gates (SHOULD be true)

| Gate | Condition | Source |
|------|-----------|--------|
| Acceptance criteria | All criteria from plan's `acceptance-criteria` met | Manual check against plan |

### Decision Logic

```
if all hard gates PASS:
    if soft gates PASS:
        -> Task status = DONE
        -> Record convergence report
        -> Continue outer loop (next task)
    else:
        -> Log which soft gates failed
        -> If inner_iteration < max (5): another iteration targeting soft gates
        -> If inner_iteration >= max (5): FORCE_STOP, mark as DONE_WITH_CAVEATS

if any hard gate FAILS:
    if inner_iteration < max_inner_iterations (5):
        -> Another iteration (back to FIX phase)
    else:
        -> FORCE_STOP: log residual failures, mark as STUCK
```

### Ceiling Detection

Track whether progress is being made:

```
if last 2 iterations have identical failure sets:
    -> STUCK (same failures, no progress)
    -> Action: Log stuck issue, FORCE_STOP
    -> Suggestion: Human review needed

if failure count is decreasing:
    -> PROGRESSING (continue iterations)

if failure count is increasing:
    -> DIVERGING (something is getting worse)
    -> Action: Consider reverting last fix, try different approach
```

### Max Inner Iterations

**Default: 5 iterations per task.**

Rationale:
- Iteration 1: ~60-70% correct (initial implementation)
- Iteration 2: ~80% correct (first round of fixes)
- Iteration 3: ~90% correct (targeted fixes for remaining issues)
- Iteration 4-5: Diminishing returns — if not green by iteration 5, it's likely a design issue

## Per-Plan Convergence (Outer Loop)

### Completion Condition

```
plan_converged = all tasks with status in {DONE, DEFERRED, DONE_WITH_CAVEATS}
```

### Session Budget

```yaml
max_tasks_per_session: 5
reason: Context budget — LLMs degrade with very long conversations
action: After 5 tasks, output summary and suggest new session
```

### Force Stop Conditions

```yaml
force_stop_conditions:
  - all_eligible_tasks_stuck: true
    # Every remaining non-deferred task is STUCK
  - session_task_count >= 5
    # Context budget exceeded
  - no_eligible_tasks:
    # All remaining tasks have unmet dependencies (blocked)
```

## Convergence Report

Generate after each task completes:

### Per-Task Report

```yaml
task_convergence_report:
  task_id: "{id}"
  task_name: "{name}"
  status: DONE|STUCK|FORCE_STOP|DONE_WITH_CAVEATS
  inner_iterations: N
  test_trajectory:
    - {iteration: 1, pass: 0, fail: 5, errors: 2}
    - {iteration: 2, pass: 5, fail: 2, errors: 0}
    - {iteration: 3, pass: 7, fail: 0, errors: 0}
  lint_trajectory: [FAIL(3), PASS, PASS]
  type_trajectory: [FAIL(1), PASS, PASS]
  residual_issues: []
  commit_hashes: ["abc123", "def456", "ghi789"]
  started_at: "2026-02-10T14:00:00Z"
  completed_at: "2026-02-10T14:30:00Z"
```

### Session Summary

```yaml
session_summary:
  tasks_attempted: N
  tasks_done: D
  tasks_stuck: S
  tasks_remaining: R
  total_inner_iterations: I
  total_commits: C
  convergence: {true|false}
  next_action: "Continue in new session"|"Plan complete"|"Blocked — needs human review"
```

## Output

```
CONVERGENCE CHECK — Task {task_id}
  Hard gates: {PASS|FAIL} ({details})
  Soft gates: {PASS|FAIL} ({details})
  Inner iterations used: {N}/{max}
  Decision: {DONE|ANOTHER_ITERATION|FORCE_STOP}

  Plan progress: {done}/{total} tasks DONE
  Session budget: {used}/{max} tasks this session
```

## Next Step

- If task DONE -> [task-selection.md](task-selection.md) (next task)
- If ANOTHER_ITERATION -> [fix-phase.md](fix-phase.md) (or [red-phase.md](red-phase.md) if tests need revision)
- If FORCE_STOP -> [task-selection.md](task-selection.md) (skip to next task)
- If plan converged -> Output final summary and exit
- If session budget exceeded -> Output session summary and suggest new session
