from database import Database


class Employee:

    employees = []

    def __init__(
            self,
            first_name,
            last_name,
            age,
            department,
            salary):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary

        self.id = Database.insert_employee(
            first_name,
            last_name,
            age,
            department,
            salary,
            "Employee"
        )

        Employee.employees.append(self)
    def show(self):
        print(f"""
        ID: {self.id}
        Name: {self.first_name} {self.last_name}
        Age: {self.age}
        Department: {self.department}
        Salary: {self.salary}
        """)
    def transfer(self, new_department):

            self.department = new_department

            Database.update_department(
                self.id,
                new_department
            )
    def fire(self):
        if self in Employee.employees:
            Employee.employees.remove(self)
        Database.delete_employee(self.id)
        
    @classmethod
    def list_employees(cls):
        employees = Database.get_all_employees()
        for employee in employees:
            print(employee)