#!/usr/bin/python3
"""
Locked class module
"""


class LockedClass:
    """
    Class that prevents dynamic creation of new instance attributes,
    except for 'first_name'.

    Attribute:
        __slots__ (list): List of allowed instance attributes.
    """
    __slots__ = ['first_name']
