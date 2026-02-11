"use client";

import { Navigation } from "./navigation";

export function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex min-h-screen flex-col bg-[var(--color-surface)]">
      <Navigation />
      <main className="flex-1">{children}</main>
      <footer className="border-t border-[var(--color-border)] px-[var(--space-6)] py-[var(--space-8)]">
        <div className="mx-auto max-w-7xl">
          <p className="text-[var(--text-sm)] text-[var(--color-muted)]">
            Music Attribution Scaffold — Open-source research companion to{" "}
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
