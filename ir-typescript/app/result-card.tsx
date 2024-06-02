export default function ResultCard({
  result,
}: {
  result: { id: string; text: string; score: string | number };
}) {
  return (
    <article className="flex items-start py-6 text-white border-accent">
      <div className="min-w-0 flex-auto">
        <h2 className="font-semibold  truncate pr-20">
          <span className="text-primary font-bold">{result.id}</span>
        </h2>
        <div className="mt-2 flex flex-wrap  leading-6  font-medium">
          {result.text}
        </div>
        <div className="text-xs text-end mt-2 text-secondary">
          {result.score}
        </div>
      </div>
    </article>
  );
}
