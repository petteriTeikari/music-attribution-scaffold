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
  placement?: "top" | "right";
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
  placement = "top",
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
          className={`absolute z-50 px-3 py-2 bg-surface-elevated border border-border shadow-md text-xs text-body max-w-64 ${
            placement === "right"
              ? "left-full top-0 ml-2"
              : "bottom-full left-0 mb-2"
          }`}
        >
          <p>{displayContent}</p>
          {level === "novice" && (
            <button
              onClick={handleDismiss}
              className="mt-1 text-accent underline underline-offset-2 text-xs"
            >
              Got it
            </button>
          )}
        </div>
      )}
    </div>
  );
}
