const defaultTheme = require("tailwindcss/defaultTheme");

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Instrument Sans", ...defaultTheme.fontFamily.sans],
        serif: ["Instrument Serif", ...defaultTheme.fontFamily.serif],
      }
    },
  },
  plugins: [],
};
