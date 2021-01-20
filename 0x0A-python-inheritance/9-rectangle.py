#!/usr/bin/python3


"jdf jkfdjk jglk gjfklj kldf"


class BaseGeometry:
    """jkj fkljkdflj ldjflk """
    def area(self):
        raise Exception("area() is not implemented")
    """FJD KJKLFDJ KDFK KLDFJ KGDJFKLV"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """J KDJFJ KDFJK JDFLKVJ KLFDJ LK"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
    """ KDJKFJ KHSKJHD KJSHD HSJKHKJS"""
    def area(self):
        return self.__width * self.__height
    """l jfkdjk fdkjg kdj fsj vkdfj kv"""
    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
