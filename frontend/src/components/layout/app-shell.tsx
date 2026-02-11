"use client";

import { Navigation } from "./navigation";

export function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-[var(--color-surface)]">
      <Navigation />

      {/* Main content: offset by sidebar on desktop, offset by top bar on mobile */}
      <main
        className="min-h-screen pt-[48px] md:pt-0"
        style={{ marginLeft: "var(--sidebar-width)" }}
      >
        <div className="md:block hidden">{/* spacer for desktop — no top offset needed */}</div>
        {children}
      </main>

      {/* Footer */}
      <footer
        className="border-t border-[var(--color-border)] px-[var(--space-8)] py-[var(--space-12)]"
        style={{ marginLeft: "var(--sidebar-width)" }}
      >
        <div className="flex items-center justify-between">
          <p
            className="editorial-caps text-xs text-[var(--color-muted)]"
            style={{
              writingMode: "vertical-rl",
              transform: "rotate(180deg)",
              height: "fit-content",
            }}
          >
            Music Attribution Scaffold
          </p>
          <div className="flex-1 px-[var(--space-8)]">
            <div className="accent-line" />
          </div>
          <p className="text-xs text-[var(--color-muted)]">
            Open-source research companion to{" "}
            <a
              href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087"
              target="_blank"
              rel="noopener noreferrer"
              className="text-[var(--color-primary)] underline underline-offset-2 hover:text-[var(--color-primary-hover)]"
            >
              SSRN No. 6109087
            </a>
          </p>
        </div>
      </footer>
    </div>
  );
}
