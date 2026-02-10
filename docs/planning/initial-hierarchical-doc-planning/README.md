# Initial Hierarchical Documentation Planning

**Status**: Draft v6 - Final (FinOps Optimization Added)
**Created**: 2026-02-03
**Updated**: 2026-02-03

## Overview

This directory contains the planning artifacts for designing the system' documentation and knowledge management architecture using **Minimum Viable Architecture (MVA)** principles.

## Documents

| Document | Purpose |
|----------|---------|
| [PLAN.md](PLAN.md) | Comprehensive architecture plan (v6 final with FinOps optimization) |
| [finops-optimization-plan.md](../finops-optimization-plan.md) | Detailed cloud cost optimization and multi-hypothesis infrastructure |
| [original-prompt.md](original-prompt.md) | Original requirements + clarifications + UQ bibliography (27 papers) |

## Key Decisions (Resolved)

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Documentation format | Pure Markdown (Option A) | Simple, Claude Code native, no LaTeX needed |
| Knowledge base structure | Hybrid with SYNTHESIS.md (Option 3) | RAG-optimized aggregation at each level |
| Database | PostgreSQL + pgvector | Neo4j overkill; document upgrade criteria |
| AI frameworks | Pure Python + Pydantic | Avoid LangChain; use LangGraph only if needed |
| UQ approach | Conformal prediction (MAPIE) | Formal guarantees; works without logit access |
| Data warehouse | Hetzner Object Storage (Parquet) + PostgreSQL | €7-34/month; same datacenter = free transfer |
| Entity resolution | Rule-based + phonetic (sprint) | Cold start via ISNI/Wikidata; embedding post-sprint |
| Batch vs real-time | Event sourcing (both paths) | Same ChangeEvent format enables migration |
| IaC tool | Pulumi (Python) | Same language as app; official Hetzner provider |
| Managed DB (MVP) | Neon PostgreSQL (€17.50/month) | Scale-to-zero, database branching, pgvector |
| Object storage | Cloudflare R2 | Zero egress costs for audio files |

## Recommendation Summary

- **Architecture**: Pure Markdown + SYNTHESIS.md pattern
- **UQ Foundation**: Beigi et al. 2024 taxonomy + conformal prediction
- **MVA Principle**: Solve current problems, anticipate but don't solve future ones
- **Key pattern**: SYNTHESIS.md at every directory level for RAG aggregation

## v6 Additions (Final)

| Section | New Content |
|---------|-------------|
| 6.3 | Query Router, Multi-Agent Pipeline, Reranker architecture |
| 6.3.1 | Multi-Agent Orchestration (Hub-and-Spoke pattern for source aggregation) |
| 6.3.2 | MCP Security (Nov 2025 spec, RFC 8707 Resource Indicators, Three-Tier Trust) |
| 6.5 | Agentic RAG with Verification Loops (max 2 revisions) |
| 8.4 | Context Engineering (prompt caching, YAML tokens, layered disclosure) |
| **11** | **Data Warehouse Architecture** |
| 11.1-11.9 | Storage layers, Entity Resolution, Database schema, Migration paths |
| **11.10** | **FinOps & Infrastructure Optimization** |
| - | Recommended stack by phase (Render→Kamal, Neon, R2) |
| - | Cloud credit strategy (NVIDIA Inception, OVHcloud, Azure) |
| - | Portability guarantees (Pulumi IaC, containerization) |
| **12** | **Mogen Integration & Voice Architecture (NEW)** |
| 12.1 | Architectural Boundary (the system as Data Provider) |
| 12.2 | MCP Interface for Third-Party Clients (Mogen, ChatGPT) |
| 12.3 | Hierarchical PRD Structure Pattern (token-efficient progressive disclosure) |
| 12.4 | Team Scalability Through Decoupling (solo dev ↔ team) |
| 12.5 | Voice Cost Reference (Vapi ~$0.12/conv → Pipecat ~$0.02/conv) |
| **Separate Doc** | [finops-optimization-plan.md](../finops-optimization-plan.md) - Full multi-hypothesis analysis |

## Reviewers

| Reviewer | Focus | Agent ID |
|----------|-------|----------|
| Architecture | Structure, scalability, retrieval | a29a0d7 |
| UQ Research | Uncertainty quantification accuracy | afb1470 |
| Implementation | Roadmap feasibility, sprint readiness | a60282d |
| Data Architecture | DuckDB/Parquet scalability, migration path | a3349cb |
| Entity Resolution | Matching algorithms, cold start, confidence | a95c53e |
| Real-time Systems | CDC, event sourcing, caching | a6aed02 |
| Cost Optimization | Hetzner pricing, self-managed vs managed | ad922c8 |
| Voice/Mogen Integration | MCP interface, hierarchical PRD, team scalability | abf5fe9 |

## Next Steps

1. ~~Review PLAN.md~~ → v6 complete with FinOps optimization
2. ~~Resolve open questions~~ → Data source, entity resolution, cost questions resolved
3. ~~Integrate 2026 patterns~~ → Multi-agent, MCP security, context engineering
4. ~~Add data architecture~~ → Section 11 with full warehouse design
5. ~~Add FinOps plan~~ → Section 11.10 + separate detailed plan
6. **Approve architecture** ← Current step
7. Begin Phase 1A (directory structure lock)

## Reference Sources Analyzed

### Primary Research
- dpp-agents knowledge-base (692 files, 17 themes)
- dpp-agents PRD system (8 PRDs, ~8,000 lines)
- sci-llm-writer LaTeX hierarchy (70 .tex files, 6 domains)
- Meta-learning documents (4 failure analysis docs)
- Music traceability domain research
- AI Passport GEO provenance framework

### External References
- Netflix GenAI webinar (Anthropic 2025)
- Cursor semantic search blog (2026)
- Edge et al. 2025 - Graph RAG
- StartupOps/MVA principles (InfoQ)

### UQ Bibliography (27 papers)
- **Foundational**: Beigi et al. 2024 (LLM uncertainty taxonomy)
- **Conformal**: Angelopoulos & Bates 2021, Wang et al. 2025 (SConU, COIN)
- **RAG**: Soudani et al. 2025 (why UQ fails in RAG)
- **Agentic**: Duan et al. 2025 (UProp), Fleming et al. 2025

### Latest Research (Jan 2025 - Feb 2026)
- TECP: Token-Entropy Conformal Prediction for LLMs
- Bayesian RAG: Uncertainty-aware retrieval
- MAPIE v1: Production conformal prediction library
- UQLM: Hallucination flagging without ground truth
