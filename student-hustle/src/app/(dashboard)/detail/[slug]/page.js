'use client';

import React, { useEffect, useState } from 'react';
import { use } from 'react';
import { toast, ToastContainer } from 'react-toastify';
import { Card, CardBody, CardTitle, CardText, CardFooter, Button, Row, Col, Container, Toast } from 'reactstrap';
import { io } from 'socket.io-client';
const socket = io('http://127.0.0.1:5000');
export default function Detail({ params }) {
  const { slug } = use(params);
  const [serviceData, setServiceData] = useState(null);
  const [userName, setUserName] = useState("");
  const [currentUsername, setCurrentUsername] = useState('');

  useEffect(() => {
    const user = localStorage.getItem('currentUser');
    if (user) {
      const parsedUser = JSON.parse(user);
      setCurrentUsername(parsedUser.id);
      socket.emit('join', { user_id: parsedUser.id });
    }
  }, []);

  const handleSendMessage = () => {
    const user = localStorage.getItem('currentUser');
    const parsedUser = user ? JSON.parse(user) : {};
    const senderName = parsedUser.username || 'Unknown';
    const messageData = { from_id: currentUsername, to_id: serviceData.userId, content: `Hello, I am interested in your service. \n ${window.location.href} \n
     id:${serviceData.id}
     title:${serviceData.title}
     content: ${serviceData.content}
     price: ${serviceData.price}
     date: ${serviceData.date} `, sender_name: senderName };
    socket.emit('send_message', messageData);
    socket.on('message_sent', (message) => {
      console.log('Message sent:', message);
  
      if (message.from_id === currentUsername) {
        toast.success('Message sent successfully', {
          position: "top-right",
          autoClose: 3000,
          hideProgressBar: false,
          closeOnClick: true,
          pauseOnHover: true,
          draggable: true,
          progress: undefined,
        });
      }
    });
  };

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
                <Button color="primary" style={{ fontWeight: 'bold', padding: '10px 20px' }} onClick={handleSendMessage}>Contact</Button>
              </CardFooter>
            </Card>
          </Col>
        </Row>
      )}
      <ToastContainer />
    </Container>
  );
}