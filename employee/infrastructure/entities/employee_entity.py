from datetime import date, datetime, timezone

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from data.database import Base


class Employee(Base):
    __tablename__ = "employees"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    role: Mapped[str] = mapped_column(default="employee", nullable=False)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    date_of_birth: Mapped[date] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(
        String(15), default="Not Specified", nullable=False
    )

    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    phone_no: Mapped[str] = mapped_column(String(20), nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    pan_number: Mapped[str] = mapped_column(String(50), nullable=False)
    emergency_contact_name: Mapped[str] = mapped_column(String(50), nullable=False)
    emergency_contact_phone: Mapped[str] = mapped_column(String(20), nullable=False)

    department: Mapped[str] = mapped_column(String(50), nullable=False)
    designation: Mapped[str] = mapped_column(String(50), nullable=False)
    date_of_join: Mapped[date] = mapped_column(nullable=False)
    manager_id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    salary: Mapped[int] = mapped_column(nullable=False)
    currency: Mapped[str] = mapped_column(String(3), nullable=False, default="INR")

    created_by: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_by: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
