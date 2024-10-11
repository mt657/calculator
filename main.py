'''Main module for the calculator REPL (Read-Eval-Print Loop) functionality.'''
from app.operations import addition, subtraction, multiplication, division

def display_menu():
    """Display the available commands to the user."""
    print("\nSimple Calculator")
    print("Available commands:")
    print("add [a] [b] - Adds two numbers")
    print("sub [a] [b] - Subtracts second number from first")
    print("mul [a] [b] - Multiplies two numbers")
    print("div [a] [b] - Divides first number by second")
    print("exit - Exit the calculator")

def repl():
    '''Run the REPL for the calculator, allowing users to perform operations interactively.'''
    print("Welcome to the Calculator REPL!")
    display_menu()
    
    while True:
        user_input = input("Please enter a command: ").strip()
        
        if user_input.lower() == "exit":
            print("Thank you for using the calculator! Goodbye!")
            break
        
        try:
            # Split user input into components
            parts = user_input.split()
            operation = parts[0]
            a = float(parts[1])
            b = float(parts[2])

            # Perform the operation based on the user input
            if operation == "add":
                result = addition(a, b)
                print(f"The result of adding {a} and {b} is: {result}")
            elif operation == "sub":
                result = subtraction(a, b)
                print(f"The result of subtracting {b} from {a} is: {result}")
            elif operation == "mul":
                result = multiplication(a, b)
                print(f"The result of multiplying {a} and {b} is: {result}")
            elif operation == "div":
                result = division(a, b)
                if isinstance(result, str):  # Handle division error message
                    print(result)
                else:
                    print(f"The result of dividing {a} by {b} is: {result}")
            else:
                print("Error: Unknown operation! Please try again.")
                display_menu()  # Display menu again for clarity

        except (ValueError, IndexError):
            print("Oops! There seems to be a problem with your input.")
            print("Please ensure you entered a valid operation followed by two numbers.")
            print("For example: 'add 10 5'")
            display_menu()  # Display menu again for clarity

if __name__ == "__main__":
    repl()
