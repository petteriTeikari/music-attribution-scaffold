# Protocol: Fix Phase (Analyze & Fix Failures)

## Purpose

Analyze failures from the VERIFY phase and apply targeted, reasoned fixes. This is where self-correction happens — the core of the Ralph Wiggum philosophy.

## Inputs

- Verification results from [verify-phase.md](verify-phase.md)
- List of specific failures with messages and file:line references
- Previous fix attempts (from state, to avoid repeating the same fix)

## Steps

### 1. Categorize Failures

Sort all failures into categories:

| Category | Source | Priority | Typical Fix |
|----------|--------|----------|-------------|
| Test failures | `pytest` | HIGH | Fix implementation logic |
| Import errors | `pytest` | CRITICAL | Fix module paths, missing deps |
| Regressions | `pytest` (full suite) | CRITICAL | Revert or adjust implementation |
| Lint errors | `ruff` / linter | MEDIUM | Apply auto-fix or manual fix |
| Type errors | `mypy` / type checker | MEDIUM | Add/fix type annotations |

### 2. Fix in Priority Order

**CRITICAL first, then HIGH, then MEDIUM.**

#### Import Errors
- Check module paths match the project structure
- Verify dependencies are installed (`uv add` if missing)
- Check `__init__.py` files exist in all packages
- Check for circular imports

#### Regressions
- Read the failing test to understand what it expects
- Read the implementation change that caused the regression
- Fix without breaking the new tests (may require redesign)

#### Test Failures
- Read the failing test assertion carefully
- Read the implementation code being tested
- Identify the root cause (wrong return value, missing field, incorrect logic)
- Make the minimum change to fix the failure

#### Lint Errors
- Try auto-fix first (e.g., `ruff check --fix` for Python, `eslint --fix` for TypeScript, `cargo clippy --fix` for Rust)
- For non-auto-fixable issues, read the rule and fix manually
- Common fixes: unused imports, missing docstrings, line length

#### Type Errors
- Read the mypy error message and the code it points to
- Add type annotations where missing
- Fix type mismatches (wrong return type, nullable types, etc.)
- For Python: use `TYPE_CHECKING` blocks for import-only types

### 3. Apply Fixes Incrementally

Make ONE category of fixes at a time. Don't shotgun-fix everything simultaneously:

```
Iteration N.1: Fix import errors -> re-verify
Iteration N.2: Fix test failures -> re-verify
Iteration N.3: Fix lint + type errors -> re-verify
```

### 4. Micro-Verify After Each Fix Category

After each fix category, run a quick re-verify (focused test only):
```bash
pytest {test_file} -v
```

If the focused test passes, run full verify. This avoids expensive full-suite runs for each micro-fix.

**Max micro-fix attempts per fix cycle: 3.** If the same failure persists after 3 attempts at the same category, mark it as STUCK.

### 5. Check for Fix Loops

Compare current failures against previous iteration's failures:
- **Same failures, same count**: Fix didn't work. Try a different approach.
- **Different failures**: Progress is being made. Continue.
- **More failures than before**: Fix introduced new problems. Revert the fix.
- **Same failure for 2 consecutive fix attempts**: Mark as STUCK.

## Escalation

When a failure is marked STUCK:

```
STUCK: {failure_description}
  Attempted fixes: {list of what was tried}
  Root cause hypothesis: {best guess}
  Recommendation: {human intervention needed / design issue / skip and continue}
```

Include STUCK items in the convergence report. The convergence protocol decides whether to FORCE_STOP or continue.

## When Tests Should Adapt (Not Implementation)

The general rule is "tests are the spec — implementation adapts." But there are legitimate exceptions discovered through execution:

### 1. External library behavior mismatch
If a test asserts behavior that the library doesn't actually exhibit, adapt the test to match real library behavior. Don't try to force the library to behave differently.

**Example:** Splink's EM training doesn't converge with small synthetic datasets. The test was changed from "blocking reduces comparisons" to "predict returns valid pair DataFrame" — testing structure, not convergence.

### 2. Plan spec errors
If the TDD spec references enum values, field names, or method signatures that don't exist in the codebase, adapt the test to match the actual code. See [spec-adaptation.md](spec-adaptation.md).

**Example:** `SourceEnum.USER_INPUT` doesn't exist — correct value is `SourceEnum.ARTIST_INPUT`.

### 3. Integration environment assumptions
If a test assumes a service is available (database, API endpoint) but it's not in the current environment, mark it as `@pytest.mark.integration` or mock the dependency.

**In all cases:** Document WHY the test was adapted, not just what changed.

## Anti-Patterns

| Anti-Pattern | Why It Fails | What To Do Instead |
|--------------|-------------|-------------------|
| Shotgun fix | Changes too many things, can't tell what helped | One fix category at a time |
| Same fix twice | Definition of insanity | Track attempted fixes, try different approach |
| Suppressing errors | `# type: ignore`, `# noqa` without justification | Fix the actual issue |
| Reverting tests for convenience | Weakening tests to hide implementation bugs | Fix implementation, not tests |
| Adding try/except broadly | Hides bugs, breaks debugging | Handle specific exceptions only |
| Fixing symptoms not causes | Problem recurs in different form | Understand root cause first |

## Output

```
FIX PHASE COMPLETE — Task {task_id} — Iteration {N}
  Fixes applied: {count}
  Categories: {import: N, test: N, lint: N, type: N}
  Stuck items: {count or "none"}
  Ready for re-verify: YES
```

## State Update

```json
{
  "current_phase": "FIX",
  "tasks": {
    "{task_id}": {
      "fix_attempts": [
        {
          "iteration": N,
          "category": "test_failure",
          "description": "Fixed return type in {function}",
          "result": "resolved|persists|new_failure"
        }
      ]
    }
  }
}
```

## Next Step

Return to [verify-phase.md](verify-phase.md) to re-run the verification suite.
