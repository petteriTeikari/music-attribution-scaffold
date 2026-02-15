import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent, act } from "@testing-library/react";
import { Provider } from "jotai";
import { useHydrateAtoms } from "jotai/utils";
import type { ReactNode } from "react";
import { AdaptiveTooltip } from "./adaptive-tooltip";
import { proficiencyStateAtom, noviceTooltipQueueAtom } from "@/lib/stores/proficiency";
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

const NOVICE_STATE: ProficiencyState = {
  review: { interactions: 0, successes: 0 },
  feedback: { interactions: 0, successes: 0 },
  confidence_reading: { interactions: 0, successes: 0 },
  permissions: { interactions: 0, successes: 0 },
};

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

describe("Novice tooltip queue (no overlap)", () => {
  it("shows only ONE tooltip at a time for novice users", () => {
    render(
      <TestProvider state={NOVICE_STATE}>
        <AdaptiveTooltip
          id="nav-works"
          skill="permissions"
          content="Works tooltip content"
        >
          <span>Works</span>
        </AdaptiveTooltip>
        <AdaptiveTooltip
          id="nav-permissions"
          skill="permissions"
          content="Permissions tooltip content"
        >
          <span>Permissions</span>
        </AdaptiveTooltip>
      </TestProvider>,
    );

    // Only one tooltip should be visible
    const tooltips = screen.getAllByRole("tooltip");
    expect(tooltips).toHaveLength(1);
    expect(tooltips[0]).toHaveTextContent("Works tooltip content");
  });

  it("shows next tooltip after dismissing the first", () => {
    render(
      <TestProvider state={NOVICE_STATE}>
        <AdaptiveTooltip
          id="nav-works"
          skill="permissions"
          content="Works tooltip"
        >
          <span>Works</span>
        </AdaptiveTooltip>
        <AdaptiveTooltip
          id="nav-permissions"
          skill="permissions"
          content="Permissions tooltip"
        >
          <span>Permissions</span>
        </AdaptiveTooltip>
      </TestProvider>,
    );

    // First tooltip visible
    expect(screen.getAllByRole("tooltip")).toHaveLength(1);
    expect(screen.getByRole("tooltip")).toHaveTextContent("Works tooltip");

    // Dismiss it
    act(() => {
      fireEvent.click(screen.getByText("Got it"));
    });

    // Second tooltip now visible
    expect(screen.getAllByRole("tooltip")).toHaveLength(1);
    expect(screen.getByRole("tooltip")).toHaveTextContent("Permissions tooltip");
  });

  it("shows no tooltips after all are dismissed", () => {
    render(
      <TestProvider state={NOVICE_STATE}>
        <AdaptiveTooltip
          id="nav-works"
          skill="permissions"
          content="Works tooltip"
        >
          <span>Works</span>
        </AdaptiveTooltip>
        <AdaptiveTooltip
          id="nav-permissions"
          skill="permissions"
          content="Permissions tooltip"
        >
          <span>Permissions</span>
        </AdaptiveTooltip>
      </TestProvider>,
    );

    // Dismiss first
    act(() => {
      fireEvent.click(screen.getByText("Got it"));
    });

    // Dismiss second
    act(() => {
      fireEvent.click(screen.getByText("Got it"));
    });

    // No tooltips remain
    expect(screen.queryAllByRole("tooltip")).toHaveLength(0);
  });
});
