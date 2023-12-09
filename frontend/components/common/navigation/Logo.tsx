import Typography from "@mui/material/Typography";

const Logo = () => {
  return (
    <Typography
      variant="h5"
      noWrap
      component="a"
      href="#app-bar-with-responsive-menu"
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
  );
};

export default Logo;
