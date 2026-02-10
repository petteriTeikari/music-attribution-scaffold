# Protocol: Checkpoint (Git Commit + State Update)

## Purpose

Create an atomic git commit and update the state file. Checkpoints serve as crash-recovery points — if context is lost, the state file tells you exactly where to resume.

## Inputs

- Current task ID and phase
- Verification results (from last VERIFY pass)
- Inner iteration count
- Files changed in this iteration

## Steps

### 1. Review Changed Files

List all files modified in this iteration:
```bash
git status
git diff --name-only
```

Verify the list makes sense:
- Test files from RED phase
- Source files from GREEN phase
- Any fix-phase modifications
- No accidental changes to unrelated files

### 2. Stage Files Selectively

Stage only the files related to this task. **Never use `git add .` or `git add -A`.**

```bash
git add src/{package}/{module}.py
git add tests/unit/test_{module}.py
git add tests/conftest.py        # if modified
git add pyproject.toml           # if deps were added
```

**Do NOT stage:**
- `.env` files or credentials
- IDE configuration (`.vscode/`, `.idea/`)
- State files (committed separately)
- Unrelated files

### 3. Craft Commit Message

Use conventional commits format:

**For GREEN checkpoint (all tests pass):**
```
feat({scope}): implement task {id} — {short description}

- Tests: {pass_count} passed
- Lint: clean
- Types: clean
- Inner iterations: {N}
```

**For intermediate checkpoint (partial progress):**
```
wip({scope}): task {id} iteration {N} — {what was accomplished}

- Tests: {pass}/{total} ({fail} failing)
- Remaining: {description of what's left}
```

**For STUCK/FORCE_STOP checkpoint:**
```
wip({scope}): task {id} STUCK after {N} iterations

- Tests: {pass}/{total} ({fail} still failing)
- Stuck on: {description of persistent failure}
- Needs: human review
```

### 4. Commit

```bash
git commit -m "{commit message}"
```

### 5. Update State File (Session Boundaries Only)

**v2.0 change:** The state file is updated at **session start** and **session end**, not after every checkpoint.

**Per-task:** The git commit IS the checkpoint. `git log --oneline` provides crash recovery — it shows exactly what was implemented and when.

**Per-session-start:**
1. Load state file
2. Verify state against `git log` (reconcile any discrepancies)
3. Set `current_task_id` to the next eligible task

**Per-session-end:**
1. Bulk update all completed tasks in the state file
2. Update convergence counters
3. Record `session_inner_iterations`

**Rationale:** In practice, per-checkpoint state updates fell behind immediately — the state file was at task 1.1 when execution had reached task 4.2. Git history is the ground truth for crash recovery; the state file provides higher-level progress tracking.

State file schema:
```json
{
  "current_task_id": "{task_id}",
  "current_phase": "CHECKPOINT",
  "session_inner_iterations": N,
  "tasks": {
    "{task_id}": {
      "status": "{DONE|STUCK}",
      "name": "{task_name}",
      "inner_iterations": N,
      "commit_hashes": ["{hash}"],
      "test_count": T,
      "completed_at": "{timestamp}"
    }
  },
  "convergence": {
    "tasks_done": D,
    "tasks_total": T,
    "tasks_stuck": S
  }
}
```

### 6. Output Progress Summary

```
CHECKPOINT — Task {task_id} — Iteration {N}
  Commit: {short_hash} {commit_message_first_line}
  Files: {count} files staged
  State: Updated tdd-state.json
  Plan progress: {done}/{total} tasks
```

## Checkpoint Frequency

- **Always** after RED phase (failing tests committed)
- **Always** after convergence (ALL_GREEN or FORCE_STOP)
- **Optionally** after significant fix progress (3+ failures resolved)

## State File Location

The state file lives at:
```
.claude/skills/self-learning-iterative-coder/state/tdd-state.json
```

This path is relative to the project root. The state file can be committed to git for cross-session visibility, or kept local as an execution artifact — project preference.

## Recovery from Crash

If the session ends unexpectedly:
1. Read `tdd-state.json` to find `current_task_id` and `current_phase`
2. Check `git log --oneline -5` to see recent commits
3. If `current_phase` is:
   - `RED`: Tests are committed but failing. Proceed to GREEN.
   - `GREEN`: Implementation exists but unverified. Proceed to VERIFY.
   - `VERIFY`: Re-run verification.
   - `FIX`: Re-run verification to see current state.
   - `CHECKPOINT`: Task is checkpointed. Proceed to CONVERGE.

## Next Step

Proceed to [convergence.md](convergence.md).
