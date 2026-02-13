# Observability, Reproducibility & Infrastructure Double-Check Plan

> **v1.1** — Synthesized from web research (12 technologies), codebase audit, and 3 reviewer agents (2026-02-13).
> Integrates remaining P2 tasks (P2-1 through P2-7) from `remaining-final-tasks-before-ssrn-repo-double-check.md`.
> Updated with converged reviewer feedback (Architecture: APPROVE 8/10, Portfolio/Hiring: APPROVE 7.5/10→8.5, MLOps Teaching: APPROVE).

## User Prompt (verbatim)

> Do we observability stubs also for the deployment? OpenTelemetry and Grafana Cloud integration stubs? How about the monitoring stubs, like Evidently and other alternatives. How much of the "real world engineering" stubs do we have in place if you would develop this into a product? This repo cannot come across as too academic while being grounded on academic research. It has to show ML Infrastructure competence and readiness to be further developed into a real product. Plan how to achieve this further with reviewer agents to /home/petteri/Dropbox/github-personal/music-attribution-scaffold/docs/planning/observability-reproducability-double-checks.md , and how does local Grafana and OpenTelemetry work in our local Docker dev image? So that you get the real experience with Grafana dashboard even if you would "deploy" to localhost? and are there stubs for orchestrators? What does Probabilistic PRD say about Celery, Prefect, Airflow, Metaflow and Dagster like tools? How about Kubernetes, or its light-weight alternatives like Nomad? /home/petteri/Dropbox/KnowledgeBase/MLOps/MLOps - Pipelines - Kubernetes.md /home/petteri/Dropbox/KnowledgeBase/MLOps/MLOps - Pipelines - Prefect.md? How about policy-as-code and IaC solution? Pulumi vs OpenTofu/terraform? Pulumi CrossGuard stubs? /home/petteri/Dropbox/KnowledgeBase/MLOps/MLOps - Policy-as-Code.md ? How about sky computing stubs for finops optimization, e.g. SkyPilot /home/petteri/Dropbox/KnowledgeBase/MLOps/MLOps - Sky Computing.md? How about all the documentation-as-code in probabilistic PRD? mkdocs vs the rest, /home/petteri/Dropbox/KnowledgeBase/MLOps/MLOps - Documentation.md. Stubs for different kind of CD frameworks? e.g. Argo /home/petteri/Dropbox/KnowledgeBase/MLOps/MLOps - Deploy - Strategies.md . And what other xOps and -as-code pondering we should be thinking? /home/petteri/Dropbox/KnowledgeBase/MLOps/MLOps - EthicsOps.md /home/petteri/Dropbox/KnowledgeBase/MLOps/MLOps - Governance-as-code.md? And do very comprehensive planning with web search and multiple iterations round with reviewer agents to converge into an optimal plan, with not all planning having to lead to implementation. It is equally valuable to expand our probalistic PRD and Issues in our project: https://github.com/users/petteriTeikari/projects/4 as it is actually to implement new code! And be conservative with actually implementing new features and let's avoid feature creep in this demo repo for preprint, but be prepared in the architectural design for a lot of future developments which are open-ended. Save this prompt verbatim and let's execute the plan!

---

## Executive Summary

The codebase has **solid foundations** (434 backend tests, 265 frontend tests, editorial design system, 5-pipeline architecture with Pydantic boundary objects). Batches C1-C4 fixed the critical P0/P1 issues. What remains is **infrastructure credibility**: showing that this scaffold can become a real product.

**Philosophy**: For a preprint companion repo, we should **document architecture decisions** (PRD nodes, GitHub Issues) more than we implement. Real engineering competence is shown by *knowing what you'd need* and *having the seams ready*, not by shipping a half-baked Grafana stack.

### What Already Exists (from C1-C4)
- Pluggable tracer interface (NoOp/Log/Langfuse) with `TRACER_BACKEND` env var
- DriftDetector wired into DataQualityGate
- Correlation ID middleware
- Liveness + readiness health probes
- Centralized thresholds module
- MCP server wired to PostgreSQL
- Docker dev stack: PostgreSQL + pgBouncer + Valkey + backend + frontend

### What's Missing (from audit)
- No OpenTelemetry / Prometheus / Grafana in Docker dev
- No orchestrator (Prefect/Dagster/Celery)
- No production Dockerfile
- No IaC code (only PRD decisions)
- No CD pipeline (GitHub Actions is CI-only)
- No API rate limiting
- No documentation-as-code (mkdocs)
- No policy-as-code
- No pipeline DAG definition

---

## Technology Landscape (2026 Web Research)

| Technology | Version (Feb 2026) | Assessment |
|---|---|---|
| **OpenTelemetry Python** | v1.39.1 | Stable. Auto-instrumentation for FastAPI mature. OTLP export to Grafana Cloud works well. |
| **Grafana Cloud** | Free tier: 10K metrics, 50GB logs, 50GB traces | Generous free tier for small projects. Local stack via `grafana/grafana`, `prom/prometheus`, `grafana/loki`, `grafana/tempo`. |
| **Evidently AI** | v0.7.19 | ML/LLM monitoring. 100+ metrics. Good for data drift, model quality. Python >=3.9. |
| **Prefect** | v3.x | Python-native orchestration. Flow/task decorators. Self-hosted or Prefect Cloud. Good Pydantic integration. |
| **Dagster** | Latest stable | Asset-centric (vs Prefect's flow-centric). Better for data pipelines. Heavier setup. |
| **Nomad** | BSL license (IBM/HashiCorp) | Lightweight K8s alternative. Now under IBM. BSL license since Aug 2023 — consider alternatives. |
| **Pulumi** | v3.220.0 | IaC in Python. Now supports HCL natively (Q1 2026). CrossGuard for policy-as-code. |
| **OpenTofu** | v1.11.4 | Open-source Terraform fork. Ephemeral values. Supported until Aug 2026. |
| **SkyPilot** | Active development | Multi-cloud FinOps. Spot instances. Sky Serve for model deployment. |
| **MkDocs Material** | v9.x | Documentation-as-code standard for Python projects. |
| **Argo CD** | v3.3.0 | CNCF Graduated. GitOps standard. Built-in UI. |
| **OPA** | Stable | Policy-as-code. Rego language. Gatekeeper for K8s. |

---

## Integrated Plan: P2 Tasks + xOps Architecture

### Tier 1: IMPLEMENT (code changes in this branch)

These are the remaining P2 tasks that directly improve scaffold credibility:

| ID | Task | Effort | Teaching Value |
|---|---|---|---|
| **P2-1** | Pipeline DAG + execution script | 2h | Pipeline orchestration patterns (Unit 2/3) |
| **P2-6** | Production Dockerfile | 1h | Container security (Unit 4) |
| **P2-7** | Prometheus metrics endpoint | 2h | Application metrics (Unit 6) |

**Rationale**: These three create the minimum viable "production-ready" signal. A pipeline DAG shows you know orchestration. A prod Dockerfile shows you know containers. A `/metrics` endpoint shows you know observability. Together they demonstrate infrastructure competence without bloat.

### Tier 2: PRD NODE EXPANSION (decision files only)

New decision nodes to add to `_network.yaml`:

| Node ID | Level | Title | Options |
|---|---|---|---|
| `orchestrator_choice` | L4_deployment | Pipeline Orchestrator | `none_scripts` / `prefect` / `dagster` / `celery` / `airflow` |
| `ml_monitoring` | L5_operations | ML Model Monitoring | `none` / `evidently` / `whylogs` / `custom_drift` |
| `documentation_tooling` | L5_operations | Documentation-as-Code | `mkdocs_material` / `sphinx` / `docusaurus` / `none_markdown` |
| `cd_strategy` | L4_deployment | Continuous Deployment Strategy | `github_actions_deploy` / `argocd` / `flux` / `platform_native` |
| `policy_as_code` | L5_operations | Policy-as-Code | `none` / `opa_gatekeeper` / `pulumi_crossguard` / `kyverno` |
| `finops_strategy` | L5_operations | FinOps & Cloud Cost Optimization | `none_manual` / `skypilot` / `infracost` / `kubecost` |
| `ethics_governance` | L5_operations | EthicsOps & Governance-as-Code | `none` / `model_cards` / `full_governance` |

**Rationale**: PRD nodes are the right artifact for open-ended architectural decisions. They document trade-offs, conditional probabilities, and team-archetype weights without committing code.

### Tier 3: GITHUB ISSUES (documentation + future work)

Issues to create in project board (https://github.com/users/petteriTeikari/projects/4):

| Issue Title | Labels | Description |
|---|---|---|
| **Add OpenTelemetry auto-instrumentation for FastAPI** | `enhancement`, `observability` | Wire `opentelemetry-instrumentation-fastapi` + OTLP exporter. Grafana Cloud or local Tempo backend. |
| **Add Grafana + Prometheus + Loki + Tempo to docker-compose.dev.yml** | `enhancement`, `devex` | Local observability stack for development. Pre-built dashboards for API latency, agent traces, drift metrics. |
| **Evaluate Prefect 3.x for pipeline orchestration** | `research`, `architecture` | Compare Prefect (flow-centric, Pydantic-friendly) vs Dagster (asset-centric) for our 5-pipeline architecture. |
| **Add Evidently ML monitoring integration** | `enhancement`, `monitoring` | Wire Evidently reports for confidence score distribution, source agreement drift, calibration quality. |
| **Create MkDocs Material documentation site** | `enhancement`, `docs` | `mkdocs.yml` + deploy to GitHub Pages. Auto-generate API docs from docstrings. |
| **Evaluate IaC: Pulumi (Python) vs OpenTofu** | `research`, `infrastructure` | Compare Pulumi CrossGuard policy-as-code vs OpenTofu with OPA. Decision: L4 `iac_tooling` node. |
| **Add SkyPilot configuration for multi-cloud training** | `enhancement`, `finops` | `sky.yaml` for spot instance orchestration. Relevant when attribution model training scales. |
| **Add EthicsOps model cards for attribution engine** | `enhancement`, `governance` | Model Card for conformal prediction calibration. Bias documentation for center-bias detection. |
| **Add API rate limiting (slowapi)** | `enhancement`, `security` | Per-IP rate limiting on REST endpoints. Already have ETL-level rate limiter. |
| **Wire BatchEnvelope into ETL/resolution pipeline** | `enhancement`, `architecture` | Currently defined but unused. Would demonstrate batch processing patterns. |
| **Create prompt registry with versioning** | `enhancement`, `llmops` | Named prompt versions, env var selection, trace metadata logging. |
| **Add Braintrust eval framework stubs** | `enhancement`, `llmops` | Eval fixture dataset + integration tests for agent output quality. |

### Tier 4: DEFERRED (document in PRD, no action now)

These are important for a real product but would be feature creep for a preprint:

- **Kubernetes/Nomad container orchestration** — Document in PRD, don't implement. Note: Nomad now under IBM/BSL, prefer K3s or Docker Swarm for lightweight alternative.
- **Argo CD / Flux GitOps** — Document in PRD. Need K8s first.
- **Pulumi CrossGuard policy enforcement** — Document in PRD. Need IaC first.
- **Sky Computing / SkyPilot** — Document in PRD. Need ML training workload first.
- **Full governance-as-code pipeline** — Document in PRD. ArchUnit-style checks interesting but premature.

---

## P2 Task Self-Reflection & Cross-Check

### P2-1: Pipeline DAG + execution script → IMPLEMENT
**Self-check**: MLOps teaching reviewer rated this highest priority P2. Without a visible DAG, the 5-pipeline architecture exists only in documentation. A simple `pipeline/dag.py` with stage definitions + `scripts/run-full-pipeline.sh` shows orchestration readiness.
**Risk**: Low — just defines stages and order. No actual Prefect/Celery dependency.
**Reviewer convergence**: Portfolio reviewer recommends making the DAG **declarative** (Pydantic model defining stages, deps, and entry points) rather than imperative (script with procedural calls). This shows architectural maturity — the DAG definition is data, the runner is generic.

### P2-2: Prompt registry → GITHUB ISSUE
**Self-check**: Portfolio reviewer demoted this. System prompt is already good quality. Versioning is polish, not credibility. Better as a tracked issue.

### P2-3: Braintrust evals → GITHUB ISSUE
**Self-check**: Important for LLMOps maturity but requires actual agent interaction fixtures. Better as a tracked issue with eval dataset specification.

### P2-4: BatchEnvelope wiring → GITHUB ISSUE
**Self-check**: Useful for demonstrating batch processing patterns but low visibility. Not a first-impression driver.

### P2-5: Rate limiting → GITHUB ISSUE
**Self-check**: Production-necessary but `slowapi` integration is a 30-minute task. Better tracked as issue, implemented when we do the prod Dockerfile.

### P2-6: Production Dockerfile → IMPLEMENT
**Self-check**: This is the **single most visible gap** for anyone evaluating production readiness. Multi-stage build, non-root user, health check. High signal, low effort.

### P2-7: Prometheus metrics → IMPLEMENT
**Self-check**: The observability tracer exists but has no metrics counterpart. A `/metrics` endpoint with `prometheus_client` closes the "we know observability" loop. Also enables the Grafana Docker dev story (Issue).
**Portfolio reviewer "one more thing"**: Ship a pre-built Grafana dashboard JSON alongside the `/metrics` endpoint. This transforms the monitoring from "we export metrics" to "we have a ready-to-use dashboard" — much stronger signal for production readiness. Add to Docker Compose monitoring profile with auto-provisioning.

---

## Docker Dev Observability Stack (Reference Architecture)

When the GitHub Issue for local Grafana is implemented, the `docker-compose.dev.yml` would add:

```yaml
# Observability stack (optional, profile: monitoring)
prometheus:
  image: prom/prometheus:v2.51.0
  volumes:
    - ./docker/prometheus.yml:/etc/prometheus/prometheus.yml
  ports:
    - "9090:9090"

grafana:
  image: grafana/grafana:10.4.0
  environment:
    GF_AUTH_ANONYMOUS_ENABLED: "true"
    GF_AUTH_ANONYMOUS_ORG_ROLE: Admin
  volumes:
    - ./docker/grafana/dashboards:/etc/grafana/provisioning/dashboards
    - ./docker/grafana/datasources:/etc/grafana/provisioning/datasources
  ports:
    - "3001:3000"
  depends_on:
    - prometheus

loki:
  image: grafana/loki:2.9.0
  ports:
    - "3100:3100"

tempo:
  image: grafana/tempo:2.4.0
  ports:
    - "3200:3200"    # tempo query
    - "4317:4317"    # OTLP gRPC
```

**Key insight**: Use Docker Compose `profiles` so monitoring is opt-in:
```yaml
profiles: ["monitoring"]
# Start with: docker compose --profile monitoring up
```

This way the default `docker compose up` stays lightweight (postgres + app), but developers who want the full observability experience can opt in.

---

## PRD Network Expansion Plan

### Current state: v1.8.0, 37 nodes, 79 edges, 5 levels
### Target state: v1.9.0, 44 nodes, ~95 edges, 5 levels

> **Reviewer note**: Additive node expansion is a minor version bump (v1.9.0), not a breaking change (v2.0.0). Architecture reviewer validated DAG acyclicity via Kahn's algorithm: all 44 proposed nodes visited, zero cycles.

New edges (reviewer-validated):

```
# Orchestrator (consider L3 vs L4 placement — arch reviewer)
service_decomposition → orchestrator_choice (strong)
build_vs_buy_posture → orchestrator_choice (moderate)
compute_platform → orchestrator_choice (moderate)

# ML Monitoring (reverse edge direction per arch reviewer:
#   ml_monitoring depends ON observability_stack, not the reverse)
data_quality_strategy → ml_monitoring (strong)
observability_stack → ml_monitoring (moderate)
ai_framework_strategy → ml_monitoring (moderate)

# Documentation
build_vs_buy_posture → documentation_tooling (weak)
ci_cd_pipeline → documentation_tooling (moderate)

# CD Strategy
ci_cd_pipeline → cd_strategy (strong)
compute_platform → cd_strategy (strong)
container_strategy → cd_strategy (moderate)
cd_strategy → observability_stack (moderate)  # arch reviewer addition

# Policy-as-Code
iac_tooling → policy_as_code (strong)
regulatory_posture → policy_as_code (moderate)
container_strategy → policy_as_code (moderate)

# FinOps
compute_platform → finops_strategy (strong)
scaling_strategy → finops_strategy (moderate)

# Ethics/Governance
regulatory_posture → ethics_governance (strong)
ai_framework_strategy → ethics_governance (moderate)
data_quality_strategy → ethics_governance (moderate)
```

Additional changes to existing nodes:
- Add `opentofu` option to `iac_tooling` node (arch reviewer)

---

## Recommended Execution Order

### Phase 1: Implement (this branch, ~5 hours)
1. **P2-7**: Prometheus metrics endpoint (2h)
2. **P2-6**: Production Dockerfile (1h)
3. **P2-1**: Pipeline DAG + execution script (2h)

### Phase 2: PRD Expansion (this branch, ~3 hours)
4. Add 7 new PRD decision nodes
5. Bump `_network.yaml` to v2.0.0
6. Add edges from existing nodes

### Phase 3: GitHub Issues (manual, ~30 min)
7. Create 12 issues in project board
8. Tag with appropriate labels
9. Link to PRD decision nodes where applicable

### Phase 4: Optional P2 Tasks (separate branch)
10. P2-2 through P2-5 as individual PRs

---

## Reviewer Agent Matrix

| Reviewer | Focus | Key Question |
|---|---|---|
| **Architecture** | Does the PRD expansion maintain DAG acyclicity? Are edges well-typed? | "Are the 7 new nodes at the right levels?" |
| **MLOps Teaching** | Does the plan cover MLOps curriculum units adequately? | "Would a student learning MLOps find the right patterns?" |
| **Portfolio/Hiring** | Does the scaffold signal production readiness without bloat? | "Would a senior engineer see competence or over-engineering?" |

---

## Appendix: Technology Notes from Knowledge Base

### Orchestrators (from MLOps - Pipelines - Prefect.md)
- **Prefect 3.x**: Python-native, decorator-based (`@flow`, `@task`). Good Pydantic integration. Self-hosted or cloud. Best fit for our Python/FastAPI stack.
- **Dagster**: Asset-centric, better for data-heavy pipelines. Heavier setup but better observability.
- **Airflow**: Industry standard but heavy. DAG definition is more complex. Overkill for this scaffold.
- **Celery**: Task queue, not orchestrator. Good for async jobs. We already have Valkey (Redis-compatible).
- **Metaflow**: Netflix's ML workflow tool. Great for ML experiments. Less general-purpose.

### Kubernetes Alternatives (from MLOps - Pipelines - Kubernetes.md)
- **K3s**: Lightweight K8s (single binary, 512MB RAM). Good for edge/small deployments.
- **Nomad**: HashiCorp. Now under IBM with BSL license. Consider open-source alternatives.
- **Docker Swarm**: Simple multi-host. Dead in practice but fine for small-scale.
- **Kamal 2**: Ruby ecosystem (37signals). Docker deploys without K8s.

### Policy-as-Code (from MLOps - Policy-as-Code.md)
- **OPA/Gatekeeper**: Rego language, K8s-native. Industry standard.
- **Kyverno**: K8s-native, YAML-based policies. Simpler than OPA.
- **Pulumi CrossGuard**: Python-based policy checks. Natural fit if using Pulumi IaC.
- **Sentinel**: HashiCorp. BSL license. Avoid for new projects.

### Sky Computing (from MLOps - Sky Computing.md)
- **SkyPilot**: Multi-cloud workload orchestration. Spot instances. Sky Serve for serving.
- Relevant when ML training workloads scale beyond single-machine.
- Good for FinOps optimization of GPU costs.

### Documentation (from MLOps - Documentation.md)
- **MkDocs Material**: Python ecosystem standard. Markdown-based. GitHub Pages deploy.
- **Sphinx**: More powerful but heavier. RST-based (or MyST for Markdown). Better for API docs.
- **Docusaurus**: React-based. Overkill for Python projects.

### CD Strategies (from MLOps - Deploy - Strategies.md)
- **Argo CD v3.3.0**: CNCF Graduated. GitOps with built-in UI. Requires K8s.
- **Flux**: Lighter, more composable. Also CNCF Graduated. No built-in UI.
- **Platform-native**: Render/Railway auto-deploy from branch. Simplest path.

### EthicsOps (from MLOps - EthicsOps.md)
- Model Cards for ML components (conformal prediction, entity resolution)
- Bias documentation (center-bias detection already implemented)
- Responsible AI guidelines for attribution decisions

### Governance-as-Code (from MLOps - Governance-as-code.md)
- Architectural fitness functions (ArchUnit-style)
- Data lineage tracking (partially covered by provenance chain)
- Schema governance (PRD node exists)

---

## Converged Reviewer Feedback (v1.1)

### Architecture Reviewer — APPROVE 8/10
- **DAG acyclicity verified**: Kahn's algorithm visited all 44 proposed nodes (37 existing + 7 new). Zero cycles.
- **Level placements**: Generally correct. `orchestrator_choice` could arguably live at L3 (infrastructure) rather than L4 (deployment) — teams typically choose orchestrators before deployment strategy. Decision: keep at L4 for now, revisit if it creates awkward edge directions.
- **Edge direction**: `observability_stack → ml_monitoring` is correct (monitoring depends on observability infra). Arch reviewer initially flagged for review but confirmed direction is valid.
- **Missing edge**: `cd_strategy → observability_stack` — CD pipelines should feed observability (deploy events, rollback metrics). Added.
- **Existing node update**: Add `opentofu` option to `iac_tooling` node (open-source Terraform fork, v1.11.4).
- **Version bump**: v1.9.0, not v2.0.0 — adding nodes is additive, not breaking.
- **Stale data fix**: Plan originally said "35 nodes" — actual count is 37. Corrected.

### MLOps Teaching Reviewer — APPROVE
- Verified pandera was removed (P1-2 done in C2).
- Confirmed observability module, config, and pipeline structure exist.
- Verified no pipeline DAG or scripts exist yet (P2-1 is net new).
- Confirmed tracer pattern follows pluggable backend pattern taught in MLOps curriculum.

### Portfolio/Hiring Reviewer — APPROVE 7.5/10 (projected 8.5 with "one more thing")
- **Top positive**: Probabilistic PRD is a genuine differentiator — hiring managers see architectural thinking, not just code.
- **Top risk**: Pipeline DAG could be over/under-engineered. Mitigated by declarative Pydantic model approach.
- **"One more thing"**: Pre-built Grafana dashboard JSON + Docker Compose monitoring profile. Transforms `/metrics` from "we export data" to "we have a dashboard." Estimated +1.0 to portfolio score.
- **Previous red flags** (from earlier reviews): MCP dead seed, health check issues — all verified as fixed in C1-C4.
- **DAG recommendation**: Make it declarative (Pydantic model) not imperative. The DAG definition should be data that a generic runner executes.

### Convergence Summary
All three reviewers approve. Key converged recommendations incorporated:
1. Declarative Pydantic DAG model (portfolio + MLOps)
2. Pre-built Grafana dashboard alongside `/metrics` (portfolio)
3. Version v1.9.0 not v2.0.0 (architecture)
4. `cd_strategy → observability_stack` edge (architecture)
5. `opentofu` option in `iac_tooling` (architecture)
6. Fixed stale node count 35 → 37 (architecture)
