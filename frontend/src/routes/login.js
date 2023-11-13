import React, {useState} from "react";
import { Link, useNavigate } from "react-router-dom";
import './styles/login.css'
import axios from "axios";

export default function Login() {
    const [userLog, setUserLog] = useState(
        JSON.parse(window.localStorage.getItem('userData')) || '',
    );
    const navigate = useNavigate();
    const handleSubmit = (reg) => {
        reg.preventDefault();
        const requestURL = 'https://cloudservices-lab2-1-daf8e22e1d25.herokuapp.com/login';
        axios.post(requestURL, userLog)
            .then((res) => {
                window.localStorage.setItem('userData', res.config.data);
                alert('Ви увійшли в акаунт');
                navigate('/home');
            })
            .catch((err) => {
                if(userLog.username == undefined || userLog.password == undefined){
                    alert("Не всі дані введені")
                }
                else{
                    alert("Такого користувача не існує")
                }
            });
    };

    return (
        <div>
            <div className="title">
                 Login
            </div>
            <div className="login">
            <form className="form">
                <br/>Username<br/>
                <input data-testid="username" name="username" type="text" align="center" placeholder="username"
                        required onChange={(e) => setUserLog((prev) => ({ ...prev, username: e.target.value}))}/>
                <br/>Password<br/>
                <input  data-testid="password" name="password" type="text" align="center" placeholder="password"
                        required onChange={(e) => setUserLog((prev) => ({ ...prev, password: e.target.value}))}/>
            </form>
            <div className="buttons-login">
                <br/><button className="btn btn-login" data-testid="login" type="submit" name="login" value="login" onClick={handleSubmit}><i>Log in</i></button>
                <Link to="/registration"><button className="btn">Registration</button></Link>
            </div>
        </div>
            <div class="home-login">
                <Link to="/home"><button className="btn">Home</button></Link>
            </div>
        </div>
    );
}