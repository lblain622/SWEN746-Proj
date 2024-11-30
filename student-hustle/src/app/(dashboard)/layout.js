import "./dashboard.css";
import Navbar from "@/components/Navbar";

export default function DashboardLayout({ children }) {
  return (
    <div>
      <Navbar></Navbar>
      <h2>THIS IS DASHBOARD</h2>
      {children}
    </div>
  );
}