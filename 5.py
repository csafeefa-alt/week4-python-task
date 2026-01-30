# employee attendace management system
attendance = {}
def mark_attendance():
    name = input("Enter employee name: ")
    day = input("Enter day (e.g., Day1): ")

    if name in attendance:
        attendance[name].append(day)
    else:
        attendance[name] = [day]

    print("Attendance marked for", name)
def calculate_working_days(name):
    if name in attendance:
        return len(attendance[name])
    else:
        return 0
def generate_report():
    print("\n--- Attendance Report ---")
    for name in attendance:
        days = calculate_working_days(name)
        print("Employee:", name)
        print("Working Days:", days)
        print("Days Present:", attendance[name])
        print("----------------------")
while True:
    print("\n--- Attendance Menu ---")
    print("1. Mark Attendance")
    print("2. Generate Report")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        mark_attendance()
    elif choice == 2:
        generate_report()
    elif choice == 3:
        print("Exiting Attendance System")
        break
    else:
        print("Invalid choice")