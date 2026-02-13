/**
 * Tests for landing page hero section — Task 1.1
 *
 * Validates that the hero section displays the paper title,
 * author attribution, and abstract excerpt.
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

// Mock motion/react
vi.mock("motion/react", () => ({
  motion: {
    div: ({ children, ...props }: { children?: React.ReactNode; [key: string]: unknown }) => {
      const { initial, animate, whileInView, viewport, variants, ...rest } = props;
      return <div {...rest}>{children}</div>;
    },
    h1: ({ children, ...props }: { children?: React.ReactNode; [key: string]: unknown }) => {
      const { initial, animate, whileInView, viewport, variants, ...rest } = props;
      return <h1 {...rest}>{children}</h1>;
    },
    p: ({ children, ...props }: { children?: React.ReactNode; [key: string]: unknown }) => {
      const { initial, animate, whileInView, viewport, variants, ...rest } = props;
      return <p {...rest}>{children}</p>;
    },
  },
}));

import HomePage from "@/app/page";

afterEach(cleanup);

describe("Landing page hero section", () => {
  it("renders the paper title", () => {
    render(<HomePage />);
    const matches = screen.getAllByText(/Governing Generative Music/);
    expect(matches.length).toBeGreaterThanOrEqual(1);
    // The h1 heading should contain the title
    const h1 = matches.find((el) => el.tagName === "H1");
    expect(h1).toBeDefined();
  });

  it("includes subtitle with attribution limits", () => {
    render(<HomePage />);
    const matches = screen.getAllByText(/Attribution Limits, Platform Incentives/);
    expect(matches.length).toBeGreaterThanOrEqual(1);
  });

  it("displays author attribution", () => {
    render(<HomePage />);
    expect(screen.getByText("Petteri Teikari (2026)")).toBeDefined();
  });

  it("includes SSRN paper link", () => {
    render(<HomePage />);
    const paperLink = screen.getByText(/Read the Paper/);
    expect(paperLink).toBeDefined();
    expect(paperLink.closest("a")?.getAttribute("href")).toContain("doi.org");
  });

  it("renders abstract excerpt", () => {
    render(<HomePage />);
    expect(
      screen.getByText(/Your favourite song may have already trained/),
    ).toBeDefined();
  });

  it("shows the demo link", () => {
    render(<HomePage />);
    expect(screen.getByText(/Explore the Demo/)).toBeDefined();
  });
});
