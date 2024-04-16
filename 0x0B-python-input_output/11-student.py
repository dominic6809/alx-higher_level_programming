#!/usr/bin/python3
"""
function to define a class Student.
"""


class Student:
    """
    Represent a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        params:
            attrs (list, optional): List of attribute names to retrieve.
                                    Defaults to None.
        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        params:
            json (dict): Dictionary containing attribute-value pairs.
        """
        for key, value in json.items():
            setattr(self, key, value)
