"""Declarative pipeline DAG definition.

The attribution pipeline is defined as a Pydantic model -- the DAG is
*data*, not imperative code. A generic runner (``runner.py``) executes
stages in topological order using Kahn's algorithm.

This design pattern separates the "what" (stage definitions, dependencies,
I/O types) from the "how" (execution engine). The same DAG definition
could be executed by a simple sequential runner, Prefect, Dagster, or
any future orchestrator via an adapter class.

Architecture (5 stages)::

    ETL -> Entity Resolution -> Attribution -> API/MCP -> Chat

Boundary objects between stages::

    RawRecord -> NormalizedRecord -> ResolvedEntity -> AttributionRecord -> APIResponse

Classes
-------
PipelineStage
    A single stage in the pipeline with name, dependencies, module
    path, and I/O types.
PipelineDAG
    Directed acyclic graph of ``PipelineStage`` instances with
    dependency validation, cycle detection, and topological sorting.

Module Attributes
-----------------
ATTRIBUTION_DAG : PipelineDAG
    Canonical 5-stage pipeline definition used by the runner and
    referenced by the PRD decision network.

See Also
--------
music_attribution.pipeline.runner : Executes this DAG.
"""

from __future__ import annotations

import logging
from collections import defaultdict, deque

from pydantic import BaseModel, Field, model_validator

logger = logging.getLogger(__name__)


class PipelineStage(BaseModel):
    """A single stage in the attribution pipeline.

    Each stage declares its dependencies, implementation module, and
    I/O boundary object types. The runner uses this metadata to
    validate and execute the pipeline.

    Attributes
    ----------
    name : str
        Unique stage identifier in ``snake_case``
        (e.g. ``"entity_resolution"``).
    description : str
        Human-readable description of what this stage does.
    depends_on : list[str]
        List of stage names that must complete before this one.
        Empty list for root stages (e.g. ETL).
    module_path : str
        Python module path containing the stage implementation
        (e.g. ``"music_attribution.resolution"``).
    entry_class : str | None
        Optional class name within the module (for documentation
        and potential reflection-based execution).
    input_type : str | None
        Name of the Pydantic boundary object consumed by this stage
        (e.g. ``"NormalizedRecord"``). ``None`` for the ETL root stage.
    output_type : str
        Name of the Pydantic boundary object produced by this stage
        (e.g. ``"ResolvedEntity"``).
    """

    name: str
    description: str
    depends_on: list[str] = Field(default_factory=list)
    module_path: str
    entry_class: str | None = None
    input_type: str | None = None
    output_type: str


class PipelineDAG(BaseModel):
    """Declarative directed acyclic graph of pipeline stages.

    The DAG is the single source of truth for pipeline architecture.
    It can be validated (dependency existence, acyclicity), topologically
    sorted, and executed by a generic runner.

    Attributes
    ----------
    name : str
        Pipeline name (e.g. ``"music_attribution"``).
    description : str
        Human-readable description of the pipeline's purpose.
    stages : list[PipelineStage]
        Ordered list of pipeline stages. Order in this list does not
        imply execution order -- use ``topological_sort()`` for that.
    """

    name: str
    description: str = ""
    stages: list[PipelineStage]

    @model_validator(mode="after")
    def validate_dependencies_exist(self) -> PipelineDAG:
        """Validate that all ``depends_on`` references point to declared stages.

        Raises
        ------
        ValueError
            If any stage references an undeclared dependency.
        """
        stage_names = {s.name for s in self.stages}
        for stage in self.stages:
            for dep in stage.depends_on:
                if dep not in stage_names:
                    msg = f"Stage '{stage.name}' depends on undeclared stage '{dep}'"
                    raise ValueError(msg)
        return self

    def validate_acyclic(self) -> None:
        """Validate that the DAG contains no cycles using Kahn's algorithm.

        Performs a topological traversal and verifies that all nodes are
        visited. If the number of visited nodes is less than the total,
        at least one cycle exists.

        Raises
        ------
        ValueError
            If a cycle is detected (visited count < total stage count).
        """
        # Build adjacency list and in-degree count
        in_degree: dict[str, int] = defaultdict(int)
        adjacency: dict[str, list[str]] = defaultdict(list)
        stage_names = {s.name for s in self.stages}

        for name in stage_names:
            in_degree.setdefault(name, 0)

        for stage in self.stages:
            for dep in stage.depends_on:
                adjacency[dep].append(stage.name)
                in_degree[stage.name] += 1

        # Start with nodes that have no incoming edges
        queue: deque[str] = deque(name for name in stage_names if in_degree[name] == 0)
        visited = 0

        while queue:
            node = queue.popleft()
            visited += 1
            for child in adjacency[node]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        if visited != len(stage_names):
            msg = f"Pipeline DAG contains a cycle (visited {visited}/{len(stage_names)} nodes)"
            raise ValueError(msg)

    def topological_sort(self) -> list[PipelineStage]:
        """Return stages in topological execution order.

        Uses Kahn's algorithm with deterministic tie-breaking (sorted
        alphabetically) to produce a stable execution order.
        Dependencies are guaranteed to appear before their dependents.

        Returns
        -------
        list[PipelineStage]
            Stages in execution order (dependencies first).

        Raises
        ------
        ValueError
            If the DAG contains a cycle.
        """
        self.validate_acyclic()

        in_degree: dict[str, int] = defaultdict(int)
        adjacency: dict[str, list[str]] = defaultdict(list)
        stage_map = {s.name: s for s in self.stages}

        for name in stage_map:
            in_degree.setdefault(name, 0)

        for stage in self.stages:
            for dep in stage.depends_on:
                adjacency[dep].append(stage.name)
                in_degree[stage.name] += 1

        queue: deque[str] = deque(sorted(name for name in stage_map if in_degree[name] == 0))
        result: list[PipelineStage] = []

        while queue:
            node = queue.popleft()
            result.append(stage_map[node])
            for child in sorted(adjacency[node]):
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        return result


# --- The Attribution Pipeline DAG ---
# This is the canonical definition of the 5-stage pipeline.
# Module paths reference actual implementation classes.

ATTRIBUTION_DAG = PipelineDAG(
    name="music_attribution",
    description=(
        "5-stage music attribution pipeline: ingest raw data, resolve entities, "
        "compute attribution scores, serve via API/MCP, and interact via chat agent."
    ),
    stages=[
        PipelineStage(
            name="etl",
            description=(
                "Extract, transform, and load records from external sources "
                "(MusicBrainz, Discogs, AcoustID, file metadata). Applies rate "
                "limiting and data quality validation via DataQualityGate."
            ),
            depends_on=[],
            module_path="music_attribution.etl",
            entry_class="DataQualityGate",
            input_type=None,
            output_type="NormalizedRecord",
        ),
        PipelineStage(
            name="entity_resolution",
            description=(
                "Probabilistic record linkage using Splink (Fellegi-Sunter model). "
                "Deduplicates and clusters records into resolved entities with "
                "reproducible random seed."
            ),
            depends_on=["etl"],
            module_path="music_attribution.resolution",
            entry_class="ResolutionOrchestrator",
            input_type="NormalizedRecord",
            output_type="ResolvedEntity",
        ),
        PipelineStage(
            name="attribution",
            description=(
                "Compute attribution scores by aggregating credits across sources. "
                "Assigns A0-A3 assurance levels and calibrates confidence using "
                "conformal prediction sets."
            ),
            depends_on=["entity_resolution"],
            module_path="music_attribution.attribution",
            entry_class="CreditAggregator",
            input_type="ResolvedEntity",
            output_type="AttributionRecord",
        ),
        PipelineStage(
            name="api",
            description=(
                "Serve attribution records via REST API and MCP server. "
                "Includes health probes, Prometheus metrics, correlation ID "
                "middleware, and permission-gated endpoints."
            ),
            depends_on=["attribution"],
            module_path="music_attribution.api",
            entry_class="create_app",
            input_type="AttributionRecord",
            output_type="APIResponse",
        ),
        PipelineStage(
            name="chat",
            description=(
                "PydanticAI agent with 4 domain tools (explain_confidence, "
                "search_attributions, suggest_correction, submit_feedback). "
                "Streams via AG-UI protocol to CopilotKit frontend."
            ),
            depends_on=["api"],
            module_path="music_attribution.chat",
            entry_class="create_attribution_agent",
            input_type="APIResponse",
            output_type="AgentResponse",
        ),
    ],
)
