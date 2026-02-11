"use client";

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

  const visibleItems = NAV_ITEMS.filter(
    (item) => !item.artistOnly || role === "artist"
  );

  return (
    <nav
      className="border-b border-[var(--color-border)] bg-[var(--color-surface)]"
      aria-label="Main navigation"
    >
      <div className="mx-auto flex max-w-7xl items-center justify-between px-[var(--space-6)] py-[var(--space-3)]">
        {/* Logo & brand */}
        <div className="flex items-center gap-[var(--space-8)]">
          <Link
            href="/"
            className="text-[var(--text-lg)] font-bold text-[var(--color-heading)] hover:text-[var(--color-primary)] transition-colors duration-[var(--transition-fast)]"
          >
            Music Attribution
          </Link>

          {/* Nav links */}
          <div className="hidden items-center gap-[var(--space-1)] md:flex">
            {visibleItems.map((item) => {
              const isActive = pathname === item.href || pathname.startsWith(`${item.href}/`);
              return (
                <Link
                  key={item.href}
                  href={item.href}
                  className={`
                    rounded-[var(--radius-md)]
                    px-[var(--space-3)] py-[var(--space-2)]
                    text-[var(--text-sm)] font-medium
                    transition-colors duration-[var(--transition-fast)]
                    ${
                      isActive
                        ? "bg-[var(--color-primary-muted)] text-[var(--color-primary)]"
                        : "text-[var(--color-label)] hover:bg-[var(--color-surface-secondary)] hover:text-[var(--color-body)]"
                    }
                  `}
                  aria-current={isActive ? "page" : undefined}
                >
                  {item.label}
                </Link>
              );
            })}
          </div>
        </div>

        {/* Right side controls */}
        <div className="flex items-center gap-[var(--space-3)]">
          <RoleToggle />
          <NotificationBadge />
          <ThemeToggle />
        </div>
      </div>
    </nav>
  );
}
