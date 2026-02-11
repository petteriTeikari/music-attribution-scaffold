import type { Credit } from "@/lib/types/attribution";
import { AssuranceBadge } from "@/components/works/assurance-badge";
import { SourceTag } from "@/components/works/source-tag";

interface CreditListProps {
  credits: Credit[];
  className?: string;
}

function formatRole(role: string): string {
  return role
    .split("_")
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase())
    .join(" ");
}

export function CreditList({ credits, className = "" }: CreditListProps) {
  return (
    <div className={className}>
      <h3 className="text-[var(--text-base)] font-semibold text-[var(--color-heading)] mb-[var(--space-4)]">
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
                  <span className="text-[var(--text-sm)] text-[var(--color-label)]">
                    {formatRole(credit.role)}
                  </span>
                </div>
                {credit.role_detail && (
                  <p className="mt-[var(--space-1)] text-[var(--text-sm)] text-[var(--color-muted)]">
                    {credit.role_detail}
                  </p>
                )}
                <div className="mt-[var(--space-2)] flex flex-wrap items-center gap-[var(--space-2)]">
                  <AssuranceBadge level={credit.assurance_level} />
                  {credit.sources.map((source) => (
                    <SourceTag key={source} source={source} />
                  ))}
                </div>
              </div>

              <div className="text-right">
                <span className="text-[var(--text-lg)] font-bold text-[var(--color-heading)]">
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
