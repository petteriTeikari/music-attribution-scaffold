"""Quality assurance: drift detection and data quality checks.

Provides statistical drift detection for monitoring pipeline health
at batch boundaries. Detects anomalous changes in confidence
distributions, source mix, and identifier coverage.

Submodules
----------
drift_detector
    ``DriftDetector`` class that compares current batch metadata
    against a historical baseline and produces a ``DriftReport``.

See Also
--------
music_attribution.observability.metrics : ``drift_detected`` counter.
music_attribution.schemas.batch.BatchMetadata : Input to drift checks.
"""

from __future__ import annotations
