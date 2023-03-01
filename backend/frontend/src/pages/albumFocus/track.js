import './albumFocus.css';
import React, {useState, useEffect, useContext, useRef} from 'react';
import axios from "axios";
import { API_URL } from '../../constants';
import AuthContext from '../../components/Context/AuthContext';

export default function Track(props) {
    let rating = props.rating;
    
    const {authToken} = useContext(AuthContext);
    // console.log(`${rating} ${props.trackname}`);
    const [likeActive, setLikeActive] = useState(rating != null && rating === true ? true : false); 
    const [dislikeActive, setDislikeActive] = useState(rating != null && rating === false ? true : false); 
    let i = props.tracknumber;
    let song = props.trackname;
    let albumId = props.albumId;

    const isFirstRenderLike = useRef(true);
    const isFirstRenderDislike = useRef(true);


    useEffect(() => {
        // console.log(rating);
        if (isFirstRenderLike.current) {
            isFirstRenderLike.current = false;
            return;
        }
        if (likeActive) {
            setDislikeActive(false)
        }
        axios.post(API_URL + "album-likes/" + albumId + "/", {
            song_name: song,
            liked: likeActive,
            disliked: dislikeActive,
        },{headers: {"Authorization": authToken}});
    }, [likeActive]);
    useEffect(() => {
        if (isFirstRenderDislike.current) {
            isFirstRenderDislike.current = false;
            return;
        }
        if (dislikeActive) {
            setLikeActive(false)
        }
        axios.post(API_URL + "album-likes/" + albumId + "/", {
            song_name: song,
            liked: likeActive,
            disliked: dislikeActive,
        },{headers: {"Authorization": authToken}});
    }, [dislikeActive]);
    return (
        <div className='tracklist'>
            <div className='track-like-dislike'>
                <button type='button' className={likeActive === true ? "like-button-active" : 'inactive-button'} onClick={()=>setLikeActive(!likeActive)}>
                    <span aria-hidden="true">&#9650;</span>
                </button> 
                <button type='button' className={dislikeActive === true ? "dislike-button-active" : 'inactive-button'} onClick={()=>setDislikeActive(!dislikeActive)}>
                    <span aria-hidden="true">&#9660;</span>
                </button> 
                {/* <div key={i} >&#9650;&#9660;</div> */}
            </div>
            <div className='tracklist-numbers'>
                <div style={{marginLeft:'auto'}} >{i+1}.</div>
            </div>
            <div className='track-names'>
                <div >{song}</div>
            </div>
        </div>
    );
}