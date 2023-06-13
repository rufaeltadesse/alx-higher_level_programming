#!/usr/bin/python3
"""class to json function"""


def class_to_json(obj):
    """Class to json
    Args:
        obj (MyClass): object.
    Returns:
        dict: dictionary.
    """
    return obj.__dict__
