"""Generic pipeline runner for declarative DAGs.

Validates and executes pipeline stages in topological order.
Currently implements validation and dry-run mode; actual stage
execution would be wired to real implementations when deploying
(or to an orchestrator like Prefect/Dagster via adapter classes).

The runner is intentionally minimal -- it validates the DAG structure
and produces an execution plan. This separation allows the same
``PipelineDAG`` model to be consumed by different execution backends
without modification.

Classes
-------
PipelineRunner
    Validates DAGs and produces dry-run execution plans.

See Also
--------
music_attribution.pipeline.dag : DAG model and ``ATTRIBUTION_DAG``.
"""

from __future__ import annotations

import logging

from music_attribution.pipeline.dag import PipelineDAG

logger = logging.getLogger(__name__)


class PipelineRunner:
    """Generic runner that validates and executes a PipelineDAG.

    The runner is intentionally simple -- it validates the DAG and
    provides a dry-run mode. Actual stage execution would be wired
    to real implementations when deploying (or to an orchestrator
    like Prefect/Dagster).

    This class is stateless and can be instantiated freely.
    """

    def validate(self, dag: PipelineDAG) -> None:
        """Validate that the DAG is well-formed and acyclic.

        Delegates to ``dag.validate_acyclic()`` and logs the result.
        Dependency existence is already validated by the Pydantic
        model validator on ``PipelineDAG``.

        Parameters
        ----------
        dag : PipelineDAG
            Pipeline DAG to validate.

        Raises
        ------
        ValueError
            If the DAG contains cycles or invalid dependency references.
        """
        dag.validate_acyclic()
        logger.info("DAG '%s' validated: %d stages, acyclic", dag.name, len(dag.stages))

    def dry_run(self, dag: PipelineDAG) -> list[str]:
        """Return the execution plan without running any stages.

        Validates the DAG and produces a topologically sorted list of
        stage names representing the execution order.

        Parameters
        ----------
        dag : PipelineDAG
            Pipeline DAG to plan.

        Returns
        -------
        list[str]
            Stage names in execution order (dependencies first).
        """
        self.validate(dag)
        order = dag.topological_sort()
        stage_names = [s.name for s in order]
        logger.info("Dry run plan: %s", " → ".join(stage_names))
        return stage_names
