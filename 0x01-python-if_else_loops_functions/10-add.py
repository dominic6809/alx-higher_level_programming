#!/usr/bin/python3

def add(a, b):
    # Add the two integers and return the result
    return (a + b)

# Test cases


result = add(1,2)
print(f"{result:02}", end="")  # Print result with two chars without a newline

result = add(98,0)
print(f"{result:02}", end="")  # Print result with two chars without a newline
