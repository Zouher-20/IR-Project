export default function ResultCard({
  result,
}: {
  result: { id: string; text: string };
}) {
  return (
    <article className="flex items-start py-6 text-white border-accent">
      <div className="min-w-0 flex-auto">
        <h2 className="font-semibold  truncate pr-20">
          <span className="text-primary font-bold">{result.id}</span>
        </h2>
        <div className="mt-2 flex flex-wrap text-sm leading-6 text-justify font-medium">
          {result.text}
        </div>
      </div>
    </article>
  );
}
