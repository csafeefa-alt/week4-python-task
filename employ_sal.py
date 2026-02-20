class Employee:
    
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def increase_salary(self, amount):
        self.salary += amount
        print(f"Salary increased by ₹{amount}")
    
    def display_details(self):
        print("\n--- Employee Details ---")
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Current Salary: ₹{self.salary}")


# Creating object
emp1 = Employee("Noorie", "EMP101", 30000)

# Calling methods
emp1.display_details()
emp1.increase_salary(5000)
emp1.display_details()