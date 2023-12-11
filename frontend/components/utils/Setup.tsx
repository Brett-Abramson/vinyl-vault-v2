"use client"
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { useVerify } from "@/hooks";

const Setup = () => {
  useVerify();

  return <ToastContainer />;
};

export default Setup;
