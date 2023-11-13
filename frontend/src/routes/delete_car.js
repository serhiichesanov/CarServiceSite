import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './styles/create_rent.css';
import './styles/delete_car.css';
import axios from 'axios';

export default function DeleteCar() {
    const [car, setCar] = useState([]);

    const [user, setUser] = useState(
        JSON.parse(window.localStorage.getItem('userData')) || {},
    );
    const navigate = useNavigate();
    const deleteData = (del) => {
        del.preventDefault();
        const requestURL = `https://cloudservices-lab2-1-daf8e22e1d25.herokuapp.com/car/${car.id}`;
        const token = btoa(`${user.username}:${user.password}`);
        axios.delete(requestURL, {
            headers: {
                Authorization: `Basic ${token}`,
            },
        })
            .then(() => {
                alert('Машина видалена');
                navigate('/cars');
            })
            .catch((err) => {
                if(car.id == undefined){
                    alert("ID машини не будо введено");
                }
                else if(typeof car.id != "number"){
                    alert("ID було введено не коректно");
                }
                else{
                    alert("Даної машини не існує");
                }
            });
    };

    return (
        <div>
            <div className="title">
                Deleting a car
            </div>
            <div className="create-rent del-car">
                <form className="form">
                    <br/>ID of car<br/>
                    <input data-testid="car-id" type="user" name="" align="center" placeholder="ID of car:"
                    required onChange={(e) => setCar((prev) => ({ ...prev, id: e.target.value }))}/>
                </form>
                <div className="buttons buttons-del">
                    <br/><button className="btn" data-testid="create" type="sumbit" name="" value="Create" onClick={deleteData}>Delete</button>
                </div>
            </div>
            <div class="home">
                <Link to="/home"><button className="btn">Home</button></Link>
            </div>
        </div>
    );
}