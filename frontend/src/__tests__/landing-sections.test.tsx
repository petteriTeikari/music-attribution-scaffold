/**
 * Tests for landing page sections — Tasks 1.2, 1.3, 1.4, 2.1
 *
 * Validates HOW IT WORKS citations, topic cards, A0-A3 section,
 * and reference list on the landing page.
 */

import { cleanup, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";

// Mock next/image
vi.mock("next/image", () => ({
  default: (props: Record<string, unknown>) => {
    const { fill, priority, ...rest } = props;
    return <img {...rest} data-fill={fill ? "true" : undefined} data-priority={priority ? "true" : undefined} />;
  },
}));

// Mock next/link
vi.mock("next/link", () => ({
  default: ({ children, href, ...props }: { children: React.ReactNode; href: string; [key: string]: unknown }) => (
    <a href={href} {...props}>{children}</a>
  ),
}));

// Mock motion/react — LazyMotion + m components
vi.mock("motion/react", () => {
  function MockDiv({ children, ...props }: { children?: React.ReactNode; [key: string]: unknown }) {
    const { initial, animate, whileInView, viewport, variants, transition, ...rest } = props;
    return <div {...rest}>{children}</div>;
  }
  function MockH1({ children, ...props }: { children?: React.ReactNode; [key: string]: unknown }) {
    const { initial, animate, whileInView, viewport, variants, transition, ...rest } = props;
    return <h1 {...rest}>{children}</h1>;
  }
  function MockP({ children, ...props }: { children?: React.ReactNode; [key: string]: unknown }) {
    const { initial, animate, whileInView, viewport, variants, transition, ...rest } = props;
    return <p {...rest}>{children}</p>;
  }
  function MockLazyMotion({ children }: { children: React.ReactNode }) {
    return <>{children}</>;
  }
  return {
    motion: { div: MockDiv, h1: MockH1, p: MockP },
    m: { div: MockDiv, h1: MockH1, p: MockP },
    LazyMotion: MockLazyMotion,
    domAnimation: {},
  };
});

import HomePage from "@/app/page";

afterEach(cleanup);

describe("HOW IT WORKS section with citations", () => {
  it("renders the Process section heading", () => {
    render(<HomePage />);
    expect(screen.getByText("How It Works")).toBeDefined();
  });

  it("renders all four pipeline steps", () => {
    render(<HomePage />);
    expect(screen.getByText("FETCH & NORMALIZE")).toBeDefined();
    expect(screen.getByText("RESOLVE ENTITIES")).toBeDefined();
    expect(screen.getByText("SCORE & CALIBRATE")).toBeDefined();
    expect(screen.getByText("REVIEW & IMPROVE")).toBeDefined();
  });

  it("includes citation superscripts in pipeline steps", () => {
    render(<HomePage />);
    // Each step should have citation references
    const citationRefs = screen.getAllByText(/\[\d+/);
    expect(citationRefs.length).toBeGreaterThanOrEqual(4);
  });
});

describe("Topic cards section (12 academic citations)", () => {
  it("renders the Key Concepts section heading", () => {
    render(<HomePage />);
    expect(screen.getByText("Key Concepts")).toBeDefined();
  });

  it("renders all 12 topic card titles", () => {
    render(<HomePage />);
    // Exact topic card titles (unique to cards, not in citation titles)
    expect(screen.getByText("Calibrated Confidence")).toBeDefined();
    expect(screen.getByText("Uncertainty vs. Confidence")).toBeDefined();
    expect(screen.getByText("Uncertainty Propagation")).toBeDefined();
    expect(screen.getByText("ETL Pipelines")).toBeDefined();
    // Regex matches that may also appear in References — use getAllByText
    expect(screen.getAllByText(/Conformal.*Selective Prediction/).length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText(/Entity Resolution/).length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText(/Active Learning/).length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText(/Drift Detection/).length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText(/Provenance.*Attribution/).length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText(/MCP Permission/).length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText(/Voice Cloning/).length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText(/MLSecOps/).length).toBeGreaterThanOrEqual(1);
  });

  it("renders Roman numeral markers I through XII", () => {
    render(<HomePage />);
    const markers = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"];
    for (const m of markers) {
      expect(screen.getAllByText(m).length).toBeGreaterThanOrEqual(1);
    }
  });

  it("renders Read More buttons for each card", () => {
    render(<HomePage />);
    const readMoreButtons = screen.getAllByRole("button", { name: /read more/i });
    expect(readMoreButtons.length).toBe(12);
  });

  it("renders group labels", () => {
    render(<HomePage />);
    expect(screen.getByText("Confidence & Uncertainty")).toBeDefined();
    expect(screen.getByText("Pipeline & Data")).toBeDefined();
    expect(screen.getByText("Governance & Security")).toBeDefined();
  });
});

describe("A0-A3 Assurance Levels section", () => {
  it("renders the Assurance Levels heading", () => {
    render(<HomePage />);
    expect(screen.getByText("Assurance Levels")).toBeDefined();
  });

  it("renders all four levels", () => {
    render(<HomePage />);
    expect(screen.getByText("A0")).toBeDefined();
    expect(screen.getByText("A1")).toBeDefined();
    expect(screen.getByText("A2")).toBeDefined();
    expect(screen.getByText("A3")).toBeDefined();
  });

  it("shows ISRC, ISWC, ISNI identifiers", () => {
    render(<HomePage />);
    expect(screen.getAllByText(/ISRC/).length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText(/ISWC/).length).toBeGreaterThanOrEqual(1);
    expect(screen.getAllByText(/ISNI/).length).toBeGreaterThanOrEqual(1);
  });
});

describe("References section", () => {
  it("renders the References heading", () => {
    render(<HomePage />);
    expect(screen.getByText("References")).toBeDefined();
  });

  it("renders citation entries with numbers", () => {
    render(<HomePage />);
    expect(screen.getByText("[1]")).toBeDefined();
    expect(screen.getByText("[13]")).toBeDefined();
  });
});
