import React, {useState, useEffect, useContext} from 'react';
import {useParams} from 'react-router-dom';
import axios from "axios";
import { API_URL, TOT_ALBUMS } from "../../constants/index.js";
import { Link } from 'react-router-dom';
import "./albumFocus.css";
import leftArrow from "../../images/leftArrow.png";
import rightArrow from "../../images/rightArrow.png";
import Track from './track.js';
import AuthContext from '../../components/Context/AuthContext.js';
  
export default function AlbumFocus() {
    // const navigate = useNavigate();
    const {setLoading, authToken} = useContext(AuthContext);
    let {albumId} = useParams();
    const [album, setAlbum] = useState({});
    const [tracklist, setTracklist] = useState({});

    useEffect(() => { 
        setLoading(true);
        // console.log(albumId);
        mountAlbumFocus();
    }, [albumId]);

    useEffect(() => {
        // if (authToken == localStorage.getItem('authToken')) {
            // window.location.
        // }
    }, [authToken]);

    const mountAlbumFocus = async () => {
        await axios.get(API_URL + "album/" + albumId + "/", 
            {headers: {
                "Authorization": localStorage.getItem('authToken')
        }})
        .then((res) => { 
            // console.log(res.data);
            setAlbum(res.data); setTracklist(Object.fromEntries(res.data.songs.map(song => [song.name, song.rating]))) 
        })
        .catch(e => {
            console.log(e.toJSON())
        });
    }

    useEffect(() => {
        // console.log('CHANGE');
        // console.log(tracklist);
    }, [tracklist]);
    
    const albumBeforeID = (album.id !== 1) ? album.id-1 : TOT_ALBUMS;
    const albumAfterID = (album.id !== TOT_ALBUMS) ? album.id+1 : 1;
     
    return (
        <div className='app'>
            <div className='arrow'> 
                <Link to={`../album/${albumBeforeID}`} path="relative">
                    <img 
                        style={{height:"80px"}}
                        src={leftArrow}
                        alt={'Left'}
                    />
                </Link>
            </div>
            <div className='album-contents'>
                <p className='album-title'>{album.title}</p>
                <div className='album-cover'>
                    <img
                        style={{width:"350px"}}
                        src={album.cover}
                        alt={album.title}
                    />
                </div>
                <div className='tracklist-wrapper'>
                    {Object.entries(tracklist).map(([song, rating], i) => (
                        // console.log(`${song} ${rating}`)
                        <Track tracknumber={i} trackname={song} rating={rating} albumId={albumId} key={song} myKey={song} />
                    ))}
                </div>
            </div>
            <div className='arrow'> 
                <Link to={`../album/${albumAfterID}`} path="relative">
                    <img
                        style={{height:"80px"}}
                        src={rightArrow}
                        alt={'Right'}
                    />   
                </Link>
            </div>
        </div>
    );
};