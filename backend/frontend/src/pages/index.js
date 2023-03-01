import React, { useState, useEffect, useContext} from "react";
import axios from "axios";
import { API_URL } from "../constants/index.js";
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import { Link } from 'react-router-dom';
import AuthContext from "../components/Context/AuthContext.js";
import "../App.css";
  
export default function Home() {
  const {user, authToken} = useContext(AuthContext);
  const [albums, setAlbums] = useState([]);
  
  useEffect(() => {
    axios.get(API_URL + "albums/", 
    {headers: {
      "Authorization": localStorage.getItem('authToken')
  }}).then((res) => setAlbums(res.data));
  }, [authToken]);

  useEffect(() => {
    // console.log(albums);
  }, [albums]);

  const handleRatingChange = (albumId, rating) => {
  if (rating === 0) {
    rating = null;
  }
  axios.post(API_URL + "album-rating/" + albumId + "/", {
    rating: rating,
  },{headers: {"Authorization": authToken}}).then((response) => {
    axios.get(API_URL + "albums/", 
    {headers: {
      "Authorization": localStorage.getItem('authToken')
    }}).then((res) => setAlbums(res.data));
  }).catch((error) => {
    console.error(error);
  });
  // console.log(albums)
}

  return (
    <div className="App-grid">
      <Grid container spacing={8} columnSpacing={{xs: 1}}>
        {albums.map(album => (
          <Grid item xs={12} sm={6} md={4} lg={3} key={album.id}>
            <div className="Grid-item">
              <div className="Rating-bar">
                <Box className="average-album-rating-wrapper"
                  sx={{
                    width: 30,
                    height: ((album.average_rating.rating__avg ? album.average_rating.rating__avg : 5)/10).toFixed(1),
                    backgroundColor: '#ABABAB',
                  }}
                > 
                  <p className="average-album-rating" >{album.average_rating.rating__avg ? (album.average_rating.rating__avg).toFixed(1) : "_"}</p>
                </Box>
              </div>
              <div className="Album-box">
                <Link to={`./album/${album.id}`} path="relative" onClick={(e) => console.log(album.id)}>
                  <img
                    style={{width:"100%"}}
                    src={album.cover}
                    alt={album.title}
                  />
                </Link>
                <div className="Album-details">
                  <div className="Album-text">
                    <div className="Album-name">{album.title === 'My Beautiful Dark Twisted Fantasy' ? 'MBDTF' : album.title.toUpperCase()}</div>
                    {/* <body className="Artist-name">{album.artist.join(", ").toUpperCase()}</body>  */}
                    <div className="Album-date">{album.release_date.substring(0,4)}</div>
                    {/* <button className="Like-button">Like</button><button className="Dislike-button">Dislike</button> */}
                  </div>
                  <div className="User-rating-box">
                      {user ? 
                      <form className='input-form' onSubmit={(e) => e.preventDefault()}> 
                        <select className = 'album-rating-dropdown' value={album.rating ? album.rating : ""} onChange={(e) => handleRatingChange(album.id, e.target.value)}>
                          
                          <option value = {0}>_</option>
                          <option value = {1}>1</option>
                          <option value = {2}>2</option>
                          <option value = {3}>3</option>
                          <option value = {4}>4</option>
                          <option value = {5}>5</option>
                          <option value = {6}>6</option>
                          <option value = {7}>7</option>
                          <option value = {8}>8</option>
                          <option value = {9}>9</option>
                          <option value = {10}>10</option>
                        </select>
                        {/* <input className="text-input-box" type="text" id="album_rating" name="album_rating" minLength="2" value={album.rating ? album.rating : ""} onChange={(e) => handleRatingChange(album.id, e.target.value)}/> */}
                      </form>
                      : <div className="empty-album-rating-box">_</div>
                      }
                    {/* </Box> */}
                  </div>
                </div>
              </div>
            </div>
          </Grid>
        ))}
      </Grid>
    </div>
  );
};