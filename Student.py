class Student:
    def __init__(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.total = 0
        self.percentage = 0.0

    def calculate(self):
        self.total = self.mark1 + self.mark2 + self.mark3
        self.percentage = (self.total / 300) * 100

    def get_grade(self):
        if self.percentage >= 90:
            return 'A+'
        elif self.percentage >= 75:
            return 'A'
        elif self.percentage >= 60:
            return 'B'
        elif self.percentage >= 50:
            return 'C'
        elif self.percentage >= 35:
            return 'D'
        else:
            return 'Fail'

    def display(self):
        self.calculate()
        print(f"Total Marks: {self.total}/300")
        print(f"Percentage: {self.percentage:.2f}%")
        print(f"Grade: {self.get_grade()}")

# Example Usage:
student1 = Student(85, 90, 88)
student1.display()
