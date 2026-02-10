# Team Archetype Profiles

Team archetypes represent the different types of teams that might instantiate this scaffold. Each archetype defines a **probability lens** — a consistent set of biases across all decision nodes that reflect the team's constraints, preferences, and capabilities.

---

## The Four Archetypes

| Archetype | Team Size | Technical Depth | Budget | Key Constraint |
|-----------|-----------|----------------|--------|----------------|
| **Engineer-Heavy Startup** | 5-15 | Deep | Moderate | Time-to-market vs. control |
| **Musician-First Team** | 1-3 | Shallow | Low | Technical complexity ceiling |
| **Solo Hacker** | 1 | Variable | Minimal | Cannot sustain any operational burden |
| **Well-Funded Startup** | 10-30+ | Deep | High | Enterprise credibility requirements |

---

## How Archetypes Modulate Decisions

Each `.decision.yaml` file contains an `archetype_weights` section with `probability_overrides` for each archetype. These overrides replace the prior probabilities when reasoning from a specific team profile.

**Example**: For the `primary_database` decision:

| Option | Prior | Engineer-Heavy | Musician-First | Solo Hacker | Well-Funded |
|--------|-------|---------------|----------------|-------------|-------------|
| PostgreSQL Unified | 0.45 | 0.60 | 0.20 | 0.15 | 0.45 |
| Supabase | 0.25 | 0.10 | 0.55 | 0.40 | 0.15 |
| SQLite/Turso | 0.15 | 0.05 | 0.20 | 0.40 | 0.05 |
| CockroachDB | 0.15 | 0.25 | 0.05 | 0.05 | 0.35 |

The same decision space, four different probability distributions reflecting four different team realities.

---

## Archetype File Structure

Each `.archetype.yaml` file contains:

- **`archetype_id`**: Unique identifier matching `archetype_weights` keys in decision nodes
- **`team_profile`**: Team size, composition, technical experience, budget range
- **`hard_constraints`**: Non-negotiable requirements that eliminate certain options
- **`soft_preferences`**: Preferences that shift probabilities without eliminating options
- **`decision_overrides`**: Per-decision probability override summary (references back to decision nodes)

---

## Using Archetypes

1. **Identify your archetype** — Which profile best describes your team?
2. **Apply the lens** — Use that archetype's probability overrides across all decisions
3. **Compose a scenario** — Collapse the probability distributions into specific choices (see [`../scenarios/`](../scenarios/))
4. **Customize** — Override individual decisions where your team differs from the archetype

---

## Creating New Archetypes

To add a new archetype:

1. Create `<name>.archetype.yaml` in this directory
2. Add `<archetype_id>` entries to `archetype_weights` in every `.decision.yaml` file
3. Ensure all `probability_overrides` sum to 1.0 for each decision
4. Add a scenario in `../scenarios/` demonstrating the archetype in action

---

## See Also

- [`../decisions/`](../decisions/) — Decision nodes with archetype probability overrides
- [`../scenarios/`](../scenarios/) — Composed paths through the decision network
- [`../domains/`](../domains/) — Domain overlays that further modulate probabilities
