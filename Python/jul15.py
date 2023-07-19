"""
4 Pillars of OOP:
Inheritance, Abstraction, Polymorphism, Encapsulation

class Father:
    vehicle = "i20"
    laptop = "i3"

    def updateVehicle(self, newVehicle):
        self.vehicle = newVehicle

class A(Father):
    college = "Royal University"
    laptop = "i5"


x = A()
print(x.vehicle)
# x.updateVehicle('Activa')
# print(x.vehicle)
# print(x.__dict__)
print(x.college)

# y = A()
# print(y.vehicle)
# print(y.__dict__)

f = Father()
f.vehicle
f.updateVehicle('Kia Sonet')

parth = A()
parth.laptop = "Macbook M2 Pro"
print(parth.laptop)

tirth = A()
print(tirth.laptop)

azim = A()
print(azim.vehicle)

kavish = A()
print(kavish.profession)
kavish.displayProperties()
"""
# MRO: Method Resolution Order

# Single level/Single/Simple Inheritance
# Multi level inheritance
# Hierarchical inheritance
# Hybrid inheritance
"""
class Father:
    vehicle = "i20"
    laptop = "i3"

    def updateVehicle(self, newVehicle):
        self.vehicle = newVehicle

class A(Father):
    college = "Royal University"
    laptop = "i5"

class Sibling(Father):
    college = "Oracle University"
    laptop = "i7"

class B(A):
    school = "Royal"
    laptop = "Toy"

p = B()
p.laptop = "iPad"
"""

# Multiple inheritance
"""
class Father:
    profession = "Business"

class Mother:
    vehicle = "i20"
    profession = "Doctor"

class A(Father, Mother):
    pass

class B(Mother, Father):
    pass

# class C(Mother, Father):
class C(A, B):
    pass

o1 = A()
print(o1.vehicle)
print(o1.profession)

o2 = B()
print(o2.vehicle)
print(o2.profession)

o3 = C()
print(o3.profession)
"""
# EMS: Employee Management System
# IMS: Inventory Management System
# CMS: Car-showroom Management System