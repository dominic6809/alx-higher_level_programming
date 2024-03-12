#!/usr/bin/python3
def islower(c):
    # Check if the ASCII value of c is in the range of lowercase letters
    ascii_value = ord(c)
    return 97 <= ascii_value <= 122

# Test cases
print(islower('a'))
print(islower('A'))
print(islower('z'))
print(islower('Z'))
print(islower('1'))
