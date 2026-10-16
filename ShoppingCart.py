class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, name, price, quantity):
        self.items.append({'name': name, 'price': price, 'quantity': quantity})
        print(f"Added {quantity} x {name} to cart.")

    def calculate_total_bill(self):
        total = 0
        print("\n--- BILL RECEIPT ---")
        for item in self.items:
            item_total = item['price'] * item['quantity']
            total += item_total
            print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{item_total:.2f}")
        print(f"--------------------")
        print(f"Total Amount Payable: ₹{total:.2f}")

# Example Usage:
cart = ShoppingCart()
cart.add_product("Laptop Mouse", 500, 2)
cart.add_product("Keyboard", 1200, 1)
cart.calculate_total_bill()
