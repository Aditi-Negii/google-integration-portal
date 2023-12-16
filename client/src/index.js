import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { GoogleOAuthProvider } from '@react-oauth/google';
import {HashRouter} from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <HashRouter>
    <GoogleOAuthProvider clientId="317608915365-5tlcf392ocsu64ceaapc5d1o3nd968th.apps.googleusercontent.com">
      <App />
    </GoogleOAuthProvider>
    </HashRouter>
  </React.StrictMode>
);


