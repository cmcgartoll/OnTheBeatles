import React from 'react';
// import { Link } from 'react-router-dom';
import {
  StyledLink,
} from './NavbarElements';

export default function Navbar() {
    return (
      <div className='Nav-bar'>
        <StyledLink to="/" >Ye or Ne</StyledLink>
        <StyledLink to="/" >Ye or Ne</StyledLink>
        <StyledLink to="/" >Ye or Ne</StyledLink>
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