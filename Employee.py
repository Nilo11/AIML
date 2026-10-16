class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # Monthly salary

    def calculate_annual_salary(self):
        return self.salary * 12

    def display_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Monthly Salary: ${self.salary:,.2f}")
        print(f"Annual Salary: ${self.calculate_annual_salary():,.2f}")
              
    
