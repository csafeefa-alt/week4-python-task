class Rectangle:
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def calculate_area(self):
        area = self.length * self.breadth
        print(f"Area of Rectangle: {area}")
    
    def update_dimensions(self, new_length, new_breadth):
        self.length = new_length
        self.breadth = new_breadth
        print("Dimensions updated successfully.")


# Creating object
rect1 = Rectangle(10, 5)

# Calling methods
rect1.calculate_area()
rect1.update_dimensions(15, 8)
rect1.calculate_area()