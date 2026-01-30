def sales_report():
    print("\n--- Sales Report ---")
    print("Total Sales: ₹2,50,000")
    print("Top Product: Laptop")
def inventory_report():
    print("\n--- Inventory Report ---")
    print("Items in Stock: 1200")
    print("Low Stock Items: 15")
def employee_report():
    print("\n--- Employee Report ---")
    print("Total Employees: 85")
    print("On Leave: 6")
REPORTS = {
    "sales": sales_report,
    "inventory": inventory_report,
    "employee": employee_report
}
def generate_report(report_name):
    report = REPORTS.get(report_name.lower())
    if report:
        report()
    else:
        print("❌ Report not found!")
def main():
    print("Available Reports:")
    for report in REPORTS:
        print("-", report.title())

    choice = input("\nEnter report name: ")
    generate_report(choice)
if __name__ == "__main__":
    main()