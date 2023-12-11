"use client";

import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { useLogout, useMenu } from "@/hooks";
import { Logo, NavMenu, UserMenu } from "@/components/common";


const Navbar = () => {

  const {
    anchorElNav,
    anchorElUser,
    handleOpenNavMenu,
    handleOpenUserMenu,
    handleCloseNavMenu,
    handleCloseUserMenu,
  } = useMenu();
  const { handleLogout, isAuthenticated } = useLogout();

  const authLinks = [
    {
      pageTitle: "Dashboard",
      pageUrl: "/dashboard",
    },
  ];
  const guestLinks = [
    {
      pageTitle: "Login",
      pageUrl: "/auth/login",
    },
    {
      pageTitle: "Sign Up",
      pageUrl: "/auth/register",
    },
  ];
  const settings = [
    {
      pageTitle: "Profile",
      pageUrl: "#",
    },
    {
      pageTitle: "Account",
      pageUrl: "/",
    },
    {
      pageTitle: "Dashboard",
      pageUrl: "/dashboard",
    },
    {
      pageTitle: "Logout",
      onClick: handleLogout,
    },
  ];


  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Box display={{ xs: "none", md: "flex" }}>
            <Logo />
          </Box>
          <NavMenu
            pages={isAuthenticated ? authLinks : guestLinks}
            anchorElNav={anchorElNav}
            handleOpenNavMenu={handleOpenNavMenu}
            handleCloseNavMenu={handleCloseNavMenu}
          />
          <Box display={{ xs: "flex", md: "none" }} flexGrow={1}>
            <Logo />
          </Box>
          <UserMenu
            settings={isAuthenticated ? settings : guestLinks}
            anchorElUser={anchorElUser}
            handleOpenUserMenu={handleOpenUserMenu}
            handleCloseUserMenu={handleCloseUserMenu}
          />
        </Toolbar>
      </Container>
    </AppBar>
  );
};
export default Navbar;
