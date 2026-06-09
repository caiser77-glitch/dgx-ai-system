/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        opencode: {
          dark: "#080e1a",            // Deep navy background
          light: "#e2e8f0",           // Readable soft-white text
          midGray: "#94a3b8",         // Slate-400 muted text
          darkSurface: "#0f1c32",     // Card/panel surface
          darkSurface2: "#162440",    // Elevated card surface
          borderGray: "#2d4a6e",      // Strong visible border
          lightSurface: "#f1f5f9",    // Light mode surface
          accentBlue: "#3b82f6",      // Blue-500
          accentBlueHover: "#2563eb", // Blue-600
          accentBlueActive: "#1d4ed8",// Blue-700
          dangerRed: "#f87171",       // Red-400 (softer on dark)
          dangerHover: "#ef4444",
          dangerActive: "#dc2626",
          successGreen: "#34d399",    // Emerald-400 (vibrant on dark bg)
          warningOrange: "#fbbf24",   // Amber-400
          warningHover: "#f59e0b",
          warningActive: "#d97706",
          textMuted: "#64748b",       // Slate-500
          textSecondary: "#475569",   // Slate-600
          borderWarm: "#1e3a5f",      // VISIBLE navy border
          borderLight: "#2d4f7a",     // Hover border state
        }
      },
      fontFamily: {
        serif: ["Inter", "Pretendard", "system-ui", "-apple-system", "sans-serif"],
        sans:  ["Inter", "Pretendard", "system-ui", "-apple-system", "sans-serif"],
        mono:  ["Berkeley Mono", "IBM Plex Mono", "ui-monospace", "SFMono-Regular", "Menlo", "Monaco", "Consolas", "monospace"],
      },
      borderRadius: {
        'none':    '0px',
        'sm':      '4px',
        'DEFAULT': '8px',
        'md':      '10px',
        'lg':      '12px',
        'xl':      '16px',
        '2xl':     '20px',
        '3xl':     '24px',
        'full':    '9999px',
      },
      boxShadow: {
        'sm':      '0 1px 3px rgba(0,0,0,0.4)',
        'DEFAULT': '0 4px 12px rgba(0,0,0,0.4)',
        'md':      '0 6px 20px rgba(0,0,0,0.45)',
        'lg':      '0 12px 35px rgba(0,0,0,0.55)',
        'xl':      '0 24px 60px rgba(0,0,0,0.65)',
        '2xl':     '0 32px 80px rgba(0,0,0,0.75)',
        'inner':   'inset 0 2px 6px rgba(0,0,0,0.4)',
        'none':    'none',
        'glow-blue':  '0 0 24px rgba(59,130,246,0.20)',
        'glow-green': '0 0 24px rgba(52,211,153,0.18)',
        'card':       '0 4px 20px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.04)',
      },
    },
  },
  plugins: [],
}
