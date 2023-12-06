import { useState, ChangeEvent, FormEvent } from "react";
import { useRegisterMutation } from "@/redux/features/authApiSlice";
import { useRouter } from "next/navigation";
import { toast } from "react-toastify";

const useRegister = () => {
  const router = useRouter();
  const [register, { data, error, isLoading }] = useRegisterMutation();

  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    username: "",
    email: "",
    password: "",
    re_password: "",
  });

  const { first_name, last_name, email, username, password, re_password } =
    formData;

  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [event.target.name]: event.target.value });
  };
  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    register({ first_name, last_name, username, email, password, re_password })
      .unwrap()
      .then(() => {
        toast.success("Please check email to verify account");
        router.push("/auth/login");
      })
      .catch(() => {
        toast.error("Failed to register account");
      });
  };

  return {
    first_name,
    last_name,
    username,
    email,
    password,
    re_password,
    isLoading,
    handleChange,
    handleSubmit,
  };
};

export default useRegister;
