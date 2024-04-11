#!/usr/bin/python3
"""
text-identation module
"""


def text_indentation(text):
    """
    Print a text with new lines after each of ., ? and :.

    params:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    letter_result = ""

    for letter in text:
        letter_result += letter
        if letter in (".", "?", ":"):
            letter_result += "\n\n"

    # Print the processed text
    print(letter_result.rstrip())
