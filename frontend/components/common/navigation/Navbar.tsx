"use client";

import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import AlbumTwoToneIcon from "@mui/icons-material/AlbumTwoTone";
import { useRouter } from "next/navigation";
import { useMenu } from "@/hooks";
import { Logo, NavMenu, UserMenu } from "@/components/common";
import { useAppSelector, useAppDispatch } from "@/redux/hooks";
import { useLogoutMutation } from "@/redux/features/authApiSlice";
import { logout as setLogout } from "@/redux/features/authSlice";

const pages = ["Products", "Pricing", "Blog"];
const settings = ["Profile", "Account", "Dashboard", "Logout"];

const Navbar = () => {
  // const router = useRouter();
  // const dispatch = useAppDispatch();

  // const [logout] = useLogoutMutation();
  // const { isAuthenticated } = useAppSelector((state) => state.auth);

  // const handleLogout = () => {
  //   logout(undefined)
  //     .unwrap()
  //     .then(() => {
  //       dispatch(setLogout());
  //     })
  //     .finally(() => {
  //       router.push("/");
  //     });
  // };

  // for these we will use { isAuthenticated ? authLinks : guestLinks } to display
  // const authLinks = (

  // )

  // const guestLinks = (

  //   )

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
          <NavMenu
            pages={pages}
            anchorElNav={anchorElNav}
            handleOpenNavMenu={handleOpenNavMenu}
            handleCloseNavMenu={handleCloseNavMenu}
          />
          
            <AlbumTwoToneIcon
              sx={{ display: { xs: "none", md: "flex" }, mr: 1 }}
            />
            {/* <Logo /> */}
            <Typography
              variant="h5"
              noWrap
              component="a"
              href="/"
              sx={{
                mr: 2,

                flexGrow: 1,
                fontWeight: 700,
                letterSpacing: ".3rem",
                color: "inherit",
                textDecoration: "none",
              }}
            >
              Vinyl Vault
            </Typography>
          
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
