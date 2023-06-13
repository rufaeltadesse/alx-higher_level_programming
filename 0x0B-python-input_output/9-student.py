#!/usr/bin/python3
"""Student class"""


class Student:
    """
    Student class
    Attributes:
        first_name: first name.
        last_name: last name.
        age: age.
    """
    def __init__(self, first_name, last_name, age):
        """New instance
        Args:
            first_name: first name.
            last_name: last name.
            age: age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """rep of student instance
        Returns:
            dict: dictionar rep.
        """
        return self.__dict__
