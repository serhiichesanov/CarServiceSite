import Home from "../home";
import * as React from 'react';
import { BrowserRouter } from 'react-router-dom';
import {render} from '@testing-library/react'

test('Testing home.js', () => {
    render(
        <BrowserRouter>
            <Home />
        </BrowserRouter>,
    );
});