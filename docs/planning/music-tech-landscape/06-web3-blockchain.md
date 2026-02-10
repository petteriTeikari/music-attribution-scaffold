# Web3 & Blockchain Approaches to Music Attribution

> **Parent**: [README.md](README.md) > Web3 & Blockchain
> **Updated**: 2026-02-10

---

## Overview

Web3 approaches to music attribution promise transparent, immutable, and automated royalty distribution via smart contracts. The core thesis: if attribution decisions and payment flows are recorded on-chain, they become auditable and trustless.

Reality check: Web3 adoption in music remains niche despite significant investment. The technical overhead (gas fees, wallet UX, bridging) often outweighs the transparency gains for most participants. However, specific implementations are worth studying for architectural patterns.

---

## Mubert Protocol

### Company Profile

| Attribute | Details |
|-----------|---------|
| **HQ** | Originally Russia; pivoted to global/Web3 |
| **Founded** | 2017 (original product); Protocol announced 2024 |
| **Scale** | 100M+ tracks generated |
| **Music catalog** | 1M+ human-made stems, loops, and samples |
| **Integrations** | Canva, Restream, Instories |
| **Blockchain** | Polkadot ecosystem (Web3 Foundation grant) |

### Technology Architecture

**Mubert Protocol** is built as a Polkadot rollup (appchain) specifically for music creator economy:

```
Creator uploads stem/sample
        ↓
Audio fingerprinted (unique hash)
        ↓
Registered on-chain (Polkadot rollup)
        ↓
AI generation uses stem as building block
        ↓
Smart contract tracks which stems used
        ↓
Revenue distributed proportionally (on-chain)
```

### Key Features

1. **On-chain fingerprinting**: Every audio element is fingerprinted and registered as a unique on-chain asset
2. **Tokenized datasets**: Training data contributions are tokenized, enabling fractional ownership and automated revenue sharing
3. **Smart contract royalties**: Revenue from AI-generated tracks automatically split among contributing creators
4. **Talisman partnership**: Data ownership wallet integration via Polkadot ecosystem

### Polkadot Integration Details

- **Rollup type**: Application-specific chain (appchain) on Polkadot
- **Consensus**: Inherited from Polkadot relay chain
- **Cross-chain**: Polkadot's XCM protocol enables interoperability with other parachains
- **Web3 Foundation grant**: Received grant for building the creator economy infrastructure

### Business Model

- Creators earn from AI generation using their stems
- API customers (Canva, etc.) pay for generation
- Revenue split tracked and executed on-chain
- B2B API for integration into content creation platforms

### Assessment

**Strengths**:
- Genuine transparency — all attribution decisions auditable on-chain
- Automatic, trustless payment execution
- Large existing catalog of human-created building blocks
- Strong B2B distribution (Canva integration is significant)

**Weaknesses**:
- Web3 UX friction for mainstream musicians
- Polkadot ecosystem is smaller than Ethereum
- "Stem-based" generation is architecturally different from full-song generation (Suno/Udio)
- On-chain overhead for every attribution decision may not scale cost-effectively
- Creator adoption of crypto wallets remains a barrier

**Relevance to scaffold**: Mubert's on-chain model is interesting as a reference architecture but not directly applicable to our scaffold's approach. Our MCP-based permission system achieves similar transparency goals without blockchain overhead. However, the fingerprint → on-chain registration → smart contract royalty pattern could inspire our confidence scoring pipeline design.

---

## Other Web3 Music Platforms

### Audius

| Attribute | Details |
|-----------|---------|
| **Type** | Decentralized streaming platform |
| **Blockchain** | Solana |
| **Token** | $AUDIO |
| **Users** | 8M+ monthly |

**Approach**: Decentralized music streaming where artists control distribution. Not directly attribution-focused, but the decentralized identity and content registration patterns are relevant.

**Relevance**: Audius's content ID system on Solana demonstrates how blockchain can handle music metadata at scale. Their artist identity verification could complement our A3 assurance level.

---

### Royal

| Attribute | Details |
|-----------|---------|
| **Founded** | 2021 |
| **Founders** | 3LAU, JD Ross |
| **Funding** | $75M+ (a16z led Series A) |
| **Type** | Music royalty marketplace |

**Approach**: Fractional ownership of music royalties via NFTs. Fans buy ownership shares of songs and earn streaming royalties.

**Relevance**: Royal's approach of tokenizing royalty streams is conceptually adjacent to attribution-based compensation. If we can determine "Song X influenced AI output Y by Z%", tokenized royalty shares could distribute that Z% among contributors.

---

### Arpeggi Labs / Arpeggi Studio

| Attribute | Details |
|-----------|---------|
| **Type** | On-chain music creation platform |
| **Blockchain** | Ethereum |

**Approach**: Music creation tools where compositions are registered on-chain. Each creation records the stems and samples used, creating an on-chain provenance trail.

**Relevance**: Most directly relevant Web3 approach to attribution-by-design. Every musical decision is recorded, creating a full provenance graph.

---

## Blockchain-Based Attribution Patterns

### Pattern 1: Content Registration

```
Audio file → Hash computation → On-chain registration
                                    ↓
                              Timestamp proof
                              Creator identity
                              License terms
```

**Applicable to scaffold**: Content registration gives us immutable timestamps for "who uploaded what, when." Could be integrated as an optional A3 assurance mechanism.

### Pattern 2: Influence Tracking

```
Training data (on-chain registered)
        ↓
AI model training (training log → on-chain proof)
        ↓
Generated output → Smart contract computes influence shares
        ↓
Royalty distribution (automatic, on-chain)
```

**Applicable to scaffold**: The influence tracking pattern is architecturally what Musical AI and Sureel do off-chain. The on-chain version adds transparency and auditability but at significant cost and complexity.

### Pattern 3: Permission Registry

```
Creator registers work + license terms on-chain
        ↓
AI company queries permission registry
        ↓
Smart contract validates license compliance
        ↓
Training proceeds (with on-chain audit trail)
```

**Applicable to scaffold**: This is functionally equivalent to our MCP permission patchbay. The on-chain version is more trustless but less practical (smart contract query latency, gas costs).

---

## Assessment: Blockchain vs Traditional for Attribution

| Dimension | Blockchain Approach | Traditional Approach (Our Scaffold) |
|-----------|-------------------|--------------------------------------|
| **Transparency** | Inherent (all on-chain) | Must be designed in (open-source, audit logs) |
| **Trust model** | Trustless (smart contracts) | Trust-but-verify (A0-A3 assurance levels) |
| **Scalability** | Limited by chain throughput | Limited by database/API performance |
| **UX** | Wallet-dependent, complex | Standard web (no crypto knowledge needed) |
| **Cost** | Gas fees per transaction | Standard infrastructure costs |
| **Adoption barrier** | High (crypto literacy required) | Low (standard web patterns) |
| **Immutability** | Guaranteed (blockchain) | Must be ensured (append-only logs, signed records) |
| **Interoperability** | Cross-chain protocols (XCM, IBC) | API standards (MCP, REST, DDEX) |

### Recommendation

For our scaffold, Web3 is not the primary path but should be considered as an **optional assurance layer**:

- **MVP**: Standard PostgreSQL + API approach
- **A3 upgrade path**: Optional blockchain registration for highest-assurance records
- **Pattern borrowing**: Use on-chain pattern concepts (content hashing, immutable logs) without actual blockchain infrastructure
- **Monitor**: Track Mubert Protocol's adoption metrics to gauge if blockchain attribution achieves meaningful scale
