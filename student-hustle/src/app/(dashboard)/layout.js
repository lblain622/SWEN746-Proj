import "./dashboard.css";
import Navbar from "@/components/Header";

export default function DashboardLayout({ children }) {
  return (
    <div>
      <Navbar></Navbar>
      {children}
    </div>
  );
}