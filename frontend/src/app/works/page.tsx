"use client";

import { useEffect } from "react";
import { useAtom, useAtomValue } from "jotai";
import {
  worksAtom,
  worksLoadingAtom,
  filteredWorksAtom,
  searchQueryAtom,
  sortFieldAtom,
  sortDirectionAtom,
  type SortField,
} from "@/lib/stores/works";
import { mockApi } from "@/lib/api/mock-client";
import { WorkCard } from "@/components/works/work-card";

const SORT_OPTIONS: { value: SortField; label: string }[] = [
  { value: "confidence", label: "Confidence" },
  { value: "title", label: "Title" },
  { value: "updated", label: "Last Updated" },
];

export default function WorksPage() {
  const [works, setWorks] = useAtom(worksAtom);
  const [loading, setLoading] = useAtom(worksLoadingAtom);
  const filteredWorks = useAtomValue(filteredWorksAtom);
  const [searchQuery, setSearchQuery] = useAtom(searchQueryAtom);
  const [sortField, setSortField] = useAtom(sortFieldAtom);
  const [sortDirection, setSortDirection] = useAtom(sortDirectionAtom);

  useEffect(() => {
    if (works.length > 0) return;
    setLoading(true);
    mockApi.getWorks().then((data) => {
      setWorks(data);
      setLoading(false);
    });
  }, [works.length, setWorks, setLoading]);

  return (
    <div className="px-[var(--space-8)] py-[var(--space-10)]">
      {/* Header */}
      <div className="mb-[var(--space-8)]">
        <span className="editorial-caps text-xs text-[var(--color-accent)] block mb-[var(--space-2)]">
          Catalog
        </span>
        <h1 className="editorial-display text-4xl text-[var(--color-heading)]">
          Work Catalog
        </h1>
        <p className="mt-[var(--space-2)] text-base text-[var(--color-label)]">
          Attribution records with confidence scoring and provenance lineage.
        </p>
      </div>

      {/* Search + Sort controls */}
      <div className="mb-[var(--space-6)] flex flex-col gap-[var(--space-3)] sm:flex-row sm:items-center sm:justify-between">
        <input
          type="search"
          placeholder="Search works or artists..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="border-b border-[var(--color-border)] bg-transparent px-0 py-[var(--space-2)] text-sm text-[var(--color-body)] placeholder:text-[var(--color-muted)] focus:border-[var(--color-accent)] focus:outline-none sm:max-w-xs"
          aria-label="Search works"
        />

        <div className="flex items-center gap-[var(--space-2)]">
          <label
            htmlFor="sort-select"
            className="editorial-caps text-xs text-[var(--color-label)]"
          >
            Sort:
          </label>
          <select
            id="sort-select"
            value={sortField}
            onChange={(e) => setSortField(e.target.value as SortField)}
            className="border-b border-[var(--color-border)] bg-transparent px-[var(--space-2)] py-[var(--space-2)] text-sm text-[var(--color-body)] focus:border-[var(--color-accent)] focus:outline-none"
          >
            {SORT_OPTIONS.map((opt) => (
              <option key={opt.value} value={opt.value}>
                {opt.label}
              </option>
            ))}
          </select>
          <button
            onClick={() =>
              setSortDirection((d) => (d === "asc" ? "desc" : "asc"))
            }
            className="border-b border-[var(--color-border)] px-[var(--space-2)] py-[var(--space-2)] text-sm text-[var(--color-body)] hover:border-[var(--color-accent)] transition-colors"
            aria-label={`Sort ${sortDirection === "asc" ? "descending" : "ascending"}`}
          >
            {sortDirection === "asc" ? "↑" : "↓"}
          </button>
        </div>
      </div>

      <div className="accent-line mb-[var(--space-6)]" style={{ opacity: 0.3 }} />

      {/* Works list */}
      {loading ? (
        <div className="space-y-[var(--space-4)]">
          {Array.from({ length: 4 }).map((_, i) => (
            <div
              key={i}
              className="h-20 animate-pulse bg-[var(--color-surface-secondary)]"
            />
          ))}
        </div>
      ) : filteredWorks.length === 0 ? (
        <div className="py-[var(--space-20)] text-center">
          <p className="editorial-display text-2xl text-[var(--color-muted)]">
            {searchQuery ? "No works match your search." : "No works found."}
          </p>
          {searchQuery && (
            <button
              onClick={() => setSearchQuery("")}
              className="mt-[var(--space-4)] text-sm text-[var(--color-accent)] underline underline-offset-2"
            >
              Clear search
            </button>
          )}
        </div>
      ) : (
        <div className="divide-y divide-[var(--color-border)]">
          {filteredWorks.map((work) => (
            <WorkCard key={work.attribution_id} work={work} />
          ))}
        </div>
      )}

      {/* Result count */}
      {!loading && filteredWorks.length > 0 && (
        <p className="mt-[var(--space-8)] text-xs text-[var(--color-muted)] editorial-caps">
          {filteredWorks.length} of {works.length} works
        </p>
      )}
    </div>
  );
}
