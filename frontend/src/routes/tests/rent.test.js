import Rent from '../rent'
import * as React from 'react';
import { BrowserRouter } from 'react-router-dom';
import {render} from '@testing-library/react'

test('Testing rent.js', () => {
    render(
        <BrowserRouter>
            <Rent />
        </BrowserRouter>,
    );
});