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
  sm: { width: 48, strokeWidth: 4, fontSize: "var(--text-sm)", labelSize: "var(--text-xs)" },
  md: { width: 80, strokeWidth: 6, fontSize: "var(--text-xl)", labelSize: "var(--text-sm)" },
  lg: { width: 140, strokeWidth: 8, fontSize: "var(--text-3xl)", labelSize: "var(--text-base)" },
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
  // Arc spans 270 degrees (¾ circle)
  const arcLength = (270 / 360) * circumference;
  const filledLength = arcLength * displayScore;
  const dashOffset = arcLength - filledLength;

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
        {/* Background track */}
        <circle
          cx={config.width / 2}
          cy={config.width / 2}
          r={radius}
          fill="none"
          stroke="var(--color-border)"
          strokeWidth={config.strokeWidth}
          strokeDasharray={`${arcLength} ${circumference}`}
          strokeLinecap="round"
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
            strokeLinecap="round"
          />
        )}
      </svg>
      {/* Center score */}
      <div
        className="absolute flex flex-col items-center justify-center"
        style={{
          width: config.width,
          height: config.width,
        }}
      >
        <span
          className="font-bold"
          style={{ fontSize: config.fontSize, color }}
        >
          {Math.round(displayScore * 100)}
        </span>
      </div>
      {/* Label below */}
      {showLabel && (
        <span
          className="mt-[var(--space-1)] font-medium"
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
      className={`inline-flex items-center gap-[var(--space-1)] rounded-[var(--radius-full)] px-[var(--space-3)] py-[var(--space-1)] text-[var(--text-xs)] font-medium ${className}`}
      style={{
        backgroundColor: `color-mix(in srgb, ${color} 12%, transparent)`,
        color,
      }}
    >
      <span
        className="h-1.5 w-1.5 rounded-full"
        style={{ backgroundColor: color }}
        aria-hidden="true"
      />
      {Math.round(score * 100)}% — {label}
    </span>
  );
}
