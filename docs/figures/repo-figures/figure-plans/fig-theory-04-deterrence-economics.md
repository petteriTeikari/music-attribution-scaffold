# fig-theory-04: Deterrence Economics

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-04 |
| **Title** | Deterrence Economics -- Why Deterrence Works Even When Detection Is Imperfect |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 (academic terms, economic reasoning) |
| **Location** | docs/theory/oracle-problem.md, docs/theory/deterrence.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure explains the deterrence economics formula and why a system does not need perfect detection to be effective. It answers: "If we can't always detect AI-generated music stealing from creators, why build attribution infrastructure at all?"

The key message is: "Deterrence works like tax audits -- you don't need to audit everyone, just make the expected penalty exceed the expected gain: p x d x F >= g."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  DETERRENCE ECONOMICS                                          |
|  ■ Why Imperfect Detection Still Works                         |
+---------------------------------------------------------------+
|                                                                |
|  THE FORMULA                                                   |
|  ───────────                                                   |
|                                                                |
|       p   x   d   x   F   >=   g                              |
|       │       │       │         │                              |
|       │       │       │         └── Gain from infringement     |
|       │       │       └──────── Fine / penalty amount          |
|       │       └──────────────── Detection probability          |
|       └──────────────────────── Audit probability              |
|                                                                |
+---------------------------------------------------------------+
|                                                                |
|  TAX AUDIT ANALOGY                                             |
|  ─────────────────                                             |
|                                                                |
|  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐         |
|  │  100 FILERS │   │  3 AUDITED  │   │  PENALTY    │         |
|  │  ┌─┐┌─┐┌─┐ │   │             │   │             │         |
|  │  │ ││ ││ │ │   │  p = 3%     │   │  F = $50K   │         |
|  │  └─┘└─┘└─┘ │   │             │   │             │         |
|  │  ... x 100  │   │  d = 80%    │   │  g = $500   │         |
|  └─────────────┘   └─────────────┘   └─────────────┘         |
|                                                                |
|  Expected penalty:  0.03 x 0.80 x $50,000 = $1,200            |
|  Expected gain:     $500                                       |
|  $1,200 >> $500  ■  DETERRENCE HOLDS                           |
|                                                                |
+---------------------------------------------------------------+
|                                                                |
|  APPLIED TO MUSIC ATTRIBUTION                                  |
|  ────────────────────────────                                  |
|                                                                |
|  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      |
|  │  Audit   │  │ Detect   │  │ Penalty  │  │  Gain    │      |
|  │  Prob.   │  │  Prob.   │  │  Scale   │  │ from     │      |
|  │──────────│  │──────────│  │──────────│  │ evasion  │      |
|  │ Random   │  │ Content  │  │ Legal +  │  │──────────│      |
|  │ sampling │  │ ID match │  │ platform │  │ Unpaid   │      |
|  │ + flag   │  │ + meta   │  │ delistng │  │ royalty  │      |
|  └──────────┘  └──────────┘  └──────────┘  └──────────┘      |
|                                                                |
|  ■ Key insight: p does not need to be 100%.                    |
|    Even 5% audit rate deters if F is large enough.             |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "DETERRENCE ECONOMICS" with coral accent square |
| Subtitle | `label_editorial` | "Why Imperfect Detection Still Works" |
| Formula display | `data_mono` | "p x d x F >= g" in monospace with variable annotations |
| Variable annotations | `label_editorial` | Four labeled arrows from formula variables to plain-English definitions |
| Tax audit section | `callout_box` | Three-panel illustration: 100 filers, 3 audited, penalty amount |
| Filer icons | `stakeholder_artist` | Small person icons representing tax filers |
| Probability values | `data_mono` | p=3%, d=80%, F=$50K, g=$500 in monospace |
| Expected penalty calculation | `data_mono` | "0.03 x 0.80 x $50,000 = $1,200" |
| Deterrence holds badge | `confidence_high` | Green-coded result: "$1,200 >> $500" |
| Music application section | `solution_component` | Four boxes mapping formula to music attribution context |
| Audit prob box | `processing_stage` | "Random sampling + flag" -- how audits happen |
| Detect prob box | `processing_stage` | "Content ID match + meta" -- detection mechanisms |
| Penalty scale box | `processing_stage` | "Legal + platform delisting" -- consequences |
| Gain from evasion box | `problem_statement` | "Unpaid royalty" -- what infringers gain |
| Key insight callout | `callout_box` | "p does not need to be 100%" -- the core takeaway |

## Anti-Hallucination Rules

1. The formula is p x d x F >= g -- do NOT alter the formula or add additional variables.
2. The tax audit analogy uses 3% audit rate -- this is an illustrative example, not an exact regulatory figure.
3. Dollar amounts ($50K penalty, $500 gain) are ILLUSTRATIVE -- do NOT claim these are real enforcement figures.
4. Do NOT reference specific legal cases, court rulings, or copyright legislation by name.
5. Do NOT claim the system achieves a specific detection rate -- the point is that ANY rate can deter if penalties are large enough.
6. The deterrence model is ECONOMIC, not technical -- do NOT describe detection algorithms.
7. "Platform delisting" is one possible penalty -- do NOT list specific platforms.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Theory visualization: deterrence economics formula p times d times F greater than or equal to g with tax audit analogy showing that even a 3 percent audit rate deters infringement when penalties are large -- applied to music attribution where imperfect detection still protects music credits through transparent confidence scoring and economic incentives rather than perfect surveillance.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Theory visualization: deterrence economics formula p times d times F greater than or equal to g with tax audit analogy showing that even a 3 percent audit rate deters infringement when penalties are large -- applied to music attribution where imperfect detection still protects music credits through transparent confidence scoring and economic incentives rather than perfect surveillance.](docs/figures/repo-figures/assets/fig-theory-04-deterrence-economics.jpg)

*Figure 4. Deterrence economics applied to music attribution: the system does not need perfect detection to be effective, just as tax audits deter fraud at a 3% audit rate -- the expected penalty (p x d x F) need only exceed the expected gain (g) from infringement.*

### From this figure plan (relative)

![Theory visualization: deterrence economics formula p times d times F greater than or equal to g with tax audit analogy showing that even a 3 percent audit rate deters infringement when penalties are large -- applied to music attribution where imperfect detection still protects music credits through transparent confidence scoring and economic incentives rather than perfect surveillance.](../assets/fig-theory-04-deterrence-economics.jpg)
