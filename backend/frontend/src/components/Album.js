import React, {Component} from "react";

class Album extends React.Component {
    constructor(props){
        super(props);

        this.state = {
            title: "",
            artist: "",
            release_date: "",
            cover: "",
            likes: 0,
            dislikes: 0
        }

        render() {
            return (
              <div className="text-center">
                <img
                  src={this.state.cover}
                  className="img-thumbnail"
                  style={{}}
                />
                {/* CEDE CODE */}
                <b>
                    {this.state.title} <br />
                    {this.state.artist} <br />
                    {this.state.release_date} <br />
                </b>
              </div>
            );
        }
    }
}