# -----------------------------
# Base Class
# -----------------------------

class Employee:

    def __init__(self, name, salary):                       # constructor
        self.name = name                                    # employee name
        self.salary = salary                                # base salary

    def calculate_salary(self):                             # method to calculate salary (will be overridden)
        return self.salary


# -----------------------------
# Regular Employee
# -----------------------------

class RegularEmployee(Employee):

    def __init__(self, name, salary, bonus):                # constructor with bonus 
        super().__init__(name, salary)                      # call parent constructor
        self.bonus = bonus                                  # extra bonus

    def calculate_salary(self):                             # override salary calculation to include bonus
        total = self.salary + self.bonus
        return total


# -----------------------------
# Contract Employee
# -----------------------------

class ContractEmployee(Employee):

    def __init__(self, name, hourly_rate, hours_worked):    # constructor with hourly rate and hours worked
        super().__init__(name, 0)                           # call parent constructor
        self.hourly_rate = hourly_rate                      # pay per hour 
        self.hours_worked = hours_worked                    # total hours

    def calculate_salary(self):                             # override salary calculation to calculate based on hours worked
        total = self.hourly_rate * self.hours_worked
        return total


# -----------------------------
# Manager
# -----------------------------

class Manager(Employee):

    def __init__(self, name, salary, allowance):           # constructor with allowance
        super().__init__(name, salary)
        self.allowance = allowance                         # extra allowance

    def calculate_salary(self):                            # override salary calculation to include allowance
        total = self.salary + self.allowance
        return total


# -----------------------------
# Main Program
# -----------------------------

emp1 = RegularEmployee("Arul", 36000, 9000)                # base salary of 36000 and bonus of 9000 
emp2 = ContractEmployee("Arun", 300, 120)                  # hourly rate of 300 and 120 hours worked
emp3 = Manager("Aara", 42000, 10000)                       # base salary of 42000 and allowance of 10000

employees = [emp1, emp2, emp3]                             # store all employees in a list

for emp in employees:                                      # loop through employees and print their name and calculated salary
    print("Name:", emp.name)
    print("Salary: Rs.", emp.calculate_salary())           # polymorphic call to calculate_salary method 
    print("-----")