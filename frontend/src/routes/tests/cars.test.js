import Cars from '../cars'
import * as React from 'react';
import { BrowserRouter } from 'react-router-dom';
import {render} from '@testing-library/react'

test('Testing cars.js', () => {
    render(
        <BrowserRouter>
            <Cars />
        </BrowserRouter>,
    );
});