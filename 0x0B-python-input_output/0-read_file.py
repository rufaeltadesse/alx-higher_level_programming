#!/usr/bin/python3
"""File Reading"""


def read_file(filename=""):
    """ Reading file
    Args:
        filename: file name "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
