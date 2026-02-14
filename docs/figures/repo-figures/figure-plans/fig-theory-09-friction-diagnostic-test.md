# fig-theory-09: Two-Friction Diagnostic Test

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-09 |
| **Title** | Two-Friction Diagnostic Test |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation logic, decision framework) |
| **Location** | docs/theory/two-friction-taxonomy.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure provides a decision flowchart for classifying any friction point in the music attribution pipeline as either administrative (automate) or discovery (preserve). It answers: "Given a specific friction point in the system, how do I decide whether to automate it or keep it?"

The key message is: "Three diagnostic questions -- Does it involve human agency? Does it build identity? Does it create community? If any answer is YES, it is discovery friction and must be preserved."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  FRICTION DIAGNOSTIC TEST                                      |
|  ■ Classify Any Friction Point                                 |
+---------------------------------------------------------------+
|                                                                |
|              ┌───────────────────────┐                         |
|              │  FRICTION POINT       │                         |
|              │  identified           │                         |
|              └───────────┬───────────┘                         |
|                          │                                     |
|                          ▼                                     |
|              ┌───────────────────────┐                         |
|              │  Does it involve      │                         |
|              │  HUMAN AGENCY?        │                         |
|              │  (choice, taste,      │                         |
|              │   judgment)           │                         |
|              └─────┬───────────┬─────┘                         |
|                YES │           │ NO                             |
|                    │           ▼                                |
|                    │  ┌───────────────────────┐                |
|                    │  │  Does it build        │                |
|                    │  │  IDENTITY?             │                |
|                    │  │  (reputation, brand,   │                |
|                    │  │   artistic voice)      │                |
|                    │  └─────┬───────────┬─────┘                |
|                    │    YES │           │ NO                    |
|                    │        │           ▼                       |
|                    │        │  ┌───────────────────────┐       |
|                    │        │  │  Does it create       │       |
|                    │        │  │  COMMUNITY?            │       |
|                    │        │  │  (connections, shared  │       |
|                    │        │  │   experience)          │       |
|                    │        │  └─────┬───────────┬─────┘       |
|                    │        │    YES │           │ NO           |
|                    │        │        │           │              |
|                    ▼        ▼        ▼           ▼              |
|          ┌──────────────────────┐  ┌──────────────────────┐   |
|          │  DISCOVERY FRICTION  │  │  ADMIN FRICTION       │   |
|          │  ────────────────── │  │  ──────────────       │   |
|          │  ■ PRESERVE         │  │  ■ AUTOMATE            │   |
|          │                     │  │                        │   |
|          │  Design the system  │  │  Build pipeline to     │   |
|          │  to support this    │  │  eliminate this         │   |
|          │  friction, not      │  │  friction entirely.     │   |
|          │  remove it.         │  │                        │   |
|          └──────────────────────┘  └──────────────────────┘   |
|                                                                |
+---------------------------------------------------------------+
|  ■ If ANY of the three questions is YES → Discovery friction.  |
|    ALL three must be NO → Administrative friction.              |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "FRICTION DIAGNOSTIC TEST" with coral accent square |
| Subtitle | `label_editorial` | "Classify Any Friction Point" |
| Entry node | `processing_stage` | "FRICTION POINT identified" -- starting point |
| Question 1: Agency | `decision_point` | "Does it involve HUMAN AGENCY?" with examples |
| Question 2: Identity | `decision_point` | "Does it build IDENTITY?" with examples |
| Question 3: Community | `decision_point` | "Does it create COMMUNITY?" with examples |
| Discovery outcome | `solution_component` | "PRESERVE" -- design the system to support this friction |
| Admin outcome | `problem_statement` | "AUTOMATE" -- build pipeline to eliminate this friction |
| YES branches | `data_flow` | All YES branches lead to Discovery friction |
| NO branches | `data_flow` | Only all-NO path leads to Admin friction |
| Footer rule | `callout_box` | "If ANY is YES -> Discovery. ALL three NO -> Administrative." |

## Anti-Hallucination Rules

1. The three diagnostic questions are: Agency, Identity, Community. Do NOT add or remove questions.
2. The logic is OR-based: if ANY question is YES, it is discovery friction. Do NOT require all three.
3. Only when ALL three are NO is it administrative friction.
4. "Agency" means choice, taste, judgment -- not software agent behavior.
5. "Identity" means artistic reputation and brand -- not database identity/entity resolution.
6. "Community" means human connections and shared experience -- not online community platforms.
7. Do NOT include specific technology names -- this is a conceptual diagnostic tool.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Decision tree: three-question diagnostic flowchart for classifying friction in music attribution pipelines -- testing for human agency, artistic identity, and community building -- where any YES identifies discovery friction to preserve and all NO identifies administrative friction to automate, enabling transparent confidence in which processes the open-source scaffold should target.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Decision tree: three-question diagnostic flowchart for classifying friction in music attribution pipelines -- testing for human agency, artistic identity, and community building -- where any YES identifies discovery friction to preserve and all NO identifies administrative friction to automate, enabling transparent confidence in which processes the open-source scaffold should target.](docs/figures/repo-figures/assets/fig-theory-09-friction-diagnostic-test.jpg)

*Figure 9. The friction diagnostic test: three questions (Does it involve human agency? Does it build identity? Does it create community?) classify any friction point in the music attribution pipeline, using OR logic where any YES means discovery friction to preserve.*

### From this figure plan (relative)

![Decision tree: three-question diagnostic flowchart for classifying friction in music attribution pipelines -- testing for human agency, artistic identity, and community building -- where any YES identifies discovery friction to preserve and all NO identifies administrative friction to automate, enabling transparent confidence in which processes the open-source scaffold should target.](../assets/fig-theory-09-friction-diagnostic-test.jpg)
