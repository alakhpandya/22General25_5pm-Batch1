# incorrect way to use a package
"""
import myPackage

myPackage.myModule.myFunc()
"""
# Correct ways:
"""
from myPackage import myModule
myModule.myFunc()
"""
"""
from myPackage import myModule as mm
mm.myFunc()
"""
"""
from myPackage.myModule import myFunc
myFunc()
"""
"""
from myPackage.myModule import myFunc as fnc
fnc()
"""

# myPackage -> subPackage -> subModule -> subFunc
"""
from myPackage.subPackage import subModule
subModule.subFunc()


from myPackage.subPackage import subModule as sm
sm.subFunc()

from myPackage.subPackage.subModule import subFunc
subFunc()

from myPackage.subPackage.subModule import subFunc as snc
snc()
"""

# Downloading & installing external packages/libraries:
# pip install <Package Name> in cmd/terminal
# import numpy as np

# Some useful built in modules
import datetime

# print(dir(datetime))

# print(datetime.MAXYEAR)
# print(datetime.MINYEAR)

todays_date = datetime.date(2023, 6, 24)
"""
# print(todays_date)
print(todays_date.day)
print(todays_date.month)
print(todays_date.year)
"""

# last_day = datetime.date(2023, 12, 31)
# print(last_day - todays_date)

# print(todays_date + 100)

# interval = datetime.timedelta(100)
"""
print(todays_date + interval)
print(todays_date - interval)
"""

# birthday = datetime.datetime(2000, 7, 31, 16, 30, 40, 575)
# birthday = datetime.datetime(2000, 7, 31, 16, 30)
# print(birthday)

dob_date = int(input("Date: "))
dob_month = int(input("Month: "))
dob_year = int(input("Year: "))

dob = datetime.datetime(dob_year, dob_month, dob_date)
curr_date = datetime.datetime.today()

print("Your age in days =", curr_date - dob)

# Next Class: strptime, strftime