class BankAccount:
    
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ₹{amount}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Amount Withdrawn: ₹{amount}")
        else:
            print("Insufficient Balance!")
    
    def display_balance(self):
        print("\n--- Account Details ---")
        print(f"Account Holder Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance}")


# Creating object
account1 = BankAccount("Noorie", "1234567890", 5000)

# Calling methods
account1.display_balance()
account1.deposit(2000)
account1.withdraw(1500)
account1.display_balance()