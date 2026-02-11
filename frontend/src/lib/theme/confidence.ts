/**
 * Confidence tier utilities.
 *
 * Thresholds:
 *   HIGH   ≥ 0.85
 *   MEDIUM 0.50–0.84
 *   LOW    < 0.50
 */

export type ConfidenceTier = "high" | "medium" | "low";

export function getConfidenceTier(score: number): ConfidenceTier {
  if (score >= 0.85) return "high";
  if (score >= 0.5) return "medium";
  return "low";
}

export function getConfidenceLabel(score: number): string {
  const tier = getConfidenceTier(score);
  const labels: Record<ConfidenceTier, string> = {
    high: "High Confidence",
    medium: "Medium Confidence",
    low: "Low Confidence",
  };
  return labels[tier];
}

export function getConfidenceCssVar(tier: ConfidenceTier): string {
  return `var(--color-confidence-${tier})`;
}

export function getConfidenceBgCssVar(tier: ConfidenceTier): string {
  return `var(--color-confidence-${tier}-bg)`;
}

export const ASSURANCE_LABELS: Record<string, string> = {
  LEVEL_0: "A0 — No Data",
  LEVEL_1: "A1 — Single Source",
  LEVEL_2: "A2 — Multi-Source",
  LEVEL_3: "A3 — Artist Verified",
};

export function getAssuranceCssVar(level: string): string {
  const map: Record<string, string> = {
    LEVEL_0: "var(--color-assurance-a0)",
    LEVEL_1: "var(--color-assurance-a1)",
    LEVEL_2: "var(--color-assurance-a2)",
    LEVEL_3: "var(--color-assurance-a3)",
  };
  return map[level] ?? "var(--color-assurance-a0)";
}

export function getSourceCssVar(source: string): string {
  const map: Record<string, string> = {
    MUSICBRAINZ: "var(--color-source-musicbrainz)",
    DISCOGS: "var(--color-source-discogs)",
    ACOUSTID: "var(--color-source-acoustid)",
    ARTIST_INPUT: "var(--color-source-artist)",
    FILE_METADATA: "var(--color-source-file)",
  };
  return map[source] ?? "var(--color-source-system)";
}
