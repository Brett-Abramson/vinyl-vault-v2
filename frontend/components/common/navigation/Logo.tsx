import Typography from "@mui/material/Typography";
import AlbumTwoToneIcon from "@mui/icons-material/AlbumTwoTone";
import { CustomLink } from "..";
import  Box  from "@mui/material/Box";

const Logo = () => {
  return (
    <CustomLink href="/" underline="none">
      <Box display="flex">
        <AlbumTwoToneIcon sx={{ mr: 1, mt: 0.5 }} />
        <Typography
          variant="h5"
          noWrap
          sx={{
            mr: 2,
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
