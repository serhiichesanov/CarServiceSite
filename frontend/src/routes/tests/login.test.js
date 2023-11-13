import { render, screen, fireEvent } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import Login from '../login';
import * as React from 'react';

test('Testing login username', () => {
    render(
        <BrowserRouter>
            <Login />
        </BrowserRouter>,
    );
    const inputUsername = screen.getByTestId('username');
    fireEvent.change(inputUsername, { target: { value: 'lordr3s' } });
    expect(inputUsername.value).toBe('lordr3s');
});

test('Testing login password', () => {
    render(
        <BrowserRouter>
            <Login />
        </BrowserRouter>,
    );
    const inputPassword = screen.getByTestId('password');
    fireEvent.change(inputPassword, { target: { value: 'qazwsx' } });
    expect(inputPassword.value).toBe('qazwsx');
});

test('Testing submit info', () => {
    render(
        <BrowserRouter>
            <Login />
        </BrowserRouter>,
    );
    const submit = screen.getByTestId('login');
    fireEvent.click(submit);
});