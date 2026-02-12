# fig-topic-12: MLSecOps & Trust Centers

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-topic-12 |
| **Title** | MLSecOps — Why Music Attribution Needs Enterprise Security |
| **Audience** | Technical |
| **Complexity** | L3 (detailed) |
| **Location** | Landing page, Topic Card XII (Governance & Security group) |
| **Priority** | P2 (Medium) |
| **Dimensions** | 1200 x 900px (4:3 aspect ratio) |

## Purpose & Key Message

Music attribution handles uniquely sensitive data: artist PII, voice biometrics, royalty financial data, and consent policies. A generic security pyramid is insufficient — this figure grounds each security layer in specific music attribution threats and shows what each certification actually protects. The trust center is not just an uptime dashboard but a real-time transparency portal showing assurance level distribution, consent query audit trails, and drift detection status. Communicates: "security for music attribution is not generic compliance — each layer protects specific assets (voice biometrics, royalty data, consent policies), and the trust center makes compliance verifiable in real time."

Key concepts:
- **Music-specific threat model**: Adversarial attacks on ER models, training data poisoning, catalog metadata manipulation, voice biometric theft
- **SOC2 Type II**: Operational controls — maps to royalty data handling, access logging
- **ISO 27001**: Information security management — maps to PII protection, voice biometric storage
- **ISO 42001**: AI management system — maps to model governance, bias detection, attribution fairness
- **Trust center**: Real-time public dashboard showing compliance status, not a static certification page

## Visual Concept (ASCII Layout)

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  WHAT WE'RE PROTECTING (and from what)                      │
│  ─────────────────────────────────────                      │
│                                                              │
│  ASSET                  THREAT                 LAYER        │
│  ────────────────────────────────────────────────────       │
│  Voice biometrics       Clone without consent  ISO 27001    │
│  (3-sec clips = identity) (VALL-E attack)     + encryption  │
│                                                              │
│  Royalty financial data  Redirect payments     SOC2 Type II │
│  ($2.5B black box)       via metadata poison   + audit log  │
│                                                              │
│  Consent policies       Forge "allow" response  MCP + PKCE  │
│  (MCP Permission Patchbay) (MITM on consent)  + signatures  │
│                                                              │
│  Attribution models     Adversarial examples   ISO 42001    │
│  (ER + confidence)      degrade match accuracy + monitoring │
│                                                              │
│  Artist PII             Deanonymize from       ISO 27001    │
│  (names, ISNIs, splits) linked metadata        + isolation  │
│                                                              │
│  SECURITY PYRAMID — EACH LAYER HAS A JOB                   │
│  ────────────────────────────────────────                   │
│                                                              │
│           ╱╲  ISO 42001 (AI GOVERNANCE)                     │
│          ╱  ╲ Model fairness audits                         │
│         ╱    ╲ Attribution bias detection                    │
│        ╱──────╲ Drift-triggered retraining gates            │
│       ╱        ╲                                            │
│      ╱ ISO 27001╲ (INFORMATION SECURITY)                    │
│     ╱            ╲ Voice biometric encryption                │
│    ╱──────────────╲ PII access controls                     │
│   ╱                ╲ Multi-tenant data isolation             │
│  ╱  SOC2 TYPE II    ╲ (OPERATIONAL CONTROLS)                │
│ ╱                    ╲ Audit logging of all consent queries  │
│╱──────────────────────╲ Change management for models         │
│ INFRASTRUCTURE          Uptime SLAs, incident response       │
│                                                              │
│  TRUST CENTER (real-time, not a PDF)                        │
│  ───────────────────────────────────                        │
│                                                              │
│  ┌─────────────────────────────────────────────┐           │
│  │                                             │           │
│  │  SYSTEM HEALTH                              │           │
│  │  uptime: 99.97%    incidents (30d): 0       │           │
│  │                                             │           │
│  │  ASSURANCE DISTRIBUTION                     │           │
│  │  A3 ██████████████░░░░░░░░  42%             │           │
│  │  A2 ████████████░░░░░░░░░░  35%             │           │
│  │  A1 ████████░░░░░░░░░░░░░░  18%             │           │
│  │  A0 ██░░░░░░░░░░░░░░░░░░░░   5%            │           │
│  │                                             │           │
│  │  CONSENT QUERIES (24h)                      │           │
│  │  Total: 14,203  Allowed: 8,412  Denied: 5,791│          │
│  │                                             │           │
│  │  DRIFT STATUS: ■ STABLE (no alerts)         │           │
│  │  Last model audit: 2026-02-10               │           │
│  │  Next scheduled: 2026-03-10                 │           │
│  │                                             │           │
│  │  CERTIFICATIONS                             │           │
│  │  SOC2 ■ current  ISO 27001 ■ current       │           │
│  │  ISO 42001 ■ in progress                    │           │
│  │                                             │           │
│  └─────────────────────────────────────────────┘           │
│                                                              │
│  MULTI-TENANT ISOLATION                                     │
│  ──────────────────────                                     │
│  Each artist's data in separate encrypted partition         │
│  ■ Artist A  ■ Artist B  ■ Artist C  (no cross-access)    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|-------------|-------------|
| Asset/threat/layer table | `region_secondary` | Five rows mapping specific music assets to threats to security layers |
| Voice biometric row | `data_accent` | Coral highlight — most sensitive asset |
| Royalty data row | `data_warning` | Orange highlight — $2.5B black box reference |
| Security pyramid | `data_primary` | Teal layered pyramid with music-specific controls at each tier |
| Layer descriptions | `label_editorial` | ALL-CAPS cert names with specific music controls (not generic) |
| Trust center dashboard | `region_secondary` | Navy rectangle with live metrics |
| Assurance distribution bars | `data_gradient` | A3 (teal) through A0 (grey) with percentages |
| Consent query stats | `typography_mono` | Monospace numbers: total, allowed, denied |
| Drift status indicator | `status_allow` | Green "STABLE" or amber/red if active alert |
| Certification badges | `data_primary` | Teal "current" / amber "in progress" |
| Multi-tenant isolation | `data_sources` | Three separate colored blocks with no cross-access |

## Anti-Hallucination Rules

1. **Font names are internal** — do NOT render them as visible labels.
2. **Semantic tags are internal** — do NOT render them.
3. **Pixel sizes and rendering instructions are internal** — do NOT render.
4. Only the following text should appear: "WHAT WE'RE PROTECTING", asset/threat/layer table content, "SECURITY PYRAMID", certification names with music-specific controls, "TRUST CENTER", dashboard metrics (uptime, incidents, assurance distribution percentages, consent query counts, drift status, audit dates, certification status), "MULTI-TENANT ISOLATION", artist partition labels.

## Alt Text

MLSecOps infographic grounding security layers in music attribution specifics. An asset-threat-layer table maps five protected assets to their threats: voice biometrics threatened by cloning attacks (protected by ISO 27001 encryption), royalty financial data threatened by metadata poisoning (protected by SOC2 audit logging), consent policies threatened by MITM on MCP queries (protected by PKCE and signatures), attribution models threatened by adversarial examples (protected by ISO 42001 monitoring), and artist PII threatened by deanonymization (protected by multi-tenant isolation). A security pyramid shows each certification tier with music-specific controls: infrastructure at the base, SOC2 Type II for consent query audit logging and change management, ISO 27001 for voice biometric encryption and PII access controls, and ISO 42001 at the apex for model fairness audits and drift-triggered retraining gates. A trust center dashboard shows real-time metrics: 99.97% uptime, 0 incidents, assurance distribution (A3: 42%, A2: 35%, A1: 18%, A0: 5%), 14,203 consent queries in 24 hours, stable drift status, and certification statuses. Multi-tenant isolation shows each artist's data in separate encrypted partitions with no cross-access.
