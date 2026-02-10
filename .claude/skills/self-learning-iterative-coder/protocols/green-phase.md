# Protocol: Green Phase (Implement Code)

## Purpose

Write the MINIMUM code necessary to make the failing tests pass. This is not the refactoring step — write clean code, but don't over-engineer beyond what the tests require.

## Inputs

- Failing tests from [red-phase.md](red-phase.md)
- TDD spec's `then-implement` block
- Task's `pyproject-deps` (dependencies to install)
- Project conventions from `CLAUDE.md`

## Steps

### 1. Install Dependencies and Configure Tooling

If the task specifies `pyproject-deps`, install and configure them:

#### 1a. Install packages

```bash
# For uv-managed Python projects:
uv add {package1} {package2}

# For dev-only dependencies:
uv add --group dev {package}
```

**Do NOT skip this step.** Missing dependencies cause confusing import errors that waste fix iterations.

#### 1b. Add mypy overrides for untyped packages

**For Python projects using mypy:** Most third-party packages (musicbrainzngs, splink, pandas, jellyfish, thefuzz, sentence-transformers, etc.) don't ship type stubs. Without explicit overrides, mypy fails on every import from these packages. For TypeScript, equivalent issues arise with missing `@types/` packages; for Rust, type checking is built-in.

After installing a new third-party package, check if mypy needs an override:

```bash
# Quick check: run mypy on a file that imports the package
mypy {source_file_that_imports_package}
# If mypy reports "Skipping analyzing" or "Library stubs not installed",
# the package needs an override.
```

If the package is untyped (mypy errors on import), add to `pyproject.toml`:

```toml
[[tool.mypy.overrides]]
module = ["{package}", "{package}.*"]
follow_untyped_imports = true
```

**This is required** — without it, mypy produces false-positive type errors on every import from the package, wasting fix iterations on non-bugs.

#### 1c. Handle slow installs

Large packages (sentence-transformers + torch, splink + DuckDB) can take minutes to install. If the install takes more than 60 seconds:
- Run it as a background task
- Do NOT proceed to the smoke test (step 6) until the install completes
- Verify the install succeeded before running any tests

#### 1d. Verify installation

```bash
python3 -c "import {package}; print(f'{package} version: {package}.__version__')"
```

### 2. Read the TDD Spec

Extract the `then-implement` block. This contains:
- Source file path(s) to create or modify
- Class/function signatures to implement
- Implementation guidance (algorithms, patterns, libraries to use)
- Pydantic models, type definitions, constants

### 3. Create Source File(s)

Follow project conventions (from `CLAUDE.md` or equivalent):
- Use the project's file template and header conventions
- Organize imports per project style (e.g., stdlib / third-party / local for Python)
- Type hints on all public functions
- Documentation on all modules, classes, and public functions

### 4. Implement Per Spec

Write the implementation following the TDD spec:
- Implement exactly what the tests require — no more, no less
- Follow the Pydantic model definitions exactly (field names, types, validators)
- Use the libraries specified in the task
- Respect project conventions (Path not strings, encoding='utf-8', etc.)

### 5. Create `__init__.py` and Package Structure

If creating new source modules:
- Create `__init__.py` files in new packages
- Add `__all__` exports if the module is part of the public API
- Update `src/{package}/__init__.py` if new submodules need re-exporting

### 6. Quick Smoke Test

Before running the full verification suite, do a quick import check:

```bash
python3 -c "from {module} import {class_or_function}; print('Import OK')"
```

This catches basic syntax errors and missing imports before the full test run.

## Anti-Patterns

| Anti-Pattern | Why It's Wrong | What To Do Instead |
|--------------|---------------|-------------------|
| Over-engineering | Adds complexity not tested, risks breaking things | Write minimum code for green tests |
| Adding features not in TDD spec | Scope creep, untested code | Stick to the spec |
| Skipping dependency installation | Confusing import errors waste iterations | Install deps first |
| Hardcoding values | Fails in different environments | Use config, constants, or parameters |
| Ignoring project conventions | Lint/type errors in verify phase | Read CLAUDE.md, follow patterns |
| Creating files in wrong location | Import resolution fails | Follow the paths in the TDD spec |

## Output

After completing the GREEN phase:
```
GREEN PHASE COMPLETE — Task {task_id}
  Source file(s): {list of files created/modified}
  Dependencies added: {list or "none"}
  Quick import check: PASS
```

## State Update

```json
{
  "current_phase": "GREEN",
  "tasks": {
    "{task_id}": {
      "source_files": ["{source_file_paths}"],
      "deps_added": ["{packages}"]
    }
  }
}
```

## Next Step

Proceed to [verify-phase.md](verify-phase.md).
