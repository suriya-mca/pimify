module.exports = {
    content: ["templates/admin/index.html"],
    media: false,
    darkMode: "class",
    theme: {
      extend: {
        colors: {
          primary: {
            50: "255 250 240",
            100: "255 238 204",
            200: "254 215 170",
            300: "253 186 114",
            400: "251 146 60",
            500: "245 121 0",
            600: "220 98 10",
            700: "184 79 18",
            800: "140 62 25",
            900: "104 47 24",
          },
        },
        fontSize: {
          0: [0, 1],
          xxs: ["11px", "14px"],
        },
        fontFamily: {
          sans: ["Inter", "sans-serif"],
        },
        minWidth: {
          sidebar: "18rem",
        },
        spacing: {
          68: "17rem",
          128: "32rem",
        },
        transitionProperty: {
          height: "height",
          width: "width",
        },
        width: {
          sidebar: "18rem",
        },
      },
    },
    variants: {
      extend: {
        borderColor: ["checked", "focus-within", "hover"],
        display: ["group-hover"],
        overflow: ["hover"],
        textColor: ["hover"],
      },
    },
  };