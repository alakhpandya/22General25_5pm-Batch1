# OOP
class Car:
    seating_capacity = 4

    # Method
    def displayDetails(self):
        print("Name:", self.model_name)
        print("Fuel:", self.fuel)
        print("Price:", self.price)
        print("Seating:", self.seating_capacity)
        print()

c1 = Car()
# Object Variables
c1.model_name = "Mercedes s610"
c1.fuel = "Petrol"
c1.price = 30000000

# print("Name:", c1.model_name)
# print("Fuel:", c1.fuel)
# print("Price:", c1.price)
# print("Seating:", c1.seating_capacity)
# print()
# c1.displayDetails()

c2 = Car()
# Object Variables
c2.model_name = "BMW i700"
c2.fuel = "Electric"
c2.price = 25000000

# print("Name:", c2.model_name)
# print("Fuel:", c2.fuel)
# print("Price:", c2.price)
# print("Seating:", c2.seating_capacity)
# print()
c2.displayDetails()
print(c2.__dict__)

c3 = Car()
c3.model_name = "XUV700"
c3.fuel = "Diesel"
c3.price = 2700000
c3.seating_capacity = 7

c3.displayDetails()
# c2.displayDetails()
print(c3.__dict__)

# MRO: Method Resolution Order
"""
Object variable has higher priority than class variable
"""

Car.seating_capacity = 5
c2.displayDetails()