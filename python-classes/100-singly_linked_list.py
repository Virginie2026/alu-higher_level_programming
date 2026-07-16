#!/usr/bin/python3
"""Module that defines a singly linked list and its nodes."""


class Node:
    """Represent a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): the data value held by the node.
            next_node (Node): reference to the next node (default None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data value of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value of the node.

        Args:
            value (int): the new data value.

        Raises:
            TypeError: if value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list.

        Args:
            value (Node): the next node, or None.

        Raises:
            TypeError: if value is neither None nor a Node instance.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly linked list of Node objects."""

    def __init__(self):
        """Initialize a new, empty SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the list, keeping it sorted (increasing).

        Args:
            value (int): the data value to insert.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return the string representation of the list, one node per line."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
