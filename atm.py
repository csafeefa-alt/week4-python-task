balance = 10000  # Initial balance

print(" Welcome to ATM Withdrawal System")
print(" Your initial balance is: ₹", balance)

while True:
    print(f"1️ Withdraw Money")
    print(f"2️ Exit")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == "2":
        print(" Thank you for using the ATM. Goodbye!")
        break

    elif choice == "1":
        try:
            amount = float(input("Enter withdrawal amount: ₹"))
            if amount <= 0:
                raise ValueError(" Withdrawal amount must be greater than zero!")
            if amount > balance:
                raise ValueError("Insufficient balance! You cannot withdraw more than " + str(balance))
            balance -= amount
            print(" Withdrawal successful!")
            print(" You withdrew: ₹", amount)
            print(" Remaining balance: ₹", balance)

        except ValueError as e:
            print("Error:", e)

    else:
        print(" Invalid choice! Please enter 1 or 2.")