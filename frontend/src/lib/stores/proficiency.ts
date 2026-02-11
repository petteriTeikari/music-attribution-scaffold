/**
 * Proficiency model for adaptive UI.
 *
 * Tracks per-skill interaction counts and success rates to determine
 * the user's proficiency level. Used by adaptive tooltips and
 * feature flag-driven UI density.
 *
 * Levels:
 * - novice: <10 interactions
 * - intermediate: 10-50 interactions + 60% success rate
 * - expert: 50+ interactions + 75% success rate
 */

import { atom } from "jotai";
import { atomWithStorage } from "jotai/utils";

export type ProficiencyLevel = "novice" | "intermediate" | "expert";

export type Skill = "review" | "feedback" | "confidence_reading";

export interface SkillMetrics {
  interactions: number;
  successes: number;
}

export type ProficiencyState = Record<Skill, SkillMetrics>;

const DEFAULT_STATE: ProficiencyState = {
  review: { interactions: 0, successes: 0 },
  feedback: { interactions: 0, successes: 0 },
  confidence_reading: { interactions: 0, successes: 0 },
};

/**
 * Persisted proficiency state — survives page reloads.
 */
export const proficiencyStateAtom = atomWithStorage<ProficiencyState>(
  "ma-proficiency",
  DEFAULT_STATE,
);

/**
 * Compute proficiency level for a given skill.
 */
export function computeLevel(metrics: SkillMetrics): ProficiencyLevel {
  const { interactions, successes } = metrics;
  const successRate = interactions > 0 ? successes / interactions : 0;

  if (interactions >= 50 && successRate >= 0.75) return "expert";
  if (interactions >= 10 && successRate >= 0.6) return "intermediate";
  return "novice";
}

/**
 * Derived atom: current proficiency level per skill.
 */
export const proficiencyLevelsAtom = atom((get) => {
  const state = get(proficiencyStateAtom);
  return {
    review: computeLevel(state.review),
    feedback: computeLevel(state.feedback),
    confidence_reading: computeLevel(state.confidence_reading),
  } satisfies Record<Skill, ProficiencyLevel>;
});

/**
 * Derived atom: overall proficiency (max of individual skills).
 */
export const overallProficiencyAtom = atom((get) => {
  const levels = get(proficiencyLevelsAtom);
  const order: ProficiencyLevel[] = ["novice", "intermediate", "expert"];
  const maxIdx = Math.max(
    ...Object.values(levels).map((l) => order.indexOf(l)),
  );
  return order[maxIdx] ?? "novice";
});
