import React from 'react';
import ReactDOM from 'react-dom';
import { API_URL } from '../../constants';

const LoginModal = ({ isShowing, hide }) => { 
  
  if (isShowing) {
    return ReactDOM.createPortal(
      <React.Fragment>
        <div className="modal-overlay"/>
        <div className="modal-wrapper" aria-modal aria-hidden tabIndex={-1} role="dialog">
          <div className="modal">
            <div className="modal-header">
              <button type="button" className="modal-close-button" data-dismiss="modal" aria-label="Close" onClick={hide}>
                <span aria-hidden="true">&ndash;</span>
              </button>
            </div>
            {/* onKeyDown={(event) => {return event.key != 'Enter';}} */}
            <div className="modal-body">
              <span style={{textTransform:'uppercase', color:'#ABABAB', marginBottom:'10px'}}>
                Please login to rate albums
              </span>
              <form className='input-form' action="" > {/*CEDE put login PATCH stuff here */}
                <input className="text-input-box" type="text" id="first_name" name="first_name" minlength="2" placeholder='FIRST NAME' />
                <input className="text-input-box" type="text" id="last_name" name="last_name" minlength="2" placeholder='LAST NAME'/>
                <input className="text-input-box" type="text" id="username" name="username" minlength="2" placeholder='USERNAME'/>
                <input className="text-input-box" type="email" id="email" name="email" minlength="2" placeholder='EMAIL'/>
                <input className="text-input-box" type="password" id="pwd" name="pwd" minlength="6" placeholder='PASSWORD'/>
                <input className="text-input-box" type="tel" id="phone" name="phone" pattern="+[0-9] ([0-9]{3})-[0-9]{3}-[0-9]{4}" placeholder='+X (XXX)-XXX-XXXX'/>
                <input className="submit-button" type="submit"/>
              </form>
              
              {/* <form action="" method="POST"> */}
                {/* <input type="text" placeholder="USERNAME" style="text-align: center" name="username" />
                <input type="submit" value="submit" />   */}
              {/* </form> */}
            </div>
          </div>
        </div>
      </React.Fragment>, document.body 
    ) 
  } 
} 


export default LoginModal;