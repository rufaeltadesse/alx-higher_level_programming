#!/usr/bin/python3
"""Square print based on size"""


def print_square(size):
    """printing a square with size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for b in range(size):
        [print("#", end="") for b in range(size)]
        print("")
