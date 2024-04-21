#!/usr/bin/python3
"""
Base class
"""


import csv
import turtle
import json


class Base:
    """
    Base class for managing unique IDs
    Attributes:
        __nb_objects (int): Private class attribute to keep track of objects.
        id (int): Public instance attribute representing the object's ID.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.
        params:
            id (int): The ID. If none, a unique ID will be generated
        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dicts.
        params:
            list_dictionaries (list): List of dictionaries.
        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list of objects to a file.
        params:
            list_objs (list): List of instances.
        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode='w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the deserialization of a JSON string
        params:
            json_string (str): JSON string representing a list of dictionaries.
        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return a class instantied from a dictionary of attribute
        params:
            **dictionary: Double pointer to a dictionary.
        Returns:
            instance: An instance with attributes set from dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Return a list of classes instantiated from a file of JSON strings.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV serialization of a list of objects to a file. 
        params:
            list_objs (list): List of objects to serialize.
        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            wr = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    wr.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    wr.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of classes instantiated from a CSV file.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                obj_list = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]),
                                  int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(int(row[1]), int(row[2]),
                                  int(row[3]), int(row[0]))

                    obj_list.append(obj)
                return obj_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''
        Draw Rectangles and Squares using the turtle graphics.
        params:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        '''
        screen = turtle.Screen()
        screen.title("Shapes Drawing")
        screen.setup(width=800, height=600)

        turt = turtle.Turtle()

        for rect in list_rectangles:
            turt.penup()
            turt.setpos(rect.x, rect.y)
            turt.pendown()
            turt.color("blue")
            for i in range(2):
                turt.forward(rect.width)
                turt.right(90)
                turt.forward(rect.height)
                turt.right(90)

        for square in list_squares:
            turt.penup()
            turt.setpos(square.x, square.y)
            turt.pendown()
            turt.color("green")
            for i in range(4):
                turt.forward(square.size)
                turt.right(90)

        turtle.done()
