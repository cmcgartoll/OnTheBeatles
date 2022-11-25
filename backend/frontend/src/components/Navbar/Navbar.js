import React from 'react';
// import { Link } from 'react-router-dom';
import {
  StyledLink,
} from './NavbarElements';
import useModal from "../../hooks/useModal";
import LoginModal from "../Modals/LoginModal";
import './Navbar.css'
import '../Modals/Modal.css'

export default function Navbar() {
  const {isShowing, toggle} = useModal();
  return (
    <div className='nav-bar'>
      <ul className='nav-grid'>
        <li >
          <StyledLink className='home-button' to="/" >Ye or Ne</StyledLink>
        </li>
        <li>
          <text className="login-button" onClick={toggle}>Login</text>
        </li>
      </ul>
      <LoginModal
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