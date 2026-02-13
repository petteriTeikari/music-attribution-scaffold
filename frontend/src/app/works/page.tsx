"use client";

import { useEffect, useState } from "react";
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
import { apiClient } from "@/lib/api/api-client";
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
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (works.length > 0) return;
    setLoading(true);
    setError(null);
    apiClient.getWorks().then((data) => {
      setWorks(data);
      setLoading(false);
    }).catch(() => {
      setError("Failed to load works. Please try again.");
      setLoading(false);
    });
  }, [works.length, setWorks, setLoading]);

  return (
    <div className="px-8 py-10">
      {/* Header */}
      <div className="mb-8">
        <span className="editorial-caps text-xs text-accent block mb-2">
          Catalog
        </span>
        <h1 className="editorial-display text-4xl text-heading">
          Work Catalog
        </h1>
        <p className="mt-2 text-base text-label">
          Attribution records with confidence scoring and provenance lineage.
        </p>
      </div>

      {/* Search + Sort controls */}
      <div className="mb-6 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <input
          type="search"
          placeholder="Search works or artists..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="border-b border-border bg-transparent px-0 py-2 text-sm text-body placeholder:text-muted focus:border-accent focus:outline-none sm:max-w-xs"
          aria-label="Search works"
        />

        <div className="flex items-center gap-2">
          <label
            htmlFor="sort-select"
            className="editorial-caps text-xs text-label"
          >
            Sort:
          </label>
          <select
            id="sort-select"
            value={sortField}
            onChange={(e) => setSortField(e.target.value as SortField)}
            className="border-b border-border bg-transparent px-2 py-2 text-sm text-body focus:border-accent focus:outline-none"
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
            className="border-b border-border px-2 py-2 text-sm text-body hover:border-accent transition-colors"
            aria-label={`Sort ${sortDirection === "asc" ? "descending" : "ascending"}`}
          >
            {sortDirection === "asc" ? "↑" : "↓"}
          </button>
        </div>
      </div>

      <div className="accent-line mb-6" style={{ opacity: 0.3 }} />

      {/* Works list */}
      {error ? (
        <div className="py-20 text-center">
          <p className="editorial-display text-2xl text-heading">{error}</p>
          <button
            onClick={() => {
              setError(null);
              setLoading(true);
              apiClient.getWorks().then((data) => {
                setWorks(data);
                setLoading(false);
              }).catch(() => {
                setError("Failed to load works. Please try again.");
                setLoading(false);
              });
            }}
            className="mt-4 text-sm text-accent underline underline-offset-2"
          >
            Retry
          </button>
        </div>
      ) : loading ? (
        <div className="space-y-4">
          {Array.from({ length: 4 }).map((_, i) => (
            <div
              key={i}
              className="h-20 animate-pulse bg-surface-secondary"
            />
          ))}
        </div>
      ) : filteredWorks.length === 0 ? (
        <div className="py-20 text-center">
          <p className="editorial-display text-2xl text-muted">
            {searchQuery ? "No works match your search." : "No works found."}
          </p>
          {searchQuery && (
            <button
              onClick={() => setSearchQuery("")}
              className="mt-4 text-sm text-accent underline underline-offset-2"
            >
              Clear search
            </button>
          )}
        </div>
      ) : (
        <div className="divide-y divide-border">
          {filteredWorks.map((work) => (
            <WorkCard key={work.attribution_id} work={work} />
          ))}
        </div>
      )}

      {/* Result count */}
      {!loading && filteredWorks.length > 0 && (
        <p className="mt-8 text-xs text-muted editorial-caps">
          {filteredWorks.length} of {works.length} works
        </p>
      )}
    </div>
  );
}
