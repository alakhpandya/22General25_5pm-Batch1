from employees import Employee

class Sale_executive(Employee):
    designation = "Sales Executive"
    department_code = "S"

    def __init__(self, name, age, gender, area):
        super().__init__(name, age, gender)
        self.area = area
