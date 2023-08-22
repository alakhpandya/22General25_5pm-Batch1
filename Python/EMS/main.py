"""
Types of employees: Peon, Manager, SalesExexecutive, GeneralManager, Developer, AdminStaff
Features:
name, age, gender, education, experience, insured amount,
salary, designation, 
id_no:
    format: 202307P102, 202008M101
date of joining, cl, working_days,
attendance:
(days/in-out hours - half day, full day, 25%, leave)
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
import sys
from employees import Employee
from admin import Admin
from peon import Peon
from developer import Developer
from sales_executive import Sale_executive
from manager import Manager
from general_manager import General_manager

def login():
    attempt = 3
    while True:
        print("Press:")
        print("1 for Admin login")
        print("2 for Peon login")
        print("3 for Developer login")
        print("4 for Sales Executive login")
        print("5 for Manager login")
        print("6 for General Manager login")
        print("9 to exit")
        choice = int(input())
        if choice in [1,2,3,4,5,6]:
            id = input("ID: ")
            pwd = input("Password: ")
        
        if choice == 1:
            if Admin.login(id, pwd):
                return "A"

        elif choice == 2:
            if Peon.login(id, pwd):
                return "P"

        elif choice == 3:
            if Developer.login(id, pwd):
                return "D"
        
        elif choice == 4:
            if Sale_executive.login(id, pwd):
                return "S"
        
        elif choice == 5:
            if Manager.login(id, pwd):
                return "M"
        
        elif choice == 6:
            if General_manager.login(id, pwd):
                return "G"

        elif choice == 9:
            break

        else:
            print("Invalid option, please try again...")

        attempt -= 1
        print("Invalid ID or Password, please try again. Attempt left:", attempt)
        if attempt == 0:
            break

    return False


gm1 = General_manager("Parth", 32, "M")
# gm1.display_details()
p1 =Peon("Ramesh", 22, "M")
# p1.display_details()
a1 = Admin("Rajeev", 28, "M")

# print(Employee.all_employees)
Employee.writeToCSV()

# department_code = login()
# if not department_code:
#     print("Your account has been blocked. Call customer care center to re-activate it.")
#     sys.exit()

# Next class: validations, more functionalitites to this program.