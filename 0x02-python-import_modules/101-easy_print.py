#!/usr/bin/python3

# Import the 'os' module and call the write method to write a string to stdout
# The string "#pythoniscool\n" is encoded into bytes before writing
import os
os.write(1, "#pythoniscool\n".encode())
