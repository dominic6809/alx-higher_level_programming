#!/usr/bin/python3
"""
function to define a class Student.
"""


class Student:
    """
    Defines a student by first_name, last_name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.
        params:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves dictionary representation
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

        return stringdict_
