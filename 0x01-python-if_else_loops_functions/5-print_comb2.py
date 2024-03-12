#!/usr/bin/python3

# Loop through numbers from 0 to 99
for number in range(100):
    # Check if the number is not the last one
    if number != 99:
        # Print the number with leading zeros and a comma
        print("{num:02d}".format(num=number), end=", ")
    else:
        # Print the last number with leading zeros and a newline
        print("{num:02d}".format(num=number), end="\n")
