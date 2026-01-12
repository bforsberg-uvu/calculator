"""
Calculator Application
A command-line calculator that performs basic arithmetic operations.
"""

# Global variables
x_reg = 0
y_reg = 0
oper = ''


def getInput(prompt, expected_type=str):
    user_input = input(prompt).strip()
    if user_input.lower() == 'q':
        print("Goodbye!")
        exit()
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
        try:
            x_reg = getInput("Please enter the first number (or 'q' to quit): ", float)
            oper = getInput("Please enter the arithmetic operation (+, -, *, /): ", str)
            y_reg = getInput("Please enter the second number: ", float)
            result = doOperation(oper, x_reg, y_reg)                                    
            print(f"Result: {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
        except Exception as e:
            print(f"Error: Invalid input. {e}\n")


if __name__ == "__main__":
    main()
