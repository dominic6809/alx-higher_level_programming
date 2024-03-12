#!/usr/bin/python3

def add(a, b):
    # Add the two integers and return the result
    return (a + b)

# Test cases


result = add(5, 3)
print(f"{result:02}", end="")  # Print result with two chars without a newline

result = add(-10, 20)
print(f"{result:02}", end="")  # Print result with two chars without a newline
