# Protocol: Spec Adaptation (Plan vs. Reality Divergence)

## Purpose

Handle cases where the executable plan's TDD spec diverges from the actual codebase. The plan is a guide, not gospel — when it conflicts with reality, reality wins.

## When This Protocol Applies

- Plan references enum values that don't exist in the codebase
- Plan assumes an API that differs from the installed library version
- Plan specifies test assertions that don't match actual library behavior
- Plan's schema/model fields (e.g., Pydantic models, TypeScript interfaces) don't match the actual code
- Plan assumes methods are public when they're private (or vice versa)
- Plan specifies a module path that doesn't exist

## Core Rule

**The CODEBASE is the source of truth, not the plan.**

The plan was written before the code existed. As implementation progresses, schemas evolve, enum values get renamed, and library APIs behave differently than documented. Adapt to what IS, not what was planned.

## Steps

### 1. Detect Divergence

Before writing tests, verify the plan's assumptions:

```
For each import/reference in the TDD spec:
  1. Does the module exist? (check with: ls src/{path})
  2. Does the class/function exist? (read the source file)
  3. Do the enum values match? (read enums.py or equivalent)
  4. Do the Pydantic field names/types match? (read the schema)
  5. Does the third-party API work as the plan assumes? (check installed version)
```

### 2. Categorize the Divergence

| Category | Example | Severity |
|----------|---------|----------|
| Enum mismatch | Plan says `USER_INPUT`, code has `ARTIST_INPUT` | Low — simple rename |
| Field mismatch | Plan says `entity_name`, schema has `scope` | Low — simple rename |
| Missing required fields | Plan's test fixture omits required Pydantic fields | Medium — add fields |
| API mismatch | Plan says `splink.blocking_rules_library`, actual is `splink.block_on` | High — redesign test |
| Behavior mismatch | Plan assumes Splink EM converges with 5 records — it doesn't | High — redesign assertion |
| Private attribute | Plan says `matcher.threshold`, actual is `matcher._threshold` | Low — use private attr |

### 3. Adapt the Test

Apply the minimum change to align the test with reality:

1. **Rename** references to match actual enum/field names
2. **Add** missing required fields to test fixtures
3. **Change** assertion logic to match actual library behavior
4. **Mock** unavailable services or slow external calls

### 4. Document the Deviation

Add a brief comment in the test explaining why it deviates from the plan:

```python
# Adapted from plan: SourceEnum.USER_INPUT does not exist;
# the correct value is SourceEnum.ARTIST_INPUT (see enums.py)
```

For significant deviations (API redesign, behavior change), add a note to the state file's task entry.

## Common Patterns (from 27-task execution)

### Enum values
**Always** read `enums.py` (or equivalent) before using enum values in tests. Plan authors frequently use intuitive names that differ from the actual implementation.

Observed: `USER_INPUT` vs `ARTIST_INPUT`, `entity_name` vs `scope`

### Third-party library APIs
**Always** check the installed version and read the actual module before writing import statements.

Observed:
- Splink v4: `from splink import block_on` (top-level), NOT `splink.blocking_rules_library`
- Splink EM training: Doesn't converge with small synthetic data — test structure, not convergence

### Pydantic required fields
**Always** read the full Pydantic model before writing test fixtures. Plans often list only the "interesting" fields, omitting required ones.

Observed: `PermissionBundle` requires `scope`, `default_permission`, `created_by`, `updated_at`, `version` — plan's test helper only had `entity_id` and `permissions`.

### Private vs public attributes
Some classes use private attributes (prefixed with `_`) where the plan assumes public ones. Check the actual class definition.

Observed: `StringSimilarityMatcher._threshold` not `.threshold`

## Anti-Patterns

| Anti-Pattern | Why It Fails | What To Do Instead |
|--------------|-------------|-------------------|
| Trusting the plan blindly | Tests fail on wrong enum values, missing fields | Verify against actual code first |
| Silently changing tests | Future readers don't know why test differs from plan | Add a comment explaining the deviation |
| Changing the source to match the plan | Plan may be wrong; source may be downstream of other tasks | Source is truth; tests adapt |
| Ignoring the deviation | Recurring pattern — same mistake in future tasks | Record in self-correction-principles.md |

## Next Step

After adapting the spec, proceed with the normal [red-phase.md](red-phase.md) workflow.
