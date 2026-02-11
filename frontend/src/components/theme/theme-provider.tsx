"use client";

import { useEffect, useCallback } from "react";
import { useAtom } from "jotai";
import { themeAtom, type Theme } from "@/lib/stores/theme";

function applyTheme(theme: Theme) {
  const root = document.documentElement;
  const isDark =
    theme === "dark" ||
    (theme === "system" &&
      window.matchMedia("(prefers-color-scheme: dark)").matches);

  root.classList.toggle("dark", isDark);
}

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useAtom(themeAtom);

  // Initialize from localStorage
  useEffect(() => {
    const stored = localStorage.getItem("theme") as Theme | null;
    if (stored && ["light", "dark", "system"].includes(stored)) {
      setTheme(stored);
    }
  }, [setTheme]);

  // Apply theme changes
  useEffect(() => {
    applyTheme(theme);
    localStorage.setItem("theme", theme);
  }, [theme]);

  // Listen for system preference changes
  const handleSystemChange = useCallback(() => {
    if (theme === "system") {
      applyTheme("system");
    }
  }, [theme]);

  useEffect(() => {
    const mq = window.matchMedia("(prefers-color-scheme: dark)");
    mq.addEventListener("change", handleSystemChange);
    return () => mq.removeEventListener("change", handleSystemChange);
  }, [handleSystemChange]);

  return <>{children}</>;
}
