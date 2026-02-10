---
name: integrate-prd-research
version: 2.0.0
description: Integrate new research (tools, libraries, articles, patterns) into the probabilistic PRD decision network
revision_notes: "v2.0: Added verification commands, mermaid ID collision check, existing node cross-reference protocol, scenario path updates, and contextualization templates"
---

# Integrate PRD Research

Standardized workflow for incorporating new research findings — tools, libraries, academic papers, industry articles, architectural patterns — into the probabilistic PRD decision network so they are discoverable for future work.

**Activation**: This is a *read-and-follow* skill. Read this file at the start of integration work. It is not a registered slash command — the `invocation` field in v1.0 was aspirational. Activate by reading the skill file when the user requests PRD integration.

## When to Use

- User discovers a new library/tool and wants it captured in the PRD
- A research session produces findings that should inform future decision-making
- New articles, papers, or industry reports shift probability estimates
- A completed implementation reveals that PRD probabilities need updating
- User says "integrate this into the PRD"

## When NOT to Use

- For implementing code (use `self-learning-iterative-coder`)
- For one-off research questions that don't need persistence
- For changes to existing implementation code

---

## Workflow

### Phase 1: Understand the Input

Read and classify the research material. Determine:

1. **What type of input?**
   - New tool/library discovery
   - Article/paper with new evidence
   - Post-implementation retrospective (empirical data)
   - Ecosystem shift (e.g., framework consolidation, pricing change)

2. **What domain does it affect?**
   - `music_attribution`, `dpp_traceability`, `generic_graph_rag`, or cross-domain

3. **What decision level?**
   - L1 Business, L2 Architecture, L3 Implementation, L4 Deployment, L5 Operations

### Phase 2: Map to the Decision Network

Read the current network state:

```
docs/prd/decisions/_network.yaml     — Node list and DAG edges
docs/prd/decisions/_schema.yaml      — Decision node schema
docs/prd/decisions/REPORT.md         — Human-readable report with mermaid
docs/prd/decisions/L{N}-{level}/     — Existing decision nodes
```

Determine the integration action:

| Situation | Action |
|-----------|--------|
| Research fits an **existing decision node** as a new option | Add option to existing `.decision.yaml` |
| Research fits an existing node but **shifts probabilities** | Update probabilities in existing `.decision.yaml` |
| Research represents a **new decision point** | Create new `.decision.yaml` + add to `_network.yaml` |
| Research is **contextual analysis** (not a decision) | Create/update a `docs/planning/` document and reference from decision nodes |
| Research **obsoletes** an existing option | Set option status to `rejected` or `deprecated` |

### Phase 3: Execute Changes

#### 3a. For NEW Decision Nodes

Create the decision file following the schema strictly:

**File**: `docs/prd/decisions/L{N}-{level}/{decision-id}.decision.yaml`

**Required fields** (from `_schema.yaml`):
- `decision_id`: snake_case, matches filename stem
- `title`: Human-readable, max 120 chars
- `description`: Extended description with trade-offs
- `decision_level`: `L1_business` | `L2_architecture` | `L3_implementation` | `L4_deployment` | `L5_operations`
- `status`: `active` | `draft`
- `options`: Array of 2+ options, each with:
  - `option_id`: snake_case
  - `title`: Human-readable
  - `description`: What it entails
  - `prior_probability`: 0.0-1.0 (all options must sum to 1.0)
  - `status`: `recommended` | `viable` | `experimental` | `deferred` | `rejected`
- `volatility`: classification + last_assessed + next_review + change_drivers
- `domain_applicability`: per-domain relevance scores (0.0-1.0)

**Optional but recommended**:
- `conditional_on`: Conditional probability tables for parent decisions
  - Each parent option row must cover ALL options in THIS decision and sum to 1.0
  - Verify parent option_ids match actual parent decision files
- `archetype_weights`: Per-archetype probability overrides
  - Archetypes: `engineer_heavy_startup`, `musician_first_team`, `solo_hacker`, `well_funded_startup`
  - Each archetype's overrides must sum to 1.0
- `rationale`: Why these probability assignments
- `references`: Links to planning docs, knowledge base articles
- `tags`: Freeform discovery tags

**Validation checklist for new nodes**:
- [ ] All prior_probability values sum to 1.0
- [ ] All conditional_table rows sum to 1.0
- [ ] All archetype probability_overrides sum to 1.0
- [ ] Parent decision_ids exist in `_network.yaml`
- [ ] Parent option_ids match the actual parent `.decision.yaml` file
- [ ] domain_applicability includes at least `music_attribution`

#### 3b. Update `_network.yaml`

Add the new node to the `nodes:` section at the correct level position.

Add edges to the `edges:` section:
- Incoming edges: from parent decisions that influence this one
- Outgoing edges: to child decisions that this one influences
- Each edge needs: `from`, `to`, `influence` (strong|moderate|weak), `rationale`

Bump the network `version` (patch for option changes, minor for new nodes).

**Verification after editing** (mandatory):
```bash
# Count nodes and edges to update REPORT.md statistics
grep "^  - id:" docs/prd/decisions/_network.yaml | wc -l
grep "^  - from:" docs/prd/decisions/_network.yaml | wc -l
```

Record these counts — they must match the REPORT.md statistics table exactly.

#### 3b-ii. Update Existing Decision Nodes (Cross-References)

When adding a new node that influences existing nodes, check whether existing
child nodes should add the new node to their `conditional_on` tables:

1. For each outgoing edge from the new node → existing child:
   - Read the child's `.decision.yaml`
   - Decide: does the new node's choice meaningfully shift the child's probabilities?
   - If yes: add a `conditional_on` entry with a full conditional table
   - If no (weak influence only): the edge in `_network.yaml` is sufficient; no conditional table needed
2. Document the decision either way (added or skipped with rationale)

This prevents "orphan edges" — edges declared in the network topology but
not reflected in the conditional probability tables of the target nodes.

#### 3c. Update `REPORT.md`

Update these sections in `docs/prd/decisions/REPORT.md`:

1. **Network Topology mermaid diagram**: Add node to correct `subgraph`, add edges, add `style` line
   - L1 nodes: `fill:#1E3A5F,color:#fff`
   - L2 nodes: `fill:#2E7D7B,color:#fff`
   - L3 nodes: `fill:#D4A03C,color:#000`
   - L4 nodes: `fill:#4A7C59,color:#fff`
   - L5 nodes: `fill:#C75050,color:#fff`
   - **Mermaid node IDs**: Use 2-3 uppercase letter abbreviations (e.g., `ADS` for Artifact Decoupling Strategy). Before adding, check for collisions with existing IDs in REPORT.md. Current IDs: `BVB, TMS, RM, RP, DMC, AP, SD, AFS, ADS, PD, GS, VS, LLM, FF, AS, DQS, CP, DH, CI, IAC, CS, OS, SS, BDR, SM, SG`

2. **Volatility heatmap**: Add node under correct classification (Stable/Shifting/Volatile)

3. **Cross-Archetype Comparison Tables**: Add row for new decision in the correct level table (L1, L3, or L4-L5)

4. **Network Statistics**: Update node counts, edge counts, percentages using the counts from step 3b verification

5. **Scenario Path diagrams**: If the new node is L1 or L2, check whether it should appear in the "Music Attribution MVP" and "DPP Enterprise" scenario paths. L3+ nodes appear only if they're on the highlighted path.

6. **See Also**: Add reference to any new planning documents

#### 3d. Create/Update Contextualization Document

For substantial research (multiple tools, comparative analysis):

**File**: `docs/planning/{topic}-contextualization.md`

**Existing templates to follow** (read one before writing):
- `docs/planning/quality-tooling-contextualization.md` — Tool-by-tool analysis with conditional probability tables, tiered adoption, validation spectrum
- `docs/planning/artifact-decoupling-contextualization.md` — 4-artifact pattern, reproducibility matrix (R0-R5), phased implementation roadmap, cross-cutting impact table

Structure:
```markdown
# {Topic} Contextualization for the Probabilistic PRD

**Date**: YYYY-MM-DD
**Status**: Research complete, not yet implemented
**Branch for implementation**: Future branches
**Related decision nodes**: [links to .decision.yaml files]

## Executive Summary
## Tool-by-Tool Analysis with Conditional Probabilities
## Cross-Cutting: How This Interacts with Other PRD Decisions
## Adoption Roadmap: Conditional on Project Phase
## Decision Network Integration
## See Also
```

Include **conditional probability tables** showing P(adopt) under different conditions.
These are the key deliverable — they make the research actionable for future branches.

Include a **"Cross-Cutting" section** mapping how the research topic interacts with
existing decision nodes. Use a table format:

```markdown
| Decision Node | How {Topic} Affects It |
|---------------|------------------------|
| `node_name`   | Description of interaction |
```

#### 3e. For EXISTING Node Updates

When updating probabilities or adding options to existing nodes:
- Read the current file first
- Verify probability sums still equal 1.0 after changes
- Update `last_updated` date
- If probabilities shift significantly, update `volatility.last_assessed`
- Check if conditional tables in child nodes need updating

### Phase 4: Verify

Run these checks before committing:

**4a. Probability sums** (mandatory for new/modified decision files):
```bash
# For each modified .decision.yaml, verify:
# - prior_probability across all options sums to 1.0
# - Each conditional_table row sums to 1.0
# - Each archetype probability_overrides sums to 1.0
# Quick check: search for all probability values and mentally sum them
```

**4b. Network integrity**:
```bash
# Count nodes and edges — record for REPORT.md
grep "^  - id:" docs/prd/decisions/_network.yaml | wc -l
grep "^  - from:" docs/prd/decisions/_network.yaml | wc -l
```

**4c. Cross-reference resolution**:
- Every `parent_decision_id` in a new `.decision.yaml` must exist as a node in `_network.yaml`
- Every `given_parent_option` must match an actual `option_id` in the parent's `.decision.yaml` file
- Every edge in `_network.yaml` must reference nodes that exist in the `nodes:` section

**4d. REPORT.md consistency**:
- Mermaid diagram node count matches `_network.yaml` node count
- Statistics table matches actual counts from 4b
- No duplicate mermaid node IDs
- Every new node has a `style` line in the mermaid diagram
- Volatility heatmap includes the new node

**4e. Orphan edge check**:
- For each edge from the new node → existing child node, verify the child's
  `.decision.yaml` either has a `conditional_on` entry for the new parent,
  OR the edge is documented as "influence only, no conditional table needed"

### Phase 5: Commit

Commit in semantically coherent chunks:
1. New/modified `.decision.yaml` files + contextualization docs
2. `_network.yaml` + `REPORT.md` updates + skill reference updates

Use commit message format:
```
docs(prd): {action} {node_name} decision node

{Description of what was added/changed and why}

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

---

## Examples

### Example 1: New Tool Discovery

User: "I found this tool called Evidently AI for ML monitoring. Integrate it into the PRD."

Action:
1. Classify: L5_operations, relates to `observability_stack` decision
2. Map: This is a new option for an existing node, not a new node
3. Execute: Add `evidently_ml_monitoring` option to `observability-stack.decision.yaml`, update conditional tables
4. Document: Note in a planning doc if the research is extensive

### Example 2: Article Shifts Probabilities

User: "This article shows Apache AGE is now production-ready. Update the PRD."

Action:
1. Classify: Evidence update for existing L3 `graph_strategy` node
2. Map: Probability shift — increase `apache_age` prior, decrease alternatives
3. Execute: Update probabilities in `graph-strategy.decision.yaml`, update `volatility.last_assessed`
4. No new contextualization doc needed — just a probability update

### Example 3: New Research Area (like quality tooling)

User: "Integrate findings about data quality tools, schema governance, and label noise detection."

Action:
1. Classify: Multiple new decision points across L3 and L5
2. Map: Create 2 new nodes (`data_quality_strategy`, `schema_governance`)
3. Execute: Create decision files, update network, update report, create `quality-tooling-contextualization.md`
4. Commit in 1-2 chunks

---

## Reference: Current Network Structure

```
L1 Business (4 nodes):
  build_vs_buy_posture, target_market_segment, revenue_model, regulatory_posture

L2 Architecture (5 nodes):
  data_model_complexity, api_protocol, service_decomposition, ai_framework_strategy,
  artifact_decoupling_strategy

L3 Implementation (7 nodes):
  primary_database, graph_strategy, vector_strategy, llm_provider,
  frontend_framework, auth_strategy, data_quality_strategy

L4 Deployment (5 nodes):
  compute_platform, database_hosting, ci_cd_pipeline, iac_tooling, container_strategy

L5 Operations (5 nodes):
  observability_stack, scaling_strategy, backup_dr_strategy,
  secrets_management, schema_governance
```

**Files to always read first**:
1. `docs/prd/decisions/_network.yaml` — current topology
2. `docs/prd/decisions/_schema.yaml` — node schema (required/optional fields)
3. The specific `L{N}/*.decision.yaml` files related to the research topic

**Key invariants to maintain**:
- All probability arrays sum to 1.0 (tolerance: 0.01)
- DAG remains acyclic
- All cross-references resolve
- REPORT.md statistics match actual node/edge counts
