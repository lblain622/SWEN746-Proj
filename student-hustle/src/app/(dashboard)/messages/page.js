'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { Card, CardBody, CardTitle, Button, ListGroup, ListGroupItem } from 'reactstrap';
import { FaPlus, FaWindowMinimize, FaTimes } from 'react-icons/fa'; // Import the icons
import SendMessage from './send/page'; // Import the SendMessage component
import io from 'socket.io-client';
import { ToastContainer, toast } from 'react-toastify'; // Import toast and ToastContainer

import 'react-toastify/dist/ReactToastify.css'; // Import toast styles

const socket = io('http://127.0.0.1:5000'); // Connect to the SocketIO server

function ViewMessages({ messages, currentUsername, handleConversationClick }) {
  return (
    <Card style={{ width:"100%" }}>
      <CardBody>
        <CardTitle tag="h4" className="text-center">Inbox</CardTitle>
        <ListGroup>
          {messages.length > 0 ? (
            messages.map((message, index) => (
              <ListGroupItem key={index} onClick={() => handleConversationClick(message.from_id)} action>
                <div className="d-flex justify-content-between">
                  <div>
                    <p>{message.sender_name} {message.total_messages}</p>
                    <p>{message.from_id === currentUsername ? `You: ${message.content}` : `${message.sender_name}: ${message.content}`}</p>
                  </div>
                  <div>
                    <small>{message.from_id}</small>
                  </div>
                </div>
              </ListGroupItem>
            ))
          ) : (
            <p>No messages found</p>
          )}
        </ListGroup>
      </CardBody>
    </Card>
  );
}

export default function Messages() {
  const [messages, setMessages] = useState([]);
  const [isComposeOpen, setIsComposeOpen] = useState(false); // State to manage compose window
  const [isComposeMinimized, setIsComposeMinimized] = useState(false); // State to manage minimized state
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

  const fetchMessages = async () => {
    const userId = currentUsername;
    const response = await fetch(`http://127.0.0.1:5000/messages/${userId}`);
    const data = await response.json();
    console.log(data)
    const uniqueMessages = data.messages.reduce((acc, message) => {
      const existing = acc.find(m => m.from_id === message.from_id);
      console.log(message);
      if(message.from_id !== message.to_id){if (!existing || new Date(existing.sent_at) < new Date(message.sent_at)) {
        return acc.filter(m => m.from_id !== message.from_id).concat(message);
      }
      return acc;}
    }, []);
    console.log(uniqueMessages);
    setMessages(uniqueMessages);
  };

  useEffect(() => {
    if (currentUsername) {
      fetchMessages();
      socket.on('receive_message', (message) => {
        if (message.to_id === currentUsername) {
          setMessages((prevMessages) => [...prevMessages, message]);
          toast.info('You have received a new message', {
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
  }, [currentUsername]);

  const handleConversationClick = (fromId) => {
    router.push(`/messages/conversation?fromId=${fromId}`);
  };

  return (
    <div className="d-flex justify-content-center min-vh-100">
      <div className="d-flex w-100 p-4">
        <ViewMessages messages={messages} currentUsername={currentUsername} handleConversationClick={handleConversationClick} />
      </div>
      {!isComposeOpen && (
        <Button 
          color="primary" 
          style={{ 
            position: 'fixed', 
            bottom: '20px', 
            right: '20px', 
            borderRadius: '50%', 
            width: '60px', 
            height: '60px', 
            display: 'flex', 
            justifyContent: 'center', 
            alignItems: 'center',
            zIndex: 1000 // Higher zIndex
          }} 
          onClick={() => setIsComposeOpen(true)} // Open compose window
        >
          <FaPlus size={20} />
        </Button>
      )}
      {isComposeOpen && (
        <div style={{ 
          position: 'fixed', 
          bottom: isComposeMinimized ? '20px' : '20px', 
          right: '20px', 
          width: isComposeMinimized ? '200px' : '600px', 
          height: isComposeMinimized ? '40px' : 'auto',
          zIndex: 1000,
          backgroundColor: 'white',
          border: '1px solid #ccc',
          borderRadius: '8px',
          overflow: 'hidden'
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px', backgroundColor: '#f5f5f5', borderBottom: '1px solid #ccc' }}>
            <span>{isComposeMinimized ? 'Compose' : 'Compose Email'}</span>
            <div>
              <FaWindowMinimize style={{ cursor: 'pointer', marginRight: '10px' }} onClick={() => setIsComposeMinimized(!isComposeMinimized)} />
              <FaTimes style={{ cursor: 'pointer' }} onClick={() => setIsComposeOpen(false)} />
            </div>
          </div>
          {!isComposeMinimized && <SendMessage onClose={() => setIsComposeOpen(false)} onMinimize={() => setIsComposeMinimized(true)} />}
        </div>
      )}
      <ToastContainer /> {/* Add ToastContainer */}
    </div>
  );
}