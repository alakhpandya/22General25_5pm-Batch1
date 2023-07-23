from employees import Employee

class Manager(Employee):
    designation = "Manager"
    department_code = "M"
    education = "MBA"

    def display_details(self):
        super().display_details()
        print("Education:", self.education)