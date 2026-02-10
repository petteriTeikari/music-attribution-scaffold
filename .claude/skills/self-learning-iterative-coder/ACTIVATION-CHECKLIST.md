# Activation Checklist

Run through this checklist before starting the iterative TDD loop. Every item must be confirmed before proceeding.

## 1. Plan File

- [ ] Plan file exists and is readable (XML, YAML, or JSON)
- [ ] Plan file path is recorded in state file under `plan_file`
- [ ] Plan has task elements with `id`, `status`, `dependencies`
- [ ] At least one task has status `NOT_STARTED`

**How to check:**
```bash
# For XML plans (status is an attribute, not child element):
python3 -c "
import xml.etree.ElementTree as ET
tree = ET.parse('path/to/plan.xml')
tasks = list(tree.iter('task'))
print(f'Found {len(tasks)} tasks')
for t in tasks[:5]:
    name_elem = t.find('name')
    name = name_elem.text.strip() if name_elem is not None and name_elem.text else 'unnamed'
    print(f'  {t.get(\"id\")}: {t.get(\"status\", \"NOT_STARTED\")} — {name}')
"
```

## 2. Project Setup

- [ ] Project has a working test command (e.g., `make test`, `pytest`)
- [ ] Project has a working lint command (e.g., `make lint`, `ruff check`)
- [ ] Project has a working typecheck command (e.g., `make typecheck`, `mypy`)
- [ ] All three commands run successfully on current codebase (baseline is green)

**How to check:**
```bash
make test && echo "TESTS: OK" || echo "TESTS: FAILING"
make lint && echo "LINT: OK" || echo "LINT: FAILING"
make typecheck && echo "TYPES: OK" || echo "TYPES: FAILING"
```

**If baseline is not green:** Fix existing issues first. The iterative loop assumes a green baseline — it detects regressions, not pre-existing problems.

## 3. Dependencies

- [ ] Package manager is available (e.g., `uv`, `npm`, `cargo`)
- [ ] Lock file is up to date (`uv.lock`, `package-lock.json`)
- [ ] Dev dependencies are installed (`uv sync`, `npm install`)
- [ ] Type checker is configured for third-party dependencies (e.g., mypy overrides for Python, `skipLibCheck` for TypeScript)

**How to check (Python/mypy):**
```bash
grep "follow_untyped_imports" pyproject.toml
# If a package you import causes mypy errors, add an override
```

## 4. State File

- [ ] State file exists at `state/tdd-state.json` (or will be created on first run)
- [ ] If resuming: state file reflects accurate progress (check `current_task_id` and `current_phase`)
- [ ] If fresh start: state file is initialized with plan metadata

**Initialize state (fresh start):**
```json
{
  "plan_file": "path/to/plan.xml",
  "plan_version": "1.0",
  "execution_mode": "autonomous",
  "current_task_id": null,
  "current_phase": null,
  "inner_iteration": 0,
  "tasks": {},
  "convergence": {
    "reached": false,
    "tasks_done": 0,
    "tasks_total": 0,
    "tasks_stuck": 0
  },
  "session_task_count": 0,
  "session_inner_iterations": 0,
  "session_start": "2026-01-01T00:00:00Z"
}
```

## 5. Project Conventions

- [ ] Read project's `CLAUDE.md` (root and `.claude/CLAUDE.md`)
- [ ] Note the package manager (uv, npm, cargo, etc.)
- [ ] Note forbidden patterns (grep for code analysis, pip, etc.)
- [ ] Note required patterns (encoding, paths, timezone, etc.)
- [ ] Note test framework and conventions

**Record conventions summary:**
```
Package manager: ___
Test command: ___
Lint command: ___
Typecheck command: ___
Forbidden: ___
Required patterns: ___
```

## 6. Execution Mode

- [ ] Choose execution mode:
  - **autonomous**: Run through tasks without pausing (Ralph Wiggum mode)
  - **interactive**: Pause after each task for developer review

- [ ] Confirm git branch is appropriate (feature branch, not main)
- [ ] Confirm working directory is clean (`git status` shows no uncommitted changes)

## Ready to Start

Once all checks pass, proceed to [protocols/task-selection.md](protocols/task-selection.md) to pick the first task.
