class Mobile:
    
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def apply_discount(self, discount_amount):
        if discount_amount <= self.price:
            self.price -= discount_amount
            print(f"Discount of ₹{discount_amount} applied successfully.")
        else:
            print("Discount amount cannot be greater than price!")
    
    def display_mobile(self):
        print("\n--- Mobile Details ---")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ₹{self.price}")


# Creating object
mobile1 = Mobile("Samsung", "Galaxy S23", 75000)

# Calling methods
mobile1.display_mobile()
mobile1.apply_discount(5000)
mobile1.display_mobile()