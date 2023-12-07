import { useState, ChangeEvent, FormEvent } from "react";
import { useLoginMutation } from "@/redux/features/authApiSlice";
import { useRouter } from "next/navigation";
import { toast } from "react-toastify";

const useLogin = () => {
  const router = useRouter();
  const [login, { data, error, isLoading }] = useLoginMutation();

  const [formData, setFormData] = useState({
    username: "",
    password: "",
  });

  const { username, password } = formData;

  const handleChange = (event: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };
  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    login({ username, password })
      .unwrap()
      .then(() => {
        toast.success("Logged In");
        router.push("/dashboard");
      })
      .catch(() => {
        toast.error("Failed to Log In");
      });
  };

  return {
    username,
    password,
    isLoading,
    handleChange,
    handleSubmit,
  };
};

export default useLogin;
