import React, {useState} from 'react';
import ReactDOM from 'react-dom';
import AuthContext from '../Context/AuthContext';
import { useContext } from 'react';

const SignUpModal = ({ isShowing, hide }) => { 
  const {loginUser, signUpUser } = useContext(AuthContext);
  const [isLogin, setIsLogin] = useState(false);

  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");

  let handleSignUp = async (e) => {
    e.preventDefault();
    signUpUser(firstName, lastName, username, email, phone, password);
    hide();
    // navigate(window.location.pathname, {replace=true});
  };

  let handleLogin = async (e) => {
    e.preventDefault();
    loginUser(username, password);
    
    hide();
    // navigate(window.location.pathname);
  };

  if (isShowing) {
    return ReactDOM.createPortal(
      <React.Fragment>
        <div className="modal-overlay"/>
        <div className="modal-wrapper" aria-modal aria-hidden tabIndex={-1} role="dialog">
          {isLogin ? (
            <div className="modal">
              <div className="modal-header">
              <button type="button" className="modal-action-button" data-dismiss="modal" aria-label="Close" onClick={() => {hide(); setIsLogin(false);}}>
                  <span className="modal-close-button" aria-hidden="true">&ndash;</span>
                </button>
                <div style={{marginLeft: 'auto', marginRight: 'auto'}}></div>
                <button type="button" className="modal-action-button" onClick={(e) => {setIsLogin(false)}}>
                  <span className="modal-back-button" aria-hidden="true">&lt;</span>
                </button>
              </div>
              <div className="modal-body">
                <span style={{textTransform:'uppercase', color:'#ABABAB', marginBottom:'10px'}}>
                  Please sign up to rate albums
                </span>
                <form className='input-form' onSubmit={handleSignUp}> 
                  <input className="text-input-box" type="text" id="first_name" name="first_name" minLength="2" value={firstName} placeholder='FIRST NAME' onChange={(e) => setFirstName(e.target.value)}/>
                  <input className="text-input-box" type="text" id="last_name" name="last_name" minLength="2" value={lastName} placeholder='LAST NAME' onChange={(e) => setLastName(e.target.value)}/>
                  <input className="text-input-box" type="text" id="username" name="username" minLength="2" value={username} placeholder='USERNAME' onChange={(e) => setUsername(e.target.value)}/>
                  <input className="text-input-box" type="email" id="email" name="email" minLength="2" value={email} placeholder='EMAIL' onChange={(e) => setEmail(e.target.value)}/>
                  <input className="text-input-box" type="tel" id="phone" name="phone"  value={phone} placeholder='+1234567890' onChange={(e) => setPhone(e.target.value)}/> {/* pattern="+[0-9][0-9]{3}[0-9]{3}[0-9]{4}" */}
                  <input className="text-input-box" type="password" id="pwd" name="pwd" minLength="8" value={password} placeholder='PASSWORD' onChange={(e) => setPassword(e.target.value)}/>
                  <input className="submit-button" type="submit"/>
                </form>
              </div>
            </div>
          ) : (
            <div className="modal">
              <div className="modal-header">
                <button type="button" className="modal-action-button" data-dismiss="modal" aria-label="Close" onClick={hide}>
                  <span className="modal-close-button" aria-hidden="true">&ndash;</span>
                </button>
              </div>
              <div className="modal-body">
                <span style={{textTransform:'uppercase', color:'#ABABAB', marginBottom:'10px'}}>
                  Please login to rate albums
                </span>
                <form className='input-form' onSubmit={handleLogin}> 
                  <input className="text-input-box" type="text" id="username" name="username" minLength="2" value={username} placeholder='USERNAME' onChange={(e) => setUsername(e.target.value)}/>
                  <input className="text-input-box" type="password" id="pwd" name="pwd" minLength="8" value={password} placeholder='PASSWORD' onChange={(e) => setPassword(e.target.value)}/>
                  <input className="submit-button" type="submit"/>
                </form>
              </div>
              <div className="sign-up-text">
                <span>No account? <p onClick={(e) => {setIsLogin(true)}} className="sign-up-link">Sign up here</p></span>
              </div>
            </div>  
          )}
        </div>            
      </React.Fragment>, document.body 
    ) 
  } 
} 


export default SignUpModal;