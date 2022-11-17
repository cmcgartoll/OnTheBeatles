import React, { useState, useEffect} from "react";
import axios from "axios";
import { API_URL } from "../constants/index.js";
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import { Link } from 'react-router-dom';
  
export default function Home() {
  const [albums, setAlbums] = useState([]);

  useEffect(() => {
    axios.get(API_URL + "albums/").then((res) => setAlbums(res.data));
  });
  // console.log("sadfasd", albums[0]);
  return (
    <div className="App-grid">
      <Grid container spacing={8} columnSpacing={{xs: 4}}>
        {albums.map(album => (
          <Grid item xs={3}>
            <div className="Grid-item">
              <div className="Rating-bar">
                <Box
                  sx={{
                    width: 35,
                    height: 80,
                    backgroundColor: '#ABABAB',
                    '&:hover': {
                      backgroundColor: '#6E6E6E',
                      opacity: [0.9, 0.8, 0.7],
                    },
                  }}
                />
              </div>
              <div className="Album-box">
                <Link to={`./album/${album.id}`} path="relative" onClick={(e) => console.log(album.id)}>
                  <img
                    style={{width:"100%"}}
                    src={album.cover}
                  />
                </Link>
                <div className="Album-details">
                  <div className="Album-text">
                    <div className="Album-name">{album.title.toUpperCase()}</div>
                    {/* <body className="Artist-name">{album.artist.join(", ").toUpperCase()}</body>  */}
                    <div className="Album-date">{album.release_date.substring(0,4)}</div>
                    {/* <button className="Like-button">Like</button><button className="Dislike-button">Dislike</button> */}
                  </div>
                  <div className="User-rating-box">
                    <Box
                      sx={{
                        width: 30,
                        height: 30,
                        backgroundColor: '#ABABAB',
                        '&:hover': {
                          backgroundColor: '#6E6E6E',
                          opacity: [0.9, 0.8, 0.7],
                        },
                      }}
                    />
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