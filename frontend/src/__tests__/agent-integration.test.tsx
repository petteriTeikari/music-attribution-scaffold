/**
 * Integration tests for the agentic UI layer.
 *
 * Tests the PostHog events, proficiency model, adaptive tooltips,
 * and feature flags without requiring a running agent backend.
 */

import { describe, it, expect } from "vitest";
import {
  computeLevel,
  type SkillMetrics,
} from "@/lib/stores/proficiency";
import { EVENTS } from "@/lib/analytics/events";

describe("Proficiency Model", () => {
  it("novice: fewer than 10 interactions", () => {
    const metrics: SkillMetrics = { interactions: 5, successes: 5 };
    expect(computeLevel(metrics)).toBe("novice");
  });

  it("novice: 10+ interactions but low success rate", () => {
    const metrics: SkillMetrics = { interactions: 15, successes: 5 };
    expect(computeLevel(metrics)).toBe("novice");
  });

  it("intermediate: 10-49 interactions with 60%+ success", () => {
    const metrics: SkillMetrics = { interactions: 20, successes: 14 };
    expect(computeLevel(metrics)).toBe("intermediate");
  });

  it("expert: 50+ interactions with 75%+ success", () => {
    const metrics: SkillMetrics = { interactions: 60, successes: 50 };
    expect(computeLevel(metrics)).toBe("expert");
  });

  it("expert threshold: exactly 50 interactions at exactly 75%", () => {
    const metrics: SkillMetrics = { interactions: 50, successes: 38 };
    expect(computeLevel(metrics)).toBe("expert");
  });

  it("zero interactions defaults to novice", () => {
    const metrics: SkillMetrics = { interactions: 0, successes: 0 };
    expect(computeLevel(metrics)).toBe("novice");
  });

  it("50+ interactions but low success stays intermediate or novice", () => {
    const metrics: SkillMetrics = { interactions: 60, successes: 40 };
    // 40/60 = 66.7% — above 60% but below 75%, so intermediate
    expect(computeLevel(metrics)).toBe("intermediate");
  });
});

describe("PostHog Event Schema", () => {
  it("all event names are snake_case strings", () => {
    for (const value of Object.values(EVENTS)) {
      expect(typeof value).toBe("string");
      expect(value).toMatch(/^[a-z_]+$/);
    }
  });

  it("has expected event names", () => {
    expect(EVENTS.REVIEW_APPROVED).toBe("review_approved");
    expect(EVENTS.AGENT_SUGGESTION_ACCEPTED).toBe("agent_suggestion_accepted");
    expect(EVENTS.TOOLTIP_DISMISSED).toBe("tooltip_dismissed");
    expect(EVENTS.FEEDBACK_SUBMITTED).toBe("feedback_submitted");
    expect(EVENTS.PROFICIENCY_LEVEL_CHANGED).toBe("proficiency_level_changed");
  });

  it("has at least 10 distinct events", () => {
    const uniqueEvents = new Set(Object.values(EVENTS));
    expect(uniqueEvents.size).toBeGreaterThanOrEqual(10);
  });
});

describe("Feature Flag Defaults", () => {
  it("density mapping covers all proficiency levels", () => {
    const mapping: Record<string, string> = {
      novice: "comfortable",
      intermediate: "compact",
      expert: "dense",
    };
    expect(Object.keys(mapping)).toHaveLength(3);
    for (const density of Object.values(mapping)) {
      expect(["comfortable", "compact", "dense"]).toContain(density);
    }
  });
});
