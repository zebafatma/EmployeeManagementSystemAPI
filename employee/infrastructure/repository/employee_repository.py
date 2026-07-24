import logging

from data.database import SessionLocal
from employee.infrastructure.entities.employee_entity import Employee

logger = logging.getLogger(__name__)


class EmployeeRepository:
    def __init__(self):
        logger.info("Starting Database Session for Employee")
        self.db = SessionLocal()

    def get_employee_by_id(self, id: int):
        logger.info("Repository method: 'get_employee_by_id' called")
        return self.db.query(Employee).filter(Employee.id == id).first()

    def create(self, employee: Employee):
        logger.info("Repository method 'create' called")
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
        logger.info("Repository method 'get_employee_by_email' called")
        return self.db.query(Employee).filter(Employee.email == email).first()

    def update(self, employee: Employee):
        logger.info("Repository method 'update' called")
        try:
            self.db.commit()
            self.db.refresh(employee)
            return employee
        except:
            self.db.rollback()
            logger.exception("Database exception while updating employee")
            raise

    def delete(self, employee: Employee):
        logger.info("Repository method 'delete' called")
        try:
            self.db.delete(employee)
            self.db.commit()
        except:
            self.db.rollback()
            logger.exception("Database exception while deleting employee")
            raise

    def get_employees(self, offset: int, request):
        logger.info("Repository method 'get_employees' called")
        query = self.db.query(Employee)
        if request.name:
            query = query.filter(Employee.name.ilike(f"%{request.name}%"))
        if request.department:
            query = query.filter(Employee.department == request.department)
        if request.role is not None:
            query = query.filter(Employee.role == request.role)
        if request.is_active is not None:
            query = query.filter(Employee.is_active == request.is_active)
        if request.manager_id is not None:
            query = query.filter(Employee.manager_id == request.manager_id)
        total_records = query.count()
        employees = query.offset(offset).limit(request.size).all()
        return employees, total_records

    def close(self):
        logger.info("Closing Database Session for Employee")
        self.db.close()
