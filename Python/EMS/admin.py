from employees import Employee

class Admin(Employee):
    designation = "Admin"
    department_code = "A"

    @staticmethod
    def login(id, pwd):
        if 'A' not in id:
            return False
        