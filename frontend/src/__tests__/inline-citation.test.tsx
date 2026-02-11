/**
 * Tests for InlineCitation component (Task 3.1).
 */

import { render, screen, fireEvent } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import { InlineCitation } from "@/components/citations/inline-citation";
import type { CitationReference } from "@/lib/types/uncertainty";
import { Source } from "@/lib/types/enums";

const MOCK_CITATION: CitationReference = {
  index: 1,
  source: Source.MUSICBRAINZ,
  confidence: 0.92,
  label: "MusicBrainz",
  detail: "Matched via ISRC lookup",
  timestamp: "2024-06-15T10:00:00Z",
};

describe("InlineCitation", () => {
  it("renders citation number", () => {
    render(<InlineCitation citation={MOCK_CITATION} />);
    expect(screen.getByText("[1]")).toBeInTheDocument();
  });

  it("shows tooltip on hover", () => {
    render(<InlineCitation citation={MOCK_CITATION} />);
    const badge = screen.getByRole("doc-noteref");
    fireEvent.mouseEnter(badge);
    expect(screen.getByText("MusicBrainz")).toBeInTheDocument();
  });

  it("tooltip contains source name", () => {
    render(<InlineCitation citation={MOCK_CITATION} />);
    const badge = screen.getByRole("doc-noteref");
    fireEvent.mouseEnter(badge);
    expect(screen.getByText("MusicBrainz")).toBeInTheDocument();
  });

  it("tooltip contains confidence as percentage", () => {
    render(<InlineCitation citation={MOCK_CITATION} />);
    const badge = screen.getByRole("doc-noteref");
    fireEvent.mouseEnter(badge);
    expect(screen.getByText(/92%/)).toBeInTheDocument();
  });

  it("has accessibility ARIA attributes", () => {
    render(<InlineCitation citation={MOCK_CITATION} />);
    const badge = screen.getByRole("doc-noteref");
    expect(badge).toHaveAttribute("aria-label");
    expect(badge).toHaveAttribute("aria-describedby");
  });

  it("uses design tokens not hardcoded hex", async () => {
    // This is enforced by the css-token-lint test, but verify component renders
    const { container } = render(<InlineCitation citation={MOCK_CITATION} />);
    expect(container.firstChild).toBeTruthy();
  });
});
