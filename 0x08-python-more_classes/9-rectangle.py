#!/usr/bin/python3
"""Defines a recta class."""


class Rectangle:
    """Represent a recta.

    Attributes:
        number_of_instances (int): number of recta instances.
        print_symbol (any): symbol used for string repr.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new recta.

        Args:
            width (int): Width of the new recta.
            height (int): height of the new recta.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the recta."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the recta."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the recta."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the recta."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the recta with the greater area.

        Args:
            rect_1 (recta): The first recta.
            rect_2 (recta): The second recta.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a recta.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new recta with width and height equal to size.

        Args:
            size (int): The width and height of the new recta.
        """
        return (cls(size, size))

    def __str__(self):
        """Return the printable representation of the recta.

        Represents the recta with the # character.
        """
        if self.__height == 0 or self.__width == 0:
            return ("")

        recta = []
        for i in range(self.__height):
            [recta.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                recta.append("\n")
        return ("".join(recta))

    def __repr__(self):
        """Return the string representation of the recta."""
        recta = "Rectangle(" + str(self.__width)
        recta += ", " + str(self.__height) + ")"
        return (recta)

    def __del__(self):
        """Print a message for every deletion of a recta."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
