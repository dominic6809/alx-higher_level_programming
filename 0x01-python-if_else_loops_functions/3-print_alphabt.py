#!/usr/bin/python3

# Loop through ASCII values for lowercase letters
for i in range(97, 123):
    # Skip printing 'e' and 'q'
    if i != 101 and i != 113:
        # Print the character
        print("{:c}".format(i), end="")
