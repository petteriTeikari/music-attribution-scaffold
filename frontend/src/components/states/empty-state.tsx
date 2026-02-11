interface EmptyStateProps {
  title: string;
  description: string;
  action?: {
    label: string;
    onClick: () => void;
  };
}

export function EmptyState({ title, description, action }: EmptyStateProps) {
  return (
    <div className="rounded-[var(--radius-lg)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-12)] text-center">
      {/* Simple illustration: a subtle circle with a question mark */}
      <div className="mx-auto mb-[var(--space-6)] flex h-16 w-16 items-center justify-center rounded-full bg-[var(--color-surface-secondary)]">
        <span className="text-[var(--text-2xl)] text-[var(--color-muted)]">
          ?
        </span>
      </div>

      <h3 className="text-[var(--text-lg)] font-semibold text-[var(--color-heading)]">
        {title}
      </h3>
      <p className="mt-[var(--space-2)] text-[var(--text-sm)] text-[var(--color-label)]">
        {description}
      </p>

      {action && (
        <button
          onClick={action.onClick}
          className="mt-[var(--space-6)] rounded-[var(--radius-md)] bg-[var(--color-primary)] px-[var(--space-6)] py-[var(--space-3)] text-[var(--text-sm)] font-medium text-white transition-colors duration-[var(--transition-fast)] hover:bg-[var(--color-primary-hover)]"
        >
          {action.label}
        </button>
      )}
    </div>
  );
}
