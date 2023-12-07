import * as React from "react";
import { LoginForm } from "@/components/forms";
import Avatar from "@mui/material/Avatar";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import Link from "@mui/material/Link";
import NextLink from "next/link";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Vinyl Vault | Login",
  description: "Vinyl Vault Login Page",
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
          Sign into your account
        </Typography>
        <LoginForm />
        <Grid container justifyContent="flex-end">
          <Grid item>
            <Link component={NextLink} href="/auth/register/" variant="body2">
              Don&apos;t have an account?{" "}
            </Link>
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
};

export default Page;
