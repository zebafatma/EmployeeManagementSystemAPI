from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {
        "application": "Employee Management System API",
        "status": "Running",
        "documentation": "/docs",
    }
