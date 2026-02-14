"""Splink probabilistic record linkage for entity resolution.

Stage 4 of the resolution cascade. Implements Fellegi-Sunter probabilistic
record linkage at scale using the Splink library. Estimates match/non-match
probability distributions via expectation-maximization and produces
calibrated linkage scores. Uses DuckDB backend for performance.

The Fellegi-Sunter model treats record comparison as a binary classification
problem: for each pair of records, it estimates the probability that they
refer to the same entity based on agreement/disagreement patterns across
comparison fields. The model parameters (m-probabilities for matches,
u-probabilities for non-matches) are estimated from the data using EM.

When Splink is not available (e.g., in lightweight test environments), the
matcher falls back to a simple exact-match heuristic on comparison columns.

Notes
-----
This module implements the probabilistic record linkage layer described in
Teikari (2026), Section 4.4. Splink v4 API is used (``from splink import
block_on``, not ``splink.blocking_rules_library``).

References
----------
.. [1] Fellegi, I. P., & Sunter, A. B. (1969). "A Theory for Record Linkage."
   Journal of the American Statistical Association, 64(328), 1183-1210.

See Also
--------
music_attribution.resolution.embedding_match : Stage 3 (runs before this).
music_attribution.resolution.graph_resolution : Stage 5 (runs after this).
"""

from __future__ import annotations

import contextlib
import logging
from collections import defaultdict
from typing import Any

import pandas as pd

logger = logging.getLogger(__name__)


class SplinkMatcher:
    """Probabilistic record linkage using the Splink library.

    Uses the Fellegi-Sunter model with configurable comparison columns
    and blocking rules to efficiently link records at scale. The workflow
    is:

    1. ``configure_model()`` -- define comparison columns.
    2. ``estimate_parameters()`` -- learn m/u probabilities from data.
    3. ``predict()`` -- compute match probabilities for all candidate pairs.
    4. ``cluster()`` -- group records by match probability threshold.

    Attributes
    ----------
    _model_configured : bool
        Whether ``configure_model()`` has been called.
    _comparison_columns : list[str]
        Column names used for record comparison.
    _linker : Any
        The Splink ``Linker`` instance (``None`` until parameters are estimated).
    """

    def __init__(self) -> None:
        self._model_configured = False
        self._comparison_columns: list[str] = []
        self._linker: Any = None

    def configure_model(self, comparison_columns: list[str]) -> None:
        """Configure the Splink model with comparison columns.

        Must be called before ``estimate_parameters()``. Each column
        will be compared using exact-match comparisons with term
        frequency adjustments.

        Parameters
        ----------
        comparison_columns : list[str]
            Column names to compare (e.g., ``["canonical_name", "isrc"]``).
        """
        self._comparison_columns = comparison_columns
        self._model_configured = True

    def estimate_parameters(self, records: pd.DataFrame) -> None:
        """Estimate Fellegi-Sunter m/u parameters from data.

        Uses random sampling to estimate u-probabilities (probability of
        agreement among non-matches) and expectation-maximization to
        estimate m-probabilities (probability of agreement among matches)
        for each comparison column.

        Parameters
        ----------
        records : pd.DataFrame
            DataFrame with a ``unique_id`` column plus all configured
            comparison columns.

        Raises
        ------
        RuntimeError
            If ``configure_model()`` has not been called first.

        Notes
        -----
        If Splink is not installed, falls back to ``None`` linker and
        subsequent calls to ``predict()`` will use the simple exact-match
        fallback.
        """
        if not self._model_configured:
            msg = "Model not configured. Call configure_model() first."
            raise RuntimeError(msg)

        try:
            import splink.comparison_library as cl
            from splink import DuckDBAPI, Linker, SettingsCreator, block_on

            comparisons = []
            for col in self._comparison_columns:
                comparisons.append(cl.ExactMatch(col).configure(term_frequency_adjustments=True))

            blocking_rules = [block_on(col) for col in self._comparison_columns]

            settings = SettingsCreator(
                link_type="dedupe_only",
                comparisons=comparisons,  # type: ignore[arg-type]
                blocking_rules_to_generate_predictions=blocking_rules,  # type: ignore[arg-type]
            )

            db_api = DuckDBAPI()
            self._linker = Linker(records, settings, db_api=db_api)  # type: ignore[arg-type]
            self._linker.training.estimate_u_using_random_sampling(max_pairs=1e5)

            # Try to estimate probability two random records match
            for col in self._comparison_columns:
                with contextlib.suppress(Exception):
                    self._linker.training.estimate_parameters_using_expectation_maximisation(
                        block_on(col), fix_u_probabilities=False
                    )

        except ImportError:
            logger.warning("Splink not available, using fallback parameter estimation")
            self._linker = None

    def predict(self, records: pd.DataFrame) -> pd.DataFrame:
        """Predict match probabilities for all candidate record pairs.

        If the Splink linker is available, uses the trained model to
        predict. Otherwise, falls back to a simple exact-match heuristic
        on the comparison columns.

        Parameters
        ----------
        records : pd.DataFrame
            DataFrame with comparison columns (used only in fallback mode).

        Returns
        -------
        pd.DataFrame
            DataFrame with columns ``unique_id_l``, ``unique_id_r``,
            and ``match_probability`` (float in [0, 1]).
        """
        if self._linker is not None:
            try:
                predictions = self._linker.inference.predict()
                df: pd.DataFrame = predictions.as_pandas_dataframe()
                return df[["unique_id_l", "unique_id_r", "match_probability"]]  # type: ignore[no-any-return]
            except Exception as e:
                logger.warning("Splink prediction failed: %s, using fallback", e)

        # Fallback: simple exact match on comparison columns
        return self._fallback_predict(records)

    def cluster(
        self,
        predictions: pd.DataFrame,
        threshold: float = 0.85,
    ) -> list[list[int]]:
        """Cluster records into entity groups based on match predictions.

        Uses union-find with path compression to transitively merge
        records connected by match probabilities above the threshold.

        Parameters
        ----------
        predictions : pd.DataFrame
            DataFrame with columns ``unique_id_l``, ``unique_id_r``,
            and ``match_probability``.
        threshold : float, optional
            Minimum match probability to consider a pair as linked.
            Default is 0.85.

        Returns
        -------
        list[list[int]]
            Clusters of ``unique_id`` values. Each cluster represents
            records believed to be the same entity.
        """
        # Filter predictions above threshold
        above = predictions[predictions["match_probability"] >= threshold]

        # Union-find clustering
        parent: dict[int, int] = {}

        def find(x: int) -> int:
            if x not in parent:
                parent[x] = x
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        # Collect all IDs
        all_ids: set[int] = set()
        for _, row in above.iterrows():
            lid = int(row["unique_id_l"])
            rid = int(row["unique_id_r"])
            all_ids.add(lid)
            all_ids.add(rid)
            union(lid, rid)

        # Also add unpaired IDs from predictions
        for _, row in predictions.iterrows():
            all_ids.add(int(row["unique_id_l"]))
            all_ids.add(int(row["unique_id_r"]))

        # Group by root
        groups: dict[int, list[int]] = defaultdict(list)
        for uid in all_ids:
            groups[find(uid)].append(uid)

        return list(groups.values())

    def _fallback_predict(self, records: pd.DataFrame) -> pd.DataFrame:
        """Fallback prediction using exact matching on comparison columns.

        Used when Splink is not available or fails. Computes match
        probability as the fraction of comparison columns with exact
        agreement between each record pair.

        Parameters
        ----------
        records : pd.DataFrame
            DataFrame with ``unique_id`` column and comparison columns.

        Returns
        -------
        pd.DataFrame
            DataFrame with columns ``unique_id_l``, ``unique_id_r``,
            ``match_probability``.
        """
        pairs = []
        n = len(records)
        for i in range(n):
            for j in range(i + 1, n):
                matches = 0
                total = len(self._comparison_columns)
                for col in self._comparison_columns:
                    val_i = records.iloc[i].get(col)
                    val_j = records.iloc[j].get(col)
                    if val_i is not None and val_j is not None and val_i == val_j:
                        matches += 1
                prob = matches / total if total > 0 else 0.0
                pairs.append(
                    {
                        "unique_id_l": records.iloc[i]["unique_id"],
                        "unique_id_r": records.iloc[j]["unique_id"],
                        "match_probability": prob,
                    }
                )
        return pd.DataFrame(pairs)
