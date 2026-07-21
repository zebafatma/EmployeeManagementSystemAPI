from pydantic import BaseModel, EmailStr


class CreateEmployeeRequest(BaseModel):
    role: str
    name: str
    date_of_birth: str
    gender: str
    email: EmailStr
    phone_no: str
    address: str
    pan_number: str
    emergency_contact_name: str
    emergency_contact_phone: str
    department: str
    designation: str
    date_of_join: str
    manager_id: int
    salary: int
