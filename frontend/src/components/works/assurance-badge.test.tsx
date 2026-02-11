import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { AssuranceBadge } from "./assurance-badge";

describe("AssuranceBadge", () => {
  it("renders LEVEL_0 label", () => {
    render(<AssuranceBadge level="LEVEL_0" />);
    expect(screen.getByText(/A0/)).toBeInTheDocument();
  });

  it("renders LEVEL_3 label", () => {
    render(<AssuranceBadge level="LEVEL_3" />);
    expect(screen.getByText(/A3/)).toBeInTheDocument();
  });

  it("renders all four levels correctly", () => {
    const levels = ["LEVEL_0", "LEVEL_1", "LEVEL_2", "LEVEL_3"] as const;
    const labels = ["A0", "A1", "A2", "A3"];

    levels.forEach((level, i) => {
      const { unmount } = render(<AssuranceBadge level={level} />);
      expect(screen.getByText(new RegExp(labels[i]))).toBeInTheDocument();
      unmount();
    });
  });
});
