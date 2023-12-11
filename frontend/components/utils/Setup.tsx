"use client"
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { useVerify } from "@/hooks";

const Setup = () => {
  useVerify(); // persists cookies 

  return <ToastContainer />;
};

export default Setup;
