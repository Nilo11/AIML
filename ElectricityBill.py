class ElectricityBill:
    def __init__(self, units):
        self.units = units

    def calculate_bill(self):
        # Example Slabs:
        # First 100 units: ₹3/unit
        # Next 100 units (101-200): ₹5/unit
        # Above 200 units: ₹8/unit
        bill = 0
        units = self.units

        if units <= 100:
            bill = units * 3
        elif units <= 200:
            bill = (100 * 3) + ((units - 100) * 5)
        else:
            bill = (100 * 3) + (100 * 5) + ((units - 200) * 8)

        return bill

    def display_bill(self):
        amount = self.calculate_bill()
        print(f"Total Units Consumed: {self.units}")
        print(f"Total Electricity Bill: ₹{amount:.2f}")

# Example Usage:
bill1 = ElectricityBill(250)
bill1.display_bill()
