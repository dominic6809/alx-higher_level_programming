#!/usr/bin/python3

def fizzbuzz():
    # Iterate through numbers from 1 to 100
    for i in range(1, 101):
        # Check if the number is a multiple of both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        # Check if the number is a multiple of 3 only
        elif i % 3 == 0:
            print("Fizz", end=" ")
        # Check if the number is a multiple of 5 only
        elif i % 5 == 0:
            print("Buzz", end=" ")
        # If the number is not a multiple of 3 or 5, print the number itself
        else:
            print(i, end=" ")

# Test the function


fizzbuzz()
