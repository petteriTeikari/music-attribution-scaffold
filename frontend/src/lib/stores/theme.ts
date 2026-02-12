import { atom } from "jotai";

export type Theme = "light" | "dark" | "system";

export const themeAtom = atom<Theme>("system");

// TODO: Atom not yet used in any component
export const resolvedThemeAtom = atom<"light" | "dark">((get) => {
  const theme = get(themeAtom);
  if (theme === "system") {
    if (typeof window === "undefined") return "light";
    return window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }
  return theme;
});
