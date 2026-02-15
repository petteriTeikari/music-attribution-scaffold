/**
 * PlatformBadge — colored dot + platform type label.
 *
 * Used in audit log rows and MCP scenario cards to visually
 * distinguish platform categories (AI generator, LLM provider, etc.).
 */

import { PlatformType } from "@/lib/types/enums";

const PLATFORM_LABELS: Record<
  (typeof PlatformType)[keyof typeof PlatformType],
  string
> = {
  [PlatformType.AI_GENERATOR]: "AI Generator",
  [PlatformType.ATTRIBUTION_INFRA]: "Attribution",
  [PlatformType.LLM_PROVIDER]: "LLM Provider",
  [PlatformType.STREAMING]: "Streaming",
  [PlatformType.RIGHTS_ORG]: "Rights Org",
  [PlatformType.LICENSING_BODY]: "Licensing",
  [PlatformType.CERTIFICATION_BODY]: "Certification",
  [PlatformType.REGISTRY]: "Registry",
  [PlatformType.INDIVIDUAL]: "Individual",
};

const PLATFORM_COLOR_VARS: Record<
  (typeof PlatformType)[keyof typeof PlatformType],
  string
> = {
  [PlatformType.AI_GENERATOR]: "var(--color-platform-ai-generator)",
  [PlatformType.ATTRIBUTION_INFRA]: "var(--color-platform-attribution)",
  [PlatformType.LLM_PROVIDER]: "var(--color-platform-llm-provider)",
  [PlatformType.STREAMING]: "var(--color-platform-streaming)",
  [PlatformType.RIGHTS_ORG]: "var(--color-platform-rights-org)",
  [PlatformType.LICENSING_BODY]: "var(--color-platform-rights-org)",
  [PlatformType.CERTIFICATION_BODY]: "var(--color-platform-certification)",
  [PlatformType.REGISTRY]: "var(--color-platform-registry)",
  [PlatformType.INDIVIDUAL]: "var(--color-platform-individual)",
};

interface PlatformBadgeProps {
  type: (typeof PlatformType)[keyof typeof PlatformType];
  className?: string;
}

export function PlatformBadge({ type, className = "" }: PlatformBadgeProps) {
  const color = PLATFORM_COLOR_VARS[type];
  const label = PLATFORM_LABELS[type];

  return (
    <span
      className={`inline-flex items-center gap-1.5 text-xs text-muted ${className}`}
    >
      <span
        className="inline-block h-2 w-2 flex-shrink-0 rounded-full"
        style={{ backgroundColor: color }}
        aria-hidden="true"
      />
      <span className="editorial-caps" style={{ fontSize: "10px" }}>
        {label}
      </span>
    </span>
  );
}
