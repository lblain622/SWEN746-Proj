'use client';

import React, { useState, useEffect } from 'react';
import { Navbar, NavbarBrand, NavbarText } from 'reactstrap';
import { Nav, NavItem, NavLink, Collapse, NavbarToggler } from 'reactstrap';
import { useRouter } from 'next/navigation';

export default function Header() {
  const [collapsed, setCollapsed] = useState(true);
  const [name, setName] = useState("");
  const router = useRouter();

  useEffect(() => {
    const fetchUserProfile = async () => {
      try {
        const currentUser = JSON.parse(localStorage.getItem("currentUser"));
        if (currentUser && currentUser.id) {
          const userId = currentUser.id;

          const response = await fetch(`http://localhost:5000/profile/${userId}`);
          const data = await response.json();

          if (data && data[1]) {
            setName(data[1]);
          }
        }
      } catch (error) {
        console.error("Error fetching profile:", error);
      }
    };

    fetchUserProfile();
  }, []);

  const toggleNavbar = () => setCollapsed(!collapsed);

  const handleLogout = () => {
    localStorage.removeItem("currentUser");

    router.push("/login");
  };

  return (
    <div>
      <Navbar className="d-flex justify-content-between align-items-center" expand="lg">
        <NavbarBrand className="d-flex flex-column align-items-center justify-content-center">
          <h3>Student Hustle</h3>
          <NavbarText>Welcome, {name || "Guest"}</NavbarText>
        </NavbarBrand>

        <NavbarToggler onClick={toggleNavbar} className="me-2" />

        <Collapse isOpen={!collapsed} navbar>
          <Nav navbar className="ms-auto d-flex">
            <NavItem>
              <NavLink href="/messages">Messages</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/services">Services</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/profile">Profile</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/my_services">My Services</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="#" onClick={handleLogout}>Logout</NavLink>
            </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
    </div>
  );
}
