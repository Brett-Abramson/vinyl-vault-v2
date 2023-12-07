"use client";
import Container from "@mui/material/Container";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import { useActivationMutation } from "@/redux/features/authApiSlice";
import { useEffect } from "react";
import { toast } from "react-toastify";
import { useRouter } from "next/navigation";

interface Props {
  params: {
    uid: string;
    token: string;
  };
}

const Page = ({ params }: Props) => {
  const router = useRouter();
  const [activation] = useActivationMutation();

  useEffect(() => {
    const { uid, token } = params;
    activation({ uid, token })
      .unwrap()
      .then(() => {
        toast.success("Account activated");
      })
      .catch(() => {
        toast.error("Failed to activate account");
      })
      .finally(() => {
        router.push("/auth/login/");
      });
  }, []);

  return (
    <Container component="main">
      <Box
        sx={{
          marginTop: 8,
          marginBottom: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Typography component="h1" variant="h5">
          Activating your acount...
        </Typography>
      </Box>
    </Container>
  );
};

export default Page;
