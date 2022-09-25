/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['templates/*.html',
  'node_modules/flowbite/**/*.js'],
  theme: {
    extend: {
      colors: {
        darkGrey: '#111827',
        grey: '#1F2937',
        lightGrey: '#374151'
      }
    },
  },
  plugins: [
      require("flowbite/plugin")
  ],
}
