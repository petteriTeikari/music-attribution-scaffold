/**
 * Tests for CitationOverlay component — Task 0.2
 *
 * The overlay provides progressive disclosure for academic content:
 * - Default: title + summary + citation superscripts
 * - Expanded: detail paragraph + figure plan placeholder
 */

import { cleanup, render, screen, fireEvent } from "@testing-library/react";
import { afterEach, describe, expect, it } from "vitest";

import { CitationOverlay } from "@/components/citations/citation-overlay";
import { CITATIONS } from "@/lib/data/citations";

afterEach(cleanup);

const defaultProps = {
  title: "Calibrated Confidence",
  marker: "I",
  summary: "Every attribution comes with a calibrated confidence score.",
  detail: "Calibration means the system\u2019s stated confidence matches its actual accuracy. This is a longer paragraph with enough detail for academic depth.",
  citationIds: [1, 2],
  figurePlan: "Calibration curve showing ideal diagonal vs. uncalibrated curve.",
  citations: CITATIONS,
};

describe("CitationOverlay", () => {
  it("renders title and summary", () => {
    render(<CitationOverlay {...defaultProps} />);
    expect(screen.getByText("Calibrated Confidence")).toBeDefined();
    expect(screen.getByText(/Every attribution comes with/)).toBeDefined();
  });

  it("renders the Roman numeral marker", () => {
    render(<CitationOverlay {...defaultProps} />);
    expect(screen.getByText("I")).toBeDefined();
  });

  it("renders citation superscript numbers", () => {
    render(<CitationOverlay {...defaultProps} />);
    // Should show [1, 2] as superscripts
    expect(screen.getByText("[1, 2]")).toBeDefined();
  });

  it("does not show detail text by default", () => {
    render(<CitationOverlay {...defaultProps} />);
    expect(screen.queryByText(/Calibration means the system/)).toBeNull();
  });

  it("shows detail text after clicking Read More", () => {
    render(<CitationOverlay {...defaultProps} />);
    const button = screen.getByRole("button", { name: /read more/i });
    fireEvent.click(button);
    expect(screen.getByText(/Calibration means the system/)).toBeDefined();
  });

  it("shows figure plan placeholder when expanded", () => {
    render(<CitationOverlay {...defaultProps} />);
    const button = screen.getByRole("button", { name: /read more/i });
    fireEvent.click(button);
    expect(screen.getByText(/Calibration curve showing/)).toBeDefined();
  });

  it("hides detail text when clicking Close", () => {
    render(<CitationOverlay {...defaultProps} />);
    const readMore = screen.getByRole("button", { name: /read more/i });
    fireEvent.click(readMore);
    expect(screen.getByText(/Calibration means the system/)).toBeDefined();

    const close = screen.getByRole("button", { name: /close/i });
    fireEvent.click(close);
    expect(screen.queryByText(/Calibration means the system/)).toBeNull();
  });

  it("renders accent square marker", () => {
    const { container } = render(<CitationOverlay {...defaultProps} />);
    const accentSquare = container.querySelector(".accent-square");
    expect(accentSquare).not.toBeNull();
  });

  it("uses editorial-caps for marker", () => {
    const { container } = render(<CitationOverlay {...defaultProps} />);
    const capsElements = container.querySelectorAll(".editorial-caps");
    expect(capsElements.length).toBeGreaterThan(0);
  });
});
