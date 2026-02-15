"use client";

import { useState } from "react";
import dynamic from "next/dynamic";
import { Navigation } from "./navigation";

const AgentSidebar = dynamic(
  () => import("@/components/chat/copilot-sidebar").then((mod) => ({ default: mod.AgentSidebar })),
  { ssr: false, loading: () => null },
);

export function AppShell({ children }: { children: React.ReactNode }) {
  const [agentOpen, setAgentOpen] = useState(false);

  return (
    <div className="min-h-screen bg-surface">
      <Navigation />

      {/* Main content: offset by sidebar on desktop, offset by top bar on mobile */}
      <main
        className="min-h-screen pt-[48px] md:pt-0"
        style={{ marginLeft: "var(--sidebar-width)" }}
      >
        <div className="md:block hidden">{/* spacer for desktop — no top offset needed */}</div>
        {children}
      </main>

      {/* Agent toggle button — fixed bottom-right */}
      <button
        onClick={() => setAgentOpen((prev) => !prev)}
        className="fixed bottom-6 right-6 z-40 flex h-12 w-12 items-center justify-center bg-accent text-white transition-colors duration-150 hover:bg-accent-hover"
        aria-label={agentOpen ? "Close agent chat" : "Open agent chat"}
        title="Attribution Agent"
      >
        <svg
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          {agentOpen ? (
            <>
              <line x1="18" y1="6" x2="6" y2="18" />
              <line x1="6" y1="6" x2="18" y2="18" />
            </>
          ) : (
            <>
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
            </>
          )}
        </svg>
      </button>

      {/* Agent sidebar */}
      <AgentSidebar open={agentOpen} onOpenChange={setAgentOpen} />

      {/* Footer */}
      <footer
        className="border-t border-border px-8 py-12"
        style={{ marginLeft: "var(--sidebar-width)" }}
      >
        <div className="flex items-center justify-between">
          <p
            className="editorial-caps text-xs text-muted"
            style={{
              writingMode: "vertical-rl",
              transform: "rotate(180deg)",
              height: "fit-content",
            }}
          >
            Music Attribution Scaffold
          </p>
          <div className="flex-1 px-8">
            <div className="accent-line" />
          </div>
          <p className="text-xs text-muted">
            Open-source research companion to{" "}
            <a
              href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087"
              target="_blank"
              rel="noopener noreferrer"
              className="text-primary underline underline-offset-2 hover:text-primary-hover"
            >
              SSRN No. 6109087
            </a>
          </p>
        </div>
      </footer>
    </div>
  );
}
