"use client";

import { useLogin } from "@/hooks";
import { Form } from "@/components/forms";

const LoginForm = () => {
  const { username, password, isLoading, handleChange, handleSubmit } =
    useLogin();

  const config = [
    {
      label: "Username",
      name: "username",
      type: "text",
      value: username,
      required: true,
    },
    {
      label: "Password",
      name: "password",
      type: "password",
      value: password,
      required: true,
    },
  ];
  <Form
    config={config}
    isLoading={isLoading}
    btnText="Log In"
    handleChange={handleChange}
    handleSubmit={handleSubmit}
  />;
};

export default LoginForm;
