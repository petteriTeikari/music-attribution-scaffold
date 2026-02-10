# Self-Correction Principles

The philosophical and practical foundations for iterative, self-correcting code generation.

## The Ralph Wiggum Philosophy

> "Ralph is monolithic. Ralph works autonomously in a single repository as a single process that performs one task per loop." — Geoffrey Huntley

The Ralph Wiggum technique is a bash loop that feeds an AI's output (errors and all) back into itself until it produces the correct answer. It is brute force meets persistence.

```bash
while :; do cat PROMPT.md | claude-code ; done
```

This skill formalizes the Ralph pattern with structure:
- **One task per loop** — don't try to do everything at once
- **Errors are feedback** — test failures guide the next fix
- **Persistence beats perfection** — iteration 3 is better than iteration 1
- **The loop is the hero** — not the model

## LLMs Are Stochastic

LLMs cannot write production-grade code in a single pass. This is not a bug — it's fundamental to how probabilistic language models work.

**Expected accuracy trajectory:**
- Iteration 1: ~60-70% correct (initial implementation, structural errors)
- Iteration 2: ~80% correct (major bugs fixed, edge cases remain)
- Iteration 3: ~90% correct (targeted fixes, lint/type cleanup)
- Iteration 4-5: ~95%+ (diminishing returns, remaining issues may be design-level)

**Implication:** Self-correction is the norm, not a failure. The skill is designed around this reality. If you're surprised that code doesn't work on the first pass, you're misunderstanding the tool.

## Ghost Completions: The #1 Failure Mode

A "ghost completion" is when the AI claims something works without actually running the verification suite.

**Signs of ghost completion:**
- "This should now pass all tests" (without running them)
- "I've fixed the type errors" (without running mypy)
- "The implementation is complete" (without running pytest)

**Prevention:** The VERIFY phase is mandatory. Every claim must be backed by actual command output. The word "should" is banned in the context of verification — replace with "does" or "does not" based on actual results.

## One Task Per Invocation

Respect context budgets. LLMs degrade with very long conversations:
- Context window fills up, earlier details get compressed or lost
- Token probability distributions shift as context length grows
- Error accumulation compounds across tasks

**Rule:** Max 20 inner iterations per session. After 20, save state and start fresh. The state file is the bridge between sessions — it carries structured data, not conversation history.

This follows Mollick's organizational theory:
> "Structured boundary objects that multiple agents of different ability levels can read and write to would solve a huge number of coordination failures and reduce token use."

The state file IS the boundary object between sessions.

## Test Failures Are Information, Not Errors

When a test fails, it's telling you something specific:
- **What** the expected behavior is (from the assertion)
- **What** the actual behavior is (from the error message)
- **Where** the discrepancy is (from the stack trace)

A failing test is a precise specification of what needs to change. It's the most valuable feedback the system produces.

**Correct response to a test failure:**
1. Read the assertion — what was expected?
2. Read the actual — what happened instead?
3. Read the stack trace — where did it go wrong?
4. Make a targeted fix based on this information
5. Re-run the test

**Incorrect response to a test failure:**
1. Rewrite the entire implementation
2. Delete the failing test
3. Add a broad try/except to suppress the error
4. Guess at a fix without reading the error message

## Boundary Objects Reduce Coordination Failures

Pydantic schemas at pipeline boundaries serve as contracts:
- The upstream producer knows exactly what to output
- The downstream consumer knows exactly what to expect
- Both sides can change their internals freely as long as the contract holds

This is why the TDD spec defines Pydantic models first — they're the boundary objects. Tests verify the contracts. Implementation satisfies the contracts.

## Shortcuts Compound Into Technical Debt

Every shortcut has a compounding cost:
- Skipping tests means bugs surface later (when context is lost)
- Skipping lint means inconsistent code style across tasks
- Skipping types means refactoring is harder
- Skipping the RED commit means you can't verify GREEN actually changed behavior
- Using `# type: ignore` means type errors propagate silently

The iterative loop exists precisely because shortcuts don't work. Each gate (tests, lint, types) catches a different class of problems. All three must be green.

## Software Is Clay on the Pottery Wheel

> "Software is now clay on the pottery wheel and if something isn't right then I just throw it back on the wheel to address items that need resolving." — Geoffrey Huntley

The old model: Build brick by brick. Each brick must be perfect because it's hard to change later.

The new model: Shape iteratively. Each pass through the loop refines the shape. The loop is cheap — running tests costs seconds, not hours.

This changes the economics of quality:
- **Old:** High cost of rework → invest in getting it right first time
- **New:** Low cost of rework → invest in fast feedback loops

## Anti-Patterns Summary

| Anti-Pattern | Root Cause | Consequence | Prevention |
|--------------|-----------|-------------|------------|
| Ghost completion | Claiming done without running tests | Silent bugs, false progress | VERIFY phase is mandatory |
| Shotgun fixing | Changing many things at once | Can't tell what helped | One fix category at a time |
| Test suppression | Deleting/weakening failing tests | Bugs become invisible | Tests are the spec — implementation adapts |
| Context hoarding | Too much work in one session | Quality degradation | Max 20 inner iterations per session |
| Convention ignorance | Not reading CLAUDE.md | Lint/type failures in every iteration | Read conventions before starting |
| Infinite loop | Retrying same fix without analysis | Wasted compute, no progress | Ceiling detection after 2 identical failures |
| Over-engineering | Adding features beyond TDD spec | Untested code, scope creep | Implement minimum for green tests |

## Meta-Learning

As you execute plans with this skill, you will discover patterns:
- Which types of tasks tend to STUCK
- Which types of test failures are most common
- Which project conventions are most frequently violated
- Which fix strategies work best for which failure categories

Record these learnings in the state file's per-task reports. Over time, these reports become a training dataset for improving the skill itself.

The skill is designed to be improved from execution experience. The first plan you execute will reveal weaknesses in the skill's protocols. Fix the protocols. The second plan will be smoother. This is the meta-loop.

## Empirical Learnings (from 27-task execution)

The following data comes from executing the full `probabilistic-prd-executable-plan.xml` (27 non-deferred tasks, 163 unit tests as reported by `pytest --co`) using v1.0.0 of this skill. Per-task `test_count` values in the state file are approximate; the `convergence.total_tests` from actual pytest discovery is the ground truth.

### Actual accuracy trajectory

| Result | Tasks | Percentage |
|--------|-------|------------|
| ALL_GREEN on iteration 1 | 19/27 | 70% |
| Fixed by iteration 2 | 7/27 | 26% |
| Required 3 iterations | 1/27 | 4% |
| Required FORCE_STOP | 0/27 | 0% |

The single 3-iteration task was Splink (2.3b) — an external library with non-obvious API and EM training that doesn't converge with synthetic data.

The v1.0 prediction of "60-70% correct on iteration 1" was **pessimistic**. With well-structured TDD specs and strong Pydantic schemas, first-pass success rate is significantly higher. The schema constraints catch many errors at the Pydantic validation layer before tests even run.

### Most common failure categories (ranked by frequency)

1. **Lint: unused imports, missing `strict=True` on `zip()`** — ~80% of fix iterations. These are trivial to fix but consistently generated. This is the LLM's most common stochastic error.

2. **Mypy: untyped third-party imports** — 100% of new packages needed `[[tool.mypy.overrides]]` with `follow_untyped_imports = true`. This was a predictable, recurring pattern that v1.0 didn't address.

3. **Schema mismatch: test fixtures missing required Pydantic fields** — 3 tasks. The TDD spec listed the "interesting" fields but omitted required ones like `scope`, `created_by`, `version`. Fix: always read the full schema before writing test fixtures.

4. **API mismatch: external lib API different from plan spec** — 2 tasks. Splink v4 API (`block_on` location), MCP `FastMCP` interface. Fix: check installed version and actual module, not plan assumptions.

5. **Logic errors: actual code bugs** — 2 tasks. Orchestrator accessing private attribute (`.threshold` vs `._threshold`), aggregator using wrong enum value (`USER_INPUT` vs `ARTIST_INPUT`). These are the failures the TDD loop is actually designed to catch.

### Session budget observation

27 tasks were completed across ~3 sessions with context compaction. Each session handled 9-13 tasks, far exceeding the v1.0 "max 5" rule. Inner iterations (not task count) correlate with actual context consumption — a 1-iteration task costs far less context than a 3-iteration task.

### What the state file looked like in practice

The state file fell behind almost immediately — it was at task 1.1 when execution had reached 4.2. Per-checkpoint state updates are high overhead with low value when `git log --oneline` provides faster, more reliable crash recovery. v2.0 changed to session-boundary state updates.

### Key insight: Pydantic schemas as force multipliers

Tasks that operated on well-defined Pydantic boundary objects (schemas) had a ~90% first-pass success rate. Tasks that interacted with external libraries (Splink, MCP) or required complex test fixtures had lower success rates. **The stronger the type system, the fewer iterations needed.** This validates the manuscript's emphasis on structured boundary objects.
