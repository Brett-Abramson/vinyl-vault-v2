"use client";

import { makeStore } from "./store";
import { Provider } from "react-redux";

// defines the props for the customProvider component
interface Props {
  children: React.ReactNode;
}

// the makeStore function is called to create a new instance of the Redux Store
// useful in a Next.js application where you may need a fresh store on each server-side rendering
const CustomProvider = ({ children }: Props) => {
  return <Provider store={makeStore()}>{children}</Provider>;
};

export default CustomProvider;
