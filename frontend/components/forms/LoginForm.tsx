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
      link: {
        linkText: "Forgot password?",
        linkUrl: "/password_reset/"
      },
      required: true,
    },
  ];
  return (
    <Form
      config={config}
      isLoading={isLoading}
      btnText="Sign In"
      handleChange={handleChange}
      handleSubmit={handleSubmit}
    />
  );
};

export default LoginForm;
