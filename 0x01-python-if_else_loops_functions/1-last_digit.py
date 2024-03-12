#!/usr/bin/python3
import random

# Generate a random signed number between -10000 and 10000
number = random.randint(-10000, 10000)

# Determine the last digit of the number
if number == 0:
    last_digit = 0
elif number > 0:
    last_digit = int(str(number)[-1])  # Convert last char of number to integer
else:
    last_digit = -1 * (int(str(number)[-1]))
    # Convert last char of number to int and negate it

# Determine the suffix based on the value of the last digit
if last_digit > 5:
    suffix = "and is greater than 5"
elif last_digit == 0:
    suffix = "and is 0"
elif last_digit < 6 and last_digit != 0:
    suffix = "and is less than 6 and not 0"

# Print the result with appropriate formatting
print(f"Last digit of {number:d} is {last_digit:d} {suffix}")
