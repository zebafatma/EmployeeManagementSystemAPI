# Employee Management System API

A backend application built using **FastAPI** that provides secure employee management with authentication, role-based authorization, and employee CRUD operations. The application follows a layered architecture using repositories and services, supports Docker deployment, and uses SQLite as the database.

---

## Live Deployment

**Base URL**

```
https://employeemanagementsystemapi-ij2t.onrender.com
```

**Swagger UI**

```
https://employeemanagementsystemapi-ij2t.onrender.com/docs
```

**ReDoc**

```
https://employeemanagementsystemapi-ij2t.onrender.com/redoc
```

---

## Features

- JWT Authentication
- Role-Based Authorization
- Secure Password Hashing (bcrypt)
- Employee CRUD Operations
- Partial Updates (PATCH)
- Pagination & Filtering
- Repository-Service Architecture
- Structured JSON Logging
- Automatic Initial Admin Seeding
- Dockerized Deployment
- Environment Variable Configuration

---

## Tech Stack

- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- python-jose (JWT)
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

## Architecture

The application follows a layered architecture:

```
Client
   │
   ▼
FastAPI Endpoints
   │
   ▼
Services
   │
   ▼
Repositories
   │
   ▼
SQLite Database
```

- **Endpoints** handle HTTP requests and responses.
- **Services** contain business logic.
- **Repositories** interact with the database.
- **JWT Authentication** secures protected APIs.

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
git clone https://github.com/zebafatma/EmployeeManagementSystemAPI.git
cd EmployeeManagementSystemAPI
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

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

Swagger:

```
http://localhost:8000/docs
```

---

## Running with Docker

### Build the image

```bash
docker build -t employee-management-api .
```

### Run the container

```bash
docker run \
  --name employee-management-app \
  --env-file .env \
  -p 8000:8000 \
  employee-management-api
```

---

## Initial Admin

On application startup, the system checks whether an administrator exists.

- If no administrator exists, a default administrator employee is seeded.
- The seeded employee can complete signup using the following details:

| Field | Value |
|-------|------|
| Employee ID | 1 |
| Email | admin@gmail.com |

After signing up, the administrator can sign in and receive a JWT access token.

The seeding process is **idempotent**, meaning it runs only when no administrator exists.

---

## Authentication Flow

1. A default administrator employee is seeded during application startup.
2. The administrator completes signup using the seeded employee details.
3. Passwords are securely hashed using bcrypt.
4. The administrator signs in to receive a JWT access token.
5. The JWT token is supplied in the `Authorization` header to access protected endpoints.

---

## Logging

Structured JSON logging is implemented for:

- Application startup
- Admin seeding
- API requests
- Error handling
- Exception logging

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

For the deployed application:

```
https://employeemanagementsystemapi-ij2t.onrender.com/docs
```

---

## Security

- JWT Authentication
- Password Hashing using bcrypt
- Environment-based configuration
- Role-Based Authorization

---

## Future Improvements

- Add automated tests using pytest
- Refactor database session management using FastAPI dependency injection
- Migrate from SQLite to PostgreSQL
- Add Alembic database migrations
- Implement GitHub Actions CI/CD
- Add Docker Compose support

---

## Author

**Zeba Fatma**