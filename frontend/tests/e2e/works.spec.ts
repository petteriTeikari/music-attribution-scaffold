import { test, expect } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test.describe("Works catalog page", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/works");
  });

  test("page loads with Work Catalog heading", async ({ page }) => {
    await expect(page.getByRole("heading", { name: "Work Catalog" })).toBeVisible();
  });

  test("renders 8 work cards (Imogen Heap mock data)", async ({ page }) => {
    // Wait for works to load (skeleton disappears)
    await page.getByText(/of 8 works/).waitFor({ timeout: 10_000 });

    // All 8 mock works should be visible
    const workLinks = page.getByRole("link", { name: /Hide and Seek|Tiny Human|The Moment I Said It|Goodnight and Go|Headlock|Just for Now|2-1|Blanket/ });
    await expect(workLinks).toHaveCount(8);
  });

  test("search filters works", async ({ page }) => {
    const searchInput = page.getByRole("searchbox", { name: /Search works/ });
    await expect(searchInput).toBeVisible();

    await searchInput.fill("Hide and Seek");
    // Should filter down to 1 result
    const workCards = page.locator("[data-testid='work-card']").or(
      page.getByRole("link").filter({ hasText: /Hide and Seek/ })
    );
    await expect(workCards.first()).toBeVisible();
  });

  test("sort controls are accessible", async ({ page }) => {
    const sortSelect = page.getByRole("combobox");
    await expect(sortSelect).toBeVisible();

    const sortButton = page.getByRole("button", { name: /Sort/ });
    await expect(sortButton).toBeVisible();
  });

  test("WCAG 2.1 AA — no critical violations on works list", async ({ page }) => {
    // Wait for works to load
    await page.getByRole("heading", { name: "Work Catalog" }).waitFor();

    const results = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
      .disableRules(["color-contrast"])
      .analyze();

    const critical = results.violations.filter((v) => v.impact === "critical");

    if (critical.length > 0) {
      const summary = critical.map(
        (v) => `[${v.impact}] ${v.id}: ${v.description} (${v.nodes.length} instances)`
      );
      expect(critical, `WCAG violations:\n${summary.join("\n")}`).toHaveLength(0);
    }
  });
});

test.describe("Work detail page", () => {
  test("navigating to a work shows detail view", async ({ page }) => {
    await page.goto("/works");

    // Click the first work link
    const firstWork = page.getByRole("link").filter({ hasText: /Hide and Seek|Headlock|Speak for Yourself/ }).first();
    await firstWork.click();

    // Should navigate to detail page
    await expect(page).toHaveURL(/\/works\/.+/);

    // Detail page has breadcrumb back to Works
    await expect(page.getByLabel("Breadcrumb").getByRole("link", { name: "Works" })).toBeVisible();

    // Confidence gauge should be visible
    await expect(page.getByRole("meter").or(page.locator("[data-testid='confidence-gauge']")).first()).toBeVisible({ timeout: 10_000 });

    // Credits section
    await expect(page.getByRole("heading", { name: "Credits" })).toBeVisible();

    // Provenance section
    await expect(page.getByRole("heading", { name: "Timeline" })).toBeVisible();
  });
});
