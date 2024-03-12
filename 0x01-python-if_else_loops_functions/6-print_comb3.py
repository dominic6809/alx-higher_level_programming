#!/usr/bin/python3
# For each first digit, iterate over the second digit from the first + 1 to 9
# Print each combination of two digits with proper formatting
for i in range(10):
    for j in range(i+1, 10):
        print("{:02d}, ".format(i*10 + j), end='')

# Print a newline character after printing all combinations

print()
