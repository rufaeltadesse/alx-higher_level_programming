#!/usr/bin/python3
"""Defining class checker"""


def is_same_class(obj, a_class):
    """Checking if obj is the same as a class

    Args:
        obj (any): obj to be checked
        a_class (type): class name
    Returns:
        result of comparision
    """
    if type(obj) == a_class:
        return True
    return False
