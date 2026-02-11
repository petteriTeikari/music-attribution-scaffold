import { describe, it, expect } from "vitest";
import { createStore } from "jotai";
import {
  worksAtom,
  searchQueryAtom,
  sortFieldAtom,
  sortDirectionAtom,
  filteredWorksAtom,
} from "./works";
import { MOCK_WORKS } from "@/lib/data/mock-works";

describe("works store", () => {
  it("filteredWorksAtom returns all works when no filter", () => {
    const store = createStore();
    store.set(worksAtom, MOCK_WORKS);
    const filtered = store.get(filteredWorksAtom);
    expect(filtered).toHaveLength(MOCK_WORKS.length);
  });

  it("filters works by search query", () => {
    const store = createStore();
    store.set(worksAtom, MOCK_WORKS);
    store.set(searchQueryAtom, "hide");
    const filtered = store.get(filteredWorksAtom);
    expect(filtered.length).toBeGreaterThanOrEqual(1);
    expect(filtered[0].work_title).toBe("Hide and Seek");
  });

  it("sorts works by confidence descending by default", () => {
    const store = createStore();
    store.set(worksAtom, MOCK_WORKS);
    store.set(sortFieldAtom, "confidence");
    store.set(sortDirectionAtom, "desc");
    const filtered = store.get(filteredWorksAtom);
    for (let i = 1; i < filtered.length; i++) {
      expect(filtered[i - 1].confidence_score).toBeGreaterThanOrEqual(
        filtered[i].confidence_score
      );
    }
  });

  it("sorts works by title ascending", () => {
    const store = createStore();
    store.set(worksAtom, MOCK_WORKS);
    store.set(sortFieldAtom, "title");
    store.set(sortDirectionAtom, "asc");
    const filtered = store.get(filteredWorksAtom);
    for (let i = 1; i < filtered.length; i++) {
      expect(
        filtered[i - 1].work_title.localeCompare(filtered[i].work_title)
      ).toBeLessThanOrEqual(0);
    }
  });
});
