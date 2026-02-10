# Protocol: Task Selection

## Purpose

Parse the executable plan, evaluate task dependencies, and select the next eligible task for the inner TDD loop.

## Inputs

- **Plan file**: Path to the executable plan (XML, YAML, or JSON)
- **State file**: Current `tdd-state.json` with task statuses

## Algorithm

```
1. Parse plan file → extract all tasks
2. Load state file → overlay stored statuses onto plan tasks
3. Filter to tasks where:
   - status is NOT_STARTED or IN_PROGRESS
   - status is NOT DONE, DEFERRED, or BLOCKED
4. For each candidate task, check dependency graph:
   - All tasks listed in `dependencies` must have status DONE
   - If any dependency is not DONE → task is BLOCKED (skip)
5. From eligible tasks, select the one with the lowest ID
   (preserves plan ordering / priority)
6. Load task details: TDD spec, acceptance criteria, dependencies
7. Update state: set current_task_id, current_phase = "RED"
```

## Expected Plan Format

The protocol expects plans with these elements. All formats (XML, YAML, JSON) must provide equivalent information.

### Required Fields

| Field | Description | Example |
|-------|-------------|---------|
| `id` | Unique task identifier | `"0.1"`, `"1.2a"` |
| `status` | Current status | `NOT_STARTED`, `IN_PROGRESS`, `DONE`, `DEFERRED`, `BLOCKED` |
| `dependencies` | List of task IDs that must be DONE first | `["0.1", "0.2"]` |

### Expected Fields (for TDD)

| Field | Description |
|-------|-------------|
| `tdd-spec.first-write-these-tests` | Test code or test descriptions to write in RED phase |
| `tdd-spec.then-implement` | Implementation guidance for GREEN phase |
| `acceptance-criteria` | Conditions for task to be considered DONE |
| `pyproject-deps` | Dependencies to install before implementation |

### Optional Fields

| Field | Description |
|-------|-------------|
| `name` | Human-readable task name |
| `description` | Detailed task description |
| `pipeline` | Which pipeline this task belongs to |
| `phase` | Which plan phase this task belongs to |

## XML Parsing Example

This example matches the actual XML format used in `probabilistic-prd-executable-plan.xml`. Adapt as needed for other plan formats.

```python
import xml.etree.ElementTree as ET

def parse_xml_plan(plan_path):
    tree = ET.parse(plan_path)
    root = tree.getroot()
    tasks = []

    for task_elem in root.iter('task'):
        task = {
            'id': task_elem.get('id'),
            # Status is an ATTRIBUTE on <task>, not a child element
            'status': task_elem.get('status', 'NOT_STARTED'),
            'name': '',
            'dependencies': [],
            'tdd_spec': {},
            'acceptance_criteria': [],
            'pyproject_deps': [],
        }

        # Name is a child element: <name>Task Name</name>
        name_elem = task_elem.find('name')
        if name_elem is not None and name_elem.text:
            task['name'] = name_elem.text.strip()

        # Dependencies are COMMA-SEPARATED text, not sub-elements
        # Example: <dependencies>0.1, 0.2</dependencies>
        deps_elem = task_elem.find('dependencies')
        if deps_elem is not None and deps_elem.text:
            task['dependencies'] = [
                d.strip() for d in deps_elem.text.split(',') if d.strip()
            ]

        # TDD spec has test-first and then-implement blocks
        tdd_elem = task_elem.find('tdd-spec')
        if tdd_elem is not None:
            tests_elem = tdd_elem.find('test-first')
            impl_elem = tdd_elem.find('then-implement')
            if tests_elem is not None and tests_elem.text:
                task['tdd_spec']['tests'] = tests_elem.text.strip()
            if impl_elem is not None and impl_elem.text:
                task['tdd_spec']['implement'] = impl_elem.text.strip()

        # pyproject-deps is a single element with comma-separated text
        # Example: <pyproject-deps>fastapi >= 0.115, uvicorn >= 0.34</pyproject-deps>
        deps_pkg_elem = task_elem.find('pyproject-deps')
        if deps_pkg_elem is not None and deps_pkg_elem.text:
            task['pyproject_deps'] = [
                d.strip() for d in deps_pkg_elem.text.split(',') if d.strip()
            ]

        tasks.append(task)

    return tasks
```

**Note:** Always verify the parser against the actual plan file structure. Different plans may use different XML conventions.

## Selection Output

After selection, output:

```
TASK SELECTED: {task_id} — {task_name}
Dependencies: {list of dependency IDs, all DONE}
TDD spec: {summary — N test functions to write, M files to implement}
Acceptance criteria: {count} criteria
Package deps: {list or "none"}
```

## Edge Cases

- **No eligible tasks**: All remaining tasks are BLOCKED or DEFERRED. Report this and stop.
- **Circular dependencies**: Log error and halt. This is a plan authoring bug.
- **IN_PROGRESS task exists**: Resume that task instead of selecting a new one. Check which phase it was in from state file.
- **Session budget exceeded**: If `session_inner_iterations >= 20`, output a session summary and stop. Do not begin a new task.

## Next Step

After selecting a task, proceed to [red-phase.md](red-phase.md).
