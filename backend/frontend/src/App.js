import React from "react";
import Header from "./components/Header";
import './App.css';
import Grid from '@material-ui/core/Grid';
import Album from './components/Album'

function App() {
  return (
    <div className="App">
      <header className="App-header"> <Header/> </header>
      <div className="App-grid">
        <Grid container spacing={6} columnSpacing={{ xs: 6, sm: 2, md: 3 }}>
          <Album/>
        </Grid>
      </div>
    </div>
  );
}


export default App;