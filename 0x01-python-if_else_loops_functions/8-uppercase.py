#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Convert each character to uppercase using ASCII values and print it
        print(chr(ord(char) - 32) if 'a' <= char <= 'z' else char)
