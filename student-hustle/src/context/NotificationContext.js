import React, { createContext, useContext, useEffect, useState } from 'react';
import io from 'socket.io-client';
import { toast, ToastContainer } from 'react-toastify';

import 'react-toastify/dist/ReactToastify.css';

const NotificationContext = createContext();

const socket = io('http://127.0.0.1:5000');

export const NotificationProvider = ({ children }) => {
  const [currentUsername, setCurrentUsername] = useState('');

  useEffect(() => {
    const user = localStorage.getItem('currentUser');
    if (user) {
      const parsedUser = JSON.parse(user);
      setCurrentUsername(parsedUser.id);
      socket.emit('join', { user_id: parsedUser.id });
      console.log(`User ${parsedUser.id} joined room`);
    }
  }, []);

  useEffect(() => {
    socket.on('receive_message', (message) => {
      toast.info(`New message from ${message.sender_name}: ${message.content}`, {
        position: "top-right",
        autoClose: 3000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
      });
    });

    socket.on('notification', (notification) => {
      toast.info(notification.message, {
        position: "top-right",
        autoClose: 3000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
      });
    });

    return () => {
      socket.off('receive_message');
      socket.off('notification');
    };
  }, []);

  return (
    <NotificationContext.Provider value={{ currentUsername }}>
      {children}
      <ToastContainer />
    </NotificationContext.Provider>
  );
};

export const useNotification = () => {
  const context = useContext(NotificationContext);
  if (!context) {
    throw new Error('useNotification must be used within a NotificationProvider');
  }
  return context;
};