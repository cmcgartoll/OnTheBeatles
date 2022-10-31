import logo from './logo.svg';
import './App.css';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import Header from './components/Header.js'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Header></Header>
        <Grid container spacing={6} columnSpacing={{ xs: 6, sm: 2, md: 3 }}>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b273cad190f1a73c024e5a40dddd'}
              />
              <b>Donda </b><br />
              Kanye West <br />
              2021
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b2731bb797bbfe2480650b6c2964'}
              />
              <b>JESUS IS KING</b><br />
              Kanye West <br />
              2019
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b273013c00ee367dd85396f79c82'}
              />
              <b>KIDS SEE GHOSTS</b><br />
              Kanye West, Kid Cudi, KIDS SEE GHOSTS <br />
              2018
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b2730cd942c1a864afa4e92d04f2'}
              />
              <b>ye</b><br />
              Kanye West <br />
              2018
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b2732a7db835b912dc5014bd37f4'}
              />
              <b>The Life of Pablo</b><br />
              Kanye West <br />
              2016
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b2731dacfbc31cc873d132958af9'}
              />
              <b>Yeezus</b><br />
              Kanye West <br />
              2013
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b273bf2d62374f877d312b34e67a'}
              />
              <b>Watch the Throne</b><br />
              Kanye West, JAY-Z <br />
              2011
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b273d9194aa18fa4c9362b47464f'}
              />
              <b>My Beautiful Dark Twisted Fantasy</b><br />
              Kanye West <br />
              2010
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b273346d77e155d854735410ed18'}
              />
              <b>808s & Heartbreak</b><br />
              Kanye West <br />
              2008
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b27326f7f19c7f0381e56156c94a'}
              />
              <b>Graduation</b><br />
              Kanye West <br />
              2007
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b273428d2255141c2119409a31b2'}
              />
              <b>Late Registration</b><br />
              Kanye West <br />
              2005
            </div>
          </Grid>
          <Grid item xs={2}>
            <div>
              <img 
                style={{width:"100%", height:"100%"}}
                src={'https://i.scdn.co/image/ab67616d0000b27325b055377757b3cdd6f26b78'}
              />
              <b>The College Dropout</b><br />
              Kanye West <br />
              2004
            </div>
          </Grid>
        </Grid>
      </header>
    </div>
  );
}


export default App;
