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
    firstName: "",
    lastName: "",
    age: "",
    sex: "",
    studentId: "",
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
      // Step 1: Create the user and get user_id
      const userResponse = await fetch("http://127.0.0.1:5000/create/user", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: formData.username,
          email: formData.email,
          password: formData.password,
        }),
      });

      if (!userResponse.ok) {
        const errorText = await userResponse.text();
        throw new Error(errorText || "Error creating user.");
      }

      const userData = await userResponse.json();
      const userId = userData.id;

      if (!userId) {
        throw new Error("User ID not returned by the backend.");
      }

      // Step 2: Create the profile
      const profilePayload = {
        user_id: userId,
        first_name: formData.firstName,
        last_name: formData.lastName,
        age: parseInt(formData.age),
        sex: formData.sex,
        student_id: formData.studentId,
      };

      console.log("Profile Payload:", profilePayload);

      const profileResponse = await fetch("http://127.0.0.1:5000/profile", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(profilePayload),
      });

      if (!profileResponse.ok) {
        const contentType = profileResponse.headers.get("Content-Type") || "";
        let errorMessage = "Error creating profile.";
        if (contentType.includes("application/json")) {
          const errorData = await profileResponse.json();
          errorMessage = errorData.message || errorMessage;
        } else {
          errorMessage = await profileResponse.text();
        }
        throw new Error(errorMessage);
      }

      setSuccessMessage("Registration successful! Redirecting to login...");
      setFormData({
        username: "",
        email: "",
        password: "",
        firstName: "",
        lastName: "",
        age: "",
        sex: "",
        studentId: "",
      });

      setTimeout(() => {
        router.push("/login");
      }, 2000);
    } catch (error) {
      console.error("Error:", error.message || error);
      setErrorMessage(error.message || "An unexpected error occurred.");
    }
  };

  const handleGoToLogin = () => {
    router.push("/login");
  };

  return (
    <Container className="mt-5">
      <Row className="justify-content-center">
        <Col md={8}>
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
              <FormGroup>
                <Label for="firstName">First Name</Label>
                <Input
                  type="text"
                  name="firstName"
                  id="firstName"
                  value={formData.firstName}
                  onChange={handleChange}
                  required
                />
              </FormGroup>
              <FormGroup>
                <Label for="lastName">Last Name</Label>
                <Input
                  type="text"
                  name="lastName"
                  id="lastName"
                  value={formData.lastName}
                  onChange={handleChange}
                  required
                />
              </FormGroup>
              <FormGroup>
                <Label for="age">Age</Label>
                <Input
                  type="number"
                  name="age"
                  id="age"
                  value={formData.age}
                  onChange={handleChange}
                  required
                />
              </FormGroup>
              <FormGroup>
                <Label for="sex">Sex</Label>
                <Input
                  type="text"
                  name="sex"
                  id="sex"
                  value={formData.sex}
                  onChange={handleChange}
                  required
                />
              </FormGroup>
              <FormGroup>
                <Label for="studentId">Student ID</Label>
                <Input
                  type="text"
                  name="studentId"
                  id="studentId"
                  value={formData.studentId}
                  onChange={handleChange}
                  required
                />
              </FormGroup>
              <Button color="primary" block type="submit">
                Register
              </Button>
              <Button color="secondary" block onClick={handleGoToLogin}>
                Go to Login
              </Button>
            </Form>
          </div>
        </Col>
      </Row>
    </Container>
  );
}
