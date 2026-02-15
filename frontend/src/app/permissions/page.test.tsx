import { describe, it, expect, vi, beforeEach } from "vitest";
import { render, screen, fireEvent, within, waitFor } from "@testing-library/react";

// Mock the API client
vi.mock("@/lib/api/api-client", () => ({
  apiClient: {
    getPermissions: vi.fn().mockResolvedValue({
      schema_version: "1.0.0",
      permission_id: "perm-test",
      entity_id: "artist-test",
      scope: "CATALOG",
      scope_entity_id: null,
      permissions: [
        {
          permission_type: "VOICE_CLONING",
          value: "DENY",
          conditions: [],
          royalty_rate: null,
          attribution_requirement: null,
          territory: null,
        },
        {
          permission_type: "AI_TRAINING",
          value: "ALLOW",
          conditions: [],
          royalty_rate: null,
          attribution_requirement: null,
          territory: null,
        },
      ],
      effective_from: "2025-01-01T00:00:00Z",
      effective_until: null,
      delegation_chain: [],
      default_permission: "ASK",
      created_by: "test",
      updated_at: "2025-01-01T00:00:00Z",
      version: 1,
    }),
    getAuditLog: vi.fn().mockResolvedValue([]),
  },
}));

// Mock animejs
vi.mock("animejs", () => ({
  createTimeline: vi.fn(() => ({
    add: vi.fn().mockReturnThis(),
    play: vi.fn(),
    pause: vi.fn(),
  })),
}));

// Mock next/dynamic to render components directly
vi.mock("next/dynamic", () => ({
  default: (loader: () => Promise<{ default: React.ComponentType }>) => {
    // Return a placeholder for lazy components
    return function DynamicComponent() {
      return <div data-testid="dynamic-placeholder" />;
    };
  },
}));

import PermissionsPage from "./page";

describe("PermissionsPage", () => {
  it("renders ConsentQueryFlow between consent profile and tabs", async () => {
    render(<PermissionsPage />);
    await waitFor(() => {
      expect(screen.getByText("Consent Profile")).toBeInTheDocument();
    });
    // Query flow SVG renders
    expect(screen.getByText("Consent Query Flow")).toBeInTheDocument();
    expect(screen.getByText("OWNER")).toBeInTheDocument();
    expect(screen.getByText("REQUESTER")).toBeInTheDocument();
  });
});

describe("PermissionsPage consent graph tab", () => {
  it("shows Consent Graph tab in DOM", async () => {
    render(<PermissionsPage />);
    await waitFor(() => {
      expect(screen.getByText("Consent Profile")).toBeInTheDocument();
    });
    const graphTab = screen.getByRole("tab", { name: /Consent Graph/i });
    expect(graphTab).toBeInTheDocument();
  });

  it("loads consent graph component on tab click", async () => {
    render(<PermissionsPage />);
    await waitFor(() => {
      expect(screen.getByText("Consent Profile")).toBeInTheDocument();
    });
    const graphTab = screen.getByRole("tab", { name: /Consent Graph/i });
    fireEvent.click(graphTab);
    // Dynamic component renders placeholder
    await waitFor(() => {
      expect(screen.getByText("Consent Propagation Graph")).toBeInTheDocument();
    });
  });
});

describe("PermissionsPage navigation", () => {
  it("switches to permissions tab and highlights row when onNavigateToEntry is triggered", async () => {
    render(<PermissionsPage />);

    // Wait for data to load
    await waitFor(() => {
      expect(screen.getByText("Consent Profile")).toBeInTheDocument();
    });

    // Find the deny count bucket (1 deny in AI & Generation)
    const denyBuckets = screen.getAllByText("1 deny");
    const bucket = denyBuckets[0].closest("[data-count-bucket]");
    expect(bucket).toBeInTheDocument();

    // Hover to open dropdown
    fireEvent.mouseEnter(bucket!);
    const dropdown = screen.getByRole("listbox");
    expect(dropdown).toBeInTheDocument();

    // Click on Voice Cloning entry
    const option = within(dropdown).getByText("Voice Cloning");
    fireEvent.click(option);

    // Should switch to permissions tab
    await waitFor(() => {
      const permTab = screen.getByRole("tab", { name: /Permission Matrix/i });
      expect(permTab).toHaveAttribute("aria-selected", "true");
    });

    // Should have the highlighted row
    const highlightedRow = document.querySelector("#perm-row-VOICE_CLONING");
    expect(highlightedRow).toBeInTheDocument();
  });
});
