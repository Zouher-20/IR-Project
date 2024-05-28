"use client";
import { useSearchParams } from "next/navigation";
import ResultCard from "../result-card";
import { useEffect, useState } from "react";
import { search } from "../actions";
import Link from "next/link";
export default function WikiResults() {
  const params = useSearchParams();
  const [results, setResults] = useState<Array<any>>([]);
  useEffect(() => {
    if (params.get("search") && params.get("dataset")) {
      search(params.get("search") as string, params.get("dataset") as string)
        .then((res) => {
          console.log(res);
          const mappedResults = [];
          for (const key in res) {
            if (Object.prototype.hasOwnProperty.call(res, key)) {
              const text = res[key];
              mappedResults.push({
                id: key,
                text,
              });
            }
          }
          setResults(mappedResults);
        })
        .catch((err) => {
          console.error(err);
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
          {results.length === 0 && (
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
