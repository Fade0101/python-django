import mysql.connector
from config import DB_CONFIG


class Database:

    @staticmethod
    def get_connection():
        return mysql.connector.connect(**DB_CONFIG)

    @staticmethod
    def insert_employee(
            first_name,
            last_name,
            age,
            department,
            salary,
            employee_type,
            managed_department=None):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO employee
        (
            first_name,
            last_name,
            age,
            department,
            salary,
            employee_type,
            managed_department
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(query, (
            first_name,
            last_name,
            age,
            department,
            salary,
            employee_type,
            managed_department
        ))

        conn.commit()

        employee_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return employee_id
    @staticmethod
    def update_department(employee_id, new_department):

        conn = Database.get_connection()
        cursor = conn.cursor()

        query = """
        UPDATE employee
        SET department=%s
        WHERE id=%s
        """

        cursor.execute(query, (
            new_department,
            employee_id
        ))

        conn.commit()

        cursor.close()
        conn.close()

    @staticmethod
    def delete_employee(employee_id):

        conn = Database.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM employee WHERE id=%s",
            (employee_id,)
        )

        conn.commit()

        cursor.close()
        conn.close()
    @staticmethod
    def get_all_employees():

        conn = Database.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM employee"
        )

        employees = cursor.fetchall()

        cursor.close()
        conn.close()

        return employees