"use client";
import { useSearchParams } from "next/navigation";
import ResultCard from "../result-card";
import { useEffect, useState } from "react";
import { search } from "../actions";
import Link from "next/link";
export default function WikiResults() {
  const params = useSearchParams();
  const [results, setResults] = useState<Array<any>>([]);
  const [loading, setLoading] = useState<boolean>(true);
  useEffect(() => {
    if (params.get("search") && params.get("dataset")) {
      setLoading(true);
      search(params.get("search") as string, params.get("dataset") as string)
        .then((res) => {
          setResults(res);
        })
        .catch((err) => {
          console.error(err);
        })
        .finally(() => {
          setLoading(false);
        });
    }
  }, []);
  return (
    <>
      <main className=" max-w-4xl py-8 m-auto">
        <Link
          href="/"
          className=" hover:text-primary hover:underline text-white"
        >
          <div className="">🔍 Back to search</div>
        </Link>
        <h3 className="text-4xl mt-4 text-white capitalize">
          {params.get("dataset")} Results:
        </h3>
        <div className="divide-y">
          {results.map((el, index) => {
            return <ResultCard key={index} result={el}></ResultCard>;
          })}
          {loading && (
            <div className="text-center text-white my-12">
              <span className="text-2xl opacity-75">
                Loading Results ⌛ ...
              </span>
              <br></br>
            </div>
          )}
          {results.length === 0 && !loading && (
            <div className="text-center text-white my-12">
              <span className="text-2xl opacity-75">
                There is nothing to see here 🌵 ...
              </span>
              <br></br>
              <Link href="/" className=" hover:text-primary hover:underline">
                <small className="text-sm mt-8">Try a different search</small>
              </Link>
            </div>
          )}
        </div>
      </main>
    </>
  );
}
