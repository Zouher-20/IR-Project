import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    colors: {
      white: "#f2f2f2",
      primary: "#ffd866",
      secondary: "#77dbe7",
      accent: "#ab9df2",
      "base-1": "#2d2a2e",
      "base-2": "#5b595c",
    },
  },
  plugins: [],
};
export default config;
