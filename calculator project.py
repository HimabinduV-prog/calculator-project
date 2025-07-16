# Define basic arithmetic operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2)
    return n1 / n2

# Dictionary to map symbols to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Main calculator function
def calculator():
    print("Welcome to the calculator!\n")

    # Get the first number
    num1 = float(input("Enter the first number: "))

    while True:
        # Show available operations
        print("\nAvailable operations:")
        for symbol in operations:
            print(symbol)

        # Choose an operation
        operation_symbol = input("Pick an operation from the above list: ")

        if operation_symbol not in operations:
            print("Invalid operation. Try again.")
            continue

        # Get the next number
        num2 = float(input("Enter the next number: "))

        # Perform calculation
        answer = operations[operation_symbol](num1, num2)

        print(f"\n answer: {num1} {operation_symbol} {num2} = {answer}")

        # Ask user whether to continue
        next_step = input(f"\nType 'y' to continue with {answer}, or 'n' to start a new calculation, or 'q' to quit: ").lower()

        if next_step == 'y':
            num1 = answer
        elif next_step == 'n':
            calculator()  # Restart the calculator
            break
        elif next_step == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid input.")
            break
        calculator()

# calling the function
calculator()
