from datetime import date, datetime

from pydantic import BaseModel, EmailStr


class EmployeeResponse(BaseModel):
    id: int
    role: str
    name: str
    date_of_birth: date
    gender: str
    email: EmailStr
    phone_no: str
    address: str
    pan_number: str
    emergency_contact_name: str
    emergency_contact_phone: str
    department: str
    designation: str
    date_of_join: date
    manager_id: int
    salary: int
    currency: str
    is_active: bool
    created_by: int
    created_at: datetime
    updated_by: int
    updated_at: datetime
