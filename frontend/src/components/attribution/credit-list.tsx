import type { Credit, ProvenanceEvent } from "@/lib/types/attribution";
import type { CitationReference } from "@/lib/types/uncertainty";
import { AssuranceBadge } from "@/components/works/assurance-badge";
import { SourceTag } from "@/components/works/source-tag";
import { InlineCitation } from "@/components/citations/inline-citation";
import type { Source } from "@/lib/types/enums";

interface CreditListProps {
  credits: Credit[];
  provenanceEvents?: ProvenanceEvent[];
  className?: string;
}

function formatRole(role: string): string {
  return role
    .split("_")
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase())
    .join(" ");
}

function buildCitationsForSources(
  sources: Source[],
  events: ProvenanceEvent[]
): CitationReference[] {
  const citations: CitationReference[] = [];
  for (const source of sources) {
    const matchingEvent = events.find(
      (e) =>
        e.details.type === "fetch" &&
        e.details.source === source &&
        e.citation_index !== null
    );
    if (matchingEvent && matchingEvent.citation_index !== null) {
      const fetchDetails = matchingEvent.details as { source: Source };
      citations.push({
        index: matchingEvent.citation_index,
        source: fetchDetails.source,
        confidence: 1.0,
        label: source.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase()),
        detail: `via ${matchingEvent.agent}`,
        timestamp: matchingEvent.timestamp,
      });
    }
  }
  return citations;
}

export function CreditList({ credits, provenanceEvents, className = "" }: CreditListProps) {
  return (
    <div className={className}>
      <h3 className="text-base font-semibold text-[var(--color-heading)] mb-[var(--space-4)]">
        Credits
      </h3>
      <ul className="space-y-[var(--space-3)]">
        {credits.map((credit, index) => (
          <li
            key={`${credit.entity_id}-${credit.role}-${index}`}
            className="rounded-[var(--radius-md)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-4)]"
          >
            <div className="flex items-start justify-between gap-[var(--space-3)]">
              <div className="min-w-0 flex-1">
                <div className="flex items-center gap-[var(--space-2)]">
                  <span className="font-medium text-[var(--color-heading)]">
                    {credit.entity_name}
                  </span>
                  <span className="text-sm text-[var(--color-label)]">
                    {formatRole(credit.role)}
                  </span>
                </div>
                {credit.role_detail && (
                  <p className="mt-[var(--space-1)] text-sm text-[var(--color-muted)]">
                    {credit.role_detail}
                  </p>
                )}
                <div className="mt-[var(--space-2)] flex flex-wrap items-center gap-[var(--space-2)]">
                  <AssuranceBadge level={credit.assurance_level} />
                  {credit.sources.map((source) => (
                    <SourceTag key={source} source={source} />
                  ))}
                  {provenanceEvents &&
                    buildCitationsForSources(credit.sources, provenanceEvents).map(
                      (citation) => (
                        <InlineCitation
                          key={citation.index}
                          citation={citation}
                        />
                      )
                    )}
                </div>
              </div>

              <div className="text-right">
                <span className="text-lg font-bold text-[var(--color-heading)]">
                  {Math.round(credit.confidence * 100)}%
                </span>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
