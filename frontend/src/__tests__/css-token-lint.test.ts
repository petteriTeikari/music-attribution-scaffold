/**
 * CSS Token Lint Tests
 *
 * Enforces single-source-of-truth for design tokens by catching
 * patterns that bypass Tailwind v4's type system.
 *
 * Background: In Tailwind v4, arbitrary values like text-[var(...)]
 * generate color instead of font-size because the text- prefix is
 * ambiguous (font-size OR color). This silently breaks font sizes.
 *
 * The [var(--...)] arbitrary value syntax is BANNED in className
 * strings. All tokens are either registered in @theme (colors,
 * radius, shadows) or map to Tailwind's built-in scale (spacing,
 * transitions).
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

  describe("[var(--*)] arbitrary values are banned in className strings", () => {
    // Catch ALL [var(--...)] patterns in className-like contexts.
    // This covers spacing, colors, accent, radius, transitions, shadows.
    //
    // Correct alternatives (use Tailwind utilities or @theme tokens):
    //   Spacing → px-8, Colors → text-heading, Accent → accent-primary,
    //   Radius → rounded-md, Transitions → duration-150, Shadows → shadow-md
    const VAR_ARBITRARY_PATTERN = /\[var\(--/g;

    it.each(tsxFiles)("no [var(--*)] arbitrary values in %s", (filePath) => {
      const content = readFileSync(filePath, "utf-8");
      const lines = content.split("\n");
      const violations: string[] = [];

      lines.forEach((line, i) => {
        // Skip comments
        if (line.trim().startsWith("//") || line.trim().startsWith("*")) return;
        // Skip import lines
        if (line.trim().startsWith("import ")) return;
        // Allow inline style objects — var(--*) is fine in style={{ }}
        // We ban ALL [var(-- which is the Tailwind arbitrary value syntax.
        // The accent-color CSS property via [var()] is NOT an exception.
        // Turbopack's parser rejects the generated CSS. Use accent-primary.
        const matches = line.match(VAR_ARBITRARY_PATTERN);
        if (matches) {
          violations.push(
            `  Line ${i + 1}: ${matches.length} instance(s) — ${line.trim().substring(0, 100)}`,
          );
        }
      });

      expect(
        violations,
        `Found [var(--*)] arbitrary value patterns (use Tailwind utilities or @theme tokens):\n${violations.join("\n")}\n\n` +
          // NOTE: Fix guide uses string concat to prevent Tailwind from
          // scanning these examples as class names and generating broken CSS.
          `Fix guide:\n` +
          `  Spacing:     px-` + `[var(--space-8)] → px-8\n` +
          `  Colors:      text-` + `[var(--color-heading)] → text-heading\n` +
          `  Accent:      accent-` + `[var(--color-primary)] → accent-primary\n` +
          `  Radius:      rounded-` + `[var(--radius-md)] → rounded-md\n` +
          `  Transitions: duration-` + `[var(--transition-fast)] → duration-150\n` +
          `  Shadows:     shadow-` + `[var(--shadow-md)] → shadow-md`,
      ).toHaveLength(0);
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

  describe("no undefined --color-text or --color-text-muted tokens in .tsx files", () => {
    // These tokens do NOT exist in globals.css. Correct alternatives:
    //   --color-text       → --color-heading or --color-body
    //   --color-text-muted → --color-muted
    const UNDEFINED_TOKEN_PATTERN = /var\(--color-text\b(?!-decoration|-transform)/g;
    const UNDEFINED_MUTED_PATTERN = /var\(--color-text-muted\)/g;

    it.each(tsxFiles)("no undefined --color-text tokens in %s", (filePath) => {
      const content = readFileSync(filePath, "utf-8");
      const lines = content.split("\n");
      const violations: string[] = [];

      lines.forEach((line, i) => {
        if (line.trim().startsWith("//") || line.trim().startsWith("*")) return;
        const textMatches = line.match(UNDEFINED_TOKEN_PATTERN);
        const mutedMatches = line.match(UNDEFINED_MUTED_PATTERN);
        if (textMatches) {
          violations.push(`  Line ${i + 1}: var(--color-text) → use --color-heading or --color-body`);
        }
        if (mutedMatches) {
          violations.push(`  Line ${i + 1}: var(--color-text-muted) → use --color-muted`);
        }
      });

      expect(
        violations,
        `Found references to undefined CSS tokens:\n${violations.join("\n")}`,
      ).toHaveLength(0);
    });
  });

  describe("globals.css must not contain feTurbulence SVG filter", () => {
    it("no feTurbulence noise overlay (CPU-rendered, causes jank)", () => {
      const globalsPath = resolve(SRC_DIR, "app", "globals.css");
      const content = readFileSync(globalsPath, "utf-8");
      expect(content).not.toContain("feTurbulence");
      expect(content).not.toContain("fractalNoise");
    });
  });

  describe("globals.css excludes __tests__ from Tailwind class scanning", () => {
    it("@source not directive excludes test directory", () => {
      const globalsPath = resolve(SRC_DIR, "app", "globals.css");
      const content = readFileSync(globalsPath, "utf-8");
      expect(content).toContain('@source not "../__tests__"');
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
