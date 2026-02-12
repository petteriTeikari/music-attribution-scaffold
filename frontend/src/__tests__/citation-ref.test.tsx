/**
 * Tests for CitationRefList component — Task 0.3
 *
 * Numbered reference list displayed at the bottom of the landing page.
 */

import { cleanup, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it } from "vitest";

import { CitationRefList } from "@/components/citations/citation-ref";
import { CITATIONS } from "@/lib/data/citations";

afterEach(cleanup);

describe("CitationRefList", () => {
  it("renders all citations", () => {
    render(<CitationRefList citations={CITATIONS} />);
    // Each citation should render its number in brackets
    for (const c of CITATIONS) {
      expect(screen.getByText(`[${c.id}]`)).toBeDefined();
    }
  });

  it("renders author and title for each citation", () => {
    render(<CitationRefList citations={CITATIONS.slice(0, 3)} />);
    expect(screen.getByText(/Stengel-Eskin/)).toBeDefined();
    expect(screen.getByText(/Calibrated Confidence/)).toBeDefined();
  });

  it("renders links for citations with URLs", () => {
    render(<CitationRefList citations={CITATIONS.slice(0, 1)} />);
    const link = screen.getByRole("link");
    expect(link).toBeDefined();
    expect(link.getAttribute("href")).toContain("arxiv.org");
    expect(link.getAttribute("target")).toBe("_blank");
    expect(link.getAttribute("rel")).toContain("noopener");
  });

  it("renders section heading", () => {
    render(<CitationRefList citations={CITATIONS} />);
    expect(screen.getByText("References")).toBeDefined();
  });

  it("uses data-mono for citation numbers", () => {
    const { container } = render(
      <CitationRefList citations={CITATIONS.slice(0, 1)} />,
    );
    const monoElements = container.querySelectorAll(".data-mono");
    expect(monoElements.length).toBeGreaterThan(0);
  });

  it("handles empty citations array", () => {
    const { container } = render(<CitationRefList citations={[]} />);
    expect(container.textContent).toContain("References");
  });
});
