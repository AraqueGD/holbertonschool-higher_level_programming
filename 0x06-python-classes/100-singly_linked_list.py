#!/usr/bin/python3
class Node:
    """ Class Node """

    def __init__(self, data, next_node=None):
        """ Initializate Class """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Getter Data """
        return (self.__data)

    @property
    def next_node(self):
        """ Getter next_node """
        return self.__next_node

    @data.setter
    def data(self, value):
        """ Setter Data """
        if (type(value) is not int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """ Setter Next_node """
        if (value is None or value is not Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """ Class Simgly LInked List """

    def __init__(self):
        """ Initializate Class """
        self.__head = None

    def sorted_insert(self, value):
        """ Function Sorted Insert """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
