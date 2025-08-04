FastAPI User Management API
A simple REST API built using FastAPI for managing users (Create, Read, Update, Delete).
This project is designed as a beginner-friendly task suitable for practice.

Features
Create User – Add a new user with name and email.

Get All Users – Fetch a list of all users.

Get User by ID – Retrieve user details by ID.

Update User – Modify existing user data.

Delete User – Remove a user by ID.

Data Storage – Simple JSON file for persistence.

Project Structure

fastapi-user-api/
│
├── app/
│   ├── main.py               # FastAPI application entry point
│   ├── models.py             # Pydantic models
│   ├── routers/
│   │   └── users.py          # User routes (CRUD)
│   ├── services/
│   │   └── user_service.py   # Business logic and file handling
│   └── data/
│       └── users.json        # JSON file to store users
└── requirements.txt          # Project dependencies
Installation
Clone the repository

bash


git clone https://github.com/your-username/fastapi-user-api.git
cd fastapi-user-api
Install dependencies


pip install fastapi uvicorn
Run the server

uvicorn app.main:app --reload
