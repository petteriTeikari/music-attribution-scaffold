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
    <div className="mx-auto max-w-4xl px-[var(--space-6)] py-[var(--space-10)]">
      {/* Header */}
      <div className="mb-[var(--space-8)]">
        <h1 className="text-[var(--text-3xl)] font-bold text-[var(--color-heading)]">
          Work Catalog
        </h1>
        <p className="mt-[var(--space-2)] text-[var(--text-base)] text-[var(--color-label)]">
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
          className="rounded-[var(--radius-md)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] px-[var(--space-4)] py-[var(--space-2)] text-[var(--text-sm)] text-[var(--color-body)] placeholder:text-[var(--color-muted)] focus:border-[var(--color-primary)] focus:outline-none focus:ring-2 focus:ring-[var(--color-primary-muted)] sm:max-w-xs"
          aria-label="Search works"
        />

        <div className="flex items-center gap-[var(--space-2)]">
          <label
            htmlFor="sort-select"
            className="text-[var(--text-sm)] text-[var(--color-label)]"
          >
            Sort:
          </label>
          <select
            id="sort-select"
            value={sortField}
            onChange={(e) => setSortField(e.target.value as SortField)}
            className="rounded-[var(--radius-md)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] px-[var(--space-3)] py-[var(--space-2)] text-[var(--text-sm)] text-[var(--color-body)]"
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
            className="rounded-[var(--radius-md)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] px-[var(--space-3)] py-[var(--space-2)] text-[var(--text-sm)] text-[var(--color-body)] hover:bg-[var(--color-surface-secondary)]"
            aria-label={`Sort ${sortDirection === "asc" ? "descending" : "ascending"}`}
          >
            {sortDirection === "asc" ? "↑" : "↓"}
          </button>
        </div>
      </div>

      {/* Works grid */}
      {loading ? (
        <div className="space-y-[var(--space-4)]">
          {Array.from({ length: 4 }).map((_, i) => (
            <div
              key={i}
              className="h-28 animate-pulse rounded-[var(--radius-lg)] bg-[var(--color-surface-secondary)]"
            />
          ))}
        </div>
      ) : filteredWorks.length === 0 ? (
        <div className="rounded-[var(--radius-lg)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-12)] text-center">
          <p className="text-[var(--text-lg)] text-[var(--color-label)]">
            {searchQuery ? "No works match your search." : "No works found."}
          </p>
          {searchQuery && (
            <button
              onClick={() => setSearchQuery("")}
              className="mt-[var(--space-4)] text-[var(--text-sm)] text-[var(--color-primary)] underline underline-offset-2"
            >
              Clear search
            </button>
          )}
        </div>
      ) : (
        <div className="space-y-[var(--space-3)]">
          {filteredWorks.map((work) => (
            <WorkCard key={work.attribution_id} work={work} />
          ))}
        </div>
      )}

      {/* Result count */}
      {!loading && filteredWorks.length > 0 && (
        <p className="mt-[var(--space-6)] text-center text-[var(--text-sm)] text-[var(--color-muted)]">
          {filteredWorks.length} of {works.length} works
        </p>
      )}
    </div>
  );
}
