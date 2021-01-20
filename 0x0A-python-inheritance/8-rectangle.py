#!/usr/bin/python3

"jfkldjgkljkgf gfdgdf"


class BaseGeometry:
    """gjfkgjdlkjlg dfjglk;dj glkdfjg"""
    def area(self):
        raise Exception("area() is not implemented")
    """fjdkgjlkdfjkl dklfgjkldfj kgjdfkg jkldfgjdf"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """rjgkjd kljgkjfkd jgkdfj kgjdkfl jgkdfj"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
