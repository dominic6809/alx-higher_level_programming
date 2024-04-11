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

    if len(text) is 0:
        return

    for char in text:
        letter_result += char
        if char in ["?", ":", "."]:
            while letter_result[0] is " ":
                letter_result = letter_result[1:]
            print(letter_result)
            print()
            letter_result = ""
    if len(letter_result) != 0:
        try:
            while letter_result[0] is " ":
                letter_result = letter_result[1:]
        except:
            pass
        print(letter_result, end="")
