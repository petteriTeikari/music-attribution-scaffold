"use client";

import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useAtomValue } from "jotai";
import { userRoleAtom } from "@/lib/stores/mode";
import { ThemeToggle } from "@/components/theme/theme-toggle";
import { RoleToggle } from "@/components/mode/role-toggle";
import { NotificationBadge } from "@/components/notifications/notification-badge";

interface NavItem {
  href: string;
  label: string;
  artistOnly?: boolean;
}

const NAV_ITEMS: NavItem[] = [
  { href: "/works", label: "Works" },
  { href: "/review", label: "Review", artistOnly: true },
  { href: "/permissions", label: "Permissions" },
];

export function Navigation() {
  const pathname = usePathname();
  const role = useAtomValue(userRoleAtom);
  const [mobileOpen, setMobileOpen] = useState(false);

  const visibleItems = NAV_ITEMS.filter(
    (item) => !item.artistOnly || role === "artist"
  );

  return (
    <>
      {/* Desktop: Fixed vertical sidebar */}
      <nav
        className="fixed left-0 top-0 z-40 hidden h-screen flex-col items-center justify-between border-r border-[var(--color-border)] bg-[var(--color-sidebar)] md:flex"
        style={{ width: "var(--sidebar-width)" }}
        aria-label="Main navigation"
      >
        {/* Top: Logo link */}
        <div className="flex flex-col items-center pt-[var(--space-4)]">
          <Link
            href="/"
            className="flex h-8 w-8 items-center justify-center text-[var(--text-sm)] font-bold text-[var(--color-heading)] hover:text-[var(--color-accent)] transition-colors duration-[var(--transition-fast)]"
            aria-label="Home"
          >
            MA
          </Link>
        </div>

        {/* Middle: Rotated nav links */}
        <div className="flex flex-1 flex-col items-center justify-center gap-[var(--space-8)]">
          {visibleItems.map((item) => {
            const isActive =
              pathname === item.href ||
              pathname.startsWith(`${item.href}/`);
            return (
              <Link
                key={item.href}
                href={item.href}
                className={`editorial-caps text-[var(--text-xs)] transition-colors duration-[var(--transition-fast)] ${
                  isActive
                    ? "text-[var(--color-accent)]"
                    : "text-[var(--color-label)] hover:text-[var(--color-heading)]"
                }`}
                style={{
                  writingMode: "vertical-rl",
                  transform: "rotate(180deg)",
                }}
                aria-current={isActive ? "page" : undefined}
              >
                {item.label}
              </Link>
            );
          })}
        </div>

        {/* Bottom: Controls + accent square */}
        <div className="flex flex-col items-center gap-[var(--space-3)] pb-[var(--space-4)]">
          <RoleToggle />
          <NotificationBadge />
          <ThemeToggle />
          <div className="accent-square" aria-hidden="true" />
        </div>
      </nav>

      {/* Mobile: Top bar + hamburger */}
      <nav
        className="fixed left-0 top-0 z-40 flex w-full items-center justify-between border-b border-[var(--color-border)] bg-[var(--color-surface)] px-[var(--space-4)] py-[var(--space-3)] md:hidden"
        aria-label="Mobile navigation"
      >
        <Link
          href="/"
          className="text-[var(--text-sm)] font-bold text-[var(--color-heading)]"
        >
          MA
        </Link>

        <button
          onClick={() => setMobileOpen(!mobileOpen)}
          className="flex h-8 w-8 items-center justify-center text-[var(--color-heading)]"
          aria-label={mobileOpen ? "Close menu" : "Open menu"}
          aria-expanded={mobileOpen}
        >
          {mobileOpen ? (
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true">
              <path d="M5 5l10 10M15 5L5 15" stroke="currentColor" strokeWidth="1.5" />
            </svg>
          ) : (
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true">
              <path d="M3 6h14M3 10h14M3 14h14" stroke="currentColor" strokeWidth="1.5" />
            </svg>
          )}
        </button>
      </nav>

      {/* Mobile: Slide-over overlay */}
      {mobileOpen && (
        <>
          <div
            className="fixed inset-0 z-40 bg-black/30 md:hidden"
            onClick={() => setMobileOpen(false)}
            aria-hidden="true"
          />
          <div className="fixed right-0 top-0 z-50 flex h-screen w-64 flex-col border-l border-[var(--color-border)] bg-[var(--color-surface)] p-[var(--space-6)] md:hidden">
            <button
              onClick={() => setMobileOpen(false)}
              className="mb-[var(--space-8)] self-end text-[var(--color-label)]"
              aria-label="Close menu"
            >
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true">
                <path d="M5 5l10 10M15 5L5 15" stroke="currentColor" strokeWidth="1.5" />
              </svg>
            </button>

            <div className="flex flex-col gap-[var(--space-4)]">
              {visibleItems.map((item) => {
                const isActive =
                  pathname === item.href ||
                  pathname.startsWith(`${item.href}/`);
                return (
                  <Link
                    key={item.href}
                    href={item.href}
                    onClick={() => setMobileOpen(false)}
                    className={`editorial-caps text-[var(--text-sm)] py-[var(--space-2)] transition-colors duration-[var(--transition-fast)] ${
                      isActive
                        ? "text-[var(--color-accent)]"
                        : "text-[var(--color-label)] hover:text-[var(--color-heading)]"
                    }`}
                    aria-current={isActive ? "page" : undefined}
                  >
                    {item.label}
                  </Link>
                );
              })}
            </div>

            <div className="mt-auto flex flex-col gap-[var(--space-3)]">
              <RoleToggle />
              <ThemeToggle />
            </div>
          </div>
        </>
      )}
    </>
  );
}
