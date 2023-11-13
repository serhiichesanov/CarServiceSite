import Users from '../users'
import * as React from 'react';
import { BrowserRouter } from 'react-router-dom';
import {render} from '@testing-library/react'

test('Testing users.js', () => {
    render(
        <BrowserRouter>
            <Users />
        </BrowserRouter>,
    );
});