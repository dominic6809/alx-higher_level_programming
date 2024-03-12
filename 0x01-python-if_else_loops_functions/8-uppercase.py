#!/usr/bin/python3
def uppercase(str):
    for c in str:
        # Convert each character to uppercase using ASCII values and print it
        print(chr(ord(c) - 32) if 'a' <= c <= 'z' else c)


# Test case

uppercase("hello")
