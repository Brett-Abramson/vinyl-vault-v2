"use client";

import { useRegister } from "@/hooks";
import { Form } from "@/components/forms"
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";


const RegisterForm = () => {
  const {
    first_name,
    last_name,
    username,
    email,
    password,
    re_password,
    isLoading,
    handleChange,
    handleSubmit,
  } = useRegister();

  const config = [
    {
      labelText: "First Name",
      labelId: "first_name",
      type: "text",
      value: first_name,
      required: false,
      fullWidth: false
    },
    {
      labelText: "Last Name",
      labelId: "Last Name",
      type: "text",
      value: last_name,
      required: false,
      fullWidth: false
    },
    {
      labelText: "Username",
      labelId: "username",
      type: "text",
      value: username,
      required: true,
      fullWidth: true
    },
    {
      labelText: "Email",
      labelId: "email",
      type: "email",
      value: email,
      required: true,
      fullWidth: true
    },
    {
      labelText: "Password",
      labelId: "password",
      type: "password",
      value: password,
      required: true,
      fullWidth: true
    },
    {
      labelText: "Confirm Password",
      labelId: "re_password",
      type: "password",
      value: re_password,
      required: true,
      fullWidth: true
    }
  ]


  return (
     <Form 
      config={config}
      isLoading={isLoading}
      btnText="Sign up"
      handleChange={handleChange}
      handleSubmit={handleSubmit}
     />
  );
};
export default RegisterForm;

