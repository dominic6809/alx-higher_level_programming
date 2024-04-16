#!/usr/bin/python3
"""
function to define a class Student.
"""


class Student:
    """
    student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
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
s
        json_dict = {}

        for attr in attrs:
            if hasattr(self, attr):
                json_dict[attr] = getattr(self, attr)

        return json_dict
