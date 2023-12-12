import Typography from "@mui/material/Typography";


const Copyright = (props: any) => {
  return (
    <Typography
      variant="body2"
      color="text.secondary"
      align="center"
      {...props}
    >
      {"Copyright © "}
        Vinyl Vault
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
};

const Footer = () => {
  return (
    <footer>
      <h1>Footer</h1>
      <Copyright sx={{ mt: 5 }} />
    </footer>
  )
};

export default Footer;