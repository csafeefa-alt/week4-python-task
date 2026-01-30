#question1- employee calculator system
def det():
    id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))
    hra = float(input("Enter HRA: "))
    da = float(input("Enter DA: "))
    pf = float(input("Enter PF Deduction: "))
    tax = float(input("Enter Tax Deduction: "))

    return id, name, basic, hra, da, pf, tax
def gross(basic, hra, da):
    return basic + hra + da
def ded(pf, tax):
    return pf + tax
def final(id, name, gross_salary, dedection, net_salary):
    print("Employee ID   :", id)
    print("Employee Name :", name)
    print("Gross Salary  :", gross_salary)
    print("Deductions    :", dedection)
    print("Net Salary    :", net_salary)
def main():
    id, name, basic, hra, da, pf, tax = det()

    gross_salary = gross(basic, hra, da)
    dedection = ded(pf, tax)
    net_salary = gross_salary - dedection

    final(id, name, gross_salary, dedection, net_salary)
main()