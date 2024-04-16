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
        """
        for i in json:
            if i in self.__dict__.keys():
                self.__dict__[i] = json[i]
