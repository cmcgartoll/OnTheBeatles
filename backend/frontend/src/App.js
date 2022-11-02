import React from "react";
import Header from "./components/Header";
import './App.css';
import Grid from '@material-ui/core/Grid';

function App() {
  return (
    <div className="App">
      <header className="App-header"> <Header/> </header>
      <div className="App-grid">
        <Grid container spacing={6} columnSpacing={{ xs: 6, sm: 2, md: 3 }}>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b273cad190f1a73c024e5a40dddd'}
              />
              <body className="album-name">Donda</body>
              <body className="artist-name">Kanye West</body> 
              <body className="album-date">2021</body>
              <button className="like-button">Like</button><button className="dislike-button">Dislike</button>
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b2731bb797bbfe2480650b6c2964'}
              />
              <body className="album-name">JESUS IS KING</body>
              <body className="artist-name">Kanye West</body> 
              <body className="album-date">2019</body>
              <button className="like-button">Like</button><button className="dislike-button">Dislike</button>
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b273013c00ee367dd85396f79c82'}
              />
              <body className="album-name">KIDS SEE GHOSTS</body>
              <body className="artist-name">Kanye West, Kid Cudi, KIDS SEE GHOSTS</body> 
              <body className="album-date">2018</body>
              <button className="like-button">Like</button><button className="dislike-button">Dislike</button>
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b2730cd942c1a864afa4e92d04f2'}
              />
              <body className="album-name">ye</body>
              <body className="artist-name">Kanye West</body> 
              <body className="album-date">2018</body>
              <button className="like-button">Like</button><button className="dislike-button">Dislike</button>
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b2732a7db835b912dc5014bd37f4'}
              />
              <body className="album-name">The Life of Pablo</body>
              <body className="artist-name">Kanye West</body> 
              <body className="album-date">2016</body>
              <button className="like-button">Like</button><button className="dislike-button">Dislike</button>
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b2731dacfbc31cc873d132958af9'}
              />
              <body className="album-name">Yeezus</body>
              <body className="artist-name">Kanye West</body> 
              <body className="album-date">2013</body>
              <button className="like-button">Like</button><button className="dislike-button">Dislike</button>
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b273bf2d62374f877d312b34e67a'}
              />
              <body className="album-name">Watch the Throne</body>
              <body className="artist-name">Kanye West, JAY-Z</body> 
              <body className="album-date">2011</body>
              <button className="like-button">Like</button><button className="dislike-button">Dislike</button>
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b273d9194aa18fa4c9362b47464f'}
              />
              <body className="album-name">My Beautiful Dark Twisted Fantasy</body>
              <body className="artist-name">Kanye West</body> 
              <body className="album-date">2010</body>
              <button className="like-button">Like</button><button className="dislike-button">Dislike</button>
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b273346d77e155d854735410ed18'}
              />
              <body className="album-name">808s & Heartbreak</body>
              <body className="artist-name">Kanye West</body> 
              <body className="album-date">2008</body>
              <button className="like-button">Like</button><button className="dislike-button">Dislike</button>
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b27326f7f19c7f0381e56156c94a'}
              />
              <body className="album-name">Graduation</body>
              <body className="artist-name">Kanye West</body> 
              <body className="album-date">2007</body>
              <button className="like-button">Like</button><button className="dislike-button">Dislike</button>
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b273428d2255141c2119409a31b2'}
              />
              <body className="album-name">Late Registration</body>
              <body className="artist-name">Kanye West</body> 
              <body className="album-date">2005</body>
              <button className="like-button">Like</button><button className="dislike-button">Dislike</button>
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b27325b055377757b3cdd6f26b78'}
              />
              <body className="album-name">The College Dropout</body>
              <body className="artist-name">Kanye West</body> 
              <body className="album-date">2004</body>
              <button className="like-button">Like</button><button className="dislike-button">Dislike</button> 
            </div>
          </Grid>
        </Grid>
      </div>
    </div>
  );
}


export default App;
