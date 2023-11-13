import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './styles/create_rent.css';
import axios from 'axios';

export default function AddCar() {
    const [user] = useState(
        JSON.parse(window.localStorage.getItem('userData')) || {},
    );

    const [carAdd, setCarAdd] = useState('');

    const navigate = useNavigate();

    const CreateData = (crt) => {
        crt.preventDefault();
        const requestURL1 = `https://cloudservices-lab2-1-daf8e22e1d25.herokuapp.com/user/${user.username}`;
        const requestURL2 = 'https://cloudservices-lab2-1-daf8e22e1d25.herokuapp.com/car';
        const token = btoa(`${user.username}:${user.password}`);
        axios.get(requestURL1, {
            headers: {
                Authorization: `Basic ${token}`,
            },
        })
            .then((resp) => {
                const data = { ...carAdd };
                console.log(data)
                axios.post(requestURL2, data, {
                    headers: {
                        Authorization: `Basic ${token}`,
                    },
                })
                    .then(() => {
                        alert('Машину додано у список');
                        navigate('/home');
                    })
                    .catch((err) => {
                        alert("Не всі дані введені");
                    });
            });
    };

    return (
        <div>
            <div className="title">
                Adding a car
            </div>
            <div className="create-rent">
                <form className="form">
                    <br/>Mark of car<br/>
                    <input data-testid="car-id" type="user" name="" align="center" placeholder="Mark of car"
                    required onChange={(e) => setCarAdd((prev) => ({ ...prev, carMark: e.target.value }))}/>
                    <br/>Speed of car<br/>
                    <input data-testid="start-rent" type="text" name="" align="center" placeholder="Speed of car"
                    required onChange={(e) => setCarAdd((prev) => ({ ...prev, carSpeed: e.target.value }))}/>
                    <br/>Price per hour<br/>
                    <input data-tesid="end-rent" type="text" name="" align="center" placeholder="Price per hour"
                    required onChange={(e) => setCarAdd((prev) => ({ ...prev, carNumber: e.target.value }))}/>
                </form>
                <div className="buttons">
                    <br/><button className="btn" data-testid="create" type="sumbit" name="" value="Create" onClick={CreateData}>Create</button>
                </div>
            </div>
            <div class="home">
                <Link to="/home"><button className="btn">Home</button></Link>
            </div>
        </div>
    );
}