class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_circumference(self):
        return 2 * 3.14 * self.radius

    def display(self):
        print("Radius:", self.radius)
        print("Area:", self.calculate_area())
        print("Circumference:", self.calculate_circumference())


# Creating a Circle object and displaying results
circle = Circle(7)
circle.display()
