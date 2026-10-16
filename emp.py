class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Monthly Salary:", self.salary)
        print("Annual Salary:", self.salary * 12)


emp = Employee("Nilofar", 5000)
emp.display()
