import { describe, it, expect, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import { ConsentGraph } from "./consent-graph";
import { MOCK_AUDIT_LOG } from "@/lib/data/mock-permissions";

// Mock d3 force simulation — JSDOM has no real layout support
vi.mock("d3", () => ({
  forceSimulation: vi.fn(() => ({
    force: vi.fn().mockReturnThis(),
    nodes: vi.fn().mockReturnThis(),
    on: vi.fn().mockReturnThis(),
    alpha: vi.fn().mockReturnThis(),
    restart: vi.fn(),
    stop: vi.fn(),
  })),
  forceLink: vi.fn(() => {
    const fn = vi.fn().mockReturnThis() as ReturnType<typeof vi.fn> & { id: ReturnType<typeof vi.fn>; distance: ReturnType<typeof vi.fn>; links: ReturnType<typeof vi.fn> };
    fn.id = vi.fn().mockReturnValue(fn);
    fn.distance = vi.fn().mockReturnValue(fn);
    fn.links = vi.fn().mockReturnValue(fn);
    return fn;
  }),
  forceManyBody: vi.fn(() => {
    const fn = vi.fn().mockReturnThis() as ReturnType<typeof vi.fn> & { strength: ReturnType<typeof vi.fn> };
    fn.strength = vi.fn().mockReturnValue(fn);
    return fn;
  }),
  forceCenter: vi.fn(() => vi.fn()),
  forceCollide: vi.fn(() => {
    const fn = vi.fn().mockReturnThis() as ReturnType<typeof vi.fn> & { radius: ReturnType<typeof vi.fn> };
    fn.radius = vi.fn().mockReturnValue(fn);
    return fn;
  }),
}));

describe("ConsentGraph", () => {
  it("renders SVG with role='img'", () => {
    render(<ConsentGraph auditLog={MOCK_AUDIT_LOG} />);
    const svg = screen.getByRole("img");
    expect(svg).toBeInTheDocument();
  });

  it("renders filter buttons", () => {
    render(<ConsentGraph auditLog={MOCK_AUDIT_LOG} />);
    expect(screen.getByText("All")).toBeInTheDocument();
    // Filter buttons and legend both contain Allow/Ask/Deny
    expect(screen.getAllByText("Allow").length).toBeGreaterThanOrEqual(2);
    expect(screen.getAllByText("Ask").length).toBeGreaterThanOrEqual(2);
    expect(screen.getAllByText("Deny").length).toBeGreaterThanOrEqual(2);
  });

  it("renders legend", () => {
    render(<ConsentGraph auditLog={MOCK_AUDIT_LOG} />);
    expect(screen.getByText("Artist")).toBeInTheDocument();
    expect(screen.getByText("Group")).toBeInTheDocument();
    expect(screen.getByText("Platform")).toBeInTheDocument();
  });

  it("renders screen reader summary", () => {
    render(<ConsentGraph auditLog={MOCK_AUDIT_LOG} />);
    const summary = screen.getByText(/consent propagation/i);
    expect(summary).toBeInTheDocument();
  });

  it("renders with empty audit log without crashing", () => {
    render(<ConsentGraph auditLog={[]} />);
    expect(screen.getByRole("img")).toBeInTheDocument();
  });
});
