import React, { useState, useEffect } from 'react';
import './styles/users.css';
import { Link } from "react-router-dom";
import axios from 'axios';

export default function Users() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        const requestURL = 'https://cloudservices-lab2-1-daf8e22e1d25.herokuapp.com/user';
        axios.get(requestURL)
            .then((data) => {
                setUsers(data.data);
            });
    }, []);

    return(
        <div>
            <div class="title">
                Users
            </div>
            <table class="table">
        <thead>
            <tr>
                <th>user ID</th>
                <th>username</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>email</th>
                <th>phone</th>
            </tr>
        </thead>
        <tbody>
        {
                            users.map((user) => (
                                <tr key={user.id}>
                                    <td>{user.id}</td>
                                    <td>{user.username}</td>
                                    <td>{user.firstName}</td>
                                    <td>{user.lastName}</td>
                                    <td>{user.email}</td>
                                    <td>{user.phone}</td>
                                </tr>
                            ))
                        }
        </tbody>
    </table>
    <div class="home">
        <Link to="/home"><button class="btn">Home</button></Link>
    </div>
        </div>
    )
}
