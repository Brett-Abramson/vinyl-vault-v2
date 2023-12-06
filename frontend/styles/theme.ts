"use client";

import { Theme, createTheme } from "@mui/material";

const theme: Theme = createTheme({});

export const darkTheme: Theme = createTheme({
  palette: {
    mode: "dark",
  },
});

export default theme;
