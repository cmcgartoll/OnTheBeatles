import React, { useEffect } from 'react';
// import { Link } from 'react-router-dom';
import {
  StyledLink,
} from './NavbarElements';
import useModal from "../../hooks/useModal";
import SignUpModal from "../Modals/SignUpModal";
import './Navbar.css'
import '../Modals/Modal.css'
import { useContext } from 'react';
import AuthContext from '../Context/AuthContext';

export default function Navbar() {
  const { user, logoutUser } = useContext(AuthContext);
  const {isShowing, toggle} = useModal();
  
  return (
    <div className='nav-bar'>
      <ul className='nav-grid'>
        <li >
          <StyledLink className='home-button' to="/" >ON THE BEAT</StyledLink>
        </li>
        <li>
          {user ? (
            <p className="login-button" onClick={logoutUser}>Logout</p>
          ) : (
            <p className="login-button" onClick={toggle}>Login</p>
          )}
        </li>
      </ul>
      <SignUpModal
        isShowing={isShowing}
        hide={toggle}
      />
    </div>
    // <>
    //   <Nav>
    //     <Bars /> 
  
    //     <NavMenu>
    //       <NavLink to='/about' activeStyle>
    //         About
    //       </NavLink>
    //       <NavLink to='/events' activeStyle>
    //         Events
    //       </NavLink>
    //       <NavLink to='/annual' activeStyle>
    //         Annual Report
    //       </NavLink>
    //       <NavLink to='/team' activeStyle>
    //         Teams
    //       </NavLink>
    //       <NavLink to='/blogs' activeStyle>
    //         Blogs
    //       </NavLink>  
    //       <NavLink to='/sign-up' activeStyle>
    //         Sign Up
    //       </NavLink>
    //       {/* Second Nav */}
    //       {/* <NavBtnLink to='/sign-in'>Sign In</NavBtnLink> */}
    //     </NavMenu>
    //     <NavBtn>
    //       <NavBtnLink to='/signin'>Sign In</NavBtnLink>
    //     </NavBtn>
    //   </Nav>
    // </>
    );
  };