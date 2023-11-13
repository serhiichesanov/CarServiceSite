import React, {useState} from "react";
import { Link, useNavigate } from "react-router-dom";
import './styles/registration.css'
import axios from 'axios';

export default function Registration() {
    const [userReg, setUserReg] = useState('');
    const navigate = useNavigate();
    const handleSubmit = (reg) => {
        reg.preventDefault();
        const requestURL = 'http://localhost:5000/user';
            const data = { ...userReg };

            axios.post(requestURL, data)
                .then(() => {
                    alert('Реєстрацію здійснено');
                    navigate('/home');
                })
                .catch((err) => {
                    if(userReg.username == undefined || userReg.password == undefined
                       || userReg.username == undefined || userReg.password == undefined
                       || userReg.username == undefined || userReg.password == undefined){
                        alert("Не всі дані введені")
                       }
                    else{
                        //alert(JSON.stringify(userReg, null, 2))
                        console.log(err.name)
                        console.log(err.message)
                    }
                });
    };

    return (
        <div>
            <div className="title1">
            Registration
            </div>
            <div className="registration">
                <form className="form">
                    <br/>username<br/>
                    <input data-testid="username" type="user" name="" align="center" placeholder="username"
                    required onChange={(e) => setUserReg((prev) => ({ ...prev, username: e.target.value}))}/>
                    <br/>Password<br/>
                    <input data-testid="password" type="text" name="" align="center" placeholder="password"
                    required onChange={(e) => setUserReg((prev) => ({ ...prev, password: e.target.value}))}/>
                    <br/>First name<br/>
                    <input data-testid="firstName" type="text" name="" align="center" placeholder="first name"
                    required onChange={(e) => setUserReg((prev) => ({ ...prev, firstName: e.target.value}))}/>
                    <br/>Last name<br/>
                    <input data-testid="lastName" type="text" name="" align="center" placeholder="last name"
                    required onChange={(e) => setUserReg((prev) => ({ ...prev, lastName: e.target.value}))}/>
                    <br/>Email<br/>
                    <input data-testid="email" type="text" name="" align="center" placeholder="email"
                    required onChange={(e) => setUserReg((prev) => ({ ...prev, email: e.target.value}))}/>
                    <br/>Phone<br/>
                    <input data-tesid="phone" type="text" name="" align="center" placeholder="phone"
                    required onChange={(e) => setUserReg((prev) => ({ ...prev, phone: e.target.value}))}/>
                </form>
                <div className="buttons-regestration">
                    <Link to="/login"><br/><button class="btn-registration">Log in</button></Link>
                    <button className="btn-registration" data-testid="registration" type="submit" name="" value="Register" onClick={handleSubmit}><i>Registration</i></button>
                </div>
            </div>
            <div class="home-registration">
                <Link to="/home"><button className="btn">Home</button></Link>
            </div>
        </div>
    );
}