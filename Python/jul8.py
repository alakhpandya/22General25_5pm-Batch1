
class Car:
    seating_capacity = 5
    all_cars = []

    def __init__(self, name, fuel, price):
        self.name = name
        self.fuel = fuel
        self.price = price
        Car.all_cars.append(self)

    # Method
    def displayDetails(self):
        print(f"--------------- Details of {self.name} ---------------")
        # print("Name:", self.name)
        print("Fuel:", self.fuel)
        print("Price:", self.price)
        print("Seating:", self.seating_capacity)
        print()

    @staticmethod
    def showInventory():
        print("Cars present in the inventory:")
        print("\nSrNo\tModel Name")
        for car in Car.all_cars:
            print(f"{Car.all_cars.index(car)}\t{car.name}")
        c = int(input("Serial number: "))
        return c

    def updateDetails(self):
        print("Enter new details:")
        name = input("Name: ")
        if name != "":
            self.name = name
        fuel = input("Fuel: ")
        if fuel != "":
            self.fuel = fuel
        price = input("Price: ")
        if price != "":
            self.price = int(price)
        seating_capacity = input("Seating: ")
        if seating_capacity != "":
            self.seating_capacity = seating_capacity

    @classmethod
    def addNewCar(cls):
        print("Enter the following details:")
        name = input("Name: ")
        fuel = input("Fuel type: ")
        price = int(input("Price: "))
        return cls(name, fuel, price)

c0 = Car("Alto", "Petrol", 400000)
# c1.displayDetails()
# Car.all_cars.append(c0)

c1 = Car("i20", "Diesel", 1000000)
# c2.displayDetails()
# Car.all_cars.append(c1)

# print(Car.all_cars)

while True:
    print("Press:")
    print("1 to add new car")
    print("2 to see details of a car")
    print("3 to update details of a car")
    print("4 to delete a car")
    print("5 to exit")

    op = int(input())
    if op == 1:
        Car.addNewCar()
    
    elif op == 2:
        c = Car.showInventory()
        Car.all_cars[c].displayDetails()

    elif op == 3:
        c = Car.showInventory()
        Car.all_cars[c].updateDetails()

    elif op == 4:
        c = Car.showInventory()
        Car.all_cars.pop(c)

    elif op == 5:
        break

    else:
        print("Invalid operation, please try again")
