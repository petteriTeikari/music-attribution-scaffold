import type { CitationRef } from "@/lib/data/citations";

interface CitationRefListProps {
  citations: CitationRef[];
}

export function CitationRefList({ citations }: CitationRefListProps) {
  return (
    <div>
      <span className="editorial-caps text-xs text-accent">
        Bibliography
      </span>
      <h2 className="editorial-display text-3xl text-heading mt-3 mb-8">
        References
      </h2>

      <div className="space-y-3">
        {citations.map((ref) => (
          <div key={ref.id} className="flex gap-3 text-sm">
            <span className="data-mono text-accent font-medium flex-shrink-0">
              [{ref.id}]
            </span>
            <p className="text-body leading-relaxed">
              {ref.url ? (
                <a
                  href={ref.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-primary underline underline-offset-2 decoration-accent decoration-1 hover:decoration-2 transition-all"
                >
                  {ref.authors}
                </a>
              ) : (
                <span>{ref.authors}</span>
              )}{" "}
              ({ref.year}).{" "}
              <span className="text-heading">
                &ldquo;{ref.title}.&rdquo;
              </span>{" "}
              <span className="text-label italic">{ref.venue}.</span>
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
