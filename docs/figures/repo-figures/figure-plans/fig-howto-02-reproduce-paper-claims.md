# fig-howto-02: How to Reproduce Paper Claims

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-howto-02 |
| **Title** | How to Reproduce Paper Claims |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 (structural mapping) |
| **Location** | README.md, docs/guides/reproducibility.md |
| **Priority** | P0 (Critical) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure bridges the academic paper (Teikari 2026, SSRN No. 6109087) and the running code. A researcher reading the paper should be able to find exactly which code module and test command validates each claim. It answers: "I read a claim in the paper -- how do I verify it in this repo?"

The key message is: "Every substantive claim in the paper maps to a specific code module and a test command you can run. The scaffold is the paper's proof-of-concept, not a separate product."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  HOW TO REPRODUCE PAPER CLAIMS                                 |
|  ■ Paper Section to Code Module to Test Command                |
+---------------------------------------------------------------+
|                                                                |
|  PAPER SECTION          CODE MODULE           TEST COMMAND     |
|  ─────────────          ───────────           ────────────     |
|                                                                |
|  I. Confidence          attribution/          make test        |
|     Scoring             confidence.py   ──>   -k confidence    |
|     (Section 3.2) ──>   attribution/                           |
|                         calibration.py                         |
|  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  |
|                                                                |
|  II. Multi-Source       resolution/           make test        |
|      Resolution         entity_resolver  ──>  -k resolution    |
|      (Section 4.1) ──> .py                                     |
|                                                                |
|  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  |
|                                                                |
|  III. Assurance         schemas/              make test        |
|       Levels A0-A3      attribution.py  ──>   -k assurance     |
|       (Section 5) ──>   schemas/enums.py                       |
|                                                                |
|  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  |
|                                                                |
|  IV. MCP Consent        mcp/server.py         make test        |
|      Infrastructure     api/routes/      ──>  -k mcp           |
|      (Section 6) ──>    permissions.py                         |
|                                                                |
|  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─  |
|                                                                |
|  V. Oracle Problem      (conceptual --        N/A              |
|     (Section 2.3) ──>   no code impl.)  ──>  (design doc)     |
|                                                                |
+---------------------------------------------------------------+
|  ■ SSRN No. 6109087 — run `make test` to verify all claims    |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "HOW TO REPRODUCE PAPER CLAIMS" in Instrument Serif ALL-CAPS with coral accent square |
| Subtitle | `label_editorial` | "Paper Section to Code Module to Test Command" in Plus Jakarta Sans caps |
| Three-column header row | `label_editorial` | "PAPER SECTION", "CODE MODULE", "TEST COMMAND" column labels |
| Row I: Confidence Scoring | `final_score` | Maps Section 3.2 to attribution/confidence.py and calibration.py |
| Row II: Multi-Source Resolution | `entity_resolve` | Maps Section 4.1 to resolution/entity_resolver.py |
| Row III: Assurance Levels | `assurance_a2` | Maps Section 5 to schemas/attribution.py and enums.py |
| Row IV: MCP Consent | `security_layer` | Maps Section 6 to mcp/server.py and api/routes/permissions.py |
| Row V: Oracle Problem | `problem_statement` | Conceptual claim -- no direct code, references design documentation |
| Horizontal dividers between rows | `accent_line` | Dashed coral lines separating each mapping row |
| Flow arrows (paper to code to test) | `data_flow` | Left-to-right arrows connecting the three columns |
| Roman numerals I-V | `section_numeral` | Row labels in editorial style |
| Footer callout | `callout_box` | SSRN reference and "run make test" instruction |

## Anti-Hallucination Rules

1. The SSRN number is 6109087 -- do not invent a different number.
2. Paper section numbers are illustrative -- the actual manuscript section numbering may differ. Present them as approximate references.
3. The Oracle Problem (Row V) is a conceptual contribution with NO direct code implementation -- this must be shown explicitly as "conceptual" to avoid implying code exists.
4. Module paths must use `music_attribution/` as the package root, not `src/` in labels.
5. Test commands use `make test -k <keyword>` pattern -- not `pytest` directly in the figure (this is the user-facing command).
6. Assurance levels are A0-A3 (four levels) -- not A1-A4 or any other range.
7. Only reference modules that actually exist in the repo -- do not invent module names.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Tutorial diagram: three-column reproducibility map linking academic paper sections on music attribution to corresponding open-source code modules and test commands, covering confidence scoring, multi-source entity resolution, A0-A3 assurance levels, and MCP consent infrastructure -- every substantive claim is verifiable by running a single make test command.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Tutorial diagram: three-column reproducibility map linking academic paper sections on music attribution to corresponding open-source code modules and test commands, covering confidence scoring, multi-source entity resolution, A0-A3 assurance levels, and MCP consent infrastructure -- every substantive claim is verifiable by running a single make test command.](docs/figures/repo-figures/assets/fig-howto-02-reproduce-paper-claims.jpg)

*Paper-to-code reproducibility map for SSRN No. 6109087 (Teikari, 2026). Each row connects a manuscript section -- from transparent confidence scoring to the Oracle Problem -- to the specific module and test keyword that validates it, making the music attribution scaffold a fully auditable companion to the research.*

### From this figure plan (relative)

![Tutorial diagram: three-column reproducibility map linking academic paper sections on music attribution to corresponding open-source code modules and test commands, covering confidence scoring, multi-source entity resolution, A0-A3 assurance levels, and MCP consent infrastructure -- every substantive claim is verifiable by running a single make test command.](../assets/fig-howto-02-reproduce-paper-claims.jpg)
