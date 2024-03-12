#!/usr/bin/python3
def print_last_digit(number):
    # Get the absolute value of the number to handle negative numbers
    number = abs(number)
    # Extract the last digit using the modulo operator
    last_digit = number % 10
    # Print the last digit
    print(last_digit)
    # Return the last digit
    return last_digit
