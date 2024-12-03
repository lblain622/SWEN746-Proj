"use client";
import React, { useState } from "react";
import {
  Form,
  FormGroup,
  Label,
  Input,
  Button,
  Container,
  Row,
  Col,
  Alert,
} from "reactstrap";
import { useRouter } from "next/navigation";

export default function Register() {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
  });
  const [successMessage, setSuccessMessage] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const router = useRouter();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:5000/create/user", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setSuccessMessage("Registration successful! Redirecting to login...");
        setFormData({
          username: "",
          email: "",
          password: "",
        });

        setTimeout(() => {
          router.push("/login");
        }, 2000);
      } else {
        const errorData = await response.json();
        setErrorMessage(errorData.message || "Error during registration. Please try again.");
      }
    } catch (error) {
      console.error("Network error:", error);
      setErrorMessage("An unexpected error occurred. Please try again.");
    }
  };

  const navigateToLogin = () => {
    router.push("/login");
  };

  return (
    <Container className="mt-5">
      <Row className="justify-content-center">
        <Col md={6}>
          <div className="border p-4 bg-light">
            <h2 className="text-center mb-4">Create Your Account</h2>
            {successMessage && <Alert color="success">{successMessage}</Alert>}
            {errorMessage && <Alert color="danger">{errorMessage}</Alert>}
            <Form onSubmit={handleSubmit}>
              <FormGroup>
                <Label for="username">Username</Label>
                <Input
                  type="text"
                  name="username"
                  id="username"
                  value={formData.username}
                  onChange={handleChange}
                  required
                />
              </FormGroup>
              <FormGroup>
                <Label for="email">Email</Label>
                <Input
                  type="email"
                  name="email"
                  id="email"
                  value={formData.email}
                  onChange={handleChange}
                  required
                />
              </FormGroup>
              <FormGroup>
                <Label for="password">Password</Label>
                <Input
                  type="password"
                  name="password"
                  id="password"
                  value={formData.password}
                  onChange={handleChange}
                  required
                />
              </FormGroup>
              <Button color="primary" block type="submit">
                Register
              </Button>
            </Form>
            <Button
              color="secondary"
              block
              className="mt-3"
              onClick={navigateToLogin}
            >
              Back to Login
            </Button>
          </div>
        </Col>
      </Row>
    </Container>
  );
}
