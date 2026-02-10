"""Splink probabilistic record linkage for entity resolution.

Implements Fellegi-Sunter probabilistic record linkage at scale. Estimates
match/non-match probability distributions and produces calibrated linkage
scores. Uses DuckDB backend for performance.
"""

from __future__ import annotations

import contextlib
import logging
from collections import defaultdict
from typing import Any

import pandas as pd

logger = logging.getLogger(__name__)


class SplinkMatcher:
    """Probabilistic record linkage using Splink.

    Uses Fellegi-Sunter model with configurable comparison columns
    and blocking rules to efficiently link records.
    """

    def __init__(self) -> None:
        self._model_configured = False
        self._comparison_columns: list[str] = []
        self._linker: Any = None

    def configure_model(self, comparison_columns: list[str]) -> None:
        """Configure the Splink model with comparison columns.

        Args:
            comparison_columns: List of column names to compare.
        """
        self._comparison_columns = comparison_columns
        self._model_configured = True

    def estimate_parameters(self, records: pd.DataFrame) -> None:
        """Estimate Fellegi-Sunter m/u parameters from data.

        Args:
            records: DataFrame with columns: unique_id + comparison columns.
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
        """Predict match probabilities for record pairs.

        Args:
            records: DataFrame with comparison columns.

        Returns:
            DataFrame with columns: unique_id_l, unique_id_r, match_probability.
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
        self, predictions: pd.DataFrame, threshold: float = 0.85,
    ) -> list[list[int]]:
        """Cluster records based on match predictions.

        Args:
            predictions: DataFrame with match probabilities.
            threshold: Minimum probability to consider a match.

        Returns:
            List of clusters (each cluster is a list of unique_ids).
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
        """Fallback prediction using exact matching on comparison columns."""
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
                pairs.append({
                    "unique_id_l": records.iloc[i]["unique_id"],
                    "unique_id_r": records.iloc[j]["unique_id"],
                    "match_probability": prob,
                })
        return pd.DataFrame(pairs)
