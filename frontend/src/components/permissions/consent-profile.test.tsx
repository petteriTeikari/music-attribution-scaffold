import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent, within } from "@testing-library/react";
import { Provider } from "jotai";
import { useHydrateAtoms } from "jotai/utils";
import type { ReactNode } from "react";
import { ConsentProfile } from "./consent-profile";
import { MOCK_PERMISSIONS } from "@/lib/data/mock-permissions";
import { proficiencyStateAtom } from "@/lib/stores/proficiency";
import type { ProficiencyState } from "@/lib/stores/proficiency";

// Mock PostHog
vi.mock("@/lib/analytics/events", () => ({
  trackEvent: vi.fn(),
  EVENTS: {
    TOOLTIP_SHOWN: "tooltip_shown",
    TOOLTIP_DISMISSED: "tooltip_dismissed",
    ONBOARDING_STEP_COMPLETED: "onboarding_step_completed",
  },
}));

function HydrateAtoms({
  initialValues,
  children,
}: {
  initialValues: [typeof proficiencyStateAtom, ProficiencyState][];
  children: ReactNode;
}) {
  useHydrateAtoms(initialValues);
  return children;
}

function NoviceProvider({ children }: { children: ReactNode }) {
  const state: ProficiencyState = {
    review: { interactions: 0, successes: 0 },
    feedback: { interactions: 0, successes: 0 },
    confidence_reading: { interactions: 0, successes: 0 },
    permissions: { interactions: 0, successes: 0 },
  };
  return (
    <Provider>
      <HydrateAtoms initialValues={[[proficiencyStateAtom, state]]}>
        {children}
      </HydrateAtoms>
    </Provider>
  );
}

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

  it("shows count dot dropdown with entry names on hover", () => {
    render(<ConsentProfile permissions={permissions} />);
    // "4 allow" in AI & Generation group
    const allowBuckets = screen.getAllByText("4 allow");
    // Hover the allow bucket
    fireEvent.mouseEnter(allowBuckets[0].closest("[data-count-bucket]")!);
    // Should show a dropdown with permission names
    const dropdown = screen.getByRole("listbox");
    expect(dropdown).toBeInTheDocument();
    // Should contain specific permission names
    expect(within(dropdown).getByText("Ai Training")).toBeInTheDocument();
    expect(within(dropdown).getByText("Lyrics In Chatbots")).toBeInTheDocument();
  });

  it("hides count dot dropdown by default", () => {
    render(<ConsentProfile permissions={permissions} />);
    expect(screen.queryByRole("listbox")).not.toBeInTheDocument();
  });

  it("count dot dropdown is keyboard accessible", () => {
    render(<ConsentProfile permissions={permissions} />);
    const buckets = screen.getAllByText("4 allow");
    const bucket = buckets[0].closest("[data-count-bucket]")!;
    expect(bucket).toHaveAttribute("aria-haspopup", "listbox");
  });

  it("passes onNavigateToEntry callback down to count bucket dropdowns", () => {
    const onNavigate = vi.fn();
    render(
      <ConsentProfile permissions={permissions} onNavigateToEntry={onNavigate} />,
    );
    const allowBuckets = screen.getAllByText("4 allow");
    fireEvent.mouseEnter(allowBuckets[0].closest("[data-count-bucket]")!);
    const dropdown = screen.getByRole("listbox");
    const firstItem = within(dropdown).getAllByRole("option")[0];
    fireEvent.click(firstItem);
    expect(onNavigate).toHaveBeenCalled();
  });

  it("renders subtitle under each group label", () => {
    render(<ConsentProfile permissions={permissions} />);
    expect(
      screen.getByText("Training, voice, style, and dataset permissions"),
    ).toBeInTheDocument();
    expect(
      screen.getByText("Streaming, download, sync, and cover licenses"),
    ).toBeInTheDocument();
    expect(
      screen.getByText("Remix, sample, and derivative work approvals"),
    ).toBeInTheDocument();
  });
});

describe("ConsentProfile onboarding", () => {
  const permissions = MOCK_PERMISSIONS.permissions;

  it("shows step 0 onboarding tooltip wrapping header for novice users", async () => {
    render(
      <NoviceProvider>
        <ConsentProfile permissions={permissions} onboardingEnabled />
      </NoviceProvider>,
    );
    // Wait for auto-show delay
    await vi.waitFor(() => {
      const tooltips = screen.getAllByRole("tooltip");
      expect(tooltips.length).toBeGreaterThanOrEqual(1);
    }, { timeout: 1000 });
    // Step 0 tooltip mentions consent profile
    const tooltip = screen.getAllByRole("tooltip")[0];
    expect(tooltip.textContent?.toLowerCase()).toContain("consent");
  });

  it("advances to step 1 after dismissing step 0", async () => {
    render(
      <NoviceProvider>
        <ConsentProfile permissions={permissions} onboardingEnabled />
      </NoviceProvider>,
    );
    await vi.waitFor(() => {
      expect(screen.getAllByRole("tooltip").length).toBeGreaterThanOrEqual(1);
    }, { timeout: 1000 });
    // Click "Got it" to dismiss step 0
    const gotItButtons = screen.getAllByText("Got it");
    fireEvent.click(gotItButtons[0]);
    // Step 1 should appear — mentions count dots
    await vi.waitFor(() => {
      const tooltips = screen.getAllByRole("tooltip");
      const step1 = tooltips.find((t) =>
        t.textContent?.toLowerCase().includes("hover"),
      );
      expect(step1).toBeTruthy();
    }, { timeout: 1000 });
  });
});
