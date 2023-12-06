"use client"

import { createTheme } from "@mui/material";

const theme = createTheme({
  palette: {},
  components: {
    MuiCssBaseline: {
      styleOverrides: `body {
          background: linear-gradient(to right, #f56565, #ecc94b, #48bb78);
        }`,
    },
  },
});

export default theme;
