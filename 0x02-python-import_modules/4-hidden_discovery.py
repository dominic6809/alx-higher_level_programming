#!/usr/bin/python3

# Import module hidden_4
import hidden_4

# Check if this script is run directly
if __name__ == "__main__":
    # Iterate through names of attributes in hidden_4 module
    for name in dir(hidden_4):
        # Exclude names starting with "__"
        if not name.startswith("__"):
            # Print non-hidden attribute names
            print(name)
