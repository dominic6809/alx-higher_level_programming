#!/usr/bin/python3
# Function to calculate the value to subtract
def calculate_subtraction(num_list):
    to_subtract_val = 0
    max_value = max(num_list)

    # Iterate over the numbers in the list
    for num in num_list:
        if max_value > num:
            to_subtract_val += num

    return (max_value - to_subtract_val)


# Function to convert Roman numeral to integer
def roman_to_int(roman_string):
    # Check if the input is empty
    if not roman_string:
        return 0

    # Check if the input is a string
    if not isinstance(roman_string, str):
        return 0

    # Dictionary mapping Roman numerals to their integer values
    roman_numerals =
    {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_digits = list(roman_numerals.keys())

    # Initialize variables
    integer_val = 0
    last_roman = 0
    num_list = [0]

    # Iterate over each character in the Roman numeral string
    for char in roman_string:
        # Iterate over each Roman numeral
        for roman_numeral in roman_digits:
            # If the current character matches a Roman numeral
            if roman_numeral == char:
                if roman_numerals.get(char) <= last_roman:
                    integer_val += calculate_subtraction(num_list)
                    num_list = [roman_numerals.get(char)]
                else:
                    num_list.append(roman_numerals.get(char))

                last_roman = roman_numerals.get(char)

    # Add the value of the last set of Roman numerals
    integer_val += calculate_subtraction(num_list)

    return integer_val
