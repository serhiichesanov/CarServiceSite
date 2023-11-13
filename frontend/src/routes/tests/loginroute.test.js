import LoginRoute from '../loginroute';
import * as React from 'react';
import { BrowserRouter } from 'react-router-dom';
import {render} from '@testing-library/react'

test('Testing loginroute.js', () => {
    render(
        <BrowserRouter>
            <LoginRoute />
        </BrowserRouter>,
    );
});