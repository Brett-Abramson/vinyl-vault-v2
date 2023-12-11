import Typography from "@mui/material/Typography";
import AlbumTwoToneIcon from "@mui/icons-material/AlbumTwoTone";
import { CustomLink } from "..";
import { Box } from "@mui/material";

const Logo = () => {
  return (
    <CustomLink href="/" variant="inherit">
      <Box display="flex">
        <AlbumTwoToneIcon sx={{ mr: 1 }} />
        <Typography
          variant="h5"
          noWrap
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
      </Box>
    </CustomLink>
  );
};

export default Logo;
