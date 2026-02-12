// TODO: Component not yet integrated — wire up during UI fine-tuning

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
    <div className="py-[var(--space-20)] text-center">
      {/* Accent line as visual marker */}
      <div className="mx-auto mb-[var(--space-6)] w-16">
        <div className="accent-line" />
      </div>

      <h3 className="editorial-display text-xl text-[var(--color-heading)]">
        {title}
      </h3>
      <p className="mt-[var(--space-2)] text-sm text-[var(--color-label)]">
        {description}
      </p>

      {action && (
        <button
          onClick={action.onClick}
          className="mt-[var(--space-6)] text-sm font-medium text-[var(--color-heading)] underline underline-offset-4 decoration-[var(--color-accent)] decoration-2 hover:text-[var(--color-accent)] transition-colors duration-[var(--transition-fast)]"
        >
          {action.label}
        </button>
      )}
    </div>
  );
}
