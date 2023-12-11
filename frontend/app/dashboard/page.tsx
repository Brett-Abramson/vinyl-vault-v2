"use client"
import useLogout from "../../hooks/use_logout";

const Page = () => {
  const { handleLogout } = useLogout();

  return (
    <main>
      <h1>Dashboard</h1>
      <button onClick={handleLogout}>Logout</button>
    </main>
  );
};

export default Page;
