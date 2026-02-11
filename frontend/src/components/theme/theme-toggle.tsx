"use client";

import { useAtom } from "jotai";
import { themeAtom, type Theme } from "@/lib/stores/theme";

const CYCLE_ORDER: Theme[] = ["light", "dark", "system"];

const ICONS: Record<Theme, string> = {
  light: "\u2600",
  dark: "\u263E",
  system: "\u2699",
};

export function ThemeToggle() {
  const [theme, setTheme] = useAtom(themeAtom);

  const next = CYCLE_ORDER[(CYCLE_ORDER.indexOf(theme) + 1) % CYCLE_ORDER.length];

  return (
    <button
      onClick={() => setTheme(next)}
      className="flex h-6 w-6 items-center justify-center text-[var(--text-sm)] text-[var(--color-label)] hover:text-[var(--color-heading)] transition-colors duration-[var(--transition-fast)]"
      aria-label={`Theme: ${theme}. Click for ${next}`}
    >
      <span aria-hidden="true">{ICONS[theme]}</span>
    </button>
  );
}
