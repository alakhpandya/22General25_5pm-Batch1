"""
Types of employees: Peon, Manager, SalesExexecutive, GeneralManager, Developer, AdminStaff
Features:
name, age, gender, education, experience, insured amount,
salary, designation, id_no, date of joining, cl, working_days,
attendance:
(days/in-out hours - half day, full day, 25%)
swipe-in method, swipe-out method in employee dashboard

create new employee
edit details of an existing employee
view details of an employee
remove an employee

print salary sleep
increment
bonus
incentives
rating by manager
promotion that increments salary automatically

"""

class Employee():
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender



while True:
    print("Press:")
    print("1 for Peon login")
    print("2 for Admin login")
    print("3 for Developer login")
    print("4 for Sales Executive login")
    print("5 for Manager login")
    print("6 for General Manager login")
    