// Signin.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { GoogleLogin } from '@react-oauth/google';
import { jwtDecode } from 'jwt-decode';
import './Signin.css';

function Signin() {
  const navigate = useNavigate();
  const [user, setUser] = useState();

  const handleLoginSuccess = (credentialResponse) => {
    const userObject = jwtDecode(credentialResponse.credential);
    setUser(userObject);
    console.log("Logged in successfully!")
    navigate('/home');
  };

  return (
    <div className="signin-container">
      <div className="signin-content">
        <h1 className="signin-heading">Welcome to Your App</h1>
        <p className="signin-subtext">Sign in to get started</p>
        <GoogleLogin
          onSuccess={handleLoginSuccess}
          onError={() => console.log('Login Failed')}
        />
      </div>
    </div>
  );
}

export default Signin;
