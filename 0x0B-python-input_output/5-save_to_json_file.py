#!/usr/bin/python3
"""Saving to json file"""
import json


def save_to_json_file(my_obj, filename):
    """Json file write up
    Args:
        my_obj (type): Obj to text file
        filename (str): name of file
    Returns:
        type: JSON representation.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        # serializing json
        json_object = json.dumps(my_obj)
        # or json.dump(my_obj, f)
        f.write(json_object)
        f.close()
