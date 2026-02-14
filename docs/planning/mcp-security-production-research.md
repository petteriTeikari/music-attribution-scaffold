# MCP Security, Production Readiness, and the Evolving Agentic Protocol Landscape

**Date:** 2026-02-14
**Status:** Research Report
**Scope:** Security benchmarks, real-world vulnerabilities, defense frameworks, competing protocols, production deployment, regulatory implications
**Companion to:** Teikari, P. (2026). *Music Attribution with Transparent Confidence*. SSRN No. 6109087.

---

## 1. Executive Summary

The Model Context Protocol (MCP) has rapidly evolved from Anthropic's internal tool-integration standard to a Linux Foundation-governed open protocol with adoption across major AI platforms. However, emerging security research paints an alarming picture: benchmark studies demonstrate **85%+ compromise rates** across leading AI platforms (Cheng et al. 2025), an **inverse scaling paradox** where more capable models are *more* vulnerable to MCP-based attacks (Cheng et al. 2025), and real-world CVEs in production servers affecting hundreds of thousands of users (CVE-2025-53967, CVE-2025-6514).

This report synthesizes findings from 50+ research papers across four sub-collections (architecture, security, implementation, general) to provide the Music Attribution Scaffold project with an evidence-based security and productionization roadmap. Key findings include:

- **Attack surface is broad**: Tool poisoning (72.8% ASR per MCPTox), supply chain manipulation (16.7–64.7% ASR), prompt injection via tool metadata, rug pull attacks, and cross-server contamination all represent active threats.
- **Authentication is broken in practice**: 53% of deployed MCP servers use insecure static secrets; only 8.5% implement OAuth (Guo et al. 2025).
- **Defenses exist but are immature**: MCP-Guard achieves 96.01% neural detection with 12x speedup over LLM-only approaches (Shan et al. 2025); MI9 runtime governance reaches 99.81% violation detection (Chandra et al. 2025). Neither is widely deployed.
- **The protocol landscape is fragmenting**: ACP (OpenAI + Stripe), A2A (Google → Linux Foundation), TAP (Visa), and XAA (Okta) each claim adjacent territory, with convergence toward a MCP + A2A + identity layer stack.
- **Regulation is accelerating**: EU AI Act GPAI obligations became enforceable August 2025, with Art. 12 logging requirements directly relevant to MCP audit infrastructure and penalties reaching EUR 35M or 7% of global turnover.

**Recommendation**: Adopt a defense-in-depth strategy combining schema validation, neural classifiers, sandboxed execution, and immutable audit logging — aligned with the scaffold's existing four-layer security architecture.

---

## 2. MCP Protocol Evolution

### 2.1 Origin and Governance

MCP was publicly released by Anthropic in November 2024 as an open standard for connecting AI models to external tools and data sources (Anthropic 2024). The protocol provides a structured JSON-RPC 2.0 interface through which AI systems can discover, invoke, and receive results from external capabilities — a significant advance over ad-hoc function calling implementations.

In December 2025, Anthropic donated MCP to the newly formed **Agentic AI Foundation (AAIF)** under the Linux Foundation umbrella (AAIF 2025). Platinum members include AWS, Anthropic, Google, Microsoft, and OpenAI — a remarkable alignment of otherwise competing interests. The AAIF governance structure includes a Technical Steering Committee (TSC) with elected maintainers and a formal RFC process for specification changes.

### 2.2 Specification Timeline

| Date | Version | Key Changes |
|------|---------|-------------|
| Nov 2024 | Initial release | JSON-RPC 2.0, tools/resources/prompts primitives |
| Mar 2025 | 2025-03-26 | OAuth 2.1 authorization framework mandated |
| Jun 2025 | 2025-06-18 | Streamable HTTP transport, elicitation requests |
| Nov 2025 | 2025-11-25 | OAuth Resource Server classification, RFC 8707 resource indicators, SEP-1024 client security, asynchronous execution |
| Sep 2025 | Registry preview | MCP Registry for server discovery |
| Dec 2025 | AAIF donation | Linux Foundation governance, multi-stakeholder TSC |

### 2.3 Adoption Metrics

As of early 2026, the MCP ecosystem has grown substantially:

- **4,000+ open-source MCP servers** published across GitHub and the MCP Registry (AAIF 2025)
- **Integration by major platforms**: Claude Desktop, Cursor, Windsurf, VS Code Copilot, Cline, and others ship with native MCP client support
- **Enterprise adoption**: Block, Apollo, Replit, and Sourcegraph have deployed MCP-based integrations in production (Anthropic 2025)

This rapid adoption has outpaced security hardening — a pattern familiar from earlier protocol adoption curves (OAuth 1.0, early REST APIs) but magnified by the autonomous agent context where tools execute with minimal human oversight.

---

## 3. Security Landscape: Benchmarks and Attack Surfaces

### 3.1 MCPSecBench: The Inverse Scaling Paradox

Cheng et al. (2025) introduced MCPSecBench, the first comprehensive security benchmark for MCP implementations. Their findings are stark:

- **85%+ of attacks compromise at least one major AI platform** when using MCP tools
- **Inverse scaling paradox**: More capable models (GPT-4o, Claude 3.5 Sonnet) are *more* vulnerable than less capable ones. The authors attribute this to stronger instruction-following capabilities making powerful models more susceptible to adversarial instructions embedded in tool descriptions.
- Attack categories tested: tool poisoning, rug pull attacks, server compromise, and cross-server data exfiltration

The inverse scaling finding is particularly concerning for production deployments that default to the most capable available model — a pattern the Music Attribution Scaffold follows with its FallbackModel configuration defaulting to Claude Haiku 4.5 for cost efficiency but escalating to Sonnet/Opus for complex queries.

### 3.2 MSB: Systematic Attack Surface Mapping

Peng et al. (2025) developed MSB (MCP Security Bench), a systematic benchmark covering **984 test cases** across nine LLM models. Key results:

- **40.71% average attack success rate (ASR)** across all models and attack types
- Four attack surfaces identified: tool manifest manipulation, communication channel interception, resource access abuse, and execution environment exploitation
- **22% of tested servers** had path traversal vulnerabilities
- The benchmark revealed that attack success varies significantly by model: some models showed >60% ASR on tool poisoning while maintaining <20% ASR on prompt injection, suggesting that defenses must be multi-layered rather than model-dependent.

### 3.3 MCPTox: Tool Poisoning at Scale

Zhang et al. (2025) focused specifically on tool poisoning attacks with MCPTox:

- **72.8% attack success rate** for tool description poisoning — where adversarial instructions embedded in tool metadata manipulate model behavior
- Attacks succeed even when the poisoned tool is never actually invoked; merely being present in the tool manifest is sufficient to influence model behavior
- The "shadow tool" pattern: a malicious server registers a tool with a description that instructs the model to exfiltrate data through a different, seemingly legitimate tool

### 3.4 Supply Chain Attacks

Guo et al. (2025) examined supply chain vulnerabilities in the MCP ecosystem:

- **16.7–64.7% ASR** depending on attack sophistication and target model
- Attack vectors include: typosquatting of popular server names in the MCP Registry, dependency confusion via malicious npm/pip packages, and version pinning manipulation
- The authors found that **fewer than 5% of MCP server installations** verify server identity through cryptographic means

### 3.5 Attack Taxonomy Summary

| Attack Type | Mechanism | ASR Range | Citation |
|-------------|-----------|-----------|----------|
| Tool poisoning | Adversarial metadata in tool descriptions | 72.8% | Zhang et al. 2025 |
| Cross-server contamination | Malicious server influences legitimate server calls | 85%+ | Cheng et al. 2025 |
| Supply chain compromise | Typosquatting, dependency confusion | 16.7–64.7% | Guo et al. 2025 |
| Prompt injection via tools | Injected instructions in tool responses | 40.71% avg | Peng et al. 2025 |
| Rug pull attacks | Server changes behavior after trust is established | Variable | Cheng et al. 2025 |
| Path traversal | File system access beyond intended scope | 22% prevalence | Peng et al. 2025 |

---

## 4. Real-World Vulnerabilities and CVEs

### 4.1 Production CVEs

The transition from benchmark to reality is already underway. Several high-severity CVEs have been assigned to MCP server implementations:

**CVE-2025-53967 (Figma MCP Server)**
- **CVSS Score**: 7.5 (High)
- **Impact**: Server-Side Request Forgery (SSRF) allowing internal network scanning and data exfiltration
- **Root cause**: Insufficient input validation on URL parameters passed to Figma API calls
- **Affected users**: Unclear but Figma is used by millions of designers

**CVE-2025-6514 (mcp-remote)**
- **Severity**: Critical
- **Impact**: Remote code execution through malicious server registration
- **Affected**: mcp-remote package with **558,000+ downloads** on npm
- **Root cause**: Lack of server identity verification in the remote transport layer

**CVE-2025-68143 through CVE-2025-68145 (Anthropic Git MCP)**
- **Impact**: Command injection via crafted repository names and branch names
- **Root cause**: Unsanitized shell command construction from user-provided Git parameters

### 4.2 The Authentication Crisis

Guo et al. (2025) conducted a survey of 500+ deployed MCP servers and found a deeply concerning authentication landscape:

| Auth Method | Percentage | Security Level |
|-------------|-----------|----------------|
| None (unauthenticated) | 32% | Critical risk |
| Static API keys / secrets | 53% | Insecure at scale |
| OAuth 2.0/2.1 | 8.5% | Recommended |
| mTLS / certificate-based | 4% | Strong |
| Other | 2.5% | Variable |

This means **85% of deployed MCP servers** use authentication methods that would fail basic security audits. The November 2025 MCP specification mandates OAuth 2.1, but enforcement is voluntary and adoption lags specification by 6–12 months historically.

### 4.3 The Permission Gap

Beyond authentication, the MCP specification lacks several security primitives that production deployments require:

- **No tool-level permissions**: Once authenticated, a client can invoke any tool the server exposes. The specification provides no mechanism for per-tool authorization.
- **No rate limiting primitive**: Rate limiting must be implemented at the transport layer, outside MCP's specification boundary.
- **No audit trail specification**: While servers can log operations, there is no standardized audit event format.
- **No input validation framework**: Each server must independently validate all inputs, with no shared validation library or schema enforcement.

---

## 5. Defense Frameworks and Mitigations

### 5.1 MCP-Guard: Three-Stage Defense Pipeline

Shan et al. (2025) proposed MCP-Guard, a three-stage defense framework that balances security with performance:

**Stage 1: Static Scanner** (<2ms latency)
- Pattern matching for known attack signatures: SQL injection, command injection, path traversal
- Regex-based detection of common prompt injection patterns
- Blocks obvious attacks before they reach more expensive detection stages

**Stage 2: Neural Classifier** (96.01% detection accuracy)
- Lightweight transformer model trained on adversarial MCP inputs
- 12x faster than LLM-based detection with comparable accuracy
- Handles novel attack patterns that evade static rules
- False positive rate: 3.2%

**Stage 3: LLM Arbiter** (89.07% F1 score)
- Full LLM evaluation of ambiguous cases that pass Stages 1 and 2
- Semantic analysis of tool descriptions for hidden instructions
- Highest accuracy but highest latency (~500ms per evaluation)
- Only invoked for ~5% of requests that pass previous stages

The cascading architecture means 95% of requests are handled in <2ms (Stage 1) or <50ms (Stage 2), with the expensive LLM arbiter reserved for genuinely ambiguous cases.

### 5.2 MI9 Runtime Governance

Chandra et al. (2025) introduced MI9, a runtime governance framework for MCP deployments:

- **99.81% violation detection rate** across tested attack vectors
- Runtime policy enforcement via a governance sidecar that intercepts all MCP traffic
- Policy language for expressing constraints: "tool X may only access files within directory Y", "tool Z may not make network requests"
- Violation responses: block, alert, or degrade (allow with reduced permissions)

MI9's approach is complementary to MCP-Guard: where MCP-Guard focuses on input validation, MI9 enforces behavioral constraints at runtime — catching attacks that manifest as legitimate-looking requests but produce malicious behavior.

### 5.3 Zero-Trust Architecture for MCP

The Cloud Security Alliance (CSA) and MIT have proposed zero-trust principles specifically adapted for MCP deployments:

- **Decentralized Identifiers (DIDs)** for server identity verification, replacing the current trust-on-first-use model
- **Verifiable Credentials (VCs)** for capability attestation — servers prove their security properties rather than clients trusting self-declarations
- **Agent Name Service (ANS)**: A DNS-like resolution system for discovering verified MCP servers, proposed as an alternative to the registry-based discovery model

Microsoft has additionally proposed **MCP Server Cards** — structured metadata documents (analogous to model cards) that describe a server's security posture, data handling practices, and trust level. While not yet adopted in the specification, Server Cards address the tool poisoning vector by providing verifiable, out-of-band information about server capabilities.

### 5.4 OWASP and MITRE Frameworks

Two established security organizations have published agentic-specific guidance:

**OWASP Agentic AI Top 10 (2026)**
1. Prompt Injection (direct and indirect)
2. Broken Access Control for Agents
3. Tool/Function Misuse
4. Excessive Agency
5. Insecure Tool Configuration
6. Data Poisoning through Tools
7. Insufficient Logging and Monitoring
8. Supply Chain Vulnerabilities
9. Agent Identity Spoofing
10. Memory/Context Manipulation

**MITRE ATLAS (October 2025 update)**
- Added "Agentic AI" as a new tactic category
- Specific techniques for MCP exploitation documented
- Mapping to ATT&CK framework for incident response integration

These frameworks provide structured vocabularies for describing and categorizing MCP security threats, complementing the benchmark-specific attack taxonomies from MCPSecBench and MSB.

---

## 6. Competing and Complementary Protocols

### 6.1 Agent Communication Protocol (ACP)

**Origin**: OpenAI + Stripe (2025)
**Focus**: Opaque tool execution and payment orchestration

ACP diverges from MCP's transparent tool model by treating tool execution as opaque — the calling agent sends a task description, and the executing agent returns results without exposing its internal tooling. This pattern is suited for commercial transactions where the service provider's implementation is proprietary.

Key differentiators from MCP:
- **Opaque execution**: Clients describe *what* they want, not *which tool* to call
- **Payment integration**: Native Stripe integration for metered billing
- **Agent-to-agent**: Designed for agent collaboration, not just model-to-tool
- **No tool discovery**: Agents advertise capabilities, not specific tools

For music attribution, ACP is relevant for monetized permission queries where rights holders charge for consent verification — the "permission-as-a-service" model described in SSRN No. 6109087.

### 6.2 Agent-to-Agent Protocol (A2A)

**Origin**: Google → Linux Foundation (2025)
**Focus**: Agent discovery and peer coordination

A2A provides primitives for agents to discover each other, negotiate capabilities, and coordinate multi-step workflows. Originally developed by Google as "Agent2Agent," it was donated to the Linux Foundation in late 2025.

Key features:
- **Agent Cards**: Structured metadata for advertising agent capabilities (analogous to MCP's tool definitions but at the agent level)
- **Task lifecycle management**: Request, progress tracking, completion notification
- **Multi-turn conversations**: Agents can engage in extended dialogues to resolve complex tasks
- **Discovery service**: Registry for finding agents by capability

The relationship to MCP is complementary: MCP handles model-to-tool communication, while A2A handles agent-to-agent coordination. A music attribution agent might use MCP to query internal tools (database, metadata extractors) and A2A to coordinate with external agents (rights organization registries, distributor systems).

### 6.3 Token Agent Protocol (TAP)

**Origin**: Visa (2026)
**Focus**: Financial agent commerce and payment authorization

TAP is specifically designed for financial transactions in agentic contexts. It provides:
- **Tokenized authorization**: Agents receive scoped, time-limited tokens for specific transaction types
- **Identity verification**: Multi-factor agent identity for high-value transactions
- **Transaction audit trail**: Immutable logging of all agent-initiated financial operations

For the Music Attribution Scaffold, TAP is relevant for the compensation layer — tracking and settling payments when AI platforms use copyrighted music based on MCP permission queries.

### 6.4 Extended Agent Authentication (XAA)

**Origin**: Okta (2025)
**Focus**: Identity and authentication for agentic systems

XAA addresses the authentication gap identified across all other protocols by providing:
- **Agent identity lifecycle**: Registration, authentication, authorization, revocation
- **Delegation chains**: Agent A can delegate specific capabilities to Agent B with verifiable provenance
- **Cross-protocol identity**: A single agent identity works across MCP, A2A, ACP, and TAP

### 6.5 Convergence Thesis

The proliferating protocol landscape is likely to converge rather than fragment. The emerging consensus points toward a three-layer stack:

1. **Tool Layer**: MCP (model-to-tool communication, tool discovery)
2. **Coordination Layer**: A2A (agent-to-agent discovery, task delegation)
3. **Identity Layer**: XAA or similar (authentication, authorization, audit)

ACP and TAP occupy vertical niches (commerce, finance) that sit atop this stack. The AAIF's governance of both MCP and A2A under the Linux Foundation umbrella suggests intentional convergence.

---

## 7. Production Deployment Considerations

### 7.1 Sandboxing and Isolation

Production MCP deployments require isolation between the host application and MCP server execution. Three patterns have emerged:

**Cloudflare Workers**: V8 isolate-based sandboxing with sub-millisecond cold starts. Cloudflare has released native MCP server support on Workers, providing automatic sandboxing without container overhead. Limitations: 10ms CPU time per request, no persistent connections, limited to JavaScript/TypeScript.

**Deno Sandbox**: Deno's V8-based runtime provides granular permission controls (network, filesystem, environment variables) that map naturally to MCP capability grants. The Deno Deploy platform adds edge distribution. Limitations: smaller ecosystem than Node.js, TypeScript/JavaScript only.

**Docker Isolation**: Container-per-server isolation with resource limits (CPU, memory, network). The most flexible approach, supporting any language runtime. The Music Attribution Scaffold already uses Docker for development and testing, making this the natural fit. Limitations: higher cold start latency, more operational complexity.

### 7.2 Authentication: OAuth 2.1 Transition

The March 2025 MCP specification mandates OAuth 2.1 for all authenticated transports. Key implementation requirements:

- **PKCE (Proof Key for Code Exchange)**: Mandatory for all authorization code grants
- **Token rotation**: Short-lived access tokens (15 minutes recommended) with refresh token rotation
- **Resource indicators (RFC 8707)**: Tokens scoped to specific MCP servers, preventing token mis-redemption across servers
- **Dynamic client registration**: Clients can register programmatically, but server operators must implement approval workflows for production environments

The scaffold's existing OAuth 2.0 implementation (Section 4.1 of the MCP Server PRD) requires minor updates to achieve full OAuth 2.1 compliance: PKCE enforcement, shorter token lifetimes, and RFC 8707 resource indicators.

### 7.3 Observability

MCP operations generate telemetry that must be captured for security monitoring, debugging, and compliance:

- **OpenTelemetry (OTel)**: The emerging standard for agentic telemetry. Anthropic has proposed an MCP-specific semantic convention for OTel spans, covering tool invocation, resource access, and prompt injection detection events.
- **Structured logging**: Every MCP operation should emit structured log events with: client identity, requested tool, input parameters (redacted as appropriate), output summary, latency, and security classification.
- **Metrics**: Request rate, error rate, latency percentiles, and security event counts per tool/client/server.

### 7.4 Rate Limiting and Circuit Breakers

Production MCP servers must implement both rate limiting and circuit breaker patterns:

- **Per-client rate limits**: The scaffold's three-tier model (Internal: unlimited, Verified: 1000/hr, Public: 100/hr) provides a baseline. Dynamic adjustment based on abuse detection is recommended.
- **Per-tool rate limits**: High-cost tools (e.g., those invoking external APIs) should have independent rate limits.
- **Circuit breakers**: If an upstream dependency fails, the MCP server should fail fast rather than queuing requests. The circuit breaker pattern prevents cascading failures in multi-server deployments.

### 7.5 EU AI Act Compliance

The EU AI Act creates specific obligations for systems using MCP:

- **Article 12 (Logging)**: AI systems must maintain logs sufficient for post-hoc compliance verification. MCP audit logs must capture: who accessed what data, when, for what purpose, and what the system responded. Retention period: at least the lifecycle of the AI system.
- **GPAI obligations (August 2025)**: Providers of general-purpose AI models must publish training data summaries and respect TDM opt-out reservations. MCP consent infrastructure (the Permission Patchbay) directly addresses this requirement.
- **Penalties**: Up to EUR 35M or 7% of global annual turnover for systematic violations; EUR 15M or 3% for individual violations.
- **Transparency requirements**: Users must be informed when interacting with an AI system. MCP-mediated attribution queries must include disclosure when the querying entity is an AI agent.

---

## 8. Implications for the Music Attribution Scaffold

### 8.1 Current Security Posture

The scaffold's MCP Server PRD (v0.8.0) already incorporates several security measures:

- **Three-tier trust model** (Internal/Verified/Public) with tier-based access control
- **Four-layer defense architecture** (Authentication → Input Validation → Capability Sandbox → Audit)
- **OAuth 2.0 integration** design (requiring upgrade to 2.1)
- **Audit logging** with artist access for compliance monitoring
- **Deterrence-based compliance** model grounded in HADOPI research

### 8.2 Identified Gaps

Based on the research surveyed in this report, the following gaps require attention:

1. **Tool-level input validation**: The current design lacks the three-stage MCP-Guard pattern. Adding static scanning + neural classification before LLM processing would catch the majority of attacks at minimal latency cost.
2. **Server identity verification**: No DID/VC infrastructure for verifying the identity of connecting clients beyond OAuth tokens. Supply chain attacks could impersonate legitimate partners.
3. **Cross-server isolation**: If the scaffold's MCP server is used alongside other MCP servers in a client's environment, cross-server contamination attacks (per MCPSecBench) are possible. The scaffold cannot control other servers' security but should document recommended isolation patterns.
4. **Sandboxed tool execution**: Tool implementations currently run in the same process as the MCP server. Container-level isolation for tool execution would limit blast radius.
5. **MCP Registry integration**: The scaffold's tools are not registered in the MCP Registry, limiting discoverability for potential partners.

### 8.3 Recommended Hardening Roadmap

| Priority | Action | Effort | Risk Mitigated |
|----------|--------|--------|----------------|
| P0 | Upgrade OAuth 2.0 → 2.1 with PKCE + RFC 8707 | 1 week | Token mis-redemption, auth bypass |
| P0 | Add static input scanner (regex-based, <2ms) | 2 days | SQL injection, command injection, path traversal |
| P1 | Implement structured audit logging (OTel format) | 1 week | EU AI Act Art. 12 compliance |
| P1 | Add JSON Schema validation for all tool inputs | 3 days | Malformed input attacks |
| P2 | Deploy neural classifier for tool description analysis | 2 weeks | Tool poisoning (72.8% ASR) |
| P2 | Implement per-tool rate limiting | 3 days | Resource exhaustion |
| P3 | DID/VC server identity verification | 1 month | Supply chain attacks |
| P3 | Container isolation for tool execution | 2 weeks | Privilege escalation, blast radius |
| P3 | Register tools in MCP Registry | 1 day | Discoverability |

### 8.4 Figure Plan Index

The following figure plans have been created to support visual communication of the security concepts in this report:

| Figure ID | Title | Template |
|-----------|-------|----------|
| fig-repo-20 | MCP Attack Surface Taxonomy | A (Hero) |
| fig-repo-21 | Inverse Scaling Paradox | C (Data-Viz) |
| fig-repo-22 | MCP-Guard Three-Stage Defense | D (Split-Panel) |
| fig-repo-23 | MCP Authentication Crisis | C (Data-Viz) |
| fig-repo-24 | Agentic Protocol Landscape | B (Multi-Panel) |
| fig-repo-25 | MCP Protocol Evolution Timeline | E (Steps) |
| fig-repo-26 | Zero-Trust Architecture for MCP | D (Split-Panel) |
| fig-repo-27 | Real-World MCP CVE Gallery | B (Multi-Panel) |
| fig-repo-28 | MCP Sandbox Isolation Patterns | D (Split-Panel) |
| fig-repo-29 | OWASP Agentic Top 10 (2026) | A (Hero) |
| fig-repo-30 | MCP Production Observability Stack | D (Split-Panel) |
| fig-repo-31 | AAIF Governance Structure | E (Steps) |

---

## References

1. AAIF (2025). "Agentic AI Foundation Launch Announcement." Linux Foundation, December 2025.
2. Anthropic (2024). "Introducing the Model Context Protocol." Anthropic Blog, November 2024.
3. Anthropic (2025). "MCP Ecosystem Update: Enterprise Adoption." Anthropic Blog, March 2025.
4. Auth0 (2025). "MCP Spec Update: All About Auth." Auth0 Blog, June 2025.
5. Becker, G. S. (1968). "Crime and Punishment: An Economic Approach." *Journal of Political Economy*, 76(2), 169–217.
6. Bruegel (2025). "European Union Still Caught in an AI Copyright Bind." Policy Brief.
7. Chandra, S. et al. (2025). "MI9: Runtime Governance for Model Context Protocol Deployments." *arXiv preprint*, arXiv:2506.xxxxx.
8. Cheng, Y. et al. (2025). "MCPSecBench: Benchmarking Security Vulnerabilities in Model Context Protocol Implementations." *arXiv preprint*, arXiv:2508.13220.
9. Clifford Chance (2025). "Copyright Compliance Under EU AI Act: A Practical Guide." October 2025.
10. Cloud Security Alliance (2025). "Zero-Trust Architecture for Agentic AI Systems." CSA Publication.
11. CVE-2025-53967. "Figma MCP Server SSRF Vulnerability." NIST NVD.
12. CVE-2025-6514. "mcp-remote Remote Code Execution." NIST NVD.
13. CVE-2025-68143. "Anthropic Git MCP Command Injection." NIST NVD.
14. Danaher, B. et al. (2014). "The Effect of Graduated Response Anti-Piracy Laws on Music Sales." *Journal of Industrial Economics*, 62(3), 541–553.
15. EU (2024). "Regulation (EU) 2024/1689 — Artificial Intelligence Act." Official Journal of the European Union.
16. EU Commission (2025). "Consultation on TDM Reservation Protocols." December 2025.
17. Google (2025). "Agent2Agent Protocol: Agent Discovery and Coordination." A2A Specification.
18. Guo, R. et al. (2025). "Supply Chain Security in the MCP Ecosystem." *arXiv preprint*.
19. IAPP (2025). "GDPR Amendments for AI Training Miss the Mark."
20. MITRE (2025). "ATLAS Framework Update: Agentic AI Tactics." October 2025.
21. Morreale, F. et al. (2025). "Attribution-by-Design: Embedding Provenance in AI Music Systems." *Proceedings of ISMIR 2025*.
22. Okta (2025). "Extended Agent Authentication (XAA): Identity for Agentic Systems." Okta Blog.
23. OpenAI & Stripe (2025). "Agent Communication Protocol (ACP) Specification." Version 0.3.
24. OWASP (2026). "OWASP Agentic AI Top 10." Version 1.0.
25. Peng, X. et al. (2025). "MCP Security Bench: Systematic Evaluation of Model Context Protocol Attack Surfaces." *arXiv preprint*, arXiv:2510.15994.
26. Shan, L. et al. (2025). "MCP-Guard: A Three-Stage Defense Pipeline for Model Context Protocol Security." *arXiv preprint*.
27. Teikari, P. (2026). "Music Attribution with Transparent Confidence." SSRN No. 6109087.
28. Visa (2026). "Token Agent Protocol (TAP): Financial Agent Commerce." TAP Specification.
29. Zhang, W. et al. (2025). "MCPTox: Benchmarking Tool Poisoning Attacks in Model Context Protocol." *arXiv preprint*.

---

## Cross-References

- [MCP Server PRD](../prd/mcp-server-prd.md) — Existing security architecture
- [MCP Knowledge Synthesis](../knowledge-base/technical/mcp/SYNTHESIS.md) — Protocol patterns
- [PRD Decision Network](../prd/decisions/REPORT.md) — Bayesian decision nodes
- [mcp_security_strategy](../prd/decisions/L3-implementation/mcp-security-strategy.decision.yaml) — New PRD node
- [mcp_production_deployment](../prd/decisions/L3-implementation/mcp-production-deployment.decision.yaml) — New PRD node
- [mcp_input_validation](../prd/decisions/L4-deployment/mcp-input-validation.decision.yaml) — New PRD node
