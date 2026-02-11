"use client";

import type { AttributionRecord } from "@/lib/types/attribution";

interface SourceContribution {
  source: string;
  contribution: number;
  color: string;
}

interface ConfidenceExplanationProps {
  work: AttributionRecord;
}

function getSourceContributions(work: AttributionRecord): SourceContribution[] {
  const sourceMap: Record<string, { count: number; color: string }> = {
    MUSICBRAINZ: { count: 0, color: "var(--color-source-musicbrainz)" },
    DISCOGS: { count: 0, color: "var(--color-source-discogs)" },
    ACOUSTID: { count: 0, color: "var(--color-source-acoustid)" },
    ARTIST_INPUT: { count: 0, color: "var(--color-source-artist)" },
    FILE_METADATA: { count: 0, color: "var(--color-source-file)" },
  };

  for (const credit of work.credits) {
    for (const source of credit.sources) {
      if (sourceMap[source]) {
        sourceMap[source].count++;
      }
    }
  }

  const total = Object.values(sourceMap).reduce((sum, s) => sum + s.count, 0) || 1;

  return Object.entries(sourceMap)
    .filter(([, v]) => v.count > 0)
    .map(([source, v]) => ({
      source,
      contribution: v.count / total,
      color: v.color,
    }))
    .sort((a, b) => b.contribution - a.contribution);
}

function getConfidenceTier(score: number): { label: string; color: string } {
  if (score >= 0.85) return { label: "High", color: "var(--color-confidence-high)" };
  if (score >= 0.5) return { label: "Medium", color: "var(--color-confidence-medium)" };
  return { label: "Low", color: "var(--color-confidence-low)" };
}

export function ConfidenceExplanation({ work }: ConfidenceExplanationProps) {
  const contributions = getSourceContributions(work);
  const tier = getConfidenceTier(work.confidence_score);

  return (
    <div className="space-y-[var(--space-5)]">
      {/* Score summary */}
      <div className="flex items-center gap-[var(--space-4)]">
        <div className="accent-square-sm" aria-hidden="true" />
        <div>
          <span className="editorial-caps text-xs text-[var(--color-label)]">
            Confidence
          </span>
          <div className="flex items-baseline gap-[var(--space-2)]">
            <span
              className="text-2xl font-semibold data-mono"
              style={{ color: tier.color }}
            >
              {Math.round(work.confidence_score * 100)}%
            </span>
            <span className="text-sm" style={{ color: tier.color }}>
              {tier.label}
            </span>
          </div>
        </div>
      </div>

      {/* Source contribution bars */}
      <div>
        <p className="editorial-caps text-xs text-[var(--color-label)] mb-[var(--space-3)]">
          Source Contributions
        </p>
        <div className="space-y-[var(--space-2)]">
          {contributions.map((c) => (
            <div key={c.source} className="flex items-center gap-[var(--space-3)]">
              <span className="text-xs text-[var(--color-label)] w-28 data-mono">
                {c.source.replace("_", " ")}
              </span>
              <div className="flex-1 h-2 bg-[var(--color-surface-secondary)] relative">
                <div
                  className="absolute inset-y-0 left-0 transition-all duration-[var(--transition-slow)]"
                  style={{
                    width: `${c.contribution * 100}%`,
                    backgroundColor: c.color,
                  }}
                />
              </div>
              <span className="text-xs text-[var(--color-muted)] w-10 text-right data-mono">
                {Math.round(c.contribution * 100)}%
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Source agreement */}
      <div className="flex items-center gap-[var(--space-3)] pt-[var(--space-2)] border-t border-[var(--color-border)]">
        <span className="text-xs text-[var(--color-label)]">Source Agreement</span>
        <span className="text-sm font-medium data-mono" style={{ color: tier.color }}>
          {Math.round(work.source_agreement * 100)}%
        </span>
      </div>

      {/* Conformal set summary */}
      {work.conformal_set && (
        <div className="pt-[var(--space-2)] border-t border-[var(--color-border)]">
          <p className="editorial-caps text-xs text-[var(--color-label)] mb-[var(--space-2)]">
            Uncertainty (Conformal Set)
          </p>
          <div className="grid grid-cols-2 gap-[var(--space-2)] text-xs">
            <div>
              <span className="text-[var(--color-muted)]">Coverage</span>
              <span className="ml-[var(--space-2)] data-mono text-[var(--color-heading)]">
                {Math.round(work.conformal_set.coverage_level * 100)}%
              </span>
            </div>
            <div>
              <span className="text-[var(--color-muted)]">Cal. Error</span>
              <span className="ml-[var(--space-2)] data-mono text-[var(--color-heading)]">
                {work.conformal_set.calibration_error.toFixed(3)}
              </span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
