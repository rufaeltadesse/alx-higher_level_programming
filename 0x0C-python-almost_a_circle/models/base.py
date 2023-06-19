#!/usr/bin/python3

"""Defining a class base"""
import csv
import json
import turtle


class Base:
    """Class definition
    Attributes:
        __nb_object (int): number of objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing a new base

        Args:
            id (int): new base id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns list

        Args:
            list_dictionaries (list): dictionaries list
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON serialization

        Args:
            list_objs (list): list of objects
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as myfile:
            if list_objs is None:
                myfile.write("[]")
            else:
                mylist = [o.to_dictionary() for o in list_objs]
                myfile.write(Base.to_json_string(mylist))

    @staticmethod
    def from_json_string(json_string):
        """Deserialization.

        Args:
            json_string (str): Json rep
        Returns: 
            string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Attribute dictionaries

        Args:
            **dictionary (dict): init dict
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """JSON string values loading

         Returns:
           List of instantiated cls
        """
        myfile = str(cls.__name__) + ".json"
        try:
            with open(myfile, "r") as jsonfile:
                mylist = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in mylist]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes to file

        Args:
            list_objs (list): inheritied obj
        """
        myfile = cls.__name__ + ".csv"
        with open(myfile, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads file from csv

        Returns:
            list of instantiated cls
        """
        myfile = cls.__name__ + ".csv"
        try:
            with open(myfile, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                mylist = csv.DictReader(csvfile, fieldnames=fieldnames)
                mylist = [dict([k, int(v)] for k, v in d.items())
                              for d in mylist]
                return [cls.create(**d) for d in mylist]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws rect

        Args:
            list_rectangles (list): rect obj
            list_squares (list): list square
        """
        newF = turtle.Turtle()
        newF.screen.bgcolor("#b7312c")
        newF.pensize(3)
        newF.shape("turtle")

        newF.color("#ffffff")
        for rect in list_rectangles:
            newF.showturtle()
            newF.up()
            newF.goto(rect.x, rect.y)
            newF.down()
            for i in range(2):
                newF.forward(rect.width)
                newF.left(90)
                newF.forward(rect.height)
                newF.left(90)
            newF.hideturtle()

        newF.color("#b5e3d8")
        for sq in list_squares:
            newF.showturtle()
            newF.up()
            newF.goto(sq.x, sq.y)
            newF.down()
            for i in range(2):
                newF.forward(sq.width)
                newF.left(90)
                newF.forward(sq.height)
                newF.left(90)
            newF.hideturtle()

        turtle.exitonclick()
