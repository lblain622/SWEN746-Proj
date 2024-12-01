import React from 'react';
import { NotificationProvider } from '@/context/NotificationContext';

function MyApp({ Component, pageProps }) {
  return (
    <NotificationProvider>
      <Component {...pageProps} />
    </NotificationProvider>
  );
}

export default MyApp;