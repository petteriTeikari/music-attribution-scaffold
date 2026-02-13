# fig-choice-08: Why Jotai over Redux?

## Metadata

| Field | Value |
|-------|-------|
| **ID** | fig-choice-08 |
| **Title** | Why Jotai over Redux? |
| **Audience** | L3 (Software Engineer) |
| **Complexity** | L3 (implementation detail) |
| **Location** | docs/planning/ |
| **Priority** | P1 (High) |
| **Dimensions** | 1200 x 900px (4:3) |

## Purpose & Key Message

Explains the client state management choice. The scaffold uses Jotai (atomic state) for theme, role mode, and works state rather than Redux (centralized store) or Zustand (simplified store). Jotai's atom-based approach minimizes boilerplate, avoids the action/reducer ceremony, and integrates naturally with React's concurrent features.

The key message is: "Jotai's atomic model provides minimal-boilerplate state management -- each piece of state is an independent atom, no action/reducer ceremony needed."

## Visual Concept (ASCII Layout)

```
+---------------------------------------------------------------+
|  WHY JOTAI OVER REDUX?                                         |
|  ■ Client State: Atomic Primitives                             |
+---------------------------------------------------------------+
|                                                                |
|  SCAFFOLD STATE NEEDS                                          |
|  Three state domains: theme (light/dark), role (artist/query), |
|  works (attribution records). All client-side, localStorage.   |
|                                                                |
|  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐          |
|  │ JOTAI        │ │ REDUX        │ │ ZUSTAND      │          |
|  │ ■ SELECTED   │ │              │ │              │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │              │ │              │ │              │          |
|  │ // Define    │ │ // Slice     │ │ // Store     │          |
|  │ const theme  │ │ createSlice({│ │ create((set) │          |
|  │ = atom('lgt')│ │  name:'theme'│ │ => ({        │          |
|  │              │ │  initialState│ │   theme:'lgt'│          |
|  │ // Use       │ │  reducers:{} │ │   setTheme:  │          |
|  │ const [val,  │ │ })           │ │   (t)=>set({ │          |
|  │  setVal] =   │ │              │ │    theme:t}) │          |
|  │ useAtom(     │ │ // + dispatch│ │ }))          │          |
|  │  theme)      │ │ // + selector│ │              │          |
|  │              │ │ // + provider│ │ // Use       │          |
|  │ 2 lines      │ │ 15+ lines   │ │ useStore()   │          |
|  │              │ │              │ │              │          |
|  │──────────────│ │──────────────│ │──────────────│          |
|  │ Atomic       │ │ Centralized  │ │ Simplified   │          |
|  │ Independent  │ │ Single store │ │ Single store │          |
|  │ atoms        │ │ + slices     │ │ No boilerplat│          |
|  │              │ │              │ │              │          |
|  │ Zero         │ │ Heavy        │ │ Moderate     │          |
|  │ boilerplate  │ │ ceremony     │ │ boilerplate  │          |
|  │              │ │              │ │              │          |
|  │ React        │ │ Middleware   │ │ Framework    │          |
|  │ concurrent   │ │ heavy        │ │ agnostic     │          |
|  │ compatible   │ │              │ │              │          |
|  └──────────────┘ └──────────────┘ └──────────────┘          |
|                                                                |
+---------------------------------------------------------------+
|  Used for: theme atom, roleMode atom, works atom + localStorage|
+---------------------------------------------------------------+
```

## Content Elements

| Element | Semantic Tag | Description |
|---------|--------------|-------------|
| Title block | `heading_display` | "WHY JOTAI OVER REDUX?" with coral accent square |
| State needs banner | `label_editorial` | Three state domains: theme, role, works |
| Jotai card | `selected_option` | Code sample, atomic model, zero boilerplate |
| Redux card | `deferred_option` | Code sample, centralized store, heavy ceremony |
| Zustand card | `deferred_option` | Code sample, simplified store, moderate boilerplate |
| Usage footer | `callout_bar` | Concrete atoms used in the scaffold |

## Anti-Hallucination Rules

1. The scaffold uses Jotai for theme, role mode, and works state -- per MEMORY.md.
2. State is persisted to localStorage -- this is part of the adaptive UI system.
3. Jotai atoms are independent -- each piece of state is a separate atom.
4. Redux Toolkit (createSlice) is the modern Redux pattern, not legacy Redux with switch statements.
5. Zustand is a viable alternative -- simpler than Redux but still store-based.
6. Do NOT claim Redux is obsolete -- it is appropriate for large-scale apps with complex state interactions.
7. The choice is driven by the scaffold's small state surface -- three client-side state domains.
8. Background must be warm cream (#f6f3e6).

## Alt Text

Three-column comparison of state management libraries: Jotai selected for atomic minimal-boilerplate approach, versus Redux centralized store and Zustand simplified store.
