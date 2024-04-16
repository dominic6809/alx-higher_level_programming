#!/usr/bin/python3
"""
function to define a class Student.
"""


class Student:
    """
    Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
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
        my_list = self.__dict__
        stringdict_ = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return my_list

                if attr in my_list:
                    stringdict_[attr] = my_list[attr]

            return stringdict_

        return my_list

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        based on a dictionary representation.

        params:
            json (dict): A dictionary containing attribute names and values.

        Returns:
            None
        """
        for i in json:
            if i in self.__dict__.keys():
                self.__dict__[i] = json[i]
