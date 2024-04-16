#!/usr/bin/python3
"""
function that returns the dictionary description
"""


def class_to_json(obj):
    """
        it returns Dictionary description suitable
        for JSON serialization
    """
    return obj.__dict__
