from pydantic import BaseModel, EmailStr


class PatchEmployeeRequest(BaseModel):
    role: str | None = None
    name: str | None = None
    date_of_birth: str | None = None
    gender: str | None = None
    email: EmailStr | None = None
    phone_no: str | None = None
    address: str | None = None
    pan_number: str | None = None
    emergency_contact_name: str | None = None
    emergency_contact_phone: str | None = None
    department: str | None = None
    designation: str | None = None
    date_of_join: str | None = None
    manager_id: int | None = None
    salary: int | None = None
    currency: str | None = None
    is_active: bool | None = None
