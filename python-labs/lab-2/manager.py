from employee import Employee
from database import Database


class Manager(Employee):

    def __init__(
            self,
            first_name,
            last_name,
            age,
            department,
            salary,
            managed_department):

        self.managed_department = managed_department

        super().__init__(
            first_name,
            last_name,
            age,
            department,
            salary
        )

        Database.delete_employee(self.id)

        self.id = Database.insert_employee(
            first_name,
            last_name,
            age,
            department,
            salary,
            "Manager",
            managed_department
        )
    def show(self):

        print(f"""
    ID: {self.id}
    Name: {self.first_name} {self.last_name}
    Age: {self.age}
    Department: {self.department}
    Salary: Confidential
    Managed Department: {self.managed_department}
    """)