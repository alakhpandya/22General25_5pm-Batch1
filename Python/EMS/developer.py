from employees import Employee

class Developer(Employee):
    designation = "Developer"
    department_code = "D"

    def __init__(self, name, age, gender, experience):
        super().__init__(name, age, gender)
        self.experience = experience
  