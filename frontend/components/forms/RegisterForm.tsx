"use client";

import { useRegister } from "@/hooks";
import { Form } from "@/components/forms";

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
      label: "First Name",
      name: "first_name",
      type: "text",
      value: first_name,
      required: false,
    },
    {
      label: "Last Name",
      name: "last_name",
      type: "text",
      value: last_name,
      required: false,
    },
    {
      label: "Username",
      name: "username",
      type: "text",
      value: username,
      required: true,
    },
    {
      label: "Email",
      name: "email",
      type: "email",
      value: email,
      required: true,
    },
    {
      label: "Password",
      name: "password",
      type: "password",
      value: password,
      required: true,
    },
    {
      label: "Confirm Password",
      name: "re_password",
      type: "password",
      value: re_password,
      required: true,
    },
  ];

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
