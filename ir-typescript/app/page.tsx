import { Press_Start_2P } from "next/font/google";
const pressTheStart = Press_Start_2P({ weight: "400", subsets: ["latin"] });

export default function Home() {
  return (
    <main>
      <form
        method="GET"
        action="/results"
        className="flex min-h-screen flex-col items-center justify-center"
      >
        <h2 className={pressTheStart.className + " text-6xl mb-12 text-accent"}>
          ZAAMM!
        </h2>
        <div className="flex rounded-sm w-[700px] bg-base-2 px-2 ">
          <div className="p-2 bg-base-2 rounded-sm">
            <svg
              width="26px"
              height="26px"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <g id="SVGRepo_bgCarrier" strokeWidth="0" />

              <g
                id="SVGRepo_tracerCarrier"
                strokeLinecap="round"
                strokeLinejoin="round"
              />

              <g id="SVGRepo_iconCarrier">
                <path
                  d="M14.9536 14.9458L21 21M17 10C17 13.866 13.866 17 10 17C6.13401 17 3 13.866 3 10C3 6.13401 6.13401 3 10 3C13.866 3 17 6.13401 17 10Z"
                  stroke="#ffd866"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </g>
            </svg>
          </div>
          <input
            name="search"
            type="text"
            autoComplete="off"
            className="w-full shadow bg-base-2 flex bg-transparent placeholder:text-[#ccc]  pl-2 rounded-sm text-primary outline-0"
            placeholder="Ask ZAAMM! something ..."
          />
        </div>
        <ul className="grid w-[900px] mt-8 gap-6 md:grid-cols-2">
          <li>
            <input
              type="radio"
              id="wiki"
              name="dataset"
              value="wiki"
              className="hidden peer"
              defaultChecked
              required
            />
            <label
              htmlFor="wiki"
              className="inline-flex items-center justify-between w-full p-5 text-[#a1a1a1] transition border rounded-sm cursor-pointer hover:text-primary peer-checked:text-primary peer-checked:bg-base-2 "
            >
              <div className="block">
                <div className="w-full text-lg font-semibold">Wiki</div>
                <div className="w-full text-sm">wikir/en1k/training</div>
              </div>
            </label>
          </li>
          <li>
            <input
              type="radio"
              id="quora"
              name="dataset"
              value="quora"
              className="hidden peer"
              required
            />
            <label
              htmlFor="quora"
              className="inline-flex items-center justify-between w-full p-5 text-[#a1a1a1] transition border rounded-sm cursor-pointer hover:text-primary peer-checked:text-primary peer-checked:bg-base-2 "
            >
              <div className="block">
                <div className="w-full text-lg font-semibold">Quora</div>
                <div className="w-full text-sm">beir/quora</div>
              </div>
            </label>
          </li>
        </ul>
      </form>
    </main>
  );
}
