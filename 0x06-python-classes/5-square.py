#!/usr/bin/python3

"""the class square to be defined."""


class Square:
    """the code to represent a square."""

    def __init__(self, size=0):
        """initialize the square.
        Args:
            size (int): the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """prints the area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints a square with the special char #"""
        for i in range(0, self.__size):
            [print('#', end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
