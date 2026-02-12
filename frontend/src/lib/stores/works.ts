import { atom } from "jotai";
import type { AttributionRecord } from "@/lib/types/attribution";

export const worksAtom = atom<AttributionRecord[]>([]);
export const worksLoadingAtom = atom<boolean>(false);
// TODO: Atom not yet used in any component
export const selectedWorkAtom = atom<AttributionRecord | null>(null);

export type SortField = "confidence" | "title" | "updated";
export type SortDirection = "asc" | "desc";

export const sortFieldAtom = atom<SortField>("confidence");
export const sortDirectionAtom = atom<SortDirection>("desc");
export const searchQueryAtom = atom<string>("");

export const filteredWorksAtom = atom<AttributionRecord[]>((get) => {
  const works = get(worksAtom);
  const query = get(searchQueryAtom).toLowerCase();
  const sortField = get(sortFieldAtom);
  const sortDir = get(sortDirectionAtom);

  let filtered = works;

  // Filter by search query
  if (query) {
    filtered = filtered.filter(
      (w) =>
        w.work_title.toLowerCase().includes(query) ||
        w.artist_name.toLowerCase().includes(query)
    );
  }

  // Sort
  const sorted = [...filtered].sort((a, b) => {
    let cmp = 0;
    switch (sortField) {
      case "confidence":
        cmp = a.confidence_score - b.confidence_score;
        break;
      case "title":
        cmp = a.work_title.localeCompare(b.work_title);
        break;
      case "updated":
        cmp =
          new Date(a.updated_at).getTime() - new Date(b.updated_at).getTime();
        break;
    }
    return sortDir === "desc" ? -cmp : cmp;
  });

  return sorted;
});
