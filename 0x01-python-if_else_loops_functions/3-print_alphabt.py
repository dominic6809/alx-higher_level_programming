#!/usr/bin/python3
# Iterate over ASCII values from 97 to 122 (lowercase letters range)
# and print each character without newline, except for 'q' and 'e'
for i in range(97, 123):
    if chr(i) not in ['q', 'e']:
        print(chr(i), end='')

# Output will be the lowercase ASCII alphabet excluding 'q' and 'e' printed without a newline
