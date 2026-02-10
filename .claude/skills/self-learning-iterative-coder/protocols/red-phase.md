# Protocol: Red Phase (Write Failing Tests)

## Purpose

Write FAILING tests BEFORE any implementation code. This is the foundational TDD step — tests define the contract that the implementation must satisfy.

## Inputs

- Selected task from [task-selection.md](task-selection.md)
- TDD spec's `first-write-these-tests` block
- Project test conventions (from `CLAUDE.md`)

## Steps

### 0. Validate Spec Against Reality

**Before writing any tests**, verify the plan's assumptions against the actual codebase:

1. If the module being tested already exists, **read the source** to check enum values, field names, method signatures, and required Pydantic fields.
2. If a third-party library is involved, check the **installed version** and verify the API matches the plan.
3. If divergence is found, follow [spec-adaptation.md](spec-adaptation.md) to adapt the test to reality.

This step prevents the most common failure mode: tests that fail not because the implementation is wrong, but because the plan spec was stale or inaccurate.

### 1. Read the TDD Spec

Extract the `first-write-these-tests` block from the selected task. This contains:
- Test file path(s) to create
- Test function signatures and descriptions
- Expected behaviors to verify
- Fixtures or test data needed

### 2. Create Test File(s)

Create the test file at the specified path. Follow project conventions:
- Use the project's test template (from `CLAUDE.md` or `conftest.py`)
- Add `from __future__ import annotations` at the top
- Import the module being tested (even though it doesn't exist yet)
- Import `pytest` and any needed fixtures

### 3. Write ALL Test Functions

Write every test function specified in the TDD spec:
- Each test should have a clear docstring explaining what it verifies
- Use Arrange-Act-Assert pattern
- Include edge cases if specified in the spec
- Use parametrize for data-driven tests when appropriate
- Write assertions that will FAIL until the implementation exists

### 4. Add Fixtures and Helpers

Create any necessary:
- Pytest fixtures (in conftest.py or inline)
- Test data files (in `tests/fixtures/`)
- Helper functions for complex assertions

### 5. Create `__init__.py` Files

If the test file is in a new subdirectory, create `__init__.py`:
```bash
touch tests/unit/__init__.py  # if it doesn't exist
```

### 6. Run Tests — They MUST Fail

```bash
pytest {test_file} -v
```

**Expected outcomes:**
- `ImportError` — Module doesn't exist yet (correct!)
- `AttributeError` — Class/function doesn't exist yet (correct!)
- `AssertionError` — Logic not implemented yet (correct!)
- All tests PASS — something is wrong (investigate!)

### 7. Investigate Unexpected Passes

If tests pass before implementation:
- The code might already exist from a previous task
- The tests might be trivially true (testing nothing)
- The imports might resolve to a different module

**Action:** If tests pass unexpectedly, review each test to ensure it's actually testing the intended behavior. Add more specific assertions if needed.

### 8. Commit Failing Tests (Optional)

The RED phase's value is in **running the tests and seeing them fail**, confirming that the tests actually test something. The separate commit is optional.

**Autonomous mode:** Skip the RED commit. Proceed directly to [green-phase.md](green-phase.md). Tests and implementation will be committed together after verification.

**Interactive mode:** Commit the failing tests if the developer wants a reviewable RED baseline:
```bash
git add {test_files}
git commit -m "test: add failing tests for task {task_id} — {task_name}"
```

## Anti-Patterns

| Anti-Pattern | Why It's Wrong | What To Do Instead |
|--------------|---------------|-------------------|
| Writing implementation alongside tests | Violates RED-GREEN separation | Complete RED phase first, then GREEN |
| Writing tests that pass immediately | Testing nothing — no specification value | Ensure tests assert behavior that requires implementation |
| Skipping test execution | Must confirm tests fail before implementing | Always run tests in RED phase, even if not committing |
| Copy-pasting tests without understanding | Tests won't catch real bugs | Understand what each test verifies |
| Importing from wrong module | Tests pass against wrong code | Verify import paths match the plan |
| Forgetting `__init__.py` | Import resolution fails in confusing ways | Create `__init__.py` in new test dirs |

## Output

After completing the RED phase:
```
RED PHASE COMPLETE — Task {task_id}
  Test file(s): {list of test files created}
  Test count: {N} tests written
  Status: ALL FAILING (expected)
  Spec adaptations: {count or "none"}
  Commit: {commit_hash or "deferred to GREEN"}
```

## State Update

```json
{
  "current_phase": "RED",
  "inner_iteration": N,
  "tasks": {
    "{task_id}": {
      "status": "IN_PROGRESS",
      "red_commit": "{commit_hash}",
      "test_files": ["{test_file_paths}"],
      "test_count": N
    }
  }
}
```

## Next Step

Proceed to [green-phase.md](green-phase.md).
