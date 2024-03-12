#!/usr/bin/python3

def uppercase(s):
    """
    Convert a string to uppercase and print it.

    Parameters:
    s (str): The string to convert to uppercase.

    Returns:
    None
    """
    output = ''  # Initialize an empty string for the output
    for char in s:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):  # Check char=lower
            output += chr(ord(char) - ord('a') + ord('A'))
        else:
            output += char  # Keep the char unchanged if it's not lowercase
    print("{:s}".format(output))  # Print the resulting uppercase string
