"use client";

// TODO: Component not yet integrated — wire up during UI fine-tuning

import { useState, useEffect } from "react";
import { useAtomValue } from "jotai";
import { proficiencyLevelsAtom } from "@/lib/stores/proficiency";
import type { Skill } from "@/lib/stores/proficiency";
import { trackEvent, EVENTS } from "@/lib/analytics/events";

interface AdaptiveTooltipProps {
  id: string;
  skill: Skill;
  content: string;
  compactContent?: string;
  children: React.ReactNode;
}

/**
 * Adaptive tooltip that adjusts behavior based on user proficiency:
 * - Novice: full tooltip, auto-shown on mount
 * - Intermediate: compact tooltip, hover-only
 * - Expert: hidden entirely
 */
export function AdaptiveTooltip({
  id,
  skill,
  content,
  compactContent,
  children,
}: AdaptiveTooltipProps) {
  const levels = useAtomValue(proficiencyLevelsAtom);
  const level = levels[skill];
  const [visible, setVisible] = useState(false);
  const [dismissed, setDismissed] = useState(false);

  // Auto-show for novice users
  useEffect(() => {
    if (level === "novice" && !dismissed) {
      const timer = setTimeout(() => {
        setVisible(true);
        trackEvent(EVENTS.TOOLTIP_SHOWN, { tooltip_id: id, skill });
      }, 500);
      return () => clearTimeout(timer);
    }
  }, [level, dismissed, id, skill]);

  function handleDismiss() {
    setDismissed(true);
    setVisible(false);
    trackEvent(EVENTS.TOOLTIP_DISMISSED, { tooltip_id: id, skill });
  }

  // Expert: no tooltip
  if (level === "expert") {
    return <>{children}</>;
  }

  const displayContent = level === "intermediate" && compactContent ? compactContent : content;

  return (
    <div
      className="relative inline-block"
      onMouseEnter={() => level === "intermediate" && setVisible(true)}
      onMouseLeave={() => level === "intermediate" && setVisible(false)}
    >
      {children}

      {visible && (
        <div
          role="tooltip"
          className="absolute z-50 bottom-full left-0 mb-[var(--space-2)] px-[var(--space-3)] py-[var(--space-2)] bg-[var(--color-surface-elevated)] border border-[var(--color-border)] shadow-[var(--shadow-md)] text-xs text-[var(--color-body)] max-w-64"
        >
          <p>{displayContent}</p>
          {level === "novice" && (
            <button
              onClick={handleDismiss}
              className="mt-[var(--space-1)] text-[var(--color-accent)] underline underline-offset-2 text-xs"
            >
              Got it
            </button>
          )}
        </div>
      )}
    </div>
  );
}
