from datetime import datetime
import csv

class Employee():
    working_days = 22
    all_employees = []

    def __init__(self, name:str, age:int, gender:str):
        assert isinstance(name, str), "Please enter name in form of a string..."
        self.name = name

        # assert isinstance(age, float), "Age must be a number"
        assert isinstance(age, int), "Age must be a number"
        assert age >= 18, "Sorry, the employee must be atleast 18 years of age"
        self.age = age
        
        self.gender = gender

        self.createId()
        self.pwd = name[:4] + self.id[:4]
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

    def updatePassword(self):
        pass

    @classmethod
    def login(cls, id, pwd):
        if cls.department_code not in id:
            return False
        try:
            emp = Employee.all_employees[int(id[-3:]) - 100]
        except IndexError:
            return False
        
        if emp.id == id and emp.pwd == pwd:
            return True
        return False
    
    @staticmethod
    def writeToCSV():
        with open("employee_data.csv", "w") as f:
            # f.writelines(Employee.all_employees)
            pass

    def loadFromCSV():
        pass

    def __repr__(self) -> str:
        return f"[{self.name}, {self.age}, {self.gender}, {self.department_code}]"

if __name__ == "__main__":
    # e1 = Employee(31, "Hero", "M")
    # e1.display_details()
    # a = "hello"
    # a = 31
    # print(isinstance(a, str))
    # e1 = Employee("Abc", 15.7, "F")
    # e1 = Employee("Hero", 15, "M")
    e1 = Employee("Hero", 20, "M")
    e1.display_details()
