/**
 * Tests for ConfidencePopover component.
 */
import { describe, it, expect, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { ConfidencePopover } from "@/components/works/confidence-popover";
import type { ConformalSet } from "@/lib/types/attribution";

const MOCK_CONFORMAL: ConformalSet = {
  coverage_level: 0.9,
  prediction_sets: {
    "artist-imogen-heap": ["PERFORMER", "SONGWRITER", "PRODUCER"] as never[],
  },
  set_sizes: { "artist-imogen-heap": 3 },
  marginal_coverage: 0.92,
  calibration_error: 0.018,
  calibration_method: "temperature_scaling",
  calibration_set_size: 1200,
};

describe("ConfidencePopover", () => {
  it("shows popover on mouseenter after delay", async () => {
    const user = userEvent.setup();
    render(
      <ConfidencePopover score={0.95} conformalSet={MOCK_CONFORMAL}>
        <span>95</span>
      </ConfidencePopover>,
    );

    expect(screen.queryByRole("tooltip")).not.toBeInTheDocument();

    const wrapper = screen.getByText("95").closest("div")!;
    await user.hover(wrapper);

    await waitFor(() => {
      expect(screen.getByRole("tooltip")).toBeInTheDocument();
    });
  });

  it("hides popover on mouseleave", async () => {
    const user = userEvent.setup();
    render(
      <ConfidencePopover score={0.95} conformalSet={MOCK_CONFORMAL}>
        <span>95</span>
      </ConfidencePopover>,
    );

    const wrapper = screen.getByText("95").closest("div")!;
    await user.hover(wrapper);

    await waitFor(() => {
      expect(screen.getByRole("tooltip")).toBeInTheDocument();
    });

    await user.unhover(wrapper);

    await waitFor(() => {
      expect(screen.queryByRole("tooltip")).not.toBeInTheDocument();
    });
  });

  it("displays coverage level, marginal coverage, calibration error, set sizes", async () => {
    const user = userEvent.setup();
    render(
      <ConfidencePopover score={0.95} conformalSet={MOCK_CONFORMAL}>
        <span>95</span>
      </ConfidencePopover>,
    );

    const wrapper = screen.getByText("95").closest("div")!;
    await user.hover(wrapper);

    await waitFor(() => {
      expect(screen.getByRole("tooltip")).toBeInTheDocument();
    });

    expect(screen.getByText("90%")).toBeInTheDocument(); // coverage_level
    expect(screen.getByText("92%")).toBeInTheDocument(); // marginal_coverage
    expect(screen.getByText("0.018")).toBeInTheDocument(); // calibration_error
    expect(screen.getByText("3")).toBeInTheDocument(); // set size
  });

  it("uses data-mono class for numbers", async () => {
    const user = userEvent.setup();
    render(
      <ConfidencePopover score={0.95} conformalSet={MOCK_CONFORMAL}>
        <span>95</span>
      </ConfidencePopover>,
    );

    const wrapper = screen.getByText("95").closest("div")!;
    await user.hover(wrapper);

    await waitFor(() => {
      expect(screen.getByRole("tooltip")).toBeInTheDocument();
    });

    const tooltip = screen.getByRole("tooltip");
    const dataMonoElements = tooltip.querySelectorAll(".data-mono");
    expect(dataMonoElements.length).toBeGreaterThanOrEqual(3);
  });

  it("calls onView callback once", async () => {
    const user = userEvent.setup();
    const onView = vi.fn();
    render(
      <ConfidencePopover
        score={0.95}
        conformalSet={MOCK_CONFORMAL}
        onView={onView}
      >
        <span>95</span>
      </ConfidencePopover>,
    );

    const wrapper = screen.getByText("95").closest("div")!;

    // First hover
    await user.hover(wrapper);
    await waitFor(() => {
      expect(screen.getByRole("tooltip")).toBeInTheDocument();
    });
    expect(onView).toHaveBeenCalledTimes(1);

    // Unhover + re-hover
    await user.unhover(wrapper);
    await waitFor(() => {
      expect(screen.queryByRole("tooltip")).not.toBeInTheDocument();
    });

    await user.hover(wrapper);
    await waitFor(() => {
      expect(screen.getByRole("tooltip")).toBeInTheDocument();
    });

    // Should still only be called once
    expect(onView).toHaveBeenCalledTimes(1);
  });
});
