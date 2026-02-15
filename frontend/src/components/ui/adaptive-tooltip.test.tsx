import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { Provider } from "jotai";
import { useHydrateAtoms } from "jotai/utils";
import type { ReactNode } from "react";
import { AdaptiveTooltip } from "./adaptive-tooltip";
import { proficiencyStateAtom } from "@/lib/stores/proficiency";
import type { ProficiencyState } from "@/lib/stores/proficiency";

// Mock PostHog
vi.mock("@/lib/analytics/events", () => ({
  trackEvent: vi.fn(),
  EVENTS: {
    TOOLTIP_SHOWN: "tooltip_shown",
    TOOLTIP_DISMISSED: "tooltip_dismissed",
  },
}));

function HydrateAtoms({
  initialValues,
  children,
}: {
  initialValues: [typeof proficiencyStateAtom, ProficiencyState][];
  children: ReactNode;
}) {
  useHydrateAtoms(initialValues);
  return children;
}

function TestProvider({
  state,
  children,
}: {
  state: ProficiencyState;
  children: ReactNode;
}) {
  return (
    <Provider>
      <HydrateAtoms initialValues={[[proficiencyStateAtom, state]]}>
        {children}
      </HydrateAtoms>
    </Provider>
  );
}

const INTERMEDIATE_STATE: ProficiencyState = {
  review: { interactions: 20, successes: 15 },
  feedback: { interactions: 20, successes: 15 },
  confidence_reading: { interactions: 20, successes: 15 },
  permissions: { interactions: 20, successes: 15 },
};

describe("AdaptiveTooltip", () => {
  it("positions tooltip above by default (top placement)", () => {
    render(
      <TestProvider state={INTERMEDIATE_STATE}>
        <AdaptiveTooltip
          id="test-top"
          skill="permissions"
          content="Top tooltip"
        >
          <button>Hover me</button>
        </AdaptiveTooltip>
      </TestProvider>,
    );
    fireEvent.mouseEnter(screen.getByText("Hover me").parentElement!);
    const tooltip = screen.getByRole("tooltip");
    expect(tooltip.className).toContain("bottom-full");
    expect(tooltip.className).not.toContain("left-full");
  });

  it('positions tooltip to the right when placement="right"', () => {
    render(
      <TestProvider state={INTERMEDIATE_STATE}>
        <AdaptiveTooltip
          id="test-right"
          skill="permissions"
          content="Right tooltip"
          placement="right"
        >
          <button>Hover me</button>
        </AdaptiveTooltip>
      </TestProvider>,
    );
    fireEvent.mouseEnter(screen.getByText("Hover me").parentElement!);
    const tooltip = screen.getByRole("tooltip");
    expect(tooltip.className).toContain("left-full");
    expect(tooltip.className).not.toContain("bottom-full");
  });
});
