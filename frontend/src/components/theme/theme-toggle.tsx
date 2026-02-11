"use client";

import { useAtom } from "jotai";
import { themeAtom, type Theme } from "@/lib/stores/theme";

const THEME_OPTIONS: { value: Theme; label: string; icon: string }[] = [
  { value: "light", label: "Light", icon: "☀" },
  { value: "dark", label: "Dark", icon: "☾" },
  { value: "system", label: "System", icon: "⚙" },
];

export function ThemeToggle() {
  const [theme, setTheme] = useAtom(themeAtom);

  return (
    <div
      className="flex items-center rounded-[var(--radius-full)] border border-[var(--color-border)] bg-[var(--color-surface-secondary)] p-[var(--space-1)]"
      role="radiogroup"
      aria-label="Theme selection"
    >
      {THEME_OPTIONS.map((option) => (
        <button
          key={option.value}
          role="radio"
          aria-checked={theme === option.value}
          aria-label={option.label}
          onClick={() => setTheme(option.value)}
          className={`
            flex items-center justify-center rounded-[var(--radius-full)]
            px-[var(--space-3)] py-[var(--space-1)]
            text-[var(--text-sm)] transition-all duration-[var(--transition-fast)]
            ${
              theme === option.value
                ? "bg-[var(--color-surface-elevated)] text-[var(--color-heading)] shadow-[var(--shadow-sm)]"
                : "text-[var(--color-muted)] hover:text-[var(--color-body)]"
            }
          `}
        >
          <span className="mr-[var(--space-1)]" aria-hidden="true">
            {option.icon}
          </span>
          <span className="hidden sm:inline">{option.label}</span>
        </button>
      ))}
    </div>
  );
}
