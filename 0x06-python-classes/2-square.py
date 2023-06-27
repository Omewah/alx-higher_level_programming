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
