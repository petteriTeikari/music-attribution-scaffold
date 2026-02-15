import { describe, it, expect, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import { ConsentQueryFlow } from "./consent-query-flow";

// Mock animejs — JSDOM has no real animation support
vi.mock("animejs", () => ({
  createTimeline: vi.fn(() => ({
    add: vi.fn().mockReturnThis(),
    play: vi.fn(),
    pause: vi.fn(),
  })),
}));

describe("ConsentQueryFlow", () => {
  it("renders SVG with role='img' and aria-label", () => {
    render(<ConsentQueryFlow />);
    const svg = screen.getByRole("img");
    expect(svg).toBeInTheDocument();
    expect(svg).toHaveAttribute("aria-label");
  });

  it("renders all 4 chain labels", () => {
    render(<ConsentQueryFlow />);
    expect(screen.getByText("OWNER")).toBeInTheDocument();
    expect(screen.getByText("MANAGER")).toBeInTheDocument();
    expect(screen.getByText("DELEGATE")).toBeInTheDocument();
    expect(screen.getByText("REQUESTER")).toBeInTheDocument();
  });

  it("renders entity names below chain labels", () => {
    render(<ConsentQueryFlow />);
    expect(screen.getByText("Imogen Heap")).toBeInTheDocument();
    expect(screen.getByText("Megaphonic")).toBeInTheDocument();
    expect(screen.getByText("Auracles")).toBeInTheDocument();
  });

  it("does not crash without IntersectionObserver", () => {
    // IntersectionObserver is not available in JSDOM by default
    const originalIO = globalThis.IntersectionObserver;
    // @ts-expect-error - deliberately removing for test
    delete globalThis.IntersectionObserver;
    expect(() => render(<ConsentQueryFlow />)).not.toThrow();
    globalThis.IntersectionObserver = originalIO;
  });
});
