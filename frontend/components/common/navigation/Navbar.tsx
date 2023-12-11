"use client";

import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { useRouter } from "next/navigation";
import { useMenu } from "@/hooks";
import { Logo, NavMenu, UserMenu } from "@/components/common";
import { useAppSelector, useAppDispatch } from "@/redux/hooks";
import { useLogoutMutation } from "@/redux/features/authApiSlice";
import { logout as setLogout } from "@/redux/features/authSlice"; //sets logout state to false




const Navbar = () => {
  const router = useRouter();
  const dispatch = useAppDispatch();

  const [logout] = useLogoutMutation();
  const { isAuthenticated } = useAppSelector((state) => state.auth);

  const handleLogout = () => {
    logout(undefined) // passing undefined to apease typescript
      .unwrap()
      .then(() => {
        dispatch(setLogout());
      })
      .finally(() => {
        router.push("/");
      });
  };

  
  const authLinks = [
    {
      pageTitle: "Dashboard",
      pageUrl: "/dashboard"
    }
  ];
  const guestLinks = [
    {
      pageTitle: "Login",
      pageUrl: "/auth/login"
    },
    {
      pageTitle: "Sign Up",
      pageUrl: "/auth/register"
    }
  ];
  const settings = [
    {
      pageTitle: "Profile",
      pageUrl: "#"
    },
    {
      pageTitle: "Account",
      pageUrl: "/"
    },
    {
      pageTitle: "Dashboard",
      pageUrl: "/dashboard"
    },
    {
      pageTitle: "Logout",
      pageUrl: "/auth/register"
    }
  ]

  const {
    anchorElNav,
    anchorElUser,
    handleOpenNavMenu,
    handleOpenUserMenu,
    handleCloseNavMenu,
    handleCloseUserMenu,
  } = useMenu();

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
            settings={settings}
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
