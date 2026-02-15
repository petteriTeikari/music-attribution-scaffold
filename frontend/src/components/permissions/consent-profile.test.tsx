import { describe, it, expect } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { ConsentProfile } from "./consent-profile";
import { MOCK_PERMISSIONS } from "@/lib/data/mock-permissions";

describe("ConsentProfile", () => {
  const permissions = MOCK_PERMISSIONS.permissions;

  it("renders the Consent Profile header", () => {
    render(<ConsentProfile permissions={permissions} />);
    expect(screen.getByText("Consent Profile")).toBeInTheDocument();
  });

  it("renders 3 group sections with roman numerals", () => {
    render(<ConsentProfile permissions={permissions} />);
    expect(screen.getByText("I")).toBeInTheDocument();
    expect(screen.getByText("II")).toBeInTheDocument();
    expect(screen.getByText("III")).toBeInTheDocument();
  });

  it("renders group labels", () => {
    render(<ConsentProfile permissions={permissions} />);
    expect(screen.getByText("AI & GENERATION")).toBeInTheDocument();
    expect(screen.getByText("DISTRIBUTION & LICENSING")).toBeInTheDocument();
    expect(screen.getByText("CREATIVE DERIVATIVES")).toBeInTheDocument();
  });

  it("shows correct allow/ask/deny counts for AI & Generation", () => {
    render(<ConsentProfile permissions={permissions} />);
    expect(screen.getByText("4 allow")).toBeInTheDocument();
    expect(screen.getByText("2 ask")).toBeInTheDocument();
    expect(screen.getByText("1 deny")).toBeInTheDocument();
  });

  it("shows voice cloning exception mentioning Jen (Futureverse)", () => {
    render(<ConsentProfile permissions={permissions} />);
    expect(screen.getByText("Voice Cloning")).toBeInTheDocument();
    expect(screen.getByText("Jen (Futureverse)")).toBeInTheDocument();
  });

  it("shows Auracles ID", () => {
    render(<ConsentProfile permissions={permissions} />);
    expect(
      screen.getByText("Auracles ID: AU-2025-IH-0001"),
    ).toBeInTheDocument();
  });

  it("shows A3 Identity-Verified assurance level", () => {
    render(<ConsentProfile permissions={permissions} />);
    expect(screen.getByText("A3 Identity-Verified")).toBeInTheDocument();
  });

  it("shows SoundCloud as connected platform with Auracles join link", () => {
    render(<ConsentProfile permissions={permissions} />);
    const link = screen.getByText("SoundCloud");
    expect(link).toBeInTheDocument();
    expect(link.closest("a")).toHaveAttribute("href", "https://auracles.io/soundcloud");
  });

  it("shows Spotify as connected platform", () => {
    render(<ConsentProfile permissions={permissions} />);
    expect(screen.getByText("Spotify")).toBeInTheDocument();
  });

  it("shows info tooltip on hover", () => {
    render(<ConsentProfile permissions={permissions} />);
    // (i) buttons: Auracles ID, SoundCloud, + one per group (3) = 5 total
    const infoButtons = screen.getAllByText("(i)");
    expect(infoButtons.length).toBe(5);

    // Hover a group tooltip
    fireEvent.mouseEnter(infoButtons[2]);
    expect(screen.getByRole("tooltip")).toBeInTheDocument();

    fireEvent.mouseLeave(infoButtons[2]);
    expect(screen.queryByRole("tooltip")).not.toBeInTheDocument();
  });

  it("shows default policy as ASK", () => {
    render(<ConsentProfile permissions={permissions} />);
    expect(screen.getByText("ASK")).toBeInTheDocument();
  });

  it("renders with empty permissions without crashing", () => {
    render(<ConsentProfile permissions={[]} />);
    expect(screen.getByText("Consent Profile")).toBeInTheDocument();
  });
});
