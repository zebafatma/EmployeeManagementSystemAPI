import logging
from datetime import date

from data.database import SessionLocal
from employee.infrastructure.entities.employee_entity import Employee

logger = logging.getLogger(__name__)


def seed_admin():
    db = SessionLocal()

    try:
        existing_admin = db.query(Employee).filter(Employee.role == "admin").first()

        if existing_admin:
            logger.info("Seed skipped. Admin employee already exists.")
            return

        employee = Employee(
            role="admin",
            name="Super Admin",
            date_of_birth=date(2000, 5, 15),
            email="admin@gmail.com",
            phone_no="64598734213",
            address="Bengaluru",
            pan_number="NFOV7643A",
            emergency_contact_name="Abc",
            emergency_contact_phone="7645287460",
            department="HR",
            designation="CEO",
            date_of_join=date(2023, 4, 18),
            manager_id=1,
            salary=1000000,
            created_by=1,
            updated_by=1,
            currency="INR",
        )

        db.add(employee)
        db.commit()
        db.refresh(employee)

        logger.info(
            "Admin employee seeded successfully. Use the credentials for Signup- Employee ID: %s, Email Id: %s",
            employee.id,
            employee.email,
        )

    except Exception:
        db.rollback()
        logger.exception("Failed to seed admin employee.")
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_admin()
