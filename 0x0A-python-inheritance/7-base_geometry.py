#!/usr/bin/python3


"gkdfgj jdf jgkdf gd"


class BaseGeometry:
    """gfkdlk lgkfdg dfg d"""
    def area(self):
        raise Exception("area() is not implemented")

    """jfkfdjkl djglkdfjlk jdklgd"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{:s} must be greater than 0".format(name))
