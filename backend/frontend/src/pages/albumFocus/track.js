import './albumFocus.css';
import React, {useState, useEffect} from 'react';
import axios from "axios";

export default function Track(props) {
    const [likeActive, setLikeActive] = useState(false); 
    const [dislikeActive, setDislikeActive] = useState(false); 
    let myKey = props.myKey;
    let i = props.tracknumber;
    let song = props.trackname;

    const handleLike = () => {
        if (dislikeActive) {
            setLikeActive(true);
            setDislikeActive(false);
        }
        else {
            setLikeActive(!likeActive);
        }
    }

    const handleDislike = () => {
        if (likeActive) {
            setDislikeActive(true);
            setLikeActive(false);
        }
        else {
            setDislikeActive(!dislikeActive);
        }
        
    }

    return (
        <div className='tracklist'>
            <div className='track-like-dislike'>
                <button type='button' className={likeActive === true ? "like-button-active" : 'inactive-button'} onClick={handleLike}>
                    <span aria-hidden="true">&#9650;</span>
                </button> 
                <button type='button' className={dislikeActive === true ? "dislike-button-active" : 'inactive-button'} onClick={handleDislike}>
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