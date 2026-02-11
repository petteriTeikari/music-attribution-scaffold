interface SkeletonProps {
  className?: string;
}

export function Skeleton({ className = "" }: SkeletonProps) {
  return (
    <div
      className={`animate-pulse rounded-[var(--radius-md)] bg-[var(--color-surface-secondary)] ${className}`}
      aria-hidden="true"
    />
  );
}

export function WorkCardSkeleton() {
  return (
    <div className="rounded-[var(--radius-lg)] border border-[var(--color-border)] bg-[var(--color-surface-elevated)] p-[var(--space-6)]">
      <div className="flex items-start gap-[var(--space-5)]">
        <Skeleton className="h-12 w-12 rounded-full" />
        <div className="flex-1 space-y-[var(--space-3)]">
          <Skeleton className="h-5 w-48" />
          <Skeleton className="h-4 w-32" />
          <div className="flex gap-[var(--space-2)]">
            <Skeleton className="h-5 w-20" />
            <Skeleton className="h-5 w-16" />
          </div>
        </div>
      </div>
    </div>
  );
}

export function DetailPageSkeleton() {
  return (
    <div className="mx-auto max-w-4xl px-[var(--space-6)] py-[var(--space-10)]">
      <div className="space-y-[var(--space-6)]">
        <Skeleton className="h-8 w-48" />
        <div className="rounded-[var(--radius-xl)] border border-[var(--color-border)] p-[var(--space-8)]">
          <div className="flex items-start gap-[var(--space-8)]">
            <Skeleton className="h-36 w-36 rounded-full" />
            <div className="flex-1 space-y-[var(--space-4)]">
              <Skeleton className="h-8 w-64" />
              <Skeleton className="h-5 w-40" />
              <div className="flex gap-[var(--space-3)]">
                <Skeleton className="h-6 w-24" />
                <Skeleton className="h-6 w-32" />
              </div>
            </div>
          </div>
        </div>
        <Skeleton className="h-64" />
      </div>
    </div>
  );
}
