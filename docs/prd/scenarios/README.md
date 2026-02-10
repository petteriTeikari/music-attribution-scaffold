# Scenario Compositions

Scenarios are **collapsed paths** through the probabilistic decision network. Each scenario records a specific set of resolved decisions (one option per decision node), the archetype and domain that produced those choices, and the joint probability of the complete path.

---

## What Is a Scenario?

While the decision network preserves the full probability space, a scenario is a **point estimate** — a single coherent configuration that a team would actually deploy. Think of it as "applying the archetype lens, choosing the highest-probability option at each node, and recording the result."

```
Scenario = Archetype + Domain + Resolved Decisions + Joint Probability
```

---

## Available Scenarios

| Scenario | Archetype | Domain | Key Choices |
|----------|-----------|--------|-------------|
| [music-attribution-mvp](music-attribution-mvp.scenario.yaml) | Engineer-Heavy | Music Attribution | PostgreSQL+AGE, MCP, Render, Neon |
| [solo-musician-mvp](solo-musician-mvp.scenario.yaml) | Musician-First | Music Attribution | Supabase, REST, auto-deploy |
| [dpp-enterprise](dpp-enterprise.scenario.yaml) | Well-Funded | DPP Traceability | AWS ECS, RDS, Terraform, Datadog |

---

## Scenario File Structure

Each `.scenario.yaml` contains:

- **`scenario_id`**: Unique identifier
- **`archetype`**: Which team archetype produced this scenario
- **`domain`**: Which domain overlay was applied
- **`resolved_decisions`**: Map of decision_id → chosen option_id for all 23 decisions
- **`joint_probability`**: Product of all chosen option probabilities (archetype-adjusted)
- **`rationale`**: Why this combination makes sense as a coherent whole
- **`trade_offs`**: What this scenario sacrifices and what it gains

---

## Creating New Scenarios

1. Choose an archetype from [`../archetypes/`](../archetypes/)
2. Choose a domain from [`../domains/`](../domains/)
3. For each decision node, select the option that best fits the archetype+domain combination
4. Calculate the joint probability as the product of selected option probabilities
5. Document rationale and trade-offs

---

## See Also

- [`../decisions/`](../decisions/) — The decision network that scenarios traverse
- [`../archetypes/`](../archetypes/) — Team profiles that produce probability lenses
- [`../domains/`](../domains/) — Domain overlays that adjust priors
