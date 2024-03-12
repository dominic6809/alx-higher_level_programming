#!/usr/bin/python3
# Print each number with two digits separated by ', ' except the last one
# Use a single print statement for the numbers with proper formatting
for i in range(100):
    print("{:02d}".format(i), end=', ' if i < 99 else '\n')
