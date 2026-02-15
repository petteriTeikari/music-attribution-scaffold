# fig-choice-17: Why Pulumi over Terraform?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-17 |
| **Title** | Why Pulumi over Terraform? Python-Native IaC with MCP Integration |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/prd/decisions/L4-deployment/iac-tooling.decision.yaml |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains the IaC tooling decision updated in PRD v2.1.0, where Pulumi was promoted to `recommended` status over Terraform. Three factors drove the change: (1) Pulumi uses real Python -- same language as the scaffold backend, (2) Pulumi has an official MCP server enabling Claude to manage infrastructure conversationally, (3) Terraform's BSL license after IBM's $6.4B HashiCorp acquisition creates vendor risk. Shows comparison including OpenTofu as the open-source Terraform fork.

The key message is: "Pulumi lets you define infrastructure in the same Python you write attribution code in, with an MCP server that lets Claude manage deployments -- while Terraform's BSL license creates vendor lock-in risk after IBM's acquisition."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WHY PULUMI OVER TERRAFORM?                                    |
|  ■ Python-Native IaC with MCP Integration                      |
+---------------------------------------------------------------+
|                                                                |
|  ┌──────────────────────────────────────────────────────┐     |
|  │  PULUMI                                               │     |
|  │  ■ RECOMMENDED (P=0.25)                               │     |
|  │                                                       │     |
|  │  LANGUAGE        Python (same as scaffold backend)    │     |
|  │  LICENSE         Apache 2.0 (open source)             │     |
|  │  MCP SERVER      Official — Claude manages infra      │     |
|  │  HETZNER         Official provider v1.32.0            │     |
|  │  POLICY          CrossGuard (Python policy-as-code)   │     |
|  │  STATE           Pulumi Cloud or self-hosted backend  │     |
|  │  TESTING         pytest integration (same test suite) │     |
|  └──────────────────────────────────────────────────────┘     |
|                                                                |
|  vs ALTERNATIVES                                               |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │ Terraform    │ │ OpenTofu     │ │ None (PaaS)  │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ HCL (custom  │ │ HCL (fork)   │ │ No IaC       │          |
|  │ language)    │ │ MPL-2.0      │ │              │          |
|  │ BSL license  │ │ (open src)   │ │ Platform     │          |
|  │ (IBM acq.)   │ │              │ │ manages all  │          |
|  │ P=0.15       │ │ P=0.10       │ │ P=0.25       │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ Risk: BSL    │ │ Pro: Open    │ │ Pro: Zero    │          |
|  │ restricts    │ │ Con: Smaller │ │ ops burden   │          |
|  │ competing    │ │ ecosystem    │ │ Con: Vendor  │          |
|  │ services     │ │              │ │ lock-in      │          |
|  └──────────────┘ └──────────────┘ └──────────────┘          |
|                                                                |
|  THREE REASONS TO CHOOSE PULUMI                                |
|  ──────────────────────────────                                |
|  ■ Same language: Python infra code in same repo               |
|  ■ MCP server: Claude deploys and manages infra                |
|  ■ License safety: Apache 2.0, no IBM BSL risk                 |
|                                                                |
+---------------------------------------------------------------+
|  Volatility: shifting — IBM acquisition changed the landscape  |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WHY PULUMI OVER TERRAFORM?" with coral accent square |
| Pulumi recommendation | `selected_option` | Language, license, MCP, Hetzner, policy, state, testing |
| Terraform alternative | `deferred_option` | HCL, BSL license, IBM acquisition risk |
| OpenTofu alternative | `deferred_option` | Open-source Terraform fork, MPL-2.0, smaller ecosystem |
| None (PaaS) alternative | `deferred_option` | No IaC, platform manages infrastructure |
| Three reasons summary | `feature_list` | Same language, MCP server, license safety |
| Volatility footer | `callout_bar` | Shifting -- IBM acquisition changed the landscape |

## Anti-Hallucination Rules

1. Pulumi is `recommended` status in PRD v2.1.0 with P=0.25 -- promoted from `viable` P=0.20.
2. Terraform was demoted to P=0.15 due to BSL (Business Source License) after IBM's $6.4B acquisition of HashiCorp in 2024.
3. Pulumi supports real programming languages: Python, TypeScript, Go, C#, Java. NOT a custom DSL.
4. Pulumi has an OFFICIAL MCP server (`@pulumi/mcp-server`) that enables LLMs to manage infrastructure.
5. Pulumi has an official Hetzner provider (v1.32.0 as of Feb 2026) -- NOT a community hack.
6. OpenTofu is the Linux Foundation fork of Terraform using MPL-2.0 license. It maintains HCL compatibility.
7. IaC tooling volatility changed from `stable` to `shifting` in v2.1.0 due to the IBM acquisition.
8. "None (PaaS)" option (P=0.25) is for teams using Render/Railway where the platform handles infrastructure.
9. CrossGuard is Pulumi's policy-as-code framework -- policies are written in Python, same as infrastructure.
10. Background must be warm cream (#f6f3e6).

## Alt Text

Architecture decision: Pulumi recommended over Terraform for music attribution scaffold infrastructure-as-code, showing Python-native language alignment with the scaffold backend, official MCP server enabling Claude to manage deployments, and Apache 2.0 license versus Terraform's BSL after IBM's HashiCorp acquisition -- compared against OpenTofu fork and no-IaC PaaS options in the open-source attribution platform.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Architecture decision: Pulumi recommended over Terraform for music attribution scaffold infrastructure-as-code, showing Python-native language alignment with the scaffold backend, official MCP server enabling Claude to manage deployments, and Apache 2.0 license versus Terraform's BSL after IBM's HashiCorp acquisition -- compared against OpenTofu fork and no-IaC PaaS options in the open-source attribution platform.](docs/figures/repo-figures/assets/fig-choice-17-pulumi-over-terraform.jpg)

*Pulumi is recommended over Terraform for the music attribution scaffold: Python-native IaC (same language as the backend), an official MCP server for Claude-managed deployments, and Apache 2.0 licensing -- while Terraform's BSL after IBM's $6.4B HashiCorp acquisition creates vendor risk (PRD v2.1.0 node: iac_tooling, volatility: shifting).*

### From this figure plan (relative)

![Architecture decision: Pulumi recommended over Terraform for music attribution scaffold infrastructure-as-code, showing Python-native language alignment with the scaffold backend, official MCP server enabling Claude to manage deployments, and Apache 2.0 license versus Terraform's BSL after IBM's HashiCorp acquisition -- compared against OpenTofu fork and no-IaC PaaS options in the open-source attribution platform.](../assets/fig-choice-17-pulumi-over-terraform.jpg)
