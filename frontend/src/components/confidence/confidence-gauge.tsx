"use client";

import { useEffect, useRef, useState } from "react";
import {
  getConfidenceTier,
  getConfidenceLabel,
  getConfidenceCssVar,
  type ConfidenceTier,
} from "@/lib/theme/confidence";

type GaugeSize = "sm" | "md" | "lg";

interface ConfidenceGaugeProps {
  score: number;
  size?: GaugeSize;
  animate?: boolean;
  showLabel?: boolean;
  className?: string;
}

const SIZE_CONFIG: Record<
  GaugeSize,
  { width: number; strokeWidth: number; fontSize: string; labelSize: string }
> = {
  sm: { width: 48, strokeWidth: 3, fontSize: "0.875rem", labelSize: "0.75rem" },
  md: { width: 80, strokeWidth: 4, fontSize: "1.25rem", labelSize: "0.875rem" },
  lg: { width: 140, strokeWidth: 5, fontSize: "1.875rem", labelSize: "1rem" },
};

export function ConfidenceGauge({
  score,
  size = "md",
  animate = true,
  showLabel = true,
  className = "",
}: ConfidenceGaugeProps) {
  const [displayScore, setDisplayScore] = useState(animate ? 0 : score);
  const hasAnimated = useRef(false);
  const tier = getConfidenceTier(score);
  const config = SIZE_CONFIG[size];

  const radius = (config.width - config.strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;
  // Arc spans 270 degrees (3/4 circle)
  const arcLength = (270 / 360) * circumference;
  const filledLength = arcLength * displayScore;

  // Mount animation
  useEffect(() => {
    if (!animate || hasAnimated.current) return;

    const prefersReduced = window.matchMedia(
      "(prefers-reduced-motion: reduce)"
    ).matches;

    if (prefersReduced) {
      setDisplayScore(score);
      hasAnimated.current = true;
      return;
    }

    hasAnimated.current = true;
    const duration = 800;
    const start = performance.now();

    function step(now: number) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      // Ease-out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      setDisplayScore(score * eased);
      if (progress < 1) {
        requestAnimationFrame(step);
      }
    }

    requestAnimationFrame(step);
  }, [score, animate]);

  // Update when score prop changes (non-animated updates)
  useEffect(() => {
    if (hasAnimated.current) {
      setDisplayScore(score);
    }
  }, [score]);

  const color = getConfidenceCssVar(tier);
  const label = getConfidenceLabel(score);
  const percentage = Math.round(score * 100);

  return (
    <div
      className={`inline-flex flex-col items-center ${className}`}
      role="meter"
      aria-valuenow={percentage}
      aria-valuemin={0}
      aria-valuemax={100}
      aria-label={`Confidence: ${percentage}% — ${label}`}
    >
      <svg
        width={config.width}
        height={config.width}
        viewBox={`0 0 ${config.width} ${config.width}`}
        className="transform -rotate-[135deg]"
      >
        {/* Background track — thin, minimal */}
        <circle
          cx={config.width / 2}
          cy={config.width / 2}
          r={radius}
          fill="none"
          stroke="var(--color-border)"
          strokeWidth={config.strokeWidth}
          strokeDasharray={`${arcLength} ${circumference}`}
          strokeLinecap="butt"
        />
        {/* Filled arc */}
        {displayScore > 0 && (
          <circle
            cx={config.width / 2}
            cy={config.width / 2}
            r={radius}
            fill="none"
            stroke={color}
            strokeWidth={config.strokeWidth}
            strokeDasharray={`${filledLength} ${circumference}`}
            strokeDashoffset={0}
            strokeLinecap="butt"
          />
        )}
      </svg>
      {/* Center score — editorial display font */}
      <div
        className="absolute flex flex-col items-center justify-center"
        style={{
          width: config.width,
          height: config.width,
        }}
      >
        <span
          className="editorial-display"
          style={{ fontSize: config.fontSize, color }}
        >
          {Math.round(displayScore * 100)}
        </span>
      </div>
      {/* Label below */}
      {showLabel && (
        <span
          className="mt-1 editorial-caps"
          style={{
            fontSize: config.labelSize,
            color,
          }}
        >
          {label}
        </span>
      )}
    </div>
  );
}

export function ConfidenceBadge({
  score,
  className = "",
}: {
  score: number;
  className?: string;
}) {
  const tier = getConfidenceTier(score);
  const color = getConfidenceCssVar(tier);
  const label = getConfidenceLabel(score);

  return (
    <span
      className={`inline-flex items-center gap-2 editorial-caps text-xs ${className}`}
      style={{ color }}
    >
      <span
        className="h-1.5 w-1.5"
        style={{ backgroundColor: color }}
        aria-hidden="true"
      />
      {Math.round(score * 100)}% — {label}
    </span>
  );
}
