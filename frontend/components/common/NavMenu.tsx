// "useClient";

// import Box from "@mui/material/Box";
// import IconButton from "@mui/material/IconButton";
// import Typography from "@mui/material/Typography";
// import Menu from "@mui/material/Menu";
// import MenuIcon from "@mui/icons-material/Menu";
// import MenuItem from "@mui/material/MenuItem";
// import { useMenu } from "@/hooks";

// const myPages = ["Albums", "Your Collection", "Spotify", "Ish"];

// const NavMenu = () => {
//   const { handleOpenNavMenu, handleCloseNavMenu, anchorElNav } = useMenu();

//   return (
//     <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "none" } }}>
//       <IconButton
//         size="large"
//         aria-label="account of current user"
//         aria-controls="menu-appbar"
//         aria-haspopup="true"
//         onClick={handleOpenNavMenu}
//         color="inherit"
//       >
//         <MenuIcon />
//       </IconButton>
//       <Menu
//         id="menu-appbar"
//         anchorEl={anchorElNav}
//         anchorOrigin={{
//           vertical: "bottom",
//           horizontal: "left",
//         }}
//         keepMounted
//         transformOrigin={{
//           vertical: "top",
//           horizontal: "left",
//         }}
//         open={Boolean(anchorElNav)}
//         onClose={handleCloseNavMenu}
//         sx={{
//           display: { ex: "block", md: "none" },
//         }}
//       >
//         {myPages.map((page) => {
//           return (
//             <MenuItem key={page} onClick={handleCloseNavMenu}>
//               <Typography textAlign="center">{page}</Typography>
//             </MenuItem>
//           );
//         })}
//       </Menu>
//     </Box>
//   );
// };

// export default NavMenu;
