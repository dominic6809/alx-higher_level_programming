#!/usr/bin/python3
"""
function to define a file-appending function.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and
    returns the number of characters written.

    params:
        filename (str): The name of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    # Check if filename is provided
    if not filename:
        print("Please provide a filename.")
        return 0

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
