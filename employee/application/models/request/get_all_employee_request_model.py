from pydantic import BaseModel


class GetAllEmployeeRequest(BaseModel):
    page: int = 1
    size: int = 10
    name: str | None = None
    department: str | None = None
    role: str | None = None
    is_active: bool | None = None
    manager_id: int | None = None
