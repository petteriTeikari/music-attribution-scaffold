import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { Provider } from "jotai";
import { useHydrateAtoms } from "jotai/utils";
import type { ReactNode } from "react";
import { Navigation } from "./navigation";
import { proficiencyStateAtom } from "@/lib/stores/proficiency";
import type { ProficiencyState } from "@/lib/stores/proficiency";

// Mock next/navigation
vi.mock("next/navigation", () => ({
  usePathname: () => "/works",
}));

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

describe("Navigation sidebar tooltips", () => {
  it("shows Works tooltip containing 'catalog' on hover", () => {
    render(
      <TestProvider state={INTERMEDIATE_STATE}>
        <Navigation />
      </TestProvider>,
    );
    // Desktop sidebar nav links
    const worksLinks = screen.getAllByText("Works");
    // Hover the desktop nav link wrapper (parent of AdaptiveTooltip)
    fireEvent.mouseEnter(worksLinks[0].closest("[class*='relative']")!);
    const tooltip = screen.getByRole("tooltip");
    expect(tooltip.textContent?.toLowerCase()).toContain("catalog");
  });

  it("shows Permissions tooltip containing 'MCP' on hover", () => {
    render(
      <TestProvider state={INTERMEDIATE_STATE}>
        <Navigation />
      </TestProvider>,
    );
    const permLinks = screen.getAllByText("Permissions");
    fireEvent.mouseEnter(permLinks[0].closest("[class*='relative']")!);
    const tooltip = screen.getByRole("tooltip");
    expect(tooltip.textContent).toContain("MCP");
  });
});
