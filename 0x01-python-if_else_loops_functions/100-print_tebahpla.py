#!/usr/bin/python3

# Iterate over the ASCII values from 'z' (122) to 'a' (97) in reverse order
for i in reversed(range(97, 123)):
    # Check if the ASCII value is even or odd
    if i % 2 == 0:
        # If even, print the character as it is
        print("{:c}".format(i), end='')
    else:
        # If odd, subtract 32 to convert to uppercase and then print
        print("{:c}".format(i - 32), end='')
