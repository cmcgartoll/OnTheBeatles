import React, { createContext, useState, useEffect } from "react";
import jwt_decode from "jwt-decode";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { API_URL } from '../../constants';
import { getBottomNavigationActionUtilityClass } from "@mui/material";

const AuthContext = createContext();

export default AuthContext;

export const AuthProvider = ({ children }) => {
  const [authToken, setAuthToken] = useState(
    localStorage.getItem("authToken") || null
  );
  const [user, setUser] = useState("");

  const loginUser = async (username, password) => {
    try {
      const response = await axios.post(API_URL + "login/", {
        username: username,
        password: password
      }, {headers: {
          "Content-Type": "application/json"
      }})
      setAuthToken(response.data.token);
      setUser(response.data.user);
      console.log(authToken);
      localStorage.setItem("authToken", response.data.token);
    } catch (error) {
      console.log(error)
    }
    // .then(response => 
    //   {setAuthToken(response.data.token);
    //   setUser(response.data.user);
    //   console.log(authToken);
    //   localStorage.setItem("authToken", authToken);}
    // ).catch((error) => console.log(error));
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
      setAuthToken(response.data.token);
      setUser(response.data.user);
      console.log(authToken);
      localStorage.setItem("authToken", response.data.token);
    } catch (error) {
      console.log(error);
    }
    // .then(response => 
    //   {}
    // ).catch((error) => console.log(error));
  };

  const logoutUser = () => {
    setAuthToken(null);
    setUser(null);
    localStorage.removeItem("authToken");
  };

  const contextData = {
    user,
    setUser,
    authToken,
    setAuthToken,
    signUpUser,
    loginUser,
    logoutUser
  };

  useEffect(() => {
    console.log(authToken);
    console.log(user);
    if (authToken) {
      axios.get(API_URL + "token/", 
        {headers: {
          "Authorization": authToken
      }}).then(response => {
        setUser(response.data.user);
        console.log('Here');
      }).catch((error) => {
        alert("Something went wrong! AHHHH");
      })
    }
    // setLoading(false);
  }, [authToken]);

  return (
    <AuthContext.Provider value={contextData}>
      {children}
    </AuthContext.Provider>
  );
};






// import React, { createContext, useState, useEffect } from "react";
// import jwt_decode from "jwt-decode";
// import { useNavigate } from "react-router-dom";
// import axios from "axios";
// import { API_URL } from '../../constants';

// const AuthContext = createContext();

// export default AuthContext;

// export const AuthProvider = ({ children }) => {
//   const [authToken, setAuthToken] = useState("92fd9f772df2ace292a4dd0241c7e174a44154e8"
//     // () =>
//     // localStorage.getItem("authToken")
//     //   ? JSON.parse(localStorage.getItem("authToken"))
//     //   : null
//   );
//   const [user, setUser] = useState(
//     // () =>
//     // localStorage.getItem("authToken")
//     //   ? jwt_decode(localStorage.getItem("authToken"))
//     //   : null
//   );
//   const [loading, setLoading] = useState(true);

//   const navigate = useNavigate();

//   const loginUser = async (username, password) => {
//     // const response = await fetch("http://127.0.0.1:8000/login/", {
//     //   method: "POST",
//     //   headers: {
//     //     "Content-Type": "application/json"
//     //   },
//     //   body: JSON.stringify({
//     //     username,
//     //     password
//     //   })
//     // });
//     console.log("YAY");
//     const response = await axios.post(API_URL + "login/", {
//       username: username,
//       password: password
//     }, {headers: {
//           "Content-Type": "application/json"
//         }})
//     .then(console.log('login modal'))
//     .catch((error) => console.log(error));
//     console.log(response);
//     console.log(response.data.token);

//     if (response.status === 200) {
//       setAuthToken(response.data.token);
//       setUser(response.data.user);
//       console.log(authToken);
//       // localStorage.setItem("authToken", JSON.stringify(authToken));
//       // navigate("/");
//     } else {
//       alert("Something went wrong!");
//     }
//   };
  
//   const signUpUser = async (firstName, lastName, username, email, phone, password) => {
//     axios.post(API_URL + "signup/", {
//       first_name: firstName,
//       last_name: lastName,
//       username: username,
//       email: email,
//       phone: phone,
//       password: password
//     })
//     .then(console.log('sign up modal'))
//     .catch((error) => console.log(error));
//     // if (response.status === 201) {
//     //   alert("YAY");
//     //   // navigate("/signup");
//     // } else {
//     //   alert("Something went wrong!");
//     // }
//   };

//   // const logoutUser = () => {
//   //   setAuthToken(null);
//   //   setUser(null);
//   //   localStorage.removeItem("authToken");
//   // };

//   const contextData = {
//     user,
//     setUser,
//     authToken,
//     setAuthToken,
//     signUpUser,
//     loginUser,
//     logoutUser
//   };

//   // useEffect(() => {
//   //   if (authToken) {
//   //     setUser(jwt_decode(authToken.access));
//   //   }
//   //   setLoading(false);
//   // }, [authToken, loading]);

//   return (
//     <AuthContext.Provider value={contextData}>
//       {loading ? null : children}
//     </AuthContext.Provider>
//   );
// };