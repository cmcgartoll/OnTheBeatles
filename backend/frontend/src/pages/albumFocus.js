import React, {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import axios from "axios";
import { API_URL } from "../constants/index.js";
import { Link } from 'react-router-dom';
import "./albumFocus.css";
import leftArrow from "../images/leftArrow.png";
import rightArrow from "../images/rightArrow.png";
  
export default function AlbumFocus() {
    let {albumId} = useParams();
    const [album, setAlbum] = useState({});
    const [tracklist, setTracklist] = useState([]);
    useEffect(() => { 
        axios.get(API_URL + "album/" + albumId + "/").then((res) => { setAlbum(res.data); setTracklist(res.data.songs) }).catch(e => {console.log(e.toJSON())});
        // setTracklist(album.songs);
        console.log(tracklist);
    });
    const albumBeforeID = (album.id != 1) ? album.id-1 : 12;
    const albumAfterID = (album.id != 12) ? album.id+1 : 1;
    
        
    //     // console.log(tracklist);
    //     // var tracklistArr = [];
    //     // for (var song in tracklist) {
    //     //     console.log(typeof song);
    //     //     tracklistArr.push(tracklist[song]);
    //     // }
    //     // console.log(tracklistArr[0]);
    //     // for (const song in tracklist) { 
    //     //     JSONObject jsonObject = (JSONObject)song;
    //     //     System.out.println(jsonObject.toString()); 
    //     // }
    // });
     
    return (
        <div className='app'>
            <div className='arrow'> 
                <Link to={`../album/${albumBeforeID}`} path="relative" onClick={(e) => console.log(album.id)}>
                    <img
                        style={{height:"80px"}}
                        src={leftArrow}
                    />
                </Link>
            </div>
            <div className='album-contents'>
                <p className='album-title'>{album.title}</p>
                <div className='album-cover'>
                    <img
                        style={{width:"350px"}}
                        src={album.cover}
                    />
                </div>
                <div className='tracklist'>
                    {tracklist.map((song, i) => (
                        <p key={i} className='song'>{i+1}. {song}</p>
                    ))}
                </div>
            </div>
            <div className='arrow'> 
                <Link to={`../album/${albumAfterID}`} path="relative" onClick={(e) => console.log(album.id)}>
                    <img
                        style={{height:"80px"}}
                        src={rightArrow}
                    />   
                </Link>
            </div>
        </div>
    );
};