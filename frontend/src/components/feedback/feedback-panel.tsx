"use client";

import { useState } from "react";
import type { FeedbackCard } from "@/lib/types/feedback";

interface FeedbackPanelProps {
  attributionId: string;
  attributionVersion: number;
  isOpen: boolean;
  onClose: () => void;
  onSubmit?: (card: Partial<FeedbackCard>) => void;
}

export function FeedbackPanel({
  attributionId,
  attributionVersion,
  isOpen,
  onClose,
  onSubmit,
}: FeedbackPanelProps) {
  const [assessment, setAssessment] = useState(0.5);
  const [freeText, setFreeText] = useState("");
  const [evidenceType, setEvidenceType] = useState("OTHER");

  const isCenterBiased = assessment >= 0.45 && assessment <= 0.55;

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    onSubmit?.({
      attribution_id: attributionId,
      attribution_version: attributionVersion,
      overall_assessment: assessment,
      free_text: freeText || null,
      evidence_type: evidenceType as FeedbackCard["evidence_type"],
      center_bias_flag: isCenterBiased,
    });
    onClose();
  }

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex justify-end" role="dialog" aria-label="Submit feedback">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-black/30"
        onClick={onClose}
        aria-hidden="true"
      />

      {/* Panel */}
      <div className="relative w-full max-w-md bg-surface-elevated border-l border-border shadow-xl overflow-y-auto">
        <div className="p-6">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-lg font-semibold text-heading">
              Submit Feedback
            </h2>
            <button
              onClick={onClose}
              className="text-muted hover:text-body text-xl"
              aria-label="Close"
            >
              ×
            </button>
          </div>

          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Overall assessment slider */}
            <div>
              <label
                htmlFor="assessment"
                className="block text-sm font-medium text-heading mb-2"
              >
                Overall Assessment: {Math.round(assessment * 100)}%
              </label>
              <input
                id="assessment"
                type="range"
                min="0"
                max="100"
                value={Math.round(assessment * 100)}
                onChange={(e) =>
                  setAssessment(parseInt(e.target.value, 10) / 100)
                }
                className="w-full accent-[var(--color-primary)]"
              />
              {isCenterBiased && (
                <p className="mt-1 text-xs text-confidence-medium">
                  Center bias detected — values near 50% may indicate
                  uncertainty. Consider moving the slider if you have a stronger
                  opinion.
                </p>
              )}
            </div>

            {/* Evidence type */}
            <div>
              <label
                htmlFor="evidence-type"
                className="block text-sm font-medium text-heading mb-2"
              >
                Evidence Type
              </label>
              <select
                id="evidence-type"
                value={evidenceType}
                onChange={(e) => setEvidenceType(e.target.value)}
                className="w-full rounded-md border border-border bg-surface px-3 py-2 text-sm text-body"
              >
                <option value="LINER_NOTES">Liner Notes</option>
                <option value="MEMORY">Personal Memory</option>
                <option value="DOCUMENT">Document</option>
                <option value="SESSION_NOTES">Session Notes</option>
                <option value="OTHER">Other</option>
              </select>
            </div>

            {/* Free text */}
            <div>
              <label
                htmlFor="feedback-text"
                className="block text-sm font-medium text-heading mb-2"
              >
                Comments
              </label>
              <textarea
                id="feedback-text"
                value={freeText}
                onChange={(e) => setFreeText(e.target.value)}
                rows={4}
                placeholder="Any additional context about this attribution..."
                className="w-full rounded-md border border-border bg-surface px-3 py-2 text-sm text-body placeholder:text-muted"
              />
            </div>

            <button
              type="submit"
              className="w-full rounded-md bg-primary py-3 text-sm font-medium text-white transition-colors duration-150 hover:bg-primary-hover"
            >
              Submit Feedback
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
