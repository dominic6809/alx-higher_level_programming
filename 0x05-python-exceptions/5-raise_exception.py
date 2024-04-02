#!/usr/bin/python3

def raise_exception():
    """
    Raises a type exception.

    """
    try:
        '{}'.format(42)
    except TypeError as e:
        raise e
    finally:
        pass
