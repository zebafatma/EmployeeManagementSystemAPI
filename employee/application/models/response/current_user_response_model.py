from datetime import datetime

from pydantic import BaseModel, EmailStr


class CurrentUserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_active: bool
    last_login: datetime

    class Config:
        from_attributes = True
