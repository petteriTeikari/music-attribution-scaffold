/**
 * Feedback types mirroring Python schemas from
 * src/music_attribution/schemas/feedback.py
 */

import type { EvidenceType, ReviewerRole } from "./enums";

export interface Correction {
  field: string;
  current_value: string;
  corrected_value: string;
  entity_id: string | null;
  confidence_in_correction: number;
  evidence: string | null;
}

export interface FeedbackCard {
  schema_version: string;
  feedback_id: string;
  attribution_id: string;
  reviewer_id: string;
  reviewer_role: ReviewerRole;
  attribution_version: number;
  corrections: Correction[];
  overall_assessment: number;
  center_bias_flag: boolean;
  free_text: string | null;
  evidence_type: EvidenceType;
  submitted_at: string; // ISO 8601
}
