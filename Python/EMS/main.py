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
from admin import Admin
from peon import Peon
from developer import Developer
from sales_executive import Sale_executive
from manager import Manager
from general_manager import General_manager

def login():
    while True:
        print("Press:")
        print("1 for Admin login")
        print("2 for Peon login")
        print("3 for Developer login")
        print("4 for Sales Executive login")
        print("5 for Manager login")
        print("6 for General Manager login")
        choice = int(input())
        id = input("ID: ")
        pwd = input("Password: ")

        if choice == 1:
            Admin.login(id, pwd)

        elif choice == 2:
            pass
        
        elif choice == 3:
            pass
        
        elif choice == 4:
            pass
        
        elif choice == 5:
            pass
        
        elif choice == 6:
            pass

        else:
            print("Invalid option, please try again...")



gm1 = General_manager("Parth", 32, "M")
# gm1.display_details()
p1 =Peon("Ramesh", 22, "M")
# p1.display_details()

