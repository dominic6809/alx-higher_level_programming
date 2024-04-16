#!/usr/bin/python3
"""
function to define a class Student.
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        params:
            attrs (list): list of strings specifying which attributes to retrieve.
                If None, all attributes will be retrieved.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__

        json_dict = {}

        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)

        return json_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        based on a dictionary representation.

        params:
            json (dict): A dictionary containing attribute names and values.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
