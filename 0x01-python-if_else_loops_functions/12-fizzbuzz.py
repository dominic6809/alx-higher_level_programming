#!/usr/bin/python3

def fizzbuzz():
    # Initialize a counter for the number of characters printed
    char_count = 0
    
    # Iterate through numbers from 1 to 100
    for i in range(1, 101):
        # Check if the number is a multiple of both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
            char_count += 8  # Increment char count by len of "FizzBuzz" + a space
        elif i % 3 == 0:
            print("Fizz", end=" ")
            char_count += 5  # Increment char count by len of "Fizz" + a space
        # Check if the number is a multiple of 5 only
        elif i % 5 == 0:
            print("Buzz", end=" ")
            char_count += 5  # Increment char count by len of "Buzz" + a space
        # If the number is not a multiple of 3 or 5, print the number itself
        else:
            num_str = str(i)
            print(num_str, end=" ")
            char_count += len(num_str) + 1
        
        # Check if total characters printed reaches 415
        if char_count >= 415:
            break

# Test the function


fizzbuzz()
