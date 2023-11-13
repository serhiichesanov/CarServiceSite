import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './styles/create_rent.css';
import axios from 'axios';
import moment from 'moment';

export default function CreateRent() {
    const [user] = useState(
        JSON.parse(window.localStorage.getItem('userData')) || {},
    );

    const [rentCreate, setRentCreate] = useState('');

    const navigate = useNavigate();

    const CreateData = (crt) => {
        crt.preventDefault();
        const requestURL1 = `https://cloudservices-lab2-1-daf8e22e1d25.herokuapp.com/user/${user.username}`;
        const requestURL2 = 'https://cloudservices-lab2-1-daf8e22e1d25.herokuapp.com/rent';
        const token = btoa(`${user.username}:${user.password}`);
        axios.get(requestURL1, {
            headers: {
                Authorization: `Basic ${token}`,
            },
        })
            .then((resp) => {
                const data = { ...rentCreate, userId: resp.data.id};
                console.log(data)
                axios.post(requestURL2, data, {
                    headers: {
                        Authorization: `Basic ${token}`,
                    },
                })
                    .then(() => {
                        alert('Замовлення створено');
                        navigate('/home');
                    })
                    .catch((err) => {
                        if(rentCreate.carId == undefined || rentCreate.startRent == undefined ||
                            rentCreate.endRent == undefined){
                           alert("Не всі дані введені");
                       }
                       else{
                           alert(err.response.data)
                       }
                        
                    });
            });
    };

    return (
        <div>
            <div className="title">
                Creating rent
            </div>
            <div className="create-rent">
                <form className="form">
                    <br/>Car ID<br/>
                    <input data-testid="car-id" type="user" name="" align="center" placeholder="car ID"
                    required onChange={(e) => setRentCreate((prev) => ({ ...prev, carId: e.target.value }))}/>
                    <br/>Starts at<br/>
                    <input data-testid="start-rent" type="text" name="" align="center" placeholder="Start of rent"
                    required onChange={(e) => setRentCreate((prev) => ({ ...prev, startRent: e.target.value }))}/>
                    <br/>Ends at<br/>
                    <input data-tesid="end-rent" type="text" name="" align="center" placeholder="End of rent"
                    required onChange={(e) => setRentCreate((prev) => ({ ...prev, endRent: e.target.value }))}/>
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