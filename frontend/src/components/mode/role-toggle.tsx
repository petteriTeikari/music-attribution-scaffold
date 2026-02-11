"use client";

import { useAtom } from "jotai";
import { userRoleAtom, type UserRole } from "@/lib/stores/mode";

const ROLES: { value: UserRole; label: string }[] = [
  { value: "artist", label: "Artist" },
  { value: "query", label: "Query" },
];

export function RoleToggle() {
  const [role, setRole] = useAtom(userRoleAtom);

  return (
    <div
      className="flex items-center rounded-[var(--radius-full)] border border-[var(--color-border)] bg-[var(--color-surface-secondary)] p-[var(--space-1)]"
      role="radiogroup"
      aria-label="User role"
    >
      {ROLES.map((option) => {
        const isActive = role === option.value;
        const accentColor =
          option.value === "artist"
            ? "var(--color-role-artist)"
            : "var(--color-role-query)";

        return (
          <button
            key={option.value}
            role="radio"
            aria-checked={isActive}
            onClick={() => setRole(option.value)}
            className={`
              rounded-[var(--radius-full)]
              px-[var(--space-4)] py-[var(--space-1)]
              text-[var(--text-sm)] font-medium
              transition-all duration-[var(--transition-fast)]
              ${
                isActive
                  ? "shadow-[var(--shadow-sm)]"
                  : "text-[var(--color-muted)] hover:text-[var(--color-body)]"
              }
            `}
            style={
              isActive
                ? {
                    backgroundColor: `${accentColor}15`,
                    color: accentColor,
                    borderColor: accentColor,
                  }
                : undefined
            }
          >
            {option.label}
          </button>
        );
      })}
    </div>
  );
}
