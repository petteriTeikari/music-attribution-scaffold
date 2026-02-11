import {
  ASSURANCE_LABELS,
  getAssuranceCssVar,
} from "@/lib/theme/confidence";
import type { AssuranceLevel } from "@/lib/types/enums";

interface AssuranceBadgeProps {
  level: AssuranceLevel;
  className?: string;
}

export function AssuranceBadge({ level, className = "" }: AssuranceBadgeProps) {
  const color = getAssuranceCssVar(level);
  const label = ASSURANCE_LABELS[level] ?? level;

  return (
    <span
      className={`inline-flex items-center gap-[var(--space-1)] rounded-[var(--radius-sm)] px-[var(--space-2)] py-[var(--space-1)] text-[var(--text-xs)] font-medium ${className}`}
      style={{
        backgroundColor: `color-mix(in srgb, ${color} 12%, transparent)`,
        color,
      }}
    >
      {label}
    </span>
  );
}
