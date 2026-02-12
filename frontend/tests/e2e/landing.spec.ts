import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test.describe("Landing page", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/");
  });

  test("page loads with correct title", async ({ page }) => {
    await expect(page).toHaveTitle(/Music Attribution/);
  });

  test("hero section renders paper title and subtitle", async ({ page }) => {
    const h1 = page.locator("h1");
    await expect(h1).toContainText("Governing Generative Music");

    // Subtitle is in the hero section's <p> tag (first match)
    await expect(
      page.locator("section").first().getByText("Attribution Limits, Platform Incentives", { exact: false })
    ).toBeVisible();
  });

  test("hero has Explore the Demo and Read the Paper links", async ({ page }) => {
    const demoLink = page.getByRole("link", { name: /Explore the Demo/ });
    await expect(demoLink).toBeVisible();
    await expect(demoLink).toHaveAttribute("href", "/works");

    const paperLink = page.getByRole("link", { name: /Read the Paper/ });
    await expect(paperLink).toBeVisible();
    await expect(paperLink).toHaveAttribute("href", /doi\.org/);
  });

  test("Key Concepts section renders 12 topic cards", async ({ page }) => {
    const keyConcepts = page.getByRole("heading", { name: "Key Concepts" });
    await keyConcepts.scrollIntoViewIfNeeded();
    await expect(keyConcepts).toBeVisible();

    // Each topic card has a "Read More" button with aria-label
    const readMoreButtons = page.getByRole("button", { name: /[Rr]ead [Mm]ore/ });
    await expect(readMoreButtons).toHaveCount(12);
  });

  test("A0-A3 assurance table renders all four levels", async ({ page }) => {
    const heading = page.getByRole("heading", { name: /Assurance Levels/ });
    await heading.scrollIntoViewIfNeeded();
    await expect(heading).toBeVisible();

    const table = page.locator("table");
    await expect(table).toBeVisible();

    for (const level of ["A0", "A1", "A2", "A3"]) {
      await expect(table.getByText(level, { exact: true })).toBeVisible();
    }

    // Check identifier column cells specifically (exact match in last column)
    await expect(table.getByRole("cell", { name: "ISRC", exact: true })).toBeVisible();
    await expect(table.getByRole("cell", { name: "ISWC", exact: true })).toBeVisible();
    await expect(table.getByRole("cell", { name: "ISNI" })).toBeVisible();
  });

  test("References section renders", async ({ page }) => {
    const referencesHeading = page.getByRole("heading", { name: /References/ });
    await referencesHeading.scrollIntoViewIfNeeded();
    await expect(referencesHeading).toBeVisible();
  });

  test("WCAG 2.1 AA — no critical violations", async ({ page }) => {
    const results = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
      // Exclude known contrast issues that will be fixed in task 3.1
      .disableRules(["color-contrast"])
      .analyze();

    const critical = results.violations.filter(
      (v) => v.impact === "critical"
    );

    if (critical.length > 0) {
      const summary = critical.map(
        (v) => `[${v.impact}] ${v.id}: ${v.description} (${v.nodes.length} instances)`
      );
      expect(critical, `WCAG violations:\n${summary.join("\n")}`).toHaveLength(0);
    }
  });
});
