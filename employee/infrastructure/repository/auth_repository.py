import logging
from datetime import datetime, timezone

from data.database import SessionLocal
from employee.infrastructure.entities.admin_credentials_entity import AdminCredentials

logger = logging.getLogger(__name__)


class AuthRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_admin_by_email(self, email: str):
        return (
            self.db.query(AdminCredentials)
            .filter(AdminCredentials.email == email)
            .first()
        )

    def create_admin(self, admin: AdminCredentials):
        db = SessionLocal()
        try:
            db.add(admin)
            db.commit()
            db.refresh(admin)
            return admin
        except:
            self.db.rollback()
            logger.exception("Database error while creating admin")
            raise

    def update_last_login(self, admin: AdminCredentials):
        try:
            if admin is None:
                return None
            admin.last_login = datetime.now(timezone.utc)
            self.db.commit()
            self.db.refresh(admin)
            return admin
        except:
            self.db.rollback()
            logger.exception("Database error while updating last login")
            raise

    def close(self):
        self.db.close()
