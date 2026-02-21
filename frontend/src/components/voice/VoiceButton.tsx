"use client";

import { useAtom } from "jotai";
import { useCallback, useEffect, useRef } from "react";

import { voiceStateAtom, type VoiceState } from "@/lib/stores/voice";

/* ── Props ───────────────────────────────────────────────────── */

interface VoiceButtonProps {
  /** Additional CSS classes. */
  className?: string;
  /** Disable the button. */
  disabled?: boolean;
}

/* ── State labels ────────────────────────────────────────────── */

const STATE_LABELS: Record<VoiceState, string> = {
  idle: "Start voice input",
  recording: "Recording — tap to stop",
  processing: "Processing your request",
  playing: "Playing response",
};

const STATE_INDICATORS: Record<VoiceState, string> = {
  idle: "",
  recording: "Recording...",
  processing: "Processing...",
  playing: "Playing...",
};

/* ── Component ───────────────────────────────────────────────── */

export function VoiceButton({ className = "", disabled = false }: VoiceButtonProps) {
  const [voiceState, setVoiceState] = useAtom(voiceStateAtom);
  const streamRef = useRef<MediaStream | null>(null);

  // C2 fix: Clean up MediaStream on unmount to release microphone
  useEffect(() => {
    return () => {
      streamRef.current?.getTracks().forEach((t) => t.stop());
      streamRef.current = null;
    };
  }, []);

  const handleClick = useCallback(async () => {
    if (disabled) return;

    if (voiceState === "recording") {
      // Stop recording
      streamRef.current?.getTracks().forEach((t) => t.stop());
      streamRef.current = null;
      setVoiceState("idle");
      return;
    }

    // Start recording
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      streamRef.current = stream;
      setVoiceState("recording");
    } catch {
      // Permission denied or no mic — stay idle
      setVoiceState("idle");
    }
  }, [voiceState, setVoiceState, disabled]);

  const isActive = voiceState === "recording";
  const indicator = STATE_INDICATORS[voiceState];

  return (
    <div className={className}>
      <button
        type="button"
        onClick={handleClick}
        disabled={disabled}
        aria-label={STATE_LABELS[voiceState]}
        aria-pressed={isActive}
        className="relative flex min-w-11 min-h-11 items-center justify-center rounded-full transition-colors"
        style={{
          backgroundColor: isActive
            ? "var(--color-accent)"
            : "var(--color-surface-secondary)",
          color: isActive ? "white" : "var(--color-body)",
          transition: "var(--transition-base)",
        }}
      >
        {/* Mic SVG icon */}
        <svg
          width="20"
          height="20"
          viewBox="0 0 20 20"
          fill="none"
          aria-hidden="true"
        >
          <path
            d="M10 1a3 3 0 0 0-3 3v6a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3Z"
            fill="currentColor"
          />
          <path
            d="M5 9a5 5 0 0 0 10 0M10 15v4m-3 0h6"
            stroke="currentColor"
            strokeWidth="1.5"
            strokeLinecap="round"
          />
        </svg>
      </button>

      {/* State indicator text */}
      {indicator && (
        <span className="mt-1 block text-center text-xs text-muted">
          {indicator}
        </span>
      )}

      {/* Live region for screen readers */}
      <span aria-live="polite" className="sr-only">
        {STATE_LABELS[voiceState]}
      </span>
    </div>
  );
}
