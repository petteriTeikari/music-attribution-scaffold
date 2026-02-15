/**
 * Tests for NodeOverlayPanel component.
 */
import { describe, it, expect, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { NodeOverlayPanel } from "@/components/permissions/node-overlay-panel";
import type { GraphNode } from "@/lib/permissions/graph-data";

const PLATFORM_NODE: GraphNode = {
  id: "platform-suno",
  label: "Suno",
  type: "platform",
  platformType: "ai_generator",
};

const GROUP_NODE: GraphNode = {
  id: "group-ai",
  label: "AI & Generation",
  type: "group",
};

const ARTIST_NODE: GraphNode = {
  id: "artist",
  label: "Imogen Heap",
  type: "artist",
};

describe("NodeOverlayPanel", () => {
  it("renders platform node with name, description, URL from ecosystem registry", () => {
    render(
      <NodeOverlayPanel node={PLATFORM_NODE} onClose={vi.fn()} />,
    );
    expect(screen.getByText("Suno")).toBeInTheDocument();
    expect(
      screen.getByText("Text-to-music generation platform"),
    ).toBeInTheDocument();
    expect(screen.getByText("https://suno.com")).toBeInTheDocument();
    expect(screen.getByText("https://suno.com")).toHaveAttribute(
      "target",
      "_blank",
    );
  });

  it("shows Fairly Trained badge for certified platforms", () => {
    const certifiedNode: GraphNode = {
      id: "platform-sureel-ai",
      label: "Sureel AI",
      type: "platform",
      platformType: "attribution_infra",
    };
    render(
      <NodeOverlayPanel node={certifiedNode} onClose={vi.fn()} />,
    );
    expect(screen.getByText("Fairly Trained Certified")).toBeInTheDocument();
  });

  it("renders group node with permission count breakdown", () => {
    const counts = { allow: 3, ask: 2, deny: 1 };
    render(
      <NodeOverlayPanel
        node={GROUP_NODE}
        groupCounts={counts}
        onClose={vi.fn()}
      />,
    );
    expect(screen.getByText("Consent Group")).toBeInTheDocument();
    expect(screen.getByText("6")).toBeInTheDocument(); // total
    expect(screen.getByText("3")).toBeInTheDocument(); // allow
    expect(screen.getByText("2")).toBeInTheDocument(); // ask
    expect(screen.getByText("1")).toBeInTheDocument(); // deny
  });

  it("renders artist node with total count and permissions link", () => {
    const onNavigate = vi.fn();
    render(
      <NodeOverlayPanel
        node={ARTIST_NODE}
        totalCount={14}
        onClose={vi.fn()}
        onNavigateToPermissions={onNavigate}
      />,
    );
    expect(screen.getByText("Imogen Heap")).toBeInTheDocument();
    expect(screen.getByText("14")).toBeInTheDocument();
    expect(
      screen.getByText("View all permissions"),
    ).toBeInTheDocument();
  });

  it("close button works", async () => {
    const user = userEvent.setup();
    const onClose = vi.fn();
    render(
      <NodeOverlayPanel node={PLATFORM_NODE} onClose={onClose} />,
    );
    await user.click(screen.getByLabelText("Close overlay"));
    expect(onClose).toHaveBeenCalledTimes(1);
  });

  it("has dialog role with aria-label", () => {
    render(
      <NodeOverlayPanel node={PLATFORM_NODE} onClose={vi.fn()} />,
    );
    expect(
      screen.getByRole("dialog", { name: /Details for Suno/i }),
    ).toBeInTheDocument();
  });
});
