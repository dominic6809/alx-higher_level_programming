#!/usr/bin/python3

# Loop through numbers from 0 to 9 for the first digit
for i in range(0, 10):
    # Loop through numbers from 1 to 9 for the second digit
    for j in range(1, 10):
        # Check if the first digit is greater than or equal to the second digit
        if i >= j:
            continue  # Skip to the next iteration if condition is met
        # Check if it's the last combination
        if i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))  # Print the combination without a comma
        else:
            print("{:d}{:d}".format(i, j), end=", ")  # Print the combination with a comma
