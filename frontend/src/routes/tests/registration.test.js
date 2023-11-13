import { render, screen, fireEvent } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import Registration from '../registration';
import * as React from 'react'

test('Testing registration username', () => {
    render(
        <BrowserRouter>
            <Registration />
        </BrowserRouter>,
    );
    const inputUsername = screen.getByTestId('username');
    fireEvent.change(inputUsername, { target: { value: 'lordr3s' } });
    expect(inputUsername.value).toBe('lordr3s');
});

test('Testing registration first name', () => {
    render(
        <BrowserRouter>
            <Registration />
        </BrowserRouter>,
    );
    const inputFName = screen.getByTestId('firstName');
    fireEvent.change(inputFName, { target: { value: 'Serhii' } });
    expect(inputFName.value).toBe('Serhii');
});

test('Testing registration last name', () => {
    render(
        <BrowserRouter>
            <Registration />
        </BrowserRouter>,
    );
    const inputLName = screen.getByTestId('lastName');
    fireEvent.change(inputLName, { target: { value: 'Chesanov' } });
    expect(inputLName.value).toBe('Chesanov');
});

test('Testing registration email', () => {
    render(
        <BrowserRouter>
            <Registration />
        </BrowserRouter>,
    );
    const inputEmail = screen.getByTestId('email');
    fireEvent.change(inputEmail, { target: { value: 'serhii.chesanov@gmail.com' } });
    expect(inputEmail.value).toBe('serhii.chesanov@gmail.com');
});

test('Testing registration password', () => {
    render(
        <BrowserRouter>
            <Registration />
        </BrowserRouter>,
    );
    const inputPassword = screen.getByTestId('password');
    fireEvent.change(inputPassword, { target: { value: 'qazwsx' } });
    expect(inputPassword.value).toBe('qazwsx');
});

test('Testing submit info', () => {
    render(
        <BrowserRouter>
            <Registration />
        </BrowserRouter>,
    );
    const submit = screen.getByTestId('registration');
    fireEvent.click(submit);
});