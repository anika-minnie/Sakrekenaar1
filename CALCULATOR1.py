#simple calculator on Python
# function to add two numbers
def add(x, y):
    return x + y
# function to subtract two numbers
def subtract(x, y):
    return x - y
# funtion to multiply two numbers
def multiply(x, y): 
    return x * y    
# function to divide two numbers 
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
# function to clear screen 
def clear_screen():
    import os
    os.system('cls'if os.name == 'nt' else 'clear')

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # loops fo calculator 
    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
            continue
        
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice! Please select a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("exiting the calculator. GOODBYE!")


