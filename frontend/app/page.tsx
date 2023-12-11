import Image from "next/image";
import styles from "./page.module.css";
import { Metadata } from "next";
import { CustomLink } from "@/components/common";

export const metadata: Metadata = {
  title: "Vinyl Vault | Home",
  description: "Vinyl Vault Home Page"
}

const Home = () => {
  return (
    <main>
      <h1>Vinyl Vault</h1>
    </main>
  );
};

export default Home;
