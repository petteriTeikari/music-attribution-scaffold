/**
 * Shared enumerations mirroring Python StrEnums from
 * src/music_attribution/schemas/enums.py
 *
 * Using `as const` objects for tree-shaking + type safety.
 */

export const Source = {
  MUSICBRAINZ: "MUSICBRAINZ",
  DISCOGS: "DISCOGS",
  ACOUSTID: "ACOUSTID",
  ARTIST_INPUT: "ARTIST_INPUT",
  FILE_METADATA: "FILE_METADATA",
} as const;
export type Source = (typeof Source)[keyof typeof Source];

export const EntityType = {
  RECORDING: "RECORDING",
  WORK: "WORK",
  ARTIST: "ARTIST",
  RELEASE: "RELEASE",
  LABEL: "LABEL",
  CREDIT: "CREDIT",
} as const;
export type EntityType = (typeof EntityType)[keyof typeof EntityType];

export const RelationshipType = {
  PERFORMED: "PERFORMED",
  WROTE: "WROTE",
  PRODUCED: "PRODUCED",
  ENGINEERED: "ENGINEERED",
  ARRANGED: "ARRANGED",
  MASTERED: "MASTERED",
  MIXED: "MIXED",
  FEATURED: "FEATURED",
  SAMPLED: "SAMPLED",
  REMIXED: "REMIXED",
} as const;
export type RelationshipType =
  (typeof RelationshipType)[keyof typeof RelationshipType];

export const ResolutionMethod = {
  EXACT_ID: "EXACT_ID",
  FUZZY_STRING: "FUZZY_STRING",
  EMBEDDING: "EMBEDDING",
  GRAPH: "GRAPH",
  LLM: "LLM",
  MANUAL: "MANUAL",
} as const;
export type ResolutionMethod =
  (typeof ResolutionMethod)[keyof typeof ResolutionMethod];

export const AssuranceLevel = {
  LEVEL_0: "LEVEL_0",
  LEVEL_1: "LEVEL_1",
  LEVEL_2: "LEVEL_2",
  LEVEL_3: "LEVEL_3",
} as const;
export type AssuranceLevel =
  (typeof AssuranceLevel)[keyof typeof AssuranceLevel];

export const ConflictSeverity = {
  LOW: "LOW",
  MEDIUM: "MEDIUM",
  HIGH: "HIGH",
  CRITICAL: "CRITICAL",
} as const;
export type ConflictSeverity =
  (typeof ConflictSeverity)[keyof typeof ConflictSeverity];

export const CreditRole = {
  PERFORMER: "PERFORMER",
  SONGWRITER: "SONGWRITER",
  COMPOSER: "COMPOSER",
  LYRICIST: "LYRICIST",
  PRODUCER: "PRODUCER",
  ENGINEER: "ENGINEER",
  MIXING_ENGINEER: "MIXING_ENGINEER",
  MASTERING_ENGINEER: "MASTERING_ENGINEER",
  ARRANGER: "ARRANGER",
  SESSION_MUSICIAN: "SESSION_MUSICIAN",
  FEATURED_ARTIST: "FEATURED_ARTIST",
  CONDUCTOR: "CONDUCTOR",
  DJ: "DJ",
  REMIXER: "REMIXER",
} as const;
export type CreditRole = (typeof CreditRole)[keyof typeof CreditRole];

export const ProvenanceEventType = {
  FETCH: "FETCH",
  RESOLVE: "RESOLVE",
  SCORE: "SCORE",
  REVIEW: "REVIEW",
  UPDATE: "UPDATE",
  FEEDBACK: "FEEDBACK",
} as const;
export type ProvenanceEventType =
  (typeof ProvenanceEventType)[keyof typeof ProvenanceEventType];

export const ReviewerRole = {
  ARTIST: "ARTIST",
  MANAGER: "MANAGER",
  MUSICOLOGIST: "MUSICOLOGIST",
  PRODUCER: "PRODUCER",
  FAN: "FAN",
} as const;
export type ReviewerRole = (typeof ReviewerRole)[keyof typeof ReviewerRole];

export const EvidenceType = {
  LINER_NOTES: "LINER_NOTES",
  MEMORY: "MEMORY",
  DOCUMENT: "DOCUMENT",
  SESSION_NOTES: "SESSION_NOTES",
  OTHER: "OTHER",
} as const;
export type EvidenceType = (typeof EvidenceType)[keyof typeof EvidenceType];

export const PermissionType = {
  STREAM: "STREAM",
  DOWNLOAD: "DOWNLOAD",
  SYNC_LICENSE: "SYNC_LICENSE",
  AI_TRAINING: "AI_TRAINING",
  VOICE_CLONING: "VOICE_CLONING",
  STYLE_LEARNING: "STYLE_LEARNING",
  LYRICS_IN_CHATBOTS: "LYRICS_IN_CHATBOTS",
  COVER_VERSIONS: "COVER_VERSIONS",
  REMIX: "REMIX",
  SAMPLE: "SAMPLE",
  DERIVATIVE_WORK: "DERIVATIVE_WORK",
} as const;
export type PermissionType =
  (typeof PermissionType)[keyof typeof PermissionType];

export const PermissionValue = {
  ALLOW: "ALLOW",
  DENY: "DENY",
  ASK: "ASK",
  ALLOW_WITH_ATTRIBUTION: "ALLOW_WITH_ATTRIBUTION",
  ALLOW_WITH_ROYALTY: "ALLOW_WITH_ROYALTY",
} as const;
export type PermissionValue =
  (typeof PermissionValue)[keyof typeof PermissionValue];

export const PermissionScope = {
  CATALOG: "CATALOG",
  RELEASE: "RELEASE",
  RECORDING: "RECORDING",
  WORK: "WORK",
} as const;
export type PermissionScope =
  (typeof PermissionScope)[keyof typeof PermissionScope];

export const DelegationRole = {
  OWNER: "OWNER",
  MANAGER: "MANAGER",
  LABEL: "LABEL",
  DISTRIBUTOR: "DISTRIBUTOR",
} as const;
export type DelegationRole =
  (typeof DelegationRole)[keyof typeof DelegationRole];

export const PipelineFeedbackType = {
  REFETCH: "REFETCH",
  RECALIBRATE: "RECALIBRATE",
  DISPUTE: "DISPUTE",
  STALE: "STALE",
} as const;
export type PipelineFeedbackType =
  (typeof PipelineFeedbackType)[keyof typeof PipelineFeedbackType];
