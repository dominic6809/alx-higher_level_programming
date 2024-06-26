#!/usr/bin/python3
"""Class module for singly linked list"""


class Node:
    """
    Define a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """Initializes a node.

        params:
            data: Data of the new node.
            next_node (Node): Reference to the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets the data of the node.

        params:
            value: Data value to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the reference to the next node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets the reference to the next node.

        params:
            value (Node): Reference to the next node.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly linked list class."""

    def __init__(self):
        """
        Initializes a singly linked list with head node = None.
        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position
        in the list

        params:
            value: Data value of the new node to be inserted.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            num = self.__head
            while (num.next_node is not None and
                    num.next_node.data < value):
                num = num.next_node
            new_node.next_node = num.next_node
            num.next_node = new_node

    def __str__(self):
        """String representation of the entire linked list.

        Returns:
            str: String representation of the linked list.
        """
        values = []
        num = self.__head
        while num is not None:
            values.append(str(num.data))
            num = num.next_node
        return ('\n'.join(values))
