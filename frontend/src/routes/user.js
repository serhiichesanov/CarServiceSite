import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './styles/user.css';
import axios from 'axios';
import icon from './styles/pictures/profile.jfif'

export default function User(){
    const [user, setUser] = useState(
        JSON.parse(window.localStorage.getItem('userData')) || {},
    );
    
    const [userInfo, setUserInfo] = useState({
        username: undefined,
        firsName: undefined,
        lastName: undefined,
        email: undefined,
        password: undefined,
        phone: undefined
    });

    useEffect(() => {
        const requestURL = `https://cloudservices-lab2-1-daf8e22e1d25.herokuapp.com/user/${user.username}`;
        axios.get(requestURL)
            .then((data) => {
                setUserInfo(data.data);
            });
    }, []);


    const [oldUser, setOldUser] = useState(
        { oldPassword: user.password, oldUsername: user.username } || '',
    );

    const navigate = useNavigate();
    
    const saveData = (e) => {
        e.preventDefault();
        const requestURL = `http://localhost:8000/user/${user.username}`;
        const token = btoa(`${user.username}:${user.password}`);
        axios.put(requestURL, user, {
            headers: {
                Authorization: `Basic ${token}`,
            },
        })
            .then(() => {
                setOldUser({ oldPassword: user.password, oldUsername: user.username });
                alert('Дані оновлено');
            })
            .catch((err) => {
                alert(err.response.data);
            });
    };

    const logout = (out) => {
        out.preventDefault();
        setUser({
            username: undefined,
            firsName: undefined,
            lastName: undefined,
            email: undefined,
            password: undefined,
            phone: undefined,
        });
        alert('Ви вийшли з акаунту');
        window.localStorage.clear();
        navigate('/login');
    };

    const deleteData = (del) => {
        del.preventDefault();
        setUser({
            username: undefined,
            firstName: undefined,
            lastName: undefined,
            email: undefined,
            password: undefined,
            phone: undefined,
        });
        const requestURL = `http://localhost:8000/user/${oldUser.oldUsername}`;
        const token = btoa(`${oldUser.oldUsername}:${oldUser.oldPassword}`);
        axios.delete(requestURL, {
            headers: {
                Authorization: `Basic ${token}`,
            },
        })
            .then(() => {
                setOldUser({ oldPassword: undefined, oldUsername: undefined });
                alert('Користучач був видалений');
                window.localStorage.clear();
            })
            .catch((err) => {
                alert(err.response.data);
            });
        navigate('/login');
    };

    return(
        <div>
          <div class="profile-user">
                <div class="left">
                    <div class="info">
                        <div class="photo-user">
                            <img alt="" className="img-user" src={require('./styles/pictures/profile.jfif')}/>
                        </div>
                    </div>  
                    <div class="buttons-user">
                        <button class="btn-user" type="submit" data-testid="edit" name="" value="Edit" onClick={saveData}>Edit</button>
                        <button class="btn-user" type="submit" data-testid="logout" name="" value="Log out" onClick={logout}>Logout</button>
                        <button class="btn-user" type="submit" data-testid="delete" name="" value="Delete" onClick={deleteData}>Delete</button>
                    </div>
                </div>
                <div class="right">
                    <div class="input-group-user">
                        username<br/>
                        <input class="input-user" data-testid="username-input" name="" type="text" defaultValue={user.username} align="center" placeholder="username" readOnly/>
                        <br/>Password<br/>
                        <input class="input-user" data-testid="password-input" name="" type="text" defaultValue={user.password} align="center" placeholder="password"
                        onChange={(e) => setUser((prev) => ({ ...prev, password: e.target.value }))}/>
                        <br/>Email<br/>
                        <input class="input-user" data-testid="email-input" name="" type="text" defaultValue={userInfo.email} align="center" placeholder="email"
                        onChange={(e) => setUser((prev) => ({ ...prev, email: e.target.value }))}/>
                    </div>
                    <div class="input-group-user">
                        First name<br/>
                        <input class="input-user" data-testid="firstName-input" name="" type="text" defaultValue={userInfo.firstName} align="center" placeholder="first name"
                        onChange={(e) => setUser((prev) => ({ ...prev, firstName: e.target.value }))}/>
                        <br/>Last name<br/>
                        <input class="input-user" data-testid="lastName-input" name="" type="text" defaultValue={userInfo.lastName} align="center" placeholder="last name"
                        onChange={(e) => setUser((prev) => ({ ...prev, lastName: e.target.value }))}/>
                        <br/>Phone<br/>
                        <input class="input-user" data-testid="phone-input" name="" type="text" defaultValue={userInfo.phone} align="center" placeholder="phone"
                        onChange={(e) => setUser((prev) => ({ ...prev, phone: e.target.value }))}/>
                    </div>   
                </div>
            </div>
            <div class="home">
                <Link to="/home"><button class="btn">Home</button></Link>
            </div>
        </div>
    )
}