// TODO: Component not yet integrated — wire up during UI fine-tuning

interface SkeletonProps {
  className?: string;
}

export function Skeleton({ className = "" }: SkeletonProps) {
  return (
    <div
      className={`animate-pulse bg-[var(--color-surface-secondary)] ${className}`}
      aria-hidden="true"
    />
  );
}

export function WorkCardSkeleton() {
  return (
    <div className="flex items-center gap-[var(--space-6)] py-[var(--space-5)] border-b border-[var(--color-border)]">
      <Skeleton className="h-8 w-12" />
      <div className="flex-1 space-y-[var(--space-2)]">
        <Skeleton className="h-4 w-48" />
        <Skeleton className="h-3 w-32" />
      </div>
    </div>
  );
}

export function DetailPageSkeleton() {
  return (
    <div className="px-[var(--space-8)] py-[var(--space-10)]">
      <div className="space-y-[var(--space-6)]">
        <Skeleton className="h-6 w-48" />
        <div className="grid gap-[var(--space-8)] lg:grid-cols-[auto_1fr]">
          <Skeleton className="h-36 w-36" />
          <div className="space-y-[var(--space-4)]">
            <Skeleton className="h-8 w-64" />
            <Skeleton className="h-4 w-40" />
            <div className="flex gap-[var(--space-3)]">
              <Skeleton className="h-5 w-24" />
              <Skeleton className="h-5 w-32" />
            </div>
          </div>
        </div>
        <Skeleton className="h-64" />
      </div>
    </div>
  );
}
