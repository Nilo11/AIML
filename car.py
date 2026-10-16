class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("-" * 20)


# Creating two Car objects
car1 = Car("Toyota", "Camry", 25000)
car2 = Car("Tesla", "Model 3", 40000)

# Displaying details of both cars
car1.display()
car2.display()
