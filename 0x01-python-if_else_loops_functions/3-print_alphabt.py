#!/usr/bin/python3
for i in range(97, 123):
    # skip printing 'e' and 'q'
    if (i != 101 and i != 113):
        # print the character
        print('{:c}'.format(i), end='')
