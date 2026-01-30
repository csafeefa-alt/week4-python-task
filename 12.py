def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def calculator():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Choose operation: "))
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if choice == 1:
        print("Result:", add(a, b))
    elif choice == 2:
        print("Result:", subtract(a, b))
    elif choice == 3:
        print("Result:", multiply(a, b))
    elif choice == 4:
        print("Result:", divide(a, b))
    else:
        print("Invalid choice")
def reverse_string(s):
    return s[::-1]
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)
def string_operations():
    print("1. Reverse String")
    print("2. Count Vowels")
    choice = int(input("Choose operation: "))
    s = input("Enter a string: ")
    if choice == 1:
        print("Reversed:", reverse_string(s))
    elif choice == 2:
        print("Vowel Count:", count_vowels(s))
    else:
        print("Invalid choice")
def is_even(n):
    return n % 2 == 0
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
def number_utilities():
    print("\n--- Number Utilities ---")
    print("1. Check Even/Odd")
    print("2. Factorial")
    choice = int(input("Choose operation: "))
    n = int(input("Enter a number: "))
    if choice == 1:
        print("Even" if is_even(n) else "Odd")
    elif choice == 2:
        print("Factorial:", factorial(n))
    else:
        print("Invalid choice")
def main_menu():
    while True:
        print("\n=== Main Menu ===")
        print("1. Calculator")
        print("2. String Operations")
        print("3. Number Utilities")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            calculator()
        elif choice == 2:
            string_operations()
        elif choice == 3:
            number_utilities()
        elif choice == 4:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

main_menu()