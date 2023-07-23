from datetime import datetime

class Employee():
    working_days = 22
    all_employees = []
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

        self.createId()
        Employee.all_employees.append(self)

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Designation:", self.designation)
        print("Department Code:", self.department_code)

    def createId(self):
        year = str(datetime.today().year)
        month = str(datetime.today().month)
        number = str(100 + len(Employee.all_employees))
        self.id = year + month.zfill(2) + self.department_code + number