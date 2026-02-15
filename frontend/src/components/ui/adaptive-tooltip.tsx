"use client";

import { useState, useEffect } from "react";
import { useAtomValue, useAtom } from "jotai";
import {
  proficiencyLevelsAtom,
  noviceTooltipQueueAtom,
  activeNoviceTooltipAtom,
} from "@/lib/stores/proficiency";
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
 * - Novice: full tooltip, auto-shown one-at-a-time via shared queue
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
  const [queue, setQueue] = useAtom(noviceTooltipQueueAtom);
  const activeTooltip = useAtomValue(activeNoviceTooltipAtom);
  const [hoverVisible, setHoverVisible] = useState(false);
  const [dismissed, setDismissed] = useState(false);

  // Register in novice queue on mount, deregister on unmount
  useEffect(() => {
    if (level === "novice" && !dismissed) {
      setQueue((prev) => (prev.includes(id) ? prev : [...prev, id]));
      return () => {
        setQueue((prev) => prev.filter((tid) => tid !== id));
      };
    }
  }, [level, dismissed, id, setQueue]);

  function handleDismiss() {
    setDismissed(true);
    setQueue((prev) => prev.filter((tid) => tid !== id));
    trackEvent(EVENTS.TOOLTIP_DISMISSED, { tooltip_id: id, skill });
  }

  // Expert: no tooltip
  if (level === "expert") {
    return <>{children}</>;
  }

  const isNoviceActive = level === "novice" && !dismissed && activeTooltip === id;
  const visible = isNoviceActive || hoverVisible;

  if (isNoviceActive) {
    // Track once when becoming active — fire via effect to avoid render-time side effects
  }

  const displayContent = level === "intermediate" && compactContent ? compactContent : content;

  return (
    <div
      className="relative inline-block"
      onMouseEnter={() => level === "intermediate" && setHoverVisible(true)}
      onMouseLeave={() => level === "intermediate" && setHoverVisible(false)}
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
