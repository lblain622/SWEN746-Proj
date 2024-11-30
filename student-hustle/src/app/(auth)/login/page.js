'use client';

import { Card, CardBody, CardTitle, Form, FormGroup, Label, Input, Button } from 'reactstrap';

export default function Login() {
  return (
    <div className="d-flex justify-content-center align-items-center min-vh-100">
      <Card style={{ width: '300px' }}>
        <CardBody>
          <CardTitle tag="h4" className="text-center">Welcome to Student Hustle</CardTitle>
          <Form>
            <FormGroup>
              <Label for="username">Username</Label>
              <Input type="text" id="username" placeholder="Enter your username" />
            </FormGroup>
            <FormGroup>
              <Label for="password">Password</Label>
              <Input type="password" id="password" placeholder="Enter your password" />
            </FormGroup>
            <Button color="primary" block>Login</Button>
          </Form>
        </CardBody>
      </Card>
    </div>
  );
}