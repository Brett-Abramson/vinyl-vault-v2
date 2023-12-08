import * as React from "react";
import { RegisterForm } from "@/components/forms";
import Avatar from "@mui/material/Avatar";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import { CustomLink } from "@/components/common";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Vinyl Vault | Register",
  description: "Vinyl Vault Register Page",
};

const Page = () => {
  return (
    <Container component="main" maxWidth="sm">
      <Box
        sx={{
          marginTop: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign up
        </Typography>
        <RegisterForm />
        <Grid container justifyContent="flex-end">
          <Grid item>
            <CustomLink href="/auth/login" variant="body2">
              Already have an account? Sign in
            </CustomLink>
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
};

export default Page;
