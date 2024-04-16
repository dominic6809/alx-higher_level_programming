#!/usr/bin/python3
"""
function to Define a class Student.
"""


class Student:
    """
    student class

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student with first name, last name, and age.

        params:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        json_dict = {}

        json_dict["first_name"] = self.first_name
        json_dict["last_name"] = self.last_name
        json_dict["age"] = self.age

        return json_dict
