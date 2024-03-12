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
        if ord(char) >= ord('a') and ord(char) <= ord('z'):  # Check if the char is lowercase
            output += chr(ord(char) - ord('a') + ord('A'))  # Convert the char to uppercase and append to output
        else:
            output += char  # Keep the char unchanged if it's not lowercase
    print("{:s}".format(output))  # Print the resulting uppercase string
