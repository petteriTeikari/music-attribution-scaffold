"use client";

import { useState } from "react";
import type { AttributionRecord } from "@/lib/types/attribution";

type FeedbackStep = "role" | "evidence" | "confidence" | "preview" | "submitted";

interface AgentFeedbackFlowProps {
  work: AttributionRecord;
  onSubmit: (feedback: FeedbackData) => void;
  onCancel: () => void;
}

export interface FeedbackData {
  workId: string;
  reviewerRole: string;
  evidenceType: string;
  overallAssessment: number;
  freeText: string;
  centerBiasFlag: boolean;
}

const REVIEWER_ROLES = [
  { value: "ARTIST", label: "Artist" },
  { value: "MANAGER", label: "Manager" },
  { value: "MUSICOLOGIST", label: "Musicologist" },
  { value: "PRODUCER", label: "Producer" },
  { value: "FAN", label: "Fan" },
];

const EVIDENCE_TYPES = [
  { value: "LINER_NOTES", label: "Liner notes" },
  { value: "MEMORY", label: "Personal memory" },
  { value: "DOCUMENT", label: "Document" },
  { value: "SESSION_NOTES", label: "Session notes" },
  { value: "OTHER", label: "Other" },
];

export function AgentFeedbackFlow({ work, onSubmit, onCancel }: AgentFeedbackFlowProps) {
  const [step, setStep] = useState<FeedbackStep>("role");
  const [reviewerRole, setReviewerRole] = useState("");
  const [evidenceType, setEvidenceType] = useState("");
  const [assessment, setAssessment] = useState(0.5);
  const [freeText, setFreeText] = useState("");

  const centerBias = 0.45 <= assessment && assessment <= 0.55;

  function handleSubmit() {
    onSubmit({
      workId: work.attribution_id,
      reviewerRole,
      evidenceType,
      overallAssessment: assessment,
      freeText,
      centerBiasFlag: centerBias,
    });
    setStep("submitted");
  }

  if (step === "submitted") {
    return (
      <div className="py-[var(--space-10)] text-center">
        <div className="accent-square mx-auto mb-[var(--space-4)]" aria-hidden="true" />
        <p className="editorial-display text-xl text-[var(--color-confidence-high)]">
          Thank you
        </p>
        <p className="mt-[var(--space-2)] text-sm text-[var(--color-label)]">
          Your feedback helps improve attribution confidence.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-[var(--space-5)]">
      {/* Step indicator */}
      <div className="flex items-center gap-[var(--space-3)]">
        <div className="accent-square-sm" aria-hidden="true" />
        <span className="editorial-caps text-xs text-[var(--color-accent)]">
          Feedback for {work.work_title}
        </span>
      </div>

      {/* Agent narration */}
      <p className="text-sm text-[var(--color-body)] border-l-2 border-[var(--color-accent-muted)] pl-[var(--space-3)]">
        {step === "role" && "First, how are you involved with this work?"}
        {step === "evidence" && "What type of evidence supports your assessment?"}
        {step === "confidence" && "How confident are you in the current attribution?"}
        {step === "preview" && "Review your feedback before submitting."}
      </p>

      {/* Step: Role */}
      {step === "role" && (
        <div className="space-y-[var(--space-2)]">
          {REVIEWER_ROLES.map((r) => (
            <button
              key={r.value}
              onClick={() => {
                setReviewerRole(r.value);
                setStep("evidence");
              }}
              className={`block w-full text-left px-[var(--space-4)] py-[var(--space-3)] text-sm border transition-colors ${
                reviewerRole === r.value
                  ? "border-[var(--color-accent)] text-[var(--color-heading)]"
                  : "border-[var(--color-border)] text-[var(--color-body)] hover:border-[var(--color-accent)]"
              }`}
            >
              {r.label}
            </button>
          ))}
        </div>
      )}

      {/* Step: Evidence */}
      {step === "evidence" && (
        <div className="space-y-[var(--space-2)]">
          {EVIDENCE_TYPES.map((e) => (
            <button
              key={e.value}
              onClick={() => {
                setEvidenceType(e.value);
                setStep("confidence");
              }}
              className={`block w-full text-left px-[var(--space-4)] py-[var(--space-3)] text-sm border transition-colors ${
                evidenceType === e.value
                  ? "border-[var(--color-accent)] text-[var(--color-heading)]"
                  : "border-[var(--color-border)] text-[var(--color-body)] hover:border-[var(--color-accent)]"
              }`}
            >
              {e.label}
            </button>
          ))}
        </div>
      )}

      {/* Step: Confidence */}
      {step === "confidence" && (
        <div className="space-y-[var(--space-4)]">
          <div>
            <label className="text-sm text-[var(--color-label)]" htmlFor="assessment-slider">
              Overall assessment
            </label>
            <input
              id="assessment-slider"
              type="range"
              min="0"
              max="100"
              value={Math.round(assessment * 100)}
              onChange={(e) => setAssessment(Number(e.target.value) / 100)}
              className="w-full mt-[var(--space-2)]"
            />
            <div className="flex justify-between text-xs text-[var(--color-muted)] data-mono">
              <span>0%</span>
              <span className="font-semibold text-[var(--color-heading)]">
                {Math.round(assessment * 100)}%
              </span>
              <span>100%</span>
            </div>
          </div>

          {centerBias && (
            <div className="px-[var(--space-4)] py-[var(--space-3)] bg-[var(--color-confidence-medium-bg)] border border-[var(--color-confidence-medium)] text-sm">
              <span className="font-semibold" style={{ color: "var(--color-confidence-medium)" }}>
                Center bias detected
              </span>
              <span className="text-[var(--color-body)]">
                {" "}
                &mdash; ratings near 50% may indicate uncertainty. Consider whether you can be more decisive.
              </span>
            </div>
          )}

          <div>
            <label className="text-sm text-[var(--color-label)]" htmlFor="free-text">
              Notes (optional)
            </label>
            <textarea
              id="free-text"
              value={freeText}
              onChange={(e) => setFreeText(e.target.value)}
              className="w-full mt-[var(--space-2)] px-[var(--space-3)] py-[var(--space-2)] text-sm bg-[var(--color-surface-secondary)] border border-[var(--color-border)] text-[var(--color-heading)] placeholder:text-[var(--color-muted)]"
              placeholder="Any additional context about this attribution..."
              rows={3}
            />
          </div>

          <button
            onClick={() => setStep("preview")}
            className="editorial-caps text-xs text-[var(--color-heading)] underline underline-offset-4 decoration-[var(--color-accent)] decoration-2"
          >
            Preview
          </button>
        </div>
      )}

      {/* Step: Preview */}
      {step === "preview" && (
        <div className="space-y-[var(--space-3)]">
          <div className="text-sm space-y-[var(--space-1)]">
            <div className="flex justify-between">
              <span className="text-[var(--color-muted)]">Role</span>
              <span className="text-[var(--color-heading)]">{reviewerRole}</span>
            </div>
            <div className="flex justify-between">
              <span className="text-[var(--color-muted)]">Evidence</span>
              <span className="text-[var(--color-heading)]">{evidenceType}</span>
            </div>
            <div className="flex justify-between">
              <span className="text-[var(--color-muted)]">Assessment</span>
              <span className="text-[var(--color-heading)] data-mono">
                {Math.round(assessment * 100)}%
              </span>
            </div>
            {freeText && (
              <div className="pt-[var(--space-2)] border-t border-[var(--color-border)]">
                <span className="text-[var(--color-muted)]">Notes: </span>
                <span className="text-[var(--color-body)]">{freeText}</span>
              </div>
            )}
          </div>

          <div className="flex gap-[var(--space-4)]">
            <button
              onClick={handleSubmit}
              className="editorial-caps text-xs text-[var(--color-heading)] underline underline-offset-4 decoration-[var(--color-confidence-high)] decoration-2 hover:text-[var(--color-confidence-high)]"
            >
              Submit
            </button>
            <button
              onClick={onCancel}
              className="editorial-caps text-xs text-[var(--color-muted)] underline underline-offset-4 hover:text-[var(--color-heading)]"
            >
              Cancel
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
