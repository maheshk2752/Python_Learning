 
# Program: Functions and Recursion in Python
# Author : Ram Beekhani
# Purpose:
# Demonstrates how functions work and how recursion
# can be used to solve problems like factorial calculation.
# ==========================================================


# ----------------------------------------------------------
# Function Example
# ----------------------------------------------------------
def greet_user(name):
    """
    Displays a welcome message.

    Parameters:
        name (str): Name of the user

    Returns:
        None
    """
    print(f"Hello, {name}! Welcome to Python Programming.")


# ----------------------------------------------------------
# Recursive Function Example
# ----------------------------------------------------------
def factorial(number):
    """
    Calculates the factorial of a number using recursion.

    Parameters:
        number (int): Positive integer

    Returns:
        int: Factorial value
    """

    # Base Case
    if number == 0 or number == 1:
        return 1

    # Recursive Case
    return number * factorial(number - 1)


# ----------------------------------------------------------
# Main Program
# ----------------------------------------------------------
print("=" * 50)
print("FUNCTIONS AND RECURSION DEMO")
print("=" * 50)

# Function Call
greet_user("Mahesh")

print("\nFactorial Calculation")

# User Input
num = int(input("Enter a positive number: "))

# Calculate and Display Result
result = factorial(num)

print(f"\nFactorial of {num} = {result}")

print("\nProgram Executed Successfully!")