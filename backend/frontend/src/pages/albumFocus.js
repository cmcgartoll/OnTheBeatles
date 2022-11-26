import React, {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import axios from "axios";
import { API_URL } from "../constants/index.js";
import { Link } from 'react-router-dom';
import "./albumFocus.css";
  
export default function AlbumFocus() {
    let {albumId} = useParams();
    const [album, setAlbum] = useState({});
    useEffect(() => {
        axios.get(API_URL + "album/" + albumId + "/").then((res) => setAlbum(res.data));
        console.log(album)
    });
     
    return (
        <div className='app'>
            <div className='arrow'> 
                <Link to={`../album/${album.id-1}`} path="relative" onClick={(e) => console.log(album.id)}>
                    <span aria-hidden="true">&lt;</span>
                </Link>
            </div>
            <div className='album-contents'>
                <body className='album-title'>{album.title}</body>
                <div className='album-cover'>
                    <img
                        style={{width:"300px"}}
                        src={album.cover}
                    />
                </div>
                <div className='tracklist'>
                    
                </div>
            </div>
            <div className='arrow'> 
                <Link to={`../album/${album.id+1}`} path="relative" onClick={(e) => console.log(album.id)}>
                    <span aria-hidden="true">&gt;</span> 
                </Link>
            </div>
            
        </div>
            
    );
};