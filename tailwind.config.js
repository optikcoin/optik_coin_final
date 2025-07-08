/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#1E90FF',
        darkbg: '#0f172a'
      }
    }
  },
  plugins: []
};
