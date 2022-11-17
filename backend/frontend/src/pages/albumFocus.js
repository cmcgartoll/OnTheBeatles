import React, {useState, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import axios from "axios";
import { API_URL } from "../constants/index.js";
  
export default function AlbumFocus() {
    let {albumId} = useParams();
    const [album, setAlbum] = useState({});
    useEffect(() => {
        axios.get(API_URL + "album/" + albumId + "/").then((res) => setAlbum(res.data));
    });
     
    return (
        <>
            <body>{album.title}</body>
        </>
    );
};