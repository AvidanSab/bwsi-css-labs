"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")
def sanitation_int(prompt: str) -> float:
    """Keeps asking until the user enters a valid number."""
    while True:
        user_input = input(prompt)
        try:
            # Tries to turn the string into a decimal number
            return float(user_input) 
        except ValueError:
            # If it fails (e.g., they typed "apple"), it catches the error and loops again
            print("That's not a valid number. Try again.")

def sanitation_str(prompt: str) -> str:
    """Keeps asking until the user enters a valid math operation."""
    valid_operations = ["add", "subtract", "divide", "multiply"]
    
    while True:
        # Ask for input, remove extra spaces, and make it lowercase
        user_input = input(prompt).strip().lower()
        
        # Check if their input is in our list of valid words
        if user_input in valid_operations:
            return user_input
        else:
            print("Invalid. Please type add, subtract, divide, or multiply.")
    

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = sanitation_int("Enter the first number: ")
    num2 = sanitation_int("Enter the second number: ")
    operation = sanitation_str("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
