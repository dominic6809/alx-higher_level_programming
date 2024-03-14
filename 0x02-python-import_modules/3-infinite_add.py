#!/usr/bin/python3

if __name__ == "__main__":
    # Import sys module
    import sys
    the_sum = 0
    # Iterate through command-line arguments
    for arg in sys.argv:
        # Exclude the script name itself
        if arg != sys.argv[0]:
            # Convert argument to integer and add to sum
            the_sum += int(arg)
    # Print the sum
    print(the_sum)
