# Agentic Systems Knowledge Synthesis

Multi-agent vs single-agent architecture decisions for the system.

## Key Research Finding: Single-Agent Preferred

Based on Google Research (2025) empirical scaling principles:

### Decision Criteria

| Condition | Recommendation | The System Relevance |
|-----------|----------------|-------------------|
| Accuracy > 45% | Don't add agents | Attribution engine target: 90%+ |
| Sequential tasks | Single-agent | Fetch → Resolve → Score pipeline |
| Parallel decomposable | Multi-agent OK | Not applicable |
| 3+ major functions | Hierarchical | Future consideration |

### Error Amplification Risk

- **17.2x** error amplification in independent parallel multi-agent systems
- Attribution requires sequential integrity (entity resolution depends on fetch accuracy)
- Cascading failures unacceptable for confidence scoring

## System Architecture Decision

**Chosen**: Single-agent with tool orchestration

```
┌─────────────────────────────────────────────────────────────────┐
│                Attribution Agent (Single)                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │  Discogs    │  │ MusicBrainz │  │  the system   │  Tools      │
│  │   Adapter   │  │   Adapter   │  │   Own Data  │             │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘             │
│         │                │                │                     │
│         └────────────────┼────────────────┘                     │
│                          │                                      │
│                          ▼                                      │
│                 ┌─────────────────┐                             │
│                 │ Entity Resolver │                             │
│                 └────────┬────────┘                             │
│                          │                                      │
│                          ▼                                      │
│                 ┌─────────────────┐                             │
│                 │Confidence Scorer│                             │
│                 └─────────────────┘                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Why Not Multi-Agent?

1. **Sequential dependency**: Entity resolution requires complete fetch data
2. **Error cascade**: Incorrect entity match propagates to confidence
3. **Orchestration overhead**: Tool calling sufficient for parallelizing fetches
4. **Debugging complexity**: Single agent easier to trace and audit

## Industry Context (2026)

### Adoption Statistics
- Agent adoption: 11% → 42% in two quarters
- 40% of enterprise apps will feature agents by 2026 (up from <5% in 2025)
- 86% of copilot spending ($7.2B) on agent-based systems

### Key Frameworks

| Framework | Status | Use Case |
|-----------|--------|----------|
| LangGraph 1.0 | Stable (Jan 2026) | Durable agents |
| A2A | Production | Peer coordination |
| MCP | Production | Tool access |

## Future Considerations

### When to Reconsider Multi-Agent

- If adding parallel user-facing features (chat + admin + analytics)
- If attribution sources exceed 5 with independent verification
- If real-time collaborative verification needed

### Hierarchical Option

If multi-agent becomes necessary:
- Keep teams to 3-7 agents
- Use team leaders for subgroup coordination
- Communication overhead grows exponentially with agent count

## Cross-References

- [agentic-systems-research-2026-02-03.md](../agentic-systems-research-2026-02-03.md) - Full research
- [attribution-engine-prd.md](../../../prd/attribution-engine-prd.md) - Engine design
- [Google Research Blog](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)
