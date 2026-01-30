employees = {}
def add_employee(emp_id, name, basic_salary=30000, bonus=0, deductions=0):
    employees[emp_id] = {
        "name": name,
        "basic_salary": basic_salary,
        "bonus": bonus,
        "deductions": deductions
    }
    print(f"Employee {name} added successfully.")
def calculate_salary(emp_id, extra_bonus=0, extra_deductions=0):
    if emp_id not in employees:
        print("Employee not found!")
        return None
    emp = employees[emp_id]
    total_salary = emp["basic_salary"] + emp["bonus"] + extra_bonus - emp["deductions"] - extra_deductions
    return total_salary
def update_bonus_deductions(emp_id, bonus=0, deductions=0):
    if emp_id not in employees:
        print("Employee not found!")
        return
    employees[emp_id]["bonus"] += bonus
    employees[emp_id]["deductions"] += deductions
    print(f"Updated bonus and deductions for {employees[emp_id]['name']}.")
def generate_payroll_report():
    print("\n--- Payroll Report ---")
    print("{:<10} {:<15} {:<10}".format("Emp ID", "Name", "Salary"))
    print("-" * 40)
    for emp_id, data in employees.items():
        salary = calculate_salary(emp_id)
        print("{:<10} {:<15} {:<10}".format(emp_id, data["name"], salary))
    print("-" * 40)
# ------------------- Sample Usage -------------------
add_employee(102, "Sara", bonus=2000)
add_employee(103, "Ravi")  
update_bonus_deductions(101, bonus=1000, deductions=500)
update_bonus_deductions(103, deductions=200)
print("\nAman's total salary:", calculate_salary(101, extra_bonus=500))
print("Sara's total salary:", calculate_salary(102, extra_deductions=300))
generate_payroll_report()