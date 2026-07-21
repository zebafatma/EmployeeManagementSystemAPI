import logging

from data.database import SessionLocal
from employee.infrastructure.entities.employee_entity import Employee

logger = logging.getLogger(__name__)


class EmployeeRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_employee_by_id(self, id: int):
        return self.db.query(Employee).filter(Employee.id == id).first()

    def create(self, employee: Employee):
        try:
            self.db.add(employee)
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except:
            self.db.rollback()
            logger.exception("Database exception while creating employee")
            raise

    def get_employee_by_email(self, email: str):
        return self.db.query(Employee).filter(Employee.email == email).first()

    def update(self, employee: Employee):
        try:
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except:
            self.db.rollback()
            logger.exception("Database exception while updating employee")
            raise

    def delete(self, employee: Employee):
        try:
            self.db.delete(employee)
            self.db.commit()
        except:
            self.db.rollback()
            logger.exception("Database exception while deleting employee")
            raise

    def get_employees(
        self,
        offset: int,
        limit: int,
        name: str | None = None,
        department: str | None = None,
        role: str | None = None,
        is_active: bool | None = None,
        manager_id: int | None = None,
    ):
        query = self.db.query(Employee)
        if name:
            query = query.filter(Employee.name.ilike(f"%{name}%"))
        if department:
            query = query.filter(Employee.department == department)
        if role is not None:
            query = query.filter(Employee.role == role)
        if is_active is not None:
            query = query.filter(Employee.is_active == is_active)
        if manager_id is not None:
            query = query.filter(Employee.manager_id == manager_id)
        total_records = query.count()
        employees = query.offset(offset).limit(limit).all()
        return employees, total_records

    def close(self):
        self.db.close()
