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
max_inner_iterations_per_session: 20
reason: >
  Inner iterations correlate with context consumption.
  Simple tasks (1 iteration) cost less than complex tasks (3+).
  In practice, 70% of tasks complete in 1 iteration.
action: After 20 cumulative inner iterations, save state and suggest new session.
```

**v2.0 change:** Replaced `max_tasks_per_session: 5` with inner-iteration budget. During the 27-task execution, the task-count limit was too conservative by 5x. Inner iterations are the real context consumption metric.

### Force Stop Conditions

```yaml
force_stop_conditions:
  - all_eligible_tasks_stuck: true
    # Every remaining non-deferred task is STUCK
  - session_inner_iterations >= 20
    # Context budget exceeded
  - no_eligible_tasks:
    # All remaining tasks have unmet dependencies (blocked)
```

## Convergence Report (Compact)

**v2.0 change:** Simplified from verbose YAML to compact format. The state file carries the detailed data; the report is for human readability.

### Per-Task Report

```
{task_id}: {DONE|STUCK|FORCE_STOP} in {N} iterations ({test_count} tests) [{commit_hash}]
```

Example:
```
2.3b: DONE in 3 iterations (5 tests) [ff73459]
3.1:  DONE in 2 iterations (5 tests) [946d01e]
3.2:  DONE in 1 iteration  (5 tests) [237a539]
```

### Session Summary

```
Session: {tasks_done}/{tasks_attempted} done, {total_iterations} inner iterations,
         {total_tests} tests, {stuck_count} stuck
Next: {continue|new_session|plan_complete|blocked}
```

Example:
```
Session: 13/13 done, 17 inner iterations, 75 tests, 0 stuck
Next: continue (budget: 17/20 iterations used)
```

## Output

```
CONVERGENCE CHECK — Task {task_id}
  Hard gates: {PASS|FAIL} ({details})
  Soft gates: {PASS|FAIL} ({details})
  Inner iterations used: {N}/{max per task}
  Decision: {DONE|ANOTHER_ITERATION|FORCE_STOP}

  Plan progress: {done}/{total} tasks DONE
  Session budget: {used}/{max} inner iterations this session
```

## Next Step

- If task DONE -> [task-selection.md](task-selection.md) (next task)
- If ANOTHER_ITERATION -> [fix-phase.md](fix-phase.md) (or [red-phase.md](red-phase.md) if tests need revision)
- If FORCE_STOP -> [task-selection.md](task-selection.md) (skip to next task)
- If plan converged -> Output final summary and exit
- If session budget exceeded -> Output session summary and suggest new session
