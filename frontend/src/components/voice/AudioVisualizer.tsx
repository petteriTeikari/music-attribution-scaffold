"use client";

import { useAtomValue } from "jotai";
import { useEffect, useRef } from "react";

import { voiceStateAtom } from "@/lib/stores/voice";

/* ── Props ───────────────────────────────────────────────────── */

interface AudioVisualizerProps {
  /** Canvas width in pixels. */
  width?: number;
  /** Canvas height in pixels. */
  height?: number;
  /** Additional CSS classes. */
  className?: string;
  /** If true, the canvas is decorative (hidden from screen readers). */
  decorative?: boolean;
}

/* ── Component ───────────────────────────────────────────────── */

export function AudioVisualizer({
  width = 200,
  height = 60,
  className = "",
  decorative = false,
}: AudioVisualizerProps) {
  const voiceState = useAtomValue(voiceStateAtom);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const rafRef = useRef<number>(0);

  useEffect(() => {
    // Check prefers-reduced-motion inside effect (not available in SSR/jsdom render)
    const prefersReduced =
      typeof window !== "undefined" &&
      typeof window.matchMedia === "function" &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    // Hoist color reads outside RAF loop (only changes on theme switch → re-render)
    const computedStyle = getComputedStyle(document.documentElement);
    const accentColor =
      computedStyle.getPropertyValue("--color-accent").trim() ||
      "currentColor";
    const mutedColor =
      computedStyle.getPropertyValue("--color-muted").trim() ||
      "currentColor";

    const barCount = 12;
    const barWidth = width / (barCount * 2);
    const isActive = voiceState === "recording" || voiceState === "playing";

    const drawBars = () => {
      ctx.clearRect(0, 0, width, height);
      ctx.fillStyle = isActive ? accentColor : mutedColor;

      for (let i = 0; i < barCount; i++) {
        const x = i * (barWidth + barWidth);
        let barHeight: number;

        if (!isActive || prefersReduced) {
          // Flat line for idle / reduced-motion
          barHeight = 2;
        } else {
          // Simulated waveform bars
          barHeight =
            Math.abs(Math.sin(Date.now() * 0.005 + i * 0.5)) *
              (height * 0.7) +
            4;
        }

        const y = (height - barHeight) / 2;
        ctx.fillRect(x, y, barWidth, barHeight);
      }

      if (isActive && !prefersReduced) {
        rafRef.current = requestAnimationFrame(drawBars);
      }
    };

    drawBars();

    return () => {
      if (rafRef.current) {
        cancelAnimationFrame(rafRef.current);
      }
    };
  }, [voiceState, width, height]);

  if (decorative) {
    return (
      <div className={className}>
        <canvas
          ref={canvasRef}
          width={width}
          height={height}
          aria-hidden="true"
        />
      </div>
    );
  }

  return (
    <div className={className}>
      <canvas
        ref={canvasRef}
        width={width}
        height={height}
        role="img"
        aria-label="Audio visualization"
      />
    </div>
  );
}
