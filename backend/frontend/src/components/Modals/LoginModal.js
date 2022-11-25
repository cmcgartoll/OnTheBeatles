import React from 'react';
import ReactDOM from 'react-dom';

const LoginModal = ({ isShowing, hide }) => isShowing ? ReactDOM.createPortal(
  <React.Fragment>
    <div className="modal-overlay"/>
    <div className="modal-wrapper" aria-modal aria-hidden tabIndex={-1} role="dialog">
      <div className="modal">
        <div className="modal-header">
          <button type="button" className="modal-close-button" data-dismiss="modal" aria-label="Close" onClick={hide}>
            <span aria-hidden="true">&ndash;</span>
          </button>
        </div>
        
        <div className="modal-body">
          <span style={{textTransform:'uppercase', color:'#ABABAB'}}>
            Please login to rate albums
          </span>
          <form action=""><input className="text-input-box" type="text" id="username" name="username" minlength="2" placeholder='USERNAME'/></form>
          {/* <form action="" method="POST"> */}
            {/* <input type="text" placeholder="USERNAME" style="text-align: center" name="username" />
            <input type="submit" value="submit" />   */}
          {/* </form> */}
        </div>
      </div>
    </div>
  </React.Fragment>, document.body
) : null;

export default LoginModal;