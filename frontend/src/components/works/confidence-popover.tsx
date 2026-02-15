"use client";

import { useState, useRef, useCallback } from "react";
import type { ConformalSet } from "@/lib/types/attribution";
import { getConfidenceTier, getConfidenceCssVar } from "@/lib/theme/confidence";

interface ConfidencePopoverProps {
  score: number;
  conformalSet: ConformalSet;
  children: React.ReactNode;
  onView?: () => void;
}

/**
 * Popover showing conformal prediction details on hover.
 * Wraps children and shows popover on mouseenter, hides on mouseleave.
 */
export function ConfidencePopover({
  score,
  conformalSet,
  children,
  onView,
}: ConfidencePopoverProps) {
  const [visible, setVisible] = useState(false);
  const timerRef = useRef<ReturnType<typeof setTimeout>>(null);
  const hasTracked = useRef(false);

  const handleMouseEnter = useCallback(() => {
    timerRef.current = setTimeout(() => {
      setVisible(true);
      if (!hasTracked.current) {
        hasTracked.current = true;
        onView?.();
      }
    }, 200);
  }, [onView]);

  const handleMouseLeave = useCallback(() => {
    if (timerRef.current) {
      clearTimeout(timerRef.current);
      timerRef.current = null;
    }
    setVisible(false);
  }, []);

  const tier = getConfidenceTier(score);
  const color = getConfidenceCssVar(tier);
  const setEntries = Object.entries(conformalSet.set_sizes);

  return (
    <div
      className="relative inline-block"
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      {children}

      {visible && (
        <div
          role="tooltip"
          data-testid="confidence-popover"
          className="absolute z-50 bottom-full left-0 mb-2 px-4 py-3 bg-surface-elevated border border-border shadow-md min-w-64"
        >
          <p className="editorial-caps text-xs text-label mb-2">
            Conformal Prediction
          </p>

          <div className="space-y-1.5 text-xs">
            <div className="flex justify-between">
              <span className="text-muted">Coverage level</span>
              <span className="data-mono" style={{ color }}>
                {Math.round(conformalSet.coverage_level * 100)}%
              </span>
            </div>

            <div className="flex justify-between">
              <span className="text-muted">Marginal coverage</span>
              <span className="data-mono" style={{ color }}>
                {Math.round(conformalSet.marginal_coverage * 100)}%
              </span>
            </div>

            <div className="flex justify-between">
              <span className="text-muted">Calibration error</span>
              <span className="data-mono text-body">
                {conformalSet.calibration_error.toFixed(3)}
              </span>
            </div>

            <div className="flex justify-between">
              <span className="text-muted">Calibration method</span>
              <span className="text-body">
                {conformalSet.calibration_method.replace(/_/g, " ")}
              </span>
            </div>

            {setEntries.length > 0 && (
              <>
                <div className="border-t border-border my-1.5" />
                <p className="text-muted">Prediction set sizes:</p>
                {setEntries.map(([entityId, size]) => (
                  <div key={entityId} className="flex justify-between pl-2">
                    <span className="text-muted truncate max-w-32">
                      {entityId.replace("artist-", "")}
                    </span>
                    <span className="data-mono text-body">{size}</span>
                  </div>
                ))}
              </>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
