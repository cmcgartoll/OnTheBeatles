import React, {useEffect} from "react";
import './App.css';

import Navbar from './components/Navbar/Navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages';
import Account from "./pages/account";
import AlbumFocus from "./pages//albumFocus/albumFocus";

export default function App() {
  useEffect(() => {
    document.title = 'YE OR NE';
  });
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path='/' exact element={<Home/>} />
          <Route path='/account' element={<Account/>} />
          <Route path='/album/:albumId' element={<AlbumFocus/>} />
        </Routes>
      </Router>
      {/* <div className="Nav-bar">
        <header > <Header/> </header>
      </div> */}
      
    </div>
  );
}