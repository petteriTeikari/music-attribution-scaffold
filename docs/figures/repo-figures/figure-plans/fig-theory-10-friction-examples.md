# fig-theory-10: Real-World Friction Examples

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-theory-10 |
| **Title** | Real-World Friction Examples |
| **Audience** | L2 (PhD Student / Policy Researcher) |
| **Complexity** | L2 (academic terms, real-world categorization) |
| **Location** | docs/theory/two-friction-taxonomy.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure presents a categorized collection of real-world friction scenarios in the music industry, classified as either administrative or discovery friction. It answers: "Can you show me concrete examples of each friction type so I can apply the taxonomy myself?"

The key message is: "Most pain points in music attribution are administrative friction that can be automated -- but some friction (curation, recommendation, taste-making) must be carefully preserved."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  FRICTION IN THE WILD                                          |
|  ■ Real-World Examples Classified                              |
+---------------------------------------------------------------+
|                                                                |
|  ADMINISTRATIVE FRICTION                                       |
|  (Automate)                                                    |
|  ─────────────────────────────────────────────                 |
|                                                                |
|  ┌────────────────┬──────────────────┬──────────────────┐     |
|  │ LICENSING       │ REGISTRATION      │ REPORTING         │     |
|  │────────────────│──────────────────│──────────────────│     |
|  │ Sync licensing │ PRO registration │ Royalty calc.     │     |
|  │ forms across   │ across ASCAP,    │ across streaming  │     |
|  │ territories    │ BMI, PRS, GEMA   │ platforms         │     |
|  │                │                  │                   │     |
|  │ Mechanical     │ ISRC assignment  │ Quarterly         │     |
|  │ license        │ for each master  │ earnings          │     |
|  │ requests       │ recording        │ statements        │     |
|  │                │                  │                   │     |
|  │ Sample         │ ISWC filing for  │ Tax withholding   │     |
|  │ clearance      │ compositions     │ documentation     │     |
|  │ paperwork      │                  │                   │     |
|  └────────────────┴──────────────────┴──────────────────┘     |
|                                                                |
|  DISCOVERY FRICTION                                            |
|  (Preserve)                                                    |
|  ─────────────────────────────────────────────                 |
|                                                                |
|  ┌────────────────┬──────────────────┬──────────────────┐     |
|  │ CURATION        │ COLLABORATION     │ GATEKEEPING       │     |
|  │────────────────│──────────────────│──────────────────│     |
|  │ DJ selecting   │ Artist choosing  │ A&R listening    │     |
|  │ tracks for     │ a producer for   │ to demos,        │     |
|  │ a set          │ their album      │ signing acts      │     |
|  │                │                  │                   │     |
|  │ Record store   │ Musicians        │ Playlist curator  │     |
|  │ owner picking  │ jamming to find  │ exercising        │     |
|  │ what to stock  │ chemistry        │ editorial taste   │     |
|  │                │                  │                   │     |
|  │ Fan exploring  │ Songwriter       │ Music journalist  │     |
|  │ album liner    │ co-writing       │ reviewing new     │     |
|  │ notes          │ sessions         │ releases          │     |
|  └────────────────┴──────────────────┴──────────────────┘     |
|                                                                |
+---------------------------------------------------------------+
|  ■ Pattern: admin friction is about COMPLIANCE AND PROCESS.    |
|    Discovery friction is about TASTE AND RELATIONSHIPS.        |
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "FRICTION IN THE WILD" with coral accent square |
| Subtitle | `label_editorial` | "Real-World Examples Classified" |
| Admin section header | `label_editorial` | "ADMINISTRATIVE FRICTION (Automate)" with accent line |
| Admin: Licensing column | `problem_statement` | Sync forms, mechanical licenses, sample clearance |
| Admin: Registration column | `problem_statement` | PRO registration, ISRC assignment, ISWC filing |
| Admin: Reporting column | `problem_statement` | Royalty calculation, earnings statements, tax docs |
| Discovery section header | `label_editorial` | "DISCOVERY FRICTION (Preserve)" with accent line |
| Discovery: Curation column | `solution_component` | DJ selection, record store stocking, fan exploration |
| Discovery: Collaboration column | `solution_component` | Producer choice, jam sessions, co-writing |
| Discovery: Gatekeeping column | `solution_component` | A&R demos, playlist curation, music journalism |
| Section dividers | `accent_line` | Coral horizontal lines separating admin from discovery |
| Footer pattern note | `callout_box` | "Admin = compliance/process. Discovery = taste/relationships." |

## Anti-Hallucination Rules

1. All examples must be genuinely from the music industry -- do NOT include generic business examples.
2. Admin examples are about FORMS, REGISTRATION, and REPORTING -- processes with no artistic judgment.
3. Discovery examples involve TASTE, JUDGMENT, and RELATIONSHIPS -- inherently human processes.
4. PRO names mentioned (ASCAP, BMI, PRS, GEMA) are real performing rights organizations -- do NOT invent others.
5. Do NOT suggest that ALL gatekeeping is good -- the taxonomy specifically means taste-based gatekeeping.
6. Do NOT include technology-specific examples (API calls, database queries) -- this is L2.
7. "Sample clearance" is admin friction, but "deciding which sample to use" would be discovery friction -- the distinction matters.
8. Background must be warm cream (#f6f3e6), not white or gray.

## Alt Text

Categorization chart: real-world music industry friction examples classified into administrative friction (sync licensing, PRO registration, ISRC assignment, royalty reporting to automate) and discovery friction (DJ curation, artist collaboration, playlist gatekeeping to preserve) -- concrete applications of the two-friction taxonomy for music attribution and transparent confidence in which processes deserve automation.

## Image Embed

### For GitHub README / MkDocs (repo-root-relative)

![Categorization chart: real-world music industry friction examples classified into administrative friction (sync licensing, PRO registration, ISRC assignment, royalty reporting to automate) and discovery friction (DJ curation, artist collaboration, playlist gatekeeping to preserve) -- concrete applications of the two-friction taxonomy for music attribution and transparent confidence in which processes deserve automation.](docs/figures/repo-figures/assets/fig-theory-10-friction-examples.jpg)

*Figure 10. Real-world friction examples classified using the two-friction taxonomy: administrative friction involves compliance and process (licensing forms, ISRC assignment, royalty calculations), while discovery friction involves taste and relationships (DJ sets, co-writing sessions, editorial curation).*

### From this figure plan (relative)

![Categorization chart: real-world music industry friction examples classified into administrative friction (sync licensing, PRO registration, ISRC assignment, royalty reporting to automate) and discovery friction (DJ curation, artist collaboration, playlist gatekeeping to preserve) -- concrete applications of the two-friction taxonomy for music attribution and transparent confidence in which processes deserve automation.](../assets/fig-theory-10-friction-examples.jpg)
