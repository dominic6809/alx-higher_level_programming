#!/usr/bin/python3
"""
function to define a text file insertion function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text into a file after each line
    containing a specific string.

    params:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line of the file.
        new_string (str): The string to insert after each line
        containing the search string.

    Returns:
        None
    """
    if not filename:
        print("Please provide a filename.")
        return

    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
