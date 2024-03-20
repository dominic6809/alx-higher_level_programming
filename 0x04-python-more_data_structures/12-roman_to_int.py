#!/usr/bin/python3

def roman_to_int(roman_string):
    # Check if the input is a string or None using a ternary operator
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Dictionary mapping Roman numerals to their integer values
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    # Initialize variables
    current_value = 0
    previous_value = 0

    # Iterate over each character in the reversed Roman numeral string
    for symbol in reversed(roman_string):
        # Get the value of the current symbol from the dictionary
        value = roman_numerals.get(symbol, 0)

        current_value += value if value >= previous_value else -value

        # Update the previous value for the next iteration
        previous_value = value

    return current_value
