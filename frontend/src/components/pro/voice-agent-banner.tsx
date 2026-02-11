"use client";

import { useState } from "react";

export function VoiceAgentBanner() {
  const [dismissed, setDismissed] = useState(false);

  if (dismissed) return null;

  return (
    <div className="mx-auto max-w-4xl px-[var(--space-6)]">
      <div className="relative overflow-hidden rounded-[var(--radius-lg)] border border-[var(--color-accent)] bg-[var(--color-accent-muted)] p-[var(--space-6)]">
        <button
          onClick={() => setDismissed(true)}
          className="absolute right-[var(--space-3)] top-[var(--space-3)] text-[var(--color-muted)] hover:text-[var(--color-body)] transition-colors"
          aria-label="Dismiss"
        >
          ×
        </button>

        <div className="flex items-center gap-[var(--space-6)]">
          {/* Mic animation */}
          <div className="flex-shrink-0">
            <div
              className="flex h-12 w-12 items-center justify-center rounded-full"
              style={{
                backgroundColor: "var(--color-accent)",
                color: "white",
              }}
            >
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
            </div>
          </div>

          <div className="flex-1">
            <h3 className="text-base font-semibold text-[var(--color-heading)]">
              Voice Agent — Pro Feature
            </h3>
            <p className="mt-[var(--space-1)] text-sm text-[var(--color-body)]">
              Ask questions about your attributions by voice.{" "}
              <span className="italic text-[var(--color-muted)]">
                &ldquo;Who produced Hide and Seek?&rdquo;
              </span>
            </p>
          </div>

          <button
            className="flex-shrink-0 rounded-[var(--radius-md)] px-[var(--space-4)] py-[var(--space-2)] text-sm font-medium transition-colors duration-[var(--transition-fast)]"
            style={{
              backgroundColor: "var(--color-accent)",
              color: "white",
            }}
            onClick={() => {
              /* Pro upsell modal would open here */
            }}
          >
            Upgrade to Pro
          </button>
        </div>
      </div>
    </div>
  );
}
