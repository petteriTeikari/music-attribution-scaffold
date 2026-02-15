"use client";

import { useEffect } from "react";

const POSTHOG_KEY = process.env.NEXT_PUBLIC_POSTHOG_KEY;
const POSTHOG_HOST = process.env.NEXT_PUBLIC_POSTHOG_HOST ?? "https://us.i.posthog.com";

/**
 * Module-level PostHog instance. Null until the dynamic import completes.
 * Consumers call getPostHogInstance() which gracefully returns null when
 * PostHog hasn't loaded yet (no env var, or still loading).
 *
 * Using Record<string, unknown> as the type since posthog-js types aren't
 * available until the dynamic import resolves.
 */
let posthogInstance: Record<string, unknown> | null = null;
let loadPromise: Promise<void> | null = null;

function loadPostHog(): Promise<void> {
  if (!loadPromise) {
    loadPromise = import("posthog-js").then(({ default: posthog }) => {
      posthogInstance = posthog as unknown as Record<string, unknown>;
      if (POSTHOG_KEY && typeof window !== "undefined") {
        posthog.init(POSTHOG_KEY, {
          api_host: POSTHOG_HOST,
          person_profiles: "identified_only",
          capture_pageview: true,
          capture_pageleave: true,
        });
      }
    });
  }
  return loadPromise;
}

/**
 * Get the PostHog instance if loaded. Returns null if not yet available.
 * Callers should handle null gracefully (all feature flag and event
 * functions already do this).
 */
export function getPostHogInstance(): Record<string, unknown> | null {
  return posthogInstance;
}

export function PostHogProvider({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    if (!POSTHOG_KEY || typeof window === "undefined") return;
    loadPostHog();
  }, []);

  return <>{children}</>;
}
