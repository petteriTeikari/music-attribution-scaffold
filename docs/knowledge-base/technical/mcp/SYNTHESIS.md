# MCP Knowledge Synthesis

Model Context Protocol patterns and security considerations for the system.

## Protocol Status (February 2026)

- **Governance**: Donated to Agentic AI Foundation (AAIF) under Linux Foundation (Dec 2025)
- **Current Spec**: November 2025 (2025-11-25)
- **Registry**: MCP Registry preview (Sep 2025) - single source of truth for servers

## Key Specification Updates

### [November 2025](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- OAuth Resource Server classification (mandatory)
- Resource Indicators ([RFC 8707](https://www.rfc-editor.org/rfc/rfc8707)) for token scoping
- SEP-1024: Client security requirements
- SEP-835: Default scopes definition
- Asynchronous execution support
- Enterprise governance features

### June 2025
- Authorization handling clarification
- Token mis-redemption threat mitigation ([Auth0 analysis](https://auth0.com/blog/mcp-specs-update-all-about-auth/))

## Security Threat Model

### Attack Success Rates
- **40.71%** average across implementations ([MCP Security Bench](https://arxiv.org/abs/2510.15994))
- **85%+** compromise at least one major platform ([MCPSecBench](https://arxiv.org/abs/2508.13220))

### Four Attack Surfaces

| Surface | Threat | The System Mitigation |
|---------|--------|---------------------|
| Tool Manifest | Prompt injection via metadata | Three-stage detection |
| Server Communication | MITM, unauthorized registration | SHA-256 whitelist |
| Resource Access | Path traversal, credential theft | Capability sandbox |
| Execution Environment | Code injection, escalation | Subprocess executor |

## the attribution MCP Architecture

### Three-Tier Trust Model

```python
class AccessTier(Enum):
    INTERNAL = 1   # Full R/W, unlimited
    VERIFIED = 2   # R + scoped W, 1000/hr
    PUBLIC = 3     # Read-only, 100/hr
```

### Tool Definitions

| Tool | Access | Purpose |
|------|--------|---------|
| `get_artist_attribution` | All | Query attribution data |
| `search_songs` | All | Search with confidence filter |
| `verify_credit` | All | Verify specific claims |
| `check_permissions` | Tier 2+ | AI training consent |
| `get_usage_audit` | Tier 2+ | Artist audit trail access |

## Commerce Integration

### Protocol Landscape (2025-2026)

| Protocol | Provider | MCP Relationship |
|----------|----------|------------------|
| ACP | OpenAI + Stripe | Uses MCP for tool access |
| AP2 | Google | Compatible via UCP |
| TAP | Visa | Agent verification layer |
| A2A | Linux Foundation | Peer coordination |

### Agentic Commerce Protocol Relationships

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'background': '#fcfaf5', 'primaryColor': '#1E3A5F', 'lineColor': '#5C5C5C'}}}%%
graph TB
    subgraph foundation[" Foundation Layer "]
        MCP[MCP<br/>Model Context Protocol<br/>Linux Foundation]
    end

    subgraph commerce[" Commerce Protocols "]
        ACP[ACP<br/>OpenAI + Stripe<br/>Payment orchestration]
        AP2[AP2<br/>Google<br/>Enterprise shopping]
        TAP[TAP<br/>Visa<br/>Agent verification]
    end

    subgraph coordination[" Coordination "]
        A2A[A2A<br/>Agent-to-Agent<br/>Peer coordination]
        UCP[UCP<br/>Universal Commerce<br/>Unification layer]
    end

    subgraph system[" System Position "]
        AURA[the attribution MCP Server<br/>Attribution + Permissions]
    end

    MCP --> ACP
    MCP --> AP2
    MCP --> A2A
    AP2 --> UCP
    ACP --> UCP
    TAP --> ACP
    TAP --> AP2

    AURA --> MCP
    AURA -.->|"Permission checks"| ACP
    AURA -.->|"Attribution data"| A2A

    style MCP fill:#1E3A5F,color:#fff
    style ACP fill:#D4A03C,color:#000
    style AP2 fill:#D4A03C,color:#000
    style TAP fill:#4A7C59,color:#fff
    style A2A fill:#2E7D7B,color:#fff
    style UCP fill:#8B8B8B,color:#fff
    style AURA fill:#1E3A5F,color:#fff
```

**System Integration Points**:
- **ACP**: Permission verification before AI music transactions
- **A2A**: Attribution data exchange between music AI agents
- **TAP**: Artist identity verification for high-value transactions

### Visual: Agentic Commerce Ecosystem

![Agentic Commerce Ecosystem](../../figures/assets/fig-domain-06-agentic-commerce-ecosystem.jpg)

*the system in agentic commerce: MCP-based attribution data flows to commerce protocols (ACP, AP2, TAP) enabling verified AI music transactions. [Market opportunity $1T US / $3-5T global by 2030](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-agentic-commerce-opportunity-how-ai-agents-are-ushering-in-a-new-era-for-consumers-and-merchants); [top AI shopping models achieve only 56%](https://arxiv.org/abs/2512.04921) due to hallucination on prices/links.*

### MCP Payment Servers

- Worldpay (Nov 2025): 52B+ transactions
- Adyen (Nov 2025): Direct LLM integration
- Visa (2026): Native API access

## Implementation Checklist

- [x] OAuth 2.0 integration design
- [x] Three-tier access control design
- [x] Tool definitions in PRD
- [ ] RFC 8707 Resource Indicators
- [ ] MCP Registry submission
- [ ] Rate limiting implementation
- [ ] Audit logging for compliance

## Cross-References

- [agentic-systems-research-2026-02-03.md](../agentic-systems-research-2026-02-03.md) - Full research synthesis
- [mcp-server-prd.md](../../../prd/mcp-server-prd.md) - API specification
- [MCP Specification](https://modelcontextprotocol.io/specification/2025-11-25)
