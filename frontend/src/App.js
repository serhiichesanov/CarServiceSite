import { BrowserRouter, Route, Routes } from 'react-router-dom';
import React from 'react';
import Home from './routes/home'
import Login from './routes/login';
import Registration from './routes/registration';
import Profile from './routes/profile';
import User from './routes/user';
import LoginRoute from './routes/loginroute';
import Users from './routes/users';
import Cars from './routes/cars';
import Rents from './routes/rent';
import AddCar from './routes/add_car';
import DeleteCar from './routes/delete_car';
import CreateRent from './routes/create_rent';

function App(){
    return(
        <div>
            <BrowserRouter>
                <Profile></Profile>
                <Routes>
                    <Route path="/login" element={<Login />} />
                    <Route path="/home" element={<Home />} />
                    <Route path="/registration" element={<Registration />} />
                    <Route path="/user" element={<LoginRoute component={User} />}/>
                    <Route path="/rent" element={<LoginRoute component={CreateRent} />}/>
                    <Route path="/users" element={<Users />}/>
                    <Route path="/cars" element={<Cars />}/>
                    <Route path="/rents" element={<Rents />}/>
                    <Route path="/addcar" element={<AddCar/>}/>
                    <Route path="/deletecar" element={<DeleteCar/>}/>
                </Routes>
            </BrowserRouter>
        </div>
    );    
}

export default App;