from employees import Employee

class Admin(Employee):
    designation = "Admin"
    department_code = "A"

    def display_details(self):
        return super().display_details()