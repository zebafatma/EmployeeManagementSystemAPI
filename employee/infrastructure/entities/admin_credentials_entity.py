from datetime import datetime, timezone

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from data.database import Base


class AdminCredentials(Base):
    __tablename__ = "admin_credentials"
    credential_id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, index=True
    )
    id: Mapped[int] = mapped_column(ForeignKey("employees.id"), nullable=False)
    email: Mapped[str] = mapped_column(
        String(100), unique=True, index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    last_login: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(timezone.utc), nullable=False
    )
