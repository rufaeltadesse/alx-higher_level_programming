#!/usr/bin/python3
"""Containing string fun"""
import json


def to_json_string(my_obj):
    """JSON representation.
    Args:
        my_obj (type): obj to be converted.
    Returns:
        str: JSON file.
    """
    return json.dumps(my_obj)
