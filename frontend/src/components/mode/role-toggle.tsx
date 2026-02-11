"use client";

import { useAtom } from "jotai";
import { userRoleAtom, type UserRole } from "@/lib/stores/mode";

const ROLES: { value: UserRole; label: string }[] = [
  { value: "artist", label: "A" },
  { value: "query", label: "Q" },
];

export function RoleToggle() {
  const [role, setRole] = useAtom(userRoleAtom);

  return (
    <div
      className="flex flex-col items-center gap-[var(--space-1)]"
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
            aria-label={option.value === "artist" ? "Artist mode" : "Query mode"}
            onClick={() => setRole(option.value)}
            className={`
              flex h-6 w-6 items-center justify-center
              text-[10px] font-bold
              transition-all duration-[var(--transition-fast)]
              ${
                isActive
                  ? ""
                  : "text-[var(--color-muted)] hover:text-[var(--color-body)]"
              }
            `}
            style={
              isActive
                ? {
                    color: accentColor,
                    borderBottom: `2px solid ${accentColor}`,
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
