import React, { createContext, useState, useEffect, } from "react";
import axios from "axios";
import { API_URL } from '../../constants';

const AuthContext = createContext();

export default AuthContext;

export const AuthProvider = ({ children }) => {
  const [authToken, setAuthToken] = useState(
    localStorage.getItem("authToken") || null
  );
  const [user, setUser] = useState(null);

  const [loading,setLoading] = useState(true);

  const loginUser = async (username, password) => {
    try {
      const response = await axios.post(API_URL + "login/", {
        username: username,
        password: password
      }, {headers: {
          "Content-Type": "application/json"
      }})
      setUser(response.data.user);
      localStorage.setItem("authToken", response.data.token);
      window.location.reload('false');
    } catch (error) {
      console.log(error)
    }
  };
  
  const signUpUser = async (firstName, lastName, username, email, phone, password) => {
    try {
      const response = await axios.post(API_URL + "signup/", {
        first_name: firstName,
        last_name: lastName,
        username: username,
        email: email,
        phone: phone,
        password: password
      })
      setUser(response.data.user);
      localStorage.setItem("authToken", response.data.token);
      window.location.reload('false');
    } catch (error) {
      console.log(error);
    }
  };

  const logoutUser = () => {
    setAuthToken(null);
    setUser(null);
    localStorage.removeItem("authToken");
    window.location.reload('false');
  };

  const contextData = {
    user,
    setUser,
    authToken,
    setAuthToken,
    signUpUser,
    loginUser,
    logoutUser,
    setLoading
  };

  useEffect(() => {
    // console.log("Loading");
    if (authToken) {
      axios.get(API_URL + "token/", 
        {headers: {
          "Authorization": authToken
      }}).then(response => {
        setUser(response.data.user);
      }).catch((error) => {
        alert("Something went wrong! AHHHH");
      })
    }
    setLoading(false);
  }, [authToken, loading]);

  return (
    <AuthContext.Provider value={contextData}>
      {children}
    </AuthContext.Provider>
  );
};

