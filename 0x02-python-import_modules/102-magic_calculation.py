#!/usr/bin/env python3

# Importing required functions from the module magic_calculation_102
from magic_calculation_102 import add, sub


# Defining a function named magic_calculation
def magic_calculation(a, b):
    # Checking if 'a' is less than 'b'
    if a < b:
        # If true, perform addition with 'a' and 'b'
        c = add(a, b)

        # Perform addition with 'c' and numbers from 4 to 5 using a loop
        for i in range(4, 6):
            c = add(c, i)

        # Return the final result after additions
        return c
    else:
        # If 'a' is not less than 'b', perform subtraction
        return sub(a, b)
