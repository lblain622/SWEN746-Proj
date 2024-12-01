'use client';

import { useState, useEffect } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import { Card, CardBody, CardTitle, Button, ListGroup, ListGroupItem, Input, InputGroup, InputGroupText } from 'reactstrap';
import { FaTelegramPlane } from 'react-icons/fa';
import io from 'socket.io-client';
import { toast, ToastContainer } from 'react-toastify';

import 'react-toastify/dist/ReactToastify.css';

const socket = io('http://127.0.0.1:5000');

export default function Conversation() {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [currentUsername, setCurrentUsername] = useState('');
  const router = useRouter();
  const searchParams = useSearchParams();
  const fromId = searchParams.get('fromId');

  useEffect(() => {
    const user = localStorage.getItem('currentUser');
    if (user) {
      const parsedUser = JSON.parse(user);
      setCurrentUsername(parsedUser.id);
      socket.emit('join', { user_id: parsedUser.id });
      console.log(`User ${parsedUser.id} joined room`);
    }
  }, []);

  const fetchConversation = async () => {
    const response = await fetch(`http://127.0.0.1:5000/messages/conversation?fromId=${fromId}&toId=${currentUsername}`);
    const data = await response.json();
    setMessages(data.messages);
  };

  useEffect(() => {
    if (fromId && currentUsername) {
      fetchConversation();
      socket.on('received_message', (message) => {
        console.log('Received message:', message);
        {
          setMessages((prevMessages) => [...prevMessages, message]);
          toast.success('Message received successfully', {
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
    }
    return () => {
      socket.off('receive_message');
      socket.off('message_sent');
    };
  }, [fromId, currentUsername]);

  const handleSendMessage = () => {
    const user = localStorage.getItem('currentUser');
    const parsedUser = user ? JSON.parse(user) : {};
    const senderName = parsedUser.name || 'Unknown';
    const messageData = { from_id: currentUsername, to_id: fromId, content: newMessage, sender_name: senderName };
    console.log('Sending message:', messageData);
    socket.emit('send_message', messageData);
    setMessages((prevMessages) => [...prevMessages, messageData]);
    setNewMessage('');
  };

  return (
    <div className="d-flex justify-content-center align-items-center min-vh-100">
      <Card style={{ width: '600px' }}>
        <CardBody>
          <CardTitle tag="h4" className="text-center">Conversation</CardTitle>
          <Button color="secondary" onClick={() => router.back()}>Back</Button>
          <ListGroup style={{ marginTop: '20px', marginBottom: '60px' }}>
            {messages.length > 0 ? (
              messages.map((message, index) => (
                <ListGroupItem 
                  key={index} 
                  style={{ 
                    display: 'flex', 
                    justifyContent: message.from_id === currentUsername ? 'flex-end' : 'flex-start', 
                    backgroundColor: message.from_id === currentUsername ? '#e0f7fa' : '#f1f8e9',
                    borderRadius: '10px',
                    marginBottom: '10px',
                    alignSelf: message.from_id === currentUsername ? 'flex-end' : 'flex-start',
                    maxWidth: '70%'
                  }}
                >
                  <div>
                    <div style={{ fontWeight: 'bold' }}>{message.sender_name}</div>
                    <div>{message.content}</div>
                  </div>
                </ListGroupItem>
              ))
            ) : (
              <p>No messages found</p>
            )}
          </ListGroup>
          <InputGroup style={{ position: 'fixed', bottom: '20px', width: '600px' }}>
            <Input 
              type="text" 
              placeholder="Type a message..." 
              value={newMessage} 
              onChange={(e) => setNewMessage(e.target.value)} 
            />
            <InputGroupText>
              <Button color="primary" onClick={handleSendMessage}>
                <FaTelegramPlane />
              </Button>
            </InputGroupText>
          </InputGroup>
        </CardBody>
      </Card>
      <ToastContainer />
    </div>
  );
}