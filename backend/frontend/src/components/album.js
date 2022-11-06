import React, {Component} from "react";
import axios from "axios";
import { API_URL } from "../constants/index.js";
import Grid from '@material-ui/core/Grid';

class Album extends Component {
  state = {
    albums: []
  };

  componentDidMount() {
    this.resetState();
  }

  getAlbums = () => {
    axios.get(API_URL + "albums/").then(res => this.setState({ albums: res.data }));
  };

  resetState = () => {
    this.getAlbums();
  };

  render() {
    const albums = this.state.albums;
    console.log(albums);
    return (
      albums.map(album => (
        <Grid item xs={2}>
          <div>
            <img 
              style={{width:"100%", height:"100%"}}
              src={album.cover}
            />
            <body className="album-name">{album.title}</body>
            <body className="artist-name">{album.artist.join(", ")}</body> 
            <body className="album-date">{album.release_date.substring(0,4)}</body>
            <button className="like-button">Like</button><button className="dislike-button">Dislike</button>
          </div>
        </Grid>
      ))
    );
  }
}

export default Album;