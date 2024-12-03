'use client';

import React, { useEffect, useState } from 'react';
import { use } from 'react';
import { Card, CardBody, CardTitle, CardText, CardFooter, Button, Row, Col, Container } from 'reactstrap';

export default function Detail({ params }) {
  const { slug } = use(params);
  const [serviceData, setServiceData] = useState(null);
  const [userName, setUserName] = useState("");

  useEffect(() => {
    const fetchService = async () => {
      const res = await fetch(`http://localhost:5000/services/${slug}`);
      const data = await res.json();

      const [id, title, content, price, date, userId] = data;

      const serviceObject = {
        id,
        title,
        content,
        price,
        date,
        userId
      };

      setServiceData(serviceObject);

      const userRes = await fetch(`http://localhost:5000/profile/${userId}`);
      const userData = await userRes.json();

      const fullName = `${userData[1]} ${userData[2]}`;
      setUserName(fullName || "Unknown");
    };

    if (slug) {
      fetchService();
    }
  }, [slug]);

  return (
    <Container className="my-5">
      <h1 className="text-center mb-4">Service Information</h1>
      {serviceData && (
        <Row className="justify-content-center">
          <Col md={10} lg={8}>
            <Card className="shadow-lg border-0" style={{ backgroundColor: '#f8f8f8', minHeight: '400px' }}>
              <CardBody>
                <div className="d-flex justify-content-between">
                  <CardTitle tag="h3" className="text-dark">{serviceData.title}</CardTitle>
                  <span className="text-muted">Service created at: {new Date(serviceData.date).toLocaleDateString()}</span>
                </div>
                <CardText className="text-muted mt-3">Person name: {userName}</CardText>
                <CardText className="text-muted">{serviceData.content}</CardText>
                <div className="d-flex justify-content-between">
                  <CardText className="font-weight-bold">Price: <span className="text-success">${serviceData.price}</span></CardText>
                </div>
              </CardBody>
              <CardFooter className="text-center" style={{ backgroundColor: '#fff', borderTop: '1px solid #ddd' }}>
                <Button color="primary" style={{ fontWeight: 'bold', padding: '10px 20px' }} href="#">Contact</Button>
              </CardFooter>
            </Card>
          </Col>
        </Row>
      )}
    </Container>
  );
}