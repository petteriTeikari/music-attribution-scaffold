"use client";

import Image from "next/image";
import Link from "next/link";
import { motion } from "motion/react";

const FEATURES = [
  {
    title: "Confidence Scoring",
    description:
      "Every attribution comes with a calibrated confidence score from conformal prediction. Know exactly how reliable each credit is.",
    detail:
      "Conformal prediction provides a mathematical guarantee: when the system says \u201c90% confident,\u201d the data is correct 90% of the time \u2014 not a heuristic, but a provable bound. Evidence is stratified across assurance levels (A0 unverified \u2192 A3 artist-verified), mapped to industry standards like ISRC, ISWC, and ISNI. Continuous monitoring detects calibration drift, triggering automatic alerts when confidence distributions shift.",
    marker: "I",
    image: "/images/figures/fig-feature-01-confidence-arc.webp",
    alt: "Concentric arcs representing conformal, Bayesian, and calibrated confidence scoring methods with a large 95% score",
  },
  {
    title: "Provenance Lineage",
    description:
      "See how confidence was built over time \u2014 from initial fetch through entity resolution to expert review. Full audit trail.",
    detail:
      "Attribution-by-design embeds provenance at creation rather than computing it retrospectively. Every event \u2014 metadata fetch, entity resolution match, source corroboration, artist confirmation \u2014 is recorded as an immutable audit entry with timestamps and source identifiers. Confidence grows with each verified touchpoint, giving artists and platforms ironclad proof of authorship that licensing authorities can trust.",
    marker: "II",
    image: "/images/figures/fig-feature-02-provenance-flow.webp",
    alt: "Constructivist data flow diagram showing provenance events connected by lines with a confidence gradient bar",
  },
  {
    title: "MCP Permission Patchbay",
    description:
      "Machine-readable permissions for AI platforms. Define granular rules: who can train on your music, who can clone your voice.",
    detail:
      "When an AI system wants to use your creative data \u2014 voice, lyrics, compositions, or metadata \u2014 it must first query your permission settings via the Model Context Protocol. Set rules per use type: allow streaming but deny training, permit non-commercial generation but require attribution, restrict voice cloning entirely. Every request is logged and archived, making compliance automatic for ethical platforms and violations auditable for legal recourse.",
    marker: "III",
    image: "/images/figures/fig-feature-03-mcp-patchbay.webp",
    alt: "Bauhaus-inspired grid of colored squares representing AI permission states for music usage types",
  },
  {
    title: "Dual-Role Interface",
    description:
      "Artist mode for editing and approving credits. Query mode for browsing and searching. One interface, two perspectives.",
    detail:
      "Artists get a private workspace: claim credits, verify collaborators, upload evidence, and approve or deny AI usage requests with bulk editing and real-time approval queues. Platforms and researchers get a read-only gateway that respects permission boundaries, with access tiers scaled from full internal to rate-limited public. The same identity serves both roles \u2014 switch between creation and consumption with a single toggle.",
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
        <div className="relative w-full px-8 py-20">
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
              <span className="editorial-caps text-xs text-accent mb-4 block">
                Open-Source Research Scaffold
              </span>
            </motion.div>

            <motion.h1
              className="editorial-display text-6xl lg:text-7xl text-heading"
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
              className="mt-6 max-w-lg text-lg leading-relaxed text-body"
              variants={fadeUp}
              transition={{ duration: 0.6, ease: "easeOut" }}
            >
              Know exactly who contributed to a recording — and how certain we
              are about it. Calibrated confidence scoring, provenance lineage,
              and MCP permission infrastructure.
            </motion.p>

            <motion.div
              className="mt-8 flex items-center gap-8"
              variants={fadeUp}
              transition={{ duration: 0.6, ease: "easeOut" }}
            >
              <Link
                href="/works"
                className="text-heading font-medium underline underline-offset-4 decoration-accent decoration-2 hover:text-accent transition-colors duration-150"
              >
                Explore the Demo
              </Link>
              <a
                href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087"
                target="_blank"
                rel="noopener noreferrer"
                className="text-label font-medium underline underline-offset-4 decoration-border hover:decoration-accent hover:text-heading transition-colors duration-150"
              >
                Read the Paper
              </a>
            </motion.div>
          </motion.div>
        </div>
      </section>

      {/* ──── WAVEFORM BAND ──── */}
      <section className="relative py-4">
        <div className="accent-line" />
        <div className="flex items-center gap-4 py-3 px-8 overflow-hidden">
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
      <section className="px-8 py-20">
        <motion.div
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: "-100px" }}
          variants={stagger}
          className="grid gap-12 lg:grid-cols-[1fr_auto] items-start"
        >
          <div>
            <motion.div variants={fadeUp} transition={{ duration: 0.5 }}>
              <span className="editorial-caps text-xs text-accent">
                Process
              </span>
              <h2 className="editorial-display text-4xl lg:text-5xl text-heading mt-3">
                How It Works
              </h2>
            </motion.div>

          <div className="mt-12">
            {/* Steps */}
            <div className="space-y-10">
              {HOW_IT_WORKS.map((item, index) => (
                <motion.div
                  key={item.label}
                  className="relative"
                  variants={fadeUp}
                  transition={{ duration: 0.5 }}
                >
                  <div className="flex items-start gap-6">
                    <div className="accent-square-sm mt-1" aria-hidden="true" />
                    <div style={{ paddingLeft: index % 2 === 1 ? "var(--space-12)" : undefined }}>
                      <h3 className="editorial-caps text-sm text-heading">
                        {item.label}
                      </h3>
                      <p className="mt-2 max-w-lg text-base text-body leading-relaxed">
                        {item.description}
                      </p>
                    </div>
                  </div>
                  {index < HOW_IT_WORKS.length - 1 && (
                    <div
                      className="accent-line mt-10"
                      style={{ opacity: 0.2 }}
                    />
                  )}
                </motion.div>
              ))}
            </div>
          </div>
          </div>

          {/* Process figure — portrait signal chain diagram, top-aligned with section */}
          <motion.div
            className="hidden lg:block max-w-[760px]"
            variants={fadeUp}
            transition={{ duration: 0.5 }}
          >
            <Image
              src="/images/figures/fig-process-graph.webp"
              alt="Portrait-mode constructivist diagram showing four stages of a music attribution pipeline as an audio signal chain, with five colored source dots converging through processing bands and a teal feedback arc"
              width={900}
              height={1200}
              className="w-full h-auto"
            />
          </motion.div>
        </motion.div>
      </section>

      {/* ──── FEATURES ──── */}
      <section className="px-8 py-20">
        <div className="accent-line mb-16" style={{ opacity: 0.4 }} aria-hidden="true" />
        <motion.div
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: "-100px" }}
          variants={stagger}
        >
          <motion.div variants={fadeUp} transition={{ duration: 0.5 }}>
            <span className="editorial-caps text-xs text-accent">
              Capabilities
            </span>
            <h2 className="editorial-display text-4xl lg:text-5xl text-heading mt-3">
              Key Features
            </h2>
          </motion.div>

          <div className="mt-16 space-y-20">
            {FEATURES.map((feature, index) => (
              <motion.div
                key={feature.title}
                className={`grid gap-8 lg:grid-cols-[1fr_1fr] items-start ${
                  index % 2 === 1 ? "lg:direction-rtl" : ""
                }`}
                variants={fadeUp}
                transition={{ duration: 0.5 }}
              >
                <div className={index % 2 === 1 ? "lg:order-2" : ""}>
                  <div className="flex items-center gap-4 mb-4">
                    <div className="accent-square" aria-hidden="true" />
                    <span className="editorial-caps text-xs text-muted">
                      {feature.marker}
                    </span>
                  </div>
                  <h3 className="editorial-display text-3xl text-heading">
                    {feature.title}
                  </h3>
                  <p className="mt-4 text-xl lg:text-2xl text-heading leading-snug max-w-lg">
                    {feature.description}
                  </p>
                  <p className="mt-4 text-sm text-muted leading-relaxed max-w-lg">
                    {feature.detail}
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
      <section className="px-8 py-20">
        <div className="accent-line mb-12" style={{ opacity: 0.4 }} />

        <motion.div
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: "-100px" }}
          variants={stagger}
          className="max-w-2xl"
        >
          <motion.div variants={fadeUp} transition={{ duration: 0.5 }}>
            <span className="editorial-caps text-xs text-accent">
              About
            </span>
            <h2 className="editorial-display text-3xl text-heading mt-3">
              Research Scaffold
            </h2>
          </motion.div>

          <motion.div
            className="mt-6 space-y-4 text-body leading-relaxed"
            variants={fadeUp}
            transition={{ duration: 0.5 }}
          >
            <p>
              Companion code to{" "}
              <a
                href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6109087"
                target="_blank"
                rel="noopener noreferrer"
                className="text-heading underline underline-offset-4 decoration-accent decoration-1 hover:decoration-2 transition-all"
              >
                &ldquo;Governing Generative Music&rdquo;
              </a>{" "}
              by Dr Petteri Teikari (SSRN No. 6109087). Transparent confidence
              scoring, provenance lineage, and MCP permission infrastructure
              working together.
            </p>
            <p>
              The demo uses Imogen Heap&apos;s discography as example data — she
              pioneered music attribution through the{" "}
              <a
                href="https://www.forbes.com/sites/georgehoward/2015/07/28/imogen-heap-gets-specific-about-mycelia-a-fair-trade-music-business-inspired-by-blockchain/"
                target="_blank"
                rel="noopener noreferrer"
                className="text-heading underline underline-offset-4 decoration-accent decoration-1 hover:decoration-2 transition-all"
              >
                Mycelia project
              </a>{" "}
              in 2015, envisioning a fair-trade music ecosystem. That vision continues today with{" "}
              <a
                href="https://auracles.io/"
                target="_blank"
                rel="noopener noreferrer"
                className="text-heading underline underline-offset-4 decoration-accent decoration-1 hover:decoration-2 transition-all"
              >
                Auracles.io
              </a>
              . Eight works showcase confidence ranging from 0% to 95%.
            </p>
            <p className="text-sm text-muted">
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
