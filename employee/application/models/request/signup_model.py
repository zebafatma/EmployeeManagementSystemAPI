from pydantic import BaseModel, EmailStr


class SignupRequest(BaseModel):
    id: int
    email: EmailStr
    name: str
    password: str
