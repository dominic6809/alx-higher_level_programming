#!/usr/bin/python3
import random

# Generate a random signed number between -10000 and 10000
number = random.randint(-10000, 10000)

# Get the last digit of the absolute value of the number
last_digit = abs(number) % 10

# Print the message along with the last digit of the number
print(f'The string Last digit of {number} is {last_digit}', end=' ')

# Check the value of the last digit and print the appropriate message
if last_digit > 5:
    print('and is greater than 5')
elif last_digit == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
