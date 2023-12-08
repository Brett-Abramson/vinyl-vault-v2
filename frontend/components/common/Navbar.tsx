import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import Menu from "@mui/material/Menu";
import MenuIcon from "@mui/icons-material/Menu";
import Container from "@mui/material/Container";
import Avatar from "@mui/material/Avatar";
import Tooltip from "@mui/material/Tooltip";
import MenuItem from "@mui/material/MenuItem";
import AlbumTwoToneIcon from "@mui/icons-material/AlbumTwoTone";
import NextLink from "next/link";
import {useMenu} from "@/hooks"
import { NavMenu } from ".";
import UserMenu from "./UserMenu";




const Navbar = () => {


  return (
    <AppBar position="static">
      {/* <Container maxWidth="xl">
        <Toolbar disableGutters>
          <AlbumTwoToneIcon
            sx={{ display: { ex: "none", md: "flex" }, mr: 1 }}
          />
          <Typography
            variant="h6"
            noWrap
            component={NextLink}
            href="#app-bar"
            sx={{
              mr: 2,
              display: { xs: "none", md: "flex" },
              fontWeight: 700,
              letterSpacing: ".3rem",
              color: "inherit",
              textDecoration: "none",
            }}
          >
            LOGO
          </Typography>
            <NavMenu />
          <AlbumTwoToneIcon
            sx={{ display: { ex: "flex", md: "none" }, mr: 1 }}
          />
          <Typography
            variant="h5"
            noWrap
            component={NextLink}
            href="#app-bar"
            sx={{
              mr: 2,
              display: { xs: "flex", md: "none" },
              flexGrow: 1,
              // fontFamily:
              fontWeight: 700,
              letterSpacing: ".3rem",
              color: "inherit",
              textDecoration: "none",
            }}
          >
            LOGO
          </Typography>
          <UserMenu />
        </Toolbar>
      </Container> */}
    </AppBar>
  );
};

export default Navbar;
