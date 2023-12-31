import Avatar from "@mui/material/Avatar";
import Box from "@mui/material/Box";
import IconButton from "@mui/material/IconButton";
import Menu from "@mui/material/Menu";
import MenuItem from "@mui/material/MenuItem";
import Tooltip from "@mui/material/Tooltip";
import Typography from "@mui/material/Typography";
import { MouseEventHandler, MouseEvent } from "react";
import { CustomLink } from "..";

interface Props {
  anchorElUser: HTMLElement | null;
  settings: {
    pageTitle: string;
    pageUrl?: string;
    onClick?: MouseEventHandler<HTMLElement>;
  }[];
  handleOpenUserMenu: (event: MouseEvent<HTMLElement>) => void;
  handleCloseUserMenu: () => void;
}

const UserMenu = ({
  settings,
  anchorElUser,
  handleOpenUserMenu,
  handleCloseUserMenu,
}: Props) => {
  return (
    <Box sx={{ flexGrow: 0, justifySelf: "flex-end" }}>
      <Tooltip title="Open settings">
        <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
          <Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg" />
        </IconButton>
      </Tooltip>
      <Menu
        sx={{ mt: "45px" }}
        id="menu-appbar"
        anchorEl={anchorElUser}
        anchorOrigin={{
          vertical: "top",
          horizontal: "right",
        }}
        keepMounted
        transformOrigin={{
          vertical: "top",
          horizontal: "right",
        }}
        open={Boolean(anchorElUser)}
        onClose={handleCloseUserMenu}
      >
        {settings.map((setting) => (
          <MenuItem key={setting.pageTitle} onClick={handleCloseUserMenu}>
            <Typography textAlign="center">
              <CustomLink href={setting.pageUrl} onClick={setting.onClick}>
                {setting.pageTitle}
              </CustomLink>
            </Typography>
          </MenuItem>
        ))}
      </Menu>
    </Box>
  );
};

export default UserMenu;
