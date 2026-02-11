/**
 * Attribution types mirroring Python schemas from
 * src/music_attribution/schemas/attribution.py
 */

import type {
  AssuranceLevel,
  CreditRole,
  ProvenanceEventType,
  Source,
} from "./enums";

export interface Credit {
  entity_id: string;
  entity_name: string; // Display name (not in Python schema — added for frontend)
  role: CreditRole;
  role_detail: string | null;
  confidence: number;
  sources: Source[];
  assurance_level: AssuranceLevel;
}

export interface ConformalSet {
  coverage_level: number;
  prediction_sets: Record<string, CreditRole[]>;
  set_sizes: Record<string, number>;
  marginal_coverage: number;
  calibration_error: number;
  calibration_method: string;
  calibration_set_size: number;
}

// Discriminated union for provenance event details
export interface FetchEventDetails {
  type: "fetch";
  source: Source;
  source_id: string;
  records_fetched: number;
  rate_limited: boolean;
}

export interface ResolveEventDetails {
  type: "resolve";
  method: string;
  records_input: number;
  entities_output: number;
  confidence_range: [number, number];
}

export interface ScoreEventDetails {
  type: "score";
  previous_confidence: number | null;
  new_confidence: number;
  scoring_method: string;
}

export interface ReviewEventDetails {
  type: "review";
  reviewer_id: string;
  feedback_card_id: string;
  corrections_applied: number;
}

export interface UpdateEventDetails {
  type: "update";
  previous_version: number;
  new_version: number;
  fields_changed: string[];
  trigger: string;
}

export interface FeedbackEventDetails {
  type: "feedback";
  feedback_card_id: string;
  overall_assessment: number;
  corrections_count: number;
  accepted: boolean;
}

export type EventDetails =
  | FetchEventDetails
  | ResolveEventDetails
  | ScoreEventDetails
  | ReviewEventDetails
  | UpdateEventDetails
  | FeedbackEventDetails;

export interface ProvenanceEvent {
  event_type: ProvenanceEventType;
  timestamp: string; // ISO 8601
  agent: string;
  details: EventDetails;
  feedback_card_id: string | null;
  step_uncertainty: import("./uncertainty").StepUncertainty | null;
  citation_index: number | null;
}

export interface AttributionRecord {
  schema_version: string;
  attribution_id: string;
  work_entity_id: string;
  work_title: string; // Display field (frontend addition)
  artist_name: string; // Display field (frontend addition)
  credits: Credit[];
  assurance_level: AssuranceLevel;
  confidence_score: number;
  conformal_set: ConformalSet;
  source_agreement: number;
  provenance_chain: ProvenanceEvent[];
  uncertainty_summary: import("./uncertainty").UncertaintyAwareProvenance | null;
  needs_review: boolean;
  review_priority: number;
  created_at: string; // ISO 8601
  updated_at: string; // ISO 8601
  version: number;
}
