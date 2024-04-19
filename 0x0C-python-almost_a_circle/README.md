# Almost a Circle Python Project

## Introduction
This project consists of building a series of classes for managing geometric shapes, starting with a base class called Base, and then creating two classes Rectangle and Square that inherit from the Base class.

## Base Class
The Base class is the base of all other classes in this project and is responsible for managing the id attribute in all future classes. It has the following features:

- Private class attribute `__nb_objects` to keep track of the number of instances created.
- Class constructor `__init__(self, id=None)`:
  - If id is not None, it assigns the public instance attribute id with the provided value.
  - If id is None, it increments `__nb_objects` and assigns the new value to the public instance attribute id.

### Example of the Base class:

```
from models.base import Base

# Creating instances and automatically assigning ids
b1 = Base()
print(b1.id)  # Output: 1

b2 = Base()
print(b2.id)  # Output: 2

# Creating an instance with a specific id
b3 = Base(10)
print(b3.id)  # Output: 10
```

## Rectangle Class
The Rectangle class inherits from the Base class and represents a rectangle shape. It has the following features:

- Private instance attributes __width, __height, __x, and __y, each with its own public getter and setter methods.
- Class constructor __init__(self, width, height, x=0, y=0, id=None):
- It calls the super class (Base) constructor with the provided id.
- It assigns each argument (width, height, x, and y) to the corresponding attribute.
  
### Additionally, the Rectangle class has the following methods:
- area(self): Returns the area value of the rectangle instance.
- display(self): Prints the rectangle instance using the character #. The x and y values determine the position of the rectangle.
- __str__(self): Overrides the __str__ method to return a string representation of the rectangle in the format [Rectangle] (<id>) <x>/<y> - <width>/<height>.

## Square Class

The Square class inherits from the Rectangle class and represents a square shape. Since a square is a special type of rectangle with equal width and height, the Square class reuses the attributes and methods from the Rectangle class.

The Square class has the following features:

- Class constructor __init__(self, size, x=0, y=0, id=None):
- It calls the super class (Rectangle) constructor with the provided id, x, y, size (which represents both width and height).
- Additionally, the Square class has a getter and setter method for the size attribute, which also updates the width and height attributes.

## Validation and Data Protection

Both the Rectangle and Square classes have validation methods to ensure that the attributes (width, height, x, y, size) are set correctly:

- -If the input is not an integer, it raises a TypeError with an appropriate error message.
- If the width or height is less than or equal to 0, it raises a ValueError with an appropriate error message.
- If the x or y is less than 0, it raises a ValueError with an appropriate error message.

## JSON Serialization and Deserialization

The classes also have methods to handle JSON serialization and deserialization:

- to_json_string(list_dictionaries): Serializes a list of dictionaries into a JSON string. If the input list is None or empty, it returns "[]".
- from_json_string(json_string): Deserializes a JSON string and returns a list of dictionaries. If the input JSON string is None or empty, it returns an empty list.
- save_to_file(cls, list_objs): Writes the JSON string representation of a list of objects (instances) to a file. The filename is based on the class name (e.g., "Rectangle.json" for Rectangle class).
- load_from_file(cls): Loads a list of instances from a JSON file and returns the list.

## Example usage:

```
from models.rectangle import Rectangle
from models.square import Square

# Creating instances
r1 = Rectangle(10, 5)
s1 = Square(7)

# Accessing and modifying attributes
r1.width = 20
s1.size = 9

# Calculating the area
print(r1.area())  # Output: 100
print(s1.area())  # Output: 81

# Displaying the shape
r1.display()  # Output: ##########
              # ##########
              # ##########
              # ##########
              # ##########
s1.display()  # Output: #######
              # #######
              # #######
              # #######
              # #######

# Printing a string representation of the shape
print(r1)  # Output: [Rectangle] (1) 0/0 - 20/5
print(s1)  # Output: [Square] (2) 0/0 - 9

# Serializing and deserializing to/from JSON
json_str = Rectangle.to_json_string([r1.to_dictionary(), s1.to_dictionary()])
print(json_str)  # Output: '[{"x": 0, "y": 0, "id": 1, "width": 20, "height": 5}, {"x": 0, "y": 0, "id": 2, "size": 9}]'
instances = Rectangle.load_from_file()
print(instances)  # Output: [<models.rectangle.Rectangle object at 0x7f5a86f94c70>, <models.square.Square object at 0x7f5a86f94b80>]
```
