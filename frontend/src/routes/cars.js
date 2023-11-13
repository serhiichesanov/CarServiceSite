import React, { useState, useEffect } from 'react';
import './styles/car.css';
import { Link, useNavigate } from "react-router-dom";
import axios from 'axios';

export default function Cars() {
    const [cars, setCars] = useState([]);

    const [user, setUser] = useState(
        JSON.parse(window.localStorage.getItem('userData')) || {},
    );

    const navigate = useNavigate();
    useEffect(() => {
        const requestURL = 'https://cloudservices-lab2-1-daf8e22e1d25.herokuapp.com/car';
        axios.get(requestURL)
            .then((data) => {
                setCars(data.data);
            });
    }, []);

    const checkUserAdd = () =>{
        if(user.username != "admin"){
            alert("Дану операцію можуть виконувати лише адміни")
            
        }
        else{
            navigate('/addcar');
        }
    }

    const checkUserDelete = () =>{
        if(user.username != "admin"){
            alert("Дану операцію можуть виконувати лише адміни")
            
        }
        else{
            navigate('/deletecar');
        }
    }

    return(
        <div>
            <div class="title">
                Cars
            </div>
            <table class="table">
        <thead>
            <tr>
                <th>car ID</th>
                <th>car mark</th>
                <th>car speed</th>
                <th>price per day($)</th>
            </tr>
        </thead>
        <tbody>
        {
                            cars.map((car) => (
                                <tr key={car.id}>
                                    <td>{car.id}</td>
                                    <td>{car.carMark}</td>
                                    <td>{car.carSpeed}</td>
                                    <td>{car.carNumber}</td>
                                </tr>
                            ))
                        }
        </tbody>
    </table>
    <div class="buttons-car">
        <button class="btn" onClick={checkUserAdd}>Add car</button>
        <button class="btn" onClick={checkUserDelete}>Delete car</button>
    </div>
    <div class="home home-car">
        <Link to="/home"><button class="btn">Home</button></Link>
    </div>
        </div>
    )
}
