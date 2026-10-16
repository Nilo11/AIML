class EmployeeDetails:
    def __init__(self, name, salary, experience):
        self.name = name
        self.salary = salary
        self.experience = experience

    def calculate_bonus(self):
        # 10% bonus for experience > 5 years, else 5%
        if self.experience > 5:
            bonus = self.salary * 0.10
        elif self.experience >= 1:
            bonus = self.salary * 0.05
        else:
            bonus = 0
        return bonus

    def display_details(self):
        bonus = self.calculate_bonus()
        print(f"Employee Name: {self.name}")
        print(f"Base Salary: ₹{self.salary}")
        print(f"Experience: {self.experience} years")
        print(f"Bonus Amount: ₹{bonus:.2f}")
        print(f"Total Salary: ₹{(self.salary + bonus):.2f}")

# Example Usage:
emp1 = EmployeeDetails("Nilofar", 60000, 6)
emp1.display_details()
