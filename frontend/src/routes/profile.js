import React, { Component } from 'react';
import { Link } from 'react-router-dom';

export default class Profile extends Component{
    render(){
        return(
            <div>
                <Link to="/user">
                    <div className="profile">
                        <i>Profile</i>
                        <img src="pictures/profile.jfif" alt="" width="40"/>
                    </div>
                </Link>
            </div>
        )
    }
}