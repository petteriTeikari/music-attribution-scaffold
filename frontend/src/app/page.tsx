"use client";

import Image from "next/image";
import Link from "next/link";
import { motion } from "motion/react";

const FEATURES = [
  {
    title: "Confidence Scoring",
    description:
      "Every attribution comes with a calibrated confidence score from conformal prediction. Know exactly how reliable each credit is.",
    marker: "I",
    image: "/images/figures/fig-feature-01-confidence-arc.webp",
    alt: "Concentric arcs representing conformal, Bayesian, and calibrated confidence scoring methods with a large 95% score",
  },
  {
    title: "Provenance Lineage",
    description:
      "See how confidence was built over time — from initial fetch through entity resolution to expert review. Full audit trail.",
    marker: "II",
    image: "/images/figures/fig-feature-02-provenance-flow.webp",
    alt: "Constructivist data flow diagram showing provenance events connected by lines with a confidence gradient bar",
  },
  {
    title: "MCP Permission Patchbay",
    description:
      "Machine-readable permissions for AI platforms. Define granular rules: who can train on your music, who can clone your voice.",
    marker: "III",
    image: "/images/figures/fig-feature-03-mcp-patchbay.webp",
    alt: "Bauhaus-inspired grid of colored squares representing AI permission states for music usage types",
  },
  {
    title: "Dual-Role Interface",
    description:
      "Artist mode for editing and approving credits. Query mode for browsing and searching. One interface, two perspectives.",
    marker: "IV",
    image: "/images/figures/fig-feature-04-dual-role.webp",
    alt: "Split composition with warm gold artist panel and cool blue query panel divided by a coral accent line",
  },
];

const HOW_IT_WORKS = [
  {
    label: "FETCH & NORMALIZE",
    description:
      "ETL pipelines pull from MusicBrainz, Discogs, AcoustID, and file metadata into normalized records.",
  },
  {
    label: "RESOLVE ENTITIES",
    description:
      "Entity resolution links records across sources using identifiers, string similarity, embeddings, and graph analysis.",
  },
  {
    label: "SCORE & CALIBRATE",
    description:
      "Attribution engine aggregates evidence, produces conformal prediction sets, and assigns calibrated confidence.",
  },
  {
    label: "REVIEW & IMPROVE",
    description:
      "Domain experts provide feedback via structured FeedbackCards. Confidence updates automatically through Bayesian calibration.",
  },
];

const fadeUp = {
  hidden: { opacity: 0, y: 24 },
  visible: { opacity: 1, y: 0 },
};

const stagger = {
  visible: {
    transition: { staggerChildren: 0.12 },
  },
};

export default function HomePage() {
  return (
    <div>
      {/* ──── HERO ──── */}
      <section className="relative min-h-[85vh] flex items-center overflow-hidden">
        {/* Background hero image — full-width behind text */}
        <motion.div
          className="absolute inset-0"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1.2, delay: 0.2 }}
          aria-hidden="true"
        >
          <Image
            src="/images/figures/fig-hero-01-waveform-tapestry.webp"
            alt=""
            fill
            priority
            className="object-cover object-right"
            sizes="100vw"
          />
          {/* Gradient overlay: solid cream on left fading to transparent on right */}
          <div
            className="absolute inset-0"
            style={{
              background: "linear-gradient(to right, var(--color-surface) 20%, var(--color-surface) 35%, transparent 70%)",
            }}
          />
          {/* Bottom fade to surface for clean transition */}
          <div
            className="absolute inset-x-0 bottom-0 h-24"
            style={{
              background: "linear-gradient(to top, var(--color-surface), transparent)",
            }}
          />
        </motion.div>

        {/* Accent line running through the section */}
        <div
          className="accent-line absolute top-1/2 left-0 right-0"
          style={{ opacity: 0.3 }}
          aria-hidden="true"
        />

        {/* Text content — positioned above the background image */}
        <div className="relative w-full px-[var(--space-8)] py-[var(--space-20)]">
          <motion.div
            initial="hidden"
            animate="visible"
            variants={stagger}
            className="max-w-xl"
          >
            <motion.div
              variants={fadeUp}
              transition={{ duration: 0.6, ease: "easeOut" }}
            >
              <span className="editorial-caps text-[var(--text-xs)] text-[var(--color-accent)] mb-[var(--space-4)] block">
                Open-Source Research Scaffold
              </span>
            </motion.div>

            <motion.h1
              className="editorial-display text-[var(--text-6xl)] lg:text-[var(--text-7xl)] text-[var(--color-heading)]"
              variants={fadeUp}
              transition={{ duration: 0.6, ease: "easeOut" }}
            >
              Music Attribution
              <br />
              with{" "}
              <em className="editorial-display-italic" style={{ color: "var(--color-accent)" }}>
                Transparent
              </em>
              <br />
              Confidence
            </motion.h1>

            <motion.p
              className="mt-[var(--space-6)] max-w-lg text-[var(--text-lg)] leading-[var(--leading-relaxed)] text-[var(--color-body)]"
              variants={fadeUp}
              transition={{ duration: 0.6, ease: "easeOut" }}
            >
              Know exactly who contributed to a recording — and how certain we
              are about it. Calibrated confidence scoring, provenance lineage,
              and MCP permission infrastructure.
            </motion.p>

            <motion.div
              className="mt-[var(--space-8)] flex items-center gap-[var(--space-8)]"
              variants={fadeUp}
              transition={{ duration: 0.6, ease: "easeOut" }}
            >
              <Link
                href="/works"
                className="text-[var(--color-heading)] font-medium underline underline-offset-4 decoration-[var(--color-accent)] decoration-2 hover:text-[var(--color-accent)] transition-colors duration-[var(--transition-fast)]"
              >
                Explore the Demo
              </Link>
              <a
                href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087"
                target="_blank"
                rel="noopener noreferrer"
                className="text-[var(--color-label)] font-medium underline underline-offset-4 decoration-[var(--color-border)] hover:decoration-[var(--color-accent)] hover:text-[var(--color-heading)] transition-colors duration-[var(--transition-fast)]"
              >
                Read the Paper
              </a>
            </motion.div>
          </motion.div>
        </div>
      </section>

      {/* ──── WAVEFORM BAND ──── */}
      <section className="relative py-[var(--space-4)]">
        <div className="accent-line" />
        <div className="flex items-center gap-[var(--space-4)] py-[var(--space-3)] px-[var(--space-8)] overflow-hidden">
          {Array.from({ length: 64 }).map((_, i) => (
            <div
              key={i}
              className="flex-shrink-0"
              style={{
                width: 2,
                height: `${8 + Math.abs(Math.sin(i * 0.3)) * 24}px`,
                backgroundColor:
                  i % 8 === 0
                    ? "var(--color-accent)"
                    : "var(--color-border-strong)",
                opacity: 0.4 + Math.abs(Math.sin(i * 0.2)) * 0.6,
              }}
              aria-hidden="true"
            />
          ))}
        </div>
        <div className="accent-line" />
      </section>

      {/* ──── HOW IT WORKS ──── */}
      <section className="px-[var(--space-8)] py-[var(--space-20)]">
        <motion.div
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: "-100px" }}
          variants={stagger}
        >
          <motion.div variants={fadeUp} transition={{ duration: 0.5 }}>
            <span className="editorial-caps text-[var(--text-xs)] text-[var(--color-accent)]">
              Process
            </span>
            <h2 className="editorial-display text-[var(--text-4xl)] lg:text-[var(--text-5xl)] text-[var(--color-heading)] mt-[var(--space-3)]">
              How It Works
            </h2>
          </motion.div>

          <div className="mt-[var(--space-12)] space-y-[var(--space-10)]">
            {HOW_IT_WORKS.map((item, index) => (
              <motion.div
                key={item.label}
                className="relative"
                variants={fadeUp}
                transition={{ duration: 0.5 }}
              >
                <div className="flex items-start gap-[var(--space-6)]">
                  <div className="accent-square-sm mt-[var(--space-1)]" aria-hidden="true" />
                  <div style={{ paddingLeft: index % 2 === 1 ? "var(--space-12)" : undefined }}>
                    <h3 className="editorial-caps text-[var(--text-sm)] text-[var(--color-heading)]">
                      {item.label}
                    </h3>
                    <p className="mt-[var(--space-2)] max-w-lg text-[var(--text-base)] text-[var(--color-body)] leading-[var(--leading-relaxed)]">
                      {item.description}
                    </p>
                  </div>
                </div>
                {index < HOW_IT_WORKS.length - 1 && (
                  <div
                    className="accent-line mt-[var(--space-10)]"
                    style={{ opacity: 0.2 }}
                  />
                )}
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* ──── FEATURES ──── */}
      <section className="px-[var(--space-8)] py-[var(--space-20)] bg-[var(--color-surface-secondary)]">
        <motion.div
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: "-100px" }}
          variants={stagger}
        >
          <motion.div variants={fadeUp} transition={{ duration: 0.5 }}>
            <span className="editorial-caps text-[var(--text-xs)] text-[var(--color-accent)]">
              Capabilities
            </span>
            <h2 className="editorial-display text-[var(--text-4xl)] lg:text-[var(--text-5xl)] text-[var(--color-heading)] mt-[var(--space-3)]">
              Key Features
            </h2>
          </motion.div>

          <div className="mt-[var(--space-16)] space-y-[var(--space-20)]">
            {FEATURES.map((feature, index) => (
              <motion.div
                key={feature.title}
                className={`grid gap-[var(--space-8)] lg:grid-cols-[1fr_1fr] items-start ${
                  index % 2 === 1 ? "lg:direction-rtl" : ""
                }`}
                variants={fadeUp}
                transition={{ duration: 0.5 }}
              >
                <div className={index % 2 === 1 ? "lg:order-2" : ""}>
                  <div className="flex items-center gap-[var(--space-4)] mb-[var(--space-4)]">
                    <div className="accent-square" aria-hidden="true" />
                    <span className="editorial-caps text-[var(--text-xs)] text-[var(--color-muted)]">
                      {feature.marker}
                    </span>
                  </div>
                  <h3 className="editorial-display text-[var(--text-3xl)] text-[var(--color-heading)]">
                    {feature.title}
                  </h3>
                  <p className="mt-[var(--space-4)] text-[var(--text-base)] text-[var(--color-body)] leading-[var(--leading-relaxed)] max-w-md">
                    {feature.description}
                  </p>
                </div>

                {/* Feature figure */}
                <div
                  className={`overflow-hidden ${
                    index % 2 === 1 ? "lg:order-1" : ""
                  }`}
                >
                  <Image
                    src={feature.image}
                    alt={feature.alt}
                    width={1600}
                    height={1195}
                    className="w-full h-auto"
                  />
                </div>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* ──── ABOUT / PAPER ──── */}
      <section className="px-[var(--space-8)] py-[var(--space-20)]">
        <div className="accent-line mb-[var(--space-12)]" style={{ opacity: 0.4 }} />

        <motion.div
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: "-100px" }}
          variants={stagger}
          className="max-w-2xl"
        >
          <motion.div variants={fadeUp} transition={{ duration: 0.5 }}>
            <span className="editorial-caps text-[var(--text-xs)] text-[var(--color-accent)]">
              About
            </span>
            <h2 className="editorial-display text-[var(--text-3xl)] text-[var(--color-heading)] mt-[var(--space-3)]">
              Research Scaffold
            </h2>
          </motion.div>

          <motion.div
            className="mt-[var(--space-6)] space-y-[var(--space-4)] text-[var(--color-body)] leading-[var(--leading-relaxed)]"
            variants={fadeUp}
            transition={{ duration: 0.5 }}
          >
            <p>
              Companion code to{" "}
              <a
                href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087"
                target="_blank"
                rel="noopener noreferrer"
                className="text-[var(--color-heading)] underline underline-offset-4 decoration-[var(--color-accent)] decoration-1 hover:decoration-2 transition-all"
              >
                &ldquo;Governing Generative Music&rdquo;
              </a>{" "}
              (SSRN No. 6109087). Transparent confidence scoring, provenance
              lineage, and MCP permission infrastructure working together.
            </p>
            <p>
              The demo uses Imogen Heap&apos;s discography as example data — she
              pioneered music attribution through the Mycelia project. Eight
              works showcase confidence ranging from 0% to 95%.
            </p>
            <p className="text-[var(--text-sm)] text-[var(--color-muted)]">
              A0–A3 assurance levels map to ISRC/ISWC/ISNI standards.
              Conformal prediction provides calibrated uncertainty.
              Attribution-by-design embeds provenance at creation.
            </p>
          </motion.div>
        </motion.div>
      </section>
    </div>
  );
}
