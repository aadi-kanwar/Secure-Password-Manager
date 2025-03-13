# Secure Password Manager

A Secure Password Manager built using Flask, React.js, PostgreSQL, and AES-256 encryption to ensure safe and efficient password storage.

## Features

1. User Login & Session Management: Secure authentication and session handling.

2. AES-256 Encryption: Encrypts stored passwords for maximum security.

3. Edit/Delete Stored Passwords: Users can modify or remove saved credentials.

4. UI Enhancements: A responsive and user-friendly interface.

## Tech Stack

> Frontend: React.js  
> Backend: Flask  
> Database: PostgreSQL  
> Encryption: AES-256


## Installation
### Pre-requisites
- Python (>=3.8)
- Node.js (>=16)
- PostgreSQL (>=14)

### Backend Setup (Flask)
`cd backend`  
`python db_init.py`  # Run once to initialize DB  
`python app.py`

### Frontend Setup (React.js)
`cd frontend`  
`npm start`

## Usage
- Register an account or log in.
- Add, edit, or delete passwords securely.
- All passwords are encrypted before being stored in the database.

## Security Measures
- Uses AES-256 encryption for storing passwords.
- Passwords are never stored in plaintext.
- Secure authentication mechanisms to prevent unauthorized access.

## Roadmap / Future Enhancements
- Two-Factor Authentication (2FA)
- Password Strength Analyzer
- Password Autofill Extension