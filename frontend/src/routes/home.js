import React, {useState} from "react";
import { Link, useNavigate } from "react-router-dom";
import './styles/home.css'

export default function Home() {
    const [user, setUser] = useState(
        JSON.parse(window.localStorage.getItem('userData')) || {},
    );
    const navigate = useNavigate();
    const checkData = () =>{
        if(user.username != "admin"){
            alert("Дану операцію можуть виконувати лише адміни")
        }
        else{
            navigate('/users');
        }
    }
    return (
        <div>
            <div className="title">
                Renting car site
            </div>
            <div className="centered-home">
                <Link to="/cars">
                    <button className="btn-home">Cars list</button>
                </Link>
                <Link to="/rent">
                    <button className="btn-home">Create new rent</button>
                </Link>
                <Link to="/rents">
                    <button className="btn-home">Watch rents</button>
                </Link>
                <button className="btn-home" onClick={checkData}>Watch users</button>
            </div>
            <Link to="/login">
                <div>
                    <button className="btn-home signup-home">Sign in</button>
                </div>
                </Link>
        </div>
    );
}