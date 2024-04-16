#!/usr/bin/python3
"""
function to Define a text file-reading function.
"""


def read_file(filename=""):
    """
    Reads the content of a text file and prints it to stdout.

    params:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    # Check if filename is provided
    if not filename:
        print("Please provide a filename.")
        return

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
