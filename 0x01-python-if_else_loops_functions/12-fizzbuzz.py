#!/usr/bin/python3

def fizzbuzz():
    """
    Print FizzBuzz game output for numbers from 1 to 100.
    For multiples of 3, print "Fizz".
    For multiples of 5, print "Buzz".
    For multiples of both 3 and 5, print "FizzBuzz".
    Otherwise, print the number itself.
    """
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz', end=' ')
        elif n % 3 == 0:
            print('Fizz', end=' ')
        elif n % 5 == 0:
            print('Buzz', end=' ')
        else:
            print(n, end=' ')

# Test the function


fizzbuzz()
