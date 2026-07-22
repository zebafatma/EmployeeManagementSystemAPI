# Employee Management System

A backend application built using **FastAPI** that provides secure employee management with authentication, role-based authorization, and CRUD operations. The application follows a layered architecture using repositories and services, supports Docker deployment, and uses SQLite as the database.

---

## Features

- JWT Authentication
- Secure Password Hashing (bcrypt)
- Employee CRUD Operations
- Partial Updates (PATCH)
- Pagination & Filtering
- Role-Based Access Control
- Repository-Service Architecture
- Structured JSON Logging
- Automatic Initial Admin Seeding
- Docker Support
- Environment Variable Configuration

---

## Tech Stack

- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT (python-jose)
- Passlib (bcrypt)
- Docker
- Python JSON Logger

---

## Project Structure

```
.
├── auth/
├── common/
├── data/
├── employee/
├── Dockerfile
├── seed.py
├── main.py
├── requirements.txt
├── .dockerignore
└── README.md
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=sqlite:///./employee.db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd <project-folder>
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
uvicorn main:app --reload
```

Swagger UI:

```
http://localhost:8000/docs
```

---

## Docker

### Build the Docker image

```bash
docker build -t app .
```

### Run the Docker container

```bash
docker run \
  --name employee-management-app \
  --env-file .env \
  -p 8000:8000 \
  app
```

---

## Initial Admin

On application startup, the system automatically checks whether an administrator exists.

- If no administrator exists, a default admin employee is created.
- If an administrator already exists, the seed process is skipped.

This initialization is idempotent and runs only when required.

---

## Authentication Flow

1. An employee with the **Admin** role is seeded into the Employee table.
2. The seeded admin signs up using their employee details.
3. Credentials are stored securely with hashed passwords.
4. The admin signs in to receive a JWT access token.
5. The JWT token is used to access protected APIs.

---

## Logging

The application uses structured JSON logging for:

- Application startup
- Employee seeding
- API events
- Errors and exceptions

---

## API Documentation

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

## Security

- JWT Authentication
- Password Hashing using bcrypt
- Environment-based configuration
- Role-Based Authorization

---

## Author

**Zeba Fatma**