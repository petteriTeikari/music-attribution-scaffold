---
name: create-pr
description: Create pull requests with full metadata — labels, issue references, project fields (priority, size, iteration), and detailed descriptions following project conventions
---

# Create PR Skill

Create pull requests with **complete metadata** so every PR matches the quality bar set by prior PRs (e.g., #53). No bare PRs with empty labels and missing project fields.

## When to Use

- Any time a PR is being created (`gh pr create`)
- When reviewing an existing PR that is missing metadata
- After the `self-learning-iterative-coder` completes a batch of tasks

## Checklist (MANDATORY for every PR)

Every PR must have ALL of the following before the `gh pr create` command (or immediately after via `gh pr edit`):

### 1. Labels

Select from existing repo labels. Every PR needs **at least 2 labels**:

| Label | When to use |
|-------|------------|
| `enhancement` | New feature or capability |
| `bug` | Bug fix |
| `documentation` | Docs-only changes |
| `infrastructure` | DevOps, Docker, CI, deployment |
| `developer-experience` | DX tooling, scripts, ergonomics |
| `frontend` | Next.js / React changes |
| `ci` | CI/CD pipeline changes |
| `chore` | Maintenance, cleanup |
| `agentic-ui` | CopilotKit / AG-UI / PydanticAI agent |
| `tech-debt` | Technical debt cleanup |

**Priority label** (exactly one):

| Label | When |
|-------|------|
| `P0` | Must have — blocking release or critical bug |
| `P1` | High value — defer only if time-limited |
| `P2` | Nice to have — post-sprint |

### 2. Issue References

Scan the branch commits and open issues to find **every related issue**. Use these patterns in the PR body:

- `Closes #N` — PR fully resolves the issue (auto-closes on merge)
- `Related to #N` — PR partially addresses or is related to the issue
- `Advances #N` — PR makes progress on a tracking issue

**How to find related issues**:
```bash
# List open issues
gh issue list --state open --limit 50

# Check what commits are in this branch
git log main..HEAD --oneline

# Cross-reference commit messages with issue titles/descriptions
```

Never create a PR without checking for related issues. Even "no related issues" should be a conscious decision, not an omission.

### 3. PR Body Format

```markdown
## Summary

<1-3 sentence overview of what this PR does and WHY>

**Related to**: #N (description), #M (description)
**Closes**: #X, #Y

### Changes

<Bulleted list of what changed, grouped by category>

### Test Results

- **N tests passing** (up from M on main, +K new tests)
- All pre-commit hooks green
- <any xfails or known limitations>

## Test plan

- [x] <completed verification>
- [ ] <manual verification needed>

🤖 Generated with [Claude Code](https://claude.com/claude-code)
```

### 4. Project Board Fields

After creating the PR, set ALL project fields:

```bash
# 1. Find the project item ID
gh project item-list 4 --owner petteriTeikari --limit 80 | grep "PR_TITLE_OR_NUMBER"

# 2. Set Status (required)
# Options: f75ad846=Backlog, e18bf179=Ready, 47fc9ee4=In progress, aba860b9=In review, 98236657=Done
gh project item-edit --project-id PVT_kwHOABAuos4BO3uZ --id ITEM_ID \
  --field-id PVTSSF_lAHOABAuos4BO3uZzg9ch1o --single-select-option-id OPTION_ID

# 3. Set Priority (required)
# Options: 79628723=P0, 0a877460=P1, da944a9c=P2
gh project item-edit --project-id PVT_kwHOABAuos4BO3uZ --id ITEM_ID \
  --field-id PVTSSF_lAHOABAuos4BO3uZzg9ch-k --single-select-option-id OPTION_ID

# 4. Set Size (required)
# Options: 911790be=XS, b277fb01=S, 86db8eb3=M, 853c8207=L, 2d0801e2=XL
gh project item-edit --project-id PVT_kwHOABAuos4BO3uZ --id ITEM_ID \
  --field-id PVTSSF_lAHOABAuos4BO3uZzg9ch-o --single-select-option-id OPTION_ID

# 5. Set Iteration (required — use current iteration)
# Current: 381c7c80 = "Iteration 1" (Feb 10 - Feb 23, 2026)
gh project item-edit --project-id PVT_kwHOABAuos4BO3uZ --id ITEM_ID \
  --field-id PVTIF_lAHOABAuos4BO3uZzg9ch-w --iteration-id ITERATION_ID
```

#### Size Guidelines

| Size | Criteria |
|------|----------|
| XS | 1-2 files, < 50 lines, trivial change |
| S | 3-5 files, < 200 lines, straightforward |
| M | 5-15 files, < 500 lines, moderate complexity |
| L | 15-30 files, < 1000 lines, significant feature |
| XL | 30+ files or 1000+ lines, major feature/refactor |

### 5. Assignee

Always assign the PR to `petteriTeikari`:
```bash
gh pr edit PR_NUMBER --add-assignee petteriTeikari
```

## Project Constants

These are specific to `petteriTeikari/music-attribution-scaffold`:

| Constant | Value |
|----------|-------|
| Project number | `4` |
| Project ID | `PVT_kwHOABAuos4BO3uZ` |
| Owner | `petteriTeikari` |
| Status field | `PVTSSF_lAHOABAuos4BO3uZzg9ch1o` |
| Priority field | `PVTSSF_lAHOABAuos4BO3uZzg9ch-k` |
| Size field | `PVTSSF_lAHOABAuos4BO3uZzg9ch-o` |
| Estimate field | `PVTF_lAHOABAuos4BO3uZzg9ch-s` |
| Iteration field | `PVTIF_lAHOABAuos4BO3uZzg9ch-w` |

### Status Options
| Name | ID |
|------|----|
| Backlog | `f75ad846` |
| Ready | `e18bf179` |
| In progress | `47fc9ee4` |
| In review | `aba860b9` |
| Done | `98236657` |

### Priority Options
| Name | ID |
|------|----|
| P0 | `79628723` |
| P1 | `0a877460` |
| P2 | `da944a9c` |

### Size Options
| Name | ID |
|------|----|
| XS | `911790be` |
| S | `b277fb01` |
| M | `86db8eb3` |
| L | `853c8207` |
| XL | `2d0801e2` |

### Iteration Options
| Name | ID | Dates |
|------|----|-------|
| Iteration 1 | `381c7c80` | Feb 10 - Feb 23, 2026 |

> **Note**: Query current iterations with `gh project field-list 4 --owner petteriTeikari --format json` if the iteration has rolled over.

## Workflow

```
1. Analyze branch commits     →  git log main..HEAD --oneline
2. List open issues            →  gh issue list --state open
3. Choose labels               →  category + priority
4. Write PR body               →  summary, issue refs, changes, tests
5. Create PR                   →  gh pr create --title --body --label --assignee
6. Add to project              →  gh project item-add (if not auto-added)
7. Set project fields          →  status, priority, size, iteration
8. Verify                      →  gh pr view PR_NUMBER
```

## Anti-Patterns

| Anti-Pattern | Correct Approach |
|-------------|-----------------|
| No labels | Always at least 2 (category + priority) |
| No issue references | Always check `gh issue list` and cross-reference |
| "Backlog" status on new PR | Set to "In review" for new PRs |
| Missing iteration | Always set to current iteration |
| Missing size | Estimate from file/line count |
| Generic description | Be specific about what changed and why |
| `gh pr create` without `--label` | Include labels in the create command |

## Example: Complete PR Creation

```bash
# Create PR with all metadata inline
gh pr create \
  --title "feat: add OpenTelemetry auto-instrumentation" \
  --label "infrastructure,enhancement,P2" \
  --assignee "petteriTeikari" \
  --body "$(cat <<'EOF'
## Summary

Add OpenTelemetry auto-instrumentation for FastAPI with OTLP export, building on the Prometheus metrics foundation from #54.

**Related to**: #55 (OpenTelemetry tracking issue), #56 (full observability stack)
**Closes**: #55

### Changes

- Added `opentelemetry-instrumentation-fastapi` and `opentelemetry-exporter-otlp` dependencies
- Created `src/music_attribution/observability/tracing.py` with TracerProvider setup
- Wired auto-instrumentation into FastAPI app startup

### Test Results

- **495 tests passing** (up from 487 on main, +8 new)
- All pre-commit hooks green

## Test plan

- [x] Unit tests for tracer configuration
- [x] Integration test with mock OTLP collector
- [ ] Manual verification with Jaeger UI

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"

# Find project item ID and set all fields
ITEM_ID=$(gh project item-list 4 --owner petteriTeikari --limit 5 | grep "OpenTelemetry" | awk '{print $NF}')

gh project item-edit --project-id PVT_kwHOABAuos4BO3uZ --id $ITEM_ID \
  --field-id PVTSSF_lAHOABAuos4BO3uZzg9ch1o --single-select-option-id aba860b9  # In review
gh project item-edit --project-id PVT_kwHOABAuos4BO3uZ --id $ITEM_ID \
  --field-id PVTSSF_lAHOABAuos4BO3uZzg9ch-k --single-select-option-id da944a9c  # P2
gh project item-edit --project-id PVT_kwHOABAuos4BO3uZ --id $ITEM_ID \
  --field-id PVTSSF_lAHOABAuos4BO3uZzg9ch-o --single-select-option-id b277fb01  # S
gh project item-edit --project-id PVT_kwHOABAuos4BO3uZ --id $ITEM_ID \
  --field-id PVTIF_lAHOABAuos4BO3uZzg9ch-w --iteration-id 381c7c80             # Iteration 1
```
