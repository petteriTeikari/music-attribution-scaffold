# fig-frontend-09: Jotai State Architecture

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-frontend-09 |
| **Title** | Jotai State Architecture: Atom Tree with Read/Write Flows |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 |
| **Location** | docs/architecture/frontend.md |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

This figure maps the Jotai atom tree across four store files (theme.ts, mode.ts, works.ts, proficiency.ts). It shows which atoms are primitive (read-write), which are derived (read-only), which use atomWithStorage for persistence, and how data flows from user interactions through atoms to component renders.

The key message is: "Four store files define the entire client state -- primitive atoms hold raw data, derived atoms compute filtered/sorted/leveled views, and atomWithStorage persists proficiency across sessions."

## Visual Concept (ASCII Layout)

```
+-----------------------------------------------------------------------+
|  JOTAI STATE ARCHITECTURE                                              |
|  ■ Atom Tree + Data Flows                                              |
+-----------------------------------------------------------------------+
|                                                                        |
|  I. THEME STORE (theme.ts)                                             |
|  ─────────────────────────                                             |
|                                                                        |
|  themeAtom (rw)                                                        |
|    "light" | "dark" | "system"                                         |
|         │                                                              |
|         └──> resolvedThemeAtom (derived, ro)                           |
|               "light" | "dark"                                         |
|               (checks window.matchMedia for "system")                  |
|                                                                        |
|  II. MODE STORE (mode.ts)                                              |
|  ─────────────────────────                                             |
|                                                                        |
|  userRoleAtom (rw)                                                     |
|    "artist" | "query"                                                  |
|    (toggles /review visibility + agent context)                        |
|                                                                        |
|  III. WORKS STORE (works.ts)                                           |
|  ──────────────────────────                                            |
|                                                                        |
|  worksAtom (rw) ─────────────────────────────────────┐                |
|    AttributionRecord[]                                │                |
|                                                       │                |
|  worksLoadingAtom (rw)                                │                |
|    boolean                                            │                |
|                                                       ▼                |
|  searchQueryAtom (rw) ──> filteredWorksAtom (derived, ro)             |
|    string                   ■ filters by title/artist query            |
|                             ■ sorts by sortField + sortDirection       |
|  sortFieldAtom (rw) ────>   ■ returns sorted AttributionRecord[]      |
|    "confidence"|"title"|"updated"                                      |
|                                                                        |
|  sortDirectionAtom (rw) ->                                             |
|    "asc" | "desc"                                                      |
|                                                                        |
|  selectedWorkAtom (rw)                                                 |
|    AttributionRecord | null                                            |
|                                                                        |
|  IV. PROFICIENCY STORE (proficiency.ts)                                |
|  ──────────────────────────────────────                                |
|                                                                        |
|  proficiencyStateAtom (atomWithStorage, "ma-proficiency")              |
|    Record<Skill, SkillMetrics>  ──────────────────────────┐           |
|    Skills: review, feedback, confidence_reading            │           |
|    Metrics: { interactions, successes }                    ▼           |
|                                          proficiencyLevelsAtom (ro)    |
|                                            per-skill: novice |        |
|                                            intermediate | expert      |
|                                                     │                  |
|                                                     ▼                  |
|                                          overallProficiencyAtom (ro)   |
|                                            max of individual levels    |
|                                                                        |
|  LEGEND                                                                |
|  ──────                                                                |
|  (rw) = read-write primitive atom                                      |
|  (ro) = read-only derived atom                                         |
|  atomWithStorage = persisted to localStorage                           |
+-----------------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "JOTAI STATE ARCHITECTURE" in display font |
| Theme store | `module_grid` | themeAtom -> resolvedThemeAtom derivation |
| Mode store | `module_grid` | userRoleAtom with role values |
| Works store | `module_grid` | 6 atoms: works, loading, search, sort field, sort direction, selected + filteredWorksAtom derived |
| Proficiency store | `module_grid` | proficiencyStateAtom (persisted) -> proficiencyLevelsAtom -> overallProficiencyAtom |
| Derivation arrows | `data_flow` | Arrows from primitive atoms to derived atoms |
| Atom type labels | `data_mono` | (rw) and (ro) markers |
| Type annotations | `data_mono` | TypeScript types for each atom value |
| Legend | `callout_box` | Explains rw, ro, and atomWithStorage |

## Anti-Hallucination Rules

1. State management is Jotai (not Redux, Zustand, or React Context).
2. There are exactly 4 store files: theme.ts, mode.ts, works.ts, proficiency.ts.
3. theme.ts: themeAtom ("light"|"dark"|"system") -> resolvedThemeAtom ("light"|"dark").
4. mode.ts: userRoleAtom ("artist"|"query") -- single atom, no derivations.
5. works.ts: 6 atoms (worksAtom, worksLoadingAtom, selectedWorkAtom, sortFieldAtom, sortDirectionAtom, searchQueryAtom) -> filteredWorksAtom.
6. proficiency.ts: proficiencyStateAtom (atomWithStorage with key "ma-proficiency") -> proficiencyLevelsAtom -> overallProficiencyAtom.
7. Skills tracked: "review", "feedback", "confidence_reading" (exactly 3).
8. Proficiency levels: novice (<10 interactions), intermediate (10-50 + 60% success), expert (50+ + 75% success).
9. computeLevel() is a pure function, not an atom.

## Alt Text

Jotai atom tree across four stores showing primitive read-write atoms, derived read-only atoms, data flow arrows, and localStorage persistence.
