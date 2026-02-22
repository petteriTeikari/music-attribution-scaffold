/**
 * Tests for AudioVisualizer component (Task 5.2 + 5.4).
 *
 * Covers rendering, canvas-based visualization, and
 * prefers-reduced-motion behavior.
 */

import { describe, it, expect, vi, afterEach } from "vitest";
import { render, screen } from "@testing-library/react";
import { Provider, createStore } from "jotai";
import React from "react";
import type { ReactNode } from "react";

import { AudioVisualizer } from "../AudioVisualizer";
import { voiceStateAtom, type VoiceState } from "@/lib/stores/voice";

/* ── Helpers ─────────────────────────────────────────────────── */

function renderWithStore(ui: ReactNode, initialState?: VoiceState) {
  const store = createStore();
  if (initialState) {
    store.set(voiceStateAtom, initialState);
  }
  return {
    store,
    ...render(<Provider store={store}>{ui}</Provider>),
  };
}

afterEach(() => {
  vi.restoreAllMocks();
});

/* ── Tests ───────────────────────────────────────────────────── */

describe("AudioVisualizer", () => {
  it("renders a canvas element", () => {
    const { container } = renderWithStore(<AudioVisualizer />);
    expect(container.querySelector("canvas")).toBeInTheDocument();
  });

  it("has correct ARIA role and label", () => {
    renderWithStore(<AudioVisualizer />);
    const viz = screen.getByRole("img", { name: /audio/i });
    expect(viz).toBeInTheDocument();
  });

  it("canvas has default width and height attributes", () => {
    const { container } = renderWithStore(<AudioVisualizer />);
    const canvas = container.querySelector("canvas");
    expect(canvas).toHaveAttribute("width", "200");
    expect(canvas).toHaveAttribute("height", "60");
  });

  it("accepts width and height props", () => {
    const { container } = renderWithStore(
      <AudioVisualizer width={300} height={80} />,
    );
    const canvas = container.querySelector("canvas");
    expect(canvas).toHaveAttribute("width", "300");
    expect(canvas).toHaveAttribute("height", "80");
  });

  it("renders in idle state", () => {
    const { container } = renderWithStore(<AudioVisualizer />, "idle");
    expect(container.querySelector("canvas")).toBeInTheDocument();
  });

  it("renders in recording state", () => {
    const { container } = renderWithStore(<AudioVisualizer />, "recording");
    expect(container.querySelector("canvas")).toBeInTheDocument();
  });

  it("is hidden from screen readers when decorative", () => {
    const { container } = renderWithStore(<AudioVisualizer decorative />);
    const canvas = container.querySelector("canvas");
    expect(canvas).toHaveAttribute("aria-hidden", "true");
  });

  it("does NOT have aria-hidden when not decorative", () => {
    const { container } = renderWithStore(<AudioVisualizer />);
    const canvas = container.querySelector("canvas");
    expect(canvas).not.toHaveAttribute("aria-hidden");
  });

  it("accepts custom className prop", () => {
    const { container } = renderWithStore(
      <AudioVisualizer className="my-viz" />,
    );
    expect(container.querySelector(".my-viz")).toBeInTheDocument();
  });
});

describe("AudioVisualizer reduced motion", () => {
  it("renders canvas when prefers-reduced-motion is set", () => {
    Object.defineProperty(window, "matchMedia", {
      writable: true,
      value: vi.fn().mockImplementation((query: string) => ({
        matches: query === "(prefers-reduced-motion: reduce)",
        media: query,
        onchange: null,
        addListener: vi.fn(),
        removeListener: vi.fn(),
        addEventListener: vi.fn(),
        removeEventListener: vi.fn(),
        dispatchEvent: vi.fn(),
      })),
    });

    const { container } = renderWithStore(<AudioVisualizer />, "recording");
    // Should still render canvas, just no animation loop
    expect(container.querySelector("canvas")).toBeInTheDocument();
  });
});
