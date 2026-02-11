/**
 * CSS Token Lint Tests
 *
 * Enforces single-source-of-truth for design tokens by catching
 * patterns that bypass Tailwind v4's type system.
 *
 * Background: In Tailwind v4, `text-[var(--text-xl)]` generates
 * `color: var(--text-xl)` instead of `font-size: var(--text-xl)`
 * because the `text-` prefix is ambiguous (font-size OR color).
 * This silently breaks all font sizes with no build error.
 *
 * See: .claude/memory/css-tailwind-v4-pitfalls.md
 */

import { readFileSync } from "fs";
import { resolve } from "path";
import { describe, expect, it } from "vitest";

// Recursively find all .tsx files under src/
function findTsxFiles(dir: string): string[] {
  const { readdirSync, statSync } = require("fs");
  const { join } = require("path");
  const results: string[] = [];

  for (const entry of readdirSync(dir)) {
    const fullPath = join(dir, entry);
    const stat = statSync(fullPath);
    if (stat.isDirectory()) {
      // Skip __tests__, node_modules
      if (entry === "__tests__" || entry === "node_modules") continue;
      results.push(...findTsxFiles(fullPath));
    } else if (entry.endsWith(".tsx") || entry.endsWith(".ts")) {
      // Skip test files and this file
      if (entry.endsWith(".test.ts") || entry.endsWith(".test.tsx")) continue;
      results.push(fullPath);
    }
  }

  return results;
}

const SRC_DIR = resolve(__dirname, "..");

describe("CSS Token Lint", () => {
  const tsxFiles = findTsxFiles(SRC_DIR);

  describe("text-[var(--text-*)] is banned (generates color instead of font-size)", () => {
    // Pattern: text-[var(--text-xs)], text-[var(--text-2xl)], etc.
    const BANNED_FONT_SIZE_PATTERN = /text-\[var\(--text-[a-z0-9]+\)\]/g;

    it.each(tsxFiles)("no broken font-size patterns in %s", (filePath) => {
      const content = readFileSync(filePath, "utf-8");
      const matches = content.match(BANNED_FONT_SIZE_PATTERN);
      expect(
        matches,
        `Found banned pattern(s): ${matches?.join(", ")}. ` +
          `Use Tailwind utilities (text-xl, text-2xl) instead of text-[var(--text-*)]. ` +
          `See .claude/memory/css-tailwind-v4-pitfalls.md`,
      ).toBeNull();
    });
  });

  describe("text-[var(--color-*)] should use @theme utilities instead", () => {
    // Pattern: text-[var(--color-heading)], text-[var(--color-muted)], etc.
    // These WORK but are redundant — @theme registers them as text-heading, text-muted
    const REDUNDANT_COLOR_PATTERN = /text-\[var\(--color-(heading|subheading|body|label|muted|accent|primary|teal)\)\]/g;

    it.each(tsxFiles)("no redundant color patterns in %s", (filePath) => {
      const content = readFileSync(filePath, "utf-8");
      const matches = content.match(REDUNDANT_COLOR_PATTERN);
      // Warn but don't fail — these work, they're just not idiomatic
      if (matches) {
        console.warn(
          `[warn] ${filePath}: Found text-[var(--color-*)] that could use @theme utility: ${matches.join(", ")}`,
        );
      }
    });
  });

  describe("no hardcoded hex colors in .tsx files", () => {
    // Pattern: hex colors like #1E3A5F, #fff, #F8F6F0 (not in comments or strings)
    // Allow: className strings that reference CSS custom properties
    const HEX_COLOR_PATTERN = /#[0-9a-fA-F]{3,8}(?![0-9a-fA-F])/g;

    it.each(tsxFiles)("no hardcoded hex colors in %s", (filePath) => {
      const content = readFileSync(filePath, "utf-8");
      const lines = content.split("\n");
      const violations: string[] = [];

      lines.forEach((line, i) => {
        // Skip comments
        if (line.trim().startsWith("//") || line.trim().startsWith("*")) return;
        // Skip import lines
        if (line.trim().startsWith("import ")) return;

        const matches = line.match(HEX_COLOR_PATTERN);
        if (matches) {
          // Filter out common false positives
          const realMatches = matches.filter((m) => {
            // Skip hex in URLs, data URIs
            if (line.includes("url(") || line.includes("data:")) return false;
            // Skip hash in IDs
            if (line.includes('href="#') || line.includes('id="')) return false;
            return true;
          });
          if (realMatches.length > 0) {
            violations.push(`  Line ${i + 1}: ${realMatches.join(", ")} — ${line.trim().substring(0, 80)}`);
          }
        }
      });

      expect(
        violations,
        `Found hardcoded hex colors (use CSS custom properties):\n${violations.join("\n")}`,
      ).toHaveLength(0);
    });
  });

  describe("globals.css does not define --text-* vars (they conflict with Tailwind)", () => {
    it("no --text-* custom properties in :root", () => {
      const globalsPath = resolve(SRC_DIR, "app", "globals.css");
      const content = readFileSync(globalsPath, "utf-8");

      // Extract :root block content
      const rootMatch = content.match(/:root\s*\{([^}]*(?:\{[^}]*\}[^}]*)*)\}/);
      if (rootMatch) {
        const rootContent = rootMatch[1];
        const textVars = rootContent.match(/--text-[a-z0-9]+\s*:/g);
        expect(
          textVars,
          `Found --text-* vars in :root that conflict with Tailwind v4 built-in scale: ${textVars?.join(", ")}. ` +
            `Remove them — Tailwind v4 defines identical values internally.`,
        ).toBeNull();
      }
    });
  });
});
