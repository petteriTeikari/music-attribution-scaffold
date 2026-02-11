import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { PermissionMatrix } from "./permission-matrix";
import type { PermissionEntry } from "@/lib/types/permissions";

const MOCK_PERMISSIONS: PermissionEntry[] = [
  {
    permission_type: "AI_TRAINING",
    value: "ALLOW_WITH_ATTRIBUTION",
    conditions: [],
    royalty_rate: null,
    attribution_requirement: "Credit in training manifest",
    territory: null,
  },
  {
    permission_type: "VOICE_CLONING",
    value: "DENY",
    conditions: [],
    royalty_rate: null,
    attribution_requirement: null,
    territory: null,
  },
  {
    permission_type: "STREAM",
    value: "ALLOW",
    conditions: [],
    royalty_rate: null,
    attribution_requirement: null,
    territory: null,
  },
];

describe("PermissionMatrix", () => {
  it("renders all permission rows", () => {
    render(<PermissionMatrix permissions={MOCK_PERMISSIONS} />);
    expect(screen.getByText("AI Training")).toBeInTheDocument();
    expect(screen.getByText("Voice Cloning")).toBeInTheDocument();
    expect(screen.getByText("Stream")).toBeInTheDocument();
  });

  it("shows correct status badges", () => {
    render(<PermissionMatrix permissions={MOCK_PERMISSIONS} />);
    expect(screen.getByText("Allow + Credit")).toBeInTheDocument();
    expect(screen.getByText("Deny")).toBeInTheDocument();
    expect(screen.getByText("Allow")).toBeInTheDocument();
  });

  it("shows attribution requirement", () => {
    render(<PermissionMatrix permissions={MOCK_PERMISSIONS} />);
    expect(
      screen.getByText("Credit in training manifest")
    ).toBeInTheDocument();
  });
});
