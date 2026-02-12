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
    <div className="py-20 text-center">
      {/* Accent line as visual marker */}
      <div className="mx-auto mb-6 w-16">
        <div className="accent-line" />
      </div>

      <h3 className="editorial-display text-xl text-heading">
        {title}
      </h3>
      <p className="mt-2 text-sm text-label">
        {description}
      </p>

      {action && (
        <button
          onClick={action.onClick}
          className="mt-6 text-sm font-medium text-heading underline underline-offset-4 decoration-accent decoration-2 hover:text-accent transition-colors duration-150"
        >
          {action.label}
        </button>
      )}
    </div>
  );
}
