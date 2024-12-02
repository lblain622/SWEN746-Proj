'use client';

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Card, CardBody, CardFooter, CardTitle, CardLink } from 'reactstrap';
import { Form, FormGroup, Label, Input, Button, Alert } from 'reactstrap';

export default function Login() {
  const router = useRouter();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleLogin = async () => {
    if (!username || !password) {
      displayError("Please fill in all fields.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        const data = await response.json();
        console.log("Login successful:", data);

        const userResponse = await fetch(`http://localhost:5000/obtain/user/${username}`);

        if (userResponse.ok) {
          const userDataArray = await userResponse.json();
          console.log("User data fetched:", userDataArray);

          const userData = {
            id: userDataArray[0],
            username: userDataArray[1],
            password: userDataArray[2],
            email: userDataArray[3],
            lastLogin: userDataArray[4],
          };

          localStorage.setItem("currentUser", JSON.stringify(userData));
          
          router.push("/services");
        } else {
          displayError("Error fetching user details.");
        }
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
              <Label for="username">Username</Label>
              <Input 
                type="text" 
                id="username"
                placeholder="Enter your username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
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
        <CardFooter>
          <CardLink href="/register">Register</CardLink>
        </CardFooter>
      </Card>
    </div>
  );
}