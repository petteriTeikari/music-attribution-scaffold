/**
 * Resolved entity types mirroring Python schemas from
 * src/music_attribution/schemas/resolved.py
 */

import type {
  AssuranceLevel,
  ConflictSeverity,
  EntityType,
  RelationshipType,
  ResolutionMethod,
  Source,
} from "./enums";

export interface SourceReference {
  record_id: string;
  source: Source;
  source_id: string;
  agreement_score: number;
}

export interface ResolutionDetails {
  string_similarity: number | null;
  embedding_similarity: number | null;
  graph_path_confidence: number | null;
  llm_confidence: number | null;
  matched_identifiers: string[];
}

export interface ResolvedRelationship {
  target_entity_id: string;
  relationship_type: RelationshipType;
  confidence: number;
  supporting_sources: Source[];
}

export interface Conflict {
  field: string;
  values: Record<string, string>;
  severity: ConflictSeverity;
}

export interface ResolvedEntity {
  schema_version: string;
  entity_id: string;
  entity_type: EntityType;
  canonical_name: string;
  alternative_names: string[];
  source_records: SourceReference[];
  resolution_method: ResolutionMethod;
  resolution_confidence: number;
  resolution_details: ResolutionDetails;
  assurance_level: AssuranceLevel;
  relationships: ResolvedRelationship[];
  conflicts: Conflict[];
  needs_review: boolean;
  review_reason: string | null;
  merged_from: string[] | null;
  resolved_at: string; // ISO 8601
}
