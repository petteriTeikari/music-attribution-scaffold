import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { ConfidenceGauge, ConfidenceBadge } from "./confidence-gauge";

describe("ConfidenceGauge", () => {
  it("renders with correct aria attributes", () => {
    render(<ConfidenceGauge score={0.85} animate={false} />);
    const meter = screen.getByRole("meter");
    expect(meter).toBeInTheDocument();
    expect(meter).toHaveAttribute("aria-valuenow", "85");
    expect(meter).toHaveAttribute("aria-valuemin", "0");
    expect(meter).toHaveAttribute("aria-valuemax", "100");
  });

  it("renders high confidence label", () => {
    render(<ConfidenceGauge score={0.95} animate={false} />);
    expect(screen.getByText("High Confidence")).toBeInTheDocument();
  });

  it("renders medium confidence label", () => {
    render(<ConfidenceGauge score={0.72} animate={false} />);
    expect(screen.getByText("Medium Confidence")).toBeInTheDocument();
  });

  it("renders low confidence label", () => {
    render(<ConfidenceGauge score={0.28} animate={false} />);
    expect(screen.getByText("Low Confidence")).toBeInTheDocument();
  });

  it("hides label when showLabel is false", () => {
    render(<ConfidenceGauge score={0.85} animate={false} showLabel={false} />);
    expect(screen.queryByText("High Confidence")).not.toBeInTheDocument();
  });

  it("renders SVG element", () => {
    const { container } = render(
      <ConfidenceGauge score={0.85} animate={false} />
    );
    const svg = container.querySelector("svg");
    expect(svg).toBeInTheDocument();
  });

  it("renders different sizes", () => {
    const { rerender, container } = render(
      <ConfidenceGauge score={0.5} size="sm" animate={false} />
    );
    let svg = container.querySelector("svg");
    expect(svg).toHaveAttribute("width", "48");

    rerender(<ConfidenceGauge score={0.5} size="lg" animate={false} />);
    svg = container.querySelector("svg");
    expect(svg).toHaveAttribute("width", "140");
  });
});

describe("ConfidenceBadge", () => {
  it("renders with correct text", () => {
    render(<ConfidenceBadge score={0.95} />);
    expect(screen.getByText(/95%/)).toBeInTheDocument();
    expect(screen.getByText(/High Confidence/)).toBeInTheDocument();
  });

  it("renders medium badge", () => {
    render(<ConfidenceBadge score={0.72} />);
    expect(screen.getByText(/72%/)).toBeInTheDocument();
  });
});
