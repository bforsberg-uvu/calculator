"""
Calculator Application
A command-line calculator that performs basic arithmetic operations.
"""

# Global variables - registers for operands and operation
x_register = 0
y_register = 0
operation = ''

def getInput(prompt, expected_type=str):
    """Get user input and validate its type."""
    user_input = input(prompt).strip()
    """ Allow user to quit the application"""
    if user_input.lower() == 'q': 
        print("Goodbye!")
        exit()
    """ Validate input type return input if valid"""
    try:
        if expected_type == float:
            return float(user_input)
        elif expected_type == str:
            if user_input in ('+', '-', '*', '/'):
                return user_input   
            else:
                raise ValueError()
    except (ValueError, TypeError) as e:
        if expected_type in (float, int):
            raise ValueError("Input must be a number. Please enter a valid number.") from e
        if expected_type == str:
            raise ValueError("Invalid arithmetic operation. Please enter one of +, -, *, /.") from e
        else:
            raise ValueError(f"Invalid input for type {expected_type.__name__}. Please enter a valid input.") from e

def doOperation(op, a, b):  
    """Perform the arithmetic operation."""
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("Cannot divide by zero. Please enter a non-zero divisor.")
        return a / b

def main():

    while True:
        """main loop to get user input and perform calculations"""
        try:
            x_register = getInput("Please enter the first number (or 'q' to quit): ", float)
            operation = getInput("Please enter the arithmetic operation (+, -, *, /): ", str)
            y_register = getInput("Please enter the second number: ", float)
            result = doOperation(operation, x_register, y_register)                                    
            print(f"Result: {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"Error: Invalid input. {e}\n")


if __name__ == "__main__":
    main()
