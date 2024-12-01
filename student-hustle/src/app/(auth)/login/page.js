'use client';

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Card, CardBody, CardTitle } from 'reactstrap';
import { Form, FormGroup, Label, Input, Button, Alert } from 'reactstrap';

export default function Login() {
  const router = useRouter();
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleLogin = async () => {
    if (!name || !password) {
      displayError("Please fill in all fields.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ name, password })
      });

      if (response.ok) {
        const data = await response.json();
        console.log("Login successful:", data);

        router.push("/services");
      } else {
        const errorData = await response.json();
        displayError(errorData.message || "Login failed. Please try again.");
      }
    } catch (error) {
      console.error("Error during login:", error);
      displayError("An unexpected error occurred. Please try again later.");
    }
  };

  const displayError = (message) => {
    setErrorMessage(message);
    setTimeout(() => setErrorMessage(""), 2000);
  };

  return (
    <div className="d-flex justify-content-center align-items-center min-vh-100">
      <Card style={{ width: '300px' }}>
        <CardBody>
          <CardTitle tag="h1" className="text-center">Welcome to Student Hustle</CardTitle>
          {errorMessage && <Alert color="danger">{errorMessage}</Alert>}
          <Form>
            <FormGroup>
              <Label for="name">Username</Label>
              <Input 
                type="text" 
                id="name" 
                placeholder="Enter your username"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
            </FormGroup>
            <FormGroup>
              <Label for="password">Password</Label>
              <Input 
                type="password" 
                id="password" 
                placeholder="Enter your password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </FormGroup>
            <Button color="primary" block onClick={handleLogin}>Login</Button>
          </Form>
        </CardBody>
      </Card>
    </div>
  );
}