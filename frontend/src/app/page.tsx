import Link from "next/link";

const FEATURES = [
  {
    title: "Confidence Scoring",
    description:
      "Every attribution comes with a calibrated confidence score from conformal prediction. Know exactly how reliable each credit is.",
    accent: "var(--color-confidence-high)",
  },
  {
    title: "Provenance Lineage",
    description:
      "See how confidence was built over time — from initial fetch through entity resolution to expert review. Full audit trail.",
    accent: "var(--color-primary)",
  },
  {
    title: "MCP Permission Patchbay",
    description:
      "Machine-readable permissions for AI platforms. Define granular rules: who can train on your music, who can clone your voice.",
    accent: "var(--color-accent)",
  },
  {
    title: "Dual-Role Interface",
    description:
      "Artist mode for editing and approving credits. Query mode for browsing and searching. One interface, two perspectives.",
    accent: "var(--color-teal)",
  },
];

const HOW_IT_WORKS = [
  {
    step: "1",
    title: "Fetch & Normalize",
    description:
      "ETL pipelines pull from MusicBrainz, Discogs, AcoustID, and file metadata into normalized records.",
  },
  {
    step: "2",
    title: "Resolve Entities",
    description:
      "Entity resolution links records across sources using identifiers, string similarity, embeddings, and graph analysis.",
  },
  {
    step: "3",
    title: "Score & Calibrate",
    description:
      "Attribution engine aggregates evidence, produces conformal prediction sets, and assigns calibrated confidence.",
  },
  {
    step: "4",
    title: "Review & Improve",
    description:
      "Domain experts provide feedback via structured FeedbackCards. Confidence updates automatically through Bayesian calibration.",
  },
];

export default function HomePage() {
  return (
    <div>
      {/* Hero */}
      <section className="px-[var(--space-6)] py-[var(--space-20)]">
        <div className="mx-auto max-w-4xl">
          <h1 className="text-[var(--text-4xl)] font-bold leading-[var(--leading-tight)] text-[var(--color-heading)] md:text-5xl">
            Music Attribution with
            <br />
            <span style={{ color: "var(--color-accent)" }}>
              Transparent Confidence
            </span>
          </h1>
          <p className="mt-[var(--space-6)] max-w-2xl text-[var(--text-lg)] leading-[var(--leading-relaxed)] text-[var(--color-body)]">
            Open-source research scaffold for calibrated music credit
            attribution. Know exactly who contributed to a recording — and how
            certain we are about it.
          </p>
          <div className="mt-[var(--space-8)] flex flex-wrap items-center gap-[var(--space-4)]">
            <Link
              href="/works"
              className="rounded-[var(--radius-md)] bg-[var(--color-primary)] px-[var(--space-6)] py-[var(--space-3)] text-[var(--text-base)] font-medium text-white transition-colors duration-[var(--transition-fast)] hover:bg-[var(--color-primary-hover)]"
            >
              Explore Demo
            </Link>
            <a
              href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087"
              target="_blank"
              rel="noopener noreferrer"
              className="rounded-[var(--radius-md)] border border-[var(--color-border)] px-[var(--space-6)] py-[var(--space-3)] text-[var(--text-base)] font-medium text-[var(--color-primary)] transition-colors duration-[var(--transition-fast)] hover:bg-[var(--color-surface-secondary)]"
            >
              Read the Paper
            </a>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="border-t border-[var(--color-border)] bg-[var(--color-surface-secondary)] px-[var(--space-6)] py-[var(--space-16)]">
        <div className="mx-auto max-w-4xl">
          <h2 className="text-[var(--text-2xl)] font-bold text-[var(--color-heading)]">
            How It Works
          </h2>
          <div className="mt-[var(--space-8)] grid gap-[var(--space-6)] md:grid-cols-2">
            {HOW_IT_WORKS.map((item) => (
              <div key={item.step} className="flex gap-[var(--space-4)]">
                <span
                  className="flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-full text-[var(--text-sm)] font-bold text-white"
                  style={{ backgroundColor: "var(--color-primary)" }}
                >
                  {item.step}
                </span>
                <div>
                  <h3 className="font-semibold text-[var(--color-heading)]">
                    {item.title}
                  </h3>
                  <p className="mt-[var(--space-2)] text-[var(--text-sm)] text-[var(--color-body)]">
                    {item.description}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="px-[var(--space-6)] py-[var(--space-16)]">
        <div className="mx-auto max-w-4xl">
          <h2 className="text-[var(--text-2xl)] font-bold text-[var(--color-heading)]">
            Key Features
          </h2>
          <div className="mt-[var(--space-8)] grid gap-[var(--space-6)] md:grid-cols-2">
            {FEATURES.map((feature) => (
              <div
                key={feature.title}
                className="rounded-[var(--radius-lg)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-6)] shadow-[var(--shadow-sm)]"
              >
                <div
                  className="mb-[var(--space-3)] h-1 w-12 rounded-[var(--radius-full)]"
                  style={{ backgroundColor: feature.accent }}
                />
                <h3 className="text-[var(--text-lg)] font-semibold text-[var(--color-heading)]">
                  {feature.title}
                </h3>
                <p className="mt-[var(--space-2)] text-[var(--text-sm)] text-[var(--color-body)]">
                  {feature.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* About */}
      <section className="border-t border-[var(--color-border)] px-[var(--space-6)] py-[var(--space-16)]">
        <div className="mx-auto max-w-4xl">
          <h2 className="text-[var(--text-2xl)] font-bold text-[var(--color-heading)]">
            About This Project
          </h2>
          <div className="mt-[var(--space-6)] space-y-[var(--space-4)] text-[var(--color-body)]">
            <p>
              This is a research scaffold — companion code to{" "}
              <a
                href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087"
                target="_blank"
                rel="noopener noreferrer"
                className="text-[var(--color-primary)] underline underline-offset-2 hover:text-[var(--color-primary-hover)]"
              >
                &ldquo;Governing Generative Music&rdquo; (SSRN No. 6109087)
              </a>
              . It demonstrates how transparent confidence scoring,
              provenance lineage, and MCP permission infrastructure can work
              together.
            </p>
            <p>
              The demo uses Imogen Heap&apos;s discography as example data — she
              pioneered music attribution through the{" "}
              <span className="font-medium">Mycelia</span> project. The 8 works
              showcase confidence ranging from 0% (unreleased, no data) to 95%
              (fully verified with rich provenance).
            </p>
            <p className="text-[var(--text-sm)] text-[var(--color-muted)]">
              A0–A3 assurance levels map to ISRC/ISWC/ISNI standards.
              Conformal prediction provides calibrated uncertainty.
              Attribution-by-design embeds provenance at creation.
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
