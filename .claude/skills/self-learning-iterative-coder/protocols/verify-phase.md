# Protocol: Verify Phase (Run Full Verification Suite)

## Purpose

Run the complete verification suite — tests, linter, and type checker — to assess whether the implementation satisfies all quality gates. This is the "reviewer" that replaces human code review.

## Inputs

- Implementation from [green-phase.md](green-phase.md) (or fixes from [fix-phase.md](fix-phase.md))
- Verification commands (project-specific)

## Verification Commands

These are configurable per project. Detect from `Makefile`, `pyproject.toml`, or `package.json`:

```yaml
# Default for Python projects with Makefile:
verification_commands:
  focused_test: "pytest {test_file} -v"     # Just this task's tests
  all_tests: "make test"                     # Full test suite (regression check)
  lint: "make lint"                          # Linter
  typecheck: "make typecheck"               # Type checker

# Alternative (no Makefile):
verification_commands:
  focused_test: "pytest {test_file} -v"
  all_tests: "pytest tests/ -v"
  lint: "ruff check src/ tests/"
  typecheck: "mypy src/"
```

## Steps

### 1. Run Focused Tests

Run only this task's test file first (fast feedback):
```bash
pytest {test_file} -v
```

Record: pass count, fail count, error count.

### 2. Run Full Test Suite

Run the complete test suite to check for regressions:
```bash
make test
```

Record: pass count, fail count, error count. Compare against baseline.

### 3. Run Linter

```bash
make lint
```

Record: issue count, issue types.

### 4. Run Type Checker (Scoped)

**Per-task:** Check only the new/modified source files for fast feedback:
```bash
# Python:     mypy {new_source_file1} {new_source_file2}
# TypeScript: npx tsc --noEmit {new_source_file1}
# Rust:       cargo check (always full-project)
```

**Per-session boundary (start and end):** Check the full project:
```bash
make typecheck  # or project-specific equivalent
```

Record: error count, error types.

**Rationale:** Full mypy runs are slow and can surface pre-existing issues unrelated to the current task. Scoping to new files gives fast, targeted feedback. Run full typecheck at session boundaries to catch regressions.

### 5. Compile Results

Produce a structured verification result:

```yaml
verify_result:
  focused_tests:
    status: PASS|FAIL
    passed: N
    failed: M
    errors: K
  all_tests:
    status: PASS|FAIL
    passed: N
    failed: M
    errors: K
    regressions: [list of previously passing tests that now fail]
  lint:
    status: PASS|FAIL
    issues: N
    auto_fixable: M
  typecheck:
    status: PASS|FAIL
    errors: N
  overall: ALL_GREEN|FAILING
  failures: [list of specific failure messages with file:line references]
```

## Decision Logic

```
if overall == ALL_GREEN:
    -> Skip FIX phase, proceed to CHECKPOINT
elif inner_iteration >= max_inner_iterations (5):
    -> FORCE_STOP: log failures, proceed to CHECKPOINT with status STUCK
else:
    -> Proceed to FIX phase
```

## Regression Detection

A regression is a test that passed before the current task's changes but now fails.

To detect:
1. Compare current full test results against the last green checkpoint
2. Any test not in the current task's test file that changed from PASS to FAIL is a regression
3. Regressions are high-priority fixes — they indicate the implementation broke existing functionality

## Output

```
VERIFY PHASE COMPLETE — Task {task_id} — Iteration {N}
  Focused tests: {pass}/{total} passed
  Full tests: {pass}/{total} passed ({regression_count} regressions)
  Lint: {issue_count} issues ({auto_fixable} auto-fixable)
  Typecheck: {error_count} errors
  Overall: {ALL_GREEN|FAILING}
```

## State Update

```json
{
  "current_phase": "VERIFY",
  "tasks": {
    "{task_id}": {
      "test_results": [
        {"iteration": N, "pass": P, "fail": F, "errors": E, "lint_issues": L, "type_errors": T, "overall": "ALL_GREEN|FAILING"}
      ]
    }
  }
}
```

## Next Step

- If `ALL_GREEN` -> [checkpoint.md](checkpoint.md)
- If `FAILING` -> [fix-phase.md](fix-phase.md)
