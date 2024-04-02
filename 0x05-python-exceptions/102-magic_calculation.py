#!/usr/bin/python3
def magic_calculation(a, b):
    """
    Perform a magic calculation.

    :param a: Integer
    :param b: Integer
    :return: Result of the magic calculation
    """
  result = 0
    for num in range(1, 3):
        try:
            if num > a:
                raise Exception('Too far')
            result += a ** b / num
        except Exception:
            result = b + a
            break
    return result
