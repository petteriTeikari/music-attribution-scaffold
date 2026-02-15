import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { Provider, createStore } from "jotai";
import { userRoleAtom } from "@/lib/stores/mode";
import { AuraclesBadge, AuraclesBadgeMobile } from "./auracles-badge";

function renderWithRole(role: "artist" | "query", ui: React.ReactElement) {
  const store = createStore();
  store.set(userRoleAtom, role);
  return render(<Provider store={store}>{ui}</Provider>);
}

describe("AuraclesBadge", () => {
  it("renders link to /permissions in artist mode", () => {
    renderWithRole("artist", <AuraclesBadge />);
    const link = screen.getByRole("link", {
      name: /auracles identity/i,
    });
    expect(link).toBeInTheDocument();
    expect(link).toHaveAttribute("href", "/permissions");
  });

  it("shows Au monogram", () => {
    renderWithRole("artist", <AuraclesBadge />);
    expect(screen.getByText("Au")).toBeInTheDocument();
  });

  it("is hidden in query mode", () => {
    renderWithRole("query", <AuraclesBadge />);
    expect(
      screen.queryByRole("link", { name: /auracles identity/i }),
    ).not.toBeInTheDocument();
  });
});

describe("AuraclesBadgeMobile", () => {
  it("renders link to /permissions in artist mode", () => {
    renderWithRole("artist", <AuraclesBadgeMobile />);
    const link = screen.getByRole("link", {
      name: /auracles identity/i,
    });
    expect(link).toBeInTheDocument();
    expect(link).toHaveAttribute("href", "/permissions");
  });

  it("shows Auracles ID label", () => {
    renderWithRole("artist", <AuraclesBadgeMobile />);
    expect(screen.getByText("Auracles ID")).toBeInTheDocument();
  });

  it("is hidden in query mode", () => {
    renderWithRole("query", <AuraclesBadgeMobile />);
    expect(
      screen.queryByRole("link", { name: /auracles identity/i }),
    ).not.toBeInTheDocument();
  });
});
