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
      className={`inline-flex items-center editorial-caps text-xs border-b-2 pb-[1px] ${className}`}
      style={{
        borderColor: color,
        color,
      }}
    >
      {label}
    </span>
  );
}
