/**
 * Uncertainty-aware provenance types mirroring Python schemas from
 * src/music_attribution/schemas/uncertainty.py
 *
 * Academic grounding:
 * - UProp (Duan 2025): intrinsic/extrinsic decomposition
 * - Liu (2025): 4-dimensional uncertainty framework
 * - Yáñez (2025): confidence-weighted source integration
 * - Tian (2025): TH-Score overconfidence detection
 * - Zhang (2026): trajectory-level calibration (HTC)
 */

import type { Source } from "./enums";

export type UncertaintySource =
  | "INTRINSIC"
  | "EXTRINSIC"
  | "ALEATORIC"
  | "EPISTEMIC";

export type ConfidenceMethod =
  | "SELF_REPORT"
  | "MULTI_SAMPLE"
  | "LOGPROB"
  | "ENSEMBLE"
  | "CONFORMAL"
  | "SOURCE_WEIGHTED"
  | "HUMAN_RATED"
  | "HTC";

export type CalibrationStatus = "CALIBRATED" | "UNCALIBRATED" | "PENDING";

export type ConfidenceTrend =
  | "INCREASING"
  | "DECREASING"
  | "STABLE"
  | "VOLATILE";

export interface StepUncertainty {
  step_id: string;
  step_name: string;
  step_index: number;
  stated_confidence: number;
  calibrated_confidence: number;
  intrinsic_uncertainty: number;
  extrinsic_uncertainty: number;
  total_uncertainty: number;
  input_uncertainty: number | null;
  reasoning_uncertainty: number | null;
  parameter_uncertainty: number | null;
  prediction_uncertainty: number | null;
  uncertainty_sources: UncertaintySource[];
  confidence_method: ConfidenceMethod;
  preceding_step_ids: string[];
}

export interface SourceContribution {
  source: Source;
  confidence: number;
  weight: number;
  calibration_quality: number;
  record_count: number;
  is_human: boolean;
}

export interface CalibrationMetadata {
  expected_calibration_error: number;
  calibration_set_size: number;
  status: CalibrationStatus;
  method: string | null;
}

export interface OverconfidenceReport {
  stated_confidence: number;
  actual_accuracy: number;
  overconfidence_gap: number;
  th_score: number | null;
  h_score: number | null;
  eci: number | null;
}

export interface TrajectoryCalibration {
  trajectory_id: string;
  step_count: number;
  confidence_trend: ConfidenceTrend;
  initial_confidence: number;
  final_confidence: number;
  htc_feature_vector: number[] | null;
}

export interface UncertaintyAwareProvenance {
  steps: StepUncertainty[];
  source_contributions: SourceContribution[];
  calibration: CalibrationMetadata | null;
  overconfidence: OverconfidenceReport | null;
  trajectory: TrajectoryCalibration | null;
  total_uncertainty: number;
  dominant_uncertainty_source: UncertaintySource | null;
}

/**
 * Simplified citation reference for UI rendering.
 * Derived from ProvenanceEvent + StepUncertainty.
 */
export interface CitationReference {
  index: number;
  source: Source;
  confidence: number;
  label: string;
  detail: string;
  timestamp: string;
}

/**
 * Provenance API response shape.
 */
export interface ProvenanceResponse {
  attribution_id: string;
  provenance_chain: import("./attribution").ProvenanceEvent[];
  uncertainty_summary: UncertaintyAwareProvenance | null;
}
