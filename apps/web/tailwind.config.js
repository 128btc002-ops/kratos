export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        kratos: {
          bg: "#0A0A0B",
          accent: "#00F5D4",
          white: "#FFFFFF",
          error: "#FF3B30",
          success: "#32D74B",
        },
      },
      fontFamily: {
        sans: ["Inter", "sans-serif"],
      },
    },
  },
  plugins: [],
}