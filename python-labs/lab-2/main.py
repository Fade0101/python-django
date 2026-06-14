from employee import Employee
from manager import Manager

while True:

    print("""
1. Add Employee
2. Add Manager
3. List Employees
4. Transfer Employee
5. Fire Employee
q. Exit
""")

    choice = input("Choice: ")

    if choice == "1":

        first_name = input("First Name: ")
        last_name = input("Last Name: ")

        age = int(input("Age: "))

        department = input("Department: ")

        salary = float(
            input("Salary: ")
        )

        Employee(
            first_name,
            last_name,
            age,
            department,
            salary
        )
    if choice == "1":
        
        first_name = input("First Name: ")
        last_name = input("Last Name: ")

        age = int(input("Age: "))

        department = input("Department: ")

        salary = float(
            input("Salary: ")
        )

        Employee(
            first_name,
            last_name,
            age,
            department,
            salary
        )
    elif choice == "2":

        first_name = input("First Name: ")
        last_name = input("Last Name: ")

        age = int(input("Age: "))

        department = input("Department: ")

        salary = float(
            input("Salary: ")
        )

        managed_department = input(
            "Managed Department: "
        )

        Manager(
            first_name,
            last_name,
            age,
            department,
            salary,
            managed_department
        )
    elif choice == "3":
        Employee.list_employees()
    elif choice == "4":
        employee_id = int(input("Employee ID: "))
        new_department = input("New Department: ")
        for emp in Employee.employees:
            if emp.id == employee_id:
                emp.transfer(new_department)
                break
    elif choice == "5":
        employee_id = int(input("Employee ID: "))
        for emp in Employee.employees:
            if emp.id == employee_id:
                emp.fire()
                break
    elif choice == "q":
        break

        