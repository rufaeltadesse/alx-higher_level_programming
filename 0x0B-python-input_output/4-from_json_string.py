#!/usr/bin/python3
"""Json to string"""
import json


def from_json_string(my_str):
    """JSON to string convert
    Args:
        my_str (str): json obj
    Returns:
        type: pyt obj.
    """
    return json.loads(my_str)
