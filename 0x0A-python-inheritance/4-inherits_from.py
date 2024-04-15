#!/usr/bin/python3
"""
Defining an inherited class-checking function.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class.

    params:
    obj: The object to check.
    a_class: The class to check against.

    Returns:
    True if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class; otherwise False.
    """
  if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
