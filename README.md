# Paytabs_Assesment1
Secure Transaction Web Application (POC)
Project Overview

The application consists of:
- A web user interface where the user enters PIN, amount, and transaction type
- System 1 which receives the transaction request
- System 2 which validates the PIN and transaction details
- Secure handling of PIN using hashing (no plaintext PIN is stored or logged)

Set of Events

1. User opens the web application
2. User enters PIN, amount, and transaction type
3. The request is sent to System 1 using a REST API
4. System 1 forwards the request to System 2
5. System 2 validates the PIN and transaction rules
6. A success or failure response is returned
7. The result is displayed on the UI

Technology Used

- Python
- Flask
- HTML
- CSS
- JavaScript

Project Structure

app.py
Main application entry point and API routing

system1.py
Handles transaction requests and forwards them for validation

system2.py
Validates PIN and transaction details

templates/index.html
Frontend UI for user interaction

static/style.css
Basic styling for the UI

requirements.txt
Python dependencies required to run the application

Test Credentials

PIN: 1234



This project fulfills the assessment requirement of demonstrating
a secure transaction system with a clear set of events and system separation.
