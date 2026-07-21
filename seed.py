from datetime import date

from data.database import SessionLocal
from employee.infrastructure.entities.employee_entity import Employee

db = SessionLocal()
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
    date_of_join=date(2003, 4, 18),
    manager_id=1,
    salary=1000000,
    created_by=1,
    updated_by=1,
)

db.add(employee)
db.commit()
db.refresh(employee)
db.close()
