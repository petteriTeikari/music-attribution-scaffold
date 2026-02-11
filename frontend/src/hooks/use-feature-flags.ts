"use client";

import { useAtomValue } from "jotai";
import { overallProficiencyAtom, type ProficiencyLevel } from "@/lib/stores/proficiency";
import { posthog } from "@/lib/analytics/posthog-provider";

export type UiDensity = "comfortable" | "compact" | "dense";

interface FeatureFlags {
  showAgentSidebar: boolean;
  uiDensity: UiDensity;
  enableBatchReview: boolean;
  showAdaptiveTooltips: boolean;
}

const DENSITY_BY_PROFICIENCY: Record<ProficiencyLevel, UiDensity> = {
  novice: "comfortable",
  intermediate: "compact",
  expert: "dense",
};

/**
 * Feature flags with PostHog remote override + local proficiency fallback.
 *
 * PostHog feature flags are checked first. If not available (PostHog
 * not initialized), falls back to proficiency-based defaults.
 */
export function useFeatureFlags(): FeatureFlags {
  const proficiency = useAtomValue(overallProficiencyAtom);

  // Try PostHog feature flags first, fall back to proficiency-based defaults
  const showAgentSidebar = getFlag("show_agent_sidebar", true);
  const uiDensity = getStringFlag("ui_density", DENSITY_BY_PROFICIENCY[proficiency]) as UiDensity;
  const enableBatchReview = getFlag("enable_batch_review", proficiency !== "novice");
  const showAdaptiveTooltips = getFlag("show_adaptive_tooltips", proficiency !== "expert");

  return {
    showAgentSidebar,
    uiDensity,
    enableBatchReview,
    showAdaptiveTooltips,
  };
}

function getFlag(key: string, fallback: boolean): boolean {
  try {
    const value = posthog.getFeatureFlag(key);
    if (typeof value === "boolean") return value;
    if (value === "true") return true;
    if (value === "false") return false;
  } catch {
    // PostHog not initialized
  }
  return fallback;
}

function getStringFlag(key: string, fallback: string): string {
  try {
    const value = posthog.getFeatureFlag(key);
    if (typeof value === "string" && value.length > 0) return value;
  } catch {
    // PostHog not initialized
  }
  return fallback;
}
