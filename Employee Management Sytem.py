class Employee():

    def __init__(self, name, salary, department):
        
        self.name = name
        self._salary = salary
        self.department = department

    def __str__(self):
        return f"Employee Name: {self.name}, Employee Salary: {self.salary}, Department = {self.department}"
    
    def show_details(self):
        
        print(f"Employee Name: {self.name}, Employee Salary: {self.salary}")

    def display_salary(self):
        print(f"{self.name}'s Salary: {self.salary}")


    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value
    
    def increase_salary(self, amount):
        self.salary += amount
        print(f"{self.name}'s new salary: {self.salary}")

class Manager(Employee):

    def __init__(self, name, salary, department, bonus=1000):
        super().__init__(name, salary, department)
        self.bonus = bonus

    def show_details(self):
        print(f"Employee Name: {self.name}, Employee Salary: {self.salary }, Bonus: {self.bonus},  Department = {self.department}")

class Developer(Employee):

    def __init__(self, name, salary, department, programming_lang):
        super().__init__(name, salary, department)
        self.programming_lang = programming_lang

    def show_details(self):
        print(f"Employee Name: {self.name}, Employee Salary: {self.salary }, Programming Language: {self.programming_lang},  Department = {self.department}")
        

m = Manager("Ramesh", 500000, "HR")
d = Developer("Suresh", 900000, "SDE", "Python")
m.show_details()
d.show_details()
d.increase_salary(60000)

        

