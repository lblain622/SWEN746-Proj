'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { Card, CardBody, CardTitle, Form, FormGroup, Label, Input, Button } from 'reactstrap';
import { FaWindowMinimize, FaTimes } from 'react-icons/fa';
import io from 'socket.io-client';
import { ToastContainer, toast } from 'react-toastify';

import 'react-toastify/dist/ReactToastify.css';

const socket = io('http://127.0.0.1:5000');

export default function SendMessage({ onClose, onMinimize }) {
  const [toUserId, setToUserId] = useState('');
  const [content, setContent] = useState('');
  const router = useRouter();
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
    const senderName = parsedUser.name || 'Unknown';
    socket.emit('send_message', { from_id: currentUsername, to_id: toUserId, content, sender_name: senderName });
    onClose();
  };

  useEffect(() => {
    socket.on('message_sent', (message) => {
      if (message.from_id === currentUsername) {
        toast.success('Message sent successfully', {
          onClick: () => router.push('/messages')
        });
      }
    });
    return () => {
      socket.off('message_sent');
    };
  }, [currentUsername]);

  return (
    <div className="d-flex justify-content-center align-items-center">
      <Card style={{ width: '600px', position: 'fixed', bottom: '20px', right: '20px' }}>
        <CardBody>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <CardTitle tag="h4" className="text-center">Compose Email</CardTitle>
            <div>
              <FaWindowMinimize style={{ cursor: 'pointer', marginRight: '10px' }} onClick={onMinimize} />
              <FaTimes style={{ cursor: 'pointer' }} onClick={onClose} />
            </div>
          </div>
          <Form>
            <FormGroup>
              <Label for="toUserId">To</Label>
              <Input type="text" id="toUserId" placeholder="Enter recipient ID" value={toUserId} onChange={(e) => setToUserId(e.target.value)} />
            </FormGroup>
            <FormGroup>
              <Label for="content">Message</Label>
              <Input type="textarea" id="content" placeholder="Enter your message" value={content} onChange={(e) => setContent(e.target.value)} style={{ height: '200px' }} />
            </FormGroup>
            <Button color="primary" block onClick={handleSendMessage}>Send</Button>
          </Form>
        </CardBody>
      </Card>
      <ToastContainer />
    </div>
  );
}