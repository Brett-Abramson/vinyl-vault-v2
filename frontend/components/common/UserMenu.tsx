// "useClient";

// import Box from "@mui/material/Box";
// import Typography from "@mui/material/Typography";
// import IconButton from "@mui/material/IconButton";
// import Menu from "@mui/material/Menu";
// import MenuItem from "@mui/material/MenuItem";
// import Avatar from "@mui/material/Avatar";
// import Tooltip from "@mui/material/Tooltip";
// import { useMenu } from "@/hooks";

// const settings = ["Profile", "Account", "Dashboard", "Logout"];

// const UserMenu = () => {
//   const { anchorElUser, handleOpenUserMenu, handleCloseUserMenu } = useMenu();

//   return (
//     <Box sx={{ flexGrow: 0 }}>
//       <Tooltip title="Open settings">
//         <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
//           <Avatar alt="Remy Sharp" />
//         </IconButton>
//       </Tooltip>
//       <Menu
//         sx={{ mt: "45px" }}
//         id="menu-appbar"
//         anchorEl={anchorElUser}
//         anchorOrigin={{
//           vertical: "top",
//           horizontal: "right",
//         }}
//         keepMounted
//         transformOrigin={{
//           vertical: "top",
//           horizontal: "right",
//         }}
//         open={Boolean(anchorElUser)}
//         onClose={handleCloseUserMenu}
//       >
//         {settings.map((setting) => {
//           return (
//             <Box key={setting}>
//               <MenuItem onClick={handleCloseUserMenu}>
//                 <Typography textAlign="center">{setting}</Typography>
//               </MenuItem>
//             </Box>
//           );
//         })}
//       </Menu>
//     </Box>
//   );
// };

// export default UserMenu;
