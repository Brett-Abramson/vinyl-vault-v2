import Box from "@mui/material/Box";
import IconButton from "@mui/material/IconButton";
import Menu from "@mui/material/Menu";
import MenuIcon from "@mui/icons-material/Menu";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import MenuItem from "@mui/material/MenuItem";
import { CustomLink } from "..";

interface Props {
  pages: {
    pageTitle: string;
    pageUrl: string;
  }[];
  anchorElNav: HTMLElement | null;
  handleOpenNavMenu: (event: React.MouseEvent<HTMLElement>) => void;
  handleCloseNavMenu: () => void;
}

const NavMenu = ({
  pages,
  anchorElNav,
  handleOpenNavMenu,
  handleCloseNavMenu,
}: Props) => {
  return (
    <>
      <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "none" } }}>
        <IconButton size="large" onClick={handleOpenNavMenu} color="inherit">
          <MenuIcon />
        </IconButton>
        <Menu
          id="menu-appbar"
          anchorEl={anchorElNav}
          anchorOrigin={{
            vertical: "bottom",
            horizontal: "left",
          }}
          keepMounted
          transformOrigin={{
            vertical: "top",
            horizontal: "left",
          }}
          open={Boolean(anchorElNav)}
          onClose={handleCloseNavMenu}
          sx={{
            display: { xs: "block", md: "none" },
          }}
        >
          {pages.map((page) => (
            <MenuItem key={page.pageTitle} onClick={handleCloseNavMenu}>
              <CustomLink href={page.pageUrl}>
                <Typography textAlign="center">{page.pageTitle}</Typography>
              </CustomLink>
            </MenuItem>
          ))}
        </Menu>
      </Box>
      <Box
        sx={{
          flexGrow: 1,
          display: { xs: "none", md: "flex" },
          justifySelf: "flex-start",
        }}
      >
        {pages.map((page) => (
          <Button
            key={page.pageTitle}
            onClick={handleCloseNavMenu}
            sx={{ my: 2, color: "white", display: "block" }}
          >
            <CustomLink href={page.pageUrl}>{page.pageTitle}</CustomLink>
          </Button>
        ))}
      </Box>
    </>
  );
};

export default NavMenu;
